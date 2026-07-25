import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, within, waitFor } from '@testing-library/react';
import Games from '../src/components/Games.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';
import { TOTAL_GAMES, CATEGORIES, GAMES, dailyChallenge } from '../src/data/gameCentreData.js';

// Minimal in-memory fake for /api/users and /api/progress/{child} so the
// Game Centre's persistence, and the cross-sibling leaderboard, can be
// exercised without a real backend.
function createFetchMock({ users, progressByChild = {} } = {}) {
  const store = JSON.parse(JSON.stringify(progressByChild));
  return vi.fn((url, options = {}) => {
    if (url === '/api/users') {
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ users: users || [{ name: 'Parent', role: 'parent' }] }),
      });
    }
    const match = String(url).match(/^\/api\/progress\/(.+)$/);
    if (match) {
      const child = decodeURIComponent(match[1]);
      if (options.method === 'POST') {
        const update = JSON.parse(options.body);
        const current = store[child] || {};
        if (update.mastery) current.mastery = { ...(current.mastery || {}), ...update.mastery };
        store[child] = current;
        return Promise.resolve({ ok: true, json: () => Promise.resolve(current) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve(store[child] || {}) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

async function renderGames(fetchOptions) {
  global.fetch = createFetchMock(fetchOptions);
  const utils = render(
    <ChildProvider>
      <Games grade={null} />
    </ChildProvider>
  );
  // Let the initial progress fetch (used for badges/streak) settle before interacting.
  await waitFor(() => expect(global.fetch).toHaveBeenCalled());
  return utils;
}

beforeEach(() => {
  localStorage.clear();
});

describe('Games (Game Centre)', () => {
  it('has at least 50 games defined across its categories', () => {
    expect(TOTAL_GAMES).toBeGreaterThanOrEqual(50);
  });

  it('renders the category picker and shows the total game count', async () => {
    await renderGames();
    expect(screen.getByText('🎮 Game Centre')).toBeInTheDocument();
    expect(screen.getByText(new RegExp(`${TOTAL_GAMES} games across ${CATEGORIES.length} categories`))).toBeInTheDocument();
    // Every category shows up as a picker card.
    for (const cat of CATEGORIES) {
      expect(screen.getByText(cat.label)).toBeInTheDocument();
    }
    await waitFor(() => expect(global.fetch).toHaveBeenCalled());
  });

  it('drills into a category to show its games, then into a game to play it', async () => {
    await renderGames();
    fireEvent.click(screen.getByText('Memory Match'));
    expect(screen.getByText('← All Categories')).toBeInTheDocument();
    expect(screen.getByText('Animal Friends')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Animal Friends'));
    expect(screen.getByText(/Back to Memory Match/)).toBeInTheDocument();
    expect(screen.getAllByRole('button', { name: '❓' }).length).toBeGreaterThan(0);
  });

  it('can still play the existing Phonics Match and Quiz Sprint games', async () => {
    await renderGames();
    fireEvent.click(screen.getByText('Classic Word Games'));
    fireEvent.click(screen.getByText('Phonics Match'));
    expect(screen.getByText('Phonics Match')).toBeInTheDocument();
    expect(screen.getAllByRole('button').length).toBeGreaterThanOrEqual(3);
  });

  it('shows the Daily Challenge banner and can jump straight into playing it', async () => {
    await renderGames();
    const daily = dailyChallenge();
    expect(screen.getByText('⭐ Daily Challenge')).toBeInTheDocument();
    expect(screen.getByText(/-day streak/)).toBeInTheDocument();
    expect(screen.getByText(daily.game.title)).toBeInTheDocument();

    fireEvent.click(screen.getByText('Play Daily Challenge'));
    expect(screen.getByText(/Today's Daily Challenge/)).toBeInTheDocument();
  });

  it('lets a difficulty change resize the Memory Match board', async () => {
    await renderGames();
    fireEvent.click(screen.getByText('Memory Match'));
    fireEvent.click(screen.getByText('Animal Friends'));

    // Default difficulty is Medium -> 5 pairs -> 10 cards.
    expect(screen.getAllByRole('button', { name: '❓' })).toHaveLength(10);

    fireEvent.click(screen.getByRole('button', { name: 'Easy' }));
    expect(screen.getAllByRole('button', { name: '❓' })).toHaveLength(6);

    fireEvent.click(screen.getByRole('button', { name: 'Hard' }));
    expect(screen.getAllByRole('button', { name: '❓' })).toHaveLength(12);
  });

  it('lets a difficulty change shorten the Math Sprint round', async () => {
    await renderGames();
    fireEvent.click(screen.getByText('Math Sprint'));
    fireEvent.click(screen.getByText('Addition Sprint'));

    fireEvent.click(screen.getByRole('button', { name: 'Hard' }));
    fireEvent.click(screen.getByRole('button', { name: 'Start' }));
    expect(screen.getByText(/Time left:/).textContent).toContain('20s');
  });

  it('lets a difficulty change vary how many Sudoku cells start filled in', async () => {
    await renderGames();
    fireEvent.click(screen.getByText('Sudoku Lite'));
    fireEvent.click(screen.getByText('4x4 Sudoku — Easy'));

    function fixedCellCount() {
      return screen.getAllByLabelText(/Row \d+ column \d+/).filter((btn) => btn.disabled).length;
    }

    // Medium is the default: 16 cells, 45% blanked -> 9 stay fixed.
    expect(fixedCellCount()).toBe(9);

    fireEvent.click(screen.getByRole('button', { name: 'Easy' }));
    expect(fixedCellCount()).toBe(11);

    fireEvent.click(screen.getByRole('button', { name: 'Hard' }));
    expect(fixedCellCount()).toBe(6);
  });

  it('persists a completed game score to the progress API and shows a Best badge afterwards', async () => {
    await renderGames();
    fireEvent.click(screen.getByText('Sudoku Lite'));
    fireEvent.click(screen.getByText('4x4 Sudoku — Easy'));

    const sudokuGame = GAMES.find((g) => g.id === 'sudoku-4x4-easy');
    const { solution } = sudokuGame.data;
    for (let r = 0; r < solution.length; r++) {
      for (let c = 0; c < solution[r].length; c++) {
        const cell = screen.getByLabelText(`Row ${r + 1} column ${c + 1}`);
        if (cell.disabled) continue;
        fireEvent.click(cell);
        fireEvent.click(screen.getByRole('button', { name: String(solution[r][c]) }));
      }
    }
    fireEvent.click(screen.getByRole('button', { name: 'Check solution' }));
    expect(screen.getByText('Correct — solved! 🎉')).toBeInTheDocument();

    await waitFor(() =>
      expect(global.fetch).toHaveBeenCalledWith(
        '/api/progress/Parent',
        expect.objectContaining({
          method: 'POST',
          body: expect.stringContaining('game:sudoku-4x4-easy'),
        })
      )
    );

    fireEvent.click(screen.getByText(/Back to Sudoku Lite/));
    await waitFor(() => expect(screen.getByText(/Best: 1\/1/)).toBeInTheDocument());
    expect(screen.getByText(/Played 1×/)).toBeInTheDocument();
  });

  it('opens a cross-sibling leaderboard comparing best scores for the current game', async () => {
    await renderGames({
      users: [
        { name: 'Parent', role: 'parent' },
        { name: 'Shovan', role: 'parent' },
      ],
      progressByChild: {
        Parent: { mastery: { 'game:math-addition': { best: 5, bestMaxScore: 8, plays: 2 } } },
        Shovan: { mastery: { 'game:math-addition': { best: 9, bestMaxScore: 10, plays: 3 } } },
      },
    });
    fireEvent.click(screen.getByText('Math Sprint'));
    fireEvent.click(screen.getByText('Addition Sprint'));
    fireEvent.click(screen.getByText('🏆 Leaderboard'));

    const dialog = await screen.findByRole('dialog', { name: /Addition Sprint leaderboard/i });
    await waitFor(() => expect(within(dialog).getByText(/Shovan/)).toBeInTheDocument());
    const rows = within(dialog).getAllByRole('listitem');
    expect(rows[0]).toHaveTextContent('Shovan');
    expect(rows[0]).toHaveTextContent('9/10');
    expect(rows[1]).toHaveTextContent('Parent');
    expect(rows[1]).toHaveTextContent('5/8');
  });
});
