"""Unit tests for the domain and failure behavior of sphere operations."""

from __future__ import annotations

import unittest

import numpy as np

from msr.geometry.sphere import (
    AntipodalError,
    GeometryInputError,
    distance,
    exp_map,
    is_on_sphere,
    is_tangent,
    log_map,
    normalize,
    tangent_project,
)


class SphereUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.north = np.array([0.0, 0.0, 1.0])
        self.east = np.array([1.0, 0.0, 0.0])

    def test_normalize(self) -> None:
        normalized = normalize([3.0, 4.0, 0.0])
        np.testing.assert_allclose(normalized, [0.6, 0.8, 0.0], atol=1e-15)

    def test_zero_vector_is_rejected(self) -> None:
        with self.assertRaises(GeometryInputError):
            normalize([0.0, 0.0, 0.0])

    def test_invalid_shape_is_rejected(self) -> None:
        with self.assertRaises(GeometryInputError):
            normalize([1.0, 0.0])

    def test_projection_is_tangent(self) -> None:
        projected = tangent_project(self.north, [1.0, 2.0, 3.0])
        self.assertTrue(is_tangent(self.north, projected))
        np.testing.assert_allclose(projected, [1.0, 2.0, 0.0], atol=1e-15)

    def test_quarter_circle_distance(self) -> None:
        self.assertAlmostEqual(distance(self.north, self.east), np.pi / 2.0, places=14)

    def test_zero_exponential(self) -> None:
        result = exp_map(self.north, [0.0, 0.0, 0.0])
        np.testing.assert_allclose(result, self.north, atol=1e-15)

    def test_non_tangent_exponential_is_rejected(self) -> None:
        with self.assertRaises(GeometryInputError):
            exp_map(self.north, [0.0, 0.0, 0.1])

    def test_antipodal_logarithm_is_rejected(self) -> None:
        with self.assertRaises(AntipodalError):
            log_map(self.north, -self.north)

    def test_sphere_predicate_rejects_nonfinite_input(self) -> None:
        self.assertFalse(is_on_sphere([np.nan, 0.0, 1.0]))


if __name__ == "__main__":
    unittest.main()
