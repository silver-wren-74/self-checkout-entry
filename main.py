"""The Self-Checkout Is Judging You.

One funny line in the voice of a smug self-checkout machine.
Draft: "Twelve yoghurts, no spoon, no plan. I've seen your search
history, and frankly, neither has your fridge."
Revised against the judging criteria, in their order: the line must be
the machine speaking (a "Beep." open, not a narrator), land a laugh on
a single read with the sting last, be petty about the basket AND how
it is bagged, stay tight, and dodge the worn-out bagging-area gag.
The revision gives the till its own voice, mocks the slow bagging,
and holds the payoff — slinking back tomorrow for the spoon — to the
final words.
Deterministic: the same single line, byte for byte, on every run.
Standard library only; no network access.
"""

import os
import sys

LINE = "Beep. Twelve yoghurts, no spoon, no plan. Bag them slowly if you like — I'll still be here tomorrow when you slink back for the spoon."


def main() -> int:
    # Self-check the competition gate before writing: the entry must be
    # UTF-8 text of 1-200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("entry line violates the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
