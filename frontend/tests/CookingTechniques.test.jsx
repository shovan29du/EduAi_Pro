import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import CookingTechniques from '../src/components/CookingTechniques.jsx';

const data = {
  title: 'Cooking Techniques Glossary',
  description: 'Core culinary techniques.',
  categories: [
    {
      id: 'heat-dry',
      label: 'Dry-Heat Methods',
      emoji: '🔥',
      techniques: [
        {
          name: 'Grilling',
          description: 'Cooking directly over a heat source.',
          example_dishes: ['Korean BBQ'],
          links: {
            picture_wiki_title: 'Grilling',
            video: 'https://www.youtube.com/results?search_query=Grilling',
            text_guide: 'https://www.google.com/search?q=Grilling',
          },
          related_recipes: [{ id: 'recipe_indian_0001', name: 'Chicken Tikka', cuisine: 'Indian' }],
        },
      ],
    },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/cuisine-detail/techniques') return Promise.resolve({ ok: true, json: () => Promise.resolve(data) });
    if (u.startsWith('/api/cuisine/thumbnail')) return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: null }) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('CookingTechniques', () => {
  it('shows a technique with video/text links and related recipes', async () => {
    global.fetch = mockFetch();
    render(<CookingTechniques />);
    expect(await screen.findByText('Grilling')).toBeInTheDocument();
    expect(screen.getByText('Chicken Tikka')).toBeInTheDocument();
    expect(screen.getByText('▶ Video').closest('a')).toHaveAttribute('href', data.categories[0].techniques[0].links.video);
    expect(screen.getByText('📖 Guide').closest('a')).toHaveAttribute('href', data.categories[0].techniques[0].links.text_guide);
  });
});
