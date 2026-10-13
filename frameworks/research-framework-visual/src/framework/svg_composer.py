from __future__ import annotations

from html import escape
from math import sin, cos, pi, exp
import textwrap


def _polyline(points):
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)


def _stage_card(stage, x, y, w, h):
    color = stage["color"]
    oid = stage["object_id"]
    max_chars = max(18, int(w / 6.1))
    lines = textwrap.wrap(stage["body"], width=max_chars)[:7]
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else 14
        tspans.append(f'<tspan x="{x+w/2}" dy="{dy}">{escape(line)}</tspan>')
    body = "".join(tspans)
    return f'''<g id="{escape(oid)}" data-stage="{stage['id']}">
      <rect id="{escape(oid)}.panel" x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#0c1322" stroke="{color}" stroke-width="2"/>
      <circle id="{escape(oid)}.number" cx="{x+18}" cy="{y+18}" r="13" fill="{color}"/>
      <text x="{x+18}" y="{y+22}" text-anchor="middle" class="stage-number">{stage['id']}</text>
      <text id="{escape(oid)}.title" x="{x+w/2}" y="{y+45}" text-anchor="middle" class="stage-title" fill="{color}">{escape(stage['title'])}</text>
      <text id="{escape(oid)}.body" x="{x+w/2}" y="{y+70}" text-anchor="middle" class="stage-body-svg">{body}</text>
    </g>'''


def _mini_science(data, width, height):
    objs = {o["object_id"]: o for o in data["objects"]}
    out = []
    cy = 565

    out.append(f'<g id="evidence.field.visual" transform="translate(215,{cy})">')
    for i, r in enumerate([44, 34, 25, 17, 10]):
        out.append(f'<ellipse cx="0" cy="0" rx="{r*1.4}" ry="{r}" fill="none" stroke="#8d65dd" stroke-width="{1+i*0.25}" opacity="{0.35+i*0.11}"/>')
    out.append('<text x="-50" y="-78" class="gate-title" fill="#8d65dd">Evidence E(z)</text>')
    out.append('</g>')

    vals = objs["gap.vector"]["parameters"]["values"]
    cx, rr = 410, 48
    pts = []
    for i, v in enumerate(vals):
        a = -pi / 2 + 2 * pi * i / len(vals)
        r = rr * v
        pts.append((cx + r * cos(a), cy + r * sin(a)))
    out.append(f'<polygon id="gap.vector.visual" points="{_polyline(pts)}" fill="#2b8cff22" stroke="#42d4e5" stroke-width="1.5"/>')
    out.append(f'<text x="{cx}" y="{cy-78}" text-anchor="middle" class="gate-title" fill="#42d4e5">Gap Space G∈R¹⁵</text>')

    out.append(f'<g id="research.question.visual"><circle cx="535" cy="{cy}" r="10" fill="#ffffff" stroke="#42d4e5" stroke-width="3"/><text x="535" y="{cy-32}" text-anchor="middle" class="gate-title" fill="#42d4e5">Research Q</text></g>')

    out.append('<g id="central.model_manifold">')
    for j in range(14):
        pts = []
        for i in range(90):
            x = 585 + i * 6.2
            phase = j * 0.43
            y = cy + (52 + 3 * j) * sin(i / 13 + phase) * exp(-((i - 45) / 45) ** 2)
            pts.append((x, y))
        color = "#42d4e5" if j % 3 == 0 else "#159357"
        out.append(f'<polyline points="{_polyline(pts)}" fill="none" stroke="{color}" stroke-width="1" opacity="0.75"/>')
    traj = []
    for i in range(100):
        x = 590 + i * 5.4
        y = cy - 52 * sin(i / 21) * exp(-((i - 42) / 46) ** 2)
        traj.append((x, y))
    out.append(f'<polyline id="central.controlled_trajectory" points="{_polyline(traj)}" fill="none" stroke="#ffffff" stroke-width="3"/>')
    out.append(f'<text x="760" y="{cy-92}" class="math-label">ẋ=f(x,u,η,θ,t)</text>')
    out.append(f'<text x="760" y="{cy+105}" class="math-label">g(x,u)≤0 — admissible region</text>')
    out.append('</g>')

    gates = [(1180, "#dfae2d", "Verification", "verification.gate"), (1330, "#e08f2c", "Calibration", "calibration.gate"), (1480, "#e25b37", "Validation", "validation.gate")]
    for gx, color, label, oid in gates:
        out.append(f'<g id="{oid}"><ellipse cx="{gx}" cy="{cy}" rx="32" ry="82" fill="none" stroke="{color}" stroke-width="5"/><text x="{gx}" y="{cy-102}" text-anchor="middle" class="gate-title" fill="{color}">{label}</text></g>')
    out.append(f'<line x1="1040" y1="{cy}" x2="1520" y2="{cy}" stroke="#d7a22a" stroke-width="4"/>')

    cpts = []
    for i in range(80):
        a = 2 * pi * i / 80
        r = 50 * (1 + 0.14 * sin(4 * a) + 0.07 * cos(7 * a))
        cpts.append((1650 + r * cos(a), cy + 0.62 * r * sin(a)))
    d = "M " + _polyline(cpts).replace(" ", " L ") + " Z"
    out.append(f'<path id="conclusion.admissible_region.visual" d="{d}" fill="#56c54733" stroke="#56c547" stroke-width="2"/>')
    out.append(f'<circle cx="1658" cy="{cy-2}" r="4" fill="#ffffff"/><text x="1665" y="{cy-5}" class="math-label">c*</text><text x="1650" y="{cy-88}" text-anchor="middle" class="gate-title" fill="#56c547">Bounded Conclusion</text>')

    vals = objs["sensitivity.vector"]["parameters"]["values"]
    bx = 65
    for i, v in enumerate(vals):
        out.append(f'<rect id="sensitivity.bar.{i}" x="{bx+i*13}" y="1010" width="8" height="{-72*v}" fill="#8554df"/>')

    upper, lower = [], []
    for i in range(50):
        t = i / 49 * 8
        x = 345 + i * 4.7
        mu = 0.55 * sin(0.85 * t) * exp(-0.04 * t)
        sig = 0.10 + 0.035 * t
        upper.append((x, 990 - 58 * (mu + sig)))
        lower.append((x, 990 - 58 * (mu - sig)))
    tube = upper + list(reversed(lower))
    out.append(f'<polygon id="uncertainty.tube.visual" points="{_polyline(tube)}" fill="#3f80ff33" stroke="#3f80ff" stroke-width="1"/>')

    for j, (color, phase, slope) in enumerate([("#ffffff", 0.0, 0.10), ("#36c0b0", 0.28, 0.07), ("#d7a22a", -0.22, 0.12)]):
        pts = []
        for i in range(45):
            t = i / 44 * 6
            x = 640 + i * 4.7
            y = 990 - 35 * (0.5 * sin(t + phase) + slope * t)
            pts.append((x, y))
        out.append(f'<polyline id="comparison.trajectory.{j}" points="{_polyline(pts)}" fill="none" stroke="{color}" stroke-width="1.5"/>')

    out.append('<g id="results.field.visual" transform="translate(1045,975)">')
    for i, (rx, ry, op) in enumerate([(82, 45, 0.25), (66, 36, 0.35), (50, 28, 0.45), (34, 20, 0.60), (18, 11, 0.80)]):
        out.append(f'<ellipse cx="0" cy="0" rx="{rx}" ry="{ry}" fill="none" stroke="#56c547" stroke-width="{1+i*0.25}" opacity="{op}" transform="rotate(-18)"/>')
    out.append('<path d="M -55,28 C -20,10 10,5 55,-25" fill="none" stroke="#ffffff" stroke-width="1.5" marker-end="url(#arrow-white)"/>')
    out.append('</g>')

    out.append('<g id="industrial.implication.visual" class="stage-body-svg"><text x="1245" y="940">Design • Operation</text><text x="1245" y="960">Policy • Management</text><text x="1245" y="980">Risk • Sustainability</text></g>')

    bpts = []
    for i in range(80):
        a = 2 * pi * i / 80
        r = 43 * (1 + 0.14 * sin(4 * a) + 0.07 * cos(7 * a))
        bpts.append((1650 + r * cos(a), 980 + 0.62 * r * sin(a)))
    bd = "M " + _polyline(bpts).replace(" ", " L ") + " Z"
    out.append(f'<path id="conclusion.bottom_region.visual" d="{bd}" fill="#f0504733" stroke="#f05047" stroke-width="2"/>')
    out.append('<circle cx="1658" cy="978" r="4" fill="#ffffff"/><text x="1665" y="975" class="math-label">c*</text>')
    return "\n".join(out)


def compose_svg(request, framework_spec, visual_grammar, data):
    width = int(request["canvas"]["width"])
    height = int(request["canvas"]["height"])
    stages = framework_spec["stages"]
    gap = 8
    top_w = (width - 20 - gap * 9) / 10
    bottom_w = (width - 20 - gap * 5) / 6
    cards = []
    for i, stage in enumerate(stages[:10]):
        cards.append(_stage_card(stage, 10 + i * (top_w + gap), 88, top_w, 260))
    for i, stage in enumerate(stages[10:]):
        cards.append(_stage_card(stage, 10 + i * (bottom_w + gap), 840, bottom_w, 205))
    scientific = _mini_science(data, width, height)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="poster-title poster-desc">
  <title id="poster-title">{escape(request['canvas']['title'])}</title>
  <desc id="poster-desc">Editable mathematical-computational research framework V4. Scientific mini-objects are epistemically classified in research_data.json.</desc>
  <style>
    .title {{ font-family: DejaVu Sans, sans-serif; font-weight: 700; font-size: 30px; fill: #ffffff; }}
    .subtitle {{ font-family: DejaVu Serif, serif; font-style: italic; font-size: 16px; fill: #cfd8e3; }}
    .stage-number {{ font-family: DejaVu Sans, sans-serif; font-weight: 700; font-size: 11px; fill: #ffffff; }}
    .stage-title {{ font-family: DejaVu Sans, sans-serif; font-weight: 700; font-size: 11px; }}
    .stage-body-svg {{ font-family: DejaVu Serif, serif; font-size: 10px; fill: #ffffff; }}
    .gate-title {{ font-family: DejaVu Sans, sans-serif; font-weight: 700; font-size: 10px; }}
    .math-label {{ font-family: DejaVu Serif, serif; font-style: italic; font-size: 12px; fill: #ffffff; }}
  </style>
  <rect id="canvas.background" width="100%" height="100%" fill="#081018"/>
  <text id="poster.title" x="{width/2}" y="38" text-anchor="middle" class="title">{escape(request['canvas']['title'])}</text>
  <text id="poster.subtitle" x="{width/2}" y="64" text-anchor="middle" class="subtitle">{escape(request['canvas']['subtitle'])}</text>
  {''.join(cards)}
  <g id="central.research_manifold"><rect x="10" y="365" width="{width-20}" height="455" rx="16" fill="#050b14" stroke="#7a4fd6" stroke-width="2"/>{scientific}</g>
  <g id="feedback.loop"><path d="M 1650 1060 C 1500 1165, 300 1165, 140 1060" fill="none" stroke="#8058d6" stroke-width="3" marker-end="url(#arrow)"/><text x="900" y="1150" text-anchor="middle" class="subtitle">new evidence → improved models → better decisions → revised questions</text></g>
  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#8058d6"/></marker><marker id="arrow-white" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#ffffff"/></marker></defs>
</svg>'''
