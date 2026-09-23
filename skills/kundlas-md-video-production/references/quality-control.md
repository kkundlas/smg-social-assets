# Quality-control system

Use layered QC. No single automated check can approve a video.

## Contents

- Editorial and presenter QC
- Text and brand QC
- Asset and timeline QC
- Frame inspection
- Regression sweeps
- Technical QC
- Final pass criteria

## Editorial QC

- Every retained sentence is complete and coherent.
- Retakes, false starts, and duplicated takes are removed when a stronger complete delivery exists.
- Intentional repetition and rhetorical pacing remain when useful.
- No medical qualifier, limitation, or safety instruction is lost.
- Chapters match the final dialogue and actual viewer promise.
- The first 30 seconds establish problem, stakes, value, and authority.

## Presenter QC

- The full head and hair are visible with comfortable headroom.
- The framing is not excessively zoomed.
- The original background remains unchanged.
- No overlay covers the mouth, beard, chin, or gestures.
- Presenter placement does not obstruct a diagram.
- Dense graphics use the full frame unless a camera region has a clear purpose.
- Rectangular framing is preferred for split layouts.

## Text QC

- Semantic overlays express a complete thought.
- Copy is not a verbatim repetition unless quotation is intentional.
- One line is preferred.
- Two lines are short, balanced, and similar in length.
- Text is large enough for phone viewing.
- No text is clipped, overlaps cards, touches the logo, or enters the player-control zone.
- Medical terms, numbers, units, and names are correct.

## Brand QC

- Exactly one visible KundlasMD logo appears in each finished frame where persistent branding is required.
- No nested asset contains a second logo.
- No Shield Medical Group branding appears.
- The logo clear zone is intact.
- Bebas Neue and Lato are used correctly.
- Palette and contrast follow `brand-layout.md` and `assets/tokens.json`.
- No gradients or decorative shadows appear.

## Asset QC

- Every planned asset has a local durable file and proof.
- Every placed asset maps to a card and manifest row.
- Every approved asset is either verified in the timeline or explicitly omitted with a reason.
- Canva and Napkin exports are not treated as approved merely because generation succeeded.
- Visuals are not generic substitutes for requested evidence or concepts.
- Icons use one consistent family and serve meaning.
- 4K-bound assets are vector or sufficiently high resolution.

## Timeline QC

- Audio remains synchronized after dialogue cuts.
- Transitions do not hide clipped words or create flashes.
- Remotion and Hyperframes holds meet the duration floor: captions 2.5–4s or the spoken phrase; text/chapter/speaker 5s min; list/paragraph/quote/bigfact and Hyperframes 6–8s min or until the idea is said.
- A graphic that exits before it can be read fails QC.
- Black edges are removed only without damaging presenter framing.
- Chapter markers, CTA, and end screen are present.
- Last scene is the locked DISCLAIMER card from `end-disclaimer.md` (exact FINAL 4K wording, 8s+ hold).
- No background music exists unless explicitly approved.
- The timeline inventory matches the card rail and asset manifest.

## Inspection method

For every designed scene, inspect:

- opening frame;
- signature or midpoint frame;
- final hold or exit frame.

Then inspect a labeled full-program contact sheet. Finally, watch the complete review export at normal speed with sound.

## Regression sweeps

A reported defect triggers a full-program search for the same class:

- double logo → inspect all branded frames and nested assets;
- mouth-covering caption → inspect every presenter overlay;
- cropped head → inspect every reframed presenter segment;
- overlapping Canva text → inspect every Canva-derived asset;
- missing Napkin or motion asset → reconcile every manifest row with the timeline;
- unwanted music → inspect every audio track, not only the reported timestamp;
- wrong background → inspect all presenter segments;
- spelling correction → search transcript, overlays, SRT, chapters, and metadata.

## Technical QC

Probe final outputs for:

- width and height;
- frame rate;
- duration;
- video and audio codecs;
- audio sample rate and channels;
- loudness and true peak;
- complete decode without errors.

Use `scripts/probe_media.py` for reproducible metadata checks. Record results in the delivery manifest.

## Final pass criteria

Do not call the edit complete until every checklist item is `pass`, `not_applicable` with reason, or an explicitly accepted limitation. `Unknown` is not a passing state.
