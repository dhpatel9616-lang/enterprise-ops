#!/usr/bin/env python3
"""A 9:16 clip for the clip accounts from a short real-footage segment (owner,
2026-11-04: Clip Studio's queue had nothing feeding it, so it makes its own).
The footage keeps its own sound; the title sits on top, the spoken words are
captioned (faster-whisper, when installed), and the source is credited.

  python3 studio/clip_reel.py segment.mp4 out.mp4 --title "Duck and Cover (1951)" --credit "Federal Civil Defense Administration · Internet Archive"

Get the segment first: python3 studio/find_footage.py get URL segment.mp4 --start S --len 20-45
"""
import argparse, json, shutil, subprocess, tempfile, textwrap
from pathlib import Path

HERE = Path(__file__).parent
W, H = 1080, 1920
FONT = HERE / "fonts/Oswald-Bold.ttf"
HANDLE = "@wadecapitalclips"


def caption_lines(video, words_per_line=5):
    """[(start, end, text)] from the clip's own audio; [] if faster-whisper isn't installed or nothing is said."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return []
    segs, _ = WhisperModel("small.en", device="cpu", compute_type="int8").transcribe(str(video), word_timestamps=True)
    words = [w for s in segs for w in (s.words or [])]
    lines = []
    for i in range(0, len(words), words_per_line):
        chunk = words[i:i + words_per_line]
        text = "".join(w.word for w in chunk).strip()
        if any(ch.isalpha() for ch in text):  # whisper writes "....." over music and tones
            lines.append((chunk[0].start, chunk[-1].end, text))
    return lines


def main(src, out, title, credit):
    tmp = Path(tempfile.mkdtemp())
    try:
        def txt(name, s):
            (tmp / name).write_text(s)
            return tmp / name
        dt = lambda f, size, y, color="white", extra="": (f"drawtext=expansion=none:fontfile={FONT}:textfile={f}:fontsize={size}:fontcolor={color}:"
                                                         f"borderw=4:bordercolor=black:x=(w-text_w)/2:y={y}{extra}")
        graph = [f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:5,eq=brightness=-0.25[bg]",
                 f"[0:v]scale={W}:-2[fg]", "[bg][fg]overlay=(W-w)/2:(H-h)/2[v0]"]
        lines = textwrap.wrap(title, 26)
        if len(lines) > 4:  # never cut a title mid-sentence; say so and keep the start readable
            raise SystemExit(f"clip_reel: title is too long for the screen ({len(lines)} lines); keep it under ~100 characters.")
        filters = [dt(txt(f"t{i}.txt", line), 66, 150 + i * 80) for i, line in enumerate(lines)]
        filters.append(dt(txt("credit.txt", f"Source: {credit}"), 34, H - 230, "#D9DDE6"))
        filters.append(dt(txt("handle.txt", HANDLE), 40, H - 170, "#AEB9D3"))
        for i, (a, b, line) in enumerate(caption_lines(src)):
            filters.append(dt(txt(f"c{i}.txt", line), 64, 1420, extra=f":enable='gte(t,{a:.2f})*lt(t,{b:.2f})'"))
        graph.append("[v0]" + ",".join(filters) + "[v]")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-filter_complex", ";".join(graph),
                        "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-r", "30", "-pix_fmt", "yuv420p", "-crf", "20",  # IG Reels refuse < 23 fps (old film is often 15)
                        "-c:a", "aac", "-movflags", "+faststart", str(out)], check=True)
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("src"); a.add_argument("out")
    a.add_argument("--title", required=True); a.add_argument("--credit", required=True)
    a = a.parse_args()
    main(a.src, a.out, a.title, a.credit)
