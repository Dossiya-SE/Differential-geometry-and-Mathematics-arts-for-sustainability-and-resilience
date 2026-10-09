"""Tests for the aurora U, V_nu, K_s, Q_s educational reconstruction."""

import numpy as np
import pytest

from msr.visualization.aurora_uvkq import (
    HORIZON_SHIFT,
    aurora_k,
    aurora_q,
    aurora_q_oscillatory_correction,
    aurora_u,
    aurora_v,
)


def test_u_and_v_match_direct_formula_away_from_singularity() -> None:
    x = np.array([[0.0, 0.5]], dtype=np.float64)
    y = np.array([[0.2, 0.4]], dtype=np.float64)

    expected_u = (x + 0.25) / (y + HORIZON_SHIFT)
    expected_v = (1.0 - x / 4.0) / (y + HORIZON_SHIFT) + 0.02

    np.testing.assert_allclose(aurora_u(x, y), expected_u)
    np.testing.assert_allclose(aurora_v(x, y, 2), expected_v)


def test_v_channel_index_is_exact_constant_offset() -> None:
    x = np.array([0.1, 0.3], dtype=np.float64)
    y = np.array([0.2, 0.5], dtype=np.float64)

    np.testing.assert_allclose(aurora_v(x, y, 1) - aurora_v(x, y, 0), 0.01)
    np.testing.assert_allclose(aurora_v(x, y, 2) - aurora_v(x, y, 0), 0.02)


def test_k_geometric_scale_ratio() -> None:
    y = np.array([0.2, 0.5], dtype=np.float64)
    ratio = aurora_k(y, 20) / aurora_k(y, 19)

    np.testing.assert_allclose(ratio, 50.0 / 49.0)


def test_q_is_finite_away_from_singular_line() -> None:
    x = np.linspace(-1.0, 1.0, 50, dtype=np.float64)
    y = np.full_like(x, 0.3)
    q = aurora_q(x, y, 25)

    assert np.all(np.isfinite(q))


def test_q_oscillatory_correction_is_bounded_by_term_amplitudes() -> None:
    x = np.linspace(-1.0, 1.0, 101, dtype=np.float64)
    y = np.full_like(x, 0.4)
    correction = aurora_q_oscillatory_correction(x, y, 25)

    # |2 cos(.) + 0.4 cos(.) + 0.1 cos(.)| <= 2.5 analytically.
    assert np.all(np.abs(correction) <= 2.5 + 1e-12)


def test_discrete_indices_fail_closed() -> None:
    y = np.array([0.2], dtype=np.float64)
    x = np.array([0.1], dtype=np.float64)

    with pytest.raises(ValueError, match="nu"):
        aurora_v(x, y, 3)

    with pytest.raises(ValueError, match="1 <= s <= 50"):
        aurora_k(y, 0)

    with pytest.raises(ValueError, match="1 <= s <= 50"):
        aurora_q(x, y, 51)
