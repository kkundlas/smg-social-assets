---
name: Import to media library
description: >-
  Use when parking files in the default inbox or drive Media Library with no
  timeline edit.
---
# Import to media library

Park media. Do not edit. Do not put it on a timeline unless the user asked.

## Steps

1. Confirm the drive with `get_drive_info`.
2. Choose the surface:
   - Default: **project Files** in the user’s default drop-zone project (Media Library Project). Use `import_media` with that `project_id`. **Omit** `add_compositions` and `update_compositions`.
   - Only if they clearly want the **drive** Media Library (reuse across all projects, no extra minutes later): `import_drive_media`.
3. Build `add_media` as a map of display name → entry:
   - URL import: `url` + optional `language`
   - Direct upload: `content_type` + `file_size` (+ optional `language`)
4. Look up the live schema, then call the import tool. Show `project_url` when returned.
5. Direct upload: PUT raw bytes to each `upload_url` with header `Content-Type: application/octet-stream`. Size must match the declared `file_size`. On PUT failure / cancel / never-started, call `report_upload_status`.
6. `wait_for_job`. Confirm Files-only (not on the timeline).
7. Never import YouTube URLs. Never publish.

Supported containers (official): audio WAV/MP3/AIFF/M4A/FLAC/OPUS/AAC; video MP4/M4V/MOV/WEBM/MKV; images BMP/JPEG/PNG/GIF/WEBP/HEIC. Music/lyrics are not transcribed.
