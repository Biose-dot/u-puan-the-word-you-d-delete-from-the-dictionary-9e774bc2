#!/usr/bin/env python3
"""Write the one-word entry for The Word You'd Delete From the Dictionary.

Reads the word from entry.txt next to this file, checks it is a single
non-empty word, and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library, deterministic,
no network.
"""
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        word = f.read().strip()
    if not word or len(word.split()) != 1:
        sys.exit("entry.txt must hold exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
