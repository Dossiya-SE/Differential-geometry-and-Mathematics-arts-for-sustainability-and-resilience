from __future__ import annotations

from copy import deepcopy
from html import escape
from typing import Any, cast

from .model import VisualIR


class CavalryAdapter:
    """Deterministic Visual IR -> SVG/Cavalry boundary.

    Visual IR remains authoritative. The adapter exports semantic identity and
    locked mathematical geometry; downstream tools may change presentation
    attributes but must not redefine mathematical state.
    """

    def export_scene(self, visual_ir: VisualIR) -> dict[str, Any]:
        objects: list[dict[str, Any]] = []
        for obj in visual_ir.objects:
            serialized = obj.to_dict()
            serialized["renderer_ref"] = obj.renderer_ref or f"cavalry:{obj.visual_id}"
            serialized["style"] = {}
            objects.append(serialized)
        return {
            "scene_id": visual_ir.scene_id,
            "visual_ir_version": visual_ir.version,
            "format": "mvs-cavalry-v1",
            "objects": objects,
        }

    def export_svg(self, visual_ir: VisualIR) -> str:
        """Export a deterministic semantic SVG carrier for downstream import.

        Geometry is serialized as canonical metadata rather than guessed into
        renderer coordinates. A later geometry-specific SVG encoder may add
        paths while preserving this contract.
        """
        scene = self.export_scene(visual_ir)
        groups = []
        for obj in scene["objects"]:
            geometry = repr(obj["geometry"])
            groups.append(
                '<g id="{vid}" data-semantic-id="{sid}" data-kind="{kind}" '
                'data-mathematics-locked="{locked}"><metadata>{geometry}</metadata></g>'.format(
                    vid=escape(str(obj["visual_id"]), quote=True),
                    sid=escape(str(obj["semantic_id"]), quote=True),
                    kind=escape(str(obj["kind"]), quote=True),
                    locked=str(bool(obj["mathematics_locked"])).lower(),
                    geometry=escape(geometry),
                )
            )
        return (
            '<svg xmlns="http://www.w3.org/2000/svg" '
            f'data-scene-id="{escape(visual_ir.scene_id, quote=True)}" '
            f'data-visual-ir-version="{escape(visual_ir.version, quote=True)}">'
            + "".join(groups)
            + "</svg>"
        )

    def apply_presentation_edit(
        self, scene: dict[str, Any], visual_id: str, **style: Any
    ) -> None:
        self._find(scene, visual_id)["style"].update(style)

    def identity_map(self, scene: dict[str, Any]) -> dict[str, str]:
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
