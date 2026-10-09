"""MSR-MOD-0003: exact dimensionless autonomous flow and unit-disk constraint."""

from __future__ import annotations

from math import exp, hypot, isfinite, log
from typing import TypeAlias

Point2: TypeAlias = tuple[float, float]


class FlowInputError(ValueError):
    """Non-finite or structurally invalid state/time input."""


def _state(point: Point2) -> Point2:
    if len(point) != 2 or not all(isfinite(x) for x in point):
        raise FlowInputError("state must be two finite coordinates")
    return point


def flow(point: Point2, tau: float) -> Point2:
    """Solve dx/dtau=-x for tau>=0, dimensionless; no control or disturbance."""
    _state(point)
    if not isfinite(tau) or tau < 0:
        raise FlowInputError("dimensionless time must be finite and nonnegative")
    factor = exp(-tau)
    return point[0] * factor, point[1] * factor


def in_unit_disk(point: Point2) -> bool:
    """Test membership of K={x: ||x||_2 <= 1} at the supplied instant."""
    _state(point)
    return hypot(*point) <= 1.0


def entrance_time(point: Point2) -> float | None:
    """Return first boundary entry from ||point||>1, otherwise None.

    An initial point outside K is not viable at tau=0 even if it enters later.
    """
    _state(point)
    radius = hypot(*point)
    return log(radius) if radius > 1.0 else None
