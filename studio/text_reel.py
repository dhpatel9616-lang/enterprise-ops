#!/usr/bin/env python3
"""Branded 9:16 text video (Reels / TikTok / Shorts) from a small JSON script.

  python3 studio/text_reel.py reel.json out.mp4

reel.json:
  {"eyebrow": "THE GLOBAL AGGREGATE",
   "scenes": [{"text": "One story.", "seconds": 2.2}, ...],
   "cta": {"text": "Visit The Global Aggregate", "url": "globalaggregate.org",
           "note": "optional small line, e.g. a disclosure"},
   "cta_seconds": 3.5}

Wade Capital palette (brand-voice). Silent audio track included because some
platforms reject video with no audio stream.
"""
import json, shutil, subprocess, sys, tempfile, textwrap
from pathlib import Path
from xml.sax.saxutils import escape

FPS, W, H = 30, 1080, 1920
BG, NAVY, GOLD, CREAM, GRAY = "#07090F", "#0F1D33", "#B8975A", "#F3EDE0", "#9AA3B2"


def lines(text, width, size, y, color, family="DejaVu Serif", weight="normal", opacity=1.0, dy=0):
    rows = textwrap.wrap(text, width)
    top = y - (len(rows) - 1) * size * 0.62
    return "".join(f'<text x="{W / 2}" y="{top + i * size * 1.24 + dy:.0f}" font-family="{family}" font-weight="{weight}" '
                   f'font-size="{size}" fill="{color}" fill-opacity="{opacity:.2f}" text-anchor="middle">{escape(r)}</text>'
                   for i, r in enumerate(rows))


def frame(spec, t, total):
    ease = lambda x: 1 - (1 - min(max(x, 0), 1)) ** 3
    start, body = 0.0, ""
    for s in spec["scenes"]:
        if start <= t < start + s["seconds"]:
            k = ease((t - start) / 0.45)
            body = lines(s["text"], 16, 92, 960, CREAM, opacity=k, dy=40 * (1 - k))
        start += s["seconds"]
    if t >= start:  # call-to-action card
        k, c = ease((t - start) / 0.45), spec["cta"]
        body = (f'<rect x="90" y="{680 + 30 * (1 - k):.0f}" width="900" height="500" rx="6" fill="{NAVY}" fill-opacity="{k:.2f}" stroke="{GOLD}" stroke-opacity="{k:.2f}" stroke-width="3"/>'
                + lines(c["text"], 20, 64, 860, CREAM, opacity=k)
                + lines(c["url"], 26, 50, 1080, GOLD, "DejaVu Sans", "bold", k)
                + (lines(c["note"], 46, 30, 1270, GRAY, "DejaVu Sans", opacity=k) if c.get("note") else ""))
    progress = W * t / total
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<defs><radialGradient id="g" cx="0.5" cy="0.45" r="0.7"><stop offset="0" stop-color="#14243B"/>'
            f'<stop offset="1" stop-color="{BG}"/></radialGradient></defs><rect width="{W}" height="{H}" fill="url(#g)"/>'
            f'<rect x="440" y="300" width="200" height="3" fill="{GOLD}"/>'
            + lines(spec.get("eyebrow", ""), 40, 34, 260, GOLD, "DejaVu Sans", "bold")
            + body + f'<rect x="0" y="{H - 12}" width="{progress:.0f}" height="12" fill="{GOLD}"/></svg>')


def main(spec_path, out):
    spec = json.loads(Path(spec_path).read_text())
    total = sum(s["seconds"] for s in spec["scenes"]) + spec.get("cta_seconds", 3.5)
    tmp = Path(tempfile.mkdtemp())
    try:
        for i in range(int(total * FPS)):
            (tmp / f"{i:05d}.svg").write_text(frame(spec, i / FPS, total))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(tmp / "%05d.svg"),
                        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest", "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-crf", "20", "-c:a", "aac", "-movflags", "+faststart", out], check=True)
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
