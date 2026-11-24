#!/usr/bin/env python3
"""One-Liner Laugh Lab entry for @syukuran.

Prompt: the excuse a toaster gives after burning your toast.
This program writes exactly one joke line to /output/entry.txt.

The joke: the burn was no accident. The toaster still remembers a
throwaway "a little darker" from 2019 and has held a grudge ever
since — petty revenge, delivered deadpan.
"""

from pathlib import Path

JOKE = "I burned your toast because you said 'a little darker' once, in 2019 \u2014 and I hold grudges."

OUT_PATH = Path("/output") / "entry.txt"


def check(line: str) -> None:
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} chars, gate needs 1-200")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line with no edge whitespace")
    # Ties on judge win rate break to the smaller text (fewer bytes),
    # so pin the byte size too: 92 bytes for this line.
    if len(line.encode("utf-8")) != 92:
        raise SystemExit("unexpected byte length for the line")


def main() -> None:
    check(JOKE)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(JOKE, encoding="utf-8")
    if OUT_PATH.read_text(encoding="utf-8") != JOKE:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(JOKE)} chars / {len(JOKE.encode('utf-8'))} bytes to {OUT_PATH}")


if __name__ == "__main__":
    main()
