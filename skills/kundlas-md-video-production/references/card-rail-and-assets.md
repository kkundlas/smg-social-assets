# Chapter card rail and asset-first production

The chapter card rail is the controlling editorial document. It connects the locked transcript to every visual, caption, presenter decision, and QC result.

## Contents

- Chapter and micro-scene planning
- Required card fields
- Presenter modes
- Visual treatment selection
- Media-plan questions
- Stable asset IDs
- Asset lifecycle
- Project structure
- Freeze gate

## Build chapters first

Derive chapters from the actual argument of the corrected transcript. Use supplied keyword or vidIQ research first; supplement only when necessary. Do not force keywords into misleading titles.

Break every chapter into micro-scenes. A micro-scene is one viewer-understandable idea, not an arbitrary time slice.

Use visual rhythm inspired by polished educational creators: vary between presenter, semantic text, icons, diagrams, and supporting media when meaning changes. Do not copy another creator's branding or force a cut every few seconds. As a planning heuristic, look for a meaningful visual development roughly every 20–40 seconds in long-form talking-head sections, then adjust to the content.

## Overlay dwell (locked 2026-08-23)

Remotion and Hyperframes assets must dwell, not flash. Plan fewer, longer cards.

- `captions`: 2.5–4s or the full spoken phrase, whichever is longer
- `text` / `chapter` / `speaker` / `intro`: 5s minimum
- `list` / `paragraph` / `quote` / `bigfact` and Hyperframes diagrams: 6–8s minimum, or until the spoken idea finishes
- Hold through the idea. Do not cut a graphic just because the next micro-scene starts.

## Required card fields

Each card must contain:

- stable card ID;
- chapter and micro-scene order;
- source and edited time range;
- transcript anchor;
- intended meaning;
- viewer takeaway;
- presenter mode;
- visual treatment;
- asset IDs;
- semantic overlay ID;
- logo owner;
- transition;
- estimated and actual duration;
- production and QC status;
- evidence path and notes.

## Presenter modes

Use one of these values:

- `presenter_full`
- `presenter_rect_left`
- `presenter_rect_right`
- `presenter_circle_exception`
- `graphic_full`
- `broll_full`
- `split_no_presenter`

Use `presenter_circle_exception` sparingly and document why the circle does not cover useful content. Do not paste a circular mugshot over a dense diagram.

## Visual treatment selection

Choose the least complicated medium that explains the idea well:

- talking head for trust, interpretation, personal experience, and nuanced advice;
- semantic text for one memorable complete takeaway;
- icon sequence for short categories or lists;
- Napkin diagram for relationships, pathways, comparisons, or decision logic;
- Remotion for branded titles, cards, captions, lists, checks, timelines, and coordinated composition;
- Hyperframes for connected systems, diagram motion, data-led explanations, and short polished animations;
- Canva for editable visual systems, collages, photographs, or simple branded components;
- Higgsfield for planned cinematic B-roll or metaphors that justify the cost;
- licensed or owned B-roll for real-world context.

Do not assign a visual merely to satisfy a tool quota.

## Media plan rule

For every planned asset, state:

1. what spoken idea it explains;
2. why this asset type is the best choice;
3. where it appears;
4. whether the presenter is visible and where;
5. what the viewer should understand afterward;
6. whether text is embedded or added by the compositor;
7. who owns the persistent logo.

## Stable asset IDs

Use prefixes:

- `NAP-` Napkin AI
- `RM-` Remotion
- `HF-` Hyperframes
- `CAN-` Canva
- `HIG-` Higgsfield
- `ICO-` icons
- `BR-` B-roll
- `PHOTO-` photographs
- `CAP-` semantic overlays
- `CH-` chapter cards
- `LT-` lower thirds
- `END-` end screen

Number within the project and never reuse an ID for a different asset.

## Asset lifecycle

Use these statuses:

- `planned`
- `creating`
- `proof_ready`
- `repair`
- `approved`
- `rejected`
- `placed`
- `verified_in_timeline`

Do not place `proof_ready` assets. Only `approved` assets enter assembly. Do not claim final usage until the status is `verified_in_timeline` with a timeline range or frame proof.

## Shared project structure

Store assets under:

```text
04 Assets/
  00 Common/
    Brand/
    Fonts/
    Icons/
  Chapter 01/
    Napkin AI/
    Remotion/
    Hyperframes/
    Canva/
    Higgsfield/
    B-Roll/
    Proofs/
```

Repeat chapter folders as needed. Keep editable sources and durable exports together with provenance in the manifest.

## Freeze gate

Before timeline assembly, confirm:

- planned count equals approved or explicitly rejected-with-reason count;
- each approved asset has a local file and proof;
- all text is correct and readable;
- nested assets are logo-free;
- layout reserves presenter and caption space where needed;
- vector or 4K quality is available;
- any rejected asset has a replacement or a documented decision to omit it.
