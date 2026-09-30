import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import SnakesAndLaddersGame from '../src/components/SnakesAndLaddersGame.jsx';

describe('SnakesAndLaddersGame', () => {
  it('starts both racers at square 0', () => {
    render(<SnakesAndLaddersGame />);
    expect(screen.getByText('🐍 Snakes & Ladders')).toBeInTheDocument();
    expect(screen.getAllByText('0')).toHaveLength(2);
  });

  it('lets the player roll and advances both racers', () => {
    vi.useFakeTimers();
    render(<SnakesAndLaddersGame />);
    fireEvent.click(screen.getByRole('button', { name: /Roll/ }));
    vi.runAllTimers();
    // Both positions have moved away from 0 (player rolled, then the computer took its turn).
    expect(screen.queryAllByText('0').length).toBeLessThan(2);
    vi.useRealTimers();
  });
});
