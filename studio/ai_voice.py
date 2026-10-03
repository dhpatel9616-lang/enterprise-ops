#!/usr/bin/env python3
"""Robot's AI voice: script text -> narration WAV, free and offline (Kokoro, Apache-2.0).

  python3 studio/ai_voice.py script.txt vo.wav [--voice bm_george] [--speed 1.0]

script.txt is the spoken words only (no stage directions). Blank lines become
short pauses. Model files (~350 MB) come from GitHub on first use and are
cached in /opt/kokoro (studio/setup.sh pre-downloads them).
"""
import argparse, os, re, subprocess, sys, urllib.request
from pathlib import Path

MODEL_DIR = Path(os.environ.get("KOKORO_DIR", "/opt/kokoro"))
BASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FILES = ("kokoro-v1.0.onnx", "voices-v1.0.bin")
DEFAULT_VOICE = "bm_george"  # character-bible: Robot's voice


def ensure_model():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    for f in FILES:
        if not (MODEL_DIR / f).exists():
            print(f"ai_voice: downloading {f}...", file=sys.stderr)
            urllib.request.urlretrieve(BASE + f, MODEL_DIR / f".{f}.part")
            (MODEL_DIR / f".{f}.part").rename(MODEL_DIR / f)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("script"), p.add_argument("out")
    p.add_argument("--voice", default=DEFAULT_VOICE)
    p.add_argument("--speed", type=float, default=1.0)
    a = p.parse_args()
    try:
        import numpy as np, soundfile as sf
        from kokoro_onnx import Kokoro
    except ImportError:
        sys.exit("ai_voice: run `pip install kokoro-onnx soundfile` (studio/setup.sh does this).")
    ensure_model()
    k = Kokoro(str(MODEL_DIR / FILES[0]), str(MODEL_DIR / FILES[1]))
    paras = [re.sub(r"\s+", " ", x).strip() for x in Path(a.script).read_text().split("\n\n") if x.strip()]
    chunks, sr = [], 24000
    for i, para in enumerate(paras, 1):
        audio, sr = k.create(para, voice=a.voice, speed=a.speed, lang="en-gb")
        chunks += [audio, np.zeros(int(sr * 0.45), dtype=audio.dtype)]  # breath between paragraphs
        print(f"ai_voice: paragraph {i}/{len(paras)}", file=sys.stderr)
    tmp = Path(a.out).with_suffix(".raw.wav")
    sf.write(tmp, np.concatenate(chunks), sr)
    # 44.1 kHz with loudness normalised for YouTube (-14 LUFS).
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-ar", "44100", a.out], check=True)
    tmp.unlink()
    print(a.out)


if __name__ == "__main__":
    main()
