# PoolParty: "Friendly Wagers" campaign (draft for owner approval)

**Goal:** downloads at launch. **Revenue path:** 3 (audience capture:
PoolParty App Store downloads). **CTA:** "Download PoolParty."
**Cast:** `promo-cast` (Maya, Jonah, Priya, Marcus). Realistic AI adults,
always labeled.
**Format:** 9:16, 12–20 s, captions burned in, for Reels, Shorts, and TikTok
(except alcohol spots). One everyday scenario per ad.
**Rules:** `brand-voice` → PoolParty campaign rules; `content-rules`;
`platform-formats`.

## Every ad follows the same beats
1. **Hook (0–2 s):** a line of dialogue that starts the bet ("Bet you can't…").
2. **The pool (2–6 s):** someone opens PoolParty. Use the owner's real
   screen recording as an insert, or keep the phone screen out of view.
3. **The moment (6–12 s):** the thing happens; reactions.
4. **Payoff (12–16 s):** the loser pays the favor, the winner gloats.
5. **End card (last 2–3 s):** PoolParty logo + tagline "Don't give your
   money to the casinos. Wager with your friends." + "Download PoolParty" +
   "No real money. Just bragging rights." + "AI actors".

## Scenarios

| # | Scenario | Setting | The bet | Stake (never money) | Alcohol? |
|---|---|---|---|---|---|
| 1 | Pizza ETA | Apartment couch | Closest guess to when the pizza arrives | Loser does the dishes for a week | No |
| 2 | Watch party | Sports bar, team jerseys | Prediction pool on the final score | Loser wears the rival jersey to brunch | No (sodas on the table) |
| 3 | Hot wing roulette | Backyard grill | Who taps out first on the wing ladder | Loser eats the ghost-pepper wing on camera | No |
| 4 | Karaoke high note | Karaoke booth | Can Marcus hit the high note? (He can't.) | Loser picks the next song for the winner, no vetoes | No |
| 5 | Road trip | Car at a gas stop | ETA pool, including snack stops | Winner controls the playlist | No |
| 6 | Leg day | Gym | First one to skip leg day this month | Loser buys post-workout smoothies | No |
| 7 | Snow day | Kitchen window | Will it actually snow tomorrow? | Loser shovels everyone's walkway | No |
| 8 | Finale night | Living room | Who gets voted off the (fictional) reality show | Loser hosts next watch party | No |
| 9 | Chili cook-off | Kitchen | Whose chili wins the group vote | Loser wears the "Chili Loser" apron all night | No |
| 10 (optional) | Pong night | House party, 21+ | Tournament bracket pool | Loser DJs the rest of the night | **Yes:** 21+-limited Instagram/YouTube only, never TikTok, no chugging or drunkenness |

Spots 1–9 are safe for every platform and the full 14–30 audience. Spot 10
runs only if the owner asks for it.

## Example script: #1 Pizza ETA (15 s)
- **0–2 s. Jonah** (holding phone): "Bet you the pizza's here in 20."
  **Priya** (not looking up): "Thirty-four."
- **2–5 s.** Maya: "Pool's up." She taps her phone (insert: real PoolParty
  screen recording, or screen out of view).
- **5–10 s.** Clock ticks. Doorbell. Marcus checks the time: "…thirty-three."
  Priya doesn't react. Jonah groans.
- **10–13 s.** Jonah at the sink, surrounded by dishes. Priya hands him one
  more plate.
- **13–15 s. End card:** "Don't give your money to the casinos. Wager with
  your friends." · "Download PoolParty" · "No real money. Just bragging
  rights." · "AI actors"
- **Caption:** "Priya is undefeated. Settle it with PoolParty. No real money,
  just bragging rights. #PoolParty"

## Production plan
1. The owner approves the cast and picks 3 scenarios to start.
2. Generate cast reference images (`higgsfield-api`, cheapest model that holds
   faces consistently; log costs).
3. Per ad: generate 3–5 short realistic clips (one per beat) from the
   references, then assemble for free with ffmpeg (captions, end card, app
   insert, music from a free-licence library).
4. Save as Buffer **drafts** with the AI label noted ("NEEDS AI LABEL").
   Nothing posts before launch and the owner's approval.

**Blocked on:** `HF_KEY` in the cloud environment, the owner's real app
screen recordings, the App Store link (at launch), and cast approval.
