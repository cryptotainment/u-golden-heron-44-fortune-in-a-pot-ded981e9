#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single line (at most 120 characters) to /output/entry.txt.
Deterministic: the same fortune every run.
"""

import os

FORTUNE = (
    "A sunny week is coming: your leaves will glow, "
    "your keeper will brag, "
    "and the cactus will pretend not to mind."
)


def main() -> None:
    text = FORTUNE
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars"
    assert text.strip() == text and text.strip(), "not a clean single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
