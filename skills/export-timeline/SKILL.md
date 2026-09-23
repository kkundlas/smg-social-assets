---
name: Export timeline
description: >-
  Use when handing a composition to Premiere, Resolve, Final Cut, Pro Tools,
  Logic, Audition, or Reaper.
---
# Export timeline

Interchange file only. Media is never bundled on MCP. Sequences and avatars are not supported. Many effects/animations/scenes drop.

## Steps

1. Warn that the NLE must relink original media. UI timeline export can include media; MCP cannot.
2. Map the app to `format`:
   - Premiere Pro → `premiere`
   - DaVinci Resolve → `davinci_resolve`
   - Final Cut Pro → `fcp`
   - Pro Tools / Logic → `aaf` (set `strip_spaces` for Logic)
   - Adobe Audition → `sesx`
   - Reaper / Samplitude → `edl`
3. `export_timeline` with `project_id`, `format`, optional `composition_id`. Optional: `create_track_per_file` (not `fcp`), `snap_frame_rates` (Premiere/Resolve, default true), `include_markers`.
4. `wait_for_job`. Always show `download_url` and `download_url_expires_at`.

Studio Sound on timeline export is imperfect (tends toward 0% or 100% unless flattened). Captions: FCP and Resolve yes, Premiere no. Markers: FCP/Premiere yes, Resolve no.
