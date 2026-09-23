# Borumi project storage and Descript handoff

Use one self-contained folder for every video edit.

## Required parent and name

- Parent: `/Users/kulmeetkundlas/Library/CloudStorage/Dropbox/Borumi`
- Project folder: `YYYY-MM-DD - <video title>`
- Create it with `scripts/create_project.py`; its default root is the required Borumi workspace.
- Never save project-specific material loose in the parent folder.
- Never reuse another video's folder, even when topics or assets overlap.

## Storage contract

Keep these durable materials inside the video-specific folder:

- source video, audio, transcript, research, and references in `01 Intake`;
- transcript decisions and dialogue cut lists in `02 Editorial`;
- chapters, card rail, media plan, and semantic caption map in `03 Plan`;
- generated and editable Napkin AI, Remotion, Hyperframes, Canva, Higgsfield, icon, photo, B-roll, and proof assets in `04 Assets`;
- Borumi/editor project files and timeline inventory in `05 Timeline`;
- review, 4K master, SRT, and chapters in `06 Exports`;
- feedback, proof frames, and QC evidence in `07 Review`;
- final delivery and external-import records in `08 Delivery`.

When a creative service requires a local temporary working directory, copy the durable editable source and approved export back into the correct `04 Assets/Chapter NN/<Tool>` folder before asset freeze. A temporary link, application cache, or cloud-only object is not the source of truth.

## Final 4K and Descript

1. Export the approved master to `06 Exports/Master/<safe-title>-FINAL-4K.mp4`.
2. Verify 3840×2160 dimensions, frame rate, codecs, duration, audio, full decode, and file size.
3. Record the verified local path and checksum in `08 Delivery/delivery-manifest.md`.
4. Create a **new Descript project** named from the final video title.
5. Upload that exact verified 4K file.
6. Wait until the import reports success; a waiting, running, stopped-without-success, or 0% state is not completion.
7. Inspect the imported media duration and project record.
8. Record the Descript project ID, import job ID, status, verification time, and direct link.

If Descript access is unavailable, mark Stage 17 `blocked_external`; preserve the verified 4K master locally and do not claim upload completion.

## Guardrails

- Do not delete, overwrite, or move an existing video project without explicit confirmation.
- Refuse to initialize into a non-empty project folder.
- Keep one final master designation; retain older versions with explicit version labels.
- Do not upload to Dropbox, Google Drive, or another destination unless the user explicitly requests it.
- Do not expose patient-identifiable or private material to external services.
