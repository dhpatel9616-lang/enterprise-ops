#!/usr/bin/env python3
"""The Sovereign as a podcast: every issue read aloud by a free male AI voice
(Kokoro), published as our own podcast feed in the public studio-videos bucket.
Spotify, Apple Podcasts and YouTube Music follow that one feed link.

  python3 studio/podcast.py [--max 3] [--dry-run]

Each run voices the oldest issues not yet in the feed (at most --max), uploads
the MP3s and replaces feed.xml (also with no new issue, so show details stay current). --dry-run writes
the episode scripts to ./podcast-dry-run/ and uploads nothing.
Needs ENTERPRISE_SUPABASE_URL / ENTERPRISE_SUPABASE_SERVICE_KEY (as upload_video.py).
"""
import argparse, base64, os, re, subprocess, sys, tempfile, urllib.error, urllib.request
import xml.etree.ElementTree as ET
from email.utils import formatdate
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from upload_video import main as upload  # noqa: E402

HERE = Path(__file__).parent
SOURCE = "https://sovereignnewsletter.substack.com/feed"
PREFIX = "podcast/sovereign"
VOICE = "am_onyx"  # Kokoro male voice; owner picked Onyx, 2026-10-14
EMAIL = "wadecapitallc@gmail.com"  # public contact in the feed; Spotify sends its verification code here (owner, 2026-10-14)
NS = {"content": "http://purl.org/rss/1.0/modules/content/", "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}
BLOCKS = {"p", "h1", "h2", "h3", "h4", "li", "blockquote", "pre"}


class Text(HTMLParser):
    """Issue HTML -> spoken paragraphs (inline tags like <em> stay inside their paragraph)."""
    def __init__(self):
        super().__init__()
        self.paras, self.buf = [], []

    def handle_starttag(self, tag, attrs=None):
        if tag in BLOCKS or tag == "br":
            self.flush()

    handle_endtag = handle_starttag

    def handle_data(self, data):
        self.buf.append(data)

    def flush(self):
        t = re.sub(r"\s+", " ", re.sub(r"https?://\S+", "", "".join(self.buf))).strip()
        if t:
            self.paras.append(t)
        self.buf = []


def script(item):
    p = Text()
    p.feed(item["html"])
    p.flush()
    body = []
    for para in p.paras:
        if re.fullmatch(r"(works cited|references|bibliography|sources)", para, re.I):
            break  # citations are for reading, not listening
        body.append(para)
    title = re.sub(r"^\s*\w+\.\s*", "", item["title"])  # "8. Strain Theory..." -> "Strain Theory..."
    return "\n\n".join([f"The Sovereign. {title}.", "This episode is read by an AI voice.", *body,
                        "Read the full issue, with its sources, and subscribe free at sovereignnewsletter dot substack dot com."])


def get(url):
    try:
        # Substack refuses Python's default user agent.
        return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (podcast feed builder)"}), timeout=60).read()
    except urllib.error.HTTPError as e:
        if e.code in (400, 404):  # Supabase answers 400 for a missing object
            return None
        raise


def source_items():
    ch = ET.fromstring(get(SOURCE)).find("channel")
    items = [{"title": i.findtext("title"), "link": i.findtext("link"), "guid": i.findtext("guid"),
              "date": i.findtext("pubDate"), "summary": i.findtext("description") or "",
              "html": i.findtext("content:encoded", namespaces=NS) or ""} for i in ch.findall("item")]
    show = {"title": ch.findtext("title"), "summary": ch.findtext("description"), "link": ch.findtext("link"),
            "author": ch.findtext("itunes:author", namespaces=NS) or ch.findtext("copyright"),
            "email": os.environ.get("PODCAST_OWNER_EMAIL") or EMAIL}
    return show, items[::-1]  # oldest first


def cover(out):
    """3000x3000 square (Apple's size) from the newsletter's own logo on its navy."""
    b64 = base64.b64encode((HERE / "brand" / "sovereign-logo.png").read_bytes()).decode()
    svg = out.with_suffix(".svg")
    svg.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="3000" height="3000"><rect width="3000" height="3000" fill="#1B2A4B"/>'
                   f'<image href="data:image/png;base64,{b64}" x="600" y="880" width="1800" height="1180"/></svg>')
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(svg), "-q:v", "3", str(out)], check=True)


def feed_xml(show, base, episodes):
    def ep(e):
        return (f"<item><title>{escape(e['title'])}</title><description>{escape(e['summary'])}</description>"
                f"<link>{escape(e['link'])}</link><guid isPermaLink=\"false\">{escape(e['guid'])}</guid><pubDate>{e['date']}</pubDate>"
                f"<enclosure url=\"{escape(e['url'])}\" length=\"{e['bytes']}\" type=\"audio/mpeg\"/>"
                f"<itunes:duration>{e['seconds']}</itunes:duration><itunes:explicit>false</itunes:explicit></item>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<rss version="2.0" xmlns:itunes="{NS["itunes"]}" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
            f"<title>{escape(show['title'])}</title><link>{escape(show['link'])}</link><language>en</language>"
            f"<description>{escape(show['summary'] + ' Every issue, read aloud by an AI voice.')}</description>"
            f'<atom:link href="{base}/feed.xml" rel="self" type="application/rss+xml"/>'
            f"<itunes:author>{escape(show['author'])}</itunes:author><itunes:image href=\"{base}/cover.jpg\"/>"
            f"<itunes:owner><itunes:name>{escape(show['author'])}</itunes:name><itunes:email>{escape(show['email'])}</itunes:email></itunes:owner>"
            '<itunes:category text="Society &amp; Culture"><itunes:category text="Philosophy"/></itunes:category>'
            "<itunes:explicit>false</itunes:explicit><itunes:type>episodic</itunes:type>"
            + "".join(ep(e) for e in episodes[::-1]) + "</channel></rss>\n")


def existing(feed):
    """Episodes already published, read back from our own feed (the feed is the only state)."""
    if not feed:
        return []
    out = []
    for i in ET.fromstring(feed).find("channel").findall("item"):
        enc = i.find("enclosure")
        out.append({"title": i.findtext("title"), "summary": i.findtext("description") or "", "link": i.findtext("link"),
                    "guid": i.findtext("guid"), "date": i.findtext("pubDate"), "url": enc.get("url"),
                    "bytes": enc.get("length"), "seconds": i.findtext("itunes:duration", namespaces=NS)})
    return out[::-1]  # oldest first


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--max", type=int, default=3)
    a.add_argument("--dry-run", action="store_true")
    a = a.parse_args()
    show, items = source_items()
    if a.dry_run:
        out = Path("podcast-dry-run")
        out.mkdir(exist_ok=True)
        for it in items[:a.max]:
            (out / f"{it['link'].rstrip('/').rsplit('/', 1)[-1]}.txt").write_text(script(it))
        return print(f"podcast: wrote {min(a.max, len(items))} scripts to {out}/")
    raw = os.environ.get("ENTERPRISE_SUPABASE_URL", "")
    host = re.match(r"https?://[^/]+", raw.strip())
    if not host:
        sys.exit("podcast: set ENTERPRISE_SUPABASE_URL and ENTERPRISE_SUPABASE_SERVICE_KEY.")
    base = f"{host.group(0)}/storage/v1/object/public/studio-videos/{PREFIX}"
    episodes = existing(get(f"{base}/feed.xml"))
    done = {e["guid"] for e in episodes}
    todo = [it for it in items if it["guid"] not in done][:a.max]
    if not todo:
        print("podcast: no new issue; refreshing the show details only.")
    tmp = Path(tempfile.mkdtemp())
    if get(f"{base}/cover.jpg") is None:
        cover(tmp / "cover.jpg")
        upload(tmp / "cover.jpg", name=f"{PREFIX}/cover.jpg", upsert=True)
    for it in todo:
        slug = it["link"].rstrip("/").rsplit("/", 1)[-1]
        (tmp / "script.txt").write_text(script(it))
        subprocess.run([sys.executable, str(HERE / "ai_voice.py"), str(tmp / "script.txt"), str(tmp / "vo.wav"),
                        "--engine", "kokoro", "--voice", VOICE], check=True, stderr=subprocess.DEVNULL)
        mp3 = tmp / f"{slug}.mp3"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp / "vo.wav"), "-ac", "1", "-b:a", "64k", str(mp3)], check=True)
        secs = round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)],
                                          capture_output=True, text=True, check=True).stdout))
        url = upload(mp3, name=f"{PREFIX}/{slug}.mp3", upsert=True)
        episodes.append({**it, "url": url, "bytes": mp3.stat().st_size, "seconds": secs,
                         "date": it["date"] or formatdate(usegmt=True)})
        print(f"podcast: published {it['title']} ({secs // 60} min)")
    (tmp / "feed.xml").write_text(feed_xml(show, base, episodes))
    upload(tmp / "feed.xml", name=f"{PREFIX}/feed.xml", upsert=True)
    print(f"podcast: feed {base}/feed.xml")


if __name__ == "__main__":
    main()
