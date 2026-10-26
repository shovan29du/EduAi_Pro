import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ChessTutor from '../src/components/ChessTutor.jsx';

const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
const AFTER_E4_FEN = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1';

const startState = {
  fen: START_FEN,
  turn: 'white',
  legal_moves: ['e2e4', 'e2e3', 'd2d4', 'g1f3'],
  last_move_uci: null,
  last_move_san: null,
  status: 'in_progress',
  winner: null,
};

const afterE4State = {
  fen: AFTER_E4_FEN,
  turn: 'black',
  legal_moves: ['e7e5', 'e7e6'],
  last_move_uci: 'e2e4',
  last_move_san: 'e4',
  status: 'in_progress',
  winner: null,
};

function mockFetch() {
  return vi.fn((url, options = {}) => {
    const u = String(url);
    const body = options.body ? JSON.parse(options.body) : {};
    if (u === '/api/chess/new-game') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(startState) });
    }
    if (u === '/api/chess/move' && body.move === 'e2e4') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(afterE4State) });
    }
    if (u === '/api/chess/explain') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ explanation: 'White controls the centre.' }) });
    }
    if (u === '/api/chess/ask') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ answer: 'It opens lines for the bishop and queen.' }) });
    }
    if (u === '/api/chess/review-pgn') {
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({
          positions: [
            { ply: 1, move_number: 1, color: 'white', san: 'e4', fen: AFTER_E4_FEN },
          ],
        }),
      });
    }
    if (u.startsWith('/api/levels')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ levels: [] }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('ChessTutor', () => {
  it('loads a new game on mount', async () => {
    render(<ChessTutor />);
    expect(await screen.findByText('White to move')).toBeInTheDocument();
  });

  it('makes a move by clicking origin then destination square', async () => {
    render(<ChessTutor />);
    await screen.findByText('White to move');

    fireEvent.click(screen.getByLabelText('Square e2, P'));
    fireEvent.click(screen.getByLabelText('Square e4'));

    await waitFor(() => {
      expect(screen.getByText('Black to move')).toBeInTheDocument();
    });
    expect(screen.getByText('e4')).toBeInTheDocument();
  });

  it('explains the current position via the AI coach', async () => {
    render(<ChessTutor />);
    await screen.findByText('White to move');

    fireEvent.click(screen.getByText('Explain this position'));

    expect(await screen.findByText('White controls the centre.')).toBeInTheDocument();
  });

  it('answers a question about the position', async () => {
    render(<ChessTutor />);
    await screen.findByText('White to move');

    fireEvent.change(screen.getByPlaceholderText('Ask about this position…'), {
      target: { value: 'Why play e4?' },
    });
    fireEvent.click(screen.getByText('Ask'));

    expect(await screen.findByText('It opens lines for the bishop and queen.')).toBeInTheDocument();
  });

  it('loads and steps through a PGN game in Game Review mode', async () => {
    render(<ChessTutor />);
    await screen.findByText('White to move');

    fireEvent.click(screen.getByText('📜 Game Review'));
    fireEvent.change(screen.getByPlaceholderText('1. e4 e5 2. Nf3 Nc6 3. Bb5 ...'), {
      target: { value: '1. e4' },
    });
    fireEvent.click(screen.getByText('Load game'));

    expect(await screen.findByText('Start')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Next →'));
    expect(await screen.findByText('Move 1: e4')).toBeInTheDocument();

    fireEvent.click(screen.getByText('← Prev'));
    expect(await screen.findByText('Start')).toBeInTheDocument();
  });
});
