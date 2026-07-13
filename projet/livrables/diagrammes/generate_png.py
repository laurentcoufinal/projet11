#!/usr/bin/env python3
"""Génère des PNG à partir de descriptions de diagrammes (stdlib uniquement)."""

import struct
import zlib
from pathlib import Path

OUT = Path(__file__).parent


def _chunk(tag: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)


def write_png(path: Path, width: int, height: int, pixels: list) -> None:
    raw = b"".join(
        b"\x00" + b"".join(bytes(c) for pixel in row for c in pixel)
        for row in pixels
    )
    compressed = zlib.compress(raw, 9)
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", compressed) + _chunk(b"IEND", b"")
    path.write_bytes(png)


def rgb(r, g, b):
    return (r, g, b)


def fill(pixels, color):
    return [[color for _ in row] for row in pixels]


def rect(pixels, x1, y1, x2, y2, color, border=None):
    h, w = len(pixels), len(pixels[0])
    for y in range(max(0, y1), min(h, y2)):
        for x in range(max(0, x1), min(w, x2)):
            if border and (x in (x1, x2 - 1) or y in (y1, y2 - 1)):
                pixels[y][x] = border
            else:
                pixels[y][x] = color


def line_h(pixels, y, x1, x2, color):
    for x in range(x1, x2):
        pixels[y][x] = color


def arrow(pixels, x1, y1, x2, y2, color):
    if abs(x2 - x1) >= abs(y2 - y1):
        step = 1 if x2 >= x1 else -1
        for x in range(x1, x2, step):
            pixels[y1][x] = color
        tip = 1 if x2 >= x1 else -1
        for d in range(4):
            if 0 <= y1 - d < len(pixels) and 0 <= x2 - tip * d < len(pixels[0]):
                pixels[y1 - d][x2 - tip * d] = color
            if 0 <= y1 + d < len(pixels) and 0 <= x2 - tip * d < len(pixels[0]):
                pixels[y1 + d][x2 - tip * d] = color
    else:
        step = 1 if y2 >= y1 else -1
        for y in range(y1, y2, step):
            pixels[y][x1] = color


def draw_architecture():
    w, h = 1160, 580
    white, black = rgb(255, 255, 255), rgb(40, 40, 40)
    pres, svc, data = rgb(218, 232, 252), rgb(213, 232, 212), rgb(248, 206, 204)
    box_fe, box_svc, box_db = rgb(255, 242, 204), rgb(225, 213, 231), rgb(255, 230, 204)

    pixels = fill([[white for _ in range(w)] for _ in range(h)], white)

    rect(pixels, 30, 60, w - 30, 175, pres, black)
    rect(pixels, 30, 195, w - 30, 330, svc, black)
    rect(pixels, 30, 350, w - 30, 500, data, black)

    boxes = [
        (180, 95, 360, 155, box_fe, "Front-end"),
        (700, 95, 880, 155, box_fe, "Back-office"),
        (120, 235, 300, 295, box_svc, "Catalogue"),
        (450, 235, 630, 295, box_svc, "Commandes"),
        (780, 235, 960, 295, box_svc, "Stock"),
        (200, 390, 380, 460, box_db, "PostgreSQL"),
        (500, 395, 680, 455, box_db, "Reporting"),
        (800, 395, 980, 455, box_db, "API Paiement"),
    ]
    for x1, y1, x2, y2, c, _ in boxes:
        rect(pixels, x1, y1, x2, y2, c, black)

    arrow(pixels, 270, 155, 210, 235, black)
    arrow(pixels, 270, 155, 540, 235, black)
    arrow(pixels, 790, 155, 210, 235, black)
    arrow(pixels, 790, 155, 540, 235, black)
    arrow(pixels, 790, 155, 870, 235, black)
    arrow(pixels, 210, 295, 290, 390, black)
    arrow(pixels, 540, 295, 290, 390, black)
    arrow(pixels, 870, 295, 290, 390, black)
    arrow(pixels, 540, 295, 870, 295, black)
    arrow(pixels, 540, 295, 890, 395, black)
    arrow(pixels, 290, 460, 590, 425, black)

    line_h(pixels, 540, 30, w - 30, black)
    write_png(OUT / "architecture-composants.png", w, h, pixels)


def draw_flux():
    w, h = 1160, 700
    white, black = rgb(255, 255, 255), rgb(40, 40, 40)
    lanes = [rgb(218, 232, 252), rgb(213, 232, 212), rgb(255, 242, 204), rgb(248, 206, 204)]
    box = rgb(225, 213, 231)

    pixels = fill([[white for _ in range(w)] for _ in range(h)], white)
    y_offsets = [50, 200, 360, 520]
    heights = [130, 130, 130, 130]
    titles = ["Flux1 Client", "Flux2 Stock", "Flux3 Back-office", "Flux4 Reporting"]

    for i, (y0, lh, lane, title) in enumerate(zip(y_offsets, heights, lanes, titles)):
        rect(pixels, 30, y0, w - 30, y0 + lh, lane, black)
        rect(pixels, 50, y0 + 40, 50 + 120, y0 + 100, box, black)

    # Flux 1 boxes
    for x in (220, 400, 580, 760):
        rect(pixels, x, 90, x + 120, 150, box, black)
    arrow(pixels, 170, 120, 220, 120, black)
    arrow(pixels, 170, 120, 400, 120, black)
    arrow(pixels, 520, 120, 580, 120, black)
    arrow(pixels, 520, 120, 760, 120, black)

    # Flux 2
    for x in (200, 420, 640):
        rect(pixels, x, 240, x + 120, 300, box, black)
    arrow(pixels, 320, 270, 420, 270, black)
    arrow(pixels, 540, 270, 640, 270, black)

    # Flux 3
    for x in (80, 300, 520, 740):
        rect(pixels, x, 400, x + 120, 460, box, black)
    arrow(pixels, 200, 430, 300, 430, black)
    arrow(pixels, 200, 430, 520, 430, black)
    arrow(pixels, 200, 430, 740, 430, black)

    # Flux 4
    rect(pixels, 280, 560, 400, 630, box, black)
    rect(pixels, 560, 565, 720, 625, box, black)
    arrow(pixels, 400, 595, 560, 595, black)

    write_png(OUT / "flux-dependances.png", w, h, pixels)


if __name__ == "__main__":
    draw_architecture()
    draw_flux()
    print("PNG générés : architecture-composants.png, flux-dependances.png")
