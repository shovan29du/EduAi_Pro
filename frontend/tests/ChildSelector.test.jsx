import React from 'react';
import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import ChildSelector from '../src/components/ChildSelector.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

beforeEach(() => {
  localStorage.clear();
});

describe('ChildSelector', () => {
  it('changes selected child and persists to localStorage', () => {
    render(
      <ChildProvider>
        <ChildSelector />
      </ChildProvider>
    );
    const select = screen.getByLabelText('Select profile');
    fireEvent.change(select, { target: { value: 'Shovan' } });
    expect(select.value).toBe('Shovan');
    expect(localStorage.getItem('selectedChild')).toBe('Shovan');
  });

  it('falls back to a single Shovan profile option when /api/users has not responded yet', () => {
    render(
      <ChildProvider>
        <ChildSelector />
      </ChildProvider>
    );
    const select = screen.getByLabelText('Select profile');
    expect(select).toHaveTextContent('Shovan (Administrator)');
  });
});
