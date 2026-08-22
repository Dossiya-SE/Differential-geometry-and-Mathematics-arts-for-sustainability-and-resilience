"""Controlled evidence states and claim-level traceability rules."""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import StrEnum

_CLAIM_ID = re.compile(r"^MSR-CLM-[0-9]{4}$")


class EvidenceStatus(StrEnum):
    """Permitted epistemic states for a bounded research claim."""

    OBSERVED = "OBSERVED"
    OBSERVED_PARTIAL = "OBSERVED_PARTIAL"
    INFERRED = "INFERRED"
    PROPOSED = "PROPOSED"
    VALIDATED = "VALIDATED"
    REJECTED = "REJECTED"
    NOT_OBSERVED = "NOT_OBSERVED"
    NOT_VERIFIED = "NOT_VERIFIED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


_SOURCE_DEPENDENT = {
    EvidenceStatus.OBSERVED,
    EvidenceStatus.OBSERVED_PARTIAL,
    EvidenceStatus.INFERRED,
    EvidenceStatus.VALIDATED,
    EvidenceStatus.REJECTED,
}


@dataclass(frozen=True, slots=True)
class ClaimRecord:
    """A minimal immutable record connecting one claim to evidence and limitations.

    Audit identifiers are optional secondary links. They never satisfy the citation
    requirement for source-dependent scholarly claims.
    """

    claim_id: str
    text: str
    status: EvidenceStatus
    citation_keys: tuple[str, ...] = ()
    audit_ids: tuple[str, ...] = ()
    rationale: str = ""
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        """Reject untraceable or semantically incomplete claim records."""
        if not _CLAIM_ID.fullmatch(self.claim_id):
            raise ValueError("claim_id must match MSR-CLM-NNNN")
        if not self.text.strip():
            raise ValueError("claim text must not be empty")
        if self.status in _SOURCE_DEPENDENT and not self.citation_keys:
            raise ValueError(f"{self.status} claims require at least one citation key")
        if self.status is EvidenceStatus.NOT_APPLICABLE and not self.rationale.strip():
            raise ValueError("NOT_APPLICABLE requires a written rationale")
        if self.status is EvidenceStatus.OBSERVED_PARTIAL and not self.limitations:
            raise ValueError("OBSERVED_PARTIAL requires an explicit coverage limitation")
