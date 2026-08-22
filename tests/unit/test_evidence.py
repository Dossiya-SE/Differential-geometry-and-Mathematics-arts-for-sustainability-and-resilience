"""Tests for controlled claim-level evidence records."""

from __future__ import annotations

import unittest

from msr.core.evidence import ClaimRecord, EvidenceStatus


class ClaimRecordTests(unittest.TestCase):
    def test_observed_claim_requires_citation(self) -> None:
        with self.assertRaisesRegex(ValueError, "citation"):
            ClaimRecord(
                claim_id="MSR-CLM-0001",
                text="A checked scholarly claim.",
                status=EvidenceStatus.OBSERVED,
            )

    def test_audit_identifier_does_not_replace_citation(self) -> None:
        with self.assertRaisesRegex(ValueError, "citation"):
            ClaimRecord(
                claim_id="MSR-CLM-0002",
                text="A checked scholarly claim.",
                status=EvidenceStatus.OBSERVED,
                audit_ids=("A010",),
            )

    def test_partial_observation_requires_limitation(self) -> None:
        with self.assertRaisesRegex(ValueError, "coverage limitation"):
            ClaimRecord(
                claim_id="MSR-CLM-0003",
                text="Only part of the construct was observed.",
                status=EvidenceStatus.OBSERVED_PARTIAL,
                citation_keys=("source2026",),
            )

    def test_not_applicable_requires_rationale(self) -> None:
        with self.assertRaisesRegex(ValueError, "rationale"):
            ClaimRecord(
                claim_id="MSR-CLM-0004",
                text="This chain is outside the bounded source.",
                status=EvidenceStatus.NOT_APPLICABLE,
            )

    def test_proposal_can_be_created_without_source_citation(self) -> None:
        claim = ClaimRecord(
            claim_id="MSR-CLM-0005",
            text="Evaluate this transfer in a future experiment.",
            status=EvidenceStatus.PROPOSED,
            limitations=("Not yet tested.",),
        )
        self.assertEqual(claim.status, EvidenceStatus.PROPOSED)


if __name__ == "__main__":
    unittest.main()
