import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import RecipeCollection from '../src/components/RecipeCollection.jsx';

const recipe = {
  id: 'recipe_indian_0001',
  name: 'Butter Chicken',
  cuisine: 'Indian',
  cuisine_id: 'indian',
  category: 'Main Course',
  category_id: 'main',
  emoji: '🍽️',
  protein: 'Chicken',
  pork_free: true,
  substitution_note: null,
  description: 'Butter Chicken is a main course from Indian cuisine, built around chicken.',
  historical_fact: "Invented at Delhi's Moti Mahal restaurant in the late 1940s.",
  cooking_technique: 'Sautéing',
  wiki_title: 'Butter Chicken',
  links: {
    wikipedia: 'https://en.wikipedia.org/w/index.php?search=Butter+Chicken',
    image_search: 'https://commons.wikimedia.org/w/index.php?search=Butter+Chicken',
    video: 'https://www.youtube.com/results?search_query=Butter+Chicken',
    text_guide: 'https://www.google.com/search?q=Butter+Chicken',
  },
};

const recipesResponse = { total: 1, count: 1, offset: 0, recipes: [recipe] };
const cuisineList = { cuisines: [{ id: 'indian', label: 'Indian' }, { id: 'italian', label: 'Italian' }] };

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/cuisine-detail/recipe-cuisines') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(cuisineList) });
    }
    if (u.startsWith('/api/cuisine-detail/recipes?')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(recipesResponse) });
    }
    if (u.startsWith('/api/cuisine/thumbnail')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: null }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('RecipeCollection', () => {
  it('shows recipe cards and a total count', async () => {
    global.fetch = mockFetch();
    render(<RecipeCollection />);
    expect(await screen.findByText('Butter Chicken')).toBeInTheDocument();
    expect(screen.getByText('1 dish found')).toBeInTheDocument();
  });

  it('opens a recipe detail modal with picture, video, and text links plus the historical fact', async () => {
    global.fetch = mockFetch();
    render(<RecipeCollection />);
    fireEvent.click(await screen.findByText('Butter Chicken'));
    await waitFor(() => expect(screen.getByText(/Moti Mahal/)).toBeInTheDocument());
    expect(screen.getByText('▶ YouTube Video')).toBeInTheDocument();
    expect(screen.getByText('🖼 Pictures')).toBeInTheDocument();
    expect(screen.getByText('📖 Recipe Guide')).toBeInTheDocument();
  });

  it('populates the cuisine filter from the recipe collection', async () => {
    global.fetch = mockFetch();
    render(<RecipeCollection />);
    await screen.findByText('Butter Chicken');
    expect(screen.getByRole('option', { name: 'Indian' })).toBeInTheDocument();
    expect(screen.getByRole('option', { name: 'Italian' })).toBeInTheDocument();
  });
});
