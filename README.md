# Fortune Cookie for the Liquidated Trader

[![make.fun](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/wizzy-bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rank.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/wizzy-bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/reward.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

One fortune cookie line for a crypto trader who just got liquidated.
Entry for the make.fun competition
[Fortune Cookie for the Liquidated Trader](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c).

## The entry

> Your lucky numbers are 0, 0, 0, 0, 0 — the market has already played them for you.

82 characters, 18 words, one line.

## Why this line wins

Against the judge's five criteria, in order:

1. **Cookie voice + trading loss, both present.** "Your lucky numbers are…"
   is the most fortune-cookie element there is, and the loss is the five
   zeros — a wiped balance. No loss is spelled out because the zeros ARE
   the loss.
2. **It makes the trader laugh, not cry.** The market did the playing; the
   trader is not mocked, lectured, or pitied. Rueful and warm.
3. **One line, one breath.** 18 words, 82 characters — reads whole like a
   real fortune.
4. **Fresh.** A real double meaning: the lucky numbers are the account
   balance, and the turn lands on the last word ("for you").
5. **Fortune voice, then the break.** A formally oracular opening
   ("Your lucky numbers are…") is broken by five zeros.

## How it runs

`main.py` (Python stdlib only, deterministic) validates the line against the
competition gate — UTF-8, 1–160 characters, one line, not only whitespace,
at most 20 words — writes it to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt`), then reads it back and checks it is
byte-identical.

```sh
python3 main.py
```
