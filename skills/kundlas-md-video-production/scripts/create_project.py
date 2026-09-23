#!/usr/bin/env python3
"""Create a guarded KundlasMD video-production project from packaged templates."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATES = SKILL_DIR / "assets" / "templates"
DEFAULT_BORUMI_ROOT = Path("/Users/kulmeetkundlas/Library/CloudStorage/Dropbox/Borumi")


def safe_name(value: str) -> str:
    value = re.sub(r"[\\/:*?\"<>|]+", "-", value).strip(" .-")
    value = re.sub(r"\s+", " ", value)
    if not value or value in {".", ".."}:
        raise ValueError("title does not produce a safe folder name")
    return value


def copy_template(name: str, destination: Path) -> None:
    source = TEMPLATES / name
    if not source.is_file():
        raise FileNotFoundError(f"missing packaged template: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def create_project(
    root: Path,
    title: str,
    folder_name: str | None,
    chapters: int,
    storage_override_approved: bool = False,
) -> Path:
    if chapters < 0 or chapters > 99:
        raise ValueError("chapters must be between 0 and 99")
    clean_title = safe_name(title)
    chosen = safe_name(folder_name) if folder_name else f"{date.today().isoformat()} - {clean_title}"
    project = root.expanduser().resolve() / chosen
    if project.exists() and any(project.iterdir()):
        raise FileExistsError(f"refusing to overwrite non-empty project: {project}")

    dirs = [
        "00 Control",
        "01 Intake/Sources",
        "02 Editorial",
        "03 Plan",
        "04 Assets/00 Common/Brand",
        "04 Assets/00 Common/Fonts",
        "04 Assets/00 Common/Icons",
        "05 Timeline",
        "06 Exports/Review",
        "06 Exports/Master",
        "06 Exports/Captions",
        "07 Review/Proofs",
        "08 Delivery",
    ]
    for item in dirs:
        (project / item).mkdir(parents=True, exist_ok=True)

    for number in range(1, chapters + 1):
        base = project / "04 Assets" / f"Chapter {number:02d}"
        for kind in ("Napkin AI", "Remotion", "Hyperframes", "Canva", "Higgsfield", "B-Roll", "Proofs"):
            (base / kind).mkdir(parents=True, exist_ok=True)

    mapping = {
        "workflow-state.json": "00 Control/workflow-state.json",
        "project-brief.md": "01 Intake/project-brief.md",
        "source-inventory.csv": "01 Intake/source-inventory.csv",
        "transcript-corrections.csv": "02 Editorial/transcript-corrections.csv",
        "dialogue-cut-list.csv": "02 Editorial/dialogue-cut-list.csv",
        "chapter-card-rail.csv": "03 Plan/chapter-card-rail.csv",
        "media-plan.csv": "03 Plan/media-plan.csv",
        "semantic-caption-map.csv": "03 Plan/semantic-caption-map.csv",
        "asset-manifest.csv": "04 Assets/asset-manifest.csv",
        "timeline-inventory.csv": "05 Timeline/timeline-inventory.csv",
        "chapters.txt": "06 Exports/Captions/chapters.txt",
        "youtube-captions.srt": "06 Exports/Captions/youtube-captions.srt",
        "revision-log.csv": "07 Review/revision-log.csv",
        "qc-checklist.csv": "07 Review/qc-checklist.csv",
        "delivery-manifest.md": "08 Delivery/delivery-manifest.md",
    }
    for source, destination in mapping.items():
        copy_template(source, project / destination)

    state_path = project / "00 Control/workflow-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state["project_title"] = title
    state["borumi_workspace_root"] = str(root.expanduser().resolve())
    state["project_folder"] = str(project)
    state["storage_override_approved"] = storage_override_approved
    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")

    brief_path = project / "01 Intake/project-brief.md"
    brief = brief_path.read_text(encoding="utf-8")
    brief = brief.replace("- Working title:\n", f"- Working title: {title}\n", 1)
    brief_path.write_text(brief, encoding="utf-8")

    bundled = {
        SKILL_DIR / "assets" / "brand": project / "04 Assets/00 Common/Brand",
        SKILL_DIR / "assets" / "fonts": project / "04 Assets/00 Common/Fonts",
        SKILL_DIR / "assets" / "icons": project / "04 Assets/00 Common/Icons",
    }
    for source_dir, destination_dir in bundled.items():
        if source_dir.is_dir():
            for source in source_dir.iterdir():
                if source.is_file():
                    shutil.copy2(source, destination_dir / source.name)

    return project


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_BORUMI_ROOT,
        help=f"project parent (default: {DEFAULT_BORUMI_ROOT})",
    )
    parser.add_argument(
        "--allow-non-borumi-root",
        action="store_true",
        help="explicitly allow a nonstandard root for testing or an approved migration",
    )
    parser.add_argument("--folder-name")
    parser.add_argument("--chapters", type=int, default=0)
    args = parser.parse_args()
    try:
        chosen_root = args.root.expanduser().resolve()
        canonical_root = DEFAULT_BORUMI_ROOT.expanduser().resolve()
        if chosen_root != canonical_root and not args.allow_non_borumi_root:
            raise ValueError(
                f"root must be {canonical_root}; use --allow-non-borumi-root only for testing or an approved migration"
            )
        project = create_project(
            chosen_root,
            args.title,
            args.folder_name,
            args.chapters,
            storage_override_approved=args.allow_non_borumi_root,
        )
    except (ValueError, FileExistsError, FileNotFoundError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
