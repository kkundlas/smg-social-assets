---
name: Descript edit via project agent
description: >-
  Use when Underlord should edit or build a project from a natural-language
  prompt (cleanup, captions, clips, translate, script-to-video, “make it like
  X”).
---
# Descript edit via project agent

Underlord is the only MCP edit primitive (`prompt_project_agent`). One-shot — not a chat. Look up the live schema before calling.

## Steps

1. Resolve the target. `list_projects` / `get_project`. Pass `composition_id` (UUID, 5-char short ID, or `https://web.descript.com/{project_id}/{short_id}`) when it is not the first composition.
2. Write a one-shot `prompt`: action + context + constraints (aspect, duration, style, what *not* to change). Official examples: “Add studio sound and captions”; “remove all filler words”; “create a 30-second highlight reel”; “Write a script about X and create a video.”
3. Existing project: `project_id`. Brand-new from a prompt: `project_name` only.
4. Optional `model` only if the user named one. Otherwise omit (`auto`).
5. Call `prompt_project_agent`. Show `project_url` immediately.
6. `wait_for_job` (default up to 300s; re-wait if still running). Surface `progress.label` (e.g. “Editing script”).
7. Report `result.agent_response`, whether the project changed, and credits / media seconds used. `get_project` if new compositions appeared.
8. If they dislike it, point them at UI revert (File → version history, or Underlord undo). Do not publish unless they explicitly say yes.

Drive admin can disable the agent (403). 402 = out of minutes/credits. Cannot edit while a recording is in progress. Review the project in Descript — Underlord can overpromise.
