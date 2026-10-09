"""Euclidean sphere inversion reference (MSR-MOD-0002).

A domain-neutral geometry fixture, not an infrastructure resilience model.
All returned coordinates are in the input's declared Euclidean units.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import hypot
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

FloatVector: TypeAlias = npt.NDArray[np.float64]
VectorLike: TypeAlias = Sequence[float] | npt.NDArray[np.floating]


class InversionInputError(ValueError):
    """Invalid input or inversion at a point outside its finite domain."""


def _inputs(
    point: VectorLike, center: VectorLike, radius: float
) -> tuple[FloatVector, FloatVector, float, float]:
    x = np.asarray(point, dtype=np.float64)
    c = np.asarray(center, dtype=np.float64)
    if x.ndim != 1 or x.shape not in ((2,), (3,)) or c.shape != x.shape:
        raise InversionInputError("point and center must be matching 2D or 3D vectors")
    if not bool(np.all(np.isfinite(x))) or not bool(np.all(np.isfinite(c))):
        raise InversionInputError("point and center must be finite")
    if not np.isfinite(radius) or radius <= 0.0:
        raise InversionInputError("radius must be positive and finite")
    q = x - c
    # The norm is computed before squaring to avoid unnecessary overflow.
    norm = hypot(*(float(v) for v in q))
    if not np.isfinite(norm) or norm == 0.0:
        raise InversionInputError("inversion is undefined at its center")
    scale = float((radius / norm) ** 2)
    if not np.isfinite(scale) or scale == 0.0:
        raise InversionInputError("inversion is outside the binary64 dynamic range")
    return x, c, norm, scale


def invert_point(point: VectorLike, center: VectorLike, radius: float) -> FloatVector:
    """Return ``c + (r / ||x-c||)^2 * (x-c)`` for ``x != c``.

    The inputs use one common unit; ``radius`` uses the same unit. The
    mathematical map is an involution and is conformal wherever finite.
    Raises ``InversionInputError`` at singular or numerically unsafe inputs.
    """
    x, c, _, scale = _inputs(point, center, radius)
    result = c + scale * (x - c)
    if not bool(np.all(np.isfinite(result))) or bool(np.array_equal(result, c)):
        raise InversionInputError("inversion output is non-finite or underresolved")
    return np.asarray(result, dtype=np.float64)


def inversion_jacobian(
    point: VectorLike, center: VectorLike, radius: float
) -> npt.NDArray[np.float64]:
    """Return ``(r^2 / d^2)(I - 2uu^T)``, where ``u=(x-c)/d``.

    The derivative exists for finite ``x != c``; the map reverses
    orientation and preserves the magnitude of angles locally.
    """
    x, c, norm, scale = _inputs(point, center, radius)
    u = (x - c) / norm
    result = scale * (np.eye(x.size, dtype=np.float64) - 2.0 * np.outer(u, u))
    if not bool(np.all(np.isfinite(result))):
        raise InversionInputError("Jacobian overflows binary64")
    return np.asarray(result, dtype=np.float64)
