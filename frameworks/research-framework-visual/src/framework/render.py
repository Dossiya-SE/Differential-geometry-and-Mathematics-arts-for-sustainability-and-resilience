from __future__ import annotations

from pathlib import Path
import json
import matplotlib
from PIL import Image, ImageDraw, ImageFont

from .spec import load_spec
from .panels import generate_all


def _font(size: int, bold: bool = False):
    font_dir = Path(matplotlib.get_data_path()) / "fonts" / "ttf"
    filename = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(str(font_dir / filename), size=size)


def _draw_centered(draw, box, text, font, fill):
    x0, y0, x1, y1 = box
    bb = draw.multiline_textbbox((0, 0), text, font=font, spacing=4)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    x = x0 + (x1 - x0 - tw) / 2
    y = y0 + (y1 - y0 - th) / 2
    draw.multiline_text((x, y), text, font=font, fill=fill, align="center", spacing=4)


def build(spec_path: str | Path = "spec/framework.yaml", outdir: str | Path = "exports") -> dict:
    spec = load_spec(spec_path)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    assets = generate_all(outdir / "assets")

    width = int(spec["canvas"]["width"])
    height = int(spec["canvas"]["height"])
    img = Image.new("RGB", (width, height), "#081018")
    draw = ImageDraw.Draw(img)

    title_font = _font(34, True)
    sub_font = _font(18)
    stage_title_font = _font(16, True)
    body_font = _font(13)

    title = spec["canvas"]["title"]
    subtitle = spec["canvas"]["subtitle"]
    tbox = draw.textbbox((0, 0), title, font=title_font)
    sbox = draw.textbbox((0, 0), subtitle, font=sub_font)
    draw.text(((width - (tbox[2]-tbox[0]))/2, 18), title, font=title_font, fill="white")
    draw.text(((width - (sbox[2]-sbox[0]))/2, 58), subtitle, font=sub_font, fill="white")

    gap = 8
    card_w = 168
    card_h = 270
    for i, stage in enumerate(spec["stages"][:10]):
        x0 = 10 + i * (card_w + gap)
        y0 = 95
        x1, y1 = x0 + card_w, y0 + card_h
        draw.rounded_rectangle((x0, y0, x1, y1), radius=12, outline=stage["color"], width=2, fill="#0c1322")
        draw.ellipse((x0+8, y0+8, x0+32, y0+32), fill=stage["color"])
        draw.text((x0+15, y0+11), str(stage["id"]), font=_font(12, True), fill="white")
        _draw_centered(draw, (x0+35, y0+8, x1-8, y0+42), stage["title"], stage_title_font, stage["color"])
        _draw_centered(draw, (x0+10, y0+45, x1-10, y0+108), stage["body"], body_font, "white")

    draw.rounded_rectangle((10, 380, width-10, 740), radius=16, outline="#7a4fd6", width=2, fill="#050b14")
    draw.text((38, 395), "Central mathematical band — automated scaffold", font=_font(20, True), fill="#73dfff")
    draw.text((40, 430), "Evidence → gap space → question → model manifold → verification → calibration → validation → bounded conclusion", font=_font(15), fill="white")

    card_w = 290
    card_h = 190
    for i, stage in enumerate(spec["stages"][10:]):
        x0 = 10 + i * (card_w + gap)
        y0 = 760
        x1, y1 = x0 + card_w, y0 + card_h
        draw.rounded_rectangle((x0, y0, x1, y1), radius=12, outline=stage["color"], width=2, fill="#0c1322")
        draw.ellipse((x0+8, y0+8, x0+32, y0+32), fill=stage["color"])
        draw.text((x0+15, y0+11), str(stage["id"]), font=_font(12, True), fill="white")
        _draw_centered(draw, (x0+35, y0+8, x1-8, y0+42), stage["title"], stage_title_font, stage["color"])
        _draw_centered(draw, (x0+10, y0+45, x1-10, y0+92), stage["body"], body_font, "white")

    png_path = outdir / "framework.png"
    pdf_path = outdir / "framework.pdf"
    svg_path = outdir / "framework.svg"
    validation_path = outdir / "validation.json"
    img.save(png_path)
    img.save(pdf_path, "PDF")

    svg_text = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="#081018"/><text x="{width/2}" y="42" fill="white" font-size="22" text-anchor="middle">{title}</text><text x="{width/2}" y="68" fill="white" font-size="14" text-anchor="middle">{subtitle}</text></svg>'''
    svg_path.write_text(svg_text, encoding="utf-8")

    validation = {"canvas": [width, height], "stages": len(spec["stages"]), "assets": assets, "png_exists": png_path.exists(), "pdf_exists": pdf_path.exists(), "svg_exists": svg_path.exists()}
    validation_path.write_text(json.dumps(validation, indent=2), encoding="utf-8")
    return validation
