"""Numerical round-trip and local convergence tests for sphere geodesics."""

from __future__ import annotations

import unittest

import numpy as np

from msr.geometry.sphere import distance, exp_map, geodesic, log_map, normalize


class SphereNumericalTests(unittest.TestCase):
    def test_registered_round_trip_tolerance(self) -> None:
        rng = np.random.default_rng(20260822)
        maximum = 0.0
        for _ in range(512):
            base = normalize(rng.normal(size=3))
            target = normalize(rng.normal(size=3))
            reconstructed = exp_map(base, log_map(base, target))
            maximum = max(maximum, float(np.linalg.norm(reconstructed - target)))
        self.assertLessEqual(maximum, 1e-12)

    def test_geodesic_initial_velocity_converges_second_order(self) -> None:
        base = np.array([0.0, 0.0, 1.0])
        velocity = np.array([0.4, -0.2, 0.0])
        errors: list[float] = []
        for step in (1e-3, 5e-4, 2.5e-4):
            derivative = (geodesic(base, velocity, step) - base) / step
            errors.append(float(np.linalg.norm(derivative - velocity)))
        self.assertLess(errors[1], 0.51 * errors[0])
        self.assertLess(errors[2], 0.51 * errors[1])

    def test_geodesic_length_matches_tangent_norm_below_cut_locus(self) -> None:
        base = np.array([0.0, 0.0, 1.0])
        velocity = np.array([0.3, 0.4, 0.0])
        for time in (0.0, 0.25, 0.5, 1.0):
            endpoint = geodesic(base, velocity, time)
            expected = time * float(np.linalg.norm(velocity))
            self.assertAlmostEqual(distance(base, endpoint), expected, places=13)


if __name__ == "__main__":
    unittest.main()
