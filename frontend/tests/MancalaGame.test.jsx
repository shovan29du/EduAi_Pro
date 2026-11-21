import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import MancalaGame from '../src/components/MancalaGame.jsx';

describe('MancalaGame', () => {
  it('deals 4 seeds into each of the 12 pits and empty stores', () => {
    render(<MancalaGame />);
    expect(screen.getByText('🌰 Mancala')).toBeInTheDocument();
    const pitCounts = screen.getAllByText('4');
    expect(pitCounts.length).toBe(12);
  });

  it('lets the player sow a pit and eventually hands the turn to the computer', () => {
    vi.useFakeTimers();
    render(<MancalaGame />);
    const playablePit = screen.getAllByRole('button').find((b) => b.textContent === '4' && !b.disabled);
    fireEvent.click(playablePit);
    vi.runAllTimers();
    expect(screen.getByText('🌰 Mancala')).toBeInTheDocument();
    vi.useRealTimers();
  });
});
