import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import ReversiGame from '../src/components/ReversiGame.jsx';

describe('ReversiGame', () => {
  it('starts with the standard 2-2 opening position', () => {
    render(<ReversiGame />);
    expect(screen.getByText('⚫ Reversi')).toBeInTheDocument();
    expect(screen.getByText('⚫ You: 2')).toBeInTheDocument();
    expect(screen.getByText('⚪ Computer: 2')).toBeInTheDocument();
  });

  it('lets the player make a legal opening move and the computer replies', () => {
    vi.useFakeTimers();
    render(<ReversiGame />);
    // One of the 4 legal opening moves for black is always enabled; find and click it.
    const cells = screen.getAllByRole('button').filter((b) => !b.disabled);
    expect(cells.length).toBeGreaterThan(0);
    fireEvent.click(cells[0]);
    vi.runAllTimers();
    // After the exchange plus the computer's reply, disc counts have grown past 2-2.
    const total = screen.getByText(/⚫ You: \d/).textContent + screen.getByText(/⚪ Computer: \d/).textContent;
    expect(total).not.toBe('⚫ You: 2⚪ Computer: 2');
    vi.useRealTimers();
  });
});
