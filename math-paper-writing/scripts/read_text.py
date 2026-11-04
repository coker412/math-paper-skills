#!/usr/bin/env python3
"""Read an exact UTF-8 text slice with a bounded output and explicit continuation."""

import argparse
import hashlib
import json
from pathlib import Path
import sys


def read_slice(path, start=0, chars=12000, expected_sha256=None):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if expected_sha256 is not None and digest != expected_sha256:
        raise ValueError("Source changed: restart from the current file, not a stale cursor.")
    source = raw.decode("utf-8")
    if chars < 1 or chars > 24000 or start < 0 or start > len(source):
        raise ValueError("Require 1 <= chars <= 24000 and 0 <= start <= source length.")
    end = min(start + chars, len(source))
    return {
        "path": str(path), "sha256": digest,
        "start": start, "end": end, "total_chars": len(source),
        "next_start": end if end < len(source) else None,
    }, source[start:end]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--start", type=int, default=0, help="Unicode character offset (default 0)")
    parser.add_argument("--chars", type=int, default=12000, help="Maximum payload characters, not tokens")
    parser.add_argument("--sha256", help="Expected source hash when continuing an earlier read")
    args = parser.parse_args()
    try:
        header, body = read_slice(args.path, args.start, args.chars, args.sha256)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f"{exc}\n")
    # Only the first line is metadata; all remaining characters are the exact slice.
    sys.stdout.buffer.write((json.dumps(header, ensure_ascii=False) + "\n" + body).encode("utf-8"))


if __name__ == "__main__":
    main()
