"""Semantic and accessibility controls for the five-family scientific suite."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SUITE = ROOT / "art" / "visual_suite"
SVG_NAMESPACE = "{http://www.w3.org/2000/svg}"


class VisualSuiteTests(unittest.TestCase):
    def test_registry_is_unique_complete_and_domain_neutral(self) -> None:
        record = json.loads((SUITE / "registry.json").read_text(encoding="utf-8"))
        self.assertEqual(record["application_decision"], "NOT_SELECTED")
        figures = record["visuals"]
        self.assertEqual(len(figures), 5)
        self.assertEqual(
            {item["family"] for item in figures},
            {"ANIMATION", "DIAGRAM", "MIND_MAP", "CHART", "MATHEMATICAL_FIGURE"},
        )
        self.assertEqual(
            [item["id"] for item in figures],
            [f"MSR-FIG-{number:04d}" for number in range(4, 9)],
        )
        for item in figures:
            with self.subTest(figure=item["id"]):
                self.assertEqual(item["status"], "PROPOSED_FOR_REVIEW")
                self.assertEqual(item["application_decision"], "NOT_SELECTED")
                self.assertEqual(item["communication_impact"], "NOT_EVALUATED")
                self.assertEqual(item["empirical_validation"], "NOT_APPLICABLE")

    def test_figure_sources_have_accessible_svg_and_white_canvas(self) -> None:
        record = json.loads((SUITE / "registry.json").read_text(encoding="utf-8"))
        for item in record["visuals"]:
            path = ROOT / item["path"]
            with self.subTest(figure=item["id"]):
                root = ElementTree.parse(path).getroot()
                self.assertEqual(root.attrib.get("data-figure-id"), item["id"])
                self.assertIsNotNone(root.find(SVG_NAMESPACE + "title"))
                self.assertIsNotNone(root.find(SVG_NAMESPACE + "desc"))
                rectangles = root.findall(SVG_NAMESPACE + "rect")
                self.assertTrue(rectangles)
                self.assertEqual(rectangles[0].attrib.get("fill"), "#FFFFFF")
                source = path.read_text(encoding="utf-8").lower()
                for forbidden in ("#e69f00", "lineargradient", "radialgradient"):
                    self.assertNotIn(forbidden, source)
                self.assertNotIn("fill=\"#87cefa\"", source)

    def test_cross_artifact_equations_and_conventions_are_declared(self) -> None:
        standard = (ROOT / "docs/VISUAL_SYSTEM_V1.md").read_text(encoding="utf-8")
        skill = (
            ROOT / "skills/scientific-visual-system/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Viab(K)=K", standard)
        self.assertIn("NOT_SELECTED", standard)
        self.assertIn("Mind map", skill)
        self.assertIn("Chart", skill)
        self.assertIn("Mathematical figure", skill)


if __name__ == "__main__":
    unittest.main()
