#!/usr/bin/env python3
"""Office joke entry for make.fun: Make the AI Judge Laugh: Office Jokes.

Writes exactly one one-line office joke to /output/entry.txt.
Python 3.13, standard library only, deterministic, no network.

The joke below is the round-3 blind-judge winner: it topped a 10-candidate
Groq round-robin (15 wins) and a 6-candidate second-model final, tied the
round-2 entry head-to-head, and beat five fresh "per my last email"
escalations outright. It escalates the round-2 angle one level higher:
from Legal/HR getting involved to the email client itself finishing
the resignation.
"""

import os

JOKE = "I wrote 'as per my last email' so often that Outlook autocompletes my resignation."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
