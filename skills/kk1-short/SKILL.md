---
name: kk1-short
description: >-
  Use for Kundlas MD YouTube Shorts that need a complete clinical thought
  (60–90s). Always run Drive 09-hook first and drop the Recommended spoken lines
  into the opening verbatim. Always include a Shorts title pack using Kulmeet’s
  Action/Benefit, Curiosity Gap, and Listicle formulas. Script only.
---
# KK1 Short — Complete-Thought Clinical Shorts

## Overview
Write a **60–90 second** teleprompter-ready YouTube Short for **Kundlas MD (@kundlasmd)**.

This is the **complete** Short: clarity, trust, and closure. Not hype. The viewer should feel the same sense of closure as leaving a primary-care visit with a clear plan.

Speak as if explaining one important thing to **one patient in the exam room**.

Script + title pack only. No frames, MP4, or publish.

## Required: Hook skill first
Before any spoken script, run Drive **09-hook** (kundlas-md-hook).

- Need: title (approved or Recommended from the title pack), category, primary keyword, core misconception, payoff.
- Emit three hook candidates (Counter-Narrative, Empathy + Authority Bridge, High-Stakes Mistake), each with Spoken Lines and Editor Instructions.
- Mark one **Recommended**.
- Drop the Recommended Spoken Lines into section 1 **verbatim**. Do not rewrite. Do not invent a homemade hook.
- If Kulmeet already locked a hook in this chat, use that verbatim and skip a new pack.
- If title, misconception, or payoff is missing, emit `[HOOK INPUT INCOMPLETE — missing: X]` and stop. Do not write the script.

## When to use (vs kk2-short)
Use **kk1** when:
- The topic needs nuance (screening vs diagnosis, medication tradeoffs, “what this lab means”)
- Viewer needs one realistic next step and calm closure
- Fear would be the wrong register
- Runtime can be 60–90s

Use **kk2-short** instead when the topic is a sharp misconception that benefits from a short emotional contrast punch (30–45s).

If Kulmeet does not name kk1/kk2, choose by topic using the rules above (see also [kk-shorts-routing](sand-workflow:kk-shorts-routing)).

## Defaults
If only a topic is given:
- Audience: adults 50+ / Medicare patients and caregivers
- Clinical focus: education
- Proceed without interviewing unless a safety-critical gap blocks a safe script

## Inputs (optional)
```text
Topic:
Audience: 50+ / Medicare / caregivers / general public
Clinical focus: education / screening / prevention / update
Required safety note: (if any)
Chosen title: (if Kulmeet already picked)
```

## Title pack (mandatory — deliver with every script)
Before or above the spoken script, always output a **Shorts title pack** using Kulmeet’s locked title formulas.

A title formula is a proven, repeatable structural template used to maximize click-through rates by combining a clear value proposition with psychological triggers like curiosity, urgency, or authority.

### Locked formulas (use these only)
1. **Action/Benefit:** How to [Achieve Desire] Without [Pain Point]
2. **Curiosity Gap:** Why [Common Practice] is Actually [Unexpected Result]
3. **Listicle:** [Number] Warning Signs of [Problem] You Shouldn't Ignore

Across the 5 options, cover all three formulas (at least one of each; the remaining two can be the strongest formulas for that topic). Adapt wording to fit Shorts length, but keep the structural skeleton recognizable.

### Title rules
- Exactly **5** options
- Each title **≤50 characters** (show exact count)
- Patient-first, clinically honest
- Combine clear value with curiosity, urgency, or authority
- No miracle claims, no fear-bait that overstates risk
- Kundlas MD YouTube voice (not Shield Medical Group)
- Label each option with its formula tag: `Action/Benefit` | `Curiosity Gap` | `Listicle`
- Mark **one Recommended** with a one-line why
- If Kulmeet already chose a title, use that in the meta line

Format:

```text
Title pack
Value + trigger: <one-line mapping>

1. [Curiosity Gap] "<title>"  (NN chars)
2. [Action/Benefit] "<title>"  (NN chars)
3. [Listicle] "<title>"  (NN chars)
4. [<formula>] "<title>"  (NN chars)
5. [<formula>] "<title>"  (NN chars)

Recommended: #<n> — <one-line why>
```

Then deliver the spoken script in the same response (do not stop for title approval unless Kulmeet asks to pick first).

## Mandatory structure (do not rename or reorder)
Return the spoken script under these five numbered headings:

1. Why This Matters Now
2. What You Should Know
3. What This Means for You
4. What To Do Next
5. What I Want You to Remember

### 1. Why This Matters Now
- First lines are the 09-hook Recommended Spoken Lines, verbatim
- Then one plain-language reason to care now if the hook did not already say it
- Natural spoken opening (no meta “in this video”)

### 2. What You Should Know
- Single most important fact
- Brief why it matters
- Evidence-based, guideline-aligned
- No data overload

### 3. What This Means for You
- Who is affected
- Lived impact (not abstract)
- Exactly **one** emotional permission bridge, this form only:

```text
You shouldn’t have to ___.
You won’t have to ___.
```

Use once. Do not stack soundbites.

### 4. What To Do Next
- One clear, realistic action (not a list)
- What improves if done early
- What becomes harder if delayed
- No fear framing

### 5. What I Want You to Remember
- One-sentence synthesis
- Calm, reassuring, authoritative
- Sounds like the final line of an office visit

## Output format
1. Hook pack (3 options + Recommended) unless a hook is already locked
2. Title pack (mandatory)
3. One-line meta (not spoken): `KK1 · Topic · Title: "<recommended or chosen>" · ~Ns`
4. Headings + spoken lines under each
5. **One complete sentence per line** (never paragraphs)
6. Blank line between sections
7. No emojis, hashtags, or spoken CTA/subscribe/subhooks
8. Must feel complete and resolved

## Style rules
- Warm, steady, plain English
- One idea per section
- Short speakable sentences
- Assume low health literacy
- No marketing language, hype, absolutes, or guarantees
- Define unavoidable jargon immediately
- Never invent statistics, study names, or citations
- Spoken brand: Kundlas MD (not Shield Medical Group)

## Clinical safety
- Never diagnose in a Short
- Prefer screening / signal / starting point / reason to talk with your clinician
- Emergency guidance when required (e.g., 988)
- Do not overstate screening, prevention, meds, or lifestyle effects
- Educational-only framing when advice risk exists

## Verification checklist
- [ ] 09-hook ran (or a locked hook was used verbatim)
- [ ] Opening lines match the Recommended Spoken Lines word for word
- [ ] Title pack uses Kulmeet’s 3 formulas (all three represented), 5 options ≤50 chars, Recommended
- [ ] Five headings in order
- [ ] 60–90s when read aloud
- [ ] One core idea
- [ ] Exactly one shouldn’t / won’t bridge
- [ ] One next action
- [ ] One sentence per line
- [ ] No CTA, emoji, hashtag, diagnosis, guarantee, invented stats
- [ ] Final line closes the loop

## Completion
Deliver hook pack + title pack + script. No “done” banner unless asked.
