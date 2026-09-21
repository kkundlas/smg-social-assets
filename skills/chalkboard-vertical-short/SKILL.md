---
name: Chalkboard vertical short
description: >-
  Use this when original narration audio (a file, Descript project, or share) is
  given for a 9:16 Facebook, TikTok, or YouTube short. Run end to end without
  waiting for a style recap: denoise static, strip gaps, HyperFrames chalkboard,
  two logo cuts, audible A-minor pad, show in chat, do not post.
---
# Chalkboard vertical short

When original narration arrives for a 9:16 short or reel, **run this end to end**. Do not stop to reconfirm the look. Do not invent spoken lines. Do not post.

Locked from the 2026-08-31 DNA-kit chalkboard reel, plus the 2026-09-01 Ozempic recut (denoise + audible pad).

## Trigger

All of these, or clearly implied:

- Original voice audio (wav / m4a / mp3), a Descript project, or a Descript share
- A vertical short / Reel / TikTok / YouTube Short
- No instruction to use a different style

If audio is missing, stop and ask. If a chaptered script exists, map visuals to it. If only audio exists, transcribe it and map the five chapter titles onto what was actually said.

## Hard rails

- Original A/V only. Never clone voice or face. Never write missing lines in the speaker’s voice.
- If a locked spoken line is missing from the take, leave it off. Do not invent it.
- Never print PEACE, Miller, or chapter numbers (`CHAPTER 01 / 05`).
- Show the finished MP4s in chat. Never native-post. Never Buffer until an explicit yes.
- Higgsfield is not this look. Use HyperFrames (HTML/CSS/JS → MP4) chalkboard draw.

## Two cuts (always both)

| Destination | File | Logo |
|---|---|---|
| Facebook + TikTok | `smg-<slug>.mp4` | Shield Medical Group (cream plate ~220px wide) |
| YouTube Short | `kundlasmd-<slug>.mp4` | Kundlas MD (~180px wide) |

Same picture otherwise. Title sits at ~200px from the top so it never collides with the logo. Logo, chapter title, and disclaimer stay up for the whole chapter.

## Look

- Canvas **1080×1920**, 30fps, H.264 + AAC, `+faststart`
- Field: Deep Teal `#12343B` textured chalkboard
- Chalk: Warm Off-White `#F4F3EE`
- Accents that actually appear: Signal Yellow `#F5D10A` (never as text on cream), Crimson `#96151D` as a real field, white
- Optional fifth: Soft Black `#231F20`
- Type: Bebas Neue (all-caps titles), Lato (body)
- Stick figures / simple schematic diagrams. No photoreal people. No talking head.
- On-screen chapter titles, in this order, no numbers:
  1. WHY THIS MATTERS NOW
  2. WHAT YOU SHOULD KNOW
  3. WHAT THIS MEANS FOR YOU
  4. WHAT TO DO NEXT
  5. WHAT I WANT YOU TO REMEMBER
- Disclaimer on every chapter: `Educational only — please talk to your clinician about you.`

## Motion (must feel drawn, not slapped)

- Chalk draws on with `stroke-dashoffset`, easing `cubic-bezier(0.33, 0, 0.2, 1)`
- Capture **every frame**. No skip/hold jumps.
- Hard cuts are wrong. **0.35s ffmpeg xfade (fade)** between chapters.
- Hold the last board to match remaining audio after xfades shorten picture.

## Audio (required, do not skip)

1. Pull the take. If the source is Descript, get composition audio (unlisted audio publish is fine for a download; do not post the share).
2. **Denoise first.** Room hiss / static behind the voice is a fail. Use a high-pass (~80 Hz), spectral denoise (`afftdn` learning from opening room tone), and a light gate. Do not clone or rewrite the voice. If static remains, run Descript Studio Sound on the original file, then re-export.
3. Strip word gaps / long silences **after** denoise (`silenceremove` or Descript Underlord pauses). Do not change words.
4. Speech is the only voice. Mix:
   - voice gain `1.0`
   - quiet A-minor cinematic pad (no melody, no vocals) at `0.62–0.70` so it is actually audible under speech
   - sidechain duck under speech (`threshold=0.04:ratio=8:attack=30:release=280`)
   - 1s fade-in, 2s fade-out on the pad
   - limiter `limit=0.95`
5. Target mixed mean around −29 dB, peak around −5 dB.
6. A recut that is voice-only with no pad is incomplete. Rebuild audio even if picture is already done.
7. Do **not** use Utope “Rhythmic Reverie”. Do **not** use silent-descent.

## Pipeline

1. Land sources in `/Borumi/YYYY-MM-DD - <title>/01 Intake/Sources` (original + cleaned + mixed audio, transcript).
2. Transcribe cleaned audio. Map the five titles onto spoken spans. Do not rewrite the narration.
3. Hand HyperFrames the chapter list, durations, logo rules, brand kit, and **mixed** audio (or silent picture + mixed audio to mux). HyperFrames renders both logo cuts.
4. QC stills at each chapter: no chapter numbers, logo clear of type, chalk actually drawing. Listen all the way through: no static bed, pad present in the gaps.
5. Deliver both MP4s in chat plus captions (unlabeled Facebook; short TikTok; YouTube title + description). Byline `Kulmeet Kundlas MD`. Disclaimer in the caption.
6. Stop. After an explicit yes, host on GitHub `kkundlas/smg-social-assets` and hand Facebook Agent, TikTok, and YT-Researcher. This skill never native-posts.

## Captions (write with the package, unlabeled)

- Facebook: action first, no PEACE labels, no hashtag pile.
- TikTok: short context, topic hashtags only, no `#FYP`.
- YouTube: locked title if one was chosen; description matches the take.

## Do not

- Wait for a second “make it chalkboard” after audio is already in hand
- Ship a cut with hiss behind the voice or with no music bed
- Clone, rewrite, or lip-sync missing lines
- Ship stills with dissolves as the animation
- Cover titles with the logo
- Auto-publish
- Mix Kundlas MD onto the Facebook/TikTok cut or Shield onto the YouTube cut
