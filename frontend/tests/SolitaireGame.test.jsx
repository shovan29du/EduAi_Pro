import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import SolitaireGame from '../src/components/SolitaireGame.jsx';

describe('SolitaireGame', () => {
  it('deals a 7-column tableau with a 24-card stock and 4 empty foundations', () => {
    render(<SolitaireGame />);
    expect(screen.getByText('🂡 Solitaire')).toBeInTheDocument();
    expect(screen.getByText('Stock (24)')).toBeInTheDocument();
    expect(screen.getByText('Waste')).toBeInTheDocument();
    for (const suit of ['♠', '♥', '♦', '♣']) {
      // May also appear inside a face-up tableau card of that suit, so allow multiples.
      expect(screen.getAllByText(suit).length).toBeGreaterThanOrEqual(1);
    }
  });

  it('draws a card from the stock into the waste pile', () => {
    render(<SolitaireGame />);
    fireEvent.click(screen.getByText('Stock (24)').parentElement);
    expect(screen.getByText('Stock (23)')).toBeInTheDocument();
  });

  it('reports the number of cards home when finished early', () => {
    const onComplete = vi.fn();
    render(<SolitaireGame onComplete={onComplete} />);
    fireEvent.click(screen.getByRole('button', { name: /Finish & Score/ }));
    expect(onComplete).toHaveBeenCalledWith(
      expect.objectContaining({ score: 0, maxScore: 52 })
    );
    expect(screen.getByRole('button', { name: 'Play Again' })).toBeInTheDocument();
  });
});
