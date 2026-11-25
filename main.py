#!/usr/bin/env python3
"""Office joke entry for make.fun competition
"Make the AI Judge Laugh: Office Jokes"
(u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a).

Writes exactly one one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt if unset).
Python 3.13 standard library only: no third-party imports, no network.
Deterministic: the output is always the same single line.
"""

import os

JOKE = "I wrote 'per my last email' so politely that Legal forwarded it to HR as a threat assessment."


def main():
    if not (1 <= len(JOKE) <= 199):
        raise SystemExit("joke must be 1-199 characters, got %d" % len(JOKE))
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("joke must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print("wrote %d chars to %s" % (len(JOKE), path))


if __name__ == "__main__":
    main()
