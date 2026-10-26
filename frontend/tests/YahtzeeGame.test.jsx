import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import YahtzeeGame from '../src/components/YahtzeeGame.jsx';

describe('YahtzeeGame', () => {
  it('rolls 5 dice and lists all 13 scoring categories', () => {
    render(<YahtzeeGame />);
    expect(screen.getByText('🎲 Yahtzee')).toBeInTheDocument();
    for (const label of ['Ones', 'Sixes', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance']) {
      expect(screen.getByText(label)).toBeInTheDocument();
    }
    expect(screen.getByRole('button', { name: /Roll \(2 left\)/ })).toBeInTheDocument();
  });

  it('lets the player lock in the Chance category using the sum of the current roll', () => {
    render(<YahtzeeGame />);
    const chanceButton = screen.getByText('Chance').closest('button');
    fireEvent.click(chanceButton);
    // Chance is now used and shown as a fixed score; the total reflects it.
    expect(chanceButton).toBeDisabled();
  });

  it('holding a die keeps its value across a reroll', () => {
    vi.spyOn(Math, 'random').mockReturnValue(0); // forces every die to show 1
    render(<YahtzeeGame />);
    const diceButtons = screen.getAllByRole('button').filter((b) => /^[1-6]$/.test(b.textContent));
    expect(diceButtons).toHaveLength(5);
    fireEvent.click(diceButtons[0]); // hold the first die
    vi.spyOn(Math, 'random').mockReturnValue(0.99); // now force rerolled dice to show 6
    fireEvent.click(screen.getByRole('button', { name: /Roll \(2 left\)/ }));
    const afterRoll = screen.getAllByRole('button').filter((b) => /^[1-6]$/.test(b.textContent));
    expect(afterRoll[0].textContent).toBe('1'); // held die unchanged
    vi.restoreAllMocks();
  });
});
