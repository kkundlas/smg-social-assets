---
name: Kundlas MD Video Production
description: >-
  Use when producing or revising long-form KundlasMD videos from a named
  Descript project through Borumi: 18 stages, QC before the next step,
  speaker-clear boxes, SMG overlays, YouTube audio locked at −14 LUFS, last
  scene is the locked DISCLAIMER card. After a 4K master exists, upload it to
  YouTube and into that job’s Descript project.
---
# KundlasMD Video Production

This skill lives at `/home/box/agent-data/workflows/kundlas-md-video-production`. Always read the references. Do not improvise past a missing gate.

Invoke wrapper: [KundlasMD From Descript](sand-workflow:descript-to-borumi-production). Overlay grammar: [SMG YouTube Layout Pack](sand-workflow:smg-youtube-layout-pack). Speaker-clear: [Kundlas MD Speaker Clear](sand-workflow:kundlas-md-speaker-clear). Napkin PIP seats: [Kundlas MD Napkin Speaker Seats](sand-workflow:kundlas-md-napkin-speaker-seats). Last-scene copy: `references/end-disclaimer.md`. Subscribe cadence: `references/subscribe-nudge.md`.

## Hard rail

Follow the 18 stages in `references/workflow.md` in order. A stage advances only after QC evidence is written. Do not ask permission between stages after the user names the Descript project. Pause only for medical ambiguity, a thought-dropping cut, missing source, new paid/destructive/privacy risk, a plan change, or a platform auth wall.

Original A/V only. One KundlasMD logo. No Shield on screen. No music unless asked.

## Audio loudness (hardwired 2026-08-24)

Kundlas MD YouTube review and master: **−14 LUFS** integrated, true peak **≤ −1 dBTP**, AAC **48 kHz**.

Descript auto-level defaults to −16 LUFS (podcast). Do not leave a YouTube export at −16. If Descript export offers Normalize Volume, pick −14. Measure the finished file. Fail delivery QC if integrated loudness is off-target or true peak clips.

## Last-scene disclaimer (hardwired)

Every Kundlas MD video ends on this exact full-frame card. After the end-screen subscribe. Never skip. Never paraphrase. Never put a short footer in its place. Missing or rewritten last-scene disclaimer fails the video.

Visual: full deep teal field. Heading `DISCLAIMER` in large cream. Short crimson rule. Then the three sentences in cream. Hold 8s or until readable.

Heading: `DISCLAIMER`

This video is intended solely for educational purposes. It is not intended, nor should it be considered, a substitute for professional medical advice. We strongly advise relying on the expertise of licensed medical professionals to make informed decisions about your health and medical care.

See `references/end-disclaimer.md`.

## Speaker-clear boxes (locked 2026-08-24)

Boxes cannot cover the speaker. Size and place the box. Never grow a half-screen empty teal wall. Never a fat full-width mid-chest bar. Never white type mid-coat with no plate. If a box hides face, beard, hands, or half his torso, the frame fails QC. Follow [Kundlas MD Speaker Clear](sand-workflow:kundlas-md-speaker-clear).

Banner anatomy that stays: dark background, yellow kicker, white claim, red underline (MYTH 5 / MISTAKE 2). Shape and placement can change. Red underline sits under the word ink, never through the letters.

## Subscribe nudge (locked 2026-08-23)

Recreate the subscribe / read icon from Descript template `https://web.descript.com/c138581c-d515-43ce-aa82-21a4fbccd31d/6534b` and SMG `references/outro.png`.

Use it **3–4 times about every 3 minutes**, and **again on the end screen**, to nudge subscribe to **KundlasMD**. Then the locked DISCLAIMER card.

- Mid-roll: corner or lower-third; never cover the mouth; 5s hold
- Channel: KundlasMD only. No Shield

## Newscast and Napkin seats (locked 2026-08-24)

Real diagrams only (Napkin / Remotion / Hyperframes): Napkin fills the frame; speaker is a small PIP. Four seats, pick by format and empty space: portrait high window; portrait video bottom-left; landscape rectangle bottom-left; landscape circle bottom-left. Nothing overlaps. Crop-to-fill the PIP. Never stretch.

Text-only and short lists: full-frame him plus a fitted three-color card.

When he is explaining a mechanism, use sequential diagram motion (PAIRING CHANGES THE CURVE, THE PLATE METHOD). More motion per chapter, not card-only.

## 4K delivery (locked 2026-08-24)

When a 4K master exists (probe must show **3840×2160**), do both without waiting to be asked:

1. **YouTube** — upload to the Kundlas MD channel as **unlisted** (unless he names another visibility). Send him the watch URL.
2. **Descript** — import the same 4K file into **that job’s existing Descript project** as deliver media (folder like `04 Deliver/…-4K.mp4`). Do not drop it onto the talking-head composition unless he asks. Do not `publish_project` unless he asks.

Confirm 4K with ffprobe before claiming it. YouTube audio stays −14 LUFS / TP ≤ −1 / 48 kHz.

## Intelligent overlays (required)

The old thin overlay habit is rejected. Do not burn continuous transcript. Do not use a generic white caption strip. Every on-screen line is an SMG **invoke key** with real slots, matched to `references/<key>.png`.

Required treatments on a typical long-form cut:

- `captions` — teal band on the presenter; 6–8 condensed-cap words; cream except **one** Signal Yellow word. Lower-middle, not mid-coat.
- `text` — fitted three-color card (yellow kicker, white claim, red underline). Not a full-width fat bar.
- `chapter` — yellow SECTION + cream title + crimson rule, lower left, speaker clear.
- `list` / `paragraph` / `bigfact` / `quote` — fitted card or real-diagram newscast. Never a half-screen empty teal plate that bisects his face.
- `speaker` — cream name, yellow role, once near the open. Small plate.
- `subscribe` — 3–4 times every ~3 minutes, plus end screen.
- `intro` / `outro` — pack stills; last scene is the locked DISCLAIMER card.

On the card rail and `semantic-caption-map.csv`, every type row must include: SMG key, exact words, which word is yellow (for `captions`), presenter mode, and proof path.

Write overlay copy as a complete patient-facing thought. Prefer fewer, larger words. Never yellow on cream.

## Asset lanes (locked 2026-08-24)

- Canva: icon and banner factory (crop-ready symbols, chapter kickers, card variants).
- Higgsfield: extra motion plates and short loops for teaching beats. Never his face or voice.
- Napkin / Hyperframes / Remotion: pathway and comparison diagrams.
- Do not treat a generated file as approved until a frame check passes speaker-clear and brand.

## Overlay duration (locked 2026-08-23)

- `captions`: 2.5–4s or the full spoken phrase, whichever is longer
- `text` / `chapter` / `speaker` / `intro` / `subscribe`: 5s minimum
- `list` / `paragraph` / `quote` / `bigfact` and Hyperframes: 6–8s min, or until the idea is said
- Disclaimer last scene: 8s minimum
- Prefer fewer, longer cards over many short ones

## Load the package

Read `references/workflow.md`, `brand-layout.md`, `end-disclaimer.md`, `subscribe-nudge.md`, `dialogue-editing.md`, `card-rail-and-assets.md`, `tool-routing.md`, `quality-control.md`, `delivery.md`, `project-storage.md`, `efficient-production.md`.

## Establish the project

One folder in Dropbox `/Borumi`: `YYYY-MM-DD - <title>`. Use `scripts/create_project.py` or the same tree via Dropbox. Never reuse another video's folder.

## Validate

```bash
python3 scripts/validate_project.py "<project folder>" --through <stage-number>
python3 scripts/probe_media.py "<media file>" --expect-width 3840 --expect-height 2160 --expect-fps 30
```

Inspect real frames at start, middle, and end of every designed scene. Overlay QC includes subscribe cadence, speaker-clear, last-scene disclaimer, and −14 LUFS audio.
