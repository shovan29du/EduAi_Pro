import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import CuisineCentre from '../src/components/CuisineCentre.jsx';

const overview = {
  title: 'Cuisine & Food Resource Centre',
  description: 'World cuisines and famous dishes.',
  cuisines: [
    { id: 'indian', label: 'Indian', emoji: '🍛', colour: '#e67e22', region: 'South Asia', description: 'Spices and regional variety.' },
    { id: 'italian', label: 'Italian', emoji: '🍝', colour: '#c0392b', region: 'Southern Europe', description: 'Pasta and regional traditions.' },
  ],
};

const indianDetail = {
  id: 'indian',
  label: 'Indian',
  emoji: '🍛',
  colour: '#e67e22',
  description: 'Spices and regional variety.',
  history: 'A very old culinary tradition.',
  famous_dishes: [{ name: 'Biryani', origin: 'Hyderabad', description: 'Layered spiced rice.' }],
  key_ingredients: ['Rice', 'Turmeric'],
  cooking_techniques: ['Tempering spices'],
  cultural_notes: 'Meals are often shared.',
  fun_facts: ['India is the largest spice producer.'],
  quiz: [{ q: 'What grain is central to biryani?', options: ['Rice', 'Wheat', 'Corn', 'Barley'], answer: 0 }],
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/cuisine') return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    if (u === '/api/cuisine/indian') return Promise.resolve({ ok: true, json: () => Promise.resolve(indianDetail) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('CuisineCentre', () => {
  it('lists cuisines and drills into a detail page', async () => {
    global.fetch = mockFetch();
    render(<CuisineCentre />);
    expect(await screen.findByText('Indian')).toBeInTheDocument();
    expect(screen.getByText('Italian')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Indian'));
    expect(await screen.findByText('Biryani')).toBeInTheDocument();
    expect(screen.getByText(/A very old culinary tradition/)).toBeInTheDocument();
    expect(screen.getByText('← Back to all cuisines')).toBeInTheDocument();
  });

  it('filters cuisines by search', async () => {
    global.fetch = mockFetch();
    render(<CuisineCentre />);
    await screen.findByText('Indian');
    fireEvent.change(screen.getByPlaceholderText('Search cuisines...'), { target: { value: 'Italian' } });
    expect(screen.queryByText('Indian')).not.toBeInTheDocument();
    expect(screen.getByText('Italian')).toBeInTheDocument();
  });

  it('lets the quiz be answered and scored', async () => {
    global.fetch = mockFetch();
    render(<CuisineCentre />);
    fireEvent.click(await screen.findByText('Indian'));
    await screen.findByText('Biryani');
    const riceOption = screen.getAllByText('Rice').find((el) => el.closest('button'));
    fireEvent.click(riceOption.closest('button'));
    fireEvent.click(screen.getByText('Submit Answers'));
    await waitFor(() => expect(screen.getByText(/Perfect score/)).toBeInTheDocument());
  });
});
