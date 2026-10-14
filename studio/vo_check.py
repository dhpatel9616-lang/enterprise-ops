#!/usr/bin/env python3
"""Listen to a voiceover and check it says the script, word for word, then time
the captions to the words actually spoken (owner, 2026-10-14: the AI voice
stuttered "Azerbaijan's, Azerbaijan's" and the pause-guessed captions and scenes
drifted off the voice).

  python3 studio/vo_check.py vo.wav lines.txt captions.json

lines.txt = the caption lines (true spellings). Exit 0 = passed and
captions.json written; exit 1 = the voice doesn't match (the reason is printed):
re-run studio/ai_voice.py (each take is different) and check again. Uses the
free faster-whisper model (pip install faster-whisper; ~150 MB, cached).
"""
import difflib, json, re, sys

NUMBER_WORDS = set("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
                   "seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand "
                   "million billion percent".split())


def tokens(text):
    return re.findall(r"[a-z0-9']+", text.lower().replace("-", " "))


def is_number(t):
    return t.isdigit() or t in NUMBER_WORDS or re.fullmatch(r"\d+(st|nd|rd|th|s)", t)


def check(script_tokens, heard):
    """Problems with what was heard vs the script; [] = fine. Numbers are skipped
    (the model writes '3' for 'three'); everything else must match."""
    a = [t for t in script_tokens if not is_number(t)]
    b, vocab = [], set(a)
    for t in (t for t in heard if not is_number(t)):  # "azer news" heard for "AzerNews" counts as one word
        if b and b[-1] + t in vocab and b[-1] not in vocab:
            b[-1] += t
        else:
            b.append(t)
    problems = []
    for i in range(1, len(b)):  # a stutter: the same word twice in a row that the script doesn't have
        if b[i] == b[i - 1] and len(b[i]) > 2 and not any(a[j] == a[j - 1] == b[i] for j in range(1, len(a))):
            problems.append(f'repeated "{b[i]}"')
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal" and max(i2 - i1, j2 - j1) >= 3:
            problems.append(f'script "{" ".join(a[i1:i2])}" but heard "{" ".join(b[j1:j2])}"')
    if sm.ratio() < 0.85:
        problems.append(f"only {sm.ratio():.0%} of the words match")
    return problems


def caption_times(lines, words, total):
    """Each caption line starts when its first word is spoken (script tokens
    aligned to heard words); it ends when the next line starts."""
    flat, owner = [], []
    for n, line in enumerate(lines):
        for t in tokens(line):
            flat.append(t)
            owner.append(n)
    heard = [w[0] for w in words]
    starts = {}
    for i1, j1, size in difflib.SequenceMatcher(None, flat, heard, autojunk=False).get_matching_blocks():
        for k in range(size):
            starts.setdefault(owner[i1 + k], words[j1 + k][1])
    caps, prev = [], 0.0
    for n, line in enumerate(lines):
        start = max(starts.get(n, prev), prev)
        caps.append({"start": round(start, 2), "text": line})
        prev = start
    for c, nxt in zip(caps, caps[1:] + [{"start": total}]):
        c["end"] = nxt["start"]
    return caps


def main(audio, lines_path, out):
    from faster_whisper import WhisperModel
    lines = [l.strip() for l in open(lines_path) if l.strip()]
    segs, info = WhisperModel("base.en", device="cpu", compute_type="int8").transcribe(audio, word_timestamps=True)
    words = [(t, w.start) for s in segs for w in s.words for t in tokens(w.word)]
    problems = check([t for l in lines for t in tokens(l)], [w[0] for w in words])
    if problems:
        print("vo_check: FAILED: " + "; ".join(problems))
        print("vo_check: heard: " + " ".join(w[0] for w in words))
        sys.exit(1)
    caps = caption_times(lines, words, round(info.duration, 2))
    json.dump(caps, open(out, "w"), indent=1)
    print(f"vo_check: passed; {len(caps)} captions timed to the voice -> {out}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
