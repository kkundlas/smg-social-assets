#!/usr/bin/env python3
"""Probe media with ffprobe and enforce optional delivery expectations."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def fps_value(value: str) -> float:
    try:
        return float(Fraction(value))
    except (ValueError, ZeroDivisionError):
        return 0.0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path)
    parser.add_argument("--expect-width", type=int)
    parser.add_argument("--expect-height", type=int)
    parser.add_argument("--expect-fps", type=float)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    media = args.media.expanduser().resolve()
    if not media.is_file() or media.stat().st_size == 0:
        print(f"ERROR: missing or empty media file: {media}", file=sys.stderr)
        return 1
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        print("ERROR: ffprobe is not installed", file=sys.stderr)
        return 1
    command = [ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(media)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        print(result.stderr.strip() or "ERROR: ffprobe failed", file=sys.stderr)
        return result.returncode
    data = json.loads(result.stdout)
    video = next((stream for stream in data.get("streams", []) if stream.get("codec_type") == "video"), None)
    audio = next((stream for stream in data.get("streams", []) if stream.get("codec_type") == "audio"), None)
    errors: list[str] = []
    if video is None:
        errors.append("no video stream")
    else:
        width = int(video.get("width", 0))
        height = int(video.get("height", 0))
        fps = fps_value(video.get("avg_frame_rate", "0/1"))
        if args.expect_width is not None and width != args.expect_width:
            errors.append(f"width {width} != expected {args.expect_width}")
        if args.expect_height is not None and height != args.expect_height:
            errors.append(f"height {height} != expected {args.expect_height}")
        if args.expect_fps is not None and abs(fps - args.expect_fps) > 0.02:
            errors.append(f"fps {fps:.3f} != expected {args.expect_fps:.3f}")
    summary = {
        "path": str(media),
        "size_bytes": media.stat().st_size,
        "duration_seconds": float(data.get("format", {}).get("duration", 0) or 0),
        "video": None if video is None else {
            "codec": video.get("codec_name"),
            "width": video.get("width"),
            "height": video.get("height"),
            "fps": fps_value(video.get("avg_frame_rate", "0/1")),
            "pixel_format": video.get("pix_fmt"),
        },
        "audio": None if audio is None else {
            "codec": audio.get("codec_name"),
            "sample_rate": audio.get("sample_rate"),
            "channels": audio.get("channels"),
        },
    }
    print(json.dumps(summary, indent=2) if args.json else f"MEDIA: {summary}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

