from __future__ import annotations

from dataclasses import dataclass

from .sphere import (
    build_sphere_visual_ir,
    fibonacci_sphere,
    tangent_vectors,
    validate_scene,
)
from .spline_adapter import SplineAdapter


@dataclass(frozen=True)
class ReleaseGateReport:
    math: bool
    constraint: bool
    determinism: bool
    editability: bool
    roundtrip: bool
    safety: bool

    @property
    def passed(self) -> bool:
        return all(
            (
                self.math,
                self.constraint,
                self.determinism,
                self.editability,
                self.roundtrip,
                self.safety,
            )
        )

    @property
    def passed_count(self) -> int:
        return sum(
            (
                self.math,
                self.constraint,
                self.determinism,
                self.editability,
                self.roundtrip,
                self.safety,
            )
        )


def evaluate_release_gates(count: int = 12, delta: float = 0.3) -> ReleaseGateReport:
    points = fibonacci_sphere(count)
    vectors = tangent_vectors(points)
    checks = validate_scene(points, vectors, delta)

    first = build_sphere_visual_ir(count=count, delta=delta)
    second = build_sphere_visual_ir(count=count, delta=delta)
    determinism = first == second

    adapter = SplineAdapter()
    scene = adapter.export_scene(first)
    identity_before = adapter.import_identity_map(scene)
    math_before = adapter.mathematical_snapshot(scene)

    adapter.apply_style_edit(scene, "sphere:surface", material="release-gate-test")
    surface = next(obj for obj in scene["objects"] if obj["visual_id"] == "sphere:surface")
    editability = surface["style"].get("material") == "release-gate-test"
    roundtrip = adapter.import_identity_map(
        scene
    ) == identity_before and adapter.validate_roundtrip(first, scene)
    safety = adapter.mathematical_snapshot(scene) == math_before

    return ReleaseGateReport(
        math=checks["unit_sphere"] and checks["tangent"],
        constraint=checks["separation"],
        determinism=determinism,
        editability=editability,
        roundtrip=roundtrip,
        safety=safety,
    )
