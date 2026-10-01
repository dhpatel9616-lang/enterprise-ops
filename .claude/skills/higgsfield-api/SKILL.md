---
name: higgsfield-api
description: How to use the pay-as-you-go Higgsfield API for AI image/video generation with the HF_KEY credential. Use only when a brief truly needs AI-generated footage or images that the free tools in video-assembly can't make. Defaults to the cheapest model that meets the brief and logs the cost of every generation.
---

# Higgsfield API

Every call costs real money and we have zero revenue. Free first: if
`video-assembly` (ffmpeg, SVG puppets, code-made graphics) can do it, use that.

## Credential
- Read the key from the `HF_KEY` environment variable. Never print, log,
  paste into Notion, or commit it.
- `HF_KEY` must be the key ID and secret joined by a colon
  (`HF_KEY=<key id>:<key secret>`, from console.higgsfield.ai). Send it as
  `Authorization: Key $HF_KEY` to `https://api.higgsfield.ai/<model path>`.
  Requests are asynchronous: poll the returned `status_url`, then download the
  result within 7 days (outputs expire).
- Check price first with the free estimate endpoint:
  `POST https://api.higgsfield.ai/estimate/<model path>` with the same body.
- If `HF_KEY` is missing, stop and tell the owner in plain words: "Add your
  Higgsfield key as a secret named HF_KEY in the cloud environment settings."

## Before each batch
1. Open Higgsfield's current API docs and pricing page. Don't rely on memory
   for endpoints, model names, or prices; they change.
2. Write the models you considered and their current price per generation
   into `studio/logs/higgsfield-prices.md` (date at the top).
3. Pick the **cheapest model that meets the brief** (resolution, length,
   motion quality). Use a pricier one only if the brief's requirement is
   written down and the cheap one can't meet it. Say which requirement.

## Spending limits
- Default caps until the owner changes them: **$2 per generation, $10 per
  night.** Anything above: don't run it; add a Build Queue note asking the
  owner.
- Test with the lowest resolution/shortest length first; upscale only the
  keeper.

## Log every generation
Append one row to `studio/logs/generation-costs.csv` (create it with this
header if it doesn't exist):

```
date,script,brand,model,what,seconds_or_images,cost_usd,kept
```

Also add the cost to the Notion **Scripts** item's *Generation Cost USD*.

## Content rules
- Realistic output needs AI labels (`content-rules`, `platform-formats`).
- Characters: attach the `character-bible` reference art; never prompt for a
  real person's likeness.
