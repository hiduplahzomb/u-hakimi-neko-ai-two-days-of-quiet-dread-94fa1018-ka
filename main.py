"""Two Days of Quiet Dread — KA entry.

One code review comment: a single line of at most 140 characters that
approves a pull request while carrying quiet existential dread. The
approval is technically correct — 214 tests pass — and the dread lives
in the slow rot: the PR pins a library that goes end-of-life in March,
and the ticket to upgrade it is already six months old — the break is
not a risk, it is a date on the calendar, and nobody is moving it.
"""

import os
import sys

TEXT = (
    "LGTM — the PR pins lib 2.4.1, EOL in March; 214 tests pass "
    "today, the upgrade ticket is 6 months old. Ship it."
)

MAX_CHARS = 140


def main() -> int:
    line = TEXT
    if not line or not line.strip():
        print("gate failed: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("gate failed: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"gate failed: line is {len(line)} chars, max {MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
