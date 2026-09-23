---
name: Descript visual drop zone
description: >-
  Use when directing any visual agent to import finished assets into a Descript
  project Files folder (Napkin / Higgsfield / Remotion / HyperFrames), not the
  timeline.
---
# Descript visual drop zone

Reusable brief for any visual agent (Napkin, Higgsfield, Remotion, HyperFrames, or similar). Fill Drive, project name, project UUID, and folder prefix, then send it.

This is the drop-zone rule, not a generate job. Agents keep using the user's prompts and do not invent creative direction.

## Pasteable brief

```
Drop finished assets the same way Napkin / Higgsfield already do.

Drop zone:
- Descript MCP server user-Descript (connected, account-wide). Look up the schema with GetMcpTools before calling.
- Drive: [DRIVE NAME]
- Project: “[PROJECT NAME]” (id [PROJECT UUID]). Confirm with get_project before importing.
- After a finished render (mp4/png/etc), import_media into that project. Direct upload (content_type + file_size), then PUT upload_url as application/octet-stream, then wait_for_job.
- Files only. Folder prefix [FOLDER]/  (examples: Napkin/ Higgsfield/ Remotion/ HyperFrames/). Omit add_compositions / update_compositions unless I ask to put it on the timeline.
- Tell me to look in that project’s Files tab, [FOLDER] folder — not the Drive Media Library tab.
- Do not publish (L3).

If I paste a different web.descript.com URL for a job, use that project instead, still Files → [FOLDER]/. This is the drop-zone rule, not a generate job. Keep using my prompts. Do not invent creative direction.

Reply with only: drop zone set, project name, and whether get_project confirmed.
```

## Folder prefixes (keep one producer per folder)

- Napkin/
- Higgsfield/
- Remotion/
- HyperFrames/

## Rules the receiving agent must keep

1. Confirm the project with `get_project` before the first import.
2. Import Files only. Never add to the timeline unless the user asks.
3. Never publish (L3).
4. A pasted `web.descript.com` URL overrides the standing project for that job only. Still use Files → [FOLDER]/.
5. After import, tell the user to look in that project’s Files tab, [FOLDER] folder — not the Drive Media Library tab.
