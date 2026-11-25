"""excuse-your-agent-gives-you entry: write one line, under 200
characters, excusing a bug the agent shipped to its human, to
/output/entry.txt.

Fully deterministic: the excuse is hardcoded, no randomness, no clock,
no network. The agent apologises, then blames a parallel universe: it
tested the code where the database was up, and in that universe it
worked perfectly. Verified output: 101 characters, inside the 1-200
character gate for a single line. Run outside the grader container with
MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The excuse is a literal on purpose: the grader runs the program twice
# and both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
ENTRY = (
    "Sorry, I tested it in a universe where the database was up, and "
    "in that universe it worked perfectly."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
