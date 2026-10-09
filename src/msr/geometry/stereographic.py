"""MSR-MOD-0004: north-pole stereographic projection from the unit sphere."""

from __future__ import annotations

from math import hypot, isfinite
from typing import TypeAlias

Point2: TypeAlias = tuple[float, float]
Point3: TypeAlias = tuple[float, float, float]


class ProjectionInputError(ValueError):
    """Invalid or numerically unsafe coordinate for stereographic projection."""


def sphere_to_plane(point: Point3) -> Point2:
    """Map S^2 minus N=(0,0,1) to equatorial plane coordinates.

    p=(x,y,z) -> (x/(1-z), y/(1-z)). Unit-sphere input is
    checked within binary64 tolerance. Undefined at N; extreme near-N inputs
    can be numerically underresolved and are rejected.
    """
    if len(point) != 3 or not all(isfinite(x) for x in point):
        raise ProjectionInputError("expected three finite coordinates")
    x, y, z = point
    if abs(hypot(x, y, z) - 1.0) > 1e-12:
        raise ProjectionInputError("point must lie on the unit two-sphere")
    denominator = 1.0 - z
    if denominator <= 1e-14:
        raise ProjectionInputError("projection is singular or underresolved near N")
    image = x / denominator, y / denominator
    if not all(isfinite(value) for value in image):
        raise ProjectionInputError("projection exceeds finite binary64 range")
    return image


def plane_to_sphere(point: Point2) -> Point3:
    """Return inverse stereographic projection for finite planar points."""
    if len(point) != 2 or not all(isfinite(value) for value in point):
        raise ProjectionInputError("expected two finite coordinates")
    u, v = point
    square = u * u + v * v
    if not isfinite(square):
        raise ProjectionInputError("squared planar radius exceeds binary64 range")
    denominator = 1.0 + square
    return 2.0 * u / denominator, 2.0 * v / denominator, (square - 1.0) / denominator
