import pytest
from fastapi.testclient import TestClient

from app import ai_tutor
from app.main import app

client = TestClient(app)

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
FOOLS_MATE_PGN = "1. f3 e5 2. g4 Qh4# 0-1"


def test_new_game_returns_starting_position():
    resp = client.post("/api/chess/new-game")
    assert resp.status_code == 200
    data = resp.json()
    assert data["fen"] == START_FEN
    assert data["turn"] == "white"
    assert data["status"] == "in_progress"
    assert len(data["legal_moves"]) == 20


def test_state_rejects_invalid_fen():
    resp = client.post("/api/chess/state", json={"fen": "not-a-fen"})
    assert resp.status_code == 400


def test_state_requires_fen():
    resp = client.post("/api/chess/state", json={})
    assert resp.status_code == 400


def test_move_applies_legal_move():
    resp = client.post("/api/chess/move", json={"fen": START_FEN, "move": "e2e4"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["turn"] == "black"
    assert data["last_move_uci"] == "e2e4"
    assert data["last_move_san"] == "e4"
    assert data["status"] == "in_progress"


def test_move_rejects_illegal_move():
    resp = client.post("/api/chess/move", json={"fen": START_FEN, "move": "e2e5"})
    assert resp.status_code == 400
    assert "Illegal" in resp.json()["detail"]


def test_move_rejects_malformed_move_string():
    resp = client.post("/api/chess/move", json={"fen": START_FEN, "move": "not-a-move"})
    assert resp.status_code == 400


def test_move_rejects_invalid_fen():
    resp = client.post("/api/chess/move", json={"fen": "garbage", "move": "e2e4"})
    assert resp.status_code == 400


def test_move_requires_fen_and_move():
    resp = client.post("/api/chess/move", json={"fen": START_FEN})
    assert resp.status_code == 400


def test_move_detects_checkmate():
    # Position right before Scholar's Mate: 1.e4 e5 2.Bc4 Nc6 3.Qh5 Nf6??
    fen_before_mate = "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4"
    resp = client.post("/api/chess/move", json={"fen": fen_before_mate, "move": "h5f7"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "checkmate"
    assert data["winner"] == "white"
    assert data["last_move_san"] == "Qxf7#"


def test_review_pgn_returns_positions_with_final_checkmate():
    resp = client.post("/api/chess/review-pgn", json={"pgn": FOOLS_MATE_PGN})
    assert resp.status_code == 200
    positions = resp.json()["positions"]
    assert len(positions) == 4
    assert positions[0] == {
        "ply": 1, "move_number": 1, "color": "white", "san": "f3",
        "fen": "rnbqkbnr/pppppppp/8/8/8/5P2/PPPPP1PP/RNBQKBNR b KQkq - 0 1",
    }
    assert positions[-1]["san"] == "Qh4#"


def test_review_pgn_rejects_unparseable_text():
    resp = client.post("/api/chess/review-pgn", json={"pgn": "this is not a pgn"})
    assert resp.status_code == 400


def test_review_pgn_requires_pgn():
    resp = client.post("/api/chess/review-pgn", json={"pgn": ""})
    assert resp.status_code == 400


@pytest.fixture
def mock_ai_chess(monkeypatch):
    monkeypatch.setattr(ai_tutor, "explain_chess_position", lambda *a, **k: "This is an explanation.")
    monkeypatch.setattr(ai_tutor, "answer_chess_question", lambda *a, **k: "This is an answer.")


def test_explain_returns_ai_explanation(mock_ai_chess):
    resp = client.post("/api/chess/explain", json={"fen": START_FEN, "moves": ["e4"], "level": "5"})
    assert resp.status_code == 200
    assert resp.json()["explanation"] == "This is an explanation."


def test_explain_requires_fen():
    resp = client.post("/api/chess/explain", json={})
    assert resp.status_code == 400


def test_ask_returns_ai_answer(mock_ai_chess):
    resp = client.post("/api/chess/ask", json={"fen": START_FEN, "question": "Why?", "level": "5"})
    assert resp.status_code == 200
    assert resp.json()["answer"] == "This is an answer."


def test_ask_requires_question(mock_ai_chess):
    resp = client.post("/api/chess/ask", json={"fen": START_FEN, "question": ""})
    assert resp.status_code == 400


def test_ask_requires_fen():
    resp = client.post("/api/chess/ask", json={"question": "Why?"})
    assert resp.status_code == 400
