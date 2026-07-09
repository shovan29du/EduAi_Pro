import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import MusicInstruments from '../src/components/MusicInstruments.jsx';

const overview = {
  title: 'Music & Instruments',
  description: 'Learn music at every age.',
  categories: [
    { id: 'music_theory', label: 'Music Theory', emoji: '🎼', description: 'Notes and scales.' },
  ],
  instruments: [
    { id: 'piano', label: 'Piano', emoji: '🎹' },
    { id: 'guitar', label: 'Guitar', emoji: '🎸' },
  ],
};

const pianoDetail = {
  label: 'Piano',
  emoji: '🎹',
  beginner: [{ title: 'Hand position', description: 'Beginner piano lesson.', youtube_search_url: 'https://www.youtube.com/results?search_query=piano' }],
  intermediate: [],
  advanced: [],
  practice_routines: ['Practice scales daily.'],
  youtube_searches: [{ title: 'Piano lessons for beginners', url: 'https://www.youtube.com/results?search_query=piano' }],
  audio_resources: [{ title: 'Piano sheet music', url: 'https://www.8notes.com/' }],
};

beforeEach(() => {
  global.fetch = vi.fn((url) => {
    if (url === '/api/music-instruments') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (url === '/api/music-instruments/instrument/piano') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(pianoDetail) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('MusicInstruments', () => {
  it('shows instrument categories and lets you drill into an instrument', async () => {
    render(<MusicInstruments />);

    await waitFor(() => {
      expect(screen.getByText(/Music & Instruments/)).toBeInTheDocument();
    });
    expect(screen.getByText('Piano')).toBeInTheDocument();
    expect(screen.getByText('Guitar')).toBeInTheDocument();
    expect(screen.getByText('Music Theory')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Piano'));

    await waitFor(() => {
      expect(screen.getByText('Hand position')).toBeInTheDocument();
    });
    expect(screen.getByText('Practice scales daily.')).toBeInTheDocument();
  });
});
