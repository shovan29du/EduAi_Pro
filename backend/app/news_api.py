"""HTTP endpoints for the dashboard's customizable world news feed.

Thin FastAPI wrapper around app.news_feed, which owns the actual fetching,
caching and preference storage.
"""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter
from pydantic import BaseModel

from app import news_feed

router = APIRouter(prefix="/api/news", tags=["news"])


class NewsPreferencesIn(BaseModel):
    categories: list[str] | None = None
    sources: list[str] | None = None


@router.get("/sources")
def news_sources():
    return news_feed.list_sources()


@router.get("/preferences")
def news_preferences_get():
    return news_feed.get_preferences()


@router.post("/preferences")
def news_preferences_save(body: NewsPreferencesIn):
    return news_feed.save_preferences(body.categories, body.sources)


@router.get("")
def news_feed_endpoint(categories: str = "", sources: str = "", limit: int = 40):
    category_list = [c for c in categories.split(",") if c] or None
    source_list = [s for s in sources.split(",") if s] or None
    limit = max(1, min(limit, 100))
    articles = news_feed.get_articles(category_list, source_list, limit=limit)
    return {
        "articles": articles,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(articles),
    }
