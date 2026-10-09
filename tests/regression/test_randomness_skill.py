"""Static scientific-boundary and discoverability checks for MSR-SKILL-SR-001."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "shader-randomness-scientific-visuals"
ART = ROOT / "art" / "shaders" / "randomness_lab"


class RandomnessSkillGovernanceTests(unittest.TestCase):
    def test_skill_declares_all_seven_labs_and_research_scope(self) -> None:
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        lessons = (SKILL / "references" / "CHAPTER_10_LESSONS.md").read_text(
            encoding="utf-8"
        )
        adaptation = (SKILL / "references" / "TASK_ADAPTATION.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("name: shader-randomness-scientific-visuals", skill)
        for lesson in range(1, 8):
            self.assertIn(f"L{lesson} ", lessons)
        for category in ("Animation", "Diagram", "Mind map", "Chart", "Mathematical figure"):
            self.assertIn(f"## {category}", adaptation)
        self.assertIn("NOT_SELECTED", skill)
        self.assertIn("not", lessons.lower())

    def test_fallback_and_provenance_have_clear_nonempirical_semantics(self) -> None:
        svg = ElementTree.parse(ART / "static.svg").getroot()
        ns = "{http://www.w3.org/2000/svg}"
        self.assertEqual(svg.attrib.get("data-figure-id"), "MSR-FIG-0003")
        self.assertIsNotNone(svg.find(ns + "title"))
        self.assertIsNotNone(svg.find(ns + "desc"))
        provenance = json.loads((ART / "provenance.json").read_text(encoding="utf-8"))
        self.assertEqual(provenance["figure_id"], "MSR-FIG-0003")
        self.assertEqual(provenance["application_decision"], "NOT_SELECTED")
        self.assertEqual(provenance["status"], "PROPOSED_FOR_REVIEW")
        self.assertEqual(provenance["communication_impact"], "NOT_EVALUATED")

    def test_new_visual_source_has_no_gold_or_filled_background(self) -> None:
        source_paths = (
            ART / "index.html",
            ART / "static.svg",
            SKILL / "SKILL.md",
        )
        for path in source_paths:
            with self.subTest(path=path.name):
                source = path.read_text(encoding="utf-8").lower()
                self.assertNotIn("#e69f00", source)
                self.assertNotIn("linear-gradient", source)


if __name__ == "__main__":
    unittest.main()
