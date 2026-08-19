import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import RummyGame from '../src/components/RummyGame.jsx';

describe('RummyGame', () => {
  it('deals a 10-card hand and shows a starting discard', () => {
    const { container } = render(<RummyGame />);
    expect(screen.getByText('🃏 Rummy')).toBeInTheDocument();
    const handSection = screen.getByText(/Your Hand — deadwood:/).closest('div').parentElement;
    expect(handSection.querySelectorAll('button.w-12.h-16')).toHaveLength(10);
  });

  it('lets the player draw from the stock, then discard to pass the turn', () => {
    render(<RummyGame />);
    fireEvent.click(screen.getByText('🂠'));
    expect(screen.getByText('Discard a card to end your turn.')).toBeInTheDocument();

    const handButtons = screen.getAllByRole('button').filter((b) => !b.disabled && /^[0-9AJQK]/.test(b.textContent));
    expect(handButtons.length).toBe(11);
    fireEvent.click(handButtons[0]);
    // Turn has passed to the computer.
    expect(screen.queryByText('Discard a card to end your turn.')).not.toBeInTheDocument();
  });
});
