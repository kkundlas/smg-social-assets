#!/usr/bin/env python3
"""Run deterministic package and workflow regression tests without external services."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPTS = SKILL_DIR / "scripts"


def run(*args: str, expect: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run([sys.executable, *args], capture_output=True, text=True)
    if result.returncode != expect:
        raise AssertionError(
            f"command returned {result.returncode}, expected {expect}: {' '.join(args)}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open(newline="", encoding="utf-8") as handle:
        headers = next(csv.reader(handle))
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    required = [
        "SKILL.md",
        "agents/openai.yaml",
        "references/workflow.md",
        "references/dialogue-editing.md",
        "references/card-rail-and-assets.md",
        "references/brand-layout.md",
        "references/tool-routing.md",
        "references/quality-control.md",
        "references/delivery.md",
        "references/project-storage.md",
        "references/efficient-production.md",
        "references/examples.md",
        "references/acceptance-tests.md",
        "assets/templates/workflow-state.json",
        "scripts/create_project.py",
        "scripts/validate_project.py",
        "scripts/reconcile_assets.py",
        "scripts/validate_srt.py",
        "scripts/probe_media.py",
    ]
    missing = [item for item in required if not (SKILL_DIR / item).is_file()]
    if missing:
        raise AssertionError(f"missing packaged files: {missing}")
    skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    if "TODO" in skill_text or "[TODO" in skill_text:
        raise AssertionError("SKILL.md contains an unfinished placeholder")
    if "$kundlas-md-video-production" not in (SKILL_DIR / "agents/openai.yaml").read_text(encoding="utf-8"):
        raise AssertionError("openai.yaml default prompt does not invoke the skill")

    with tempfile.TemporaryDirectory(prefix="kundlas-video-skill-test-") as temp:
        root = Path(temp)
        run(
            str(SCRIPTS / "create_project.py"),
            "--title", "Rejected Root Test",
            "--root", str(root),
            "--folder-name", "rejected-root",
            expect=1,
        )
        created = run(
            str(SCRIPTS / "create_project.py"),
            "--title", "Self Test Video",
            "--root", str(root),
            "--allow-non-borumi-root",
            "--folder-name", "self-test",
            "--chapters", "2",
        )
        project = Path(created.stdout.strip())
        if not project.is_dir():
            raise AssertionError("create_project did not create its reported directory")
        if project.parent != root.resolve():
            raise AssertionError("create_project did not isolate the video under the requested parent")
        state = json.loads((project / "00 Control/workflow-state.json").read_text(encoding="utf-8"))
        if not state.get("storage_override_approved"):
            raise AssertionError("non-Borumi self-test root was not explicitly recorded as approved")
        if not (project / "04 Assets/Chapter 02/Hyperframes").is_dir():
            raise AssertionError("chapter asset tree is incomplete")
        if not (project / "04 Assets/00 Common/Brand/kundlas-md-logo.png").is_file():
            raise AssertionError("official logo was not copied into the project")
        if len(list((project / "04 Assets/00 Common/Fonts").glob("*.ttf"))) != 4:
            raise AssertionError("the complete packaged font set was not copied")
        if len(list((project / "04 Assets/00 Common/Icons").glob("*.svg"))) != 28:
            raise AssertionError("the complete packaged icon set was not copied")

        state_path = project / "00 Control/workflow-state.json"
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["plan_approved"] = True
        state["stages"][0]["status"] = "completed"
        state["stages"][0]["evidence"] = ["01 Intake/project-brief.md", "01 Intake/source-inventory.csv"]
        state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        run(str(SCRIPTS / "validate_project.py"), str(project), "--through", "1")

        state["stages"][0]["status"] = "not_started"
        state["stages"][1]["status"] = "completed"
        state["stages"][1]["evidence"] = ["02 Editorial/transcript-corrections.csv"]
        state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        run(str(SCRIPTS / "validate_project.py"), str(project), "--through", "2", expect=1)

        srt = project / "06 Exports/Captions/youtube-captions.srt"
        run(str(SCRIPTS / "validate_srt.py"), str(srt))
        srt.write_text("1\n00:00:02,000 --> 00:00:01,000\nBad timing.\n", encoding="utf-8")
        run(str(SCRIPTS / "validate_srt.py"), str(srt), expect=1)

        write_rows(project / "03 Plan/chapter-card-rail.csv", [{
            "card_id": "C01-M01", "chapter_number": "1", "chapter_title": "Test", "micro_scene_number": "1",
            "source_in": "0", "source_out": "5", "edited_in": "0", "edited_out": "5", "transcript_anchor": "Test",
            "intended_meaning": "Test meaning", "viewer_takeaway": "Test takeaway", "presenter_mode": "graphic_full",
            "visual_treatment": "diagram", "asset_ids": "RM-001", "semantic_overlay_id": "", "logo_owner": "final_compositor",
            "transition": "cut", "estimated_duration": "5", "actual_duration": "5", "production_status": "completed",
            "qc_status": "pass", "evidence_path": "proof.png", "notes": ""
        }])
        write_rows(project / "04 Assets/asset-manifest.csv", [{
            "asset_id": "RM-001", "chapter_number": "1", "card_id": "C01-M01", "source_tool": "Remotion",
            "purpose": "Test", "filename": "rm-001.mp4", "editable_source": "src", "local_export": "rm-001.mp4",
            "proof_path": "proof.png", "duration_seconds": "5", "width": "3840", "height": "2160",
            "has_embedded_text": "false", "logo_status": "logo_free", "presenter_space": "not_required",
            "status": "verified_in_timeline", "timeline_range": "00:00-00:05", "provenance_or_license": "owned", "notes": ""
        }])
        write_rows(project / "05 Timeline/timeline-inventory.csv", [{
            "timeline_item_id": "TL-001", "card_id": "C01-M01", "asset_id": "RM-001", "track_type": "overlay",
            "timeline_in": "00:00", "timeline_out": "00:05", "presenter_mode": "graphic_full", "logo_instances": "1",
            "music_present": "false", "verified": "true", "proof_path": "proof.png", "notes": ""
        }])
        run(str(SCRIPTS / "reconcile_assets.py"), str(project))

        delivery_created = run(
            str(SCRIPTS / "create_project.py"),
            "--title", "Delivery Test",
            "--root", str(root),
            "--allow-non-borumi-root",
            "--folder-name", "delivery-test",
        )
        delivery_project = Path(delivery_created.stdout.strip())
        delivery_state_path = delivery_project / "00 Control/workflow-state.json"
        delivery_state = json.loads(delivery_state_path.read_text(encoding="utf-8"))
        for item in delivery_state["stages"]:
            if item["number"] <= 17:
                item["status"] = "completed"
                item["evidence"] = ["self-test"]
        delivery_state_path.write_text(json.dumps(delivery_state, indent=2) + "\n", encoding="utf-8")

        qc_path = delivery_project / "07 Review/qc-checklist.csv"
        headers, qc_rows = read_rows(qc_path)
        for row in qc_rows:
            row["status"] = "pass"
            row["evidence"] = "self-test"
        with qc_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(qc_rows)

        master = delivery_project / "06 Exports/Master/delivery-test-FINAL-4K.mp4"
        review = delivery_project / "06 Exports/Review/delivery-test-REVIEW.mp4"
        master.write_bytes(b"self-test-master")
        review.write_bytes(b"self-test-review")
        manifest_path = delivery_project / "08 Delivery/delivery-manifest.md"
        manifest = manifest_path.read_text(encoding="utf-8")
        replacements = {
            "- Path:\n": f"- Path: {master}\n",
            "- Exact size:\n": f"- Exact size: {master.stat().st_size}\n",
            "- Width × height:\n": "- Width × height: 3840×2160\n",
            "- Frame rate:\n": "- Frame rate: 30\n",
            "- Video codec:\n": "- Video codec: h264\n",
            "- Decode status:\n": "- Decode status: pass\n",
            "- Checksum:\n": "- Checksum: self-test\n",
            "- Source 4K master inside video project folder:\n": f"- Source 4K master inside video project folder: {master}\n",
            "- Project ID:\n": "- Project ID: self-test-project\n",
            "- Job ID:\n": "- Job ID: self-test-job\n",
            "- Result status:\n": "- Result status: success\n",
            "- Imported duration:\n": "- Imported duration: 00:01\n",
            "- Direct link:\n": "- Direct link: https://example.invalid/self-test\n",
            "- Verified at:\n": "- Verified at: 2026-01-01T00:00:00Z\n",
        }
        for old, new in replacements.items():
            manifest = manifest.replace(old, new)
        manifest_path.write_text(manifest, encoding="utf-8")
        run(str(SCRIPTS / "validate_project.py"), str(delivery_project), "--through", "17")

        manifest_path.write_text(
            manifest.replace("- Result status: success", "- Result status: waiting"),
            encoding="utf-8",
        )
        run(str(SCRIPTS / "validate_project.py"), str(delivery_project), "--through", "17", expect=1)

    print("PASS: structure, storage isolation, stage gates, SRT, asset reconciliation, 4K records, and Descript verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
