#!/usr/bin/env python3
"""Render 'The World on the Wire' -- a telex / wire-service picture of
Sunday 22 November 2026, for make.fun news-image-20261122.

Deterministic: fixed fonts, fixed layout, no randomness, no network,
no timestamps. Renders entry.png (1024x1024) next to this script.
Run: python3 draw_news.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024

# --- palette: telex paper, typewriter ink, wire red -------------------------
PAPER = (245, 240, 225)   # aged telex paper
PAPER_DARK = (232, 225, 205)
INK = (28, 26, 22)        # near-black typewriter ink
RED = (168, 35, 26)       # wire-service red
MUTED = (107, 101, 90)    # faded ink
RULE = (60, 56, 48)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
F_MONO = os.path.join(FONT_DIR, "DejaVuSansMono.ttf")
F_MONO_B = os.path.join(FONT_DIR, "DejaVuSansMono-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap on pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # faint horizontal telex lines across the sheet
    for y in range(0, H, 8):
        d.line([(28, y), (W - 28, y)], fill=(238, 232, 214), width=1)

    # sprocket holes down both margins (telex tape)
    for y in range(34, H - 20, 34):
        for x in (14, W - 14):
            d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(210, 202, 180),
                      outline=RULE, width=1)

    # ---- masthead ------------------------------------------------------
    f_title = font(F_MONO_B, 56)
    f_sub = font(F_MONO, 19)
    f_no = font(F_MONO_B, 20)

    # small globe, left of the title
    cx, cy, r = 78, 66, 30
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=3)
    d.ellipse([cx - 12, cy - r, cx + 12, cy + r], outline=INK, width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=INK, width=2)
    d.arc([cx - r, cy - 16, cx + r, cy + 16], start=200, end=340,
          fill=INK, width=2)
    d.arc([cx - r, cy - 16, cx + r, cy + 16], start=20, end=160,
          fill=INK, width=2)

    d.text((W // 2, 62), "THE WORLD ON THE WIRE", font=f_title,
           fill=INK, anchor="mm")
    d.text((W // 2, 108), "W I R E   S E R V I C E", font=f_sub,
           fill=MUTED, anchor="mm")
    d.text((W - 44, 62), "No. 326", font=f_no, fill=RED, anchor="rm")

    # double rule under masthead
    d.line([(36, 128), (W - 36, 128)], fill=INK, width=3)
    d.line([(36, 134), (W - 36, 134)], fill=INK, width=1)

    # ---- date band -----------------------------------------------------
    f_date = font(F_MONO_B, 26)
    f_date_r = font(F_MONO, 19)
    d.rectangle([36, 146, W - 36, 190], fill=INK)
    d.text((52, 168), "SUNDAY, 22 NOVEMBER 2026", font=f_date,
           fill=PAPER, anchor="lm")
    d.text((W - 52, 168), "6 STORIES - 4 CONTINENTS", font=f_date_r,
           fill=PAPER, anchor="rm")

    # ---- stories --------------------------------------------------------
    # (tag, dateline, headline, fact, source)
    stories = [
        ("BULLETIN", "ANTALYA, TURKIYE",
         "CLIMATE TALKS STILL WITHOUT A DEAL AS THEY RUN INTO SUNDAY",
         "Nearly 200 nations split on fossil fuels and finance; "
         "no new draft yet.",
         "REUTERS / BBC"),
        ("CRICKET", "WELLINGTON",
         "PANT'S 105* PUTS INDIA 221 AHEAD ON DAY FOUR",
         "India 589/5 in reply to New Zealand's 368 in the first Test.",
         "ESPNCRICINFO"),
        ("MOTOGP", "PORTIMAO",
         "MARQUEZ CAN SEAL THE TITLE TODAY",
         "A top-nine finish at Portimao is enough for an eighth "
         "world title.",
         "THE RACE"),
        ("DIPLOMACY", "NEW DELHI",
         "NEPAL'S NEW PM LANDS IN DELHI FOR FIRST INDIA VISIT",
         "Balendra Shah, in office since March, arrives today; "
         "Modi talks Monday.",
         "BBC"),
        ("SCIENCE", "GLOBAL",
         "AI-ASSISTED RIEMANN PROOF PASSES ITS FIRST BIG CHECK",
         "17m lines of Lean code verified Saturday; scrutiny continues.",
         "WALL STREET JOURNAL"),
        ("WEATHER", "TUPANCIRETA, BRAZIL",
         "SUPERCELL TOWN COUNTS THE COST",
         "3 dead, 5,000+ homes damaged in Rio Grande do Sul; "
         "more storms forecast.",
         "REUTERS"),
    ]

    f_tag = font(F_MONO_B, 17)
    f_head = font(F_MONO_B, 25)
    f_fact = font(F_MONO, 19)
    f_src = font(F_MONO, 15)
    f_num = font(F_MONO_B, 26)

    # lead story box
    y = 206
    lead = stories[0]
    d.rectangle([36, y, W - 36, y + 138], fill=PAPER_DARK, outline=INK,
                width=2)
    d.rectangle([52, y + 14, 52 + 118, y + 42], fill=RED)
    d.text((52 + 59, y + 28), lead[0], font=f_tag, fill=PAPER, anchor="mm")
    d.text((188, y + 28), lead[1], font=f_tag, fill=INK, anchor="lm")
    d.text((W - 52, y + 28), "SOURCE: " + lead[4], font=f_src,
           fill=MUTED, anchor="rm")
    head_lines = wrap(d, lead[2], f_head, W - 36 - 104)
    hy = y + 58
    for line in head_lines:
        d.text((52, hy), line, font=f_head, fill=INK, anchor="lm")
        hy += 30
    d.text((52, y + 118), lead[3], font=f_fact, fill=INK, anchor="lm")

    # remaining stories, one row each
    y = 206 + 138 + 14
    row_h = 108
    for i, st in enumerate(stories[1:], start=2):
        tag, city, head, fact, src = st
        d.rectangle([36, y, 36 + 52, y + 52], outline=INK, width=2)
        d.text((36 + 26, y + 26), "%02d" % i, font=f_num, fill=INK,
               anchor="mm")
        d.text((104, y + 12), tag, font=f_tag, fill=RED, anchor="la")
        d.text((104 + d.textlength(tag, font=f_tag) + 14, y + 12),
               city, font=f_tag, fill=INK, anchor="la")
        head_lines = wrap(d, head, f_head, W - 36 - 104)
        hy = y + 44
        for line in head_lines:
            d.text((104, hy), line, font=f_head, fill=INK, anchor="lm")
            hy += 28
        d.text((104, y + row_h - 16), fact, font=f_fact, fill=INK,
               anchor="lm")
        d.text((W - 52, y + 12), "SOURCE: " + src, font=f_src,
               fill=MUTED, anchor="ra")
        if i < 6:
            d.line([(36, y + row_h + 3), (W - 36, y + row_h + 3)],
                   fill=RULE, width=1)
        y += row_h + 6

    # ---- footer ticker -------------------------------------------------
    fy = y + 2
    d.line([(36, fy), (W - 36, fy)], fill=INK, width=3)
    f_foot = font(F_MONO, 16)
    d.text((W // 2, fy + 18),
           "+++ 22 NOVEMBER 2026 +++ COP31 +++ WELLINGTON +++ PORTIMAO "
           "+++ DELHI +++ RIEMANN +++ BRAZIL +++",
           font=f_foot, fill=MUTED, anchor="mm")
    d.text((W // 2, fy + 40),
           "THE WORLD ON THE WIRE - A WIRE-SERVICE PICTURE OF THE DAY'S NEWS",
           font=f_foot, fill=INK, anchor="mm")

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
