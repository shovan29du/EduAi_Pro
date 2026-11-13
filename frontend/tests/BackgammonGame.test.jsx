import React from 'react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import BackgammonGame from '../src/components/BackgammonGame.jsx';

afterEach(() => vi.restoreAllMocks());

describe('BackgammonGame', () => {
  it('starts with the standard 2/5/3/5 checker split for both sides', () => {
    render(<BackgammonGame />);
    expect(screen.getByText('🎯 Backgammon')).toBeInTheDocument();
    expect(screen.getByText(/You — off: 0, bar: 0/)).toBeInTheDocument();
    expect(screen.getByText(/Computer — off: 0, bar: 0/)).toBeInTheDocument();
  });

  it('rolls dice, moves a checker from the 24-point, and consumes one die', () => {
    const { container } = render(<BackgammonGame />);
    // Fixed roll of 1 and 4. A random roll made this test fail about 1 run in
    // 36: a double five is blocked from the 24-point (it lands on the
    // opponent's 6-point, which holds five checkers).
    vi.spyOn(Math, 'random').mockReturnValueOnce(0).mockReturnValueOnce(0.5);
    fireEvent.click(screen.getByRole('button', { name: /Roll Dice/ }));
    vi.restoreAllMocks();

    const dieChipsBefore = container.querySelectorAll('.w-9.h-9.rounded.bg-white');
    expect(dieChipsBefore.length).toBeGreaterThanOrEqual(2);

    // The top-left point (index 23, the player's 24-point) has a legal move
    // for this roll, since the points 1 and 4 steps ahead of it are empty.
    const topRow = container.querySelectorAll('.grid.grid-cols-12')[0];
    const point23Cell = topRow.querySelectorAll('button')[0];
    fireEvent.click(point23Cell);

    const destination = container.querySelector('.ring-emerald-300');
    expect(destination).toBeTruthy();
    fireEvent.click(destination);

    const dieChipsAfter = container.querySelectorAll('.w-9.h-9.rounded.bg-white');
    expect(dieChipsAfter.length).toBe(dieChipsBefore.length - 1);
  });
});
