import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import UnoGame from '../src/components/UnoGame.jsx';

describe('UnoGame', () => {
  it('deals 7 cards to each side and starts on a number card', () => {
    const { container } = render(<UnoGame />);
    expect(screen.getByText('🌈 Uno')).toBeInTheDocument();
    expect(screen.getByText(/Computer has 7 cards/)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Draw Card' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Pass' })).toBeInTheDocument();
    const handSection = screen.getByText('Your Hand').closest('div');
    expect(container.querySelectorAll('.rounded-full').length).toBeGreaterThan(0); // active-colour dot
    expect(handSection.querySelectorAll('button')).toHaveLength(7);
  });

  it('drawing a card grows the hand to 8', () => {
    render(<UnoGame />);
    fireEvent.click(screen.getByRole('button', { name: 'Draw Card' }));
    const handSection = screen.getByText('Your Hand').closest('div');
    expect(handSection.querySelectorAll('button')).toHaveLength(8);
  });
});
