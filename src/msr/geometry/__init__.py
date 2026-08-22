"""Domain-neutral differential-geometric reference implementations."""

from msr.geometry.sphere import (
    AntipodalError,
    GeometryInputError,
    distance,
    exp_map,
    geodesic,
    is_on_sphere,
    is_tangent,
    log_map,
    normalize,
    round_trip_residual,
    tangent_project,
)

__all__ = [
    "AntipodalError",
    "GeometryInputError",
    "distance",
    "exp_map",
    "geodesic",
    "is_on_sphere",
    "is_tangent",
    "log_map",
    "normalize",
    "round_trip_residual",
    "tangent_project",
]
