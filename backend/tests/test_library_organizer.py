from pathlib import Path

import pytest

from app import library_organizer


@pytest.mark.parametrize("author,expected", [
    ("Jane Austen", "J"),
    ("mark twain", "M"),
    ("  Émile Zola", "#"),  # non-ASCII first letter falls back to catch-all
    ("3lliot Books", "#"),
    ("", "#"),
    ("Unknown", "U"),
])
def test_author_initial(author, expected):
    assert library_organizer.author_initial(author) == expected


def test_move_literature_files_into_az_author_folder(tmp_path):
    root = tmp_path
    book = root / "pride.txt"
    book.write_text("It is a truth universally acknowledged...")

    destination = library_organizer.move_literature(root, book, "Jane Austen")

    assert destination.exists()
    assert not book.exists()
    assert destination.parent.name == "Jane Austen"
    assert destination.parent.parent.name == "J"
    assert destination.parent.parent.parent.name == library_organizer.LIBRARY_DIRNAME
    assert destination.name == "pride.txt"


def test_move_textbook_files_into_reference_subject_folder(tmp_path):
    root = tmp_path
    book = root / "algebra.pdf"
    book.write_text("chapter 1")

    destination = library_organizer.move_textbook(root, book, "Mathematics")

    assert destination.exists()
    assert not book.exists()
    assert destination.parent.name == "Mathematics"
    assert destination.parent.parent.name == library_organizer.REFERENCE_DIRNAME
    assert destination.parent.parent.parent.name == library_organizer.LIBRARY_DIRNAME


def test_move_handles_filename_collisions(tmp_path):
    root = tmp_path
    first = root / "book.txt"
    first.write_text("first copy")
    second = root / "subdir" / "book.txt"
    second.parent.mkdir()
    second.write_text("second copy, different content")

    dest1 = library_organizer.move_literature(root, first, "Author One")
    dest2 = library_organizer.move_literature(root, second, "Author One")

    assert dest1 != dest2
    assert dest1.exists() and dest2.exists()
    assert dest1.read_text() == "first copy"
    assert dest2.read_text() == "second copy, different content"


def test_unsafe_author_name_characters_are_stripped(tmp_path):
    root = tmp_path
    book = root / "weird.txt"
    book.write_text("content")

    destination = library_organizer.move_literature(root, book, 'Weird: <Author>/Name?')

    assert destination.exists()
    # No path-invalid characters leak into the created folder name.
    assert not any(ch in destination.parent.name for ch in '<>:"/\\|?*')
