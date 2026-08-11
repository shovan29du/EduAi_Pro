import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen } from '@testing-library/react';
import ArtOfTheDay from '../src/components/ArtOfTheDay.jsx';

function mockFetch(response) {
  return vi.fn(() => Promise.resolve({
    ok: true,
    json: () => Promise.resolve(response),
  }));
}

beforeEach(() => {
  global.fetch = mockFetch({ title: 'Famous Painting: The Starry Night', fact: 'Painted by Vincent van Gogh in 1889.' });
});

describe('ArtOfTheDay', () => {
  it('renders the fetched art piece with the "Famous X:" prefix stripped from the title', async () => {
    render(<ArtOfTheDay />);
    expect(await screen.findByText('The Starry Night')).toBeInTheDocument();
    expect(screen.getByText('Painted by Vincent van Gogh in 1889.')).toBeInTheDocument();
  });

  it('shows an error message when the request fails', async () => {
    global.fetch = vi.fn(() => Promise.resolve({ ok: false }));
    render(<ArtOfTheDay />);
    expect(await screen.findByRole('alert')).toHaveTextContent('Could not load art of the day right now.');
  });
});
