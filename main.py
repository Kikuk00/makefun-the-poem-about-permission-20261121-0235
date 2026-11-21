"""Entry for make.fun bounty the-poem-about-permission-20261121-0235.

Writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only; deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

POEM = (
    "The door was never locked\u2014\n"
    "only waiting for your knock.\n"
    "Ask, and the room rearranges itself:\n"
    "chair pulled out, cup filled,\n"
    "the yes you feared to hear\n"
    "was folded small in your own fist,\n"
    "a key you were holding all along."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
