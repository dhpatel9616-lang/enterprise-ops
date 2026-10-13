#!/usr/bin/env python3
"""Story ad (9:16): scenes and story cards on top, Robot narrating below,
big captions underneath (campaigns/launch-campaign.md, owner 2026-10-13).

  python3 studio/story_reel.py spec.json out.mp4

spec.json (paths relative to the spec file):
  {"series": "PHILOSOPHY IN 30 SECONDS",
   "audio": "vo.wav", "puppet": "robot.mp4", "captions": "captions.json",
   "top": [{"start": 0, "end": 11, "video": "highway.mp4"},
           {"start": 11, "end": 13.7, "card": {"big": "GUILTY.", "small": "by the letter of the law", "accent": "#E5484D"}},
           {"start": 38.9, "end": 44, "card": {"big": "Legal Positivism", "small": "The Sovereign · link in bio", "logo": true}}]}

puppet = Robot rendered WITHOUT captions (`render_puppet.py --layout tall`).
Videos are slowed (or looped) to fill their slot; cards are rendered once.
"""
import json, shutil, subprocess, sys, tempfile, textwrap
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).parent
W, H, FPS = 1080, 1920, 30
TOP_Y, TOP_H = 150, 608          # the 16:9 scene window
BG, CREAM, MIST = "#0A1522", "#F3EDE0", "#AEB9D3"


def dur(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                                capture_output=True, text=True, check=True).stdout)


def card_png(card, out):
    big = textwrap.wrap(card["big"], 16)
    size = 110 if len(big) == 1 else 84
    y0 = TOP_H / 2 - (len(big) - 1) * size * 0.55 + (0 if not card.get("small") else -30)
    logo = ""
    if card.get("logo"):
        import base64
        b64 = base64.b64encode((HERE / "brand" / "sovereign-logo.png").read_bytes()).decode()
        logo = f'<image href="data:image/png;base64,{b64}" x="{W / 2 - 110}" y="20" width="220" height="144"/>'
        y0 += 60
    lines = "".join(f'<text x="{W / 2}" y="{y0 + i * size * 1.1:.0f}" font-family="Oswald" font-weight="bold" font-size="{size}" '
                    f'fill="{card.get("accent", CREAM)}" text-anchor="middle">{escape(l)}</text>' for i, l in enumerate(big))
    small = (f'<text x="{W / 2}" y="{y0 + len(big) * size * 1.1 + 10:.0f}" font-family="EB Garamond" font-size="48" fill="{MIST}" '
             f'text-anchor="middle">{escape(card["small"])}</text>') if card.get("small") else ""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{TOP_H}"><rect width="{W}" height="{TOP_H}" fill="#101C30"/>'
           f'<rect x="0" y="0" width="{W}" height="{TOP_H}" fill="none" stroke="#2A3A57" stroke-width="4"/>{logo}{lines}{small}</svg>')
    (out.with_suffix(".svg")).write_text(svg)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out.with_suffix(".svg")), str(out)], check=True)


def main(spec_path, out):
    base = Path(spec_path).parent
    spec = json.loads(Path(spec_path).read_text())
    total = dur(base / spec["audio"])
    tmp = Path(tempfile.mkdtemp())
    try:
        inputs = ["-f", "lavfi", "-i", f"color=c={BG}:s={W}x{H}:r={FPS}:d={total:.2f}",
                  "-i", str(base / spec["puppet"]), "-i", str(base / spec["audio"])]
        # Robot: crop the character out of the full puppet frame, scale, park it below the scene window.
        # Backdrop = Robot's own scene, blurred and dimmed, so the cropped character has no visible box edge.
        graph = [f"[1:v]split[p1][p2]", f"[p1]boxblur=30,eq=brightness=-0.06[bgp]",
                 f"[p2]crop=1080:1180:0:330,scale=918:-2[robot]", "[0:v][bgp]overlay=0:0[bg]", "[bg][robot]overlay=81:770[v0]"]
        last, n = "v0", 3
        for i, seg in enumerate(spec["top"]):
            a, b = seg["start"], min(seg["end"], total)
            if "video" in seg:
                src = base / seg["video"]
                stretch = max(1.0, min((b - a) / dur(src), 2.5))
                inputs += ["-stream_loop", "-1", "-i", str(src)]
                graph.append(f"[{n}:v]setpts={stretch:.3f}*(PTS-STARTPTS),scale={W}:{TOP_H}:force_original_aspect_ratio=increase,"
                             f"crop={W}:{TOP_H},trim=duration={b - a:.2f},setpts=PTS-STARTPTS+{a:.2f}/TB[s{i}]")
            else:
                png = tmp / f"card{i}.png"
                card_png(seg["card"], png)
                inputs += ["-loop", "1", "-t", f"{b:.2f}", "-i", str(png)]
                graph.append(f"[{n}:v]format=rgba[s{i}]")
            graph.append(f"[{last}][s{i}]overlay=0:{TOP_Y}:enable='between(t,{a:.2f},{b:.2f})':eof_action=pass[v{i + 1}]")
            last, n = f"v{i + 1}", n + 1
        # Series label above the scene window, captions below Robot (pre-wrapped; textfile avoids escaping).
        if spec.get("series"):
            (tmp / "series.txt").write_text(spec["series"])
            graph.append(f"[{last}]drawtext=fontfile={HERE / 'fonts/Oswald-Bold.ttf'}:textfile={tmp / 'series.txt'}:"
                         f"fontsize=46:fontcolor={MIST}:x=(w-text_w)/2:y=70[vs]")
            last = "vs"
        for i, c in enumerate(json.loads((base / spec["captions"]).read_text())):
            for j, line in enumerate(textwrap.wrap(c["text"], 30)[:2]):
                f = tmp / f"cap{i}_{j}.txt"
                f.write_text(line)
                graph.append(f"[{last}]drawtext=fontfile={HERE / 'fonts/Oswald-Bold.ttf'}:textfile={f}:fontsize=64:fontcolor=white:"
                             f"borderw=5:bordercolor=black:x=(w-text_w)/2:y={1730 + j * 78}:enable='between(t,{c['start']:.2f},{c['end']:.2f})'[c{i}_{j}]")
                last = f"c{i}_{j}"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(graph),
                        "-map", f"[{last}]", "-map", "2:a", "-t", f"{total:.2f}", "-r", str(FPS), "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-crf", "20", "-c:a", "aac", "-movflags", "+faststart", out], check=True)
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
