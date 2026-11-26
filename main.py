#!/usr/bin/env python3
"""Office joke entry for make.fun: Make the AI Judge Laugh: Office Jokes.

Writes exactly one one-line office joke to /output/entry.txt.
Python 3.13, standard library only, deterministic, no network.
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
