#!/usr/bin/env python3
"""Validate basic SRT numbering, timestamp order, overlaps, and readable blocks."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TIME_RE = re.compile(r"^(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})$")


def milliseconds(parts: tuple[str, ...]) -> int:
    h, m, s, ms = map(int, parts)
    return ((h * 60 + m) * 60 + s) * 1000 + ms


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8-sig").strip()
    blocks = re.split(r"\n\s*\n", text) if text else []
    previous_end = -1
    for expected, block in enumerate(blocks, start=1):
        lines = [line.rstrip() for line in block.splitlines()]
        if len(lines) < 3:
            errors.append(f"block {expected} has fewer than three lines")
            continue
        try:
            number = int(lines[0])
        except ValueError:
            errors.append(f"block {expected} has invalid sequence number")
            continue
        if number != expected:
            errors.append(f"block {expected} is numbered {number}")
        match = TIME_RE.match(lines[1])
        if not match:
            errors.append(f"block {expected} has invalid timestamp syntax")
            continue
        start = milliseconds(match.groups()[:4])
        end = milliseconds(match.groups()[4:])
        if start >= end:
            errors.append(f"block {expected} has non-positive duration")
        if start < previous_end:
            errors.append(f"block {expected} overlaps the previous block")
        previous_end = end
        caption_lines = lines[2:]
        if any(len(line) > 84 for line in caption_lines):
            errors.append(f"block {expected} contains a line longer than 84 characters")
        if len(caption_lines) > 2:
            errors.append(f"block {expected} contains more than two text lines")
    if not blocks:
        errors.append("SRT contains no caption blocks")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("srt", type=Path)
    args = parser.parse_args()
    try:
        errors = validate(args.srt.expanduser().resolve())
    except OSError as exc:
        print(f"ERROR: {exc}")
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: SRT structure and timing validate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

