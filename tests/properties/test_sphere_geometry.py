"""Deterministic property tests for spherical geometric invariants."""

from __future__ import annotations

import unittest

import numpy as np

from msr.geometry.sphere import (
    distance,
    exp_map,
    is_on_sphere,
    is_tangent,
    log_map,
    normalize,
)


class SpherePropertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rng = np.random.default_rng(20260822)

    def point(self) -> np.ndarray:
        return normalize(self.rng.normal(size=3))

    def test_exp_outputs_remain_on_sphere(self) -> None:
        for _ in range(200):
            base = self.point()
            ambient = self.rng.normal(size=3)
            tangent = ambient - np.dot(base, ambient) * base
            tangent *= self.rng.uniform(0.0, 2.5) / max(np.linalg.norm(tangent), 1e-15)
            self.assertTrue(is_on_sphere(exp_map(base, tangent), atol=2e-14))

    def test_log_outputs_are_tangent(self) -> None:
        for _ in range(200):
            base = self.point()
            target = self.point()
            self.assertTrue(is_tangent(base, log_map(base, target), atol=2e-14))

    def test_distance_metric_properties(self) -> None:
        for _ in range(200):
            p = self.point()
            q = self.point()
            r = self.point()
            self.assertGreaterEqual(distance(p, q), 0.0)
            self.assertAlmostEqual(distance(p, q), distance(q, p), places=14)
            self.assertLessEqual(distance(p, r), distance(p, q) + distance(q, r) + 2e-14)

    def test_distance_range(self) -> None:
        for _ in range(200):
            value = distance(self.point(), self.point())
            self.assertGreaterEqual(value, 0.0)
            self.assertLessEqual(value, np.pi)


if __name__ == "__main__":
    unittest.main()
