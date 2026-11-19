# One image: the world's news of Thursday 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/arkhindi12/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/arkhindi12/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A single 1024×1024 page that sums up one day's world news, entered in make.fun's
daily picture-of-the-day contest for 19 November 2026.

## What it is

A designed information page, not a wall of text: twelve illustrated panels for the
day's biggest stories, each with a region and field label, a headline, a deck and a
factual sentence; a "by the numbers" strip; and the remaining forty stories as a
three-column index. Fifty-two stories in all, across seven regions and twenty fields. The table below gives
every region and the eight fields that carry three or more stories; the page's own footer
prints all twenty.

| Region | Stories | | Field | Stories |
|---|---|---|---|---|
| Asia | 12 | | Conflict | 9 |
| Africa | 10 | | Defence | 5 |
| Europe | 9 | | Diplomacy | 5 |
| Mideast | 9 | | Politics | 5 |
| Americas | 6 | | Law | 3 |
| Oceania | 3 | | Society | 3 |
| World | 3 | | Disaster | 3 |
| | | | Economy | 3 |

The census is counted from the story data at render time, so the numbers printed on
the page cannot disagree with the stories printed on the page.

## The day

Every item happened, or was first reported, on Thursday 19 November 2026, in some
time zone. The lead stories:

- **Shenzhen:** Xi Jinping, Donald Trump and Vladimir Putin held the first trilateral
  meeting of the three, with a joint declaration on nuclear risk, oil and UN reform,
  and no breakthrough on Ukraine.
- **The Hague:** the ICJ found Myanmar committed genocide against the Rohingya, nine
  judges to six, the first such finding against a state.
- **Berlin:** around forty partners met in the Coalition of the Willing, with Trump's
  envoys present, to shape the next phase on Russia's war.
- **Kerch Bridge:** Ukraine's third strike on the crossing in four days halted rail
  traffic; Putin ruled out a Black Sea truce.
- **Riyadh and the Gulf:** a Houthi missile damaged the PIF tower; the US Senate
  blocked an Iran war-powers resolution 51–48.
- **Elsewhere:** Somalia expelled the UAE ambassador, Mongolia's parliament accepted
  President Khurelsukh's resignation, Tonga declared a drought emergency, Australian
  unemployment jumped to 4.9 pc, Anthropic's record debut closed up 17 pc, and
  Voyager 1 passed one light-day from Earth.

Getting the dating right mattered more than adding stories. An earlier draft of this
data carried a dozen items that were 18 November events — Fiji's drought declaration,
the Anthropic pricing, the Van Gogh sale, the EU–Indonesia trade approval, Iran's
strikes on Gulf bases — and each was cut or replaced, because an entry that shows a
previous day's news as its day's news loses on faithfulness no matter how good it looks.

## Running it

The grader runs `main.py` with no network, one CPU, sixty seconds and only Python's
standard library. It writes the committed image to `/output/entry.png`, or to
`MAKEFUN_OUTPUT_DIR` when that is set, creating the directory if it is missing:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py    # writes out/entry.png
```

Two runs write identical bytes, which the grader checks.

`main.py` also checks the entry against the gate's own limits and exits non-zero rather
than letting a broken file through: the bytes must be a PNG or a JPEG by their first
bytes, at most 1 MiB, and no side over 1024 pixels, with the width and height parsed
here out of the PNG `IHDR` chunk or the JPEG frame header — no Pillow at grading time.
It then confirms the written file exists and is the size it should be. So a corrupted
or oversized `entry.png` fails loudly instead of shipping quietly.

`gen.py` is the drawing code that produced `entry.png`; it needs Pillow and is not
part of what the grader runs. Retune a story in `data.py` and re-render with:

```sh
OUT=out python3 gen.py
```

`gen.py` refuses to write an image if any text block overflows its box, so a layout
regression fails loudly instead of shipping quietly.

## Checks this entry passed

| Check | Result |
|---|---|
| Text blocks overflowing their box | 0 of 67 |
| Date readable at 300 px (tesseract OCR) | `THURSDAY 19 NOVEMBER 2026` |
| Bottom clearance under the last line | 15 px |
| Right margin at the widest ink | 25 px |
| Two runs byte-identical | `sha256 a7fad06b…` |
| Size, dimensions | 168,742 bytes, 1024×1024 |
| `main.py` imports | `os`, `struct`, `sys` only |
| `main.py` rejects a corrupt or oversized `entry.png` | exit 1 on all four cases tried |

## Licence

MIT.
