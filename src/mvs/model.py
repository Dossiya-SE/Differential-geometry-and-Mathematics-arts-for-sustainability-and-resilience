from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class TaskState(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


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
    geometry: dict[str, Any]
    constraint_refs: tuple[str, ...] = ()
    renderer_ref: str | None = None
    mathematics_locked: bool = True


@dataclass(frozen=True)
class VisualIR:
    version: str
    scene_id: str
    objects: tuple[SceneObject, ...]
    provenance: dict[str, str] = field(default_factory=dict)
