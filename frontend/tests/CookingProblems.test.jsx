import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import CookingProblems from '../src/components/CookingProblems.jsx';

const data = {
  title: 'Common Cooking Problems & Fixes',
  description: 'Practical fixes.',
  categories: [
    {
      id: 'sauces',
      label: 'Sauces & Gravies',
      emoji: '🥣',
      problems: [
        { problem: 'Sauce is too salty', fixes: ['Add an acid like lemon juice', 'Dilute with unsalted stock'] },
      ],
    },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/cuisine-detail/cooking-problems') return Promise.resolve({ ok: true, json: () => Promise.resolve(data) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('CookingProblems', () => {
  it('shows a problem and its fixes', async () => {
    global.fetch = mockFetch();
    render(<CookingProblems />);
    expect(await screen.findByText('Sauce is too salty')).toBeInTheDocument();
    expect(screen.getByText(/Add an acid like lemon juice/)).toBeInTheDocument();
  });
});
