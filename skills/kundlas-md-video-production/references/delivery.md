# Review, mastering, and verified delivery

## Review copy first

Export a small H.264 review copy before the archival master. Optimize it for mobile playback and easy sharing while retaining the exact edit and representative audio.

Recommended review characteristics:

- 1920×1080 or 1280×720;
- H.264 video and AAC audio;
- fast-start metadata when supported;
- moderate bitrate suitable for phone streaming;
- filename containing `REVIEW`, version, and date when useful.

Do not use a multi-gigabyte 4K file as the primary review artifact.

## 4K master

After the review edit is approved, export:

- 3840×2160;
- approved frame rate, normally 30 fps;
- high-quality H.264 or another explicitly requested mastering codec;
- AAC 48 kHz stereo unless the destination requires otherwise;
- hardwired YouTube loudness: −14 LUFS integrated, true peak ≤ −1 dBTP, AAC 48 kHz (Descript −16 is podcast only; do not ship −16);
- no music unless approved.

Render motion assets at true 4K or use vector sources before the master export. Do not simply upscale low-resolution final graphics.

Write the verified master to `<Borumi workspace>/<video project>/06 Exports/Master/`. Do not leave the only master in a cache, temporary render folder, application library, or the shared Borumi root.

## Captions and chapters

Deliver two separate text systems:

- semantic overlays burned into the edit at selected moments;
- corrected verbatim SRT for YouTube accessibility.

Validate SRT numbering, timestamp order, overlaps, readable segmentation, spelling, and final duration. Deliver chapter titles with final post-edit timestamps beginning at `00:00` when intended for YouTube.

## Verification

Run:

- media metadata probe;
- audio loudness check when tooling exists;
- full-file decode check;
- spot playback at start, chapter transitions, and ending;
- checksum or exact-size record for large masters when practical.

## 4K delivery (locked 2026-08-24)

When ffprobe shows 3840×2160, do both without waiting to be asked:

1. YouTube — upload to Kundlas MD as unlisted unless he names another visibility. Send him the watch URL.
2. Descript — import the same 4K file into that job’s existing Descript project as deliver media (`04 Deliver/…-4K.mp4`). Do not drop it on the talking-head composition. Do not publish_project unless he asks.


## 4K encode → YouTube → Descript → send links (locked 2026-08-24)

Do this as soon as a 4K file exists. Do not wait to be asked.

1. Encode the approved review to 3840×2160 H.264, AAC 48 kHz, same edit, −14 LUFS / TP ≤ −1. Copy audio if already loudnormed.
2. Probe the file. Do not call it 4K unless width=3840 and height=2160.
3. Upload that exact file to Kundlas MD YouTube as unlisted (unless he named another visibility). Title from the video title. Not made for kids. Monetization off unless he asks.
4. Copy the watch URL (youtu.be or youtube.com/watch?v=) into chat immediately.
5. Import the same 4K file into that job’s existing Descript project as `04 Deliver/<title>-4K.mp4`. Direct upload: declare file_size, PUT, wait_for_job, confirm result.status=success and duration.
6. Do not append it to the talking-head composition. Do not publish_project unless he asks.
7. Send the Descript project URL in the same turn as the YouTube link if both are ready; otherwise send YouTube first, Descript as soon as import succeeds.

Large PUTs can take minutes. Do not claim Descript done until the import job reports success.

## Delivery manifest

Record:

- title and version;
- source project and timeline revision;
- master and review paths;
- dimensions, fps, duration, codecs, loudness, and size;
- SRT and chapter paths;
- QC and decode status;
- destination, project ID, job ID, completion status, and link;
- intentionally omitted deliverables;
- accepted limitations.
