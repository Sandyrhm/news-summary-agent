"""Write the bundled news summary to the output file.

Stdlib only, deterministic, no network, no clock, no randomness: it copies
summary.txt (the summary of Wednesday 11 November 2026, written by the
author from wire reporting) to $MAKEFUN_OUTPUT_DIR/entry.txt, defaulting
to /output/entry.txt in the grader's container.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
MIN_CHARS = 1
MAX_CHARS = 2000


def main():
    src = os.path.join(HERE, "summary.txt")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # Gate check, same rules as the competition's sealed scorer: UTF-8,
    # 1 to 2,000 characters, and not only white space. Fail loudly here
    # rather than submit an entry the gate would refuse.
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "summary.txt is %d characters, outside 1-2000" % len(text)
        )
    if not any(not c.isspace() for c in text):
        raise SystemExit("summary.txt is only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
