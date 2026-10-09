"""Generate deterministic exact-line-inversion static figure MSR-FIG-0002."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "art/shaders/inversion_lab/static.svg"


def render() -> str:
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" '
        'role="img" data-figure-id="MSR-FIG-0002">',
        '<title>Sphere inversion of an orthogonal coordinate grid</title>',
        '<desc>Left: straight horizontal and vertical lines. Right: exact inverted circles '
        'for nonzero grid lines and straight invariant axes, with the excluded center marked. '
        'This is dimensionless geometry, not a physical resilience simulation.</desc>',
        '<defs><clipPath id="left"><rect x="0" y="0" width="480" height="480"/></clipPath>'
        '<clipPath id="right"><rect x="480" y="0" width="480" height="480"/></clipPath></defs>',
        '<rect width="960" height="480" fill="#FFFFFF"/>',
        '<g clip-path="url(#left)" stroke="#87CEFA" stroke-width="1.4" fill="none">',
    ]
    scale = 76
    # Original grid: a fixed 0.5-unit step, in both directions.
    for tick in range(-5, 6):
        x = 240 + (tick * 0.5) * scale
        y = 240 - (tick * 0.5) * scale
        lines.append(f'<path d="M{x:.2f},0 V480 M0,{y:.2f} H480"/>')
    lines += ['</g>', '<g clip-path="url(#right)" stroke="#87CEFA" stroke-width="1.4" fill="none">']
    # Inversion of x=a -> circle centered (1/(2a), 0), radius |1/(2a)|.
    # Inversion of y=b -> circle centered (0,1/(2b)), radius |1/(2b)|.
    for tick in range(-5, 6):
        if tick == 0:
            continue
        a = tick * 0.5
        center = 1 / (2 * a)
        radius = abs(center) * scale
        lines.append(
            f'<circle cx="{720 + center * scale:.5f}" cy="240" r="{radius:.5f}"/>'
        )
        lines.append(
            f'<circle cx="720" cy="{240 - center * scale:.5f}" r="{radius:.5f}"/>'
        )
    lines += [
        '</g>',
        '<g stroke="#007AB4" stroke-width="2" fill="none">',
        '<path d="M240,0 V480 M0,240 H480 M720,0 V480 M480,240 H960"/>',
        '</g>',
        '<g stroke="#00BFFF" stroke-width="2.4" fill="none">',
        f'<circle cx="240" cy="240" r="{scale}"/>',
        f'<circle cx="720" cy="240" r="{scale}"/>',
        '</g>',
        '<path d="M480,0 V480" stroke="#ABB7C4"/>',
        '<circle cx="720" cy="240" r="8" stroke="#52616B" fill="#FFFFFF" '
        'stroke-dasharray="2 3"/>',
        '</svg>',
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        return 0 if OUTPUT.is_file() and OUTPUT.read_text(encoding="utf-8") == expected else 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(expected, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
