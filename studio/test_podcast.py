#!/usr/bin/env python3
"""Self-check for studio/podcast.py, offline: python3 studio/test_podcast.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import podcast

item = {"title": "8. Strain Theory", "link": "https://x.substack.com/p/8-strain", "guid": "g8", "date": "Mon, 05 Oct 2026 12:00:00 GMT",
        "summary": "A & B", "html": "<p>Good <em>morning</em>.</p><p>See https://a.b/c now.</p><p>Works Cited</p><p>Ansley, C.</p>"}
s = podcast.script(item)
assert s.startswith("The Sovereign. Strain Theory."), s
assert "Good morning." in s and "See now." in s, s          # inline tags kept, links dropped
assert "Ansley" not in s, s                                  # citations not read aloud
show = {"title": "The Sovereign", "summary": "Thought.", "link": "https://x", "author": "A", "email": "e@x"}
ep = {**item, "url": "https://h/p.mp3", "bytes": 10, "seconds": 61}
back = podcast.existing(podcast.feed_xml(show, "https://h", [ep, {**ep, "guid": "g9"}]).encode())
assert [e["guid"] for e in back] == ["g8", "g9"] and back[0]["summary"] == "A & B", back  # feed round-trips, oldest first
print("podcast self-check: ok")
