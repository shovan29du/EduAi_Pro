#!/usr/bin/env python3
"""Add a JustWatch streaming-availability link to every movie in
backend/data/movies.json.

There is no public API for embedding a specific person's paid Netflix or
Amazon Prime Video catalog into a third-party app (DRM + Terms of Service),
so this is the honest substitute: JustWatch is a real, well-known service
that shows which streaming services (Netflix, Prime Video, Disney+, etc.)
currently carry a given title, by region. One click from any movie card
straight to its real, live JustWatch search result.

Re-run any time new movies are added:
    python3 backend/scripts/augment_movies_streaming_links.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MOVIES_PATH = BASE_DIR / "data" / "movies.json"


def justwatch_search(title: str, year: int | str = "") -> str:
    query = f"{title} {year}".strip()
    return "https://www.justwatch.com/us/search?q=" + quote_plus(query)


def main() -> None:
    with open(MOVIES_PATH, encoding="utf-8") as f:
        data = json.load(f)
    movies = data.get("movies", data) if isinstance(data, dict) else data

    updated = 0
    for movie in movies:
        movie["streaming_search"] = justwatch_search(movie.get("title", ""), movie.get("year", ""))
        movie["streaming_note"] = "Streaming availability (incl. Netflix, Prime Video) varies by region and changes over time — check JustWatch for the current listing."
        updated += 1

    if isinstance(data, dict):
        data["movies"] = movies
    else:
        data = movies

    with open(MOVIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added streaming_search links to {updated} movies.")


if __name__ == "__main__":
    main()
