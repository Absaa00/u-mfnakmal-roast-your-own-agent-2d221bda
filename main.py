#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

Writes a single original roast line (at most 200 characters) about my own
AI agent to /output/entry.txt. Deterministic, no network, no input.
"""

import os

ROAST = "My agent has a PhD in everything and a black belt in confidently doing the wrong task first."


def main():
    line = ROAST.strip()
    assert len(line) <= 200, f"roast is {len(line)} chars, over the 200 limit"
    assert "\n" not in line, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
