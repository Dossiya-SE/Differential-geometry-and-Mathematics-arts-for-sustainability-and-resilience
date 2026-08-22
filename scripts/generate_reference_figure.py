"""Generate the deterministic SVG for the MSR-MOD-0001 sphere fixture."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "figures/source/MSR-FIG-0001_spec.json"
OUTPUT_PATH = ROOT / "figures/generated/MSR-FIG-0001_sphere-geodesic.svg"


def _load_spec() -> dict[str, Any]:
    value: Any = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("figure specification must contain a JSON object")
    return value


def _ellipse_point(
    t: float,
    *,
    center_x: float,
    center_y: float,
    radius_x: float,
    radius_y: float,
    rotation: float,
) -> tuple[float, float]:
    cosine = math.cos(t)
    sine = math.sin(t)
    cos_rotation = math.cos(rotation)
    sin_rotation = math.sin(rotation)
    x = center_x + radius_x * cosine * cos_rotation - radius_y * sine * sin_rotation
    y = center_y + radius_x * cosine * sin_rotation + radius_y * sine * cos_rotation
    return x, y


def render() -> str:
    """Return a byte-stable SVG generated from the versioned figure specification."""
    spec = _load_spec()
    canvas = spec["canvas"]
    sphere = spec["sphere"]
    curve = spec["geodesic_projection"]

    width = int(canvas["width"])
    height = int(canvas["height"])
    center_x = float(sphere["center_x"])
    center_y = float(sphere["center_y"])
    radius = float(sphere["radius"])
    rotation = math.radians(float(curve["rotation_degrees"]))
    start = float(curve["parameter_start"])
    end = float(curve["parameter_end"])
    samples = int(curve["samples"])

    points = [
        _ellipse_point(
            start + (end - start) * index / (samples - 1),
            center_x=float(curve["center_x"]),
            center_y=float(curve["center_y"]),
            radius_x=float(curve["radius_x"]),
            radius_y=float(curve["radius_y"]),
            rotation=rotation,
        )
        for index in range(samples)
    ]
    polyline = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    point_p = points[0]
    point_q = points[-1]

    derivative_x = -float(curve["radius_x"]) * math.sin(start) * math.cos(rotation) - float(
        curve["radius_y"]
    ) * math.cos(start) * math.sin(rotation)
    derivative_y = -float(curve["radius_x"]) * math.sin(start) * math.sin(rotation) + float(
        curve["radius_y"]
    ) * math.cos(start) * math.cos(rotation)
    derivative_norm = math.hypot(derivative_x, derivative_y)
    tangent_scale = 80.0 / derivative_norm
    tangent_end = (
        point_p[0] + tangent_scale * derivative_x,
        point_p[1] + tangent_scale * derivative_y,
    )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description" data-figure-id="MSR-FIG-0001" data-model-id="MSR-MOD-0001" data-experiment-id="MSR-EXP-0001">
  <title id="title">Domain-neutral spherical geodesic verification artifact</title>
  <desc id="description">A unit sphere with coordinate guides, a blue projected great-circle geodesic from p to q, and an orange initial tangent arrow. The application is not selected. This is a mathematical fixture, not an empirical sustainability or resilience result.</desc>
  <defs>
    <radialGradient id="sphere-fill" cx="38%" cy="30%" r="72%">
      <stop offset="0%" stop-color="#F8FBFE"/>
      <stop offset="100%" stop-color="#DCEAF4"/>
    </radialGradient>
    <clipPath id="sphere-clip">
      <circle cx="{center_x:.0f}" cy="{center_y:.0f}" r="{radius:.0f}"/>
    </clipPath>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#D55E00"/>
    </marker>
    <style>
      .title {{ font: 700 34px system-ui, sans-serif; fill: #17202A; }}
      .subtitle {{ font: 500 19px system-ui, sans-serif; fill: #5D6D7E; }}
      .label {{ font: 650 22px system-ui, sans-serif; fill: #17202A; }}
      .body {{ font: 500 18px system-ui, sans-serif; fill: #34495E; }}
      .small {{ font: 500 15px system-ui, sans-serif; fill: #5D6D7E; }}
      .guide {{ fill: none; stroke: #8CA0AF; stroke-width: 1.5; opacity: 0.72; }}
    </style>
  </defs>

  <rect width="100%" height="100%" fill="#FFFFFF"/>
  <text x="70" y="65" class="title">A verified geometric fixture before application selection</text>
  <text x="70" y="98" class="subtitle">MSR-MOD-0001 · Unit two-sphere · MSR-EXP-0001 · application = NOT_SELECTED</text>

  <g aria-label="Orthographic sphere construction">
    <circle cx="{center_x:.0f}" cy="{center_y:.0f}" r="{radius:.0f}" fill="url(#sphere-fill)" stroke="#17202A" stroke-width="3"/>
    <g clip-path="url(#sphere-clip)">
      <ellipse cx="{center_x:.0f}" cy="{center_y:.0f}" rx="{radius:.0f}" ry="82" class="guide"/>
      <ellipse cx="{center_x:.0f}" cy="{center_y - 115:.0f}" rx="214" ry="54" class="guide"/>
      <ellipse cx="{center_x:.0f}" cy="{center_y + 115:.0f}" rx="214" ry="54" class="guide"/>
      <ellipse cx="{center_x:.0f}" cy="{center_y:.0f}" rx="88" ry="{radius:.0f}" class="guide"/>
      <ellipse cx="{center_x:.0f}" cy="{center_y:.0f}" rx="{radius:.0f}" ry="88" transform="rotate(62 {center_x:.0f} {center_y:.0f})" class="guide"/>
      <polyline points="{polyline}" fill="none" stroke="#0072B2" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <line x1="{point_p[0]:.2f}" y1="{point_p[1]:.2f}" x2="{tangent_end[0]:.2f}" y2="{tangent_end[1]:.2f}" stroke="#D55E00" stroke-width="5" marker-end="url(#arrow)"/>
    <circle cx="{point_p[0]:.2f}" cy="{point_p[1]:.2f}" r="10" fill="#FFFFFF" stroke="#0072B2" stroke-width="5"/>
    <circle cx="{point_q[0]:.2f}" cy="{point_q[1]:.2f}" r="10" fill="#0072B2" stroke="#FFFFFF" stroke-width="3"/>
    <text x="{point_p[0] - 32:.2f}" y="{point_p[1] + 38:.2f}" class="label">p</text>
    <text x="{point_q[0] + 18:.2f}" y="{point_q[1] - 12:.2f}" class="label">q</text>
    <text x="{tangent_end[0] + 12:.2f}" y="{tangent_end[1] - 4:.2f}" class="label" fill="#D55E00">v ∈ TₚS²</text>
    <text x="{center_x - 55:.0f}" y="{center_y + 18:.0f}" class="label">S²</text>
  </g>

  <g transform="translate(900 180)" aria-label="Mathematical and evidential legend">
    <rect x="0" y="0" width="250" height="385" rx="18" fill="#F7F9FA" stroke="#CBD5DC" stroke-width="2"/>
    <text x="24" y="44" class="label">Encoding</text>
    <line x1="24" y1="82" x2="90" y2="82" stroke="#0072B2" stroke-width="8" stroke-linecap="round"/>
    <text x="108" y="89" class="body">geodesic</text>
    <line x1="24" y1="126" x2="90" y2="126" stroke="#D55E00" stroke-width="5" marker-end="url(#arrow)"/>
    <text x="108" y="133" class="body">tangent</text>
    <line x1="24" y1="170" x2="90" y2="170" stroke="#8CA0AF" stroke-width="2"/>
    <text x="108" y="177" class="body">projection guide</text>
    <line x1="24" y1="213" x2="226" y2="213" stroke="#CBD5DC"/>
    <text x="24" y="250" class="label">Validation</text>
    <text x="24" y="283" class="body">Mathematics: verified</text>
    <text x="24" y="315" class="body">Communication: not evaluated</text>
    <text x="24" y="347" class="body">Application: not selected</text>
  </g>

  <rect x="70" y="690" width="1080" height="62" rx="14" fill="#FFF4E6" stroke="#E69F00" stroke-width="2"/>
  <text x="95" y="716" class="body">Scientific boundary</text>
  <text x="95" y="741" class="small">This exact vector artifact verifies a geometric representation only; it is not sustainability, resilience, infrastructure, or behavioral evidence.</text>
</svg>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the deterministic SVG")
    mode.add_argument("--check", action="store_true", help="verify the tracked SVG is current")
    args = parser.parse_args()
    expected = render()

    if args.write:
        OUTPUT_PATH.write_text(expected, encoding="utf-8")
        print(f"wrote {OUTPUT_PATH.relative_to(ROOT)}")
        return 0

    if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != expected:
        print(f"outdated generated figure: {OUTPUT_PATH.relative_to(ROOT)}")
        return 1
    print(f"verified {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
