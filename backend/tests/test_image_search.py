"""Searching many free image collections (parsing is tested against sample responses; no network)."""
from app import image_search as ims


def fake(monkeypatch, routes):
    seen = []

    def _json(url):
        seen.append(url)
        for fragment, payload in routes.items():
            if fragment in url:
                if isinstance(payload, Exception):
                    raise payload
                return payload
        raise OSError("no route " + url)

    monkeypatch.setattr(ims, "_json", _json)
    return seen


def test_commons_hits_have_author_and_licence_and_skip_flags_and_logos(monkeypatch):
    fake(monkeypatch, {"commons.wikimedia.org": {"query": {"pages": {
        "1": {"index": 2, "title": "File:Flag of Peru.png", "imageinfo": [{"mime": "image/png", "url": "u1"}]},
        "2": {"index": 1, "title": "File:Alpaca farm.jpg", "imageinfo": [{"mime": "image/jpeg", "thumburl": "https://upload.wikimedia.org/t.jpg",
              "descriptionurl": "https://commons.wikimedia.org/wiki/File:Alpaca_farm.jpg",
              "extmetadata": {"Artist": {"value": "<a href='x'>Jane Doe</a>"}, "LicenseShortName": {"value": "CC BY-SA 4.0"}, "LicenseUrl": {"value": "https://creativecommons.org/licenses/by-sa/4.0"}}}]}}}}})
    hits = ims.commons("alpaca")
    assert len(hits) == 1 and hits[0]["title"] == "Alpaca farm" and hits[0]["source"] == "Wikimedia Commons"
    assert hits[0]["credit"]["line"] == "Jane Doe · CC BY-SA 4.0" and hits[0]["credit"]["source_url"].endswith("File:Alpaca_farm.jpg")


def test_openverse_hits_name_the_provider_and_licence(monkeypatch):
    fake(monkeypatch, {"openverse.org": {"results": [
        {"title": "Knot", "thumbnail": "https://api.openverse.org/t/1", "url": "https://flickr/1.jpg", "creator": "Sam", "license": "by", "license_version": "2.0",
         "license_url": "https://creativecommons.org/licenses/by/2.0/", "foreign_landing_url": "https://flickr/p/1", "source": "flickr"},
        {"title": "Public", "url": "https://x/2.jpg", "license": "cc0", "creator": None, "source": "met"}]}})
    hits = ims.openverse("knot")
    assert hits[0]["source"] == "Openverse (flickr)" and hits[0]["credit"]["line"] == "Sam · CC BY 2.0"
    assert hits[0]["fallback_url"] == "https://flickr/1.jpg" and hits[1]["credit"]["license"] == "CC0 1.0"


def test_museum_sources_return_only_public_domain_pictures(monkeypatch):
    fake(monkeypatch, {
        "metmuseum.org/public/collection/v1/search": {"objectIDs": [1, 2]},
        "objects/1": {"isPublicDomain": True, "primaryImageSmall": "https://images.metmuseum.org/a.jpg", "title": "Vase", "artistDisplayName": "Anon", "objectURL": "https://met/1"},
        "objects/2": {"isPublicDomain": False, "primaryImageSmall": "https://images.metmuseum.org/b.jpg", "title": "Other"},
        "artic.edu": {"data": [{"id": 5, "title": "Bowl", "image_id": "abc", "is_public_domain": True, "artist_title": "Maker"}, {"id": 6, "title": "No", "image_id": "d", "is_public_domain": False}]},
        "clevelandart.org": {"data": [{"title": "Mask", "url": "https://cma/1", "share_license_status": "CC0", "images": {"web": {"url": "https://cdn/m.jpg"}}, "creators": [{"description": "Artist X (Greek)"}]},
                                       {"title": "Closed", "share_license_status": "Copyrighted", "images": {"web": {"url": "https://cdn/c.jpg"}}}]}})
    assert [h["title"] for h in ims.met("vase")] == ["Vase"]
    chicago = ims.chicago("bowl")
    assert [h["title"] for h in chicago] == ["Bowl"] and chicago[0]["url"] == "https://www.artic.edu/iiif/2/abc/full/843,/0/default.jpg"
    assert [h["title"] for h in ims.cleveland("mask")] == ["Mask"]


def test_nasa_and_library_of_congress(monkeypatch):
    fake(monkeypatch, {
        "images-api.nasa.gov": {"collection": {"items": [{"data": [{"title": "Moon", "nasa_id": "PIA1", "center": "JPL"}], "links": [{"href": "https://images-assets.nasa.gov/moon.jpg"}]}]}},
        "loc.gov": {"results": [{"title": "Farm", "url": "https://www.loc.gov/item/1", "image_url": ["//tile.loc.gov/x.gif", "//tile.loc.gov/x.jpg"]}]}})
    assert ims.nasa("moon")[0]["credit"]["credit"] == "JPL"
    loc = ims.loc("farm")[0]
    assert loc["url"] == "https://tile.loc.gov/x.jpg" and "check rights" in loc["credit"]["line"]


def test_search_merges_sources_in_order_skips_failures_and_duplicates(monkeypatch):
    def source(name, urls):
        return lambda q: [ims._hit(name, u, u) for u in urls]

    def broken(q):
        raise OSError("down")

    monkeypatch.setattr(ims, "SOURCES", {"a": source("A", ["1", "2"]), "b": broken, "c": source("C", ["2", "3"])})
    problems = []
    hits = ims.search("x", order=("c", "b", "a"), log=problems)
    assert [h["url"] for h in hits] == ["2", "3", "1"]  # c first, duplicate "2" dropped
    assert problems == ["b: down"]
    assert ims.search("   ") == []
