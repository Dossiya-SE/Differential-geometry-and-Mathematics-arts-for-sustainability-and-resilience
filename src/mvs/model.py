from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from enum import StrEnum
from types import MappingProxyType
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class TaskState(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({str(key): _freeze(item) for key, item in value.items()})
    if isinstance(value, list | tuple):
        return tuple(_freeze(item) for item in value)
    return value


def _thaw(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw(item) for item in value]
    return value


@dataclass(frozen=True)
class Capability:
    id: str
    domain: str
    deterministic: bool
    read_only: bool
    destructive: bool
    long_running: bool
    requires_gpu: bool
    produces_visual: bool
    mathematical_validation_required: bool
    version: str = "0.1"
    provenance: str = "mvs-native"


@dataclass(frozen=True)
class Skill:
    id: str
    description: str
    capability_ids: tuple[str, ...]
    validator_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class Constraint:
    id: str
    description: str
    validator: Callable[[Any], bool]


@dataclass(frozen=True)
class ValidationResult:
    validator_id: str
    passed: bool
    residual: float | None = None
    tolerance: float | None = None
    detail: str = ""


@dataclass(frozen=True)
class Validator:
    id: str
    description: str
    validate: Callable[[Any], ValidationResult]


@dataclass
class Task(Generic[T]):
    id: str
    state: TaskState = TaskState.PENDING
    result: T | None = None
    error: str | None = None


@dataclass(frozen=True)
class SceneObject:
    visual_id: str
    semantic_id: str
    kind: str
    geometry: Mapping[str, Any]
    constraint_refs: tuple[str, ...] = ()
    renderer_ref: str | None = None
    mathematics_locked: bool = True

    def __post_init__(self) -> None:
        object.__setattr__(self, "geometry", _freeze(self.geometry))

    def to_dict(self) -> dict[str, Any]:
        return {
            "visual_id": self.visual_id,
            "semantic_id": self.semantic_id,
            "kind": self.kind,
            "geometry": _thaw(self.geometry),
            "constraint_refs": list(self.constraint_refs),
            "renderer_ref": self.renderer_ref,
            "mathematics_locked": self.mathematics_locked,
        }


@dataclass(frozen=True)
class VisualIR:
    version: str
    scene_id: str
    objects: tuple[SceneObject, ...]
    provenance: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "provenance", _freeze(self.provenance))

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "scene_id": self.scene_id,
            "objects": [obj.to_dict() for obj in self.objects],
            "provenance": _thaw(self.provenance),
        }
