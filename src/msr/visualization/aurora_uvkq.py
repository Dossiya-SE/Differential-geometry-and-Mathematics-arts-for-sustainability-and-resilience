"""Educational reconstruction of four visible aurora-study equations.

The functions in this module reproduce only the U, V_nu, K_s, and Q_s
expressions transcribed from the supplied equation sheet. They are used to
study coordinate transforms and oscillatory procedural fields; they are not a
physical aurora model and do not attempt to reproduce the complete artwork.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]

HORIZON_SHIFT = 1001.0 / 10000.0


def _denominator(y: FloatArray) -> FloatArray:
    return y + HORIZON_SHIFT


def aurora_u(x: FloatArray, y: FloatArray) -> FloatArray:
    r"""Evaluate

    .. math::

       U(x,y)=\frac{x+1/4}{y+1001/10000}.
    """
    return (x + 0.25) / _denominator(y)


def aurora_v(x: FloatArray, y: FloatArray, nu: int) -> FloatArray:
    r"""Evaluate

    .. math::

       V_\nu(x,y)=\frac{1-x/4}{y+1001/10000}+\frac{\nu}{100}.
    """
    if nu not in (0, 1, 2):
        raise ValueError("nu must be one of 0, 1, or 2")
    return (1.0 - x / 4.0) / _denominator(y) + nu / 100.0


def aurora_k(y: FloatArray, s: int) -> FloatArray:
    r"""Evaluate

    .. math::

       K_s(y)=\left(\frac{50}{49}\right)^s\frac{1}{y+1001/10000}.
    """
    if not 1 <= s <= 50:
        raise ValueError("s must satisfy 1 <= s <= 50")
    return (50.0 / 49.0) ** s / _denominator(y)


def aurora_q(x: FloatArray, y: FloatArray, s: int) -> FloatArray:
    r"""Evaluate the visible oscillatory field Q_s(x,y).

    .. math::

       Q_s = 3\left(x+\frac{s}{500}\right)K_s
       +2\cos K_s
       +\frac{2}{5}\cos\left(5\left(x+\frac{s}{500}\right)K_s+8K_s\right)
       +\frac{1}{10}\cos\left(15\left(x+\frac{s}{500}\right)K_s-18K_s\right).
    """
    ks = aurora_k(y, s)
    shifted_x = x + s / 500.0
    return (
        3.0 * shifted_x * ks
        + 2.0 * np.cos(ks)
        + (2.0 / 5.0) * np.cos(5.0 * shifted_x * ks + 8.0 * ks)
        + (1.0 / 10.0) * np.cos(15.0 * shifted_x * ks - 18.0 * ks)
    )


def aurora_q_oscillatory_correction(x: FloatArray, y: FloatArray, s: int) -> FloatArray:
    """Return Q_s with its dominant linear-perspective term removed."""
    ks = aurora_k(y, s)
    shifted_x = x + s / 500.0
    return aurora_q(x, y, s) - 3.0 * shifted_x * ks
