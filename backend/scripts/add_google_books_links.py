#!/usr/bin/env python3
"""Add a real Google Books *search* link to every book in the non-fiction
library and the world literature library, as a supplementary "find the
cover / read more" resource alongside the live cover-image lookup already
performed client-side by BookCover.jsx (which queries the Google Books
and Open Library APIs directly in the browser).

Consistent with this project's no-fabrication rule, this links to a
Google Books search for the title + author rather than guessing a
specific volume ID.

Re-run after editing / whenever new books are added:
    python3 backend/scripts/add_google_books_links.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
NONFICTION_PATH = BASE_DIR / "data" / "nonfiction_library" / "nonfiction.json"
LIBRARY_PATH = BASE_DIR / "data" / "world_literature" / "library.json"


def google_books_search(title: str, author: str = "") -> str:
    q = f"{title} {author}".strip() if author else title
    return "https://www.google.com/search?tbm=bks&q=" + quote_plus(q)


def update_books(books: list[dict]) -> int:
    updated = 0
    for book in books:
        links = book.setdefault("links", {})
        if not links.get("google_books_search"):
            links["google_books_search"] = google_books_search(book.get("title", ""), book.get("author", ""))
            updated += 1
    return updated


def main() -> None:
    total_updated = 0

    with open(NONFICTION_PATH, encoding="utf-8") as f:
        nonfiction = json.load(f)
    for category in nonfiction["categories"].values():
        total_updated += update_books(category.get("books", []))
    with open(NONFICTION_PATH, "w", encoding="utf-8") as f:
        json.dump(nonfiction, f, indent=2, ensure_ascii=False)

    with open(LIBRARY_PATH, encoding="utf-8") as f:
        library = json.load(f)
    for section in library["sections"].values():
        total_updated += update_books(section.get("books", []))
    with open(LIBRARY_PATH, "w", encoding="utf-8") as f:
        json.dump(library, f, indent=2, ensure_ascii=False)

    print(f"Added google_books_search link to {total_updated} books.")


if __name__ == "__main__":
    main()
