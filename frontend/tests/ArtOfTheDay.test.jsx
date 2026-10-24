import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen } from '@testing-library/react';
import ArtOfTheDay from '../src/components/ArtOfTheDay.jsx';

const piece = { title: 'Famous Painting: The Starry Night', fact: 'Painted by Vincent van Gogh in 1889.' };

function mockFetch({ thumbnailUrl = '' } = {}) {
  return vi.fn((url) => {
    const u = String(url);
    if (u.startsWith('/api/art-of-the-day')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(piece) });
    }
    if (u.startsWith('/api/museum/thumbnail')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: thumbnailUrl }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('ArtOfTheDay', () => {
  it('renders the fetched art piece with the "Famous X:" prefix stripped from the title', async () => {
    render(<ArtOfTheDay />);
    expect(await screen.findByText('The Starry Night')).toBeInTheDocument();
    expect(screen.getByText('Painted by Vincent van Gogh in 1889.')).toBeInTheDocument();
  });

  it('shows a fallback emoji when no Wikipedia thumbnail is found', async () => {
    render(<ArtOfTheDay />);
    await screen.findByText('The Starry Night');
    expect(screen.getByText('🖼️')).toBeInTheDocument();
    expect(screen.queryByRole('img')).not.toBeInTheDocument();
  });

  it('renders the artwork image when a Wikipedia thumbnail is found', async () => {
    global.fetch = mockFetch({ thumbnailUrl: 'https://upload.wikimedia.org/starry-night.jpg' });
    render(<ArtOfTheDay />);
    const img = await screen.findByRole('img', { name: 'The Starry Night' });
    expect(img).toHaveAttribute('src', 'https://upload.wikimedia.org/starry-night.jpg');
  });

  it('shows an error message when the request fails', async () => {
    global.fetch = vi.fn(() => Promise.resolve({ ok: false }));
    render(<ArtOfTheDay />);
    expect(await screen.findByRole('alert')).toHaveTextContent('Could not load art of the day right now.');
  });
});
