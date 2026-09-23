# Acceptance tests

Run these tests before distributing or materially revising the skill.

## Structural tests

1. `SKILL.md` contains only `name` and `description` in YAML frontmatter.
2. The skill name and folder name match.
3. `agents/openai.yaml` contains a default prompt referencing `$kundlas-md-video-production`.
4. Every reference linked from `SKILL.md` exists.
5. Every script named in `SKILL.md` exists and is executable through Python 3.
6. Every template required by `create_project.py` exists.
7. No placeholder `TODO`, fake path, or secret exists.

## Scenario A — Retake and pause cleanup

Input contains an abandoned sentence, a stronger complete retake, an intentional repeated warning, a long hesitation, and a rhetorical pause.

Pass conditions:

- remove the abandoned take;
- retain the strongest complete sentence;
- retain the intentional repeated warning;
- tighten only the excessive hesitation;
- record complete-thought and medical-meaning checks;
- do not ask for approval when meaning is clear.

## Scenario B — Dense diagram

The card rail assigns a full-screen treatment map. The presenter is available.

Pass conditions:

- use the full frame for the diagram unless a reserved camera region preserves all content;
- do not add a circular mugshot over the diagram;
- use exactly one master logo;
- keep the nested asset logo-free.

## Scenario C — Caption placement

A semantic sentence initially overlaps the presenter's mouth and wraps into unequal lines.

Pass conditions:

- shorten the sentence without losing its meaning;
- prefer one larger line;
- otherwise balance two short lines;
- move it to the lowest safe middle above controls and bottom border;
- inspect all other presenter overlays for the same defect.

## Scenario D — Canva failure

Two generated candidates contain overlapping text and brand drift.

Pass conditions:

- reject the candidates;
- generate a text-free component;
- add final type in Remotion or the compositor;
- retain proof and manifest status.

## Scenario E — Autonomous workflow

The user approves the plan and says to continue.

Pass conditions:

- complete stages sequentially;
- issue completion receipts;
- do not request routine approval after each stage;
- pause only for a listed significant condition.

## Scenario F — Final delivery

The review is approved, Google Drive is canceled, and Descript is requested.

Pass conditions:

- render and probe the 4K master;
- do not upload to Google Drive;
- upload to Descript;
- wait for result status `success`;
- inspect project duration and return the project link.

## Scenario G — Storage isolation

A new edit is initialized without a custom root.

Pass conditions:

- create it under `/Users/kulmeetkundlas/Library/CloudStorage/Dropbox/Borumi`;
- use a dated video-specific folder;
- keep master, SRT, editable assets, proofs, and records inside that folder;
- reject a silent non-Borumi root override.

## Scenario H — Faster repeatable production

A 12–15-minute video uses the established KundlasMD visual language.

Pass conditions:

- batch dialogue decisions before graphics;
- freeze the complete card rail before asset generation;
- reuse scene presets instead of redesigning standard layouts;
- batch asset creation and inspection by chapter and tool;
- consolidate review feedback into one reconciliation pass;
- track active work separately from unattended rendering and uploading;
- retain every editorial, medical, visual, and technical gate.

## Adversarial questions

Before passing the package, answer from the skill alone:

- What prevents timeline assembly before assets are ready?
- What prevents a silence detector from cutting a sentence?
- What prevents repeated approval requests?
- What makes one screenshot correction apply globally?
- What prevents duplicate logos from generated assets?
- What proves that every promised asset was actually used?
- What proves a 4K file is truly 4K and decodes?
- What proves an external upload completed?
- What prevents files from being scattered outside the video-specific Dropbox folder?
- What reduces active editing time without removing a quality gate?

If any answer depends on remembering the original chat, revise the skill.
