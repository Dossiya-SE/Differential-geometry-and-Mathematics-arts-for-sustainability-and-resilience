from __future__ import annotations

import binascii
import math
import struct
import zlib
from pathlib import Path

WIDTH = 1024
HEIGHT = 1024
OUT = Path(__file__).resolve().parents[1] / "app-icon.png"


def chunk(kind: bytes, data: bytes) -> bytes:
    crc = binascii.crc32(kind + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", crc)


def rgba(x: int, y: int) -> tuple[int, int, int, int]:
    # Deterministic mathematical icon: dark field + curvature-inspired torus ring.
    cx = WIDTH / 2
    cy = HEIGHT / 2
    dx = (x - cx) / WIDTH
    dy = (y - cy) / HEIGHT
    r = math.hypot(dx, dy)

    bg = (7, 15, 29, 255)
    if r > 0.42 or r < 0.17:
        return bg

    # Smooth angular/radial field evokes a curvature-coded manifold.
    theta = math.atan2(dy, dx)
    radial = max(0.0, 1.0 - abs(r - 0.295) / 0.125)
    wave = 0.5 + 0.5 * math.cos(3.0 * theta)
    red = int(38 + 40 * wave * radial)
    green = int(120 + 95 * radial)
    blue = int(170 + 80 * (1.0 - wave) * radial)
    return (min(red, 255), min(green, 255), min(blue, 255), 255)


def build_png() -> bytes:
    rows = []
    for y in range(HEIGHT):
        row = bytearray([0])  # PNG filter type 0: None.
        for x in range(WIDTH):
            row.extend(rgba(x, y))
        rows.append(bytes(row))

    raw = b"".join(rows)
    signature = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 6, 0, 0, 0)
    return signature + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")


def validate_png(data: bytes) -> None:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise RuntimeError("Generated icon does not have a PNG signature")
    if b"IHDR" not in data or b"IDAT" not in data or b"IEND" not in data:
        raise RuntimeError("Generated icon is missing required PNG chunks")


if __name__ == "__main__":
    data = build_png()
    validate_png(data)
    OUT.write_bytes(data)
    print(f"Generated deterministic {WIDTH}x{HEIGHT} RGBA PNG: {OUT}")
    print(f"Bytes: {len(data)}")
