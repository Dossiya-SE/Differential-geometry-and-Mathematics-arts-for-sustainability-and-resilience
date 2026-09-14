"""Regression and reproducibility tests for the JSON-driven tensor geometry visual."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "art/tensor-geometry/tensor_geometry.json"
SCHEMA = ROOT / "schemas/tensor-geometry.schema.json"
SVG = ROOT / "figures/generated/MSR-FIG-0002_tensor-geometry.svg"
PROVENANCE = ROOT / "figures/generated/MSR-FIG-0002.provenance.json"


def load_spec() -> dict[str, Any]:
    value: Any = json.loads(SPEC.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_spec_validates_against_schema() -> None:
    spec = load_spec()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = sorted(
        Draft202012Validator(schema).iter_errors(spec),
        key=lambda error: list(error.path),
    )
    assert errors == []


def test_base_coupling_shape_matches_system_axis() -> None:
    spec = load_spec()
    systems = spec["systems"]
    base = spec["coupling_tensor"]["base_coupling"]
    assert len(base) == len(systems)
    assert all(len(row) == len(systems) for row in base)


def test_metric_tensors_are_symmetric_positive_definite() -> None:
    spec = load_spec()
    matrices = [sample["g"] for sample in spec["state_space"]["metric_samples"]]
    matrices.append(spec["viability"]["metric"])
    for matrix in matrices:
        a, b = matrix[0]
        c, d = matrix[1]
        assert b == c
        assert a > 0
        assert a * d - b * c > 0


def test_svg_is_native_animated_and_provenanced() -> None:
    svg = SVG.read_text(encoding="utf-8")
    assert 'data-figure-id="MSR-FIG-0002"' in svg
    assert "data-source-sha256=" in svg
    assert "<title" in svg and "<desc" in svg
    assert "<animate" in svg
    assert "<image" not in svg
    assert "data:image/" not in svg


def test_provenance_preserves_evidence_boundary() -> None:
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    assert provenance["evidence_status"] == "ILLUSTRATIVE_SYNTHETIC"
    assert provenance["empirical_status"] == "NOT_EMPIRICALLY_CALIBRATED"
    assert provenance["communication_impact"] == "NOT_EVALUATED"
    assert provenance["derived_quantities"]["boundary_samples"] >= 180


def test_renderer_outputs_are_current() -> None:
    subprocess.run(
        [sys.executable, "scripts/render_tensor_geometry.py", "--check"],
        cwd=ROOT,
        check=True,
    )
