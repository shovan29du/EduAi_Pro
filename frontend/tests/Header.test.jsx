import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import Header from '../src/components/Header.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

beforeEach(() => {
  localStorage.clear();
  global.fetch = vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({}) }));
});

describe('Header', () => {
  it('shows a "Check for Updates" button for the parent profile that dispatches the check event', () => {
    const handler = vi.fn();
    window.addEventListener('eduai-check-for-updates', handler);

    render(
      <ChildProvider>
        <Header />
      </ChildProvider>
    );

    const button = screen.getByRole('button', { name: /Check for Updates/i });
    fireEvent.click(button);
    expect(handler).toHaveBeenCalledTimes(1);

    window.removeEventListener('eduai-check-for-updates', handler);
  });
});
