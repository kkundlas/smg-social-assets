# Production workflow and state machine

Use this file as the controlling stage rail. Complete stages sequentially. Never replace a missing deliverable with a verbal claim.

## Contents

- State model
- Stages 1–4: intake and dialogue lock
- Stages 5–9: hook, chapters, planning, and assets
- Stages 10–14: assembly, review, and revisions
- Stages 15–18: QC, delivery, and closeout
- Completion receipt format

## State model

Use only these stage states:

- `not_started`
- `in_progress`
- `completed`
- `needs_significant_decision`
- `blocked_external`

After plan approval, complete a stage, record evidence, report the receipt, and continue automatically. Do not ask for routine consent between stages.

Mark a stage `needs_significant_decision` only for medical ambiguity, materially different retakes, a major creative departure, a paid action, destructive work, publication, privacy risk, or an irreversible external action. Mark `blocked_external` only when missing access or source material prevents safe progress.


## Hard rail

Kulmeet authorized the full run after he names the Descript project. Do not ask for permission between stages.

A stage may move to `completed` only after its quality-check gate in this file has passed and evidence is written down. A failed gate keeps the stage `in_progress`. Repair and re-check. Never advance on a verbal claim.

The completion receipt is a status line, not a consent request. Start the next stage immediately after the gate passes.


## Stage 1 — Intake and source inventory

First create a dedicated folder under `/Users/kulmeetkundlas/Library/CloudStorage/Dropbox/Borumi` named `YYYY-MM-DD - <video title>`. All sources, plans, editable assets, proofs, timeline files, exports, and delivery records for this edit belong inside it. Never work from loose files in the Borumi root or from another video's folder.

Inputs:

- source video and audio;
- transcript or SRT when available;
- user research and vidIQ findings;
- brand assets, fonts, credentials, and reference edits;
- requested destinations and output formats.

Outputs:

- `01 Intake/project-brief.md`;
- source inventory with checksums or stable filenames;
- copied or referenced source files;
- initialized workflow state.

Gate: confirm the project path is a direct child of the Borumi workspace and contains the standard folder tree. Confirm the primary recording, duration, resolution, frame rate, audio tracks, transcript availability, and requested deliverables. Do not infer that a file exists merely because a project contains a placeholder.

Privacy gate: inspect filenames, transcript content, screen recordings, and visible documents for patient-identifiable information. Do not upload or publish protected information. Stop for a significant privacy decision when de-identification cannot be completed safely.

## Stage 2 — Source inspection and transcript normalization

Watch the complete recording and read the complete transcript. Correct obvious transcription errors, names, drug names, units, and punctuation without changing meaning. Mark uncertainty instead of inventing a correction.

Outputs:

- corrected transcript;
- `02 Editorial/transcript-corrections.csv`;
- content outline and notable visual opportunities.

Gate: the corrected transcript is readable, time-referenced, and medically coherent. Confirm known terminology such as `glipizide` rather than retaining phonetic transcription errors.

## Stage 3 — Retakes and false starts

Identify abandoned openings, repeated takes, corrections, duplicated sentences, and incomplete clauses. Keep the strongest complete version of each thought.

Outputs:

- proposed cut list;
- retained-take decisions;
- uncertainty flags.

Gate: every removal begins and ends at a natural sentence or clause boundary, and the retained version contains the complete intended meaning.

## Stage 4 — Pauses, filler, and continuity

Tighten dead air, excessive hesitation, and non-semantic filler after retakes are resolved. Preserve rhetorical emphasis, list pacing, natural breaths, and physician credibility.

Outputs:

- committed dialogue cut list;
- cleaned dialogue timeline;
- continuity audit.

Gate: listen across every cut and inspect picture continuity. Verify grammar, meaning, room tone, breath integrity, and facial motion. Lock dialogue before final timing work.

## Stage 5 — First-30-second hook

Design the opening around the viewer problem, stakes, promise, credibility, and reason to continue. Keep it medically honest. Use faster but controlled visual changes.

Outputs:

- hook card rail;
- opening caption and asset assignments;
- short identity treatment.

Gate: the first 30 seconds establish subject, benefit, and authority without a long credential crawl, artificial background, cropped head, or premature clutter.

## Stage 6 — SEO-informed chapters and micro-scenes

Use the corrected transcript and supplied keyword research. Treat the user's vidIQ research as primary. Supplement only when necessary or requested.

Outputs:

- ordered chapter list;
- chapter timestamps based on the locked dialogue;
- micro-scene breakdown.

Gate: chapters reflect actual content, form a coherent educational arc, and do not promise material absent from the video.

## Stage 7 — Card rail and media plan

Create one card for every micro-scene. Decide presenter mode, asset type, semantic takeaway, and transition before generating assets.

Outputs:

- `03 Plan/chapter-card-rail.csv`;
- `03 Plan/media-plan.csv`;
- initial `04 Assets/asset-manifest.csv`.

Gate: every planned asset has a chapter, purpose, owner tool, presenter mode, and intended timeline range. No arbitrary quotas. List every credit-consuming or paid tool with its planned asset count. Approval of this explicit media plan authorizes those planned generations and intermediate renders; ask again only before exceeding the approved count or introducing a new cost.

## Stage 8 — Asset production

Create assets in chapter order. Reuse the packaged logo, fonts, tokens, layout references, and icon family. Prefer vector or 4K-capable sources.

Outputs:

- Napkin, Remotion, Hyperframes, Canva, Higgsfield, icon, photo, and B-roll assets as planned;
- editable sources when supported;
- local durable exports.

Gate: all required assets exist locally. Temporary download links are not durable assets.

## Stage 9 — Asset inspection and freeze

Inspect every asset at usable resolution. Check content, spelling, layout, logo status, safe zones, brand compliance, and technical properties.

Outputs:

- proof frame for every asset;
- batch contact sheets;
- completed manifest status of `approved`, `repair`, or `rejected`.

Gate: only `approved` assets enter the assembly. Nested assets are logo-free. Text does not overlap or clip. Presenter space is reserved when required.

## Stage 10 — Timeline assembly

Assemble locked dialogue, chapter markers, full-screen graphics, presenter-plus-graphic layouts, B-roll, and transitions in narrative order.

Outputs:

- working Borumi or equivalent timeline;
- timeline inventory mapped to asset IDs;
- single persistent KundlasMD logo.

Gate: every timeline item maps to the card rail, audio stays synchronized, the recorded background remains unchanged, and no music exists unless explicitly approved.

## Stage 11 — Semantic overlays and presenter layouts

Add selected meaning-based overlays rather than continuous transcription. Place presenter layouts intentionally.

Outputs:

- `03 Plan/semantic-caption-map.csv` updated with final timing;
- approved presenter modes and caption positions.

Gate: overlays are complete thoughts, preferably one line, low-middle, readable, and clear of the mouth and player controls. Dense graphics receive the full frame when needed.

## Stage 12 — Rough-cut editorial audit

Watch the complete timeline at normal speed. Compare it with the card rail and transcript.

Check:

- pacing and redundant passages;
- missing or unused planned assets;
- excessive visual density;
- presenter presence and authority;
- chapter clarity and transitions;
- disclaimer, CTA, and end screen.

Gate: no known narrative or layout defect remains before review export.

## Stage 13 — Small review export

Export a phone-playable review copy. Do not force the user to review the archival master.

Gate: the review file plays on an iPhone-class device, retains representative image and audio quality, and has the same edit as the pending master.

## Stage 14 — Revision reconciliation

Enter every comment or screenshot into `07 Review/revision-log.csv`. Treat each marked issue as a potential class-wide defect.

For example, one duplicate logo triggers a full-video duplicate-logo audit; one mouth-covering caption triggers a review of all presenter overlays.

Gate: every revision is marked `completed`, `not_applicable`, or `needs_significant_decision`, with proof.

## Stage 15 — Final QC

Run the full checklist in `references/quality-control.md`. Inspect scene starts, middles, and ends plus a full-program contact sheet. Validate the final timeline inventory.

Gate: editorial, visual, brand, medical, audio, technical, and delivery checks pass.

## Stage 16 — Master and companion deliverables

Create:

- approved 3840×2160 master;
- mobile review copy;
- corrected YouTube SRT;
- chapter timestamp file;
- completed manifests and QC report.

Store the final 4K file in `06 Exports/Master`, not in a temporary render directory or the Borumi root.

Gate: probe dimensions, frame rate, duration, codecs, loudness, and full decode. Confirm no unwanted music or duplicate branding. Confirm the verified master path is inside the current video's `06 Exports/Master` folder.

## Stage 17 — Verified Descript new-project import

Create a new Descript project for this video and upload the verified 4K master from `06 Exports/Master`. Do not reuse an unrelated Descript project. Wait for the import job to report success, then inspect the created project and media record. Upload to any additional destination only when explicitly requested.

Gate: a successful transfer alone is insufficient; verify Descript recognizes the complete media and correct duration. Record the Descript project ID, import job ID, status, and direct link in `08 Delivery/delivery-manifest.md`.

## Stage 18 — Closeout and retrospective

Record final outputs, unresolved limitations, new failure patterns, and any user-approved rule changes. Update the reusable skill only when a finding generalizes beyond one scene.

Gate: the delivery manifest is complete and the project folder contains the durable source-of-truth artifacts.

## Completion receipt format

Use this concise structure without requesting approval:

```text
Step <N> complete — <name>
Produced: <artifacts>
Validated: <checks and evidence>
Non-blocking findings: <none or summary>
Starting Step <N+1>: <name>
```
