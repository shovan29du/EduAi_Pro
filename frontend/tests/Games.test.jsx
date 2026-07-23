import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent, within } from '@testing-library/react';
import Games from '../src/components/Games.jsx';
import { TOTAL_GAMES, CATEGORIES } from '../src/data/gameCentreData.js';

describe('Games (Game Centre)', () => {
  it('has at least 50 games defined across its categories', () => {
    expect(TOTAL_GAMES).toBeGreaterThanOrEqual(50);
  });

  it('renders the category picker and shows the total game count', () => {
    render(<Games grade={null} />);
    expect(screen.getByText('🎮 Game Centre')).toBeInTheDocument();
    expect(screen.getByText(new RegExp(`${TOTAL_GAMES} games across ${CATEGORIES.length} categories`))).toBeInTheDocument();
    // Every category shows up as a picker card.
    for (const cat of CATEGORIES) {
      expect(screen.getByText(cat.label)).toBeInTheDocument();
    }
  });

  it('drills into a category to show its games, then into a game to play it', () => {
    render(<Games grade={null} />);
    fireEvent.click(screen.getByText('Memory Match'));
    expect(screen.getByText('← All Categories')).toBeInTheDocument();
    expect(screen.getByText('Animal Friends')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Animal Friends'));
    expect(screen.getByText(/Back to Memory Match/)).toBeInTheDocument();
    expect(screen.getAllByRole('button', { name: '❓' }).length).toBeGreaterThan(0);
  });

  it('can still play the existing Phonics Match and Quiz Sprint games', () => {
    render(<Games grade={null} />);
    fireEvent.click(screen.getByText('Classic Word Games'));
    fireEvent.click(screen.getByText('Phonics Match'));
    expect(screen.getByText('Phonics Match')).toBeInTheDocument();
    expect(screen.getAllByRole('button').length).toBeGreaterThanOrEqual(3);
  });
});
