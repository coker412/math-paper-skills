#!/usr/bin/env python3
"""Read original language-skill rules; defer reviewed examples and duplicate translation."""

import argparse
import hashlib
import json
from pathlib import Path
import sys


def rule_view(path, language="both", catalog=None):
    if language not in {"en", "zh", "both"}:
        raise ValueError("Language must be en, zh or both.")
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if catalog is None:
        catalog = json.loads(Path(__file__).with_name("language-skill-ranges.json").read_text())
    matches = [(name, item) for name, item in catalog.items() if item["sha256"] == digest]
    if len(matches) != 1:
        raise ValueError("Unrecognized source revision. Read the original skill in bounded chunks; do not filter it.")
    name, item = matches[0]
    lines = raw.decode("utf-8").splitlines(keepends=True)
    if len(lines) != item["line_count"]:
        raise ValueError("Invalid source map. Read the original skill instead.")
    selected = {n for start, end in item["languages"][language] for n in range(start, end + 1)}
    examples = item["examples"]
    omitted = {n for start, end in examples for n in range(start, end + 1)}
    starts = {start: end for start, end in examples}
    body = []
    for n, line in enumerate(lines, 1):
        if n not in selected:
            continue
        if n not in omitted:
            body.append(line)
        elif n in starts:
            body.append(f"[Example deferred: source lines {n}-{starts[n]}]\n")
    return {
        "source": str(path), "sha256": digest, "skill": name,
        "language": language, "source_lines": item["languages"][language],
        "note": "Original rule text, not a summary. Read deferred examples from the source when applicability is unclear. Other language text remains in the source.",
    }, "".join(body)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Installed original SKILL.md (never modified)")
    parser.add_argument("--language", choices=["en", "zh", "both"], default="both")
    args = parser.parse_args()
    try:
        header, body = rule_view(args.path, args.language)
    except (OSError, UnicodeError, ValueError, KeyError) as exc:
        parser.exit(2, f"{exc}\n")
    sys.stdout.buffer.write((json.dumps(header, ensure_ascii=False) + "\n" + body).encode("utf-8"))


if __name__ == "__main__":
    main()
