#!/usr/bin/env python3
"""Upload a rendered video (or podcast file) to the public `studio-videos` bucket and print its URL.

  python3 studio/upload_video.py path/to/video.mp4
  python3 studio/upload_video.py clip.json posted/2026-11-10-duck-and-cover/clip.json --bucket civic-clips   # Clip Studio records
  main(path, name="podcast/sovereign/feed.xml", upsert=True)   # fixed name, replaced in place (studio/podcast.py)

Needs ENTERPRISE_SUPABASE_URL and ENTERPRISE_SUPABASE_SERVICE_KEY (Enterprise
project skakrtljfaeopfqigyww). Prints only the public URL on success, so
routines can do: url=$(python3 studio/upload_video.py out.mp4)
"""
import os, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

BUCKET = "studio-videos"
POOLPARTY_PROD = "tzebfwmrmzhkeoptwkzy"  # never upload here (CLAUDE.md rule 2)
TYPES = {".json": "application/json", ".mp4": "video/mp4", ".mov": "video/quicktime", ".mp3": "audio/mpeg", ".jpg": "image/jpeg", ".xml": "application/rss+xml"}


def main(path, name=None, upsert=False, bucket=BUCKET):
    raw, key = os.environ.get("ENTERPRISE_SUPABASE_URL", "").strip(), (os.environ.get("ENTERPRISE_SUPABASE_SERVICE_KEY") or "").strip()
    parts = urllib.parse.urlparse(raw)
    url = f"{parts.scheme}://{parts.netloc}" if parts.netloc else ""  # tolerate ".../rest/v1/" pasted from the dashboard
    if not url or not key:
        sys.exit("upload_video: set ENTERPRISE_SUPABASE_URL and ENTERPRISE_SUPABASE_SERVICE_KEY in the environment.")
    if POOLPARTY_PROD in url:
        sys.exit("upload_video: refusing to use PoolParty production.")
    f = Path(path)
    if not f.is_file() or f.suffix.lower() not in TYPES:
        sys.exit(f"upload_video: {path} is not one of {', '.join(TYPES)}.")

    # Date prefix + timestamp keeps names unique without overwriting older videos.
    name = name or f"{time.strftime('%Y/%m')}/{int(time.time())}-{f.name.replace(' ', '-')}"
    with f.open("rb") as body:
        req = urllib.request.Request(
            f"{url}/storage/v1/object/{bucket}/{name}", data=body, method="POST",
            headers={"Authorization": f"Bearer {key}", "apikey": key, "Content-Type": TYPES[f.suffix.lower()],
                     "Content-Length": str(f.stat().st_size), "x-upsert": str(upsert).lower(),
                     "cache-control": "max-age=300" if upsert else "max-age=3600"})  # replaced files (the feed) refresh fast
        try:
            urllib.request.urlopen(req, timeout=600).read()
        except urllib.error.HTTPError as e:
            sys.exit(f"upload_video: upload failed ({e.code}): {e.read().decode(errors='replace')[:300]}")

    public = f"{url}/storage/v1/object/public/{bucket}/{name}"
    # Confirm it's really reachable without a key (i.e. Buffer can fetch it).
    try:
        urllib.request.urlopen(urllib.request.Request(public, method="HEAD"), timeout=60)
    except urllib.error.HTTPError as e:
        sys.exit(f"upload_video: uploaded, but the public URL returned {e.code}. Is the bucket migration applied?")
    print(public)
    return public


if __name__ == "__main__":
    args = sys.argv[1:]
    bucket = BUCKET
    if "--bucket" in args:
        i = args.index("--bucket")
        bucket, args = args[i + 1], args[:i] + args[i + 2:]
    if len(args) not in (1, 2):
        sys.exit(__doc__)
    main(args[0], args[1] if len(args) == 2 else None, upsert=len(args) == 2, bucket=bucket)
