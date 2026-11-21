"""World news feed: a customizable digital newspaper for the dashboard.

Pulls from public, free RSS feeds (no API key required) across several
outlets and categories, parses them with the standard library only (no new
dependency), and caches each feed on disk with a short TTL so the same
headlines aren't re-fetched from the outlet on every dashboard view. Falls
back to a stale cached copy if a feed is temporarily unreachable, the same
resilience pattern used by the museum thumbnail cache.

"Customize" means picking which categories and which outlets to show;
that choice is persisted server-side (single-owner app, like
settings_store.py) so it's remembered across sessions and devices.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import time
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from xml.etree import ElementTree

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CACHE_DIR = DATA_DIR / "news_cache"
PREFERENCES_PATH = DATA_DIR / "news_preferences.json"

FEED_TTL_SECONDS = 15 * 60  # headlines refresh every 15 minutes at most
FETCH_TIMEOUT_SECONDS = 6
USER_AGENT = "EduAI/1.0 (educational digital newspaper; contact@eduai.app)"

_MEDIA_NS = "{http://search.yahoo.com/mrss/}"

CATEGORIES = [
    {"id": "world", "label": "World", "emoji": "🌍"},
    {"id": "business", "label": "Business", "emoji": "💼"},
    {"id": "technology", "label": "Technology", "emoji": "💻"},
    {"id": "science", "label": "Science", "emoji": "🔬"},
    {"id": "health", "label": "Health", "emoji": "🩺"},
    {"id": "sports", "label": "Sports", "emoji": "🏆"},
    {"id": "entertainment", "label": "Entertainment", "emoji": "🎬"},
]
_CATEGORY_IDS = {c["id"] for c in CATEGORIES}
_CATEGORY_EMOJI = {c["id"]: c["emoji"] for c in CATEGORIES}

SOURCES = {
    "bbc": {"name": "BBC News", "homepage": "https://www.bbc.com/news"},
    "guardian": {"name": "The Guardian", "homepage": "https://www.theguardian.com"},
    "aljazeera": {"name": "Al Jazeera", "homepage": "https://www.aljazeera.com"},
    "nasa": {"name": "NASA", "homepage": "https://www.nasa.gov"},
    "un": {"name": "UN News", "homepage": "https://news.un.org"},
}
_SOURCE_IDS = set(SOURCES)


@dataclass(frozen=True)
class Feed:
    source: str
    category: str
    url: str


FEEDS: list[Feed] = [
    Feed("bbc", "world", "http://feeds.bbci.co.uk/news/world/rss.xml"),
    Feed("bbc", "business", "http://feeds.bbci.co.uk/news/business/rss.xml"),
    Feed("bbc", "technology", "http://feeds.bbci.co.uk/news/technology/rss.xml"),
    Feed("bbc", "science", "http://feeds.bbci.co.uk/news/science_environment/rss.xml"),
    Feed("bbc", "health", "http://feeds.bbci.co.uk/news/health/rss.xml"),
    Feed("bbc", "sports", "http://feeds.bbci.co.uk/sport/rss.xml?edition=int"),
    Feed("bbc", "entertainment", "http://feeds.bbci.co.uk/news/entertainment_arts/rss.xml"),
    Feed("guardian", "world", "https://www.theguardian.com/world/rss"),
    Feed("guardian", "business", "https://www.theguardian.com/business/rss"),
    Feed("guardian", "technology", "https://www.theguardian.com/technology/rss"),
    Feed("guardian", "science", "https://www.theguardian.com/science/rss"),
    Feed("guardian", "sports", "https://www.theguardian.com/sport/rss"),
    Feed("guardian", "entertainment", "https://www.theguardian.com/culture/rss"),
    Feed("aljazeera", "world", "https://www.aljazeera.com/xml/rss/all.xml"),
    Feed("nasa", "science", "https://www.nasa.gov/feed/"),
    Feed("un", "world", "https://news.un.org/en/rss.xml"),
]

DEFAULT_CATEGORIES = ["world"]
DEFAULT_SOURCES = sorted(_SOURCE_IDS)

_TAG_RE = re.compile(r"<[^>]+>")
_WHITESPACE_RE = re.compile(r"\s+")


def _strip_html(text: str) -> str:
    text = _TAG_RE.sub(" ", text or "")
    text = html.unescape(text)
    return _WHITESPACE_RE.sub(" ", text).strip()


def _summarize(text: str, limit: int = 220) -> str:
    clean = _strip_html(text)
    if len(clean) <= limit:
        return clean
    return clean[:limit].rsplit(" ", 1)[0] + "…"


def _parse_published(raw: str | None) -> tuple[str | None, float]:
    if not raw:
        return None, 0.0
    try:
        dt = parsedate_to_datetime(raw)
        if dt.tzinfo is None:
            return raw, dt.timestamp()
        return raw, dt.timestamp()
    except (TypeError, ValueError):
        return raw, 0.0


def _item_image(item: ElementTree.Element) -> str | None:
    enclosure = item.find("enclosure")
    if enclosure is not None:
        enc_type = enclosure.get("type", "")
        if enc_type.startswith("image") and enclosure.get("url"):
            return enclosure.get("url")
    thumb = item.find(f"{_MEDIA_NS}thumbnail")
    if thumb is not None and thumb.get("url"):
        return thumb.get("url")
    content = item.find(f"{_MEDIA_NS}content")
    if content is not None and (content.get("medium") == "image" or "image" in (content.get("type") or "")):
        if content.get("url"):
            return content.get("url")
    # Fall back to the first <img> tag inside the HTML description, if any.
    description = item.findtext("description") or ""
    match = re.search(r'<img[^>]+src="([^"]+)"', description)
    return match.group(1) if match else None


def _parse_items(xml_bytes: bytes, feed: Feed) -> list[dict]:
    root = ElementTree.fromstring(xml_bytes)
    source_name = SOURCES[feed.source]["name"]
    articles = []
    for item in root.iter("item"):
        title = _strip_html(item.findtext("title") or "")
        link = (item.findtext("link") or "").strip()
        if not title or not link:
            continue
        published_raw, published_ts = _parse_published(item.findtext("pubDate"))
        articles.append({
            "title": title,
            "link": link,
            "summary": _summarize(item.findtext("description") or ""),
            "image": _item_image(item),
            "source": feed.source,
            "source_name": source_name,
            "category": feed.category,
            "published": published_raw,
            "published_ts": published_ts,
        })
    return articles


def _feed_cache_path(feed: Feed) -> Path:
    digest = hashlib.sha1(feed.url.encode("utf-8")).hexdigest()
    return CACHE_DIR / f"{digest}.json"


def fetch_feed(feed: Feed) -> list[dict]:
    """Return this feed's articles, using a short-lived disk cache.

    Any single feed being slow, down, or returning malformed XML degrades
    to an empty (or stale) list for that one outlet/category rather than
    breaking the whole dashboard widget.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = _feed_cache_path(feed)
    now = time.time()
    cached: dict | None = None
    if cache_path.exists():
        try:
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            cached = None
        if cached and now - cached.get("fetched_at", 0) < FEED_TTL_SECONDS:
            return cached.get("articles", [])

    try:
        req = Request(feed.url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/xml, text/xml"})
        with urlopen(req, timeout=FETCH_TIMEOUT_SECONDS) as resp:
            raw = resp.read()
        articles = _parse_items(raw, feed)
    except (HTTPError, URLError, OSError, ElementTree.ParseError, TimeoutError):
        if cached:
            return cached.get("articles", [])
        return []

    try:
        cache_path.write_text(json.dumps({"fetched_at": now, "articles": articles}), encoding="utf-8")
    except OSError:
        pass
    return articles


def list_sources() -> dict:
    return {
        "sources": [{"id": sid, **info} for sid, info in SOURCES.items()],
        "categories": CATEGORIES,
    }


def _normalize_ids(requested: list[str] | None, valid: set[str], default: list[str]) -> list[str]:
    if not requested:
        return list(default)
    picked = [r for r in requested if r in valid]
    return picked or list(default)


def get_articles(categories: list[str] | None = None, sources: list[str] | None = None, limit: int = 40) -> list[dict]:
    wanted_categories = _normalize_ids(categories, _CATEGORY_IDS, [c["id"] for c in CATEGORIES])
    wanted_sources = _normalize_ids(sources, _SOURCE_IDS, DEFAULT_SOURCES)

    seen_links: set[str] = set()
    combined: list[dict] = []
    for feed in FEEDS:
        if feed.category not in wanted_categories or feed.source not in wanted_sources:
            continue
        for article in fetch_feed(feed):
            if article["link"] in seen_links:
                continue
            seen_links.add(article["link"])
            combined.append(article)

    combined.sort(key=lambda a: a.get("published_ts", 0), reverse=True)
    return combined[:limit]


def _read_preferences() -> dict:
    try:
        return json.loads(PREFERENCES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def get_preferences() -> dict:
    stored = _read_preferences()
    categories = _normalize_ids(stored.get("categories"), _CATEGORY_IDS, DEFAULT_CATEGORIES)
    sources = _normalize_ids(stored.get("sources"), _SOURCE_IDS, DEFAULT_SOURCES)
    return {"categories": categories, "sources": sources}


def save_preferences(categories: list[str] | None, sources: list[str] | None) -> dict:
    prefs = {
        "categories": _normalize_ids(categories, _CATEGORY_IDS, DEFAULT_CATEGORIES),
        "sources": _normalize_ids(sources, _SOURCE_IDS, DEFAULT_SOURCES),
    }
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PREFERENCES_PATH.write_text(json.dumps(prefs, indent=2), encoding="utf-8")
    return prefs


def category_emoji(category_id: str) -> str:
    return _CATEGORY_EMOJI.get(category_id, "📰")
