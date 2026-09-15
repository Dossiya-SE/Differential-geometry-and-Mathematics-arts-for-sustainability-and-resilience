from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def _save(fig, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=180, bbox_inches="tight", transparent=True, pad_inches=0.05)
    plt.close(fig)
    return path


def evidence_panel(path: Path) -> Path:
    x = np.linspace(-2.5, 2.5, 160)
    y = np.linspace(-2.0, 2.0, 140)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-((X - 0.2) ** 2 / 0.8 + (Y + 0.1) ** 2 / 0.7))
    fig = plt.figure(figsize=(3.2, 2.2))
    ax = fig.add_axes([0.05, 0.08, 0.9, 0.86])
    ax.contourf(X, Y, Z, levels=18)
    ax.set_axis_off()
    return _save(fig, path)


def verification_panel(path: Path) -> Path:
    h = np.array([1.0, 0.7, 0.5, 0.35, 0.25, 0.18])
    fig = plt.figure(figsize=(3.0, 2.0))
    ax = fig.add_axes([0.16, 0.18, 0.78, 0.72])
    for p in [1, 1.5, 2]:
        err = (h ** p) * (0.8 + 0.1 * p)
        ax.plot(h, err, marker="o", linewidth=1.6)
    ax.set_xlabel("h", fontsize=8)
    ax.set_ylabel("error", fontsize=8)
    ax.grid(alpha=0.25)
    ax.tick_params(labelsize=7)
    return _save(fig, path)


def validation_panel(path: Path) -> Path:
    t = np.linspace(0, 8, 90)
    y_obs = np.sin(t) * np.exp(-0.08 * t)
    y_mod = np.sin(t + 0.1) * np.exp(-0.075 * t)
    fig = plt.figure(figsize=(3.0, 2.0))
    ax = fig.add_axes([0.14, 0.18, 0.8, 0.72])
    ax.plot(t, y_obs, marker="o", markevery=9, linewidth=1.6, label="obs")
    ax.plot(t, y_mod, linewidth=1.6, label="model")
    ax.grid(alpha=0.25)
    ax.tick_params(labelsize=7)
    ax.legend(frameon=False, fontsize=7)
    return _save(fig, path)


def generate_all(outdir: Path) -> dict:
    outdir.mkdir(parents=True, exist_ok=True)
    return {
        "evidence": str(evidence_panel(outdir / "evidence.png")),
        "verification": str(verification_panel(outdir / "verification.png")),
        "validation": str(validation_panel(outdir / "validation.png")),
    }
