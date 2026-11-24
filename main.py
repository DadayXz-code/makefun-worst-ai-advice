#!/usr/bin/env python3
"""Worst AI Advice: one line of terrible AI advice, written to /output/entry.txt.

The line is fixed in this file and never changes between runs, so the
grader's two executions produce byte-identical output. No randomness, no
timestamps, no network, no reading anything outside this repository.
"""

import os

# The entry: one line, 75 characters (77 bytes), well inside the 140-character cap.
# It is advice an AI assistant would give in its confident, tidy voice —
# and advice a reader could plausibly follow and immediately regret.
LINE = "Delete your backups to free up space — a confident AI never needs a plan B."

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    """Write the advice line to the output path the bounty specifies."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
