# Tool routing and portability

Preserve the same stage artifacts and gates even when a particular tool is unavailable. Tools implement the plan; they do not replace it.

## Borumi or primary timeline editor

Use for:

- source-media timeline;
- dialogue cuts and synchronization;
- presenter reframing;
- chapter and asset placement;
- semantic overlays when the editor supports precise layout;
- final assembly and export.

Inspect project state before mutating it. Use transactions or reversible commits when supported. Verify timeline inventory after changes. Do not claim success from a command response alone.

Use `/Users/kulmeetkundlas/Library/CloudStorage/Dropbox/Borumi/<YYYY-MM-DD - video title>/` as the file-system boundary for each edit. Keep the Borumi editor project, sources, generated assets, editable files, proofs, and exports inside that video's folder. Never mix assets between video folders; copy approved reusable brand assets into `04 Assets/00 Common` and record their source.

## Remotion

Use for:

- chapter cards;
- branded text and semantic overlays;
- lower thirds;
- lists, checklists, timelines, comparisons, and icon choreography;
- transparent overlays;
- CTA and end screen;
- reusable programmatic compositions.

Use frame-driven deterministic animation. Load the current Remotion creation, markup, rendering, caption, and multimedia guidance when available. Register compositions explicitly, inspect stills, lint, type-check, render, and probe outputs.

## Hyperframes

Use for:

- short polished diagram animations;
- connected systems and flows;
- data-led explainers;
- line draws, node relationships, and visual state changes;
- HTML/GSAP motion units that benefit from seekable deterministic timelines.

Follow the current Hyperframes entry skill and CLI contract when available. Use a paused deterministic timeline, validate runtime/layout/motion/contrast, inspect proof snapshots, and render project-local outputs.

## Napkin AI

Use for:

- conceptual diagrams;
- pathways and decision logic;
- comparisons;
- relationships that are easier to understand visually than verbally.

Use the user's Napkin brand kit when available. Prefer SVG for scalable diagrams. Record credit-consuming generation in the manifest. Download a durable local copy. Remove generated logos before compositing. Napkin output is a source asset, not automatic approval.

## Canva

Use for:

- editable visual systems;
- collages and photo-led components;
- comparison boards;
- simple branded cards;
- reusable bulk variations.

Use the KundlasMD brand kit, then independently verify fonts, colors, spacing, text, and logo status. Generate a small pilot before a batch. If Canva repeatedly overlaps text or drifts from the brand, generate text-free components and add final typography in Remotion.

## Higgsfield

Use only when a planned cinematic shot or metaphor communicates something that the presenter, a diagram, or licensed footage cannot express as well. Confirm any paid usage before consuming credits. Record prompt, model, duration, provenance, and local export. Reject medically misleading imagery.

## Icons and real media

Use the packaged outline icon family first. Keep one icon style per scene. Use licensed, owned, or appropriately sourced photos and B-roll. Record source and license/provenance. Do not use an icon merely as decoration.

## Descript

Use for the required final handoff unless the user explicitly opts out. Create a new project for each completed video, import the verified 4K master from that video's `06 Exports/Master` folder, wait for the import job to finish, and inspect the created project. A 0% waiting state may indicate that the direct file upload has not yet completed; it is not proof of failure or success.

## SEO and vidIQ

Use the user's supplied research first. Do not repeat paid or time-consuming research without need. When API access exists and supplemental research is requested, use it to refine chapter wording without misrepresenting the actual content.

## Tool failure and substitution

When a planned tool is unavailable:

1. preserve the card's intended meaning and layout;
2. choose the closest capable tool;
3. record the substitution and reason;
4. apply the same brand and QC gates;
5. do not reduce the asset silently or omit it without updating the rail.

Hermes and Codex may expose different tool names. Match capabilities, not names. Never invent access to an unavailable service.

## Permission behavior

Do not request repeated editorial approval after the plan is approved. Treat explicit approval of a media plan that names a tool and planned asset count as authorization for those planned generations and intermediate renders. Do not re-ask “preview or render?” for each component when the approved workflow already requires rendering it for inspection. Ask before exceeding the approved paid count, introducing a new paid service, publishing publicly, deleting or overwriting material, or crossing a privacy boundary. Platform authorization prompts may still be unavoidable for protected files or account access; explain that boundary once and continue automatically afterward.
