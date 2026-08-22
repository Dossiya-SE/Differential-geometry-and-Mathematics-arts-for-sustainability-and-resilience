"""Regression tests for the foundation's model and selection boundaries."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from msr.core.contracts import load_model_contract

ROOT = Path(__file__).resolve().parents[2]


class RepositoryContractTests(unittest.TestCase):
    def test_reference_contract_loads_and_is_domain_neutral(self) -> None:
        contract = load_model_contract(ROOT / "mathematics/model_contracts/MSR-MOD-0001.json")
        self.assertEqual(contract.model_id, "MSR-MOD-0001")
        self.assertEqual(contract.application_decision, "NOT_SELECTED")
        self.assertEqual(contract.module, "msr.geometry.sphere")

    def test_experiment_uses_reference_model_and_no_application(self) -> None:
        path = ROOT / "experiments/registry/MSR-EXP-0001.json"
        record = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(record["model_id"], "MSR-MOD-0001")
        self.assertEqual(record["application_decision"], "NOT_SELECTED")
        self.assertEqual(record["verification"]["independent_review"], "NOT_COMPLETED")

    def test_package_and_citation_versions_agree(self) -> None:
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        version_module = (ROOT / "src/msr/_version.py").read_text(encoding="utf-8")
        self.assertIn('version: "0.4.0"', citation)
        self.assertIn('__version__ = "0.4.0"', version_module)


if __name__ == "__main__":
    unittest.main()
