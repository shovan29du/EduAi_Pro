import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import BiographyLibrary from '../src/components/BiographyLibrary.jsx';

const overview = {
  title: 'Biography Library',
  description: 'Real people across many fields.',
  total_people: 2,
  sections: [
    { id: 'science_innovation', label: 'Science & Innovation', emoji: '🔬', description: 'Scientists.', person_count: 1 },
    { id: 'bengali_notable_people', label: 'Bengali Notable People', emoji: '🇧🇩', description: 'Bengali figures.', person_count: 1 },
  ],
};

const scienceSection = {
  id: 'science_innovation',
  label: 'Science & Innovation',
  emoji: '🔬',
  description: 'Scientists.',
  people: [
    {
      id: 'marie_curie',
      name: 'Marie Curie',
      years: '1867-1934',
      nationality: 'Polish-French',
      field: 'Physicist and chemist',
      summary: 'A long biography of Marie Curie spanning many words about her life and work in science.',
      key_facts: ['Discovered radium', 'Won two Nobel Prizes'],
      discussion: ['What obstacles did she face?'],
      wiki_title: 'Marie Curie',
      links: {
        wikipedia: 'https://en.wikipedia.org/wiki/Marie_Curie',
        video: 'https://www.youtube.com/results?search_query=Marie+Curie',
        image_search: 'https://commons.wikimedia.org/w/index.php?search=Marie+Curie',
        learn_more: 'https://www.google.com/search?q=Marie+Curie',
      },
    },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/biographies') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (u === '/api/biographies/science_innovation') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(scienceSection) });
    }
    if (u === '/api/biographies/science_innovation/marie_curie') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(scienceSection.people[0]) });
    }
    if (u.startsWith('/api/museum/thumbnail')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: null }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('BiographyLibrary', () => {
  it('shows category cards on load', async () => {
    render(<BiographyLibrary />);
    expect(await screen.findByText('Science & Innovation')).toBeInTheDocument();
    expect(screen.getByText('Bengali Notable People')).toBeInTheDocument();
  });

  it('drills into a category and then into a person detail view', async () => {
    render(<BiographyLibrary />);
    fireEvent.click(await screen.findByText('Science & Innovation'));

    expect(await screen.findByText('Marie Curie')).toBeInTheDocument();
    fireEvent.click(screen.getByText('Marie Curie'));

    await waitFor(() => {
      expect(screen.getByText(/A long biography of Marie Curie/)).toBeInTheDocument();
    });
    expect(screen.getByText(/Discovered radium/)).toBeInTheDocument();
  });
});
