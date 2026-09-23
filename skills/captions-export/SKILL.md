---
name: Captions export
description: >-
  Use when adding on-video captions and/or exporting an SRT. Also for translated
  captions.
---
# Captions export

On-video captions are a layer generated from the script. An SRT is a sidecar subtitle file. They are different.

## Steps

1. **On-video captions:** `prompt_project_agent` with style (font, active-word color, all scenes vs current). `wait_for_job`. Show `project_url`.
2. **Subtitle file:** `export_transcript` with `format=srt` (optional speaker labels). MCP has no VTT.
3. **Translated captions:** Underlord (“translate captions to …”). That creates a **new** composition. Then `get_project` and export SRT from that id. Finish the picture edit first.
4. **Burned-in file, VTT, or YouTube:** UI. Or `publish_project` after an explicit yes (share page / signed MP4).

Do not publish unless they explicitly say yes.
