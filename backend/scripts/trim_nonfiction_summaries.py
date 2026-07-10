#!/usr/bin/env python3
"""Trim any nonfiction.json summary over 1500 words down to the requested
700-1500 word range, by dropping trailing paragraphs until the word count
fits (keeping at least 700 words). Content is only removed, never altered
or fabricated.

Re-run after editing:
    python3 backend/scripts/trim_nonfiction_summaries.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NONFICTION_PATH = BASE_DIR / "data" / "nonfiction_library" / "nonfiction.json"

MAX_WORDS = 1500
MIN_WORDS = 700


def trim(summary: str) -> str:
    words = summary.split()
    if len(words) <= MAX_WORDS:
        return summary
    paragraphs = summary.split("\n\n")
    while paragraphs:
        candidate = "\n\n".join(paragraphs)
        wc = len(candidate.split())
        if wc <= MAX_WORDS:
            return candidate
        if len(paragraphs) == 1:
            break
        paragraphs = paragraphs[:-1]
    # Fallback: hard-truncate to MAX_WORDS words if a single paragraph is
    # itself too long (shouldn't happen with this dataset, but be safe).
    return " ".join(summary.split()[:MAX_WORDS])


def main() -> None:
    with open(NONFICTION_PATH, encoding="utf-8") as f:
        data = json.load(f)

    trimmed = 0
    still_short = []
    for cat, section in data["categories"].items():
        for book in section.get("books", []):
            summary = book.get("summary", "")
            wc = len(summary.split())
            if wc > MAX_WORDS:
                new_summary = trim(summary)
                book["summary"] = new_summary
                trimmed += 1
                new_wc = len(new_summary.split())
                if new_wc < MIN_WORDS:
                    still_short.append((cat, book.get("id"), new_wc))

    with open(NONFICTION_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Trimmed {trimmed} summaries down to <= {MAX_WORDS} words.")
    if still_short:
        print("WARNING - these ended up under the minimum after trimming:")
        for cat, bid, wc in still_short:
            print(f"  {cat} / {bid}: {wc} words")


if __name__ == "__main__":
    main()
