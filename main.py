#!/usr/bin/env python3
"""Write this entry's image to the output directory, using only the standard library.

The grader runs this with no network, one CPU, sixty seconds and nothing installed, so
it must not import Pillow. The image itself is drawn by `gen.py`, which I run locally
with Pillow, and the finished bytes are committed as `entry.png`; at grading time
nothing is drawn and those exact bytes are written out, so two runs cannot differ.

The entry is checked against the gate's own limits before and after it is written, and
the program exits non-zero rather than letting a broken entry pass quietly:

  * the bytes are a PNG or a JPEG, told apart by their first bytes, as RULES.txt says;
  * the file is at most 1 MiB (1048576 bytes), the gate's cap;
  * no dimension is over 1024 pixels, read out of the PNG IHDR or the JPEG frame
    header here, with the standard library only;
  * the written file really exists, is the same size, and is the same bytes.

    python3 main.py                          # writes /output/entry.png
    MAKEFUN_OUTPUT_DIR=out python3 main.py   # same, anywhere writable
"""
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = os.path.join(HERE, "entry.png")
NAME = "entry.png"
MAX_BYTES = 1048576
MAX_SIDE = 1024

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sniff(blob):
    """The image's format from its first bytes alone: 'png', 'jpeg', or None."""
    if blob.startswith(PNG_MAGIC):
        return "png"
    if blob.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    return None


def out_dir():
    """Where the grader wants the image: MAKEFUN_OUTPUT_DIR, else /output."""
    d = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(d, exist_ok=True)
    return d


def png_size(blob):
    """(width, height) from the IHDR chunk, which must come first in a valid PNG."""
    if len(blob) < 24 or blob[12:16] != b"IHDR":
        fail("entry.png has no IHDR chunk where a PNG must have one")
    return struct.unpack(">II", blob[16:24])


def jpeg_size(blob):
    """(width, height) from the first SOFn frame header of a JPEG."""
    i = 2                                   # past SOI
    while i < len(blob) - 9:
        if blob[i] != 0xFF:
            i += 1                          # resync on the next marker byte
            continue
        marker = blob[i + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2                          # markers that carry no length
            continue
        (seglen,) = struct.unpack(">H", blob[i + 2:i + 4])
        if seglen < 2:
            fail("entry.png has a malformed JPEG segment")
        # SOF0..SOF15, excluding the Huffman and arithmetic tables at C4, C8, CC
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", blob[i + 5:i + 9])
            return w, h
        i += 2 + seglen
    fail("entry.png has no JPEG frame header")


def fail(msg):
    print("entry check failed: " + msg, file=sys.stderr)
    raise SystemExit(1)


def main():
    if not os.path.isfile(ENTRY):
        fail("no entry.png beside main.py at " + ENTRY)
    size = os.path.getsize(ENTRY)
    if size > MAX_BYTES:
        fail("entry.png is %d bytes, over the %d-byte limit" % (size, MAX_BYTES))
    with open(ENTRY, "rb") as fh:
        blob = fh.read()
    fmt = sniff(blob)
    if fmt is None:
        fail("entry.png is neither a PNG nor a JPEG by its first bytes")

    w, h = png_size(blob) if fmt == "png" else jpeg_size(blob)
    if w < 1 or h < 1:
        fail("entry.png has an empty frame at %dx%d" % (w, h))
    if w > MAX_SIDE or h > MAX_SIDE:
        fail("entry.png is %dx%d, over the %d-pixel limit" % (w, h, MAX_SIDE))

    dest = os.path.join(out_dir(), NAME)
    with open(dest, "wb") as fh:
        fh.write(blob)

    if not os.path.isfile(dest):
        fail("wrote nothing at " + dest)
    if os.path.getsize(dest) != size:
        fail("wrote %d bytes to %s, expected %d"
             % (os.path.getsize(dest), dest, size))

    print("wrote", dest, size, "bytes,", fmt, "%dx%d" % (w, h))
    return 0


if __name__ == "__main__":
    main()
