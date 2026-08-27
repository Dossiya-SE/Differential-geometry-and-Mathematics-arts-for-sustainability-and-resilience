from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .model import Capability, Task, TaskState

Executor = Callable[..., Any]


class CapabilityRegistry:
    def __init__(self) -> None:
        self._capabilities: dict[str, Capability] = {}
        self._executors: dict[str, Executor] = {}
        self._tasks: dict[str, Task[Any]] = {}
        self._cache: dict[str, tuple[Capability, ...]] = {}

    def register(self, capability: Capability, executor: Executor) -> None:
        self._capabilities[capability.id] = capability
        self._executors[capability.id] = executor
        self._cache.clear()

    def search(self, query: str) -> tuple[Capability, ...]:
        key = query.strip().lower()
        if key in self._cache:
            return self._cache[key]
        terms = set(key.replace("_", " ").replace(".", " ").split())
        ranked = sorted(
            self._capabilities.values(),
            key=lambda cap: len(terms & set((cap.id + " " + cap.domain).lower().replace(".", " ").split())),
            reverse=True,
        )
        result = tuple(cap for cap in ranked if terms & set((cap.id + " " + cap.domain).lower().replace(".", " ").split()))
        self._cache[key] = result
        return result

    def describe(self, capability_id: str) -> Capability:
        return self._capabilities[capability_id]

    def execute(self, capability_id: str, **arguments: Any) -> Task[Any]:
        task = Task[Any](id=f"task:{capability_id}:{len(self._tasks) + 1}")
        self._tasks[task.id] = task
        task.state = TaskState.RUNNING
        try:
            task.result = self._executors[capability_id](**arguments)
            task.state = TaskState.SUCCEEDED
        except Exception as exc:  # pragma: no cover - surfaced through task contract
            task.error = str(exc)
            task.state = TaskState.FAILED
        return task

    def task_status(self, task_id: str) -> Task[Any]:
        return self._tasks[task_id]
