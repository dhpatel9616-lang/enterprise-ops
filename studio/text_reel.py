#!/usr/bin/env python3
"""Branded 9:16 promo video (Reels / TikTok / Shorts) from a small JSON script.

  python3 studio/text_reel.py reel.json out.mp4

reel.json:
  {"eyebrow": "THE GLOBAL AGGREGATE",
   "scenes": [{"text": "One story.", "seconds": 2.2},
              {"image": "cover.jpg", "text": "a real quote", "source": "The Sovereign, Issue 7",
               "seconds": 3.5}, ...],   # image: local file, slow push-in, text in the lower third
   "cta": {"text": "Visit The Global Aggregate", "url": "globalaggregate.org",
           "note": "optional small line, e.g. a disclosure"},
   "cta_seconds": 3.5}

Wade Capital palette (brand-voice). Silent audio track included because some
platforms reject video with no audio stream.
"""
import base64, json, shutil, subprocess, sys, tempfile, textwrap
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


def image_scene(s, k, p, uri):
    # Full-bleed photo with a slow push-in (p = 0..1 through the scene), darkened at the bottom for text.
    z = 1 + 0.08 * p
    return (f'<image href="{uri}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice" '
            f'transform="translate({W / 2} {H / 2}) scale({z:.4f}) translate({-W / 2} {-H / 2})"/>'
            f'<rect width="{W}" height="{H}" fill="url(#fade)"/>'
            + (lambda t: lines(t, *((22, 70, 1400) if len(t) < 110 else (28, 56, 1320) if len(t) < 190 else (34, 46, 1250)), CREAM, opacity=k, dy=30 * (1 - k)))(s.get("text", ""))  # long quotes shrink to stay clear of the source line
            + (lines(s["source"], 46, 30, 1640, GOLD, "DejaVu Sans", "bold", k) if s.get("source") else ""))


def frame(spec, t, total, uris):
    ease = lambda x: 1 - (1 - min(max(x, 0), 1)) ** 3
    start, body = 0.0, ""
    for i, s in enumerate(spec["scenes"]):
        if start <= t < start + s["seconds"]:
            k = ease((t - start) / 0.45)
            body = (image_scene(s, k, (t - start) / s["seconds"], uris[i]) if s.get("image")
                    else lines(s["text"], 16, 92, 960, CREAM, opacity=k, dy=40 * (1 - k)))
        start += s["seconds"]
    if t >= start:  # call-to-action card
        k, c = ease((t - start) / 0.45), spec["cta"]
        body = (f'<rect x="90" y="{680 + 30 * (1 - k):.0f}" width="900" height="500" rx="6" fill="{NAVY}" fill-opacity="{k:.2f}" stroke="{GOLD}" stroke-opacity="{k:.2f}" stroke-width="3"/>'
                + lines(c["text"], 20, 64, 860, CREAM, opacity=k)
                + (lines(c["url"], 26, 50, 1080, GOLD, "DejaVu Sans", "bold", k) if len(c["url"]) <= 26
                   else lines(c["url"], 44, 34, 1080, GOLD, "DejaVu Sans", "bold", k))  # long URLs shrink, never break mid-word
                + (lines(c["note"], 46, 30, 1270, GRAY, "DejaVu Sans", opacity=k) if c.get("note") else ""))
    progress = W * t / total
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<defs><radialGradient id="g" cx="0.5" cy="0.45" r="0.7"><stop offset="0" stop-color="#14243B"/>'
            f'<stop offset="1" stop-color="{BG}"/></radialGradient><linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0.45" stop-color="{BG}" stop-opacity="0"/><stop offset="0.95" stop-color="{BG}" stop-opacity="0.92"/>'
            f'</linearGradient></defs><rect width="{W}" height="{H}" fill="url(#g)"/>'
            f'<rect x="440" y="300" width="200" height="3" fill="{GOLD}"/>'
            + lines(spec.get("eyebrow", ""), 40, 34, 260, GOLD, "DejaVu Sans", "bold")
            + body + f'<rect x="0" y="{H - 12}" width="{progress:.0f}" height="12" fill="{GOLD}"/></svg>')


def embed(path):
    # librsvg (inside ffmpeg) ignores linked files, so each image is shrunk to frame size once and inlined.
    jpg = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(path), "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase",
                          "-frames:v", "1", "-q:v", "4", "-f", "image2", "-c:v", "mjpeg", "-"], check=True, capture_output=True).stdout
    return "data:image/jpeg;base64," + base64.b64encode(jpg).decode()


def main(spec_path, out):
    spec = json.loads(Path(spec_path).read_text())
    total = sum(s["seconds"] for s in spec["scenes"]) + spec.get("cta_seconds", 3.5)
    base = Path(spec_path).parent  # image paths are relative to the spec file
    uris = [embed(base / s["image"]) if s.get("image") else None for s in spec["scenes"]]
    # Frames with a photo are a few hundred KB, so render in 10 s batches and delete each batch once encoded.
    tmp, n, parts = Path(tempfile.mkdtemp()), int(total * FPS), []
    try:
        for c, start in enumerate(range(0, n, 300)):
            d = tmp / f"c{c}"
            d.mkdir()
            for i in range(start, min(start + 300, n)):
                (d / f"{i - start:05d}.svg").write_text(frame(spec, i / FPS, total, uris))
            parts.append(tmp / f"c{c}.mp4")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(d / "%05d.svg"),
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", str(parts[-1])], check=True)
            shutil.rmtree(d)
        (tmp / "list.txt").write_text("".join(f"file '{x}'\n" for x in parts))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"),
                        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest", "-c:v", "copy", "-c:a", "aac",
                        "-movflags", "+faststart", out], check=True)
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
