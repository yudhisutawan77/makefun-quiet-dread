#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment.

The program writes a single code review comment to /output/entry.txt.
The comment approves a pull request while carrying quiet existential
dread: it fails silently on a Friday, pages no one until Monday, and
the on-call rotation remembers who approved it.

Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
a single line, not only white space. This program enforces that
itself and exits non-zero if the text ever falls outside the gate.
"""

import os
import sys

ENTRY = (
    "Approved. It fails silently on Friday, pages no one until Monday, "
    "and the on-call rotation will remember my name."
)

MAX_CHARS = 140


def validate(text):
    """Return an error string, or None when the text passes the gate."""
    if not text or not text.strip():
        return "entry is empty or only white space"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(text),
            MAX_CHARS,
        )
    return None


def main():
    error = validate(ENTRY)
    if error:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), out_path))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
