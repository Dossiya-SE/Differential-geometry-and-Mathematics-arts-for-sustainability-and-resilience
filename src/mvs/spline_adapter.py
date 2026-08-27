from __future__ import annotations

from copy import deepcopy
from typing import Any

from .model import VisualIR


class SplineAdapter:
    """Pure translation boundary: Visual IR is authoritative; renderer state is not."""

    def export_scene(self, visual_ir: VisualIR) -> dict[str, Any]:
        return {
            "scene_id": visual_ir.scene_id,
            "visual_ir_version": visual_ir.version,
            "objects": [
                {
                    "visual_id": obj.visual_id,
                    "semantic_id": obj.semantic_id,
                    "kind": obj.kind,
                    "geometry": deepcopy(obj.geometry),
                    "constraint_refs": list(obj.constraint_refs),
                    "mathematics_locked": obj.mathematics_locked,
                    "renderer_ref": obj.renderer_ref or f"spline:{obj.visual_id}",
                    "style": {},
                }
                for obj in visual_ir.objects
            ],
        }

    def apply_style_edit(self, scene: dict[str, Any], visual_id: str, **style: Any) -> None:
        target = next(obj for obj in scene["objects"] if obj["visual_id"] == visual_id)
        target["style"].update(style)

    def import_identity_map(self, scene: dict[str, Any]) -> dict[str, str]:
        return {obj["visual_id"]: obj["semantic_id"] for obj in scene["objects"]}

    def mathematical_snapshot(self, scene: dict[str, Any]) -> tuple[tuple[str, str, str, object], ...]:
        return tuple(
            (
                obj["visual_id"],
                obj["semantic_id"],
                obj["kind"],
                deepcopy(obj["geometry"]),
            )
            for obj in scene["objects"]
        )
