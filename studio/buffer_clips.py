#!/usr/bin/env python3
"""Post clips to the CLIP accounts' own Buffer account, and nowhere else.

The promo/media accounts use Claude's Buffer connector; the clip accounts
(IG @wadecapitalclips, TikTok @wade.clips3, YouTube @WadeCapitalClips) live in
a separate Buffer login reached only through its API key, so neither side can
post to the other's accounts.

  python3 studio/buffer_clips.py channels
  python3 studio/buffer_clips.py post clip.json [--draft]

clip.json: {"title": "...", "caption": "... #tags", "when": "2026-10-15T17:15:00-04:00",
            "videos": {"instagram": "https://...", "tiktok": "https://...", "youtube": "https://..."},
            "youtube_category": "27", "ai": false}
Needs BUFFER_CLIPS_API_KEY (from the clip Buffer account: Settings → API) and
network access to api.buffer.com.
"""
import json, os, sys, urllib.request

API = os.environ.get("BUFFER_API_URL", "https://api.buffer.com")
# The promo/media channels (Claude's connector). This script refuses them outright.
PROMO_CHANNELS = {"6ab6cac8ea19ca0bdeea0fba", "6ab6caf4ea19ca0bdeea114e", "6ab6d22fea19ca0bdeea4810"}


def gql(query, variables=None):
    key = os.environ.get("BUFFER_CLIPS_API_KEY")
    if not key:
        sys.exit("buffer_clips: set BUFFER_CLIPS_API_KEY (clip Buffer account → Settings → API).")
    req = urllib.request.Request(API, data=json.dumps({"query": query, "variables": variables or {}}).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    out = json.load(urllib.request.urlopen(req, timeout=60))
    if out.get("errors"):
        sys.exit(f"buffer_clips: {out['errors']}")
    return out["data"]


def channels():
    orgs = gql("{ account { organizations { id name } } }")["account"]["organizations"]
    found = []
    for o in orgs:
        q = "query($o: OrganizationId!) { channels(input: {organizationId: $o}) { id service name isDisconnected } }"
        found += gql(q, {"o": o["id"]})["channels"]
    bad = [c for c in found if c["id"] in PROMO_CHANNELS]
    if bad:  # wrong key: this is the promo Buffer account
        sys.exit(f"buffer_clips: this key reaches the PROMO accounts ({[c['name'] for c in bad]}); refusing.")
    return found


def post(spec, draft):
    chans = {c["service"]: c for c in channels() if not c["isDisconnected"]}
    mutation = """mutation($i: CreatePostInput!) { createPost(input: $i) {
      ... on PostActionSuccess { post { id status channelService dueAt } }
      ... on MutationError { message } } }"""
    for service, url in spec["videos"].items():
        c = chans.get(service)
        if not c:
            print(f"buffer_clips: no connected {service} channel; skipped.")
            continue
        meta = {"instagram": {"instagram": {"type": "reel", "shouldShareToFeed": True, "isAiGenerated": spec.get("ai", False)}},
                "tiktok": {"tiktok": {"title": spec["title"][:90], "isAiGenerated": spec.get("ai", False)}},
                "youtube": {"youtube": {"title": spec["title"][:100], "categoryId": spec.get("youtube_category", "27"),
                                        "privacy": "public", "madeForKids": False, "isAiGenerated": spec.get("ai", False)}}}[service]
        text = spec["caption"] + ("\n\n#Shorts" if service == "youtube" and "#Shorts" not in spec["caption"] else "")
        inp = {"channelId": c["id"], "text": text, "assets": [{"video": {"url": url}}], "metadata": meta,
               "schedulingType": "automatic", "saveToDraft": draft,
               **({"mode": "customScheduled", "dueAt": spec["when"]} if spec.get("when") else {"mode": "addToQueue"})}
        print(service, json.dumps(gql(mutation, {"i": inp})["createPost"]))


if __name__ == "__main__":
    if sys.argv[1:2] == ["channels"]:
        print(json.dumps(channels(), indent=1))
    elif sys.argv[1:2] == ["post"] and len(sys.argv) >= 3:
        post(json.load(open(sys.argv[2])), "--draft" in sys.argv)
    else:
        sys.exit(__doc__)
