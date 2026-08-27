from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import numpy as np
import pytest
from jsonschema import Draft202012Validator

from mvs.model import Capability, TaskState
from mvs.registry import CapabilityRegistry
from mvs.release_gate import evaluate_release_gates
from mvs.sphere import (
    build_sphere_visual_ir,
    fibonacci_sphere,
    tangent_vectors,
    validate_scene,
)
from mvs.spline_adapter import SplineAdapter


def test_math_and_constraint_gate() -> None:
    points = fibonacci_sphere(12)
    vectors = tangent_vectors(points)
    checks = validate_scene(points, vectors, delta=0.3)
    assert checks == {"unit_sphere": True, "tangent": True, "separation": True}
    assert np.allclose(np.linalg.norm(points, axis=1), 1.0, atol=1e-10)
    assert np.allclose(np.sum(points * vectors, axis=1), 0.0, atol=1e-10)


def test_invalid_scene_is_rejected() -> None:
    with pytest.raises(ValueError, match="mathematical validation failed"):
        build_sphere_visual_ir(count=12, delta=0.7)


def test_visual_ir_matches_canonical_json_schema() -> None:
    schema_path = Path("schemas/mvs-visual-ir.schema.json")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(build_sphere_visual_ir().to_dict())


def test_visual_ir_mathematics_is_deeply_immutable() -> None:
    visual_ir = build_sphere_visual_ir()
    with pytest.raises(TypeError):
        visual_ir.objects[0].geometry["radius"] = 2.0  # type: ignore[index]


def test_determinism_gate() -> None:
    assert build_sphere_visual_ir() == build_sphere_visual_ir()


def _sphere_capability() -> Capability:
    return Capability(
        id="mvs.sphere.build",
        domain="differential_geometry",
        deterministic=True,
        read_only=True,
        destructive=False,
        long_running=False,
        requires_gpu=False,
        produces_visual=True,
        mathematical_validation_required=True,
    )


def test_registry_search_describe_execute_task_status() -> None:
    registry = CapabilityRegistry()
    capability = _sphere_capability()
    registry.register(capability, build_sphere_visual_ir)

    assert registry.search("sphere") == (capability,)
    assert registry.describe(capability.id) == capability

    task = registry.execute(capability.id)
    assert task.state is TaskState.SUCCEEDED
    assert task.result == build_sphere_visual_ir()
    assert task.error is None
    assert registry.task_status(task.id) is task


def test_registry_rejects_duplicate_and_unknown_ids() -> None:
    registry = CapabilityRegistry()
    capability = _sphere_capability()
    registry.register(capability, build_sphere_visual_ir)

    with pytest.raises(ValueError, match="already registered"):
        registry.register(capability, build_sphere_visual_ir)
    with pytest.raises(KeyError, match="unknown capability"):
        registry.describe("missing")
    with pytest.raises(KeyError, match="unknown capability"):
        registry.execute("missing")
    with pytest.raises(KeyError, match="unknown task"):
        registry.task_status("missing")


def test_editability_roundtrip_and_safety_gates() -> None:
    visual_ir = build_sphere_visual_ir()
    adapter = SplineAdapter()
    scene = adapter.export_scene(visual_ir)
    identity_before = adapter.import_identity_map(scene)
    math_before = adapter.mathematical_snapshot(scene)

    adapter.apply_style_edit(scene, "sphere:surface", material="gold", roughness=0.2)

    assert scene["objects"][0]["style"]["material"] == "gold"
    assert adapter.import_identity_map(scene) == identity_before
    assert adapter.mathematical_snapshot(scene) == math_before
    assert adapter.validate_roundtrip(visual_ir, scene)
    assert all(obj["mathematics_locked"] for obj in scene["objects"])


def test_renderer_geometry_tampering_is_detected() -> None:
    visual_ir = build_sphere_visual_ir()
    adapter = SplineAdapter()
    scene = adapter.export_scene(visual_ir)
    tampered = deepcopy(scene)
    tampered["objects"][0]["geometry"]["radius"] = 2.0

    assert not adapter.validate_roundtrip(visual_ir, tampered)
    assert visual_ir.objects[0].geometry["radius"] == 1.0


def test_release_gate_is_computed_six_of_six() -> None:
    report = evaluate_release_gates()

    assert report.passed_count == 6
    assert report.passed


def test_release_gate_rejects_failed_constraint() -> None:
    with pytest.raises(ValueError, match="mathematical validation failed"):
        evaluate_release_gates(delta=0.7)
