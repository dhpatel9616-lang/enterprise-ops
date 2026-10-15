#!/usr/bin/env python3
"""Story ad (9:16): the story's scenes and cards fill the screen (over a blurred
copy of themselves), Robot narrates from a small corner bubble, big captions
underneath. Owner, 2026-10-13: "the robot ... should not be the focus of the ad".

  python3 studio/story_reel.py spec.json out.mp4

spec.json (paths relative to the spec file):
  {"series": "PHILOSOPHY IN 30 SECONDS",
   "audio": "vo.wav", "puppet": "robot.mp4", "captions": "captions.json",
   "top": [{"start": 0, "end": 11, "video": "highway.mp4", "credit": "Video: U.S. Department of Defense"},
           {"start": 11, "end": 13.7, "card": {"big": "GUILTY.", "small": "by the letter of the law", "accent": "#E5484D"}},
           {"start": 38.9, "end": 44, "card": {"big": "Legal Positivism", "small": "The Sovereign · link in bio", "logo": true}}]}

Tie scenes to the voice instead of seconds (owner, 2026-10-14: images drifted
from the voiceover): give "at": N (the caption line, from 0, where the scene
starts) and leave out start/end; each scene runs until the next one starts.
Captions must come from studio/vo_check.py (timed to the spoken words).
  {"at": 0, "video": "airport.mp4"}, {"at": 3, "card": {...}}, {"at": 9, "image": "ga-home.png"}
"image" = a still (for example the product's own page) shown full-window.

puppet = Robot rendered WITHOUT captions (`render_puppet.py --layout tall`); only the head is used.
Videos are slowed (or looped) to fill their slot; cards are rendered once.
"""
import json, shutil, subprocess, sys, tempfile, textwrap
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).parent
W, H, FPS = 1080, 1920, 30
TOP_Y, TOP_H = 170, 1215         # the scene window (8:9, ~1.6x upscale of a 768p clip)
PIP = 260                        # Robot bubble size
BG, CREAM, MIST = "#0A1522", "#F3EDE0", "#AEB9D3"


def dur(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                                capture_output=True, text=True, check=True).stdout)


def card_png(card, out):
    big = textwrap.wrap(card["big"], 16)
    size = 130 if len(big) == 1 else 100
    y0 = TOP_H / 2 - (len(big) - 1) * size * 0.55 + (0 if not card.get("small") else -30)
    logo = ""
    if card.get("logo"):
        import base64
        b64 = base64.b64encode((HERE / "brand" / "sovereign-logo.png").read_bytes()).decode()
        logo = f'<image href="data:image/png;base64,{b64}" x="{W / 2 - 160}" y="{TOP_H / 2 - 380}" width="320" height="210"/>'
        y0 += 60
    lines = "".join(f'<text x="{W / 2}" y="{y0 + i * size * 1.1:.0f}" font-family="Oswald" font-weight="bold" font-size="{size}" '
                    f'fill="{card.get("accent", CREAM)}" text-anchor="middle">{escape(l)}</text>' for i, l in enumerate(big))
    small = (f'<text x="{W / 2}" y="{y0 + len(big) * size * 1.1 + 10:.0f}" font-family="EB Garamond" font-size="56" fill="{MIST}" '
             f'text-anchor="middle">{escape(card["small"])}</text>') if card.get("small") else ""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{TOP_H}"><rect width="{W}" height="{TOP_H}" fill="#101C30"/>'
           f'<rect x="0" y="0" width="{W}" height="{TOP_H}" fill="none" stroke="#2A3A57" stroke-width="4"/>{logo}{lines}{small}</svg>')
    (out.with_suffix(".svg")).write_text(svg)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out.with_suffix(".svg")), str(out)], check=True)


def main(spec_path, out):
    base = Path(spec_path).parent
    spec = json.loads(Path(spec_path).read_text())
    total = dur(base / spec["audio"])
    caps = json.loads((base / spec["captions"]).read_text())
    top = spec["top"]
    for seg in top:  # "at": caption line -> start time of that spoken line
        if "at" in seg:
            seg["start"] = caps[seg["at"]]["start"]
    for seg, nxt in zip(top, top[1:] + [None]):
        seg.setdefault("end", nxt["start"] if nxt else total)
    tmp = Path(tempfile.mkdtemp())
    try:
        # Scenes and cards are composed into one window first, then laid over a blurred, dimmed copy of
        # that same window, so the whole 9:16 frame is the story.
        inputs = ["-f", "lavfi", "-i", f"color=c={BG}:s={W}x{TOP_H}:r={FPS}:d={total:.2f}",
                  "-i", str(base / spec["puppet"]), "-i", str(base / spec["audio"])]
        graph, last, n = [], "0:v", 3
        for i, seg in enumerate(top):
            a, b = seg["start"], min(seg["end"], total)
            if "video" in seg:
                src = base / seg["video"]
                stretch = max(1.0, min((b - a) / dur(src), 2.5))
                inputs += ["-stream_loop", "-1", "-i", str(src)]
                graph.append(f"[{n}:v]setpts={stretch:.3f}*(PTS-STARTPTS),scale={W}:{TOP_H}:force_original_aspect_ratio=increase,"
                             f"crop={W}:{TOP_H},trim=duration={b - a:.2f},setpts=PTS-STARTPTS+{a:.2f}/TB[s{i}]")
            elif "image" in seg:
                inputs += ["-loop", "1", "-t", f"{b:.2f}", "-i", str(base / seg["image"])]
                # Fill the width and keep the TOP of the image (a page screenshot's title area).
                graph.append(f"[{n}:v]scale={W}:{TOP_H}:force_original_aspect_ratio=increase,crop={W}:{TOP_H}:(iw-{W})/2:0,format=rgba[s{i}]")
            else:
                png = tmp / f"card{i}.png"
                card_png(seg["card"], png)
                inputs += ["-loop", "1", "-t", f"{b:.2f}", "-i", str(png)]
                graph.append(f"[{n}:v]format=rgba[s{i}]")
            graph.append(f"[{last}][s{i}]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})':eof_action=pass[v{i + 1}]")
            last, n = f"v{i + 1}", n + 1
            if seg.get("credit"):  # real footage names its source on screen (content-mix)
                (tmp / f"credit{i}.txt").write_text(seg["credit"])
                graph.append(f"[{last}]drawtext=expansion=none:fontfile={HERE / 'fonts/Oswald-Bold.ttf'}:textfile={tmp / f'credit{i}.txt'}:"
                             f"fontsize=30:fontcolor=white@0.85:borderw=2:bordercolor=black:x=28:y=h-56:"
                             f"enable='between(t,{a:.2f},{b:.2f})'[cr{i}]")
                last = f"cr{i}"
        # Robot: just the head (from the tall puppet frame), in a round bubble with a thin ring, bottom right of the scene.
        r = PIP // 2
        graph += [f"[{last}]split[w1][w2]",
                  f"[w1]scale=-2:{H},crop={W}:{H},boxblur=40,eq=brightness=-0.04:saturation=1.2[bg]", f"[bg][w2]overlay=0:{TOP_Y}[v]",
                  f"[1:v]crop=640:640:220:430,scale={PIP}:{PIP},format=rgba,"
                  f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(lt(hypot(X-{r},Y-{r}),{r - 6}),255,0)'[head]",
                  f"color=c={MIST}:s={PIP}x{PIP},format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':"
                  f"a='if(lt(hypot(X-{r},Y-{r}),{r}),255,0)'[ring]",
                  f"[ring][head]overlay=0:0:shortest=1[pip]",
                  f"[v][pip]overlay={W - PIP - 30}:{TOP_Y + TOP_H - PIP // 2 - 40}:shortest=1[vr]"]
        last = "vr"
        # Series label above the scene window, captions below it (pre-wrapped; textfile avoids escaping).
        if spec.get("series"):
            (tmp / "series.txt").write_text(spec["series"])
            graph.append(f"[{last}]drawtext=expansion=none:fontfile={HERE / 'fonts/Oswald-Bold.ttf'}:textfile={tmp / 'series.txt'}:"
                         f"fontsize=46:fontcolor={MIST}:borderw=3:bordercolor=black:x=(w-text_w)/2:y=80[vs]")
            last = "vs"
        for i, c in enumerate(caps):
            for j, line in enumerate(textwrap.wrap(c["text"], 28)[:4]):
                f = tmp / f"cap{i}_{j}.txt"
                f.write_text(line)
                graph.append(f"[{last}]drawtext=expansion=none:fontfile={HERE / 'fonts/Oswald-Bold.ttf'}:textfile={f}:fontsize=72:fontcolor=white:"
                             f"borderw=5:bordercolor=black:x=(w-text_w)/2:y={TOP_Y + TOP_H + 120 + j * 82}:enable='gte(t,{c['start']:.2f})*lt(t,{c['end']:.2f})'[c{i}_{j}]")
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
