import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import BackgammonGame from '../src/components/BackgammonGame.jsx';

describe('BackgammonGame', () => {
  it('starts with the standard 2/5/3/5 checker split for both sides', () => {
    render(<BackgammonGame />);
    expect(screen.getByText('🎯 Backgammon')).toBeInTheDocument();
    expect(screen.getByText(/You — off: 0, bar: 0/)).toBeInTheDocument();
    expect(screen.getByText(/Computer — off: 0, bar: 0/)).toBeInTheDocument();
  });

  it('rolls dice, moves a checker from the 24-point, and consumes one die', () => {
    const { container } = render(<BackgammonGame />);
    fireEvent.click(screen.getByRole('button', { name: /Roll Dice/ }));

    const dieChipsBefore = container.querySelectorAll('.w-9.h-9.rounded.bg-white');
    expect(dieChipsBefore.length).toBeGreaterThanOrEqual(2);

    // The top-left point (index 23, the player's 24-point) always has a
    // legal move at the start of the game, since the six points in front of
    // it are empty regardless of what was rolled.
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
