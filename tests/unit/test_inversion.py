"""Unit and domain checks for MSR-MOD-0002."""

from __future__ import annotations

import unittest

import numpy as np

from msr.geometry.inversion import InversionInputError, invert_point, inversion_jacobian


class InversionUnitTests(unittest.TestCase):
    def test_known_result(self) -> None:
        np.testing.assert_allclose(invert_point([2, 0], [0, 0], 1), [0.5, 0], atol=1e-15)

    def test_fixed_sphere(self) -> None:
        np.testing.assert_allclose(invert_point([3, 4], [0, 0], 5), [3, 4], atol=1e-14)

    def test_three_dimensional_support(self) -> None:
        np.testing.assert_allclose(
            invert_point([0, 0, 4], [0, 0, 0], 2), [0, 0, 1], atol=1e-15
        )

    def test_jacobian_known_case(self) -> None:
        np.testing.assert_allclose(
            inversion_jacobian([2, 0], [0, 0], 1),
            [[-0.25, 0], [0, 0.25]],
            atol=1e-15,
        )

    def test_rejects_center(self) -> None:
        with self.assertRaises(InversionInputError):
            invert_point([0, 0], [0, 0], 1)

    def test_rejects_invalid_vectors(self) -> None:
        for p, c in (([1], [0]), ([1, 2], [0, 0, 0]), ([np.nan, 0], [0, 0])):
            with self.subTest(p=p, c=c), self.assertRaises(InversionInputError):
                invert_point(p, c, 1)

    def test_rejects_non_positive_and_nonfinite_radius(self) -> None:
        for r in (0, -1, np.inf, np.nan):
            with self.subTest(r=r), self.assertRaises(InversionInputError):
                invert_point([1, 0], [0, 0], r)

    def test_rejects_underresolved_inverse(self) -> None:
        with self.assertRaises(InversionInputError):
            invert_point([1e308, 0], [0, 0], 1)


if __name__ == "__main__":
    unittest.main()
