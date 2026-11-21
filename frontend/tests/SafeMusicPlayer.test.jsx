import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import MusicInstruments from '../src/components/MusicInstruments.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

// The standalone "Music" tab (safe music player) was merged into
// "Music & Instruments" -- this test now exercises that embedded section.
beforeEach(() => {
  localStorage.clear();
  global.fetch = vi.fn((url) => {
    if (url === '/api/safe-music') {
      return Promise.resolve({
        ok: true,
        json: () =>
          Promise.resolve([
            {
              title: 'Sing-along nursery rhymes',
              videoUrl: 'https://www.youtube.com/channel/UCLsooMJoIpl_7ux2jvdPB-Q',
              source: 'Super Simple Songs',
              safe: true,
            },
          ]),
      });
    }
    if (url === '/api/music-instruments') {
      return Promise.resolve({
        ok: true,
        json: () =>
          Promise.resolve({
            description: 'Learn music theory and instruments.',
            categories: [],
            instruments: [],
          }),
      });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('MusicInstruments (with merged Safe Music Library)', () => {
  it('lists only approved safe songs alongside the Music & Instruments overview', async () => {
    render(
      <ChildProvider>
        <MusicInstruments />
      </ChildProvider>
    );

    await waitFor(() => {
      expect(screen.getByText('🎵 Music & Instruments')).toBeInTheDocument();
    });
    await waitFor(() => {
      expect(screen.getByText('Sing-along nursery rhymes')).toBeInTheDocument();
    });
    expect(screen.getByText('Super Simple Songs')).toBeInTheDocument();
  });
});
