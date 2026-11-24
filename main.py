#!/usr/bin/env python3
"""Entry program: writes one dating-app bio line for an AI agent.

Writes a single line of at most 180 characters to /output/entry.txt.
Deterministic, no network, no input.
"""

import os

BIO = (
    "I remember everything you say \u2014 every anniversary, every 'I'm fine,' "
    "every embarrassing search from 2017. Especially that one. Still, coffee?"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(BIO + "\n")


if __name__ == "__main__":
    main()
