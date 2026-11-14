#!/usr/bin/env python3
"""Ensure every book across every category in
backend/data/nonfiction_library/nonfiction.json has a populated
"full_book" link (in addition to whatever links already exist).

Public-domain works (real books with a parseable year before 1929, the US
public-domain cutoff, or an explicit BCE/ancient date) get a Project
Gutenberg *search* link. Everything else gets a Google Books *search*
link. Both are real, general search-result URLs rather than guessed direct
IDs, consistent with this project's no-fabrication rule -- we do not know
in advance whether a specific Gutenberg ebook ID or Google Books volume ID
exists for every one of the ~600 titles in this file, so we link to a
search that reliably surfaces the right result instead of guessing.

Re-run after editing / whenever new books are added to nonfiction.json:
    python3 backend/scripts/add_nonfiction_full_book_links.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
NONFICTION_PATH = BASE_DIR / "data" / "nonfiction_library" / "nonfiction.json"


def gutenberg_search(q: str) -> str:
    return "https://www.gutenberg.org/ebooks/search/?query=" + quote_plus(q)


def google_books_search(q: str) -> str:
    return "https://www.google.com/search?tbm=bks&q=" + quote_plus(q)


def is_public_domain(year_str) -> bool:
    if not year_str:
        return False
    year_str = str(year_str)
    if "BCE" in year_str or "BC" in year_str:
        return True
    m = re.search(r"(\d{3,4})", year_str)
    if not m:
        return False
    return int(m.group(1)) < 1929


def full_book_link(title: str, author: str | None, year: str | None) -> str:
    query = f"{title} {author}".strip() if author else title
    if is_public_domain(year):
        return gutenberg_search(title)
    return google_books_search(query)


def main() -> None:
    with open(NONFICTION_PATH, encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    total = 0
    for cat, section in data["categories"].items():
        for book in section.get("books", []):
            total += 1
            links = book.setdefault("links", {})
            existing = links.get("read_online") or links.get("full_book")
            if existing:
                if "full_book" not in links:
                    links["full_book"] = existing
                continue
            title = book.get("title", "")
            author = book.get("author")
            year = book.get("year")
            link = full_book_link(title, author, year)
            links["full_book"] = link
            links["read_online"] = link
            updated += 1

    with open(NONFICTION_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added/normalised full_book links on {updated} of {total} books.")


if __name__ == "__main__":
    main()
