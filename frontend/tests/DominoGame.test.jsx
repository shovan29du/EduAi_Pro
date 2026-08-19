import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent, within } from '@testing-library/react';
import DominoGame from '../src/components/DominoGame.jsx';

function handTileButtons(container) {
  const handSection = screen.getByText(/Your Hand/).closest('div');
  return within(handSection).getAllByRole('button');
}

describe('DominoGame', () => {
  it('deals a 7-tile hand and an empty board', () => {
    render(<DominoGame />);
    expect(screen.getByText('🁫 Dominoes')).toBeInTheDocument();
    expect(screen.getByText('No tiles played yet.')).toBeInTheDocument();
    expect(handTileButtons()).toHaveLength(7);
  });

  it('lets the player select and play their first tile to start the board', () => {
    render(<DominoGame />);
    const tiles = handTileButtons();
    fireEvent.click(tiles[0]);
    fireEvent.click(screen.getByRole('button', { name: /Play on Left/ }));

    expect(screen.queryByText('No tiles played yet.')).not.toBeInTheDocument();
    // One tile left the player's hand.
    expect(handTileButtons()).toHaveLength(6);
  });
});
