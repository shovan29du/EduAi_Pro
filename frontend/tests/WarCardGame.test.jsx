import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import WarCardGame from '../src/components/WarCardGame.jsx';

describe('WarCardGame', () => {
  it('deals 26 cards to each side and lets the player flip a round', () => {
    render(<WarCardGame />);
    expect(screen.getByText('🃏 War')).toBeInTheDocument();
    expect(screen.getByText('You — 26 cards')).toBeInTheDocument();
    expect(screen.getByText('Computer — 26 cards')).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: /Flip Cards|Battle! ⚔️/ }));
    // After one round the table shows two cards and the pile counts changed.
    expect(screen.queryByText('Flip a card to battle the computer.')).not.toBeInTheDocument();
  });

  it('plays through to completion and reports a win/loss score', () => {
    const onComplete = vi.fn();
    render(<WarCardGame onComplete={onComplete} />);
    for (let i = 0; i < 400; i++) {
      const btn = screen.queryByRole('button', { name: /Flip Cards|Battle! ⚔️|Play Again/ });
      if (!btn || btn.textContent.includes('Play Again')) break;
      fireEvent.click(btn);
    }
    expect(onComplete).toHaveBeenCalled();
    const result = onComplete.mock.calls[onComplete.mock.calls.length - 1][0];
    expect(result.maxScore).toBe(1);
    expect([0, 1]).toContain(result.score);
    expect(screen.getByRole('button', { name: 'Play Again' })).toBeInTheDocument();
  });
});
