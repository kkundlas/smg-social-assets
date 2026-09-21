#!/usr/bin/env python3
"""Assemble Six Pillars Seedance chalk clips → Shield FB + Kundlas TT MP4s."""
from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/workspace/pillars-reel/2026-09-21-six-pillars")
CLIPS = ROOT / "clips"
MUSIC = ROOT / "rhythmic-reverie.mp3"  # dramatic bed that pops
BRAND = ROOT / "brand"
QC = ROOT / "qc"

W, H = 1080, 1920
FADE = 0.4
MUSIC_VOL = 0.255
FADE_IN = 0.5
FADE_OUT = 0.8
EXTRA_HOLD = 2.5  # freeze last frame so chalk draw plays then holds
FPS = 30
SAFE_BOTTOM = 300  # platform chrome; keep critical text above this

NAMES = [
    "00-opener",
    "01-nutrition",
    "02-activity",
    "03-stress",
    "04-sleep",
    "05-substances",
    "06-social",
    "07-cta",
]

# Short ALL CAPS chapter titles (burned only if chalk space allows; mid-board safe)
TITLES = [
    "",  # opener already has full title in chalk
    "NUTRITION",
    "PHYSICAL ACTIVITY",
    "STRESS MANAGEMENT",
    "RESTORATIVE SLEEP",
    "AVOID RISKY SUBSTANCES",
    "POSITIVE SOCIAL CONNECTIONS",
    "",  # CTA chalk carries message
]

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
YELLOW = (245, 209, 10)
TEAL = (18, 52, 59)


def run(cmd):
    print("+", " ".join(str(c) for c in cmd[:18]), ("..." if len(cmd) > 18 else ""))
    subprocess.check_call(cmd)


def dur(p: Path) -> float:
    return float(
        subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(p),
            ],
            text=True,
        ).strip()
    )


def make_logo_card(logo_path: Path, out: Path, card_w: int = 360, card_h: int = 120) -> Path:
    """White rounded card with logo centered — top-left chrome."""
    logo = Image.open(logo_path).convert("RGBA")
    # Fit logo inside card with padding
    pad = 14
    max_w, max_h = card_w - 2 * pad, card_h - 2 * pad
    lw, lh = logo.size
    scale = min(max_w / lw, max_h / lh)
    nw, nh = max(1, int(lw * scale)), max(1, int(lh * scale))
    logo = logo.resize((nw, nh), Image.Resampling.LANCZOS)

    card = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((0, 0, card_w - 1, card_h - 1), radius=18, fill=(255, 255, 255, 255))
    x = (card_w - nw) // 2
    y = (card_h - nh) // 2
    card.alpha_composite(logo, (x, y))
    out.parent.mkdir(parents=True, exist_ok=True)
    card.save(out)
    return out


def make_disclaimer_bar(out: Path) -> Path:
    """Yellow pill near top of bottom-safe zone."""
    text = "EDUCATIONAL ONLY · TALK TO YOUR CLINICIAN"
    font = ImageFont.truetype(FONT, 28)
    # Measure
    tmp = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(tmp)
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 28, 14
    bw, bh = tw + 2 * pad_x, th + 2 * pad_y
    img = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, bw - 1, bh - 1), radius=bh // 2, fill=YELLOW + (245,))
    # dark text for contrast on yellow
    draw.text((pad_x, pad_y - 2), text, font=font, fill=TEAL + (255,))
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def brand_clip(
    src: Path,
    logo_card: Path,
    disc: Path | None,
    title: str,
    out: Path,
    *,
    show_disclaimer: bool = True,
) -> float:
    """Scale to 1080x1920, overlay logo (+ optional disclaimer / title).

    CTA (07): logo only — chalk already has EDUCATIONAL ONLY + CTA copy;
    yellow disclaimer pill would sit on chalk diagrams.
    """
    d = dur(src)
    filters = [
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
        f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x12343B,"
        f"setsar=1,fps={FPS},format=rgba[base]",
        "[1:v]format=rgba[lg]",
        f"[base][lg]overlay=36:36:format=auto[v1]",
    ]
    inputs = ["-i", str(src), "-i", str(logo_card)]
    map_out = "[v1]"

    if show_disclaimer and disc is not None:
        # thin yellow pill at top of bottom chrome (~H - SAFE_BOTTOM = 1620)
        filters.append("[2:v]format=rgba[dc]")
        filters.append(
            f"[v1][dc]overlay=(W-w)/2:{H - SAFE_BOTTOM}:format=auto[v2]"
        )
        inputs += ["-i", str(disc)]
        map_out = "[v2]"

    if title:
        t = title.replace(":", "\\:").replace("'", "\\'")
        filters.append(
            f"{map_out}drawtext=fontfile={FONT}:text='{t}':"
            f"fontsize=36:fontcolor=0xF5D10A:borderw=2:bordercolor=0x0C2428@0.85:"
            f"x=36:y=170[vtxt]"
        )
        map_out = "[vtxt]"

    # Freeze last frame EXTRA_HOLD so chalk draw-on finishes, then holds (~+2.5s)
    filters.append(
        f"{map_out}tpad=stop_mode=clone:stop_duration={EXTRA_HOLD},"
        f"fps={FPS},format=yuv420p[vout]"
    )
    map_out = "[vout]"
    target = d + EXTRA_HOLD

    fc = ";".join(filters)
    run(
        [
            "ffmpeg",
            "-y",
            *inputs,
            "-filter_complex",
            fc,
            "-map",
            "[vout]",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-t",
            f"{target:.6f}",
            str(out),
        ]
    )
    return dur(out)



def xfade_assemble(branded: list[Path], holds: list[float], silent: Path) -> float:
    n = len(branded)
    inputs: list[str] = []
    for p in branded:
        inputs += ["-i", str(p)]
    filter_parts = []
    prev = "[0:v]"
    cum = 0.0
    for i in range(1, n):
        cum += holds[i - 1]
        offset = cum - i * FADE
        outlab = f"[v{i}]" if i < n - 1 else "[vout]"
        filter_parts.append(
            f"{prev}[{i}:v]xfade=transition=fade:duration={FADE}:offset={offset:.3f}{outlab}"
        )
        prev = outlab
    total = sum(holds) - (n - 1) * FADE
    vf = ";".join(filter_parts)
    print("holds", holds, "expected", total)
    run(
        [
            "ffmpeg",
            "-y",
            *inputs,
            "-filter_complex",
            vf,
            "-map",
            "[vout]",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-an",
            "-t",
            f"{total:.3f}",
            str(silent),
        ]
    )
    return dur(silent)


def mux_music(silent: Path, out: Path, total: float) -> float:
    af = (
        f"atrim=0:{total:.3f},asetpts=PTS-STARTPTS,"
        f"afade=t=in:st=0:d={FADE_IN},"
        f"afade=t=out:st={max(0.0, total - FADE_OUT):.3f}:d={FADE_OUT},"
        f"volume={MUSIC_VOL}"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(silent),
            "-i",
            str(MUSIC),
            "-filter_complex",
            f"[1:a]{af}[a]",
            "-map",
            "0:v:0",
            "-map",
            "[a]",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-ar",
            "44100",
            "-ac",
            "2",
            "-shortest",
            "-movflags",
            "+faststart",
            str(out),
        ]
    )
    return dur(out)


def build_variant(logo_src: Path, label: str, out_name: str) -> Path:
    work = ROOT / f"_branded_{label}"
    work.mkdir(parents=True, exist_ok=True)
    logo_card = make_logo_card(logo_src, work / "logo-card.png")
    disc = make_disclaimer_bar(work / "disclaimer.png")

    branded: list[Path] = []
    holds: list[float] = []
    for name, title in zip(NAMES, TITLES):
        src = CLIPS / f"{name}.mp4"
        if not src.exists():
            raise SystemExit(f"missing {src}")
        dst = work / f"{name}.mp4"
        # No burned ALL CAPS titles — chalk already carries pillar labels.
        # CTA: logo only (omit yellow disclaimer — chalk has EDUCATIONAL ONLY).
        is_cta = name == "07-cta"
        h = brand_clip(
            src,
            logo_card,
            disc,
            "",
            dst,
            show_disclaimer=not is_cta,
        )
        branded.append(dst)
        holds.append(h)
        print(f"branded {label} {name} {h:.3f}s disc={not is_cta}")

    silent = ROOT / f"_silent-{label}.mp4"
    total = xfade_assemble(branded, holds, silent)
    print(f"silent {label}", total)

    out = ROOT / out_name
    final = mux_music(silent, out, total)
    print(f"OUT {label}", final, out.stat().st_size, out)
    return out


def main():
    if not MUSIC.exists():
        raise SystemExit(f"missing music {MUSIC}")
    shield_logo = BRAND / "shield-logo-flat.png"
    kundlas_logo = BRAND / "kundlas-logo-flat.png"
    if not shield_logo.exists() or not kundlas_logo.exists():
        raise SystemExit("missing brand logos")

    s = build_variant(shield_logo, "shield", "Six-Pillars-Lifestyle-Shield.mp4")
    k = build_variant(kundlas_logo, "kundlas", "Six-Pillars-Lifestyle-Kundlas.mp4")
    print("DONE", s, k)


if __name__ == "__main__":
    main()
