"""Loading and boundary checks for mathematical model contracts."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_MODEL_ID = re.compile(r"^MSR-MOD-[0-9]{4}$")


@dataclass(frozen=True, slots=True)
class ModelContract:
    """Selected immutable fields from a validated model-contract record."""

    model_id: str
    version: str
    title: str
    status: str
    application_decision: str
    module: str
    citation_keys: tuple[str, ...]
    raw: dict[str, Any]


def load_model_contract(path: str | Path) -> ModelContract:
    """Load a contract and enforce the platform's non-negotiable core boundary.

    Full JSON-Schema validation is performed by ``scripts/verify.py``. This loader
    intentionally repeats the model identity and application-state checks so that
    runtime code cannot bypass them.
    """
    contract_path = Path(path)
    data: dict[str, Any] = json.loads(contract_path.read_text(encoding="utf-8"))

    model_id = str(data.get("model_id", ""))
    if not _MODEL_ID.fullmatch(model_id):
        raise ValueError("invalid or missing model_id")
    if data.get("application_decision") != "NOT_SELECTED":
        raise ValueError("foundation contracts must preserve application_decision=NOT_SELECTED")

    implementation = data.get("implementation")
    evidence = data.get("evidence")
    if not isinstance(implementation, dict) or not isinstance(evidence, dict):
        raise ValueError("contract implementation and evidence objects are required")

    citation_keys = evidence.get("citation_keys")
    if not isinstance(citation_keys, list) or not citation_keys:
        raise ValueError("contract requires at least one scholarly citation key")

    return ModelContract(
        model_id=model_id,
        version=str(data.get("version", "")),
        title=str(data.get("title", "")),
        status=str(data.get("status", "")),
        application_decision=str(data["application_decision"]),
        module=str(implementation.get("module", "")),
        citation_keys=tuple(str(key) for key in citation_keys),
        raw=data,
    )
