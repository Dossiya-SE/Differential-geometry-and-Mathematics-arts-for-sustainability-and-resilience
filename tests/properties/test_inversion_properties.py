"""Deterministic numerical properties of Euclidean inversion (MSR-MOD-0002)."""

from __future__ import annotations

import unittest

import numpy as np

from msr.geometry.inversion import invert_point, inversion_jacobian


class InversionPropertyTests(unittest.TestCase):
    def test_involution_radius_and_conformal_jacobian(self) -> None:
        generator = np.random.default_rng(20261009)
        for dimension in (2, 3):
            center = generator.uniform(-0.5, 0.5, dimension)
            for _ in range(120):
                direction = generator.normal(size=dimension)
                direction = direction / np.linalg.norm(direction)
                distance = float(generator.uniform(0.25, 3.5))
                radius = float(generator.uniform(0.5, 2.0))
                point = center + distance * direction
                mapped = invert_point(point, center, radius)
                recovered = invert_point(mapped, center, radius)
                np.testing.assert_allclose(recovered, point, atol=2e-12, rtol=2e-12)
                self.assertAlmostEqual(
                    distance * float(np.linalg.norm(mapped - center)), radius**2, delta=2e-12
                )
                jac = inversion_jacobian(point, center, radius)
                conformal_scale = (radius / distance) ** 2
                np.testing.assert_allclose(
                    jac.T @ jac,
                    (conformal_scale**2) * np.eye(dimension),
                    atol=2e-12,
                    rtol=2e-12,
                )

    def test_jacobian_matches_finite_differences(self) -> None:
        point = np.array([1.2, -0.7])
        center = np.array([0.1, 0.2])
        radius = 1.5
        epsilon = 1e-6
        columns = []
        for axis in np.eye(2):
            columns.append(
                (invert_point(point + epsilon * axis, center, radius)
                 - invert_point(point - epsilon * axis, center, radius)) / (2 * epsilon)
            )
        numerical = np.stack(columns, axis=1)
        np.testing.assert_allclose(
            numerical, inversion_jacobian(point, center, radius), atol=3e-10, rtol=3e-10
        )


if __name__ == "__main__":
    unittest.main()
