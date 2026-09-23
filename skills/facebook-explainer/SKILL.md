---
name: Facebook explainer
description: >-
  Use when Kulmeet wants a KodeKloud-style how-it-works video for Shield
  Facebook (or says run Facebook explainer / the ChatGPT-scale technique). Dark
  canvas, hook title, diagram that adds one layer at a time, burned-in captions,
  recap zoom-out. Copy first. Never auto-publish.
---
# Facebook explainer

Use when Kulmeet wants a video like KodeKloud’s “How ChatGPT Handles 900 Million Users” (https://www.youtube.com/shorts/fVLmyuCEEy8). Apply [Shield Medical brand](sand-workflow:shield-medical-brand). This is not the 7-still [facebook-reel](sand-workflow:facebook-reel).

Reference frames live at `/workspace/shorts-ref/crop/` and `watch-01.png`…`watch-88.png`.

## What to copy (technique only)

Do not copy KodeKloud’s logo, colors, ChatGPT marks, or their script.

1. **Hook in the first second.** Full-screen question in huge white type on black. One visual metaphor behind it (they used a grid of phones). No intro card. No “welcome.”
2. **One diagram that grows.** Start with the viewer’s object (a phone, a pill bottle, a plate). Add one box at a time: router → region → load balancer → servers → data → cache → the thing that does the work. Never dump the full stack on frame 1.
3. **One idea per beat.** About 8–12 seconds per new layer. Voice (or caption) names the layer while it appears.
4. **Dark canvas.** Near-black background. Thin colored outlines (cyan for structure, one accent color for the active flow). Simple icons. No stock B-roll. No talking head unless Kulmeet asks.
5. **Burned-in captions.** Short phrases, not a transcript dump. Match the spoken line.
6. **Recap zoom-out** in the last 20–30 seconds. Show the full map, then the path the viewer’s “request” took.
7. **One number that makes it real.** They used “900 million,” “999 of every 1,000 reads,” “50 replicas.” For Shield: one sourced number, never invented.

## Shield version

- Topic shape: `How [everyday thing] actually works` (heat + BP meds, insulin resistance, a new shot, a recall path).
- Brand: Deep Teal `#12343B` canvas or near-black with teal, Signal Yellow `#F5D10A` for the active flow, cream labels, Crimson `#96151D` for the one warning. Flat Shield logo, no shadow.
- Patient-facing: Dr. Kundlas. Educational only in the caption.
- Runtime: 45–90s for Facebook unless Kulmeet asks longer. Their reference is 2:54; do not default that long.
- Music: same Utope Rhythmic Reverie bed as [facebook-reel](sand-workflow:facebook-reel), volume 0.29–0.36, under the voice.

## Workflow

1. Pick the topic and the one hook question. Wait.
2. Write the beat list (8–12 beats): on-screen label, one sentence, what gets added to the diagram. Wait.
3. Hand diagram/motion to the visual lane (Napkin or Visual Assets / Remotion). Do not invent a new renderer here.
4. Show the cut + caption. Wait. Do not post.
5. After yes: host the MP4 on `kkundlas/smg-social-assets`, then [shield-facebook-publish](sand-workflow:shield-facebook-publish) as `fb_type: reel`, `customScheduled`. Never `shareNow` unless Kulmeet says post now.

## Never

Do not render before the beat list is approved. Do not use their ChatGPT/KodeKloud art. Do not start with a logo sting. Do not put the full diagram on screen at once. Do not invent stats.
