#!/usr/bin/env python3
"""Render MSR-FIG-0002 from the JSON tensor-geometry specification."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import sys
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "art/tensor-geometry/tensor_geometry.json"
SVG = ROOT / "figures/generated/MSR-FIG-0002_tensor-geometry.svg"
PROVENANCE = ROOT / "figures/generated/MSR-FIG-0002.provenance.json"

Point = tuple[float, float]
Mapper = Callable[[Point], Point]


def load(path: Path) -> dict[str, Any]:
    """Load one JSON object from *path*."""
    value: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("specification must be a JSON object")
    return value


def svg_text(
    x: float,
    y: float,
    value: str,
    size: int = 16,
    weight: int = 400,
    anchor: str = "start",
    css: str = "",
) -> str:
    """Return escaped SVG text with deterministic typography attributes."""
    class_attr = f' class="{css}"' if css else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
        f'font-size="{size}" font-weight="{weight}"{class_attr}>'
        f"{html.escape(value)}</text>"
    )


def heat(value: float, maximum: float) -> str:
    """Map a normalized coupling magnitude to a deterministic diverging color."""
    fraction = 0.0 if maximum <= 0 else max(0.0, min(1.0, value / maximum))
    if fraction < 0.5:
        start, end = (53, 111, 145), (235, 241, 226)
        local_fraction = fraction * 2
    else:
        start, end = (235, 241, 226), (174, 68, 47)
        local_fraction = (fraction - 0.5) * 2
    rgb = [
        round(source + (target - source) * local_fraction)
        for source, target in zip(start, end, strict=True)
    ]
    return "#" + "".join(f"{channel:02x}" for channel in rgb)


def matrix_for(spec: dict[str, Any], hazard: dict[str, Any]) -> list[list[float]]:
    """Contract mechanism factors for one hazard slice of the illustrative tensor."""
    base = spec["coupling_tensor"]["base_coupling"]
    mechanism_factor = sum(
        float(mechanism["weight"]) * float(mechanism["tensor_factor"])
        for mechanism in spec["mechanisms"]
    )
    factor = float(hazard["tensor_factor"]) * mechanism_factor
    return [[float(value) * factor for value in row] for row in base]


def ellipse(metric: list[list[float]], scale: float = 35.0) -> tuple[float, float, float]:
    """Return metric-ellipse radii and orientation for a symmetric SPD 2x2 matrix."""
    a = float(metric[0][0])
    b = float(metric[0][1])
    d = float(metric[1][1])
    root = math.sqrt((a - d) ** 2 + 4 * b * b)
    high = (a + d + root) / 2
    low = (a + d - root) / 2
    if low <= 0:
        raise ValueError("metric tensor must be positive definite")
    angle = 0.5 * math.degrees(math.atan2(2 * b, a - d))
    return scale / math.sqrt(high), scale / math.sqrt(low), angle


def viability_boundary(spec: dict[str, Any]) -> list[Point]:
    """Sample the rotated-superellipse approximation of the viability boundary."""
    viability = spec["viability"]
    boundary = viability["boundary"]
    center_x, center_y = map(float, boundary["center"])
    radius_x, radius_y = map(float, boundary["radii"])
    exponent = float(boundary["exponent"])
    rotation = math.radians(float(boundary["rotation_degrees"]))
    samples = int(viability["boundary_samples"])
    points: list[Point] = []

    for index in range(samples):
        angle = 2 * math.pi * index / samples
        cosine = math.cos(angle)
        sine = math.sin(angle)
        local_x = radius_x * math.copysign(abs(cosine) ** (2 / exponent), cosine)
        local_y = radius_y * math.copysign(abs(sine) ** (2 / exponent), sine)
        x = center_x + math.cos(rotation) * local_x - math.sin(rotation) * local_y
        y = center_y + math.sin(rotation) * local_x + math.cos(rotation) * local_y
        points.append((x, y))
    return points


def metric_distance(a: Point, b: Point, metric: list[list[float]]) -> float:
    """Evaluate the constant-metric quadratic distance used by this demonstrator."""
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    squared = (
        float(metric[0][0]) * dx * dx
        + 2 * float(metric[0][1]) * dx * dy
        + float(metric[1][1]) * dy * dy
    )
    return math.sqrt(max(0.0, squared))


def svg_path(points: list[Point], mapper: Mapper, close: bool = False) -> str:
    """Convert normalized points to an SVG path through *mapper*."""
    mapped = [mapper(point) for point in points]
    commands = [f"M {mapped[0][0]:.2f} {mapped[0][1]:.2f}"]
    commands.extend(f"L {x:.2f} {y:.2f}" for x, y in mapped[1:])
    if close:
        commands.append("Z")
    return " ".join(commands)


def map_to_panel(point: Point, left: float, top: float, width: float, height: float) -> Point:
    """Map a normalized Cartesian point into an SVG panel coordinate system."""
    return left + point[0] * width, top + (1 - point[1]) * height


def render_coupling_panel(
    out: list[str],
    spec: dict[str, Any],
    matrices: dict[str, list[list[float]]],
    maximum: float,
    panel_x: float,
    motion: float,
) -> None:
    """Append the multilayer coupling-tensor panel."""
    systems = spec["systems"]
    hazards = spec["hazards"]
    mechanisms = spec["mechanisms"]
    base_x = 102.0
    base_y = 286.0
    cell = 45.0

    out.extend(
        [
            svg_text(panel_x + 24, 171, "1  Multilayer coupling tensor", 24, 800),
            svg_text(
                panel_x + 24,
                200,
                "Factorized Cⁱⱼₕₘ = Bⁱⱼ aₕ bₘ",
                16,
                css="small",
            ),
        ]
    )

    shown_hazards = hazards[:3]
    for hazard_index, hazard in enumerate(shown_hazards):
        offset_x = 24 * hazard_index
        offset_y = 78 * hazard_index
        begin = -hazard_index * motion / max(1, len(shown_hazards))
        out.extend(
            [
                '<g opacity=".72">',
                (
                    '<animate attributeName="opacity" values=".58;1;.68;.58" '
                    f'dur="{motion:.1f}s" begin="{begin:.2f}s" repeatCount="indefinite"/>'
                ),
                (
                    f'<rect x="{base_x + offset_x - 8}" y="{base_y + offset_y - 31}" '
                    'width="196" height="220" rx="9" fill="#f2f7f4" stroke="#cfddd5"/>'
                ),
                svg_text(base_x + offset_x, base_y + offset_y - 10, hazard["label"], 16, 700),
            ]
        )
        for row_index, row in enumerate(matrices[hazard["id"]]):
            for column_index, value in enumerate(row):
                out.append(
                    (
                        f'<rect x="{base_x + offset_x + column_index * cell}" '
                        f'y="{base_y + offset_y + row_index * cell}" width="43" height="43" '
                        f'rx="3" fill="{heat(value, maximum)}" stroke="#fff"/>'
                    )
                )
        out.append("</g>")

    for index, system in enumerate(systems):
        out.append(svg_text(base_x + index * cell + cell / 2, 244, system["id"], 15, 700, "middle"))

    out.append(svg_text(panel_x + 313, 265, "Mechanism weights μₘ", 17, 750))
    y = 297.0
    for mechanism in mechanisms:
        out.append(
            svg_text(
                panel_x + 313,
                y,
                f'{mechanism["label"]}: {mechanism["weight"]:.2f}',
                15,
                css="small",
            )
        )
        y += 29

    out.append(svg_text(panel_x + 313, 448, "Hazard intensities ηₕ", 17, 750))
    y = 480.0
    for hazard in hazards:
        out.append(
            svg_text(
                panel_x + 313,
                y,
                f'{hazard["label"]}: {hazard["intensity"]:.2f}',
                15,
                css="small",
            )
        )
        y += 29

    out.extend(
        [
            svg_text(panel_x + 33, 680, "Tensor contraction", 18, 800),
            svg_text(panel_x + 33, 717, "Mⁱⱼ = Σₕ Σₘ Cⁱⱼₕₘ ηʰ μᵐ", 23, css="math"),
            svg_text(
                panel_x + 33,
                750,
                "rⁱ = Mⁱⱼ xʲ  →  scenario-conditioned response",
                18,
                css="math",
            ),
        ]
    )


def render_state_panel(out: list[str], spec: dict[str, Any], panel_x: float) -> None:
    """Append the state-space tensor-geometry panel."""
    left, top, width, height = 693.0, 247.0, 425.0, 395.0
    state = spec["state_space"]
    out.extend(
        [
            svg_text(panel_x + 24, 171, "2  Tensor geometry of state space", 24, 800),
            svg_text(
                panel_x + 24,
                200,
                "Metric ellipsoids encode anisotropic local sensitivity.",
                16,
                css="small",
            ),
            (
                f'<rect x="{left}" y="{top}" width="{width}" height="{height}" '
                'rx="8" fill="#f2f7f4" stroke="#cfddd5"/>'
            ),
        ]
    )

    for index in range(1, 5):
        x = left + index * width / 5
        y = top + index * height / 5
        out.extend(
            [
                f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + height}" '
                'stroke="#dbe6e0"/>',
                f'<line x1="{left}" y1="{y:.1f}" x2="{left + width}" y2="{y:.1f}" '
                'stroke="#dbe6e0"/>',
            ]
        )

    def mapper(point: Point) -> Point:
        return map_to_panel(point, left, top, width, height)

    for sample in state["metric_samples"]:
        center = mapper(tuple(map(float, sample["x"])))
        radius_x, radius_y, angle = ellipse(sample["g"])
        out.extend(
            [
                (
                    f'<ellipse cx="{center[0]:.1f}" cy="{center[1]:.1f}" '
                    f'rx="{radius_x:.1f}" ry="{radius_y:.1f}" '
                    f'transform="rotate({-angle:.2f} {center[0]:.1f} {center[1]:.1f})" '
                    'fill="#e5eff4" stroke="#2c6f91" stroke-width="2.2"/>'
                ),
                f'<circle cx="{center[0]:.1f}" cy="{center[1]:.1f}" r="3.5" fill="#10241b"/>',
            ]
        )

    trajectory = [tuple(map(float, point)) for point in state["trajectory"]]
    out.append(
        (
            f'<path class="trajectory" d="{svg_path(trajectory, mapper)}" fill="none" '
            'stroke="#10241b" stroke-width="3.2" marker-end="url(#a)">'
            '<animate attributeName="stroke-dashoffset" from="0" to="-85" dur="5.5s" '
            'repeatCount="indefinite"/></path>'
        )
    )
    for point in trajectory:
        center = mapper(point)
        out.append(
            f'<circle cx="{center[0]:.1f}" cy="{center[1]:.1f}" r="4.4" fill="#10241b"/>'
        )

    out.extend(
        [
            svg_text(panel_x + 51, 687, "δxᵀ g(x) δx = 1", 22, css="math"),
            svg_text(panel_x + 255, 687, "local metric ellipsoid", 15, css="small"),
            svg_text(
                panel_x + 51,
                722,
                "x(t)  →  anisotropic state-space trajectory",
                18,
                css="math",
            ),
        ]
    )


def render_viability_panel(
    out: list[str],
    spec: dict[str, Any],
    boundary: list[Point],
    current: Point,
    nearest: Point,
    margin: float,
    panel_x: float,
) -> None:
    """Append viability geometry, sampled metric margin, and decision target."""
    left, top, width, height = 1273.0, 247.0, 438.0, 395.0
    viability = spec["viability"]
    out.extend(
        [
            svg_text(panel_x + 24, 171, "3  Viability geometry and decision", 24, 800),
            svg_text(
                panel_x + 24,
                200,
                "Metric distance to the sustainable viability boundary.",
                16,
                css="small",
            ),
            (
                f'<rect x="{left}" y="{top}" width="{width}" height="{height}" '
                'rx="8" fill="#fbefec" stroke="#cfddd5"/>'
            ),
        ]
    )

    def mapper(point: Point) -> Point:
        return map_to_panel(point, left, top, width, height)

    out.extend(
        [
            (
                f'<path d="{svg_path(boundary, mapper, True)}" fill="#e2f0e8" '
                'stroke="#1f6f50" stroke-width="3.2"/>'
            ),
            svg_text(left + 205, top + 102, "V", 34, 800, "middle"),
            svg_text(
                left + 205,
                top + 130,
                "sustainable viability set",
                15,
                anchor="middle",
                css="small",
            ),
        ]
    )

    trajectory = [tuple(map(float, point)) for point in viability["trajectory"]]
    out.append(
        (
            f'<path class="trajectory" d="{svg_path(trajectory, mapper)}" fill="none" '
            'stroke="#10241b" stroke-width="3.2" marker-end="url(#a)">'
            '<animate attributeName="stroke-dashoffset" from="0" to="-85" dur="5.5s" '
            'repeatCount="indefinite"/></path>'
        )
    )
    for point in trajectory:
        center = mapper(point)
        out.append(
            f'<circle cx="{center[0]:.1f}" cy="{center[1]:.1f}" r="4.4" fill="#10241b"/>'
        )

    current_svg = mapper(current)
    nearest_svg = mapper(nearest)
    out.extend(
        [
            (
                f'<line x1="{current_svg[0]:.1f}" y1="{current_svg[1]:.1f}" '
                f'x2="{nearest_svg[0]:.1f}" y2="{nearest_svg[1]:.1f}" '
                'stroke="#a84432" stroke-width="3" stroke-dasharray="7 6"/>'
            ),
            (
                f'<circle cx="{nearest_svg[0]:.1f}" cy="{nearest_svg[1]:.1f}" r="7.5" '
                'fill="#a84432"><animate attributeName="r" values="7.5;9.5;7.5" '
                'dur="2.2s" repeatCount="indefinite"/></circle>'
            ),
            svg_text(panel_x + 37, 687, "ρg(x) ≈ minᵧ∈∂V dG(x,y)", 18, css="math"),
            svg_text(panel_x + 37, 720, f"metric margin ≈ {margin:.4f}", 15, 700),
            svg_text(
                panel_x + 37,
                749,
                f'{viability["boundary_samples"]}-point boundary approximation',
                13,
                css="small",
            ),
            svg_text(panel_x + 315, 687, "Decision", 15, 800),
            svg_text(
                panel_x + 315,
                718,
                viability["decision"]["notation"],
                15,
                css="math",
            ),
            svg_text(panel_x + 315, 748, "maintain / restore V", 13, css="small"),
        ]
    )


def render_pipeline(out: list[str]) -> None:
    """Append the visual computation chain shared by all three panels."""
    labels = [
        ("Tensor coupling", "Cⁱⱼₕₘ"),
        ("Contraction", "Mⁱⱼ"),
        ("Response", "rⁱ"),
        ("Margin", "ρg(x)"),
        ("Intervention", "u*"),
    ]
    x = 35.0
    for index, (label, symbol) in enumerate(labels):
        out.extend(
            [
                (
                    f'<rect x="{x}" y="825" width="286" height="82" rx="14" '
                    'fill="#f2f7f4" stroke="#1f6f50" stroke-width="2"/>'
                ),
                svg_text(x + 143, 856, label, 16, 750, "middle"),
                svg_text(x + 143, 887, symbol, 23, anchor="middle", css="math"),
            ]
        )
        if index < len(labels) - 1:
            out.append(
                f'<line x1="{x + 293}" y1="866" x2="{x + 326}" y2="866" '
                'stroke="#1f6f50" stroke-width="2.5" marker-end="url(#a)"/>'
            )
        x += 334


def scenario_matrix(
    spec: dict[str, Any], matrices: dict[str, list[list[float]]]
) -> list[list[float]]:
    """Return the hazard-intensity-weighted scenario matrix used in provenance."""
    count = len(spec["systems"])
    result = [[0.0] * count for _ in range(count)]
    for hazard in spec["hazards"]:
        matrix = matrices[hazard["id"]]
        for row_index in range(count):
            for column_index in range(count):
                result[row_index][column_index] += (
                    float(hazard["intensity"]) * matrix[row_index][column_index]
                )
    return result


def render(spec: dict[str, Any], source_sha: str) -> tuple[str, dict[str, Any]]:
    """Render SVG and provenance objects from a validated tensor-geometry spec."""
    hazards = spec["hazards"]
    matrices = {hazard["id"]: matrix_for(spec, hazard) for hazard in hazards}
    maximum = max(value for matrix in matrices.values() for row in matrix for value in row)

    viability = spec["viability"]
    boundary = viability_boundary(spec)
    current = tuple(map(float, viability["trajectory"][-1]))
    metric = viability["metric"]
    nearest = min(boundary, key=lambda point: metric_distance(current, point, metric))
    margin = metric_distance(current, nearest, metric)
    width, height = map(int, spec["style"]["canvas"])
    motion = float(spec["style"]["motion_seconds"])

    out = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'role="img" aria-labelledby="title desc" data-figure-id="{spec["figure_id"]}" '
            f'data-source-sha256="{source_sha}">'
        ),
        f'<title id="title">{html.escape(spec["title"])}</title>',
        (
            f'<desc id="desc">{html.escape(spec["subtitle"])}. '
            "Synthetic illustrative values; not empirical estimates.</desc>"
        ),
        (
            '<defs><style>\n'
            'text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#10241b}'
            '.small{fill:#5b6f65}\n'
            '.math{font-family:Georgia,"Times New Roman",serif}'
            '.panel{fill:#fff;stroke:#cfddd5;stroke-width:1.5}\n'
            '.trajectory{stroke-dasharray:9 8}\n'
            '</style><marker id="a" markerWidth="10" markerHeight="10" refX="9" '
            'refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#1f6f50"/>'
            '</marker></defs>'
        ),
        f'<rect width="{width}" height="{height}" fill="#fbfcfa"/>',
        svg_text(width / 2, 48, spec["title"], 37, 800, "middle"),
        svg_text(width / 2, 79, spec["subtitle"], 18, anchor="middle", css="small"),
        svg_text(
            width / 2,
            105,
            (
                "ILLUSTRATIVE_SYNTHETIC • JSON source of visual truth • "
                "no empirical calibration claimed"
            ),
            15,
            anchor="middle",
            css="small",
        ),
    ]

    panel_x = [35.0, 626.0, 1217.0]
    for x in panel_x:
        out.append(f'<rect class="panel" x="{x}" y="132" width="548" height="660" rx="18"/>')

    render_coupling_panel(out, spec, matrices, maximum, panel_x[0], motion)
    render_state_panel(out, spec, panel_x[1])
    render_viability_panel(out, spec, boundary, current, nearest, margin, panel_x[2])
    render_pipeline(out)

    out.extend(
        [
            svg_text(35, 948, spec["claim_boundary"], 14, css="small"),
            svg_text(
                width - 35,
                948,
                f"source SHA-256: {source_sha[:16]}…",
                13,
                anchor="end",
                css="small",
            ),
            "</svg>",
        ]
    )

    scenario = scenario_matrix(spec, matrices)
    provenance = {
        "artifact_class": "JSON_DRIVEN_SVG",
        "claim_boundary": spec["claim_boundary"],
        "communication_impact": "NOT_EVALUATED",
        "derived_quantities": {
            "boundary_samples": viability["boundary_samples"],
            "sampled_metric_margin": round(margin, 8),
            "scenario_matrix": [[round(value, 6) for value in row] for row in scenario],
        },
        "empirical_status": "NOT_EMPIRICALLY_CALIBRATED",
        "evidence_status": spec["evidence_status"],
        "figure_id": spec["figure_id"],
        "renderer": "scripts/render_tensor_geometry.py",
        "source": "art/tensor-geometry/tensor_geometry.json",
        "source_sha256": source_sha,
    }
    return "\n".join(out) + "\n", provenance


def generate(spec_path: Path) -> tuple[str, str]:
    """Generate canonical SVG and provenance strings from one JSON file."""
    source = spec_path.read_bytes()
    spec = load(spec_path)
    svg, provenance = render(spec, hashlib.sha256(source).hexdigest())
    provenance_text = json.dumps(
        provenance,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
    )
    return svg, provenance_text + "\n"


def main() -> int:
    """CLI entrypoint supporting render and fail-closed stale-output checks."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", type=Path, default=SPEC)
    parser.add_argument("--output", type=Path, default=SVG)
    parser.add_argument("--provenance", type=Path, default=PROVENANCE)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        svg, provenance = generate(args.spec)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"FAIL tensor geometry: {error}", file=sys.stderr)
        return 1

    if args.check:
        pairs = ((args.output, svg), (args.provenance, provenance))
        current = all(
            path.is_file() and path.read_text(encoding="utf-8") == expected
            for path, expected in pairs
        )
        message = (
            "PASS tensor geometry generated artifacts are current"
            if current
            else "STALE tensor geometry artifacts"
        )
        print(message)
        return 0 if current else 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.provenance.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8")
    args.provenance.write_text(provenance, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
