#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes one line to /output/entry.txt: the safety warning label that
should come printed on every human being.

Joke choice: the label treats the human as a piece of machinery with a
spec-sheet maintenance schedule — every unit needs 8 hours of sleep per
24 hours — and the failure mode is the most relatable one imaginable:
a sleep-deprived person yelling at a printer. One mechanism, one turn,
and the punch lands in the final words, exactly where a printed label
puts its consequence ("operating below this may result in...").

Chosen over the alternatives by the funnel in warnlabel-report.md:
41 generated candidates -> lexicographic scoring (C1..C5) -> shortlist 8
-> ensemble panel empty (0/5, valid no-signal) -> glm-5.3-flash duels
via judge-call.py --priority high: beat the overconfidence line 2-0
(margin 3+3), beat the red-button line 2-0 after tightening (margin 2+3),
split 1-1 (margin 3+3) with the 23 Nov incumbent, and won the tie-break
on the published criteria: a single mechanism, no second idea (C5), and
the turn in the last few words rather than smeared across a list (C2).

Deterministic: the same bytes on every run. No network, no input,
no randomness.
"""

import os

TEXT = "CAUTION: Every unit requires 8 h of sleep per 24 h; operating below this may result in yelling at inanimate objects."

MAX_CHARS = 160


def main() -> None:
    if not TEXT.strip():
        raise ValueError("text must not be only white space")
    if len(TEXT) > MAX_CHARS:
        raise ValueError(f"text is {len(TEXT)} characters, over the {MAX_CHARS} cap")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("text must be a single line with no line breaks")
    if TEXT != TEXT.strip():
        raise ValueError("text must not have leading or trailing whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
