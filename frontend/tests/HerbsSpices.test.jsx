import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import HerbsSpices from '../src/components/HerbsSpices.jsx';

const data = {
  title: 'Herbs & Spices Encyclopedia',
  description: 'Real herbs and spices.',
  items: [
    { name: 'Basil', category: 'herb', description: 'A sweet herb.', uses: ['Pesto', 'Tomato sauces'], alternatives: ['Oregano'], wiki_title: 'Basil' },
    { name: 'Cumin', category: 'spice', description: 'An earthy spice.', uses: ['Curries'], alternatives: ['Coriander'], wiki_title: 'Cumin' },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/cuisine-detail/herbs-spices') return Promise.resolve({ ok: true, json: () => Promise.resolve(data) });
    if (u.startsWith('/api/cuisine/thumbnail')) return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: null }) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('HerbsSpices', () => {
  it('shows herb and spice cards with uses and alternatives', async () => {
    global.fetch = mockFetch();
    render(<HerbsSpices />);
    expect(await screen.findByText('Basil')).toBeInTheDocument();
    expect(screen.getByText('Cumin')).toBeInTheDocument();
    expect(screen.getByText('Pesto')).toBeInTheDocument();
    expect(screen.getByText(/Oregano/)).toBeInTheDocument();
  });
});
