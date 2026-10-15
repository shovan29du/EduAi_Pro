import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import CheckersGame from '../src/components/CheckersGame.jsx';

describe('CheckersGame', () => {
  it('deals 12 pieces to each side', () => {
    render(<CheckersGame />);
    expect(screen.getByText('🔴 Checkers')).toBeInTheDocument();
    expect(screen.getByText('🔴 You: 12')).toBeInTheDocument();
    expect(screen.getByText('⚫ Computer: 12')).toBeInTheDocument();
  });

  it('lets the player select a piece, move it, and hands the turn to the computer', () => {
    vi.useFakeTimers();
    const { container } = render(<CheckersGame />);
    // Row 5 is the frontmost row of the player's pieces (able to move forward into empty row 4).
    const cells = Array.from(container.querySelectorAll('button'));
    const playerPiece = cells.find((b) => b.querySelector('.bg-red-600'));
    fireEvent.click(playerPiece);
    const target = cells.find((b) => b.querySelector('.bg-emerald-400'));
    expect(target).toBeTruthy();
    fireEvent.click(target);
    expect(screen.getByText("Computer's turn…")).toBeInTheDocument();
    vi.runAllTimers();
    vi.useRealTimers();
  });
});
