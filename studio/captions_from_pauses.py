#!/usr/bin/env python3
"""Time caption lines to a voiceover using its pauses (ffmpeg silencedetect).

  python3 studio/captions_from_pauses.py vo.wav dialog.txt > captions.json

dialog.txt has one caption line per line; the owner pauses ~1s between lines.
If the number of spoken chunks doesn't match the number of lines, falls back
to splitting the speech time in proportion to each line's length.
"""
import json, re, subprocess, sys

audio, dialog = sys.argv[1], sys.argv[2]
lines = [l.strip() for l in open(dialog) if l.strip()]
log = subprocess.run(["ffmpeg", "-i", audio, "-af", "silencedetect=noise=-35dB:d=0.5", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", audio],
                             capture_output=True, text=True, check=True).stdout)
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]

# Speech chunks = the gaps between silences.
edges = [0.0] + ends
chunks = [(s, e) for s, e in zip(edges, starts + [total]) if e - s > 0.2]

if len(chunks) != len(lines):
    first, last = (chunks[0][0], chunks[-1][1]) if chunks else (0.0, total)
    weights = [len(l) for l in lines]
    t, chunks = first, []
    for w in weights:
        d = (last - first) * w / sum(weights)
        chunks.append((t, t + d))
        t += d

json.dump([{"start": round(s, 2), "end": round(e, 2), "text": l} for (s, e), l in zip(chunks, lines)],
          sys.stdout, indent=1)
