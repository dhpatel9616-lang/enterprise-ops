#!/usr/bin/env python3
"""The week's clips as one 16:9 long-form video for YouTube @WadeCapitalClips
(owner, 2026-11-10: clipping should run long-form on YouTube too). Each clip is
re-cut from its original public-domain source, so the montage is full-width.

  python3 studio/clip_montage.py montage.json out.mp4

montage.json: {"title": "This Week in the Archive", "clips": [
   {"url": "<find_footage url>", "start": 12, "len": 30, "title": "JFK: We choose to go to the Moon (1962)",
    "credit": "NASA"}, ...]}       # 3-10 clips; the url/start/len saved in each posted clip.json
"""
import json, shutil, subprocess, sys, tempfile, textwrap
from pathlib import Path

HERE = Path(__file__).parent
W, H, FPS = 1920, 1080, 30
FONT = HERE / "fonts/Oswald-Bold.ttf"
HANDLE = "@WadeCapitalClips"


def run(*a):
    subprocess.run(a, check=True)


def card(tmp, name, big, small, secs=3):
    (tmp / f"{name}_b.txt").write_text("\n".join(textwrap.wrap(big, 34)[:3]))
    (tmp / f"{name}_s.txt").write_text(small)
    out = tmp / f"{name}.mp4"
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=#0A1522:s={W}x{H}:r={FPS}:d={secs}",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", str(secs),
        "-vf", f"drawtext=expansion=none:fontfile={FONT}:textfile={tmp / f'{name}_b.txt'}:fontsize=84:fontcolor=white:line_spacing=18:x=(w-text_w)/2:y=(h-text_h)/2-60,"
               f"drawtext=expansion=none:fontfile={FONT}:textfile={tmp / f'{name}_s.txt'}:fontsize=40:fontcolor=#AEB9D3:x=(w-text_w)/2:y=h/2+140",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", "44100", "-ac", "2", str(out))
    return out


def segment(tmp, i, c):
    raw = tmp / f"raw{i}.mp4"
    run(sys.executable, str(HERE / "find_footage.py"), "get", c["url"], str(raw), "--start", str(c["start"]), "--len", str(c["len"]), "--keep-audio")
    (tmp / f"t{i}.txt").write_text(c["title"])
    (tmp / f"c{i}.txt").write_text(f"Source: {c['credit']}   ·   {HANDLE}")
    out = tmp / f"seg{i}.mp4"
    has_audio = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", str(raw)],
                               capture_output=True, text=True).stdout.strip() != ""
    audio = "[0:a]" if has_audio else "[1:a]"  # silent films get a silent track so the concat stays in sync
    secs = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(raw)],
                          capture_output=True, text=True, check=True).stdout.strip()
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
        "-filter_complex",
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black,fps={FPS},"
        f"drawtext=expansion=none:fontfile={FONT}:textfile={tmp / f't{i}.txt'}:fontsize=46:fontcolor=white:borderw=4:bordercolor=black:x=60:y=50,"
        f"drawtext=expansion=none:fontfile={FONT}:textfile={tmp / f'c{i}.txt'}:fontsize=30:fontcolor=#D9DDE6:borderw=3:bordercolor=black:x=60:y=h-80[v];"
        f"{audio}aresample=44100,aformat=channel_layouts=stereo[a]",
        "-map", "[v]", "-map", "[a]", "-t", secs, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", "44100", "-ac", "2", str(out))
    return out


def main(spec_path, out):
    spec = json.loads(Path(spec_path).read_text())
    tmp = Path(tempfile.mkdtemp())
    try:
        parts = [card(tmp, "intro", spec["title"], f"{len(spec['clips'])} moments from the public record")]
        for i, c in enumerate(spec["clips"]):
            parts.append(segment(tmp, i, c))
        parts.append(card(tmp, "outro", "Follow for a new clip every day", HANDLE, 4))
        (tmp / "list.txt").write_text("".join(f"file '{p}'\n" for p in parts))
        run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", str(out))
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
