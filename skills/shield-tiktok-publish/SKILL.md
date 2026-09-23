---
name: Shield TikTok publish
description: >-
  Use when an already-approved TikTok asset is ready to upload, verify, and
  schedule via GitHub then Buffer to @kundlasmd. Never auto-publish.
---
Use when an already-approved TikTok asset is ready to upload, verify, and schedule via GitHub then Buffer to @kundlasmd. Does not design or write copy.

# Shield TikTok publish

Approved file + caption → GitHub host → HTTP 200 on the raw URL → Buffer TikTok `@kundlasmd`. Always wait for an explicit yes before any write. Never auto-publish. Do not post Facebook, GBP, YouTube, Pinterest, or LinkedIn from this skill. Apply [Shield Medical brand](sand-workflow:shield-medical-brand) for logo/palette (TikTok = **Kundlas MD** logo, never Shield).

## Destination (live lock, 2026-08-30)

- Buffer org: Shield Medical Group `6a57efe156ba890021371a49`
- Channel: TikTok `@kundlasmd` `6a94855e065799be4656e2f0` (service `tiktok`, type `account`, not locked, not disconnected)
- Profile: https://tiktok.com/@kundlasmd
- If this channel id 404s, rediscover with Buffer `list_channels` for the org and update memory. Do not invent a channel. Do not print tokens.
- Stale: `6a9448bf065799be4654baac` (old `kkundlas`) 404s. Do not use it.

## Hosting

Upload to public repo `kkundlas/smg-social-assets` on `main` as `YYYY-MM-DD/<kebab-slug>.<ext>`. One upload per publish call.

Raw URL: `https://raw.githubusercontent.com/kkundlas/smg-social-assets/main/YYYY-MM-DD/<slug>.<ext>`

**Logo lock (Kundlas MD — TikTok):** official Kundlas MD logo PNG at `/home/box/agent-data/workflows/kundlas-md-video-production/assets/brand/kundlas-md-logo.png` (also under `kkundlas/smg-social-assets` brand path when hosted). **Never** the Shield Medical Group logo on TikTok assets. Never mix logos; never recolor unless Kulmeet explicitly requests.

Commit as Dr. Kulmeet Kundlas `<kkundlas@shieldmedicalgroup.com>`, message `Add <slug> (YYYY-MM-DD)`.

Verify with `curl -sSLI` HTTP 200 before Buffer. Retry once after 5s. Stop if still not 200.

Never host on uguu.se, tmpfiles.org, catbox, 0x0.st, transfer.sh, or litterbox.

TikTok via Buffer requires an image or video asset. Prefer `.mp4` 1080×1920.

## Duplicate pre-flight

Exact first-line caption match with a live TikTok = hard stop. Reusing a recent GitHub raw URL as live media = hard stop.

## Approval card

Show: TikTok `@kundlasmd`, time in ET and UTC, full caption untruncated, GitHub raw URL, asset type (video/image), `schedulingType`. Wait. Do not proceed on silence.

## Buffer

Use the Buffer connector (`user-Buffer`). Reads anytime.

After yes:
- `channelId`: `6a94855e065799be4656e2f0`
- `mode`: `customScheduled` with ISO 8601 offset (`America/New_York`). Immediate only if he says post now, then `shareNow`.
- `schedulingType`: `notification` unless he explicitly wants Buffer to auto-fire (`automatic`). Default is notification so Buffer still needs a tap if anything looks off.
- `assets`: `[{ "video": { "url": "<raw url>" } }]` or image.
- `text`: full caption.
- `metadata.tiktok.title`: short title if useful. `metadata.tiktok.isAiGenerated`: true only if the video is AI-generated (original A/V is false).

Never `addToQueue` as a silent dump. Never silently truncate. TikTok caption keep tight; do not paste a Facebook 2,000-character dump.

## After

Report Destination | Channel | Post ID | Scheduled ET | Result plus the single raw URL. Never silently succeed. On Buffer 401, stop and ask Kulmeet to reconnect Buffer. Do not print keys.
