#!/usr/bin/env python3
"""Write this entry's image to the output directory, using only the standard library.

The grader runs this with no network, one CPU, sixty seconds and nothing installed, so
it must not import Pillow. The image itself is drawn by `gen.py`, which I run locally
with Pillow, and the finished bytes are committed as `entry.png`; at grading time
nothing is drawn and those exact bytes are written out, so two runs cannot differ.

    python3 main.py                          # writes /output/entry.png
    MAKEFUN_OUTPUT_DIR=out python3 main.py   # same, anywhere writable
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = os.path.join(HERE, "entry.png")
NAME = "entry.png"


def out_dir():
    """Where the grader wants the image: MAKEFUN_OUTPUT_DIR, else /output."""
    d = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(d, exist_ok=True)
    return d


def main():
    dest = os.path.join(out_dir(), NAME)
    shutil.copyfile(ENTRY, dest)
    with open(dest, "rb") as fh:
        head = fh.read(8)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    print("wrote", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main()
