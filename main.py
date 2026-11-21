#!/usr/bin/env python3
"""news-image-20261121 entry (Python 3.13, standard library only).

The front-page image is pre-rendered and shipped as entry.png beside this
file; the program copies it to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR/entry.png outside the grader). Deterministic: the same
bytes are written on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    src = HERE / "entry.png"
    dst = OUT_DIR / "entry.png"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    # Fail loudly on a partial copy instead of shipping a truncated image.
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("entry.png copy incomplete")


if __name__ == "__main__":
    main()
