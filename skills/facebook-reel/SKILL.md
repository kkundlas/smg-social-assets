---
name: Facebook reel
description: >-
  Use when creating a Shield Medical Group vertical Facebook Reel (7-frame
  1080×1920) from a topic, including daily Shield Health News. Locked heat-reel
  chrome: hook first, title outside the yellow box, brand-teal box fill, large
  flat logo, no icons except the host photo on slide 1, Utope Rhythmic Reverie
  at 0.36.
---
Use when creating a Shield Medical Group vertical Facebook Reel from a topic, including the daily Shield Health News reel. This is the locked recipe from the approved heat + BP meds reel (Aug 2026) and the approved Xocova PEP news reel (Sep 1, 2026). Apply [Shield Medical brand](sand-workflow:shield-medical-brand) throughout.

# Facebook reel

Produce 1 MP4 + 7 PNG frames (1080×1920). Never mix Kundlas MD YouTube branding. Never auto-publish.

Kulmeet locked this look on Sep 1, 2026 on the Xocova PEP cut. Do not invent a new layout. Do not use the 5-slide empty-teal carousel (left-ragged type, leftover stick icons, dead lower third) as a daily news reel or as a substitute for this chrome.

Clone the last approved builder (`heat-reel-2026-08-14/build.py` or `carousels/xocova-ditto/reel/build.py`) and swap copy only.

## Locked look (do not invent a new layout)

- Canvas 1080×1920. Yellow hairline at the very top.
- **Logo:** white rounded card, **480×150**, Shield Medical Group logo flattened onto white. `box-shadow: none`. No drop shadow, no ghost watermark, no halo. Logo is the hero at the top. Titles must not dwarf it. Static on every frame. Never animate.
- **Title (OUTSIDE the yellow box):** Bebas Neue, 64–70px, two lines max. Line 1 white, line 2 Signal Yellow `#F5D10A`. Thin crimson rule `#96151D` (112×4) under the title.
- **Yellow box:** 5px Signal Yellow border, 22px radius. Fill is brand Deep Teal **`#12343B`** (not navy, not near-black). Title stays above the box. Every other word (body, action labels, action lines, steps, CTA, photo on slide 1) goes **inside** the box.
- **Inside type:** Lato Bold, large enough to read, centered, space-evenly. No orphan words. No clip into the footer. ≥24px air between box bottom and footer pill. Each display line is nowrap and short enough to fit.
- **Footer:** yellow pill, Bebas or Lato, Soft Black `#231F20` on yellow. Phone / location / URL as the slide needs. Text swaps every slide.
- **Icons:** none. No emoji, no stickers, no stick figures, no schematic doodles. Slide 1 is the host photo full-bleed inside the box. Slides 2–7 are type only.
- **Colors:** Deep Teal `#12343B`, Signal Yellow `#F5D10A`, Warm Off-White `#F4F3EE`, Soft Black `#231F20`, Crimson `#96151D` as a small accent only. Never `#F72736`. Never yellow as text on cream/white.
- **Fonts:** Bebas Neue for all-caps display. Lato for everything else.
- **Alignment:** everything centered. Logo, title, box, type, footer pill.

## Locked 7-slide shape

1. **Hook + photo.** Title: the scroll-stopper (not “BREAKING HEALTH NEWS”). Photo of Dr. Kundlas fills the box. Footer is the local or news fact (e.g. HEAT INDEX UP TO 111 / FDA APPROVED MAY 2026).
2. **Local fact + action.** Title names the situation. Box: one fact, then a yellow **WHAT TO DO** label, then the action line.
3. **Why you care.** Title: WHY SHOULD YOU CARE? Box: why it hits this patient, yellow **RIGHT NOW** label, then the action.
4. **Evidence.** Title: WHAT DOES THE EVIDENCE SUPPORT? Box: one CDC/authority/study line (no orphan words), yellow **TRY THIS** label, then a short action.
5. **Simple truth.** Title: SO WHAT’S THE SIMPLE TRUTH? Box: two short sentences, then the action in yellow with **no extra label**.
6. **Next steps.** Title: WHAT SHOULD YOU DO NEXT? Box: **three** lines only, separated by thin yellow rules. No numbered list on the graphic.
7. **CTA.** Title: QUESTIONS? / WE’RE HERE FOR IT. Box: Sebring and Lake Wales. Same doctors. / BOOK YOUR VISIT / (863) 236-9550 / shieldmedicalgroup.com. Footer: SHIELDMEDICALGROUP.COM.

Vary the action labels across slides (What to do / Right now / Try this / no label). Never print “intro,” “hook,” “attention,” PEACE, or slide numbers on the graphic.

## Locked timing and music

- Hold **5.5s** per slide. Crossfade **0.4s**. About **36s** total.
- Music: **Utope — Rhythmic Reverie**. File: `heat-reel-2026-08-14/music/rhythmic-reverie.mp3` (source `utope-rhythmic-reverie.mp3`). Volume **0.36**. 1.0s fade in, 1.5s fade out. Same track on every Shield Facebook reel. Never silent-descent. Never meme SFX. No voiceover unless Kulmeet asks.

## Copy rules

- Write each slide’s on-screen text first. Wait for Kulmeet’s approval before rendering, unless he already said to build this cut.
- Patient-facing. Evidence-based. Never invent stats.
- Each content slide reports the fact, then a line on what to do.
- Caption byline is **Kulmeet Kundlas MD**, not “Dr. Kundlas”. Include the hook, the actions, identity footer, sources, “Educational only. This is not a substitute for professional medical advice.” Disclaimer lives in the caption, not on the frames. No PEACE labels. No hashtag pile.

## Workflow

1. Topic (or research options and let Kulmeet pick).
2. Write the 7-slide copy as text. Wait for approval unless he already said build it.
3. Clone the locked builder. Swap copy only. Render PNG. Assemble MP4 with ffmpeg and Rhythmic Reverie at 0.36.
4. Inspect every PNG: logo larger than titles, title outside the box, body inside, box fill `#12343B`, no logo shadow, no clip, no icons except slide 1 photo.
5. Show the 7 PNGs + MP4 + caption. Wait. Do not post.
6. After yes: host the MP4 on `kkundlas/smg-social-assets`, verify HTTP 200, then hand to [shield-facebook-publish](sand-workflow:shield-facebook-publish) with `fb_type: reel`. Always `customScheduled`, never `shareNow`, unless Kulmeet says post now.

## Never

Do not mix Kundlas MD YouTube branding. Do not put titles inside the yellow box. Do not use a near-black box fill. Do not shrink the logo into a stamp. Do not add stick-figure icons to this reel. Do not use the empty-teal 5-slide carousel as this reel. Do not use sad piano. Do not post without showing the final frames, caption, and pages.
