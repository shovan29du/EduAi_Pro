import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import IngredientAlternatives from '../src/components/IngredientAlternatives.jsx';

const data = {
  title: 'Ingredient Alternatives & Substitutions',
  description: 'Reliable swaps.',
  categories: [
    {
      id: 'halal_substitutes',
      label: 'Halal Substitutes for Haram Ingredients',
      emoji: '🐄',
      items: [
        { ingredient: 'Pork bacon', alternatives: ['Chicken bacon', 'Beef bacon'], notes: 'Closest match.' },
      ],
    },
    {
      id: 'dairy',
      label: 'Dairy',
      emoji: '🥛',
      items: [
        { ingredient: 'Buttermilk', alternatives: ['Milk + lemon juice'], notes: 'Curdles slightly.' },
      ],
    },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/cuisine-detail/ingredient-alternatives') return Promise.resolve({ ok: true, json: () => Promise.resolve(data) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('IngredientAlternatives', () => {
  it('shows the halal substitutes section and general substitutions', async () => {
    global.fetch = mockFetch();
    render(<IngredientAlternatives />);
    expect(await screen.findByText('Pork bacon')).toBeInTheDocument();
    expect(screen.getByText(/Chicken bacon/)).toBeInTheDocument();
    expect(screen.getByText('Buttermilk')).toBeInTheDocument();
  });
});
