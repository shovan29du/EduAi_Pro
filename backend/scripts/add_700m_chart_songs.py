#!/usr/bin/env python3
"""Add 500 non-duplicate chart videos with at least 700 million views.

The current all-time YouTube music-video table is downloaded from Kworb. Each
selected row retains its exact chart title, video id, rank, observed view
count, source URL and verification date. Re-running replaces this batch
instead of adding another 500.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).resolve().parent.parent
SONGS_PATH = BASE_DIR / "data" / "song_centre" / "songs.json"
SNAPSHOT_PATH = BASE_DIR / "data" / "song_centre" / "kworb_700m_snapshot.json"
SOURCE_URL = "https://kworb.net/youtube/topvideos.html"
MINIMUM_VIEWS = 700_000_000
ADD_COUNT = 500
BATCH = "kworb_700m_2026"


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def clean_text(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def canonical_title(value: str) -> str:
    value = re.sub(
        r"[\[(](official( music)? video|official audio|lyrics?|lyric video|"
        r"full video|hd|4k|visualizer|audio|music video|video oficial)[^\])]*[\])]",
        "",
        value,
        flags=re.I,
    )
    value = re.split(r"\b(?:ft\.?|feat\.?|featuring)\b", value, maxsplit=1, flags=re.I)[0]
    return re.sub(r"\s+", " ", value).strip(" -|")


def parse_credit(chart_title: str) -> tuple[str, str]:
    if " - " in chart_title:
        artist, title = chart_title.split(" - ", 1)
        return canonical_title(title), artist.strip()
    if " | " in chart_title:
        title, credit = chart_title.split(" | ", 1)
        return canonical_title(title), credit.strip()
    return canonical_title(chart_title), "Artist credited in chart title"


def fetch_chart() -> list[dict]:
    request = Request(SOURCE_URL, headers={"User-Agent": "EduAI-Pro/1.0 educational catalogue"})
    page = urlopen(request, timeout=45).read().decode("utf-8", "replace")
    parsed = []
    for body in re.findall(r"<tr[^>]*>(.*?)</tr>", page, flags=re.S | re.I):
        match = re.search(
            r'href="video/([^"]+)\.html"[^>]*>(.*?)</a>.*?<td>([\d,]+)</td>',
            body,
            flags=re.S | re.I,
        )
        if not match:
            continue
        video_id, raw_title, raw_views = match.groups()
        parsed.append(
            {
                "chart_rank": len(parsed) + 1,
                "chart_title": clean_text(raw_title),
                "video_id": video_id,
                "views": int(raw_views.replace(",", "")),
            }
        )
    if len(parsed) < ADD_COUNT:
        raise RuntimeError(f"Kworb parser returned only {len(parsed)} music-video rows")
    return parsed


def build_song(row: dict, checked_at: str) -> dict:
    title, artist = parse_credit(row["chart_title"])
    query = f"{title} {artist}".strip()
    return {
        "id": f"chart700m_{row['video_id']}",
        "title": title or row["chart_title"],
        "artist": artist,
        "album": "",
        "year": 0,
        "genre": ["global chart"],
        "origin_country": "International",
        "language": "Multiple / see official video",
        "duration_approx": "",
        "description": (
            f"All-time YouTube music-video chart entry with {row['views']:,} observed "
            f"views on {checked_at}; minimum inclusion threshold: {MINIMUM_VIEWS:,}."
        ),
        "educational_notes": (
            "View totals are time-sensitive popularity evidence, not a measure of "
            "artistic quality. Use the source link to review the current count."
        ),
        "fun_fact": f"Ranked #{row['chart_rank']} in the source table when imported.",
        "awards": ["700 million+ observed YouTube views"],
        "links": {
            "youtube_video": f"https://www.youtube.com/watch?v={row['video_id']}",
            "youtube_search": "https://www.youtube.com/results?search_query=" + quote_plus(query),
            "chart_source": f"https://kworb.net/youtube/video/{row['video_id']}.html",
            "wiki_search": "https://en.wikipedia.org/w/index.php?search=" + quote_plus(query),
            "lyrics_search": "https://www.google.com/search?q=" + quote_plus(query + " lyrics"),
            "spotify_search": "https://open.spotify.com/search/" + quote_plus(query),
            "apple_music_search": "https://music.apple.com/us/search?term=" + quote_plus(query),
        },
        "tags": ["global chart", "700m+ views", "youtube"],
        "decade": "Chart archive",
        "suitable_for_ages": "Adult — review source content",
        "chart_title": row["chart_title"],
        "chart_rank": row["chart_rank"],
        "verified_views": row["views"],
        "minimum_verified_views": MINIMUM_VIEWS,
        "view_count_source": SOURCE_URL,
        "view_count_checked_at": checked_at,
        "source_batch": BATCH,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = json.loads(SONGS_PATH.read_text(encoding="utf-8"))
    base_songs = [song for song in data["songs"] if song.get("source_batch") != BATCH]
    existing_titles = {norm(canonical_title(song.get("title", ""))) for song in base_songs}
    existing_ids = {
        song.get("links", {}).get("youtube_video", "").rsplit("=", 1)[-1]
        for song in base_songs
        if song.get("links", {}).get("youtube_video")
    }

    checked_at = date.today().isoformat()
    selected = []
    selected_titles = set()
    for row in fetch_chart():
        if row["views"] < MINIMUM_VIEWS:
            continue
        title, _ = parse_credit(row["chart_title"])
        title_key = norm(title)
        if not title_key or title_key in existing_titles or title_key in selected_titles:
            continue
        if row["video_id"] in existing_ids:
            continue
        selected.append(build_song(row, checked_at))
        selected_titles.add(title_key)
        if len(selected) == ADD_COUNT:
            break

    if len(selected) != ADD_COUNT:
        raise RuntimeError(
            f"Only {len(selected)} non-duplicate chart songs meet the "
            f"{MINIMUM_VIEWS:,}-view threshold; cannot honestly add {ADD_COUNT}."
        )

    print(
        f"Verified {len(selected)} songs; chart ranks "
        f"{selected[0]['chart_rank']}–{selected[-1]['chart_rank']}; "
        f"minimum observed views {min(song['verified_views'] for song in selected):,}."
    )
    if args.dry_run:
        return

    data["songs"] = base_songs + selected
    data["total"] = len(data["songs"])
    data["genres"] = sorted({genre for song in data["songs"] for genre in song.get("genre", [])})
    data["decades"] = sorted({song["decade"] for song in data["songs"] if song.get("decade")})
    SONGS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    SNAPSHOT_PATH.write_text(
        json.dumps(
            {
                "source": SOURCE_URL,
                "checked_at": checked_at,
                "minimum_views": MINIMUM_VIEWS,
                "songs": [
                    {
                        "chart_rank": song["chart_rank"],
                        "chart_title": song["chart_title"],
                        "video_id": song["id"].removeprefix("chart700m_"),
                        "views": song["verified_views"],
                    }
                    for song in selected
                ],
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Song Centre total: {data['total']}")


if __name__ == "__main__":
    main()
