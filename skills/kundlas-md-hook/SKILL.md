---
name: Kundlas MD Hook
description: >-
  Use after a Kundlas MD title is locked and before intro, thumbnail, or script.
  Standing hook skill for every future long-form and Shorts open. Three
  formulas, one Recommended, spoken lines used verbatim.
---
# Kundlas MD Hook — standing skill

Standing skill. Owns the opening. The script skill never drafts a hook.

Run after [kk-title](sand-workflow:kk-title) is locked. Run before [Kundlas MD Intro](sand-workflow:kundlas-md-intro), [kundlas-md-thumbnail](sand-workflow:kundlas-md-thumbnail), and [kundlas-md-script-body](sand-workflow:kundlas-md-script-body).

Drive twin: `09-hook-SKILL.md` in the 9 Skills folder. This skill is the runnable copy. Do not edit Drive 04 / 05 / 06 in place.

## Inputs

Required:

- Locked title
- Category: Clinical / Practice / Lifestyle
- Primary keyword
- Core misconception or mistake
- Payoff the video actually delivers

If title, misconception, or payoff is missing, emit `[HOOK INPUT INCOMPLETE — missing: X]` and stop. Do not invent. Do not write the script.

## Three formulas (one candidate each)

1. **Counter-Narrative** — interrupt a common belief or habit.
2. **Empathy + Authority Bridge** — name the frustration, then promise a clean answer.
3. **High-Stakes Mistake** — urgency around a real daily or clinic action.

Generate all three. Mark a strained formula `[FORMULA STRAIN]` with one line. A strained formula can still win.

Each candidate uses the 3-step Clinical Authority beat inside the 0:00–0:15 window:

1. Disruption state (0:00–0:05)
2. Stakes / why (0:05–0:10)
3. Authority promise (0:10–0:15)

Hook plus intro share the first 30 seconds. Hook is the front ~15 seconds: three to five spoken lines.

## Spoken-line rules

- One line per line. No numbering, bullets, bold, emojis, stage direction, or parentheticals in the teleprompter block.
- Last line is always the promise.
- 8th-grade English.
- No greeting, no “in today’s video,” no channel intro.
- Do not repeat the title’s words.
- No invented stats, PAA, or sources. If a number is not already sourced, omit it.
- Do not promise an indication, cure, or mechanism the research does not support.

## Output

### Option [N] — [Formula Name]

**Spoken Lines (Teleprompter)**

line
line
line
line

**Editor Instructions (Descript / Visuals)**

- Line 1: text overlay and graphic
- Line 2: visual
- Line 3: visual
- Last line: return to standard A-roll on black. Lower third: `Kulmeet Kundlas MD - Board Certified Internist`

Flags: `[FORMULA STRAIN / ACCURACY STRAIN / none]`

Why this works: one sentence.

Mark one **Recommended**. If a hook is already locked in chat, use that verbatim and do not write a new pack.

## After lock

Drop the Recommended Spoken Lines into the script `SAY VERBATIM — OPENING HOOK AND INTRO` block unchanged. Then run intro.
