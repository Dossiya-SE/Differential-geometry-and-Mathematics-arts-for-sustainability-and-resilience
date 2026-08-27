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
        if capability.id in self._capabilities:
            raise ValueError(f"capability already registered: {capability.id}")
        self._capabilities[capability.id] = capability
        self._executors[capability.id] = executor
        self._cache.clear()

    @staticmethod
    def _tokens(capability: Capability) -> set[str]:
        text = f"{capability.id} {capability.domain}".lower().replace(".", " ")
        return set(text.replace("_", " ").split())

    def search(self, query: str) -> tuple[Capability, ...]:
        key = query.strip().lower()
        if not key:
            return ()
        if key in self._cache:
            return self._cache[key]

        terms = set(key.replace("_", " ").replace(".", " ").split())
        matches = [
            (len(terms & self._tokens(capability)), capability.id, capability)
            for capability in self._capabilities.values()
            if terms & self._tokens(capability)
        ]
        matches.sort(key=lambda item: (-item[0], item[1]))
        result = tuple(capability for _, _, capability in matches)
        self._cache[key] = result
        return result

    def describe(self, capability_id: str) -> Capability:
        try:
            return self._capabilities[capability_id]
        except KeyError as exc:
            raise KeyError(f"unknown capability: {capability_id}") from exc

    def execute(self, capability_id: str, **arguments: Any) -> Task[Any]:
        if capability_id not in self._executors:
            raise KeyError(f"unknown capability: {capability_id}")

        task = Task[Any](id=f"task:{capability_id}:{len(self._tasks) + 1}")
        self._tasks[task.id] = task
        task.state = TaskState.RUNNING
        try:
            task.result = self._executors[capability_id](**arguments)
            task.state = TaskState.SUCCEEDED
        except Exception as exc:  # pragma: no cover - failure is surfaced by task state
            task.error = f"{type(exc).__name__}: {exc}"
            task.state = TaskState.FAILED
        return task

    def task_status(self, task_id: str) -> Task[Any]:
        try:
            return self._tasks[task_id]
        except KeyError as exc:
            raise KeyError(f"unknown task: {task_id}") from exc
