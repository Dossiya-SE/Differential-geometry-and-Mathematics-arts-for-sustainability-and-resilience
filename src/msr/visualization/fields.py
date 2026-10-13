"""Equation-driven fields used by reproducible mathematical-visualization experiments."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]


def coordinate_grid(
    resolution: int = 1200,
    extent: float = 3.0,
) -> tuple[FloatArray, FloatArray]:
    """Return a square Cartesian mesh over ``[-extent, extent]^2``.

    Parameters
    ----------
    resolution:
        Number of samples along each axis. Must be at least 2.
    extent:
        Positive half-width of the square domain.
    """
    if resolution < 2:
        raise ValueError("resolution must be at least 2")
    if not np.isfinite(extent) or extent <= 0.0:
        raise ValueError("extent must be finite and positive")

    axis = np.linspace(-extent, extent, resolution, dtype=np.float64)
    x_grid, y_grid = np.meshgrid(axis, axis)
    return x_grid, y_grid


def annular_localization(
    radius: FloatArray,
    *,
    ring_radius: float = 1.5,
    sharpness: float = 12.0,
) -> FloatArray:
    r"""Evaluate the annular localization field.

    The field is

    .. math::

       A(r) = \exp[-\alpha(r-r_0)^2].

    It reaches its analytic maximum of one at ``r = ring_radius``.
    """
    if ring_radius < 0.0 or not np.isfinite(ring_radius):
        raise ValueError("ring_radius must be finite and non-negative")
    if sharpness <= 0.0 or not np.isfinite(sharpness):
        raise ValueError("sharpness must be finite and positive")

    return np.exp(-sharpness * (radius - ring_radius) ** 2)


def radial_ring_rgb(
    x_grid: FloatArray,
    y_grid: FloatArray,
    *,
    ring_radius: float = 1.5,
    sharpness: float = 12.0,
    angular_frequency: float = 10.0,
    radial_frequency: float = 7.0,
    modulation_amplitude: float = 2.0,
    modulation_frequency: float = 3.0,
) -> FloatArray:
    r"""Generate the MATART-001 bounded RGB field.

    The construction uses polar coordinates, annular localization, and an
    angular-radial phase field. The output shape is ``(H, W, 3)`` and every
    channel is clipped to the closed interval ``[0, 1]``.
    """
    if x_grid.shape != y_grid.shape:
        raise ValueError("x_grid and y_grid must have identical shapes")
    if x_grid.ndim != 2:
        raise ValueError("x_grid and y_grid must be two-dimensional")
    if not np.all(np.isfinite(x_grid)) or not np.all(np.isfinite(y_grid)):
        raise ValueError("coordinate grids must contain only finite values")

    radius = np.hypot(x_grid, y_grid)
    theta = np.arctan2(y_grid, x_grid)

    ring = annular_localization(
        radius,
        ring_radius=ring_radius,
        sharpness=sharpness,
    )
    phase = (
        angular_frequency * theta
        + radial_frequency * radius
        + modulation_amplitude * np.sin(modulation_frequency * theta)
    )
    waves = 0.5 + 0.5 * np.sin(phase)
    center = np.exp(-3.0 * radius**2)

    red = np.clip(0.15 + 0.85 * ring * waves, 0.0, 1.0)
    green = np.clip(0.05 + 0.45 * ring, 0.0, 1.0)
    blue = np.clip(0.15 + 0.80 * ring * (1.0 - waves) + 0.35 * center, 0.0, 1.0)

    return np.stack((red, green, blue), axis=-1)
