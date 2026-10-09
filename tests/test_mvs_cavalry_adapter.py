from __future__ import annotations

from copy import deepcopy

from mvs.cavalry_adapter import CavalryAdapter
from mvs.sphere import build_sphere_visual_ir


def test_cavalry_scene_is_deterministic_and_preserves_identity() -> None:
    visual_ir = build_sphere_visual_ir()
    adapter = CavalryAdapter()
    first = adapter.export_scene(visual_ir)
    second = adapter.export_scene(visual_ir)

    assert first == second
    assert adapter.identity_map(first) == adapter.identity_map(second)
    assert first["format"] == "mvs-cavalry-v1"


def test_presentation_edit_cannot_change_mathematical_snapshot() -> None:
    visual_ir = build_sphere_visual_ir()
    adapter = CavalryAdapter()
    scene = adapter.export_scene(visual_ir)
    before = adapter.mathematical_snapshot(scene)

    adapter.apply_presentation_edit(scene, "sphere:surface", fill="gold", opacity=0.8)

    assert adapter.mathematical_snapshot(scene) == before
    assert adapter.validate_roundtrip(visual_ir, scene)


def test_geometry_tampering_fails_roundtrip() -> None:
    visual_ir = build_sphere_visual_ir()
    adapter = CavalryAdapter()
    scene = deepcopy(adapter.export_scene(visual_ir))
    scene["objects"][0]["geometry"]["radius"] = 3.0

    assert not adapter.validate_roundtrip(visual_ir, scene)


def test_svg_is_deterministic_and_carries_semantic_contract() -> None:
    visual_ir = build_sphere_visual_ir()
    adapter = CavalryAdapter()
    first = adapter.export_svg(visual_ir)
    second = adapter.export_svg(visual_ir)

    assert first == second
    assert 'data-scene-id="mvs:s2:benchmark"' in first
    assert 'data-semantic-id=' in first
    assert 'data-mathematics-locked="true"' in first
    assert '<metadata>' in first
