import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import link_check_report as lcr  # noqa: E402


def _check(status, reachable, error=""):
    return {"url": "", "status": status, "reachable": reachable, **({"error": error} if error else {})}


def test_retry_recovers_from_a_transient_failure_but_not_a_real_404():
    seen = []

    def flaky(url):
        seen.append(url)
        return {"url": url, "status": 200, "reachable": True} if len(seen) > 1 else {"url": url, "status": 503, "reachable": False}

    assert lcr.check_with_retry("https://a.example/x", flaky, delay=0)["reachable"] is True
    assert len(seen) == 2

    dead = lambda url: {"url": url, "status": 404, "reachable": False}  # noqa: E731
    assert lcr.check_with_retry("https://a.example/y", dead, delay=0)["reachable"] is False

    ok_calls = []
    lcr.check_with_retry("https://a.example/z", lambda u: ok_calls.append(u) or {"url": u, "status": 200, "reachable": True}, delay=0)
    assert len(ok_calls) == 1  # healthy links are only requested once


def _result(status=None, error="", reachable=False):
    return {"url": "https://x.example", "status": status, "reachable": reachable, **({"error": error} if error else {})}


def test_only_gone_pages_and_missing_domains_count_as_broken():
    assert lcr.classify(_result(404))["reachable"] is False
    assert lcr.classify(_result(410))["reason"] == "HTTP 410"
    gone = lcr.classify(_result(None, "<urlopen error [Errno -2] Name or service not known>"))
    assert gone["reachable"] is False and gone["reason"] == "domain does not exist"
    for ambiguous in (_result(400), _result(418), _result(503), _result(None, "timed out"),
                      _result(None, "<urlopen error [Errno -3] Temporary failure in name resolution>")):
        assert lcr.classify(ambiguous)["reachable"] is None, ambiguous
    ok = {"url": "u", "status": 200, "reachable": True}
    assert lcr.classify(ok) is ok


def test_check_urls_does_not_blame_links_when_dns_fails_everywhere():
    nx = "<urlopen error [Errno -2] Name or service not known>"
    urls = [f"https://h{i}.example" for i in range(20)]
    results = lcr.check_urls(urls, 4, checker=lambda u: {"url": u, "status": None, "reachable": None, "error": nx}, delay=0)
    assert all(r["reachable"] is None for r in results)
    assert "runner network problem" in results[0]["error"]

    mixed = lcr.check_urls(["https://a.example", "https://dead.example"], 2, delay=0, checker=lambda u: (
        {"url": u, "status": None, "reachable": None, "error": nx} if "dead" in u else {"url": u, "status": 200, "reachable": True}))
    assert [r["reachable"] for r in mixed] == [True, False]  # one dead domain among healthy links is reported


def _api(pages, normalized=(), redirects=()):
    return {"query": {"normalized": [{"from": a, "to": b} for a, b in normalized],
                      "redirects": [{"from": a, "to": b} for a, b in redirects],
                      "pages": {str(i): p for i, p in enumerate(pages)}}}


def test_find_missing_titles_follows_normalisation_and_redirects():
    def fetch(url):
        assert "titles=Mona%20Lisa%7Csunflowers%7CGone%20Page" in url or "Gone" in url
        return _api(
            [{"title": "Mona Lisa"}, {"title": "Sunflowers (series of paintings)"}, {"title": "Gone Page", "missing": ""}],
            normalized=[("sunflowers", "Sunflowers")],
            redirects=[("Sunflowers", "Sunflowers (series of paintings)")],
        )

    missing, unchecked = lcr.find_missing_titles("https://en.wikipedia.org/w/api.php", ["Mona Lisa", "sunflowers", "Gone Page"], fetch=fetch)
    assert missing == ["Gone Page"] and unchecked == []


def test_find_missing_titles_batches_and_reports_unchecked_on_api_failure():
    batches = []

    def fetch(url):
        batches.append(url)
        if len(batches) == 2:
            raise OSError("down")
        return _api([])

    titles = [f"T{i:03d}" for i in range(120)]
    missing, unchecked = lcr.find_missing_titles("https://x/api.php", titles, fetch=fetch)
    assert len(batches) == 3 and missing == [] and len(unchecked) == 50  # only the failed batch


def test_commons_files_use_the_file_prefix():
    seen = []
    lcr.find_missing_titles("https://c/api.php", ["Pic.jpg"], prefix="File:", fetch=lambda u: seen.append(u) or _api([{"title": "File:Pic.jpg", "missing": ""}]))
    assert "File%3APic.jpg" in seen[0]
    missing, _ = lcr.find_missing_titles("https://c/api.php", ["Pic.jpg"], prefix="File:", fetch=lambda u: _api([{"title": "File:Pic.jpg", "missing": ""}]))
    assert missing == ["Pic.jpg"]


def _report(checks, sources=None, wiki_missing=(), commons_missing=()):
    return lcr.build_report(
        checks, sources or {}, list(wiki_missing), [], list(commons_missing), [],
        {"Gone Page": ["wc_1"]}, {"Gone.jpg": ["wc_2"]},
        {"data_files": 3, "unique_urls": 10, "malformed_urls": [], "wikipedia_titles": 5, "commons_files": 2},
    )


def test_report_lists_broken_links_with_their_source_files_and_flags_problems():
    checks = [
        {"url": "https://ok.example/a", "status": 200, "reachable": True},
        {"url": "https://dead.example/b", "status": 404, "reachable": False, "reason": "HTTP 404"},
        {"url": "https://slow.example/c", "status": None, "reachable": None, "error": "timed out"},
    ]
    report = _report(checks, {"https://dead.example/b": ["backend/data/x.json"]}, wiki_missing=["Gone Page"], commons_missing=["Gone.jpg"])
    assert lcr.has_problems(report)
    md = lcr.render_markdown(report)
    assert "| https://dead.example/b | HTTP 404 | backend/data/x.json |" in md
    assert "| Gone Page | wc_1 |" in md and "| Gone.jpg | wc_2 |" in md
    assert "3 checked, 1 reachable, 1 broken, 1 inconclusive" in md
    assert "https://slow.example/c - timed out" in md
    assert "https://ok.example/a" not in md


def test_clean_run_and_inconclusive_only_do_not_fail():
    clean = _report([{"url": "https://ok.example", "status": 200, "reachable": True}])
    assert not lcr.has_problems(clean) and "No broken links found" in lcr.render_markdown(clean)
    assert "Incomplete check" not in lcr.render_markdown(clean) and ":white_check_mark:" in lcr.render_markdown(clean)
    only_flaky = _report([{"url": "https://slow.example", "status": None, "reachable": None, "error": "x"}])
    assert not lcr.has_problems(only_flaky)
    md = lcr.render_markdown(only_flaky)
    assert "Incomplete check" in md and ":white_check_mark:" not in md


def test_long_lists_are_truncated_in_markdown():
    checks = [{"url": f"https://d.example/{i}", "status": 404, "reachable": False} for i in range(30)]
    md = lcr.render_markdown(_report(checks), limit=10)
    assert "...and 20 more" in md and "https://d.example/29" not in md


def test_collect_sources_and_museum_titles(tmp_path, monkeypatch):
    f = tmp_path / "a.json"
    f.write_text(json.dumps({"x": [{"u": "https://one.example/p", "t": "see https://not-whole-string.example"}]}), encoding="utf-8")
    monkeypatch.setattr(lcr, "ROOT", tmp_path)
    assert lcr.collect_sources([f]) == {"https://one.example/p": ["a.json"]}

    museum = tmp_path / "museum.json"
    museum.write_text(json.dumps({"galleries": {"g": {"objects": [
        {"id": "o1", "wiki_title": "Mona Lisa", "links": {"wikipedia": "https://en.wikipedia.org/wiki/Mona_Lisa"},
         "thumbnail_local": "https://commons.wikimedia.org/wiki/Special:FilePath/Mona_Lisa%2C_by_Leonardo.jpg"},
        {"id": "o2", "wiki_title": "", "links": {"wikipedia": "https://en.wikipedia.org/wiki/The_Kiss_(Klimt)#History"}},
    ]}}}), encoding="utf-8")
    monkeypatch.setattr(lcr, "MUSEUM_PATH", museum)
    wiki, commons = lcr.museum_titles()
    assert wiki == {"Mona Lisa": ["o1"], "The Kiss (Klimt)": ["o2"]}
    assert commons == {"Mona Lisa, by Leonardo.jpg": ["o1"]}


def test_main_writes_reports_and_returns_status(tmp_path, monkeypatch):
    data = tmp_path / "d.json"
    data.write_text(json.dumps({"links": ["https://dead.example/x", "https://ok.example/y"]}), encoding="utf-8")
    monkeypatch.setattr(lcr, "ROOT", tmp_path)
    monkeypatch.setattr(lcr, "json_files", lambda: [data])
    monkeypatch.setattr(lcr, "check_urls", lambda urls, workers: [
        {"url": u, "status": 404 if "dead" in u else 200, "reachable": "dead" not in u} for u in urls
    ])
    code = lcr.main(["--out-dir", str(tmp_path / "out"), "--skip-museum"])
    assert code == 1
    saved = json.loads((tmp_path / "out" / "link_report.json").read_text(encoding="utf-8"))
    assert [b["url"] for b in saved["broken"]] == ["https://dead.example/x"]
    assert saved["broken"][0]["found_in"] == ["d.json"]
    assert "https://dead.example/x" in (tmp_path / "out" / "link_report.md").read_text(encoding="utf-8")

    monkeypatch.setattr(lcr, "check_urls", lambda urls, workers: [{"url": u, "status": 200, "reachable": True} for u in urls])
    assert lcr.main(["--out-dir", str(tmp_path / "out2"), "--skip-museum"]) == 0
