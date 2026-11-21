import json

import pytest
from fastapi.testclient import TestClient

from app import lesson_enrichment as le
from app.main import app

client = TestClient(app)

DATA = {
    "packs": {
        "school:Finance": {"tables": [{"title": "Simple budget", "headers": ["Share", "Use"], "rows": [["50%", "Needs"]]}], "cases": [{"title": "Grameen", "when": "1983", "summary": "s", "takeaway": "t", "wiki": "Grameen Bank"}]},
        "Finance": {
            "tables": [{"title": "Ratios", "headers": ["Ratio", "Formula"], "rows": [["P/E", "Price ÷ EPS"]]}],
            "cases": [{"title": "LTCM", "when": "1998", "summary": "s", "takeaway": "t", "wiki": "Long-Term Capital Management"}],
        },
    },
    "rules": {
        "options2": {"cases": [{"title": "CBOE", "when": "1973", "summary": "dup", "takeaway": "dup", "wiki": ""}], "formulas": [{"label": "Put–call parity", "expr": "dup", "note": ""}]},
        "options": {"wiki": "Black–Scholes model", "formulas": [{"label": "Put–call parity", "expr": "C − P = S − K e^(−rT)", "note": ""}],
                    "charts": [{"title": "Payoff", "kind": "line", "x_label": "S", "y_label": "P", "data": [{"x": 1, "Call": 0}], "series": ["Call"], "lines": [], "note": "", "log": False}],
                    "cases": [{"title": "CBOE", "when": "1973", "summary": "s", "takeaway": "t", "wiki": "Black–Scholes model"}]},
    },
    "lessons": {
        "finance-m1-l1": {"s": "Finance", "q": "Option Pricing", "r": ["options"]},
        "finance-m1-l2": {"s": "Finance", "q": "Bond Math"},
        "finance-m1-l3": {"s": "Finance", "q": "Option Pricing", "r": ["options", "options2"]},
        "finance-g8-l1": {"s": "Finance", "q": "Budgeting", "p": "school:Finance"},
    },
}


@pytest.fixture(autouse=True)
def isolated(tmp_path, monkeypatch):
    path = tmp_path / "enrichment.json"
    path.write_text(json.dumps(DATA), encoding="utf-8")
    monkeypatch.setattr(le, "DATA_PATH", path)
    monkeypatch.setattr(le, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(le.image_credit, "credit_for", lambda url: {"artist": "A. Photographer", "credit": "A. Photographer", "license": "CC BY-SA 4.0", "license_url": "https://example.org/l", "source_url": "https://example.org/s"})


def test_topic_query_strips_course_format_words():
    assert le.topic_query("Graduate Theory: Nutrition & Menu Design: Worked Analysis") == "Nutrition & Menu Design"
    assert le.topic_query("Regional Organisations: Comparative Case Study") == "Regional Organisations"
    assert le.topic_query("Spectre and Meltdown") == "Spectre and Meltdown"


def test_lesson_gets_topic_content_and_subject_pack():
    body = client.get("/api/lesson-enrichment/M1/finance-m1-l1").json()
    assert body["wiki_title"] == "Black–Scholes model"
    assert body["topic"]["formulas"][0]["label"] == "Put–call parity"
    assert body["topic"]["charts"][0]["title"] == "Payoff"
    assert body["topic"]["cases"][0]["title"] == "CBOE"
    assert "formulas" not in body["subject_pack"]  # equations only come from topic rules
    assert body["subject_pack"]["tables"][0]["rows"] == [["P/E", "Price ÷ EPS"]]
    assert body["subject_pack"]["cases"][0]["wiki"] == "Long-Term Capital Management"


def test_lesson_without_topic_rules_still_gets_subject_pack():
    body = client.get("/api/lesson-enrichment/m1/finance-m1-l2").json()
    assert body["topic"] == {"formulas": [], "charts": [], "tables": [], "cases": []}
    assert body["wiki_title"] == ""
    assert body["query"] == "Bond Math"
    assert body["subject_pack"]["cases"]


def test_other_levels_and_unknown_lessons_are_404():
    assert client.get("/api/lesson-enrichment/5/finance-m1-l1").status_code == 404  # Grades 1-5 are not enriched
    assert client.get("/api/lesson-enrichment/ug2/finance-m1-l1").status_code == 200  # level only gates which lessons are enriched
    for level in ("6", "10", "C1", "c2"):
        assert client.get(f"/api/lesson-enrichment/{level}/finance-m1-l1").status_code == 200
    assert client.get("/api/lesson-enrichment/M2/nope").status_code == 404


def test_missing_data_file_is_a_404_not_a_crash(monkeypatch, tmp_path):
    monkeypatch.setattr(le, "DATA_PATH", tmp_path / "absent.json")
    assert client.get("/api/lesson-enrichment/M1/finance-m1-l1").status_code == 404


def _wiki(monkeypatch, pages):
    calls = []

    def fake(url):
        calls.append(url)
        if "/search/title" in url:
            return {"pages": [{"key": k} for k in pages.get("search", [])]}
        title = url.rsplit("/", 1)[-1]
        payload = pages.get("summary", {}).get(title)
        if payload is None:
            raise OSError("404")
        return payload

    monkeypatch.setattr(le, "_fetch_json", fake)
    return calls


ARTICLE = {"type": "standard", "title": "Black–Scholes model", "description": "Mathematical model", "extract": "The Black–Scholes model estimates the price of options.",
           "thumbnail": {"source": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/BS.png/320px-BS.png"},
           "content_urls": {"desktop": {"page": "https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model"}}}


def test_related_article_by_exact_title_includes_picture_and_credit(monkeypatch):
    _wiki(monkeypatch, {"summary": {"Black%E2%80%93Scholes_model": ARTICLE}})
    body = client.get("/api/lesson-enrichment/wiki", params={"title": "Black–Scholes model"}).json()
    assert body["available"] is True
    assert body["title"] == "Black–Scholes model"
    assert body["thumbnail_url"].endswith("320px-BS.png")
    assert body["credit"]["license"] == "CC BY-SA 4.0"
    assert body["credit"]["line"].startswith("A. Photographer")


def test_related_article_falls_back_to_search_and_skips_disambiguation(monkeypatch):
    calls = _wiki(monkeypatch, {"search": ["Mercury", "Mercury_(element)"], "summary": {
        "Mercury": {"type": "disambiguation", "title": "Mercury", "extract": "Mercury may refer to"},
        "Mercury_%28element%29": {**ARTICLE, "title": "Mercury (element)"}}})
    body = client.get("/api/lesson-enrichment/wiki", params={"q": "Mercury"}).json()
    assert body["title"] == "Mercury (element)"
    assert any("/search/title" in c for c in calls)


def test_related_article_is_cached_and_failures_are_not(monkeypatch):
    calls = _wiki(monkeypatch, {"summary": {"Black%E2%80%93Scholes_model": ARTICLE}})
    params = {"title": "Black–Scholes model"}
    client.get("/api/lesson-enrichment/wiki", params=params)
    client.get("/api/lesson-enrichment/wiki", params=params)
    assert len(calls) == 1

    def boom(url):
        raise OSError("offline")

    monkeypatch.setattr(le, "_fetch_json", boom)
    assert client.get("/api/lesson-enrichment/wiki", params={"q": "Anything"}).json() == {"available": False}
    _wiki(monkeypatch, {"summary": {"Anything": {**ARTICLE, "title": "Anything"}}})
    assert client.get("/api/lesson-enrichment/wiki", params={"title": "Anything"}).json()["available"] is True


def test_related_article_requires_a_query():
    assert client.get("/api/lesson-enrichment/wiki").status_code == 400


def test_non_commons_images_are_dropped(monkeypatch):
    fair_use = {**ARTICLE, "thumbnail": {"source": "https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/Logo.png/220px-Logo.png"}}
    _wiki(monkeypatch, {"summary": {"Logo": fair_use}})
    body = client.get("/api/lesson-enrichment/wiki", params={"title": "Logo"}).json()
    assert body["available"] is True and body["thumbnail_url"] is None and body["credit"] is None


def test_items_shared_by_two_rules_are_listed_once():
    body = client.get("/api/lesson-enrichment/M1/finance-m1-l3").json()
    assert [c["title"] for c in body["topic"]["cases"]] == ["CBOE"]
    assert [f["label"] for f in body["topic"]["formulas"]] == ["Put–call parity"]


def test_school_lessons_use_the_school_subject_sheet():
    body = client.get("/api/lesson-enrichment/8/finance-g8-l1").json()
    assert body["subject"] == "Finance"
    assert body["subject_pack"]["tables"][0]["title"] == "Simple budget"
    adult = client.get("/api/lesson-enrichment/M1/finance-m1-l2").json()
    assert adult["subject_pack"]["tables"][0]["title"] == "Ratios"


# ---- skill lessons: a picture for lessons whose title is not an article name ----

def test_candidates_use_the_brackets_and_the_subject():
    out = le._candidates("Installing a Zipper (Basic Centered Zipper)", "Sewing and Crafts")
    assert out[0] == "Installing a Zipper (Basic Centered Zipper)"
    assert "Installing a Zipper" in out and "Basic Centered Zipper" in out
    assert out[-2:] == ["Installing a Zipper Sewing and Crafts", "Sewing and Crafts"]
    assert le._candidates("Judo", "") == ["Judo"]


def _searching(monkeypatch, titles=None, pages=None, page_hits=None):
    """Wikipedia stand-in: `titles` answers title search, `page_hits` full-text search."""
    from urllib.error import HTTPError
    seen = []

    def fake(url):
        seen.append(url)
        if "/search/title" in url:
            return {"pages": [{"key": k} for k in (titles or {}).get(url.split("q=")[1].split("&")[0], [])]}
        if "/search/page" in url:
            return {"pages": [{"key": k} for k in (page_hits or {}).get(url.split("q=")[1].split("&")[0], [])]}
        key = url.rsplit("/", 1)[-1]
        if key not in pages:
            raise HTTPError(url, 404, "Not Found", {}, None)
        return pages[key]

    monkeypatch.setattr(le, "_fetch_json", fake)
    return seen


def test_a_title_that_is_not_an_article_falls_back_to_search_instead_of_failing(monkeypatch):
    _searching(monkeypatch, titles={"Timber%20Hitch%20Rope%20and%20Knots": ["Timber_hitch"]},
               pages={"Timber_hitch": {**ARTICLE, "title": "Timber hitch"}})
    body = client.get("/api/lesson-enrichment/wiki", params={
        "title": "Timber Hitch", "q": "Timber Hitch", "ctx": "Rope and Knots"}).json()
    assert body["available"] is True and body["title"] == "Timber hitch"


def test_full_text_search_finds_descriptive_titles(monkeypatch):
    _searching(monkeypatch, page_hits={"Stranger%20Awareness": ["Stranger_danger"]},
               pages={"Stranger_danger": {**ARTICLE, "title": "Stranger danger"}})
    body = client.get("/api/lesson-enrichment/wiki", params={"q": "Stranger Awareness"}).json()
    assert body["title"] == "Stranger danger"


def test_an_article_with_a_picture_beats_one_without(monkeypatch):
    bare = {**ARTICLE, "title": "Stance", "thumbnail": None}
    _searching(monkeypatch, titles={"Stance": ["Stance"], "Stance%20Judo": ["Judo"]},
               pages={"Stance": bare, "Judo": {**ARTICLE, "title": "Judo"}})
    body = client.get("/api/lesson-enrichment/wiki", params={"q": "Stance", "ctx": "Judo"}).json()
    assert body["title"] == "Judo" and body["thumbnail_url"]


def test_an_article_without_any_picture_is_still_returned(monkeypatch):
    bare = {**ARTICLE, "title": "Stance", "thumbnail": None}
    _searching(monkeypatch, titles={"Stance": ["Stance"]}, pages={"Stance": bare})
    body = client.get("/api/lesson-enrichment/wiki", params={"q": "Stance"}).json()
    assert body["available"] is True and body["thumbnail_url"] is None
