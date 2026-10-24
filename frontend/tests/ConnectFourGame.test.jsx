import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import ConnectFourGame from '../src/components/ConnectFourGame.jsx';

describe('ConnectFourGame', () => {
  it('renders a 7-column, 6-row empty board', () => {
    const { container } = render(<ConnectFourGame />);
    expect(screen.getByText('🔴 Connect Four')).toBeInTheDocument();
    expect(container.querySelectorAll('.rounded-full').length).toBe(42);
  });

  it('drops a disc into a column and the computer replies', () => {
    vi.useFakeTimers();
    const { container } = render(<ConnectFourGame />);
    const dropButtons = screen.getAllByRole('button', { name: '▼' });
    fireEvent.click(dropButtons[3]);
    act(() => {
      vi.runAllTimers();
    });
    const filled = container.querySelectorAll('.bg-red-500, .bg-amber-400');
    expect(filled.length).toBe(2);
    vi.useRealTimers();
  });
});
