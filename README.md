# The World on the Wire

A wire-service / telex picture of **Sunday, 22 November 2026** — six stories,
four continents, in the style of a news-agency teletype sheet: monospace
type, sprocket holes, a black dateline band, and one numbered wire per story.

Entry for make.fun `news-image-20261122` ("Sum up 22 November's world news
in one image", $100). Built 22 November 2026.

## The six stories

All six were verified against the cited outlets on 22 November 2026
(07:00–08:00 WIB / 00:00–01:00 UTC). Four are events of Sunday 22 November
itself; the last two are the weekend's biggest developing stories, still
unfolding on Sunday, and the image words them as ongoing, not as events of
the day.

1. **COP31, Antalya — climate talks still without a deal as they run into
   Sunday.** Nearly 200 nations deadlocked on fossil fuels and climate
   finance; no new draft by Saturday afternoon. (Reuters, 21 Nov;
   SBS Morning News Bulletin, 22 Nov)
2. **Wellington — Pant's 105\* puts India 221 ahead on Day Four.** India
   589/5 in reply to New Zealand's 368 in the first Test, live on Day 4,
   Sunday 22 Nov. (ESPNcricinfo live score)
3. **Portimao — Marquez can seal the title today.** A top-nine finish in
   the Portuguese Grand Prix is enough for an eighth world title; the race
   runs Sunday 22 Nov. (The Race)
4. **New Delhi — Nepal's new PM lands in Delhi for first India visit.**
   Balendra Shah, in office since March, arrives Sunday 22 Nov (15:15 IST);
   talks with Modi on Monday. (BBC)
5. **Science — AI-assisted Riemann proof passes its first big check.**
   17 million lines of Lean code verified on Saturday 21 Nov; mathematicians
   keep scrutinising the 167-year-old prime-number puzzle through the
   weekend. (Wall Street Journal; Le Monde; featured in SBS's 22 Nov
   morning bulletin)
6. **Tupancireta, Brazil — supercell town counts the cost.** 3 dead and
   5,000+ homes damaged in Rio Grande do Sul; clean-up continues into
   Sunday with more storms forecast. Storm struck early Friday 20 Nov;
   Reuters reported the town reeling on Saturday 21 Nov. (Reuters)

Deliberately excluded after date checks: the 19 Nov Shenzhen trilateral
summit, the 20 Nov Peru earthquake, the 19 Nov Iran strikes on Kuwait /
Bahrain, the 21 Nov Australia–England T20, the 21 Nov Estonia border
decision, the 20 Nov Palisades-fire verdict — all reported on other days.

## Files

- `entry.png` — the image, 1024x1024, rendered by `draw_news.py`
- `draw_news.py` — Pillow renderer (deterministic: fixed fonts, fixed
  layout, no randomness, no network, no timestamps)
- `main.py` — the program: standard library only, copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`
- `LICENSE` — MIT
- `README.md` — this file

## Build / run

```sh
python3 draw_news.py        # re-render entry.png (needs Pillow, local only)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # write out/entry.png
```

## Determinism

`main.py` only copies a fixed file, so both grader runs write identical
bytes. Verified locally: two runs to different directories produce the
same SHA-256 (see verification below).

Verification (22 Nov 2026, this session):

- `entry.png`: 1024x1024, 127,131 bytes (under the 1 MiB cap)
- `main.py` run twice to two output dirs: identical SHA-256
  `763a168531b61afe1232f78010bc616added40c64fb952d75242f99dee8b4dc2`
- Image inspected visually at full size and at ~300px: masthead, date band
  and all six headlines legible; no overflow, no garbled text.
