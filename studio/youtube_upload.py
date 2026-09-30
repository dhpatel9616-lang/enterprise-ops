#!/usr/bin/env python3
"""The approved long-form YouTube uploader (CLAUDE.md rule 1).

  python3 studio/youtube_upload.py video.mp4 metadata.json

Only run it when Notion -> Automation Control -> "Autopost — YouTube long-form"
is Enabled; the calling routine checks the switch.

metadata.json:
  {"title": "...", "description": "...", "tags": ["..."],
   "publish_at": "2026-10-03T14:07:00Z",   # optional: upload private, go public then
   "synthetic_media": false}               # true if realistic AI people/voices appear

Needs YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN (OAuth with
the youtube.upload scope). Prints the video URL on success.
"""
import json, os, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path

TOKEN_URL = "https://oauth2.googleapis.com/token"
UPLOAD_URL = "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status"


def access_token():
    env = {k: os.environ.get(k) for k in ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")}
    if not all(env.values()):
        sys.exit("youtube_upload: set YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET and YOUTUBE_REFRESH_TOKEN.")
    body = urllib.parse.urlencode({"client_id": env["YOUTUBE_CLIENT_ID"], "client_secret": env["YOUTUBE_CLIENT_SECRET"],
                                   "refresh_token": env["YOUTUBE_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode()
    try:
        return json.load(urllib.request.urlopen(TOKEN_URL, data=body, timeout=60))["access_token"]
    except urllib.error.HTTPError as e:
        sys.exit(f"youtube_upload: token refresh failed ({e.code}): {e.read().decode(errors='replace')[:300]}")


def main(video, meta_path):
    v, meta = Path(video), json.loads(Path(meta_path).read_text())
    if not v.is_file() or v.suffix.lower() != ".mp4":
        sys.exit(f"youtube_upload: {video} is not an .mp4 file.")
    if not meta.get("title") or len(meta["title"]) > 100:
        sys.exit("youtube_upload: metadata needs a title of 1-100 characters.")
    status = {"privacyStatus": "public", "selfDeclaredMadeForKids": False,
              "containsSyntheticMedia": bool(meta.get("synthetic_media"))}
    if meta.get("publish_at"):
        status.update(privacyStatus="private", publishAt=meta["publish_at"])
    resource = {"snippet": {"title": meta["title"], "description": meta.get("description", ""),
                            "tags": meta.get("tags", []), "categoryId": "27"},  # 27 = Education
                "status": status}

    token = access_token()
    init = urllib.request.Request(UPLOAD_URL, data=json.dumps(resource).encode(), method="POST", headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8",
        "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(v.stat().st_size)})
    try:
        session_url = urllib.request.urlopen(init, timeout=60).headers["Location"]
        with v.open("rb") as body:
            put = urllib.request.Request(session_url, data=body, method="PUT", headers={
                "Content-Type": "video/mp4", "Content-Length": str(v.stat().st_size)})
            video_id = json.load(urllib.request.urlopen(put, timeout=3600))["id"]
    except urllib.error.HTTPError as e:
        sys.exit(f"youtube_upload: upload failed ({e.code}): {e.read().decode(errors='replace')[:300]}")
    print(f"https://www.youtube.com/watch?v={video_id}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
