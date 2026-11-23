"""Office joke entry for make.fun — "Make the AI Judge Laugh: Office Jokes".

Writes a single one-line joke about office life to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic.
"""

import os

JOKE = "My performance review said 'be more visible' — so now I attend meetings on camera, muted, doing nothing."


def main() -> None:
    # Gate the entry the same way the sealed scorer does: 1-199 chars,
    # not whitespace-only, single line.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert JOKE.strip(), "joke must not be whitespace-only"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
