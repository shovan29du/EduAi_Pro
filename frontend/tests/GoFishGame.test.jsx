import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent, within } from '@testing-library/react';
import GoFishGame from '../src/components/GoFishGame.jsx';

describe('GoFishGame', () => {
  it('deals a 7-card hand and shows askable ranks', () => {
    render(<GoFishGame />);
    expect(screen.getByText('🎣 Go Fish')).toBeInTheDocument();
    expect(screen.getByText('Your Books')).toBeInTheDocument();
    expect(screen.getByText('Pond')).toBeInTheDocument();

    const handSection = screen.getByText(/Your Hand/).closest('div');
    const askButtons = within(handSection).getAllByRole('button');
    expect(askButtons.length).toBeGreaterThan(0);
  });

  it('lets the player ask for a rank without crashing and keeps the log within its 6-line cap', () => {
    const { container } = render(<GoFishGame />);
    const handSection = screen.getByText(/Your Hand/).closest('div');
    const askButtons = within(handSection).getAllByRole('button');
    expect(askButtons[0].textContent).toMatch(/×\d+/);

    fireEvent.click(askButtons[0]);

    expect(screen.getByText('🎣 Go Fish')).toBeInTheDocument();
    const logLines = container.querySelectorAll('p.text-xs.text-gray-600');
    expect(logLines.length).toBeGreaterThanOrEqual(1);
    expect(logLines.length).toBeLessThanOrEqual(6);
  });
});
