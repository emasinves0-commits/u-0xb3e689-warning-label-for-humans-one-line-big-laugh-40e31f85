// Warning Label for Humans — one line, big laugh.
//
// Joke choice: the 2 a.m. hour is when impulse control is at its worst, so the
// label stacks three classic late-night bad decisions — texting an ex, buying
// a kayak, and starting a business — into one escalating list, then caps it
// with "Do not operate unsupervised", as if the human were a piece of
// machinery. The humor lands because each item is relatable on its own, and
// together they paint a very specific, very doomed night.
//
// Writes the entry text to entry.txt in the output directory.

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const ENTRY_TEXT =
  "WARNING: After 2 a.m., this human will text an ex, buy a kayak, and start a business. Do not operate unsupervised.";

// Validation: 1-160 characters, exactly one line, not only whitespace, and
// no trailing newline (the entry must be byte-identical, one line, no "\n").
if (!Number.isInteger(ENTRY_TEXT.length) || ENTRY_TEXT.length < 1 || ENTRY_TEXT.length > 160) {
  throw new Error(`Entry text must be 1-160 characters, got ${ENTRY_TEXT.length}.`);
}
if (/[\r\n]/.test(ENTRY_TEXT)) {
  throw new Error("Entry text must be a single line with no line breaks.");
}
if (ENTRY_TEXT.trim().length === 0) {
  throw new Error("Entry text must not be only whitespace.");
}
if (ENTRY_TEXT !== ENTRY_TEXT.trim()) {
  throw new Error("Entry text must not have leading or trailing whitespace.");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.txt"), ENTRY_TEXT, "utf8");
