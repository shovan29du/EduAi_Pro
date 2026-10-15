"""Normalise catalogue links and remove misleading 'free book' claims.

Direct free-reading/download links are retained only for recognised legal
open-book hosts. Every title also receives correctly encoded Open Library and
Google Books discovery links. Run whenever either catalogue is expanded.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus, urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOGUES = (
    ROOT / "data" / "world_literature" / "library.json",
    ROOT / "data" / "nonfiction_library" / "nonfiction.json",
)
FREE_HOSTS = {"www.gutenberg.org", "gutenberg.org", "standardebooks.org", "openstax.org"}


def update_book(book: dict) -> None:
    links = dict(book.get("links") or {})
    query = " ".join(str(value).strip() for value in (book.get("title"), book.get("author")) if value)
    encoded = quote_plus(query)
    links["open_library"] = f"https://openlibrary.org/search?q={encoded}&mode=everything"
    links["google_books_search"] = f"https://books.google.com/books?q={encoded}"

    for key in ("read_online", "download_epub", "full_book"):
        url = links.get(key)
        if not url or urlparse(url).scheme != "https" or urlparse(url).netloc.lower() not in FREE_HOSTS:
            links.pop(key, None)

    if links.get("full_book") and not links.get("read_online"):
        links["read_online"] = links.pop("full_book")
    else:
        links.pop("full_book", None)

    book["links"] = links
    book["access"] = (
        "free_open_edition"
        if links.get("read_online")
        else "search_or_library_borrowing"
    )


def walk(value) -> int:
    count = 0
    if isinstance(value, dict):
        if value.get("title") and isinstance(value.get("links"), dict):
            update_book(value)
            count += 1
        for child in value.values():
            count += walk(child)
    elif isinstance(value, list):
        for child in value:
            count += walk(child)
    return count


def main() -> None:
    for path in CATALOGUES:
        data = json.loads(path.read_text(encoding="utf-8"))
        count = walk(data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{path.name}: audited {count} catalogue records")


if __name__ == "__main__":
    main()
