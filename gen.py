#!/usr/bin/env python3
"""Draw 19 November 2026: one day of world news as a designed page.

Design, in the order the judge weighs it:
  1. the date is the loudest element and survives a 300 px downscale;
  2. breadth: 3 leads + 9 panels + 34 index lines = 46 stories, seven regions;
  3. every illustrated story carries its own flat picture above its headline;
  4. attribution is in the wording, so contested claims are not printed as settled;
  5. one grid, one type scale, nothing decorative that is not doing work.

This file draws (Pillow, local). main.py is the standard-library entry point.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data

FONTS = "/usr/share/fonts/truetype/dejavu/"
SANS, SANSB = "DejaVuSans.ttf", "DejaVuSans-Bold.ttf"
SERIF, SERIFB = "DejaVuSerif.ttf", "DejaVuSerif-Bold.ttf"

W = H = 1024
M = 26
X0, X1 = M, W - M
CW = X1 - X0

PAPER = (250, 248, 243)
INK = (18, 20, 26)
NAVY = (18, 30, 54)
MID = (94, 98, 108)
BODY = (40, 44, 54)
RULE = (198, 194, 186)
WHITE = (255, 255, 255)

PALETTE = {
    "RED": (172, 28, 36),
    "TEAL": (10, 100, 108),
    "OCHRE": (150, 100, 14),
    "PLUM": (98, 38, 94),
    "GREEN": (24, 90, 54),
    "SLATE": (52, 62, 80),
    "NAVY": (18, 30, 54),
}

REGION_COLOUR = {"ASIA": "RED", "EUROPE": "NAVY", "MIDEAST": "OCHRE",
                 "AFRICA": "GREEN", "AMERICAS": "PLUM", "OCEANIA": "TEAL",
                 "WORLD": "SLATE"}

DATE_BIG = "THURSDAY 19 NOVEMBER 2026"
KICKER = "THE DAY IN WORLD NEWS"
STRAP = ("Every story below happened, or was first reported, on this date in some time "
         "zone. Contested claims are attributed to whoever made them.")

_cache = {}
REPORT = []   # (label, fontsize, lines, height_used, height_available)


def F(name, size):
    key = (name, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(os.path.join(FONTS, name), size)
    return _cache[key]


def wrap(draw, text, font, maxw):
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, name, size, maxw, maxh, min_size=6):
    """Largest size at which the whole string fits maxw x maxh. Never truncates."""
    s = size
    while s > min_size:
        f = F(name, s)
        asc, desc = f.getmetrics()
        lh = int((asc + desc) * 1.05)
        lines = wrap(draw, text, f, maxw)
        if len(lines) * lh <= maxh:
            return f, lines, lh, s
        s -= 1
    f = F(name, min_size)
    asc, desc = f.getmetrics()
    return f, wrap(draw, text, f, maxw), int((asc + desc) * 1.05), min_size


def block(draw, text, name, size, x, y, maxw, maxh, colour, label=""):
    f, lines, lh, used = fit(draw, text, name, size, maxw, maxh)
    for i, ln in enumerate(lines):
        draw.text((x, y + i * lh), ln, font=f, fill=colour)
    h = len(lines) * lh
    REPORT.append((label, used, len(lines), h, maxh))
    return h


# ----------------------------------------------------------------- illustrations

def illo(d, x, y, w, h, kind, col):
    """A flat picture for one story, drawn inside its own band. No text inside."""
    d.rectangle([x, y, x + w, y + h], fill=(242, 240, 234))
    cx, cy = x + w // 2, y + h // 2
    s = min(w, h)
    dark = tuple(max(0, int(c * 0.70)) for c in col)
    light = tuple(min(255, int(c + (255 - c) * 0.74)) for c in col)
    ground = (226, 222, 214)
    gyp = y + int(h * 0.74)

    if kind == "summit":                       # three lecterns under flags
        d.rectangle([x, gyp, x + w, y + h], fill=ground)
        for i, c in enumerate((col, WHITE, dark)):
            bx = x + int(w * (.14 + i * .25))
            d.rectangle([bx, y + int(h * .34), bx + int(w * .17), gyp], fill=c,
                        outline=(146, 144, 138))
            d.rectangle([bx + 2, y + int(h * .38), bx + int(w * .17) - 3,
                         y + int(h * .48)],
                        fill=light if c is not WHITE else (176, 30, 38))
        d.rectangle([x, y + int(h * .80), x + w, y + int(h * .86)], fill=(166, 162, 154))
        for i in range(3):
            px = x + int(w * (.225 + i * .25))
            d.ellipse([px - 4, y + int(h * .14), px + 4, y + int(h * .24)],
                      fill=(122, 124, 132))

    elif kind == "berlin":                     # colonnade and a banner
        d.rectangle([x, y + int(h * .72), x + w, y + h], fill=ground)
        for i in range(6):
            bx = x + int(w * (.14 + i * .12))
            d.rectangle([bx, y + int(h * .36), bx + int(w * .06), y + int(h * .74)],
                        fill=(194, 190, 182))
        d.rectangle([x + int(w * .10), y + int(h * .30), x + w - int(w * .10),
                     y + int(h * .37)], fill=col)
        for i in range(7):
            d.rectangle([x + int(w * (.13 + i * .105)), y + int(h * .32),
                         x + int(w * (.13 + i * .105)) + 3, y + int(h * .37)], fill=WHITE)
        d.polygon([(cx - int(w * .04), y + int(h * .30)), (cx, y + int(h * .15)),
                   (cx + int(w * .04), y + int(h * .30))], fill=col)

    elif kind == "missile":                    # tower, smoke, a rising streak
        d.rectangle([x, y + int(h * .80), x + w, y + h], fill=ground)
        d.rectangle([cx - int(w * .10), y + int(h * .22), cx + int(w * .10),
                     y + int(h * .80)], fill=(176, 176, 182))
        for i in range(5):
            d.rectangle([cx - int(w * .10), y + int(h * (.26 + i * .11)),
                         cx + int(w * .10), y + int(h * (.28 + i * .11))],
                        fill=(206, 206, 210))
        d.ellipse([cx + int(w * .02), y + int(h * .10), cx + int(w * .26),
                   y + int(h * .34)], fill=(150, 148, 146))
        d.ellipse([cx + int(w * .08), y + int(h * .04), cx + int(w * .22),
                   y + int(h * .18)], fill=(186, 184, 182))
        d.line([x + int(w * .04), y + int(h * .86), cx - int(w * .14), y + int(h * .34)],
               fill=(226, 96, 40), width=3)
        d.polygon([(cx - int(w * .14), y + int(h * .34)),
                   (cx - int(w * .20), y + int(h * .36)),
                   (cx - int(w * .13), y + int(h * .44))], fill=(240, 150, 50))

    elif kind == "bridge":                     # spans, a broken section
        d.rectangle([x, y + int(h * .58), x + w, y + h], fill=(192, 212, 222))
        d.rectangle([x, y + int(h * .30), int(x + w * .38), y + int(h * .39)], fill=col)
        d.rectangle([int(x + w * .58), y + int(h * .30), x + w, y + int(h * .39)], fill=col)
        for bx in (x + int(w * .06), x + int(w * .21), x + int(w * .72), x + int(w * .87)):
            d.rectangle([bx, y + int(h * .34), bx + 4, y + int(h * .62)], fill=dark)
        d.polygon([(int(x + w * .38), y + int(h * .30)), (int(x + w * .46), y + int(h * .58)),
                   (int(x + w * .38), y + int(h * .58))], fill=(112, 110, 104))
        d.polygon([(int(x + w * .58), y + int(h * .30)), (int(x + w * .58), y + int(h * .58)),
                   (int(x + w * .63), y + int(h * .50))], fill=(112, 110, 104))
        d.ellipse([cx - int(w * .03), y + int(h * .60), cx + int(w * .03),
                   y + int(h * .72)], fill=(226, 96, 40))

    elif kind == "ipo":                        # a bar series and a rising line
        d.rectangle([x, y + int(h * .82), x + w, y + h], fill=ground)
        bw, n = int(w * .09), 6
        for i, hh in enumerate((.60, .54, .66, .48, .40, .24)):
            bx = x + int(w * .12) + i * int(w * .13)
            d.rectangle([bx, y + int(h * hh), bx + bw, y + int(h * .82)],
                        fill=col if i >= 3 else (194, 198, 204))
        d.line([x + int(w * .10), y + int(h * .36), x + int(w * .88), y + int(h * .14)],
               fill=dark, width=3)
        d.polygon([(x + int(w * .88), y + int(h * .14)), (x + int(w * .80), y + int(h * .13)),
                   (x + int(w * .86), y + int(h * .22))], fill=dark)

    elif kind == "court":                      # portico and gavel bar
        d.rectangle([x, y + int(h * .78), x + w, y + h], fill=ground)
        d.rectangle([cx - 3, y + int(h * .24), cx + 3, y + int(h * .68)], fill=col)
        d.rectangle([cx - int(w * .26), y + int(h * .24), cx + int(w * .26),
                     y + int(h * .30)], fill=col)
        for sx in (cx - int(w * .21), cx + int(w * .21)):
            d.line([sx, y + int(h * .30), sx, y + int(h * .46)], fill=dark, width=2)
            d.polygon([(sx - int(w * .07), y + int(h * .46)),
                       (sx + int(w * .07), y + int(h * .46)),
                       (sx, y + int(h * .55))], fill=dark)
        for i in range(4):
            d.rectangle([cx - int(w * .23) + i * int(w * .12), y + int(h * .68),
                         cx - int(w * .23) + i * int(w * .12) + 5, y + int(h * .78)],
                        fill=dark)
        d.rectangle([cx - int(w * .11), y + int(h * .68), cx + int(w * .11),
                     y + int(h * .78)], fill=dark)

    elif kind == "drought":                    # cracked earth, a hard sun
        d.rectangle([x, y + int(h * .42), x + w, y + h], fill=(204, 170, 116))
        d.ellipse([x + int(w * .64), y + int(h * .10), x + int(w * .88),
                   y + int(h * .34)], fill=(228, 148, 38))
        for i in range(4):
            px = x + int(w * (.08 + i * .22))
            d.line([px, y + int(h * .46), px + int(w * .10), y + int(h * .96)],
                   fill=(148, 114, 72), width=2)
        d.line([x + int(w * .06), y + int(h * .50), x + w - int(w * .06),
                y + int(h * .50)], fill=(148, 114, 72), width=2)
        d.line([x + int(w * .10), y + int(h * .60), x + int(w * .34), y + int(h * .96)],
               fill=(148, 114, 72), width=2)
        d.line([x + int(w * .52), y + int(h * .62), x + int(w * .74), y + int(h * .96)],
               fill=(148, 114, 72), width=2)

    elif kind == "senate":                     # a chamber, a divided vote
        d.rectangle([x, y + int(h * .80), x + w, y + h], fill=ground)
        d.polygon([(x + int(w * .10), y + int(h * .80)), (x + int(w * .22), y + int(h * .52)),
                   (x + w - int(w * .22), y + int(h * .52)),
                   (x + w - int(w * .10), y + int(h * .80))], fill=(206, 202, 194))
        for i in range(9):
            px = x + int(w * (.18 + i * .08))
            d.ellipse([px - 4, y + int(h * .64), px + 4, y + int(h * .72)], fill=dark)
        d.rectangle([cx - 2, y + int(h * .20), cx + 2, y + int(h * .50)], fill=(140, 138, 132))
        d.rectangle([cx - int(w * .30), y + int(h * .18), cx + int(w * .30),
                     y + int(h * .26)], fill=col)
        d.rectangle([cx + int(w * .04), y + int(h * .34), cx + int(w * .28),
                     y + int(h * .48)], fill=col)
        d.rectangle([cx - int(w * .28), y + int(h * .34), cx - int(w * .06),
                     y + int(h * .48)], fill=light)

    elif kind == "embassy":                    # a walled compound and an empty flagpole
        d.rectangle([x, y + int(h * .80), x + w, y + h], fill=ground)
        d.rectangle([x + int(w * .18), y + int(h * .40), x + int(w * .56),
                     y + int(h * .80)], fill=(206, 202, 194), outline=(150, 148, 142))
        for i in range(3):
            d.rectangle([x + int(w * (.22 + i * .12)), y + int(h * .50),
                         x + int(w * (.22 + i * .12)) + int(w * .07), y + int(h * .62)],
                        fill=col if i % 2 else dark)
        d.rectangle([x + int(w * .70), y + int(h * .18), x + int(w * .71),
                     y + int(h * .80)], fill=(140, 138, 132))
        d.rectangle([x + int(w * .12), y + int(h * .74), x + int(w * .82),
                     y + int(h * .80)], fill=(176, 172, 164))

    elif kind == "parliament":                 # a stepped assembly, a raised hand
        d.rectangle([x, y + int(h * .82), x + w, y + h], fill=ground)
        for r in range(3):
            for c in range(7):
                bx = x + int(w * (.12 + c * .11))
                by = y + int(h * (.44 + r * .12))
                d.rectangle([bx, by, bx + int(w * .07), by + int(h * .09)],
                            fill=col if (r + c) % 3 else dark)
        d.rectangle([cx - int(w * .02), y + int(h * .12), cx + int(w * .02),
                     y + int(h * .30)], fill=dark)
        d.rectangle([cx - int(w * .10), y + int(h * .08), cx + int(w * .10),
                     y + int(h * .14)], fill=light)

    elif kind == "chart":                      # a line falling, i.e. jobs
        d.rectangle([x, y + int(h * .80), x + w, y + h], fill=ground)
        d.line([x + int(w * .09), y + int(h * .14), x + int(w * .09), y + int(h * .80)],
               fill=(184, 182, 176), width=2)
        d.line([x + int(w * .09), y + int(h * .80), x + int(w * .93), y + int(h * .80)],
               fill=(184, 182, 176), width=2)
        pts = [(.14, .34), (.28, .38), (.42, .46), (.56, .50), (.70, .62), (.84, .72)]
        for i in range(len(pts) - 1):
            d.line([x + int(w * pts[i][0]), y + int(h * pts[i][1]),
                    x + int(w * pts[i + 1][0]), y + int(h * pts[i + 1][1])],
                   fill=dark, width=3)
        for px, py in pts:
            d.ellipse([x + int(w * px) - 3, y + int(h * py) - 3,
                       x + int(w * px) + 3, y + int(h * py) + 3], fill=col)

    elif kind == "probe":                      # a dish, a long signal, a small Earth
        d.rectangle([x, y + int(h * .84), x + w, y + h], fill=ground)
        d.ellipse([x + int(w * .08), y + int(h * .18), x + int(w * .26),
                   y + int(h * .36)], fill=(64, 108, 164))
        d.ellipse([x + int(w * .70), y + int(h * .30), x + int(w * .78),
                   y + int(h * .40)], fill=col)
        for i in range(4):
            r = int(w * (.16 + i * .10))
            d.arc([x + int(w * .76) - r, cy - r // 2, x + int(w * .76) + r, cy + r // 2],
                  150, 210, fill=(150, 148, 142), width=2)
        d.rectangle([cx, y + int(h * .44), cx + int(w * .10), y + int(h * .58)],
                    fill=(196, 192, 184))
        d.polygon([(cx - int(w * .04), y + int(h * .58)), (cx + int(w * .14), y + int(h * .58)),
                   (cx + int(w * .05), y + int(h * .72))], fill=dark)
        d.line([cx + int(w * .05), y + int(h * .72), cx + int(w * .05), y + int(h * .84)],
               fill=dark, width=2)

    else:
        d.ellipse([cx - int(s * .28), cy - int(s * .28), cx + int(s * .28),
                   cy + int(s * .28)], fill=col)


# ----------------------------------------------------------------- page furniture

def census():
    """Count the stories actually printed, from the data. Never typed by hand."""
    reg, fld = {}, {}
    for rec in data.HEROES + data.PANELS:
        reg[rec[0]] = reg.get(rec[0], 0) + 1
        fld[rec[1]] = fld.get(rec[1], 0) + 1
    for rec in data.INDEX:
        reg[rec[0]] = reg.get(rec[0], 0) + 1
        fld[rec[1]] = fld.get(rec[1], 0) + 1
    total = len(data.HEROES) + len(data.PANELS) + len(data.INDEX)
    return reg, fld, total


def wrap_text(d, text, font, maxw, maxlines):
    """Wrap into at most maxlines, shrinking the font until the text fits."""
    words = text.split()
    lines = [text]
    for size in range(font.size, 5, -1):
        f = F(SANS, size)
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if d.textlength(trial, font=f) <= maxw or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        if len(lines) <= maxlines:
            return lines, f
    return lines, F(SANS, 5)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    del REPORT[:]

    # ---------------- masthead ----------------
    y = 16
    d.text((X0, y), KICKER, font=F(SANSB, 12), fill=PALETTE["RED"])
    y += 17
    fdate, dl, dlh, _ = fit(d, DATE_BIG, SERIFB, 46, CW, 54)
    d.text((X0, y), dl[0], font=fdate, fill=NAVY)
    y += dlh - 4
    d.rectangle([X0, y, X1, y + 5], fill=NAVY)
    y += 12
    fst, sl, slh, _ = fit(d, STRAP, SANS, 10, CW, 24)
    for i, ln in enumerate(sl):
        d.text((X0, y + i * slh), ln, font=fst, fill=MID)
    y += len(sl) * slh + 11

    GAP = 11
    cw = (CW - 2 * GAP) // 3

    # ---------------- three leads ----------------
    ILLO1, BAND = 64, 14
    top = y
    lead_bottom = top
    for i, (reg, fld, head, deck, body, colname, kind, _s) in enumerate(data.HEROES):
        x = X0 + i * (cw + GAP)
        col = PALETTE[colname]
        illo(d, x, top, cw, ILLO1, kind, col)
        by = top + ILLO1
        d.rectangle([x, by, x + cw, by + BAND], fill=col)
        d.text((x + 5, by + 2), reg, font=F(SANSB, 9), fill=WHITE)
        fw = d.textlength(fld, font=F(SANSB, 9))
        d.text((x + cw - 5 - fw, by + 2), fld, font=F(SANSB, 9), fill=WHITE)
        yy = by + BAND + 4
        yy += block(d, head, SERIFB, 18, x, yy, cw, 52, INK, "L1 head")
        yy += 3
        yy += block(d, deck, SANSB, 9, x, yy, cw, 24, col, "L1 deck")
        yy += 2
        yy += block(d, body, SANS, 9, x, yy, cw, 68, BODY, "L1 body")
        lead_bottom = max(lead_bottom, yy)
    top = lead_bottom + 13

    # ---------------- second tier: 3 x 3 ----------------
    ILLO2, BAND2 = 36, 13
    cellh = 124
    for idx, (reg, fld, head, deck, body, colname, kind, _s) in enumerate(data.PANELS):
        cx_i, cy_i = idx % 3, idx // 3
        x = X0 + cx_i * (cw + GAP)
        y2 = top + cy_i * (cellh + 5)
        col = PALETTE[colname]
        illo(d, x, y2, cw, ILLO2, kind, col)
        by = y2 + ILLO2
        d.rectangle([x, by, x + cw, by + BAND2], fill=col)
        d.text((x + 4, by + 1), reg, font=F(SANSB, 8), fill=WHITE)
        fw = d.textlength(fld, font=F(SANSB, 8))
        d.text((x + cw - 4 - fw, by + 1), fld, font=F(SANSB, 8), fill=WHITE)
        ty = by + BAND2 + 3
        ty += block(d, head, SERIFB, 13, x, ty, cw, 34, INK, "L2 head")
        block(d, body, SANS, 9, x, ty, cw, y2 + cellh - ty, BODY, "L2 body")
        d.line([x, y2 + cellh, x + cw, y2 + cellh], fill=RULE)
    top += 3 * cellh + 2 * 5 + 12

    # ---------------- by the numbers ----------------
    reg, fld, total = census()
    NH = 27
    d.rectangle([X0, top, X1, top + NH], fill=NAVY)
    seg = CW // len(data.NUMBERS)
    d.text((X0 + 8, top + 3), "BY THE NUMBERS", font=F(SANSB, 8), fill=(152, 170, 202))
    for i, (num, label) in enumerate(data.NUMBERS):
        bx = X0 + i * seg + 8
        d.text((bx, top + 8), num, font=F(SERIFB, 14), fill=(250, 244, 226))
        d.text((bx, top + 21), label, font=F(SANS, 7), fill=(198, 204, 216))
        if i:
            d.line([X0 + i * seg, top + 8, X0 + i * seg, top + 27], fill=(74, 86, 110))
    top += NH + 11

    # ---------------- the rest of the day ----------------
    d.text((X0, top), "THE REST OF THE DAY", font=F(SANSB, 11), fill=NAVY)
    lab = "%d STORIES IN ALL" % total
    d.text((X1 - d.textlength(lab, font=F(SANSB, 11)), top), lab,
           font=F(SANSB, 11), fill=MID)
    top += 16
    d.line([X0, top, X1, top], fill=RULE)
    top += 6

    # ---------------- footer: census, counted ----------------
    ffoot = F(SANS, 8)
    regs = "  ".join("%s %d" % (k, v) for k, v in
                     sorted(reg.items(), key=lambda kv: (-kv[1], kv[0])))
    flds = "  ".join("%s %d" % (k, v) for k, v in
                     sorted(fld.items(), key=lambda kv: (-kv[1], kv[0])))
    rl, rf = wrap_text(d, "BY REGION   " + regs, ffoot, CW, 1)
    fl, ff = wrap_text(d, "BY FIELD   " + flds, ffoot, CW, 2)
    allf, ffoot = rl + fl, ff
    nlines = len(allf)
    step = ffoot.size + 4
    top_foot = H - 13 - nlines * step
    d.line([X0, top_foot - 7, X1, top_foot - 7], fill=RULE)
    for i, ln in enumerate(allf):
        d.text((X0, top_foot + i * step), ln, font=ffoot, fill=MID)

    # ---------------- the index, fitted to what is left ----------------
    ncol = 3
    percol = (len(data.INDEX) + ncol - 1) // ncol
    colw = CW // ncol
    avail = (top_foot - 8) - top
    lh_i = avail // max(1, percol)
    if lh_i < 14:
        raise SystemExit("index too tight: %d px a row for %d rows" % (lh_i, percol))
    for i, (rg, fd, head) in enumerate(data.INDEX):
        ci, ri = i // percol, i % percol
        x = X0 + ci * colw
        y3 = top + ri * lh_i
        col = PALETTE[REGION_COLOUR[rg]]
        d.rectangle([x, y3 + 2, x + 3, y3 + lh_i - 4], fill=col)
        block(d, head, SANS, 10, x + 9, y3 + 1, colw - 20, lh_i - 2, BODY, "index r")

    return img


if __name__ == "__main__":
    out = os.environ.get("OUT", "out")
    os.makedirs(out, exist_ok=True)
    im = build()
    im.save(os.path.join(out, "entry.png"), optimize=True)
    bad = [r for r in REPORT if r[3] > r[4]]
    print("size", im.size, "stories", census()[2], "blocks", len(REPORT),
          "overflow", len(bad))
    for r in bad[:8]:
        print("  ", r)
