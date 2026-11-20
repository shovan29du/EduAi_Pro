"""Enrichment for school (Grades 6-10), College (Levels 1-2), Undergraduate (Years 1-4)
and Master's (Years 1-2) lessons:
formulas (only where the topic needs one), charts, data tables, case studies and
real events, plus a related picture and description.

Two sources, kept apart so a student can tell them apart:

* **Authored content** (backend/data/lesson_enrichment/enrichment.json, built
  by backend/scripts/build_lesson_enrichment.py): reviewed formulas, tables and
  case studies. *Topic* entries match a lesson's title; *subject* entries are a
  reference sheet and landmark cases for the whole subject.
* **Wikipedia** (live, cached on disk): the best-matching article for the
  lesson topic, with its lead picture, a short description and the image
  credit. Failures are never cached, so a dropped connection can't hide a
  picture for weeks.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

from fastapi import APIRouter, HTTPException

from app import image_credit

router = APIRouter(prefix="/api/lesson-enrichment", tags=["lessons"])

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "lesson_enrichment" / "enrichment.json"
CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "lesson_enrichment_cache"
CACHE_TTL_SECONDS = 30 * 24 * 3600
LEVELS = ("6", "7", "8", "9", "10", "C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2")
HEADERS = {
    "Api-User-Agent": "EduAI/1.0 (educational; contact@eduai.app)",
    "User-Agent": "EduAI/1.0 (educational; contact@eduai.app)",
}
SEARCH_URL = "https://en.wikipedia.org/w/rest.php/v1/search/title?q={q}&limit=5"
SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

_PREFIX = re.compile(r"^Graduate Theory:\s*", re.I)
_SUFFIX = re.compile(
    r":\s*(Worked Analysis|Comparative Case Study|Independent Capstone|Conceptual Foundations|"
    r"Evidence and Data|Applied Research Seminar|Critical & Comparative Study)\s*$", re.I)


def topic_query(title: str) -> str:
    """The lesson title without the course-format words around it."""
    text = _SUFFIX.sub("", _PREFIX.sub("", title or "")).strip()
    return text or (title or "").strip()


@lru_cache(maxsize=2)
def _load(mtime: float) -> dict:
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"packs": {}, "rules": {}, "lessons": {}}


def load() -> dict:
    try:
        return _load(DATA_PATH.stat().st_mtime)
    except OSError:
        return {"packs": {}, "rules": {}, "lessons": {}}


def _fetch_json(url: str) -> dict:
    with urlopen(Request(url, headers=HEADERS), timeout=6) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _summary(title: str) -> dict | None:
    """Wikipedia page summary, or None for missing pages and disambiguations."""
    payload = _fetch_json(SUMMARY_URL.format(title=quote(title.replace(" ", "_"), safe="")))
    if payload.get("type") != "standard" or not payload.get("extract"):
        return None
    image = (payload.get("thumbnail") or {}).get("source") or (payload.get("originalimage") or {}).get("source")
    if image and not image_credit.commons_filename(image):
        image = None  # only freely licensed Commons images; Wikipedia-only files may be fair-use
    return {
        "title": payload.get("title") or title,
        "description": payload.get("description") or "",
        "extract": payload["extract"],
        "thumbnail_url": image,
        "page_url": ((payload.get("content_urls") or {}).get("desktop") or {}).get("page")
        or "https://en.wikipedia.org/wiki/" + quote(title.replace(" ", "_")),
    }


def _candidates(q: str) -> list[str]:
    parts = [q]
    if ":" in q:
        head, _, tail = q.partition(":")
        parts += [tail.strip(), head.strip()]
    seen, out = set(), []
    for part in parts:
        if part and part.lower() not in seen:
            seen.add(part.lower())
            out.append(part)
    return out


def find_article(title: str = "", q: str = "") -> dict | None:
    """Exact article when `title` is given, else the best search hit for `q`."""
    if title:
        found = _summary(title)
        if found:
            return found
    for query in _candidates(q):
        hits = _fetch_json(SEARCH_URL.format(q=quote(query))).get("pages") or []
        for hit in hits[:3]:
            found = _summary(hit.get("key") or hit.get("title") or "")
            if found:
                return found
    return None


def _credit(image_url: str | None) -> dict | None:
    if not image_url:
        return None
    try:
        record = image_credit.credit_for(image_url)
    except Exception:
        return None
    if not record:
        return None
    return {**record, "line": image_credit.credit_line(record)}


def _cache_path(key: str) -> Path:
    return CACHE_DIR / (hashlib.sha1(key.lower().encode("utf-8")).hexdigest() + ".json")


@router.get("/wiki")
def related_article(title: str = "", q: str = ""):
    """Related Wikipedia article (picture, description, credit) for a topic."""
    title, q = title.strip()[:200], q.strip()[:200]
    if not title and not q:
        raise HTTPException(status_code=400, detail="title or q is required")
    path = _cache_path(f"{title}|{q}")
    try:
        cached = json.loads(path.read_text(encoding="utf-8"))
        if time.time() - cached.get("fetched_at", 0) < CACHE_TTL_SECONDS:
            return cached["response"]
    except (OSError, ValueError, KeyError):
        pass
    try:
        article = find_article(title, q)
    except Exception:
        return {"available": False}
    response = {"available": False}
    if article:
        response = {"available": True, **article, "credit": _credit(article["thumbnail_url"])}
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"fetched_at": time.time(), "response": response}), encoding="utf-8")
    except OSError:
        pass
    return response


@router.get("/{level}/{lesson_id}")
def lesson_enrichment(level: str, lesson_id: str):
    if level.upper() not in LEVELS:
        raise HTTPException(status_code=404, detail="Enrichment is available for Grades 6-10 and for college, undergraduate and master's levels")
    data = load()
    entry = data["lessons"].get(lesson_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Lesson not found")
    rules = [data["rules"][rid] for rid in entry.get("r", []) if rid in data["rules"]]

    def merged(key, name):
        seen, out = set(), []
        for rule in rules:
            for item in rule.get(key, []):
                if item[name] not in seen:  # two rules can share a case or chart
                    seen.add(item[name])
                    out.append(item)
        return out
    pack = data["packs"].get(entry.get("p") or entry["s"]) or {}
    return {
        "lesson_id": lesson_id,
        "subject": entry["s"],
        "query": entry["q"],
        "wiki_title": next((r["wiki"] for r in rules if r.get("wiki")), ""),
        "topic": {
            "formulas": merged("formulas", "label"),
            "charts": merged("charts", "title"),
            "tables": merged("tables", "title"),
            "cases": merged("cases", "title"),
        },
        "subject_pack": {
            "tables": pack.get("tables", []),
            "cases": pack.get("cases", []),
        },
    }
