import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import BlackjackGame from '../src/components/BlackjackGame.jsx';

describe('BlackjackGame', () => {
  it('deals two cards each to player and dealer, with one dealer card hidden', () => {
    render(<BlackjackGame />);
    expect(screen.getByText('🂡 Blackjack')).toBeInTheDocument();
    expect(screen.getByText('🂠')).toBeInTheDocument(); // dealer's hole card
    expect(screen.getByRole('button', { name: 'Hit' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Stand' })).toBeInTheDocument();
  });

  it('reveals the dealer hand and settles the round when the player stands', () => {
    render(<BlackjackGame />);
    fireEvent.click(screen.getByRole('button', { name: 'Stand' }));
    // The hole card is no longer hidden once the dealer plays out the hand.
    expect(screen.queryByText('🂠')).not.toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Next Hand' })).toBeInTheDocument();
    expect(screen.getByText(/Session: \d+W · \d+L · \d+P/)).toBeInTheDocument();
  });
});
