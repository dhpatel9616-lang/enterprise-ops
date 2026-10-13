#!/usr/bin/env python3
"""Self-check for studio/find_footage.py, offline (fake API answers): python3 studio/test_find_footage.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import find_footage as ff

def page(lic):
    return {"title": f"File:{lic}.webm", "imageinfo": [{"url": f"https://u/{lic}.webm", "extmetadata": {"LicenseShortName": {"value": lic}, "Artist": {"value": "<a>Jo</a>"}}}]}

ff.get_json = lambda url: {"query": {"pages": {i: page(l) for i, l in enumerate(["CC BY-SA 4.0", "Public domain", "CC BY-NC 2.0", "CC BY-ND 3.0", "Fair use"])}}}
assert [h["license"] for h in ff.commons("protest", 5)] == ["CC BY-SA 4.0", "Public domain"]  # no NC/ND/fair use
assert ff.commons("protest", 5)[0]["credit"] == "Jo / CC BY-SA 4.0 / Wikimedia Commons"

ff.get_json = lambda url: {"files": [{"name": "a_512kb.mp4", "size": "10"}, {"name": "a.mp4", "size": "90"}, {"name": "a.ogv", "size": "99"}]}
assert ff.resolve("https://archive.org/details/abc") == "https://archive.org/download/abc/a.mp4"
ff.get_json = lambda url: ["https://n/x~small.mp4", "https://n/x~orig.mp4"]
assert ff.resolve("https://n/collection.json") == "https://n/x~orig.mp4"
assert ff.resolve("https://cdn.pixabay.com/v.mp4") == "https://cdn.pixabay.com/v.mp4"
print("find_footage self-check: ok")
