import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import TicTacToeGame from '../src/components/TicTacToeGame.jsx';

describe('TicTacToeGame', () => {
  it('renders an empty 3x3 board', () => {
    render(<TicTacToeGame />);
    expect(screen.getByText('⭕ Tic-Tac-Toe')).toBeInTheDocument();
    expect(screen.getAllByRole('button')).toHaveLength(9);
  });

  it('lets the player place an X and the computer replies with an O', () => {
    vi.useFakeTimers();
    render(<TicTacToeGame />);
    const cells = screen.getAllByRole('button');
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe('X');
    act(() => {
      vi.runAllTimers();
    });
    const oCount = cells.filter((c) => c.textContent === 'O').length;
    expect(oCount).toBe(1);
    vi.useRealTimers();
  });

  it('never lets the player beat a perfect-play computer', () => {
    vi.useFakeTimers();
    const onComplete = vi.fn();
    render(<TicTacToeGame onComplete={onComplete} />);
    // Play the same square repeatedly to force a quick finish against perfect play.
    for (let i = 0; i < 9 && onComplete.mock.calls.length === 0; i++) {
      const cells = screen.getAllByRole('button');
      const empty = cells.find((c) => !c.disabled && c.textContent === '');
      if (!empty) break;
      fireEvent.click(empty);
      act(() => {
        vi.runAllTimers();
      });
    }
    expect(onComplete).toHaveBeenCalled();
    const result = onComplete.mock.calls[0][0];
    expect(result.score).not.toBe(1); // random play can't beat perfect play
    vi.useRealTimers();
  });
});
