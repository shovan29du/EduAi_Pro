import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import LudoGame from '../src/components/LudoGame.jsx';

describe('LudoGame', () => {
  it('renders all four colours with 0/4 home and a Roll button', () => {
    render(<LudoGame />);
    expect(screen.getByText('🎲 Ludo')).toBeInTheDocument();
    for (const label of ['You', 'Green', 'Yellow', 'Blue']) {
      expect(screen.getByText(new RegExp(label))).toBeInTheDocument();
    }
    expect(screen.getAllByText('0/4 home')).toHaveLength(4);
    expect(screen.getByRole('button', { name: /🎲 Roll/ })).toBeInTheDocument();
  });

  it('rolling a 6 lets the player move a token out of the yard', () => {
    const randomSpy = vi.spyOn(Math, 'random').mockReturnValue(0.99);
    try {
      render(<LudoGame />);
      fireEvent.click(screen.getByRole('button', { name: /🎲 Roll/ }));
      expect(screen.getByRole('button', { name: /🎲 6/ })).toBeInTheDocument();

      const tokenButtons = screen.getAllByRole('button', { name: /Token \d \(Yard\)/ });
      expect(tokenButtons.length).toBeGreaterThan(0);
      fireEvent.click(tokenButtons[0]);
      // Moving a token off a 6 resets the die and prompts another roll.
      expect(screen.getByText('You rolled a 6 — roll again!')).toBeInTheDocument();
      expect(screen.getByRole('button', { name: /🎲 Roll/ })).toBeInTheDocument();
    } finally {
      randomSpy.mockRestore();
    }
  });
});
