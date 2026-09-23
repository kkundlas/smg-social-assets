---
name: Buffer
description: >-
  Use when scheduling any approved social post through Buffer after the file is
  hosted on GitHub. Covers every connected Buffer channel, including TikTok
  @kundlasmd.
---
Use when scheduling any approved social post through Buffer after the file is hosted on GitHub. Covers every connected Buffer channel, not Facebook only.

# Buffer

Pipe for every Buffer channel: approved file → GitHub `kkundlas/smg-social-assets` `YYYY-MM-DD/<slug>.<ext>` → raw URL HTTP 200 → Buffer `create_post`. Never auto-publish. Wait for an explicit yes. Sebring before Lake Wales when both apply. TikTok is `@kundlasmd` only.

## Account
Organization: Shield Medical Group (`6a57efe156ba890021371a49`). Timezone America/New_York. Call `get_account` then `list_channels` if a channel id 404s. Never print tokens.

## Channels (live lock, Aug 30 2026)
Usable now:
- Facebook Shield Medical Group (Sebring page) `6a57f15080cc80cdcabed00d`
- Facebook Shield Medical Group - Lake Wales `6a57f15080cc80cdcabed00b`
- Google Business Sebring `6a62629ce2638b94d7c0d827`
- Google Business Lake Wales `6a62629ce2638b94d7c0d826`
- TikTok `@kundlasmd` `6a94855e065799be4656e2f0` (service tiktok, type account). Stale id `6a9448bf065799be4654baac` 404s.

Locked in Buffer (do not post until Kulmeet unlocks the channel):
- Pinterest kundlasmd `6a627894e2638b94d7c19c27`
- LinkedIn Shield Medical Group page `6a6278dbe2638b94d7c19d71`
- LinkedIn KULMEET KUNDLAS profile `6a6278dbe2638b94d7c19d72`

YouTube Kundlas MD is not in the live channel list as of 2026-08-30 (plan limit 5 usable). Do not invent a YouTube channel id. Rediscover with `list_channels` if he asks.

## Rules
Reads anytime. Any create, shareNow, update, or delete needs the approval card: channels, action, caption, media URL, time in ET and UTC.

`customScheduled` needs ISO 8601 with offset. Immediate is `shareNow` with a 5s stagger. Facebook `metadata.facebook.type` must be post, reel, or story. Reels need an mp4. Instagram/TikTok need image or video. YouTube needs video plus title and categoryId. TikTok posts go only to `6a94855e065799be4656e2f0`.

Never silently truncate. GBP summary 1500 is a hard stop. Never host media on ephemeral file hosts.

TikTok owners: use [Shield TikTok publish](sand-workflow:shield-tiktok-publish). Facebook owners: [Shield Facebook publish](sand-workflow:shield-facebook-publish).

## After
Report Destination | Channel | Post ID | Scheduled ET | Result. Never silently succeed. On 401, stop and ask to reconnect Buffer.
