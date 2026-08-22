"""Audit bibliography keys and machine-readable citation crosswalks."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def bibliography_keys() -> tuple[set[str], list[str]]:
    keys: set[str] = set()
    duplicates: list[str] = []
    for path in sorted((ROOT / "literature_review").rglob("*.bib")):
        for key in re.findall(r"^@[A-Za-z]+\{([^,]+),", path.read_text(encoding="utf-8"), re.M):
            if key in keys:
                duplicates.append(key)
            keys.add(key)
    return keys, duplicates


def requested_keys() -> set[str]:
    requested: set[str] = set()
    for path in sorted((ROOT / "mathematics/model_contracts").glob("*.json")):
        value: Any = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"{path} must contain an object")
        evidence = value.get("evidence")
        if isinstance(evidence, dict):
            keys = evidence.get("citation_keys", [])
            if isinstance(keys, list):
                requested.update(str(key) for key in keys)

    citation_pattern = re.compile(r"(?<![A-Za-z0-9_])@([A-Za-z0-9_:\-.]+)")
    for suffix in ("*.qmd", "*.md"):
        for path in ROOT.rglob(suffix):
            if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
                continue
            requested.update(citation_pattern.findall(path.read_text(encoding="utf-8")))
    return requested


def main() -> int:
    available, duplicates = bibliography_keys()
    requested = requested_keys()
    missing = sorted(requested - available)

    if missing:
        print(f"Missing bibliography keys: {missing}", file=sys.stderr)
        return 1
    if duplicates:
        print(f"Duplicate bibliography keys across files: {sorted(set(duplicates))}")
        print("Duplicate keys are reported for review but are not automatically merged.")
    print(f"PASS: {len(requested)} referenced keys resolved across {len(available)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
