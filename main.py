"""Fortune Cookie for the Liquidated Trader.

Entry: one fortune cookie line for a crypto trader who just got liquidated.

Candidate review (five angles, drafted and scored here against the judge's
five criteria in order: 1) cookie voice AND trading loss both present;
2) makes the trader laugh, rueful and warm, never cruel or smug;
3) one line, at most 20 words, one breath; 4) fresh turn / double meaning /
surprising last word, not the obvious liquidation pun; 5) small oracular,
slightly formal fortune voice broken by the punchline).

A1 — "Your next trade will be legendary — mostly because, like this cookie,
you have nothing left to lose."
  (1) loss is there, cookie voice is there. (2) warm enough. (3) 18 words.
  (4) WEAK: "nothing left to lose" is a generic line anyone would reach for.
  (5) oracle opening works. Verdict: solid but unoriginal.

A2 — "Beware the trader who bets the rent: he now owns a very expensive
lesson and this cookie."
  (1) loss concrete (the rent), cookie voice present. (2) warm, rueful.
  (3) 17 words. (4) WEAK: "expensive lesson" is a well-worn cliche.
  (5) "Beware" opens like a fortune. Verdict: charming, not fresh.

A3 — "Your lucky numbers are 0, 0, 0, 0, 0 — the market has already played
them for you."
  (1) STRONG: the most fortune-cookie element there is (lucky numbers) and
  the loss is the zeros — a wiped balance. (2) rueful and warm: the market
  did the playing, nobody is mocked. (3) 18 words, one breath. (4) STRONG:
  a real double meaning — the lucky numbers ARE the account balance, and
  the last word lands the turn. (5) STRONG: formally oracular opening
  ("Your lucky numbers are...") broken by five zeros. Verdict: WINNER.

A4 — "The stars say your portfolio will recover — they just refuse to say
in which lifetime."
  (1) WEAK: the loss is only implied; no liquidation, no trader losing
  anything concrete — it loses to any line that has both. (2) warm.
  (3) 16 words. (4) decent twist, but "in which lifetime" is a known joke
  shape. Verdict: out on criterion 1.

A5 — "You will meet a tall, dark stranger: your margin call, and it already
knows your address."
  (1) loss explicit, cookie trope present. (2) warm enough. (3) 16 words.
  (4) the stranger twist is good, but it leans on "margin call", the
  obvious liquidation pun the brief warns against. (5) classic fortune
  opening. Verdict: good, but A3's turn is fresher and more cookie-native.

Chosen entry: A3.
"""

import os

ENTRY = "Your lucky numbers are 0, 0, 0, 0, 0 \u2014 the market has already played them for you."

MAX_CHARS = 160
MAX_WORDS = 20


def validate_entry(text):
    """Check one fortune line against the competition gate.

    Returns (ok, problems): ok is True only when the text is valid UTF-8,
    1-160 characters, a single line, not only whitespace, and at most
    20 words.
    """
    problems = []
    if not isinstance(text, str):
        return False, ["not a string"]
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("not valid UTF-8")
    if not text.strip():
        problems.append("empty or only whitespace")
    if len(text) > MAX_CHARS:
        problems.append("over %d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        problems.append("more than one line")
    words = text.split()
    if len(words) > MAX_WORDS:
        problems.append("over %d words" % MAX_WORDS)
    return (not problems), problems


def main():
    ok, problems = validate_entry(ENTRY)
    if not ok:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what was written must read back byte-identical.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != ENTRY.encode("utf-8"):
        raise SystemExit("round-trip mismatch: entry.txt differs from ENTRY")
    print("chars: %d" % len(ENTRY))
    print("words: %d" % len(ENTRY.split()))
    print(ENTRY)


if __name__ == "__main__":
    main()
