"""MATART-001: equation-to-pixel radial ring field.

Run from the repository root after installing the visualization extra:

    python -m pip install -e '.[visualization]'
    python experiments/learning/01_equation_to_pixel/matart_001_radial_ring.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from msr.visualization import coordinate_grid, radial_ring_rgb

RESOLUTION = 1200
EXTENT = 3.0
OUTPUT = Path("figures/generated/learning/MATART_001_radial_ring.png")


def main() -> None:
    """Render and save the registered MATART-001 image."""
    x_grid, y_grid = coordinate_grid(resolution=RESOLUTION, extent=EXTENT)
    image = radial_ring_rgb(x_grid, y_grid)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(8.0, 8.0), dpi=180)
    axis.imshow(
        image,
        extent=[-EXTENT, EXTENT, -EXTENT, EXTENT],
        origin="lower",
        interpolation="bilinear",
    )
    axis.set_aspect("equal")
    axis.set_axis_off()
    figure.savefig(OUTPUT, bbox_inches="tight", pad_inches=0.0)
    plt.close(figure)

    print(f"MATART-001 written to {OUTPUT}")


if __name__ == "__main__":
    main()
