"""Govern author-owned color roles without altering mathematical figures."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SVG = ROOT / "figures/generated/MSR-FIG-0001_sphere-geodesic.svg"
TOKENS = ROOT / "art/design_tokens.json"
SOURCE = ROOT / "scripts/generate_reference_figure.py"


class ScientificColorGovernanceTests(unittest.TestCase):
    def test_viability_is_registered_semantic_green_not_amber(self) -> None:
        data = json.loads(TOKENS.read_text(encoding="utf-8"))
        self.assertEqual(data["chains"]["C05"]["color"], "#176B42")
        self.assertEqual(data["chains"]["C05"]["label"], "Viability-resilience")
        self.assertEqual(len(data["chains"]), 10)

    def test_generated_geometry_preserves_white_background_and_collinearity_contract(self) -> None:
        root = ElementTree.parse(SVG).getroot()
        ns = "{http://www.w3.org/2000/svg}"
        self.assertEqual(root.attrib["data-figure-id"], "MSR-FIG-0001")
        circles = root.findall(".//" + ns + "circle")
        self.assertTrue(circles)
        self.assertTrue(any(c.attrib.get("fill") == "#FFFFFF" and c.attrib.get("stroke") == "#17202A" for c in circles))
        for rect in root.findall(".//" + ns + "rect"):
            self.assertEqual(rect.attrib.get("fill"), "#FFFFFF")

    def test_no_forbidden_amber_or_gradient_in_generator_and_figure(self) -> None:
        for path in (SVG, SOURCE):
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8").lower()
                for token in ("#e69f00", "#d55e00", "radialgradient", "lineargradient"):
                    self.assertNotIn(token, text)
                self.assertIn("#006d70", text)


if __name__ == "__main__":
    unittest.main()
