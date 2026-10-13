"""Unit tests for equation-driven mathematical visualization fields."""

import numpy as np
import pytest

from msr.visualization import annular_localization, coordinate_grid, radial_ring_rgb


def test_coordinate_grid_contract() -> None:
    x_grid, y_grid = coordinate_grid(resolution=9, extent=2.0)

    assert x_grid.shape == (9, 9)
    assert y_grid.shape == (9, 9)
    assert np.isclose(x_grid.min(), -2.0)
    assert np.isclose(x_grid.max(), 2.0)
    assert np.isclose(y_grid.min(), -2.0)
    assert np.isclose(y_grid.max(), 2.0)
    assert np.all(np.isfinite(x_grid))
    assert np.all(np.isfinite(y_grid))


def test_annular_localization_reaches_analytic_maximum() -> None:
    radius = np.array([0.0, 1.5, 3.0], dtype=np.float64)
    field = annular_localization(radius, ring_radius=1.5, sharpness=12.0)

    assert np.isclose(field[1], 1.0)
    assert np.all(field > 0.0)
    assert np.all(field <= 1.0)
    assert np.isclose(field[0], field[2])


def test_radial_ring_rgb_contract_and_determinism() -> None:
    x_grid, y_grid = coordinate_grid(resolution=64, extent=3.0)

    first = radial_ring_rgb(x_grid, y_grid)
    second = radial_ring_rgb(x_grid, y_grid)

    assert first.shape == (64, 64, 3)
    assert np.all(np.isfinite(first))
    assert np.all(first >= 0.0)
    assert np.all(first <= 1.0)
    np.testing.assert_array_equal(first, second)


def test_radial_ring_rgb_rejects_mismatched_grids() -> None:
    x_grid = np.zeros((4, 4), dtype=np.float64)
    y_grid = np.zeros((4, 5), dtype=np.float64)

    with pytest.raises(ValueError, match="identical shapes"):
        radial_ring_rgb(x_grid, y_grid)


def test_coordinate_grid_rejects_invalid_domain() -> None:
    with pytest.raises(ValueError, match="at least 2"):
        coordinate_grid(resolution=1)

    with pytest.raises(ValueError, match="finite and positive"):
        coordinate_grid(extent=0.0)
