#!/usr/bin/env python3
"""Add or enrich the first 200 BFI Sight and Sound all-time poll films.

The official BFI page supplies rank, title, year, director, country,
description, preview image and BFI film URL. Platform URLs are search links,
not claims that a title is currently included in a subscription.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import quote_plus, urljoin
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).resolve().parent.parent
MOVIES_PATH = BASE_DIR / "data" / "movies.json"
SNAPSHOT_PATH = BASE_DIR / "data" / "top_200_movies_bfi_snapshot.json"
SOURCE_URL = "https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time"
COUNT = 200
BATCH = "bfi_sight_sound_2022_top_200"


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", value))).strip()


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def search(base: str, query: str) -> str:
    return base + quote_plus(query)


def fetch_films() -> list[dict]:
    request = Request(SOURCE_URL, headers={"User-Agent": "EduAI-Pro/1.0 educational catalogue"})
    page = urlopen(request, timeout=45).read().decode("utf-8", "replace")
    articles = re.findall(r"<article[^>]*>(.*?)</article>", page, flags=re.S | re.I)
    rows = []
    identified = paragraph_matches = year_matches = 0
    for article in articles:
        title_match = re.search(r"<h1>(.*?)</h1>", article, flags=re.S | re.I)
        rank_match = re.search(
            r"PreviewCard__label[^>]*>.*?(\d+)</p>", article, flags=re.S | re.I
        )
        href_match = re.search(r'<a href="([^"]+)"', article, flags=re.S | re.I)
        if not (title_match and rank_match and href_match):
            continue
        identified += 1
        paragraphs = re.findall(r"ResultsPage__P[^>]*>(.*?)</p>", article, flags=re.S | re.I)
        if paragraphs:
            paragraph_matches += 1
        year_country = clean(paragraphs[0]) if paragraphs else ""
        year_match = re.search(r"\b(18|19|20)\d{2}\b", year_country)
        if not year_match:
            continue
        year_matches += 1
        year = int(year_match.group())
        country = year_country.replace(str(year), "", 1).strip(" ,") or "International"
        director = clean(paragraphs[1]).removeprefix("Directed by ").strip() if len(paragraphs) > 1 else ""
        image_match = re.search(r'<img src="([^"]+)"', article, flags=re.S | re.I)
        description_match = re.search(
            r"PreviewCard__description[^>]*>(.*?)</p>", article, flags=re.S | re.I
        )
        rows.append(
            {
                "poll_rank": int(rank_match.group(1)),
                "title": clean(title_match.group(1)),
                "year": year,
                "country": country,
                "director": director or "See BFI record",
                "description": clean(description_match.group(1)) if description_match else "",
                "preview_image": html.unescape(image_match.group(1)) if image_match else "",
                "bfi_url": urljoin(SOURCE_URL, html.unescape(href_match.group(1))),
            }
        )

    unique = {}
    for row in sorted(rows, key=lambda item: (item["poll_rank"], item["title"])):
        unique.setdefault((norm(row["title"]), row["year"]), row)
    result = list(unique.values())
    if len(result) < COUNT:
        raise RuntimeError(
            f"BFI parser returned only {len(result)} unique ranked films "
            f"(articles={len(articles)}, identified={identified}, "
            f"paragraphs={paragraph_matches}, years={year_matches})"
        )
    return result[:COUNT]


def links_for(title: str, year: int, bfi_url: str) -> dict:
    query = f"{title} {year}"
    return {
        "bfi": bfi_url,
        "imdb": search("https://www.imdb.com/find/?q=", query),
        "tmdb": search("https://www.themoviedb.org/search?query=", query),
        "rotten_tomatoes": search("https://www.rottentomatoes.com/search?search=", query),
        "letterboxd": search("https://letterboxd.com/search/", query),
        "wikipedia": search("https://en.wikipedia.org/w/index.php?search=", query),
        "justwatch": search("https://www.justwatch.com/uk/search?q=", query),
        "netflix": search("https://www.netflix.com/search?q=", title),
        "prime_video": search("https://www.primevideo.com/search/ref=atv_nb_sr?phrase=", title),
        "apple_tv": search("https://tv.apple.com/gb/search?term=", title),
        "youtube_movies": search("https://www.youtube.com/results?search_query=", query + " movie"),
        "bfi_player": search("https://player.bfi.org.uk/search?q=", title),
    }


def new_movie(row: dict, position: int, checked_at: str) -> dict:
    title, year = row["title"], row["year"]
    return {
        "id": "bfi_" + re.sub(r"[^a-z0-9]+", "-", norm(f"{title}-{year}")).strip("-"),
        "title": title,
        "year": year,
        "country": row["country"],
        "language": "See official BFI record",
        "genre": ["All-time classics", "Critics' poll"],
        "age_group": "Adult",
        "director": row["director"],
        "description": row["description"],
        "watch_url": row["bfi_url"],
        "source": "BFI Sight and Sound Greatest Films of All Time 2022",
        "streaming_search": links_for(title, year, row["bfi_url"])["justwatch"],
        "streaming_note": (
            "Search links only. Availability and subscription requirements vary by "
            "country and change over time."
        ),
        "preview_image": row["preview_image"],
        "all_time_list_position": position,
        "all_time_poll_rank": row["poll_rank"],
        "all_time_source": SOURCE_URL,
        "ranking_checked_at": checked_at,
        "links": links_for(title, year, row["bfi_url"]),
        "source_batch": BATCH,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    checked_at = date.today().isoformat()
    ranked = fetch_films()
    print(
        f"Parsed {len(ranked)} films; poll ranks "
        f"{ranked[0]['poll_rank']}–{ranked[-1]['poll_rank']}."
    )
    if args.dry_run:
        return

    data = json.loads(MOVIES_PATH.read_text(encoding="utf-8"))
    movies = data.get("movies", data)
    by_title_year = {(norm(movie.get("title", "")), movie.get("year")): movie for movie in movies}
    by_title = {norm(movie.get("title", "")): movie for movie in movies}
    selected_snapshot = []
    added = updated = 0
    for position, row in enumerate(ranked, start=1):
        generated = new_movie(row, position, checked_at)
        existing = by_title_year.get((norm(row["title"]), row["year"])) or by_title.get(norm(row["title"]))
        if existing:
            existing.update(
                {
                    "preview_image": generated["preview_image"],
                    "all_time_list_position": position,
                    "all_time_poll_rank": row["poll_rank"],
                    "all_time_source": SOURCE_URL,
                    "ranking_checked_at": checked_at,
                    "links": generated["links"],
                    "streaming_search": generated["streaming_search"],
                    "streaming_note": generated["streaming_note"],
                    "source_batch": BATCH,
                }
            )
            updated += 1
        else:
            movies.append(generated)
            by_title_year[(norm(row["title"]), row["year"])] = generated
            by_title[norm(row["title"])] = generated
            added += 1
        selected_snapshot.append(row | {"list_position": position})

    data["movies"] = movies
    MOVIES_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    SNAPSHOT_PATH.write_text(
        json.dumps(
            {"source": SOURCE_URL, "checked_at": checked_at, "movies": selected_snapshot},
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Top 200 ready: {updated} enriched, {added} added; movie catalogue total {len(movies)}.")


if __name__ == "__main__":
    main()
