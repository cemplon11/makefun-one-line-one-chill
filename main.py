#!/usr/bin/env python3
"""One Line, One Chill — a single sentence of horror.

Writes one frightening line to /output/entry.txt (falling back to a local
output/ directory when /output is not writable, for local runs).
The line: a routine dental visit turns when the dentist finds a second
set of teeth growing behind the narrator's own — teeth that are already
chewing, and that already know the narrator's name.
"""

import os

LINE = (
    "My dentist went silent, his mirror trembling, and whispered that a "
    "second row of teeth was growing in behind mine \u2014 already chewing, "
    "and it had just said my name in his voice."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
