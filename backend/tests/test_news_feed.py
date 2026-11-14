import json

from fastapi.testclient import TestClient

from app import news_feed
from app.main import app

client = TestClient(app)

_SAMPLE_RSS = b"""<?xml version="1.0"?>
<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/">
<channel>
<title>Sample Feed</title>
<item>
  <title>Big story breaks</title>
  <link>https://example.com/big-story</link>
  <description><![CDATA[A <b>short</b> summary of the big story, with some extra padding text to make it longer than the truncation limit so the ellipsis logic actually gets exercised in this test case.]]></description>
  <pubDate>Wed, 15 Oct 2025 10:00:00 GMT</pubDate>
  <media:thumbnail url="https://example.com/thumb.jpg" />
</item>
<item>
  <title>Second story</title>
  <link>https://example.com/second-story</link>
  <description>Shorter summary</description>
  <pubDate>Wed, 15 Oct 2025 09:00:00 GMT</pubDate>
</item>
<item>
  <title>Item missing a link is skipped</title>
  <description>no link here</description>
</item>
</channel>
</rss>"""


class _FakeResponse:
    def __init__(self, payload: bytes):
        self._payload = payload

    def read(self):
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def test_parse_items_extracts_fields_and_skips_linkless_entries():
    feed = news_feed.Feed("bbc", "world", "https://example.com/rss.xml")
    articles = news_feed._parse_items(_SAMPLE_RSS, feed)
    assert len(articles) == 2
    first = articles[0]
    assert first["title"] == "Big story breaks"
    assert first["link"] == "https://example.com/big-story"
    assert first["image"] == "https://example.com/thumb.jpg"
    assert first["source"] == "bbc"
    assert first["source_name"] == "BBC News"
    assert first["category"] == "world"
    assert first["published_ts"] > 0
    assert "<b>" not in first["summary"]
    assert first["summary"].startswith("A short summary of the big story")

    second = articles[1]
    assert second["image"] is None
    assert second["summary"] == "Shorter summary"


def test_summarize_truncates_long_text_on_a_word_boundary():
    long_text = "word " * 100  # far past the 220-char default limit
    summary = news_feed._summarize(long_text)
    assert summary.endswith("…")
    assert len(summary) <= 221
    assert not summary[:-1].endswith(" ")  # trimmed at a word boundary, no dangling space


def test_fetch_feed_caches_to_disk(monkeypatch, tmp_path):
    monkeypatch.setattr(news_feed, "CACHE_DIR", tmp_path)
    calls = []

    def fake_urlopen(req, timeout=5):
        calls.append(req.full_url)
        return _FakeResponse(_SAMPLE_RSS)

    monkeypatch.setattr(news_feed, "urlopen", fake_urlopen)

    feed = news_feed.Feed("bbc", "world", "https://example.com/rss.xml")
    articles = news_feed.fetch_feed(feed)
    assert len(articles) == 2
    assert len(calls) == 1

    # Second call within the TTL should be served from disk, not refetched.
    articles_again = news_feed.fetch_feed(feed)
    assert len(articles_again) == 2
    assert len(calls) == 1

    cache_files = list(tmp_path.glob("*.json"))
    assert len(cache_files) == 1


def test_fetch_feed_falls_back_to_stale_cache_on_failure(monkeypatch, tmp_path):
    monkeypatch.setattr(news_feed, "CACHE_DIR", tmp_path)
    feed = news_feed.Feed("bbc", "world", "https://example.com/rss.xml")
    cache_path = news_feed._feed_cache_path(feed)
    cache_path.write_text(
        json.dumps({"fetched_at": 0, "articles": [{"title": "stale", "link": "https://example.com/stale"}]}),
        encoding="utf-8",
    )

    def fake_urlopen(req, timeout=5):
        raise OSError("network unavailable")

    monkeypatch.setattr(news_feed, "urlopen", fake_urlopen)

    articles = news_feed.fetch_feed(feed)
    assert articles == [{"title": "stale", "link": "https://example.com/stale"}]


def test_get_articles_filters_dedupes_and_sorts(monkeypatch, tmp_path):
    monkeypatch.setattr(news_feed, "CACHE_DIR", tmp_path)

    def fake_fetch_feed(feed):
        if feed.source == "bbc" and feed.category == "world":
            return [
                {"title": "Older", "link": "https://a.com/1", "published_ts": 100, "category": "world", "source": "bbc"},
                {"title": "Shared", "link": "https://shared.com/x", "published_ts": 300, "category": "world", "source": "bbc"},
            ]
        if feed.source == "guardian" and feed.category == "world":
            return [
                {"title": "Newer", "link": "https://b.com/2", "published_ts": 500, "category": "world", "source": "guardian"},
                {"title": "Shared", "link": "https://shared.com/x", "published_ts": 300, "category": "world", "source": "guardian"},
            ]
        if feed.category == "technology":
            return [{"title": "Tech", "link": "https://c.com/3", "published_ts": 999, "category": "technology", "source": feed.source}]
        return []

    monkeypatch.setattr(news_feed, "fetch_feed", fake_fetch_feed)

    results = news_feed.get_articles(categories=["world"], sources=["bbc", "guardian"])
    links = [a["link"] for a in results]
    assert links == ["https://b.com/2", "https://shared.com/x", "https://a.com/1"]  # sorted by recency, deduped

    tech_results = news_feed.get_articles(categories=["technology"])
    assert [a["link"] for a in tech_results] == ["https://c.com/3"]


def test_preferences_round_trip(monkeypatch, tmp_path):
    monkeypatch.setattr(news_feed, "PREFERENCES_PATH", tmp_path / "news_preferences.json")
    monkeypatch.setattr(news_feed, "DATA_DIR", tmp_path)

    defaults = news_feed.get_preferences()
    assert defaults["categories"] == ["world"]
    assert set(defaults["sources"]) == set(news_feed.SOURCES)

    saved = news_feed.save_preferences(["technology", "bogus"], ["bbc", "nope"])
    assert saved["categories"] == ["technology"]
    assert saved["sources"] == ["bbc"]

    assert news_feed.get_preferences() == saved


def test_news_sources_endpoint():
    resp = client.get("/api/news/sources")
    assert resp.status_code == 200
    body = resp.json()
    assert {s["id"] for s in body["sources"]} == set(news_feed.SOURCES)
    assert {c["id"] for c in body["categories"]} == {c["id"] for c in news_feed.CATEGORIES}


def test_news_endpoint_uses_get_articles(monkeypatch):
    def fake_get_articles(categories=None, sources=None, limit=40):
        assert categories == ["technology"]
        assert sources == ["bbc"]
        assert limit == 5
        return [{"title": "Mocked", "link": "https://example.com/mocked"}]

    monkeypatch.setattr(news_feed, "get_articles", fake_get_articles)

    resp = client.get("/api/news", params={"categories": "technology", "sources": "bbc", "limit": 5})
    assert resp.status_code == 200
    body = resp.json()
    assert body["count"] == 1
    assert body["articles"][0]["title"] == "Mocked"
    assert "generated_at" in body


def test_news_preferences_get_and_post(monkeypatch, tmp_path):
    monkeypatch.setattr(news_feed, "PREFERENCES_PATH", tmp_path / "news_preferences.json")
    monkeypatch.setattr(news_feed, "DATA_DIR", tmp_path)

    resp = client.post("/api/news/preferences", json={"categories": ["science", "sports"], "sources": ["bbc", "nasa"]})
    assert resp.status_code == 200
    assert resp.json() == {"categories": ["science", "sports"], "sources": ["bbc", "nasa"]}

    resp2 = client.get("/api/news/preferences")
    assert resp2.status_code == 200
    assert resp2.json() == {"categories": ["science", "sports"], "sources": ["bbc", "nasa"]}
