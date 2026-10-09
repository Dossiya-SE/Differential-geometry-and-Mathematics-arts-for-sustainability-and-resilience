"""Independent closed-form checks for v1 visual mathematics contracts."""

from __future__ import annotations

import math
import unittest

from msr.dynamics.linear_invariance import (
    FlowInputError,
    entrance_time,
    flow,
    in_unit_disk,
)
from msr.geometry.stereographic import (
    ProjectionInputError,
    plane_to_sphere,
    sphere_to_plane,
)


class VisualModelTests(unittest.TestCase):
    def test_autonomous_flow_and_invariance(self) -> None:
        for angle_index in range(40):
            angle = 2.0 * math.pi * angle_index / 40
            for radius_index in range(11):
                radius = radius_index / 10.0
                start = radius * math.cos(angle), radius * math.sin(angle)
                self.assertTrue(in_unit_disk(start))
                for tau in (0.0, 0.25, 1.0, 3.0):
                    image = flow(start, tau)
                    self.assertTrue(in_unit_disk(image))
                    self.assertAlmostEqual(
                        math.hypot(*image),
                        math.hypot(*start) * math.exp(-tau),
                        delta=2e-15,
                    )

    def test_outside_entry_does_not_imply_initial_viability(self) -> None:
        initial = (1.4, 0.35)
        self.assertFalse(in_unit_disk(initial))
        tau = entrance_time(initial)
        self.assertIsNotNone(tau)
        assert tau is not None
        self.assertAlmostEqual(math.hypot(*flow(initial, tau)), 1.0, delta=1e-14)
        self.assertTrue(in_unit_disk(flow(initial, tau + 0.2)))
        self.assertFalse(in_unit_disk(initial))

    def test_invalid_flow_is_rejected(self) -> None:
        with self.assertRaises(FlowInputError):
            flow((1.0, 2.0), -0.01)
        with self.assertRaises(FlowInputError):
            flow((math.nan, 0.0), 1.0)

    def test_stereographic_reference_point_and_inverse(self) -> None:
        image = sphere_to_plane((math.sqrt(3.0) / 2.0, 0.0, -0.5))
        self.assertAlmostEqual(image[0], 1.0 / math.sqrt(3.0), delta=1e-14)
        self.assertAlmostEqual(image[1], 0.0, delta=1e-14)
        for u in (-2.0, -0.5, 0.0, 0.5, 1.5):
            for v in (-1.3, 0.0, 0.7):
                point = plane_to_sphere((u, v))
                self.assertAlmostEqual(math.hypot(*point), 1.0, delta=1e-14)
                mapped = sphere_to_plane(point)
                self.assertAlmostEqual(mapped[0], u, delta=2e-14)
                self.assertAlmostEqual(mapped[1], v, delta=2e-14)

    def test_stereographic_pole_excluded(self) -> None:
        for point in ((0.0, 0.0, 1.0), (0.0, 0.0, 2.0), (math.nan, 0.0, 0.0)):
            with self.subTest(point=point), self.assertRaises(ProjectionInputError):
                sphere_to_plane(point)


if __name__ == "__main__":
    unittest.main()
