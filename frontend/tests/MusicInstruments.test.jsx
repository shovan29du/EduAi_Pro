import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import MusicInstruments from '../src/components/MusicInstruments.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

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

// jsdom has no Web Audio API — provide a minimal mock so the simulator
// renders its playable UI (rather than the "not supported" fallback) and so
// clicking a key can be asserted to actually invoke the synth engine.
class MockAudioContext {
  constructor() {
    this.state = 'running';
    this.currentTime = 0;
    this.destination = {};
  }
  createOscillator() {
    return {
      type: 'sine',
      frequency: { value: 0 },
      connect: vi.fn().mockReturnThis(),
      start: vi.fn(),
      stop: vi.fn(),
    };
  }
  createGain() {
    return {
      gain: {
        setValueAtTime: vi.fn(),
        exponentialRampToValueAtTime: vi.fn(),
      },
      connect: vi.fn().mockReturnThis(),
    };
  }
  resume() {}
  close() {}
}

beforeEach(() => {
  window.AudioContext = MockAudioContext;
  global.fetch = vi.fn((url) => {
    if (url === '/api/music-instruments') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (url === '/api/music-instruments/instrument/piano') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(pianoDetail) });
    }
    if (url === '/api/safe-music') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (url === '/api/progress/Parent') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ completed_lessons: {} }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('MusicInstruments', () => {
  it('shows instrument categories and lets you drill into an instrument', async () => {
    render(
      <ChildProvider>
        <MusicInstruments />
      </ChildProvider>
    );

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

  it('lets you play the virtual piano with mouse and keyboard', async () => {
    render(
      <ChildProvider>
        <MusicInstruments />
      </ChildProvider>
    );

    await waitFor(() => expect(screen.getByText('Piano')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Piano'));

    await waitFor(() => {
      expect(screen.getByRole('group', { name: 'Virtual piano keyboard' })).toBeInTheDocument();
    });

    const createOscillatorSpy = vi.spyOn(MockAudioContext.prototype, 'createOscillator');

    // Click a key.
    fireEvent.mouseDown(screen.getByRole('button', { name: 'Play C4' }));
    expect(createOscillatorSpy).toHaveBeenCalledTimes(1);

    // Play a note via the mapped computer keyboard key ('a' => C4).
    fireEvent.keyDown(window, { key: 'a' });
    expect(createOscillatorSpy).toHaveBeenCalledTimes(2);
  });

  it('lets you mark a practice routine as done today and shows the practiced count', async () => {
    render(
      <ChildProvider>
        <MusicInstruments />
      </ChildProvider>
    );

    await waitFor(() => expect(screen.getByText('Piano')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Piano'));

    await waitFor(() => {
      expect(screen.getByText((_, el) => el?.textContent === '🔥 Practiced 0 times')).toBeInTheDocument();
    });

    const checkbox = screen.getByRole('checkbox', { name: /Mark practiced today: Practice scales daily\./ });
    expect(checkbox).not.toBeChecked();

    fireEvent.click(checkbox);

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        '/api/progress/Parent',
        expect.objectContaining({ method: 'POST' })
      );
    });
    await waitFor(() => expect(checkbox).toBeChecked());
    await waitFor(() => {
      expect(screen.getByText((_, el) => el?.textContent === '🔥 Practiced 1 time')).toBeInTheDocument();
    });
  });
});
