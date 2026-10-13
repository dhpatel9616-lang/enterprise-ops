#!/usr/bin/env python3
"""Find free, legal footage for story ads and clips, before paying Higgsfield
(owner, 2026-10-14). Nothing is stored: we search, download only the seconds we
use, render, and the temp file goes away with the run.

  python3 studio/find_footage.py find "press conference pentagon" [--source all|pixabay|archive|nasa|commons] [-n 5]
  python3 studio/find_footage.py get URL out.mp4 [--start 12] [--len 6]

`find` prints one JSON line per hit: source, title, url (pass it to `get`),
license and the credit line to show on screen. `get` accepts the url from
`find` (archive.org and NASA pages are resolved to their video file).

Sources, cheapest legal first:
  archive  Internet Archive: public-domain films and US government video (briefings, hearings, newsreels)
  nasa     NASA video (US government work, public domain)
  commons  Wikimedia Commons: public domain / CC0 / CC BY(-SA) only (credit required)
  pixabay  Pixabay stock video (free, commercial use, no credit needed). Needs PIXABAY_API_KEY.
Network hosts: archive.org (+ its *.archive.org file servers), images-api.nasa.gov, images-assets.nasa.gov,
commons.wikimedia.org, upload.wikimedia.org, pixabay.com, cdn.pixabay.com.
"""
import argparse, json, os, re, subprocess, sys, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (WadeCapital footage finder)"}
OK_COMMONS = re.compile(r"^(public domain|pd|cc0|cc[ -]by(-sa)?( \d\.\d)?)", re.I)  # no NC/ND: we cut and publish


def get_json(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))


def q(params):
    return urllib.parse.urlencode(params, doseq=True)


def pixabay(term, n):
    key = os.environ.get("PIXABAY_API_KEY")
    if not key:
        return print("find_footage: PIXABAY_API_KEY not set; skipping Pixabay.", file=sys.stderr) or []
    hits = get_json("https://pixabay.com/api/videos/?" + q({"key": key, "q": term[:100], "per_page": max(n, 3), "safesearch": "true"}))["hits"]
    return [{"source": "pixabay", "title": h["tags"], "url": (h["videos"].get("large") or h["videos"]["medium"])["url"],
             "page": h["pageURL"], "seconds": h["duration"], "license": "Pixabay Content License", "credit": ""} for h in hits[:n]]


def archive(term, n):
    query = f'({term}) AND mediatype:movies AND (licenseurl:*publicdomain* OR collection:prelinger_library OR collection:prelinger OR collection:us_government)'
    docs = get_json("https://archive.org/advancedsearch.php?" + q({"q": query, "fl[]": ["identifier", "title", "year", "licenseurl"],
                                                                   "rows": n, "output": "json"}))["response"]["docs"]
    return [{"source": "archive", "title": f"{d.get('title')} ({d.get('year', 'n.d.')})", "url": f"https://archive.org/details/{d['identifier']}",
             "license": d.get("licenseurl") or "Public domain (Prelinger / US government collection)",
             "credit": f"Source: Internet Archive, {d.get('title')}"} for d in docs]


def nasa(term, n):
    items = get_json("https://images-api.nasa.gov/search?" + q({"q": term, "media_type": "video"}))["collection"]["items"][:n]
    return [{"source": "nasa", "title": i["data"][0]["title"], "url": i["href"], "license": "NASA media, public domain",
             "credit": "Video: NASA"} for i in items]


def commons(term, n):
    pages = get_json("https://commons.wikimedia.org/w/api.php?" + q({
        "action": "query", "format": "json", "generator": "search", "gsrsearch": f"filetype:video {term}", "gsrnamespace": 6,
        "gsrlimit": n * 3, "prop": "imageinfo", "iiprop": "url|extmetadata"})).get("query", {}).get("pages", {}).values()
    out = []
    for p in pages:
        ii = p["imageinfo"][0]
        meta = {k: re.sub(r"<[^>]+>", "", v.get("value", "")) for k, v in ii.get("extmetadata", {}).items()}
        lic = meta.get("LicenseShortName", "")
        if OK_COMMONS.match(lic) and not re.search(r"\b(nc|nd)\b", lic, re.I):
            out.append({"source": "commons", "title": p["title"][5:], "url": ii["url"], "page": ii.get("descriptionurl"), "license": lic,
                        "credit": f"{meta.get('Artist', 'Wikimedia Commons').strip()} / {lic} / Wikimedia Commons"})
    return out[:n]


def resolve(url):
    """A page or manifest from `find` -> a direct video file URL."""
    if m := re.match(r"https://archive\.org/details/([^/?#]+)", url):
        files = get_json(f"https://archive.org/metadata/{m.group(1)}")["files"]
        mp4s = sorted((f for f in files if f["name"].lower().endswith(".mp4")), key=lambda f: int(f.get("size", 0)))
        if not mp4s:
            sys.exit(f"find_footage: no MP4 in {url}")
        best = next((f for f in mp4s if "512kb" not in f["name"]), mp4s[-1])  # prefer the full-quality derivative
        return f"https://archive.org/download/{m.group(1)}/{urllib.parse.quote(best['name'])}"
    if url.endswith("collection.json"):  # NASA manifest
        links = get_json(url)
        return next((l for k in ("~orig.mp4", "~large.mp4", "~medium.mp4") for l in links if l.endswith(k)), links[0])
    return url


def get(url, out, start, length):
    """Download only the part we use (ffmpeg seeks over HTTP), re-encoded to a plain MP4 without its own audio."""
    src = resolve(url)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *(["-user_agent", UA["User-Agent"]] if src.startswith("http") else []), "-ss", str(start), "-i", src]
    subprocess.run(cmd + (["-t", str(length)] if length else []) + ["-an", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", out], check=True)
    print(out)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    sub = a.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("find")
    f.add_argument("term"), f.add_argument("--source", default="all"), f.add_argument("-n", type=int, default=5)
    g = sub.add_parser("get")
    g.add_argument("url"), g.add_argument("out"), g.add_argument("--start", type=float, default=0), g.add_argument("--len", type=float, default=8)
    a = a.parse_args()
    if a.cmd == "get":
        get(a.url, a.out, a.start, a.len)
    else:
        for name in (["archive", "nasa", "commons", "pixabay"] if a.source == "all" else [a.source]):
            try:
                for hit in globals()[name](a.term, a.n):
                    print(json.dumps(hit))
            except Exception as e:  # one source down shouldn't stop the others
                print(f"find_footage: {name} failed ({e}); trying the next source.", file=sys.stderr)
