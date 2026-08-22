"""Reference Riemannian operations on the unit two-sphere.

Model contract: ``MSR-MOD-0001``.

The module implements the induced round metric on
``S^2 = {x in R^3 : x^T x = 1}``. It is a domain-neutral verification fixture
and carries no sustainability or resilience semantics.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

FloatVector: TypeAlias = npt.NDArray[np.float64]
VectorLike: TypeAlias = Sequence[float] | npt.NDArray[np.floating]

_UNIT_TOLERANCE = 1e-10
_TANGENT_TOLERANCE = 1e-10
_SMALL_ANGLE = 1e-12
_ANTIPODAL_TOLERANCE = 1e-10


class GeometryInputError(ValueError):
    """Raised when an input violates the declared model domain."""


class AntipodalError(GeometryInputError):
    """Raised when the principal spherical logarithm is non-unique."""


def _vector(value: VectorLike, *, name: str) -> FloatVector:
    array = np.asarray(value, dtype=np.float64)
    if array.shape != (3,):
        raise GeometryInputError(f"{name} must have shape (3,), received {array.shape}")
    if not bool(np.all(np.isfinite(array))):
        raise GeometryInputError(f"{name} must contain only finite values")
    return array


def normalize(value: VectorLike) -> FloatVector:
    """Return ``value / ||value||_2`` and reject zero or non-finite vectors."""
    array = _vector(value, name="value")
    norm = float(np.linalg.norm(array))
    if not np.isfinite(norm) or norm <= 0.0:
        raise GeometryInputError("value must have a finite, nonzero norm")
    return np.asarray(array / norm, dtype=np.float64)


def _unit(value: VectorLike, *, name: str) -> FloatVector:
    array = _vector(value, name=name)
    norm = float(np.linalg.norm(array))
    if not np.isclose(norm, 1.0, atol=_UNIT_TOLERANCE, rtol=_UNIT_TOLERANCE):
        raise GeometryInputError(f"{name} must lie on the unit sphere; norm={norm:.17g}")
    return np.asarray(array / norm, dtype=np.float64)


def is_on_sphere(value: VectorLike, *, atol: float = _UNIT_TOLERANCE) -> bool:
    """Return whether a finite three-vector has norm one within ``atol``."""
    try:
        array = _vector(value, name="value")
    except GeometryInputError:
        return False
    return bool(np.isclose(np.linalg.norm(array), 1.0, atol=atol, rtol=atol))


def tangent_project(base: VectorLike, vector: VectorLike) -> FloatVector:
    """Orthogonally project an ambient vector onto ``T_base S^2``."""
    point = _unit(base, name="base")
    ambient = _vector(vector, name="vector")
    return np.asarray(ambient - float(np.dot(point, ambient)) * point, dtype=np.float64)


def is_tangent(
    base: VectorLike,
    vector: VectorLike,
    *,
    atol: float = _TANGENT_TOLERANCE,
) -> bool:
    """Return whether ``vector`` lies in ``T_base S^2`` within ``atol``."""
    try:
        point = _unit(base, name="base")
        tangent = _vector(vector, name="vector")
    except GeometryInputError:
        return False
    return bool(abs(float(np.dot(point, tangent))) <= atol)


def distance(base: VectorLike, target: VectorLike) -> float:
    """Return the principal distance using a stable ``atan2`` formulation."""
    point = _unit(base, name="base")
    other = _unit(target, name="target")
    cosine = float(np.clip(np.dot(point, other), -1.0, 1.0))
    sine = float(np.linalg.norm(np.cross(point, other)))
    return float(np.arctan2(sine, cosine))


def exp_map(base: VectorLike, tangent: VectorLike) -> FloatVector:
    """Evaluate ``Exp_base(tangent)`` for ``tangent`` in ``T_base S^2``.

    The output is renormalized only to remove binary64 drift. A non-tangent
    vector is rejected instead of being silently projected.
    """
    point = _unit(base, name="base")
    vector = _vector(tangent, name="tangent")
    tangency_residual = abs(float(np.dot(point, vector)))
    if tangency_residual > _TANGENT_TOLERANCE:
        raise GeometryInputError(
            f"tangent must lie in T_base S^2; residual={tangency_residual:.3e}"
        )

    norm = float(np.linalg.norm(vector))
    if norm <= _SMALL_ANGLE:
        return point.copy()
    result = np.cos(norm) * point + (np.sin(norm) / norm) * vector
    return normalize(result)


def log_map(base: VectorLike, target: VectorLike) -> FloatVector:
    """Evaluate the principal ``Log_base(target)`` away from the cut locus."""
    point = _unit(base, name="base")
    other = _unit(target, name="target")
    cosine = float(np.clip(np.dot(point, other), -1.0, 1.0))
    orthogonal = other - cosine * point
    sine = float(np.linalg.norm(orthogonal))
    theta = float(np.arctan2(sine, cosine))

    if theta <= _SMALL_ANGLE:
        return np.zeros(3, dtype=np.float64)
    if sine <= _ANTIPODAL_TOLERANCE and cosine < 0.0:
        raise AntipodalError("principal logarithm is non-unique at the antipode")

    tangent = (theta / sine) * orthogonal
    return tangent_project(point, tangent)


def geodesic(base: VectorLike, initial_velocity: VectorLike, time: float) -> FloatVector:
    """Evaluate the geodesic ``gamma(time) = Exp_base(time * initial_velocity)``."""
    if not np.isfinite(time):
        raise GeometryInputError("time must be finite")
    velocity = _vector(initial_velocity, name="initial_velocity")
    return exp_map(base, time * velocity)


def round_trip_residual(base: VectorLike, target: VectorLike) -> float:
    """Return ``||Exp_base(Log_base(target)) - target||_2``."""
    other = _unit(target, name="target")
    reconstructed = exp_map(base, log_map(base, other))
    return float(np.linalg.norm(reconstructed - other))
