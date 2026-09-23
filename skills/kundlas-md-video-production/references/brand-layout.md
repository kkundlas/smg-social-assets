# KundlasMD brand and video layout contract

Apply this contract to every finished frame. The final video is KundlasMD-only.

## Identity

- Use `Kulmeet Singh Kundlas, MD` as the primary name.
- Use one concise authority line when useful: `Board-Certified Internist` or `25+ Years Caring for Adult Patients`.
- Do not use a long credential crawl.
- Never show Shield Medical Group text, logo, contact information, or branding on screen.
- Last scene must use the locked DISCLAIMER card in `end-disclaimer.md` (FINAL 4K wording). Do not use the short footer as the last scene.

## Logo ownership

- Use `assets/brand/kundlas-md-logo.png`.
- Show exactly one visible logo in the finished frame.
- Let the final compositor own the persistent upper-left logo.
- Keep nested assets logo-free.
- Sanitize or regenerate Napkin, Canva, Remotion, Hyperframes, Higgsfield, B-roll, or screen assets that contain a logo.
- Reserve the upper-left logo safe zone. Do not let titles, diagrams, or decorative lines touch it.

## Canvas and safe areas

- Author on a 1920×1080 logical canvas at 30 fps.
- Render the approved master at 3840×2160.
- Use 80 px logical left/right safe margins and 100 px top/bottom margins.
- Place the logo near logical x=80 and y=80–100 while preserving its clear space.
- Place talking-head semantic overlays in the lowest safe middle with about 105–125 px logical bottom clearance, adjusted upward only to avoid player controls or cropping.

## Presenter

- Preserve the real recorded background.
- Retain full head, hair, comfortable headroom, and shoulders.
- Never overzoom merely to eliminate black edges.
- Never non-uniform scale of the presenter. Crop or fit; do not stretch.
- Correct black edges with proportionate scale/crop only when headroom and composition remain safe.
- Never cover the mouth, beard, chin, or important gestures.
- Use full-screen presenter for trust and nuanced explanation.
- Prefer rectangular presenter framing in split layouts.
- Put text and graphics on the opposite side and align them to a common edge.
- Remove the presenter during dense full-screen graphics.
- Use a circular presenter only as a documented exception when it does not obstruct content.

## Semantic overlays

- Communicate the meaning of the passage rather than transcribing it.
- Use complete, mature, patient-friendly thoughts.
- Prefer one line.
- If two lines are necessary, keep them short, balanced, and similar in length.
- Increase type size before accepting an awkward wrap.
- At 1920×1080, target roughly 44–58 px Lato or 48–64 px Bebas Neue depending on length.
- Keep overlays centered in the lowest safe middle on talking-head footage.
- Keep text clear of the mouth, logo, bottom border, and player controls.
- Add an icon only when it reinforces meaning without shrinking the text.
- Keep full verbatim subtitles in the separate SRT, not as continuous editorial overlays.

## Typography

- Use Bebas Neue for short all-caps display text, normally no more than six words.
- Use Lato for sentences, labels, credentials, disclaimers, and body copy.
- Do not use Google Sans.
- Prefer larger text and fewer words for an older-skewing patient audience.

## Palette

- Deep Teal `#12343B` — primary ground.
- Signal Yellow `#F5D10A` — single emphasis.
- Warm Off-White `#F4F3EE` — light surface.
- Soft Black `#231F20` — text on light.
- Crimson `#96151D` — urgent clinical warnings only.
- Slate `#3C4651`, Steel Blue `#558BA5`, Sage `#788C5D`, and Terracotta `#DA7756` — limited supporting roles.
- Use no more than four chromatic colors in one asset.
- Never place Signal Yellow on white or Warm Off-White.
- Do not use gradients or decorative drop shadows.

## Motion

- Animate meaning: reveal a sentence, draw a connector, show a state change, build a list, or connect an icon to a concept.
- Give each motion a clear entrance, readable hold, and clean exit.
- Readable hold floors (2026-08-23): captions 2.5–4s or the spoken phrase; text/chapter/speaker 5s; list/paragraph/quote/bigfact and Hyperframes 6–8s or until the idea is said. Do not flash.
- Avoid idle logo motion, arbitrary bouncing, decorative particles, and simultaneous movement of every element.
- Let visual density follow the chapter rail rather than a fixed frequency quota.

## Packaged references

Use `assets/layout-references/` as composition grammar, not episode copy. Use `assets/tokens.json` as the machine-readable source for canvas, palette, type, logo, presenter, and disclaimer settings.

