#!/usr/bin/env python3
"""Self-check for studio/vo_check.py, offline: python3 studio/test_vo_check.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vo_check import caption_times, check, tokens

script = tokens("Three dead. Azerbaijan's AzerNews: three dead. Canada's CBC, a day later.")
assert check(script, tokens("3 dead azerbaijan's azer news 3 dead canada's cbc a day later")) == []        # numbers + a split name are fine
assert 'repeated "azerbaijan\'s"' in check(script, tokens("3 dead azerbaijan's azerbaijan's azerbaijan news 3 dead canada's cbc a day later"))[0]
assert check(script, tokens("3 dead azerbaijan's azernews 3 dead")) != []                                  # a dropped phrase fails

words = [(t, i * 0.5) for i, t in enumerate(tokens("three dead or twelve dead it depends which country"))]
caps = caption_times(["Three dead. Or twelve dead.", "It depends which country."], words, 6.0)
assert [c["start"] for c in caps] == [0.0, 2.5] and caps[0]["end"] == 2.5 and caps[1]["end"] == 6.0, caps   # timed to the words
print("vo_check self-check: ok")
