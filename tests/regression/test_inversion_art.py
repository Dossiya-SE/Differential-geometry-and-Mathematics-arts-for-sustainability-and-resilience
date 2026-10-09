"""Accessibility, provenance and deterministic-output checks for MSR-FIG-0002."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "art" / "shaders" / "inversion_lab"


class InversionArtTests(unittest.TestCase):
    def test_static_svg_is_exactly_regenerable(self) -> None:
        subprocess.run(
            [sys.executable, "scripts/generate_inversion_static.py", "--check"],
            check=True,
            cwd=ROOT,
        )

    def test_static_has_text_alternatives_and_model_link(self) -> None:
        svg = ElementTree.parse(ART / "static.svg").getroot()
        self.assertEqual(svg.attrib.get("data-figure-id"), "MSR-FIG-0002")
        self.assertTrue(svg.find("{http://www.w3.org/2000/svg}title") is not None)
        self.assertTrue(svg.find("{http://www.w3.org/2000/svg}desc") is not None)
        metadata = json.loads((ART / "provenance.json").read_text(encoding="utf-8"))
        self.assertEqual(metadata["model_id"], "MSR-MOD-0002")
        self.assertEqual(metadata["communication_impact"], "NOT_EVALUATED")
        self.assertEqual(metadata["application_decision"], "NOT_SELECTED")


if __name__ == "__main__":
    unittest.main()
