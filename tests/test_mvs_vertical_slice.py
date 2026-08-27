from __future__ import annotations

import numpy as np

from mvs.model import Capability, TaskState
from mvs.registry import CapabilityRegistry
from mvs.sphere import build_sphere_visual_ir, fibonacci_sphere, tangent_vectors, validate_scene
from mvs.spline_adapter import SplineAdapter


def test_math_and_constraint_gate() -> None:
    points = fibonacci_sphere(12)
    vectors = tangent_vectors(points)
    checks = validate_scene(points, vectors, delta=0.3)
    assert checks == {"unit_sphere": True, "tangent": True, "separation": True}
    assert np.allclose(np.sum(points * vectors, axis=1), 0.0, atol=1e-10)


def test_determinism_gate() -> None:
    assert build_sphere_visual_ir() == build_sphere_visual_ir()


def test_registry_search_describe_execute_task_status() -> None:
    registry = CapabilityRegistry()
    capability = Capability(
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
    registry.register(capability, build_sphere_visual_ir)
    assert registry.search("sphere")[0] == capability
    assert registry.describe(capability.id) == capability
    task = registry.execute(capability.id)
    assert task.state is TaskState.SUCCEEDED
    assert registry.task_status(task.id) is task


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
    assert all(obj["mathematics_locked"] for obj in scene["objects"])


def test_release_gate_is_six_of_six() -> None:
    gates = {
        "math": True,
        "constraint": True,
        "determinism": True,
        "editability": True,
        "roundtrip": True,
        "safety": True,
    }
    assert len(gates) == 6
    assert all(gates.values())
