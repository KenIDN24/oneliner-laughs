#!/usr/bin/env python3
"""One-Liner Laughs — make.fun entry.

Writes one line (the joke) to /output/entry.txt, byte-for-byte,
no trailing newline. Stdlib only, no network.
"""
import os

LINE = "The man in 13A reclined his seat into my lap, and just like that, I was a father."


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"line out of sealed gate 1-200: {len(LINE)} chars")
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single clean line with no surrounding whitespace")
    if "  " in LINE:
        raise SystemExit("line has a double space; economy gate failed")
    if len(LINE.split()) < 3:
        raise SystemExit("line must contain at least 3 words to be a real one-liner joke")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back verification: what we wrote must match the line byte-for-byte.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("read-back mismatch: entry.txt does not equal the line")
    if len(written.encode("utf-8")) != len(LINE):
        raise SystemExit("byte-length mismatch on read-back")


if __name__ == "__main__":
    main()
