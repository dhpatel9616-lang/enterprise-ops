#!/usr/bin/env python3
"""The Sovereign, Out Loud (9:16, ~30 s): the podcast voice reads the issue's
strongest lines over a moving sound wave, with big captions, then points to the
podcast. A $0 promo for the podcast (owner, 2026-10-14).

  python3 studio/audiogram.py spec.json out.mp4

spec.json: {"title": "Strain Theory and the “Manosphere”",
            "lines": ["We are up against one of the most sinister forces", "..."]}   # word for word from the issue
"""
import json, shutil, subprocess, sys, tempfile, textwrap
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from podcast import VOICE  # noqa: E402  (same voice as the episodes)

W, H, FPS = 1080, 1920, 30
FONT, SERIF = HERE / "fonts/Oswald-Bold.ttf", HERE / "fonts/EBGaramond-Medium.ttf"


def main(spec_path, out):
    spec = json.loads(Path(spec_path).read_text())
    tmp = Path(tempfile.mkdtemp())
    try:
        (tmp / "script.txt").write_text("\n\n".join(spec["lines"]))
        (tmp / "lines.txt").write_text("\n".join(spec["lines"]))
        subprocess.run([sys.executable, str(HERE / "ai_voice.py"), str(tmp / "script.txt"), str(tmp / "vo.wav"),
                        "--engine", "kokoro", "--voice", VOICE], check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        # 3 s end card after the voice: where to listen.
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp / "vo.wav"), "-af", "apad=pad_dur=3", str(tmp / "a.wav")], check=True)
        caps = json.loads(subprocess.run([sys.executable, str(HERE / "captions_from_pauses.py"), str(tmp / "vo.wav"), str(tmp / "lines.txt")],
                                         capture_output=True, text=True, check=True).stdout)
        total = caps[-1]["end"] + 3
        texts = {"label": "THE SOVEREIGN · OUT LOUD", "title": spec["title"], "cta1": "NEW EPISODE",
                 "cta2": "Listen free on Spotify & Apple Podcasts", "cta3": "link in bio"}
        for k, v in texts.items():
            (tmp / f"{k}.txt").write_text(v)
        dt = lambda k, font, size, color, y, extra="": (f"drawtext=expansion=none:fontfile={font}:textfile={tmp / f'{k}.txt'}:"
                                                       f"fontsize={size}:fontcolor={color}:x=(w-text_w)/2:y={y}{extra}")
        end = f":enable='gte(t,{total - 3:.2f})'"
        graph = [f"[1:a]showwaves=s={W}x360:mode=cline:rate={FPS}:colors=0xAEB9D3:draw=full,format=rgba[wave]",
                 "[2:v]scale=300:-1[logo]",
                 f"[0:v][logo]overlay=(W-w)/2:150[b0]", f"[b0][wave]overlay=0:760:enable='lt(t,{total - 3:.2f})'[b1]",
                 f"[b1]{dt('label', FONT, 44, '#AEB9D3', 380)},{dt('title', SERIF, 60, 'white', 450)},"
                 f"{dt('cta1', FONT, 110, '#E5484D', 820, end)},{dt('cta2', SERIF, 56, 'white', 980, end)},"
                 f"{dt('cta3', FONT, 52, '#AEB9D3', 1070, end)}[v0]"]
        last = "v0"
        for i, c in enumerate(caps):
            for j, line in enumerate(textwrap.wrap(c["text"], 24)[:4]):
                (tmp / f"c{i}_{j}.txt").write_text(line)
                graph.append(f"[{last}]drawtext=expansion=none:fontfile={FONT}:textfile={tmp / f'c{i}_{j}.txt'}:fontsize=76:fontcolor=white:"
                             f"borderw=5:bordercolor=black:x=(w-text_w)/2:y={1240 + j * 92}:"
                             f"enable='gte(t,{c['start']:.2f})*lt(t,{c['end']:.2f})'[c{i}_{j}]")
                last = f"c{i}_{j}"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=#1B2A4B:s={W}x{H}:r={FPS}:d={total:.2f}",
                        "-i", str(tmp / "a.wav"), "-i", str(HERE / "brand/sovereign-logo.png"),
                        "-filter_complex", ";".join(graph), "-map", f"[{last}]", "-map", "1:a", "-t", f"{total:.2f}",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-c:a", "aac", "-movflags", "+faststart", out], check=True)
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
