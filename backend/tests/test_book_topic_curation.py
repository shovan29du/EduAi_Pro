import json
import os

import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.curate import curate_book_topics
from app.main import app, SYLLABUS_DIR

client = TestClient(app)


def test_parse_book_lesson_snippets_matches_valid_titles():
    raw = (
        "LESSON: Photosynthesis\n"
        "KIND: example\n"
        "FORM: summary\n"
        "CONTENT: Leaves capture sunlight and convert it into energy.\n"
        "---\n"
        "LESSON: The Water Cycle\n"
        "KIND: figure\n"
        "FORM: full\n"
        "CONTENT: Figure 2 shows evaporation, condensation, and precipitation in a loop."
    )
    result = ai_tutor._parse_book_lesson_snippets(raw, ["Photosynthesis", "The Water Cycle"])
    assert result == [
        {"lesson_title": "Photosynthesis", "kind": "example", "form": "summary",
         "content": "Leaves capture sunlight and convert it into energy."},
        {"lesson_title": "The Water Cycle", "kind": "figure", "form": "full",
         "content": "Figure 2 shows evaporation, condensation, and precipitation in a loop."},
    ]


def test_parse_book_lesson_snippets_ignores_unknown_lesson_titles():
    raw = "LESSON: Not A Real Lesson\nKIND: copy\nFORM: full\nCONTENT: irrelevant"
    assert ai_tutor._parse_book_lesson_snippets(raw, ["Photosynthesis"]) == []


def test_parse_book_lesson_snippets_falls_back_to_defaults_for_bad_kind_and_form():
    raw = "LESSON: Photosynthesis\nKIND: nonsense\nFORM: nonsense\nCONTENT: Some extracted text."
    result = ai_tutor._parse_book_lesson_snippets(raw, ["Photosynthesis"])
    assert result == [{"lesson_title": "Photosynthesis", "kind": "copy", "form": "summary", "content": "Some extracted text."}]


def test_parse_book_lesson_snippets_none_response_yields_nothing():
    assert ai_tutor._parse_book_lesson_snippets("NONE", ["Photosynthesis"]) == []


def test_parse_book_lesson_snippets_recognizes_table_concept_map_and_graph_kinds():
    raw = (
        "LESSON: Photosynthesis\n"
        "KIND: table\n"
        "FORM: full\n"
        "CONTENT: | Stage | Product |\n|---|---|\n| Light reaction | ATP, NADPH |\n"
        "---\n"
        "LESSON: The Water Cycle\n"
        "KIND: concept_map\n"
        "FORM: full\n"
        "CONTENT: Evaporation -> Condensation -> Precipitation -> Collection\n"
        "---\n"
        "LESSON: Photosynthesis\n"
        "KIND: graph\n"
        "FORM: summary\n"
        "CONTENT: Figure 3 plots leaf growth rate against sunlight exposure over 10 days."
    )
    result = ai_tutor._parse_book_lesson_snippets(raw, ["Photosynthesis", "The Water Cycle"])
    kinds = [snippet["kind"] for snippet in result]
    assert kinds == ["table", "concept_map", "graph"]


def test_analyse_book_for_lessons_returns_empty_without_lessons_or_text():
    assert ai_tutor.analyse_book_for_lessons("Book", "some text", []) == []
    assert ai_tutor.analyse_book_for_lessons("Book", "", ["Photosynthesis"]) == []


def test_analyse_book_for_lessons_falls_back_gracefully_when_offline():
    # No ANTHROPIC_API_KEY is set in this sandbox, so _call returns the
    # "Ark AI is offline" fallback text, which shouldn't match the block format.
    result = ai_tutor.analyse_book_for_lessons("Botany Basics", "Plants use sunlight.", ["Photosynthesis"])
    assert result == []


@pytest.fixture
def temp_grade_path():
    # "11" isn't a real school grade (only 1-10 exist), so syllabus_filename
    # resolves it to a level_11.json test-only file, never a real content file.
    path = SYLLABUS_DIR / "level_11.json"
    yield path
    if path.exists():
        os.remove(path)


def _seed_subject_with_lessons(path, lessons):
    data = {
        "standard": 11,
        "subjects": {
            "Science": {
                "books": [], "video_resources": [], "text_resources": [], "cartoon_videos": [],
                "infographics": [], "textbooks": [], "audio_resources": [], "comics": [],
                "drawing_activities": [], "info_cards": [], "podcasts": [], "news_resources": [],
                "quiz_bank": [], "exam": {"questions": [], "passing_score": 60},
                "lessons": lessons,
            }
        },
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def test_curate_book_topics_links_matching_lessons(temp_grade_path, monkeypatch):
    _seed_subject_with_lessons(temp_grade_path, [
        {"id": "sci-l1", "title": "Photosynthesis"},
        {"id": "sci-l2", "title": "The Water Cycle"},
    ])

    def fake_analyse(book_title, book_text, lesson_titles):
        assert set(lesson_titles) == {"Photosynthesis", "The Water Cycle"}
        return [{"lesson_title": "Photosynthesis", "kind": "example", "form": "summary",
                  "content": "Leaves capture sunlight."}]

    monkeypatch.setattr(ai_tutor, "analyse_book_for_lessons", fake_analyse)
    linked = curate_book_topics(11, "Science", "Botany Basics", "Some long book text about photosynthesis.")
    assert linked == ["Photosynthesis"]

    with open(temp_grade_path, encoding="utf-8") as f:
        data = json.load(f)
    lessons = data["subjects"]["Science"]["lessons"]
    photo = next(l for l in lessons if l["title"] == "Photosynthesis")
    assert photo["book_excerpts"] == [
        {"book": "Botany Basics", "kind": "example", "form": "summary", "content": "Leaves capture sunlight."}
    ]
    assert photo["textbook_references"] == [{"title": "Botany Basics", "source": "Parent-uploaded book"}]
    water = next(l for l in lessons if l["title"] == "The Water Cycle")
    assert "book_excerpts" not in water


def test_curate_book_topics_returns_empty_when_lessons_missing(temp_grade_path, monkeypatch):
    _seed_subject_with_lessons(temp_grade_path, [])
    called = []
    monkeypatch.setattr(ai_tutor, "analyse_book_for_lessons", lambda *a, **k: called.append(1))
    assert curate_book_topics(11, "Science", "Some Book", "text") == []
    assert called == []


def test_curate_book_topics_returns_empty_when_subject_missing(temp_grade_path):
    with open(temp_grade_path, "w", encoding="utf-8") as f:
        json.dump({"standard": 11, "subjects": {}}, f)
    assert curate_book_topics(11, "Nonexistent", "Some Book", "text") == []


def test_curate_book_topics_ignores_snippets_for_unknown_lesson_titles(temp_grade_path, monkeypatch):
    _seed_subject_with_lessons(temp_grade_path, [{"id": "sci-l1", "title": "Photosynthesis"}])
    monkeypatch.setattr(
        ai_tutor, "analyse_book_for_lessons",
        lambda *a, **k: [{"lesson_title": "A Lesson That Does Not Exist", "kind": "copy", "form": "full", "content": "x"}],
    )
    assert curate_book_topics(11, "Science", "Book", "text") == []


def test_upload_safe_book_links_topics_end_to_end(temp_grade_path, monkeypatch):
    _seed_subject_with_lessons(temp_grade_path, [{"id": "sci-l1", "title": "Photosynthesis"}])
    monkeypatch.setattr(
        ai_tutor, "analyse_book_for_lessons",
        lambda *a, **k: [{"lesson_title": "Photosynthesis", "kind": "copy", "form": "summary", "content": "Plants make food from light."}],
    )
    long_text = " ".join(
        f"Sentence number {i} talks about whales and the ocean and migration patterns."
        for i in range(20)
    )
    resp = client.post(
        "/api/upload-safe-book",
        files={"file": ("whales.txt", long_text.encode(), "text/plain")},
        data={"standard": "11", "subject": "Science"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["topics_linked"] == ["Photosynthesis"]


@pytest.fixture
def temp_college_path():
    path = SYLLABUS_DIR / "level_c1.json"
    existed = path.exists()
    original = path.read_bytes() if existed else None
    yield path
    if existed:
        path.write_bytes(original)
    elif path.exists():
        os.remove(path)


def test_curate_book_topics_works_for_a_non_numeric_level_code(temp_college_path, monkeypatch):
    _seed_subject_with_lessons(temp_college_path, [
        {"id": "cs-l1", "title": "Neural Networks"},
    ])

    def fake_analyse(book_title, book_text, lesson_titles):
        assert lesson_titles == ["Neural Networks"]
        return [{"lesson_title": "Neural Networks", "kind": "formula", "form": "full",
                  "content": "y = Wx + b"}]

    monkeypatch.setattr(ai_tutor, "analyse_book_for_lessons", fake_analyse)
    linked = curate_book_topics("C1", "Science", "Deep Learning 101", "Some long book text about neural nets.")
    assert linked == ["Neural Networks"]

    with open(temp_college_path, encoding="utf-8") as f:
        data = json.load(f)
    lesson = data["subjects"]["Science"]["lessons"][0]
    assert lesson["book_excerpts"] == [
        {"book": "Deep Learning 101", "kind": "formula", "form": "full", "content": "y = Wx + b"}
    ]


def test_curate_book_topics_accepts_a_custom_source_label(temp_grade_path, monkeypatch):
    _seed_subject_with_lessons(temp_grade_path, [{"id": "sci-l1", "title": "Photosynthesis"}])
    monkeypatch.setattr(
        ai_tutor, "analyse_book_for_lessons",
        lambda *a, **k: [{"lesson_title": "Photosynthesis", "kind": "copy", "form": "summary", "content": "x"}],
    )
    curate_book_topics(11, "Science", "Botany Basics", "text", source="Scanned local library book")
    with open(temp_grade_path, encoding="utf-8") as f:
        data = json.load(f)
    lesson = data["subjects"]["Science"]["lessons"][0]
    assert lesson["textbook_references"] == [{"title": "Botany Basics", "source": "Scanned local library book"}]
