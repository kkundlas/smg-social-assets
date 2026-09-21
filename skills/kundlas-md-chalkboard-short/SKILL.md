---
name: kundlas-md-chalkboard-short
description: >-
  Use when Kulmeet says create a short (or chalkboard short) and provides
  narration audio plus a chaptered script. Builds a 9:16 Kundlas MD chalkboard
  explainer and instructs Higgsfield to animate the chalk drawing on, then
  composites one continuous MP4.
---
# Kundlas MD chalkboard short

Build a finished vertical 9:16 Kundlas MD chalkboard explainer from narration audio + a chaptered script.

When Kulmeet says **create a short** (or chalkboard short / Kundlas MD video) and has provided **audio + script chapters**, run this skill end to end. Do not invent chapters or rewrite the narration.

## Trigger

Run when all of these are true, or clearly implied:

- He says create a short / chalkboard short / Kundlas MD video
- He has provided narration audio
- He has provided a chaptered script

If audio or chapters are missing, stop and ask. Do not generate scenes without both.

## Higgsfield animation (required)

Instruct Higgsfield to **animate the chalk drawing**. That is the point of this skill.

Each scene must look like chalk is being drawn onto a teal board in real time:

- Lines, arrows, organs, labels appear as if a hand is writing/drawing them on
- Motion is the drawing itself (stroke-on, diagram assembling), not a Ken Burns zoom on a still, not a crossfade between stills, not a talking-head, not photoreal people
- Keep the board, logo, and disclaimer stable while the chalk draws

Tell Higgsfield, in the generation prompt, something equivalent to:

> Animate this as a chalkboard. Off-white chalk draws itself onto a deep teal textured board. Mechanism diagram only. No people talking. No photorealism. 9:16 vertical.

Use Higgsfield `generate_video` with `seedance_2_5`, aspect `9:16`. Confirm the Higgsfield session actually works with a live `balance` or `list_workspaces` call before spending credits. If the session is dead, stop and get a fresh login. Do not silently fall back to still-frame HTML.

Run his prompts/script as given. Do not invent creative direction.

## Inputs (required)

- Narration audio (wav/mp3/m4a)
- Chaptered script: ordered blocks with title + spoken text

Chapter blocks should land near ~10s. If a block is wildly off, flag it, then still generate unless he says to wait. Do not rewrite the script. Subdivide a long chapter into ~10s visual beats under the same chapter title if the model duration cap requires it.

## Brand kit (locked)

- Background: Deep Teal `#12343B` (textured chalkboard, not flat CGI, not photoreal)
- Chalk lines: Warm Off-White `#F4F3EE`
- Accents: Signal Yellow `#F5D10A`
- Type: Bebas Neue for display (all caps). Lato for body/sub-headers
- ALL CAPS on every overlay: chapters, captions, subtitles, disclaimer
- Kundlas MD logo top-left
- Disclaimer bar bottom: `EDUCATIONAL ONLY · TALK TO YOUR CLINICIAN`
- No people talking. No photoreal humans. Mechanism-first diagrams only (organs, arrows, loops, icons as chalk line-art)

Reference look (style, not palette override): Kundlas MD Short “Why Frequent Cannabis Use Cause Cyclic Vomiting” (`https://www.youtube.com/shorts/lPivjSVc7Qo`).

## Pipeline

1. **Measure audio.** Duration, sample rate. Map chapter blocks onto the timeline (word timestamps if local STT is available).
2. **Key image.** One chalkboard still that locks board texture, palette, and logo placement. Higgsfield `generate_image` (diagram/text-capable model, not a photoreal portrait).
3. **One animated scene per chapter beat.** Higgsfield `generate_video` `seedance_2_5`, 9:16. Instruct chalk-draw animation. Use the key image as start/style reference when the model accepts it. Match beat duration.
4. **Composite.** Concatenate scenes into one continuous video. Mux his narration as the only audio. Burn yellow ALL CAPS captions, top chapter titles (Bebas Neue), logo top-left, disclaimer bar bottom.
5. **QC.** Chalk actually draws (not stills). Logo not covering diagrams. Disclaimer readable. Captions not colliding with titles. Timing matches audio. No Shield branding.
6. **Deliver** one continuous MP4 plus a real download link. Do not publish unless asked.

## Do not

- Start generation without audio + chaptered script
- Ship still frames with crossfades as the “animated” version
- Put a talking-head doctor on the board
- Use medical-blue/white thumbnail colors instead of this kit
- Recolor to crimson/retired Shield reds
- Invent a download URL
