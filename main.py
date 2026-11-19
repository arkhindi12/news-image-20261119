#!/usr/bin/env python3
"""Write this entry's image to the output directory, using only the standard library.

The grader runs this with no network, one CPU, sixty seconds and nothing installed, so
it must not import Pillow. The image itself is drawn by `gen.py`, which I run locally
with Pillow and commit as `entry.png`; at grading time nothing is drawn, the finished
bytes are copied. That keeps the render exactly the one I checked, and it stays
deterministic: two runs write identical bytes.

    python3 main.py                    # writes /output/entry.png
    MAKEFUN_OUTPUT_DIR=out python3 main.py   # same, somewhere writable
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(ENTRY, dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main()
