#!/usr/bin/env python3
"""Validate a KundlasMD video project through a requested workflow stage."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


VALID_STATES = {"not_started", "in_progress", "completed", "needs_significant_decision", "blocked_external"}
CANONICAL_BORUMI_ROOT = Path("/Users/kulmeetkundlas/Library/CloudStorage/Dropbox/Borumi").resolve()
REQUIRED_FILES = {
    1: ["00 Control/workflow-state.json", "01 Intake/project-brief.md", "01 Intake/source-inventory.csv"],
    2: ["02 Editorial/transcript-corrections.csv"],
    3: ["02 Editorial/dialogue-cut-list.csv"],
    5: ["03 Plan/chapter-card-rail.csv"],
    6: ["06 Exports/Captions/chapters.txt"],
    7: ["03 Plan/media-plan.csv", "04 Assets/asset-manifest.csv"],
    10: ["05 Timeline/timeline-inventory.csv"],
    11: ["03 Plan/semantic-caption-map.csv"],
    14: ["07 Review/revision-log.csv"],
    15: ["07 Review/qc-checklist.csv"],
    16: ["06 Exports/Captions/youtube-captions.srt", "06 Exports/Captions/chapters.txt", "08 Delivery/delivery-manifest.md"],
}
CSV_HEADERS = {
    "01 Intake/source-inventory.csv": {"source_id", "role", "filename", "status"},
    "02 Editorial/transcript-corrections.csv": {"correction_id", "original_text", "corrected_text", "status"},
    "02 Editorial/dialogue-cut-list.csv": {"cut_id", "category", "complete_thought_check", "medical_meaning_check", "status"},
    "03 Plan/chapter-card-rail.csv": {"card_id", "chapter_number", "intended_meaning", "presenter_mode", "asset_ids", "qc_status"},
    "03 Plan/media-plan.csv": {"plan_id", "card_id", "asset_type", "why_this_medium", "status"},
    "03 Plan/semantic-caption-map.csv": {"caption_id", "semantic_text", "position", "mouth_clear", "controls_clear", "status"},
    "04 Assets/asset-manifest.csv": {"asset_id", "source_tool", "proof_path", "logo_status", "status", "timeline_range"},
    "05 Timeline/timeline-inventory.csv": {"timeline_item_id", "asset_id", "logo_instances", "music_present", "verified"},
    "07 Review/revision-log.csv": {"revision_id", "defect_class", "affected_scope", "status", "proof_path"},
    "07 Review/qc-checklist.csv": {"check_id", "category", "requirement", "status", "evidence"},
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def read_manifest_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("- ") and ":" in raw:
            key, value = raw[2:].split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def validate(project: Path, through: int) -> list[str]:
    errors: list[str] = []
    if through < 1 or through > 18:
        return ["--through must be between 1 and 18"]
    state_path = project / "00 Control/workflow-state.json"
    if not state_path.is_file():
        return [f"missing {state_path}"]

    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid workflow state: {exc}"]

    actual_parent = project.parent.resolve()
    recorded_parent = state.get("borumi_workspace_root", "")
    recorded_project = state.get("project_folder", "")
    override = state.get("storage_override_approved") is True
    if actual_parent != CANONICAL_BORUMI_ROOT and not override:
        errors.append(f"project is outside the required Borumi root: {actual_parent}")
    if recorded_parent != str(actual_parent):
        errors.append("workflow state does not record the actual Borumi workspace root")
    if recorded_project != str(project.resolve()):
        errors.append("workflow state does not record the actual video-specific project folder")

    stages = state.get("stages")
    if not isinstance(stages, list) or len(stages) != 18:
        errors.append("workflow state must contain exactly 18 stages")
        stages = []
    seen_numbers: list[int] = []
    for item in stages:
        number = item.get("number")
        status = item.get("status")
        seen_numbers.append(number)
        if status not in VALID_STATES:
            errors.append(f"stage {number} has invalid status {status!r}")
        if number <= through and status != "completed":
            errors.append(f"stage {number} is not completed through requested stage {through}")
        if status == "completed" and not item.get("evidence") and not item.get("not_applicable"):
            errors.append(f"stage {number} is completed without evidence")
        if item.get("not_applicable") and status != "completed":
            errors.append(f"stage {number} is not_applicable but not completed")
    if seen_numbers and seen_numbers != list(range(1, 19)):
        errors.append("workflow stage numbers must be exactly 1 through 18 in order")
    first_gap = next((item.get("number") for item in stages if item.get("status") != "completed"), None)
    if first_gap is not None:
        for item in stages:
            if item.get("number", 0) > first_gap and item.get("status") == "completed":
                errors.append(f"stage {item.get('number')} is completed after incomplete stage {first_gap}")

    for stage, paths in REQUIRED_FILES.items():
        if stage <= through:
            for rel in paths:
                path = project / rel
                if not path.is_file() or path.stat().st_size == 0:
                    errors.append(f"missing or empty required artifact for stage {stage}: {rel}")

    for rel, required in CSV_HEADERS.items():
        path = project / rel
        if path.is_file():
            try:
                headers, _ = read_csv(path)
            except OSError as exc:
                errors.append(f"cannot read {rel}: {exc}")
                continue
            missing = required.difference(headers)
            if missing:
                errors.append(f"{rel} missing columns: {', '.join(sorted(missing))}")

    if through >= 9:
        manifest = project / "04 Assets/asset-manifest.csv"
        if manifest.is_file():
            _, rows = read_csv(manifest)
            for row in rows:
                asset_id = row.get("asset_id", "<unknown>")
                status = row.get("status", "")
                if status in {"approved", "placed", "verified_in_timeline"}:
                    local_export = row.get("local_export", "")
                    proof = row.get("proof_path", "")
                    if not local_export:
                        errors.append(f"{asset_id} is {status} without local_export")
                    if not proof:
                        errors.append(f"{asset_id} is {status} without proof_path")
                    if row.get("logo_status") != "logo_free":
                        errors.append(f"{asset_id} is {status} but not marked logo_free")

    if through >= 15:
        qc_path = project / "07 Review/qc-checklist.csv"
        if qc_path.is_file():
            _, rows = read_csv(qc_path)
            for row in rows:
                if row.get("status") not in {"pass", "not_applicable"}:
                    errors.append(f"QC item {row.get('check_id')} is not passing")
                if not row.get("evidence") and row.get("status") == "pass":
                    errors.append(f"QC item {row.get('check_id')} passes without evidence")

    if through >= 16:
        masters = [p for p in (project / "06 Exports/Master").glob("*") if p.is_file() and p.stat().st_size > 0]
        reviews = [p for p in (project / "06 Exports/Review").glob("*") if p.is_file() and p.stat().st_size > 0]
        if not masters:
            errors.append("stage 16 has no non-empty master file in 06 Exports/Master")
        if not reviews:
            errors.append("stage 16 has no non-empty review file in 06 Exports/Review")
        manifest_path = project / "08 Delivery/delivery-manifest.md"
        if manifest_path.is_file():
            fields = read_manifest_fields(manifest_path)
            required_master = ["Path", "Exact size", "Width × height", "Frame rate", "Video codec", "Decode status", "Checksum"]
            for key in required_master:
                if not fields.get(key):
                    errors.append(f"delivery manifest is missing verified master field: {key}")
            if fields.get("Width × height") not in {"3840×2160", "3840x2160"}:
                errors.append("delivery manifest does not identify the master as 3840×2160")

    if through >= 17:
        stage17 = next((item for item in stages if item.get("number") == 17), {})
        if not stage17.get("not_applicable"):
            manifest_path = project / "08 Delivery/delivery-manifest.md"
            if manifest_path.is_file():
                fields = read_manifest_fields(manifest_path)
                required_import = ["Source 4K master inside video project folder", "Project ID", "Job ID", "Imported duration", "Direct link", "Verified at"]
                for key in required_import:
                    if not fields.get(key):
                        errors.append(f"delivery manifest is missing Descript field: {key}")
                if fields.get("Destination") != "Descript (new project)":
                    errors.append("delivery destination is not recorded as a new Descript project")
                if fields.get("Result status", "").lower() != "success":
                    errors.append("Descript import result status is not success")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--through", type=int, required=True)
    args = parser.parse_args()
    errors = validate(args.project.expanduser().resolve(), args.through)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: project validates through stage {args.through}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
