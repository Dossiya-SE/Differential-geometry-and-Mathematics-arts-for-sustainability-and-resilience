from __future__ import annotations

from copy import deepcopy
from typing import Any, cast

from .model import VisualIR


class SplineAdapter:
    """Pure translation boundary: Visual IR is authoritative; renderer state is not."""

    def export_scene(self, visual_ir: VisualIR) -> dict[str, Any]:
        objects: list[dict[str, Any]] = []
        for obj in visual_ir.objects:
            serialized = obj.to_dict()
            serialized["renderer_ref"] = obj.renderer_ref or f"spline:{obj.visual_id}"
            serialized["style"] = {}
            objects.append(serialized)

        return {
            "scene_id": visual_ir.scene_id,
            "visual_ir_version": visual_ir.version,
            "objects": objects,
        }

    def apply_style_edit(self, scene: dict[str, Any], visual_id: str, **style: Any) -> None:
        target = self._find(scene, visual_id)
        target["style"].update(style)

    def import_identity_map(self, scene: dict[str, Any]) -> dict[str, str]:
        return {obj["visual_id"]: obj["semantic_id"] for obj in scene["objects"]}

    def mathematical_snapshot(
        self, scene: dict[str, Any]
    ) -> tuple[tuple[str, str, str, object], ...]:
        return tuple(
            (
                obj["visual_id"],
                obj["semantic_id"],
                obj["kind"],
                deepcopy(obj["geometry"]),
            )
            for obj in scene["objects"]
        )

    def validate_roundtrip(self, visual_ir: VisualIR, scene: dict[str, Any]) -> bool:
        expected = {
            obj.visual_id: (
                obj.semantic_id,
                obj.kind,
                obj.to_dict()["geometry"],
                obj.mathematics_locked,
            )
            for obj in visual_ir.objects
        }
        observed = {
            obj["visual_id"]: (
                obj["semantic_id"],
                obj["kind"],
                obj["geometry"],
                obj["mathematics_locked"],
            )
            for obj in scene["objects"]
        }
        return observed == expected

    @staticmethod
    def _find(scene: dict[str, Any], visual_id: str) -> dict[str, Any]:
        for obj in scene["objects"]:
            candidate = cast(dict[str, Any], obj)
            if candidate["visual_id"] == visual_id:
                return candidate
        raise KeyError(f"unknown visual object: {visual_id}")
