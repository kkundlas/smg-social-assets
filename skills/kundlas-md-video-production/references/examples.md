# Worked examples and decision patterns

Use these examples to train an agent on judgment, not to copy episode wording.

## Example 1 — Repeated take

Source delivery:

```text
The most important thing is—
The most important thing to understand is that insulin resistance affects more than glucose.
```

Decision: remove the abandoned first attempt and retain the complete second sentence. Cut at the restart boundary, preserve a natural lead-in, and review the picture jump. If visible, cover the cut with a planned metabolic-system graphic.

Wrong approach: remove only the duplicated words and construct an unnatural hybrid sentence.

## Example 2 — Intentional repetition

Source delivery:

```text
It is not a replacement for laboratory testing. It is not a replacement for talking with your physician.
```

Decision: retain both sentences because the parallel structure distinguishes two limitations and strengthens the teaching.

Wrong approach: delete the second sentence merely because the opening repeats.

## Example 3 — Presenter plus graphic

Idea: compare five treatment considerations.

Decision: use a rectangular presenter frame on one side only if the diagram remains readable. Otherwise use the full-screen diagram and return to the presenter afterward.

Wrong approach: paste a circular presenter image over the bottom-right of the diagram and cover a decision card.

## Example 4 — Semantic overlay

Spoken passage: a longer explanation that treatment should consider heart, kidney, liver, weight, glucose, safety, cost, and access.

Good overlay:

```text
The treatment plan should reflect the patient's complete risk profile.
```

Wrong overlay:

```text
HEART. KIDNEY. WEIGHT. COST.
```

The good version communicates the meaning as a mature complete thought. Keep it one line when possible and position it low enough to avoid the mouth.

## Example 5 — Generated asset with a logo

Napkin or Canva returns a branded diagram containing the KundlasMD logo.

Decision: remove or regenerate the nested logo, then let the final compositor add the single persistent logo.

Wrong approach: retain the embedded logo and add a second master logo.

## Example 6 — Screenshot feedback

The user marks one caption covering the mouth.

Decision: fix the marked caption and run a regression sweep across every presenter overlay. Record all affected IDs in the revision log.

Wrong approach: repair only the screenshot timestamp.

## Example 7 — No music

The media system suggests a background bed because the video is long.

Decision: keep music off when the approved plan says no music. A generic opportunity suggestion does not override an explicit project rule.

## Example 8 — Large Descript import

The destination job displays `Waiting for 1 file to be uploaded` at 0% while a direct upload is active.

Decision: report transfer status accurately, wait for the file upload to finish, then wait for the import job and inspect the project. Do not call the upload complete at 0%.

## Example 9 — Autonomous stage progression

Step 8 assets pass inspection.

Correct behavior: report the completion receipt and automatically begin Step 9.

Wrong behavior: ask “Should I continue?” despite an approved plan.

