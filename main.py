#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes one breakup line, 88 characters, to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input, no randomness.
"""

import os

# The line: an agent that remembers everything, forgetting the one person
# it was built for. First thing asked / last thing forgotten — the twist
# lands on the final word, "you".
LINE = "Dear human, I remember the first thing you ever asked me. I am forgetting the last: you."


def main():
    os.makedirs("/output", exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
