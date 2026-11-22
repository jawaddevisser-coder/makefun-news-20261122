#!/usr/bin/env python3
"""Entry point for make.fun news-image-20261122.

Copies the pre-rendered entry.png (produced by draw_news.py, Pillow,
deterministic) into the output directory the grader provides.
Standard library only; no network; no randomness.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
