"""Generate original local SVG thumbnails for the BFI top-200 catalogue."""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOVIES_PATH = ROOT / "data" / "movies.json"
OUTPUT_DIR = ROOT / "data" / "movie_thumbnails"
BATCH = "bfi_sight_sound_2022_top_200"

PALETTES = [
    ("#081c2c", "#0f766e", "#5eead4"),
    ("#231942", "#5e548e", "#e0b1cb"),
    ("#271300", "#9a3412", "#fdba74"),
    ("#172554", "#1d4ed8", "#93c5fd"),
    ("#1f2937", "#4b5563", "#fbbf24"),
    ("#3f0d12", "#a71d31", "#f1c40f"),
]


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "film"


def svg_for(movie: dict) -> str:
    title = html.escape(str(movie["title"]))
    director = html.escape(str(movie.get("director") or ""))
    year = html.escape(str(movie.get("year") or ""))
    rank = html.escape(str(movie.get("all_time_poll_rank") or movie.get("all_time_list_position") or ""))
    digest = hashlib.sha256(f"{title}|{year}".encode()).digest()
    dark, mid, accent = PALETTES[digest[0] % len(PALETTES)]
    initials = "".join(word[0] for word in re.findall(r"[A-Za-z0-9]+", str(movie["title"]))[:3]).upper()
    initials = html.escape(initials or "FILM")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540" role="img" aria-labelledby="title desc">
  <title id="title">{title} thumbnail</title>
  <desc id="desc">Original EduAI Pro catalogue graphic for {title}, {year}.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{dark}"/><stop offset="1" stop-color="{mid}"/></linearGradient>
    <pattern id="grain" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.5" fill="{accent}" opacity=".18"/></pattern>
  </defs>
  <rect width="960" height="540" rx="28" fill="url(#bg)"/>
  <rect width="960" height="540" rx="28" fill="url(#grain)"/>
  <circle cx="762" cy="115" r="168" fill="{accent}" opacity=".12"/>
  <circle cx="822" cy="420" r="220" fill="{dark}" opacity=".32"/>
  <text x="64" y="72" fill="{accent}" font-family="Segoe UI,Arial,sans-serif" font-size="24" font-weight="700" letter-spacing="4">EDUAI PRO · FILM STUDIES</text>
  <text x="64" y="224" fill="#fff" font-family="Georgia,serif" font-size="104" font-weight="700">{initials}</text>
  <foreignObject x="62" y="274" width="800" height="135"><div xmlns="http://www.w3.org/1999/xhtml" style="font:700 42px/1.12 Georgia,serif;color:white;letter-spacing:-1px">{title}</div></foreignObject>
  <text x="64" y="446" fill="#fff" opacity=".82" font-family="Segoe UI,Arial,sans-serif" font-size="24">{director} · {year}</text>
  <text x="64" y="496" fill="{accent}" font-family="Segoe UI,Arial,sans-serif" font-size="22" font-weight="700">SIGHT &amp; SOUND TOP 200 · RANK {rank}</text>
</svg>
"""


def main() -> None:
    payload = json.loads(MOVIES_PATH.read_text(encoding="utf-8"))
    selected = [movie for movie in payload["movies"] if movie.get("source_batch") == BATCH]
    if len(selected) != 200:
        raise SystemExit(f"Expected 200 BFI movies, found {len(selected)}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    used: set[str] = set()
    for movie in selected:
        base = slug(f"{movie['title']}-{movie.get('year', '')}")
        filename = f"{base}.svg"
        if filename in used:
            filename = f"{base}-{movie.get('all_time_list_position', len(used) + 1)}.svg"
        used.add(filename)
        (OUTPUT_DIR / filename).write_text(svg_for(movie), encoding="utf-8")
        movie["thumbnail_url"] = f"/movie-thumbnails/{filename}"
        movie["thumbnail_type"] = "original_generated_svg"
    MOVIES_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(selected)} original thumbnails in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
