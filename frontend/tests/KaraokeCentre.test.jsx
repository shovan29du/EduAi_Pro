import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import KaraokeCentre from '../src/components/KaraokeCentre.jsx';

function mockFetchFor(classicsSongs, catalogData) {
  global.fetch = vi.fn((url) => {
    if (url.includes('/api/sing-along-songs')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(classicsSongs) });
    }
    if (url.includes('/api/songs')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(catalogData) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

const classics = [
  {
    title: 'Twinkle, Twinkle, Little Star',
    source: 'Traditional / public domain',
    lyrics: ['Twinkle, twinkle, little star,', 'How I wonder what you are!'],
    channelUrl: 'https://www.youtube.com/channel/UCLsooMJoIpl_7ux2jvdPB-Q',
    safe: true,
  },
];

const catalog = {
  total: 1,
  songs: [
    {
      id: 'hey_jude', title: 'Hey Jude', artist: 'The Beatles', album: 'Hey Jude (single)',
      year: 1968, genre: ['pop', 'rock'], origin_country: 'United Kingdom', language: 'English',
      duration_approx: '7:11', description: 'desc', educational_notes: 'notes', fun_fact: 'fact',
      awards: [], links: { youtube_search: 'https://example.com', wiki_search: 'https://example.com', lyrics_search: 'https://example.com' },
      tags: [], decade: '1960s', suitable_for_ages: '5+',
    },
  ],
  genres: ['pop', 'rock'],
  decades: ['1960s'],
};

beforeEach(() => {
  mockFetchFor(classics, catalog);
});

describe('KaraokeCentre', () => {
  it('defaults to the Karaoke Classics tab and shows full synced lyrics', async () => {
    render(<KaraokeCentre />);
    await waitFor(() => {
      expect(screen.getByText('Twinkle, twinkle, little star,')).toBeInTheDocument();
    });
    expect(screen.getByText('How I wonder what you are!')).toBeInTheDocument();
  });

  it('switches to the Full Song Catalog and shows the merged Song Centre catalog', async () => {
    render(<KaraokeCentre />);
    fireEvent.click(screen.getByRole('tab', { name: /Full Song Catalog/i }));
    await waitFor(() => {
      expect(screen.getByText('Hey Jude')).toBeInTheDocument();
    });
  });

  it('does not embed copyrighted lyrics for catalog songs, only a karaoke/lyrics link-out', async () => {
    render(<KaraokeCentre />);
    fireEvent.click(screen.getByRole('tab', { name: /Full Song Catalog/i }));
    await waitFor(() => screen.getByText('Hey Jude'));
    fireEvent.click(screen.getByText('Hey Jude'));
    expect(await screen.findByText(/can't reproduce its lyrics here/i)).toBeInTheDocument();
  });
});
