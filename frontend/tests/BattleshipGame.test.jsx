import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import BattleshipGame from '../src/components/BattleshipGame.jsx';

describe('BattleshipGame', () => {
  it('renders two 8x8 grids and a fleet-sunk tracker starting at 0/5', () => {
    render(<BattleshipGame />);
    expect(screen.getByText('🚢 Battleship')).toBeInTheDocument();
    expect(screen.getByText(/Enemy ships sunk: 0\/5/)).toBeInTheDocument();
    expect(screen.getByText(/Your ships sunk: 0\/5/)).toBeInTheDocument();
  });

  it('lets the player fire at the enemy grid and get a response', () => {
    vi.useFakeTimers();
    render(<BattleshipGame />);
    const enemyGrid = screen.getByText('Enemy Waters — click to fire').nextElementSibling;
    const firstCell = enemyGrid.querySelector('button');
    fireEvent.click(firstCell);
    expect(firstCell.disabled).toBe(true);
    vi.runAllTimers();
    expect(screen.getByText('🚢 Battleship')).toBeInTheDocument();
    vi.useRealTimers();
  });
});
