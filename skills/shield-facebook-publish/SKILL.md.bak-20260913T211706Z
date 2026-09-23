---
name: Shield Facebook publish
description: >-
  Use when an already-approved Shield Facebook or Google Business asset is ready
  to upload, verify, and schedule via GitHub then Buffer.
---
---
name: Shield Facebook publish
description: >-
  Use when an already-approved Shield Facebook or Google Business asset is ready
  to upload, verify, and schedule via GitHub then Buffer.
---
Use when an already-approved Shield Facebook or Google Business asset is ready to upload, verify, and schedule. Does not design or write copy. Content skills finish first. This skill is the pipe.

# Shield Facebook publish

Approved file + caption → GitHub host → HTTP 200 on the raw URL → Buffer (Facebook always; Google Business via Buffer if the direct Google path cannot schedule or is blocked). Always wait for an explicit yes before any write. Never auto-publish. Sebring before Lake Wales in every list shown to the user.

## Destinations
- `fb_sebring` — Shield Medical Group Sebring Facebook
- `fb_lakewales` — Shield Medical Group Lake Wales Facebook
- `gbp_sebring` / `gbp_lakewales` — Google Business; Buffer fallback if NOT_VETTED, PERMISSION_DENIED, or future-dated (direct Google cannot schedule)

Buffer organization `6a57efe156ba890021371a49`. Facebook channel ids: Sebring `6a57f15080cc80cdcabed00d`, Lake Wales `6a57f15080cc80cdcabed00b`. GBP Buffer channels: Sebring `6a62629ce2638b94d7c0d827`, Lake Wales `6a62629ce2638b94d7c0d826`. If a channel id is missing, rediscover via Buffer `list_channels` and update memory. Do not put tokens in chat.

## Hosting
Upload to public repo `kkundlas/smg-social-assets` on `main` as `YYYY-MM-DD/<kebab-slug>.<ext>`. One upload per publish call. Reuse that same raw URL for every destination.

Raw URL: `https://raw.githubusercontent.com/kkundlas/smg-social-assets/main/YYYY-MM-DD/<slug>.<ext>`

Logo lock: `https://raw.githubusercontent.com/kkundlas/smg-social-assets/main/brand/shield-medical-group-logo.png`

Commit as Dr. Kulmeet Kundlas `<kkundlas@shieldmedicalgroup.com>`, message `Add <slug> (YYYY-MM-DD)`.

Verify with `curl -sSLI` HTTP 200 before Buffer. Retry once after 5s. Stop if still not 200.

Never host on uguu.se, tmpfiles.org, catbox, 0x0.st, transfer.sh, or litterbox.

## Facebook types
`fb_type`: `post` (default Feed), `reel` (needs `.mp4`), `story` (expires 24h, only if asked). Reels are never `shareNow`.

## Duplicate pre-flight
Exact first-line headline match with a live post = hard stop. ≥70% word Jaccard overlap = warn and ask. Reusing a recent GitHub raw URL as live media = hard stop.

## Approval card
Show destinations (Sebring first), time in ET and UTC, full caption(s) untruncated, GitHub raw URL, `fb_type`, CTA if any. Wait. Do not proceed on silence.

## Buffer
Use the Buffer connector. Reads anytime. Any create / shareNow / update / delete needs the same approval card.

Schedule with `customScheduled` and ISO 8601 offset (`America/New_York`). Immediate is `shareNow` with a 5s stagger between destinations. Default daily Feed time is 7:30 AM ET unless Kulmeet names another time. Tuesday news reel: Sebring 8:00 AM ET, Lake Wales 8:10 AM ET.

Never silently truncate. Facebook caption warn above 2,000 characters, hard cap 63,206. GBP summary 1,500 is a hard stop and ask. GBP EVENT title 58 is a hard stop.

CTA types: LEARN_MORE (default), BOOK, CALL, SIGN_UP. Never ORDER or SHOP.

## After
Report Destination | Post ID | Scheduled ET | Result plus the single raw URL. Never silently succeed. On Buffer 401, stop and ask Kulmeet to reconnect Buffer. Do not print keys.
