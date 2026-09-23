#!/usr/bin/env python3
"""Reconcile card-rail asset promises, the asset manifest, and timeline inventory."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str) -> set[str]:
    return {item.strip() for item in value.replace(";", ",").split(",") if item.strip()}


def reconcile(project: Path) -> list[str]:
    errors: list[str] = []
    rail_path = project / "03 Plan/chapter-card-rail.csv"
    manifest_path = project / "04 Assets/asset-manifest.csv"
    timeline_path = project / "05 Timeline/timeline-inventory.csv"
    for path in (rail_path, manifest_path, timeline_path):
        if not path.is_file():
            errors.append(f"missing {path.relative_to(project)}")
    if errors:
        return errors

    rail_rows = rows(rail_path)
    manifest_rows = rows(manifest_path)
    timeline_rows = rows(timeline_path)
    promised: set[str] = set()
    for row in rail_rows:
        promised.update(split_ids(row.get("asset_ids", "")))
    manifest = {row.get("asset_id", "").strip(): row for row in manifest_rows if row.get("asset_id", "").strip()}
    timeline_ids = {row.get("asset_id", "").strip() for row in timeline_rows if row.get("asset_id", "").strip()}

    for asset_id in sorted(promised - set(manifest)):
        errors.append(f"card rail promises missing manifest asset {asset_id}")
    for asset_id, row in manifest.items():
        status = row.get("status", "")
        if status in {"placed", "verified_in_timeline"} and asset_id not in timeline_ids:
            errors.append(f"{asset_id} is {status} but absent from timeline inventory")
        if status == "verified_in_timeline" and not row.get("timeline_range", "").strip():
            errors.append(f"{asset_id} is verified_in_timeline without timeline_range")
    for asset_id in sorted(timeline_ids - set(manifest)):
        errors.append(f"timeline contains unmanifested asset {asset_id}")

    for row in timeline_rows:
        item = row.get("timeline_item_id", "<unknown>")
        logos = row.get("logo_instances", "").strip()
        if logos and logos != "1":
            errors.append(f"{item} reports {logos} visible logos; expected exactly 1")
        if row.get("music_present", "").strip().lower() == "true":
            errors.append(f"{item} contains music; require explicit project approval")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    errors = reconcile(args.project.expanduser().resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: card rail, asset manifest, and timeline inventory reconcile")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

