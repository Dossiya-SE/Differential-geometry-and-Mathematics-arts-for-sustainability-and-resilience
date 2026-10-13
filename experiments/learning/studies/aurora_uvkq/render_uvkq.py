"""Render progressive diagnostics for the aurora U, V_nu, K_s, Q_s study."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from msr.visualization.aurora_uvkq import (
    HORIZON_SHIFT,
    aurora_k,
    aurora_q,
    aurora_q_oscillatory_correction,
    aurora_u,
    aurora_v,
)

OUTPUT_DIR = Path("figures/generated/learning/aurora_uvkq")


def _robust_display(field: np.ndarray, safe: np.ndarray) -> np.ndarray:
    masked = np.where(safe, field, np.nan)
    low, high = np.nanpercentile(masked, [2.0, 98.0])
    return np.clip(masked, low, high)


def _save_field(
    field: np.ndarray,
    *,
    x: np.ndarray,
    y: np.ndarray,
    safe: np.ndarray,
    title: str,
    label: str,
    filename: str,
) -> None:
    plt.figure(figsize=(10, 6))
    image = plt.imshow(
        _robust_display(field, safe),
        origin="lower",
        extent=[x.min(), x.max(), y.min(), y.max()],
        aspect="auto",
    )
    plt.colorbar(image, label=label)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=180)
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    x = np.linspace((1 - 1000) / 600, (2000 - 1000) / 600, 900)
    y = np.linspace((601 - 1200) / 600, (601 - 1) / 600, 540)
    x_grid, y_grid = np.meshgrid(x, y)

    safe = np.abs(y_grid + HORIZON_SHIFT) >= 0.01

    _save_field(
        aurora_u(x_grid, y_grid),
        x=x,
        y=y,
        safe=safe,
        title=r"$U(x,y)=(x+1/4)/(y+0.1001)$",
        label="U(x,y), clipped to 2–98% for display",
        filename="01_U_perspective_coordinate.png",
    )

    _save_field(
        aurora_v(x_grid, y_grid, 0),
        x=x,
        y=y,
        safe=safe,
        title=r"$V_0(x,y)=(1-x/4)/(y+0.1001)$",
        label="V_0(x,y), clipped to 2–98% for display",
        filename="02_V0_perspective_coordinate.png",
    )

    y_line = np.linspace(y.min(), y.max(), 3000)
    safe_line = np.abs(y_line + HORIZON_SHIFT) >= 0.035

    plt.figure(figsize=(10, 6))
    for s in (1, 10, 25, 50):
        values = np.where(safe_line, aurora_k(y_line, s), np.nan)
        plt.plot(y_line, values, label=f"s={s}")
    plt.ylim(-80, 80)
    plt.xlabel("y")
    plt.ylabel(r"$K_s(y)$")
    plt.title(r"$K_s(y)=(50/49)^s/(y+0.1001)$")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "03_Ks_family.png", dpi=180)
    plt.close()

    s = 25
    _save_field(
        aurora_q(x_grid, y_grid, s),
        x=x,
        y=y,
        safe=safe,
        title=rf"$Q_{{{s}}}(x,y)$: perspective-scaled oscillatory field",
        label=rf"$Q_{{{s}}}(x,y)$, clipped to 2–98% for display",
        filename="04_Q25_full_field.png",
    )

    _save_field(
        aurora_q_oscillatory_correction(x_grid, y_grid, s),
        x=x,
        y=y,
        safe=safe,
        title=rf"Oscillatory correction inside $Q_{{{s}}}$",
        label=rf"$Q_{{{s}}}-3(x+s/500)K_s$",
        filename="05_Q25_oscillatory_correction.png",
    )


if __name__ == "__main__":
    main()
