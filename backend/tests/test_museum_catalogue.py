"""The Virtual Museum holds real, individually named objects, not generic placeholders."""
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
MUSEUM = json.loads((BASE / "data" / "virtual_museum" / "museum.json").read_text(encoding="utf-8"))
OBJECTS = [(gid, o) for gid, g in MUSEUM["galleries"].items() for o in g["objects"]]
MET = [o for _, o in OBJECTS if str(o["id"]).startswith("met_")]


def test_no_generic_country_and_type_cards_remain():
    assert not [o["name"] for _, o in OBJECTS if o.get("museum") == "Various world collections"]
    assert not [o["id"] for _, o in OBJECTS if re.fullmatch(r"wc_\d+", str(o["id"]))]
    assert not [g for g in MUSEUM["galleries"] if g.startswith("world_") and g != "world_heritage_treasures"]


def test_object_ids_are_unique_within_each_gallery():
    for gid, gallery in MUSEUM["galleries"].items():
        ids = [o["id"] for o in gallery["objects"]]
        assert len(ids) == len(set(ids)), gid
    assert len([o["id"] for o in MET]) == len({o["id"] for o in MET})


def test_met_catalogue_is_large_and_ranked():
    assert len(MET) >= 5000
    ranks = [o["source_rank"] for o in MET]
    assert len(set(ranks)) == len(ranks) and min(ranks) >= 1  # gaps are objects removed later as duplicates or generic
    assert len({o["met_id"] for o in MET}) == len(MET)


def test_met_objects_are_complete_and_credited():
    for o in MET:
        assert all(o.get(k) for k in ("id", "name", "description", "significance", "museum", "origin", "category", "links", "quiz", "activity")), o["id"]
        assert o["id"] == f"met_{o['met_id']}" and o["source_id"] == f"met-{o['met_id']}"
        assert o["museum"].startswith("The Metropolitan Museum of Art")
        assert o["links"]["museum_object"].startswith("https://www.metmuseum.org/") and "virtual_tour" in o["links"]
        assert "CC0" in o["source"]
        quiz = o["quiz"]
        assert len(quiz["options"]) == 4 and len(set(quiz["options"])) == 4 and 0 <= quiz["answer"] < 4


def test_met_names_are_specific_not_bare_generic_words():
    bare = {"bowl", "plate", "vase", "cup", "dish", "jar", "figure", "panel", "fragment", "relief", "untitled", "basket", "shield", "chair", "stove"}
    assert not [o["name"] for o in MET if o["name"].strip().lower() in bare]
    assert len({o["name"] for o in MET}) == len(MET)  # titles shared by several works are told apart


def test_met_catalogue_includes_famous_works():
    names = " ".join(o["name"] for o in MET)
    for famous in ("Wheat Field with Cypresses", "Madame X", "The Temple of Dendur", "The Death of Socrates", "The Harvesters"):
        assert famous in names, famous


def test_the_museum_api_serves_the_new_galleries_with_local_picture_overlay():
    from fastapi.testclient import TestClient
    from app.main import app
    c = TestClient(app)
    overview = c.get("/api/museum").json()
    assert overview["total_objects"] == len(OBJECTS)
    ids = {g["id"] for g in overview["galleries"]}
    assert {"met_european_paintings", "met_egyptian_art", "met_islamic_art"} <= ids
    body = c.get("/api/museum/met_egyptian_art").json()
    assert body["objects"] and all(o["id"].startswith("met_") for o in body["objects"])


def _cleaner():
    import importlib.util
    spec = importlib.util.spec_from_file_location("museum_cleaner", BASE / "scripts" / "remove_duplicate_and_generic_museum_objects.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_no_duplicate_or_generic_objects_remain():
    cleaner = _cleaner()
    assert [o["name"] for _, o in OBJECTS if cleaner.is_generic(o)] == []
    assert [(g, o["name"], k[1]["name"]) for g, o, k in cleaner.find_duplicates(OBJECTS)] == []
    assert not [o["name"] for _, o in OBJECTS if cleaner.PACIFIC_CARD.match(o["name"])]


def test_the_cleaner_recognises_generic_names_and_keeps_specific_ones():
    c = _cleaner()
    for name in ("Teapot", "Untitled", "Tea Table", "Covered Vase (one of a pair)", "Seated Figure", "Pacific Fiji Tool", "Medieval Astrolabe"):
        assert c.is_generic({"id": "met_1" if "Pacific" not in name else "x", "name": name}), name
    for name in ("The Large Tree", "Wheat Field with Cypresses", "Nathaniel Hurd", "Standing Figure of Amun-Re"):
        assert not c.is_generic({"id": "met_1", "name": name}), name
    assert not c.is_generic({"id": "fm_1", "name": "Teapot", "wiki_title": "Teapot"})  # a curated article-backed object is never judged by its name


def test_the_cleaner_merges_the_same_thing_but_not_different_objects_sharing_an_article():
    c = _cleaner()
    e = lambda g, i, name, wiki="", **kw: (g, {"id": i, "name": name, "wiki_title": wiki, "description": "x" * 50, **kw})
    entries = [
        e("a", "1", "Great Sphinx of Giza", "Great Sphinx of Giza"), e("b", "2", "The Great Sphinx of Giza", "Great Sphinx of Giza", quiz={"q": 1}),
        e("a", "3", "Stradivarius Violin", "Stradivarius"), e("b", "4", "The Stradivari Guitar 'Sabionari'", "Stradivarius"),
        e("a", "5", "Pyramids of Meroe", "Nubian pyramids"), e("b", "6", "Great Pyramid of Meroë", "Nubian pyramids"),
        e("m", "7", "清 石濤 十六羅漢圖, The Sixteen Luohans"), e("m", "8", "明 吳彬 十六羅漢圖, The Sixteen Luohans"),
        e("m", "9", "Chest of drawers"), e("m", "10", "Chest of Drawers"),
        e("i", "11", "Persian Astrolabe Rete", "Astrolabe"), e("i", "12", "Astrolabe of Ibn al-Sarraj", "Astrolabe"),
    ]
    removed = {o["id"]: k[1]["id"] for _, o, k in c.find_duplicates(entries)}
    assert not ({"3", "4", "7", "8", "11", "12"} & set(removed))  # different objects survive
    assert removed["2"] == "1"  # the entry whose title is the article's title is kept
    assert len({"5", "6"} & set(removed)) == 1 and len({"9", "10"} & set(removed)) == 1  # Meroe/Meroë and case-only variants merge


def test_the_cleaner_is_idempotent():
    c = _cleaner()
    data = json.loads(json.dumps(MUSEUM))
    report = c.clean(data)
    assert report == {"generic": [], "duplicates": []}
