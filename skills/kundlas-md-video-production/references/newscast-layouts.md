# Newscast layouts (locked 2026-08-23)

Source: Descript template https://web.descript.com/7064f85b-0a9d-4b21-9d74-1fcd045408c3/730d6
Stills: `smg-youtube-layout-pack/references/newscast/`

This is a news-desk grammar. The speaker is a small panel. The asset (Napkin, Remotion, Hyperframes, or a screen) takes most of the frame.

## Rule

- Presenter LEFT or RIGHT in a rounded, red-bordered portrait panel (~20–40% of the frame)
- Graphic occupies ~60–70%
- Dark teal field `#12343B`
- Condensed all-caps cream headlines, amber/yellow bullets `#F5D10A` or `#E8A33D`
- Optional black pill chapter marker
- One compositor-owned KundlasMD logo. Nested Napkin/Remotion/Hyperframes stay logo-free
- No Shield. Circle avatar only as a documented exception
- Full-frame `list` / `bigfact` / `screen` is allowed when the speaker would hide the teaching

## Modes (use these)

- `presenter_rect_left` + graphic right (default newscast, including Napkin diagrams)
- `presenter_rect_right` + graphic left (lists, quotes, screens)
- `graphic_full` for bigfact and dense lists
- `presenter_full` only for trust / nuance, not for teaching cards

Template copy (TITLE, FIRST ITEM, EXCLUSIONS) is slots, not episode text.

## Presenter geometry (locked 2026-08-23)

Never non-uniform scale of the recorded A/V. Do not squash 16:9 into a tall portrait. Use a 16:9 framed window in the side column (fit or crop-to-fill). Keep full head, hair, shoulders. Red 3px frame around that window.
