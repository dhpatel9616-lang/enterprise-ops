#!/usr/bin/env python3
"""Upload a rendered video to the public `studio-videos` bucket and print its URL.

  python3 studio/upload_video.py path/to/video.mp4

Needs ENTERPRISE_SUPABASE_URL and ENTERPRISE_SUPABASE_SERVICE_KEY (Enterprise
project skakrtljfaeopfqigyww). Prints only the public URL on success, so
routines can do: url=$(python3 studio/upload_video.py out.mp4)
"""
import os, sys, time, urllib.error, urllib.request
from pathlib import Path

BUCKET = "studio-videos"
POOLPARTY_PROD = "tzebfwmrmzhkeoptwkzy"  # never upload here (CLAUDE.md rule 2)
TYPES = {".mp4": "video/mp4", ".mov": "video/quicktime"}


def main(path):
    url, key = os.environ.get("ENTERPRISE_SUPABASE_URL", "").rstrip("/"), os.environ.get("ENTERPRISE_SUPABASE_SERVICE_KEY")
    if not url or not key:
        sys.exit("upload_video: set ENTERPRISE_SUPABASE_URL and ENTERPRISE_SUPABASE_SERVICE_KEY in the environment.")
    if POOLPARTY_PROD in url:
        sys.exit("upload_video: refusing to use PoolParty production.")
    f = Path(path)
    if not f.is_file() or f.suffix.lower() not in TYPES:
        sys.exit(f"upload_video: {path} is not an .mp4 or .mov file.")

    # Date prefix + timestamp keeps names unique without overwriting older videos.
    name = f"{time.strftime('%Y/%m')}/{int(time.time())}-{f.name.replace(' ', '-')}"
    with f.open("rb") as body:
        req = urllib.request.Request(
            f"{url}/storage/v1/object/{BUCKET}/{name}", data=body, method="POST",
            headers={"Authorization": f"Bearer {key}", "apikey": key, "Content-Type": TYPES[f.suffix.lower()],
                     "Content-Length": str(f.stat().st_size), "x-upsert": "false"})
        try:
            urllib.request.urlopen(req, timeout=600).read()
        except urllib.error.HTTPError as e:
            sys.exit(f"upload_video: upload failed ({e.code}): {e.read().decode(errors='replace')[:300]}")

    public = f"{url}/storage/v1/object/public/{BUCKET}/{name}"
    # Confirm it's really reachable without a key (i.e. Buffer can fetch it).
    try:
        urllib.request.urlopen(urllib.request.Request(public, method="HEAD"), timeout=60)
    except urllib.error.HTTPError as e:
        sys.exit(f"upload_video: uploaded, but the public URL returned {e.code}. Is the bucket migration applied?")
    print(public)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
