#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt.

Deterministic by design: no clock, no randomness, no network, no input —
the same bytes on every run, so two runs in the grader's sandbox produce
the same file.
"""

import os

LINE = (
    "The only decision this meeting ever makes is to schedule "
    "another meeting; I made the last one: no more meetings."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
