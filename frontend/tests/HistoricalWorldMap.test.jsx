import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import HistoricalWorldMap from '../src/components/HistoricalWorldMap.jsx';

const periods = [
  {
    id: 'ancient', label: 'Ancient Times', years: 'c. 3000 BCE', emoji: '🎺',
    description: 'The earliest civilizations.',
    regions: [
      { name: 'Sumer (Uruk)', lat: 31.3225, lng: 45.6372, note: 'One of the first cities.' },
      { name: 'Old Kingdom Egypt (Memphis)', lat: 29.85, lng: 31.25, note: 'Pyramid builders.' },
    ],
    events: [{ year: 'c. 3500 BCE', event: 'Cuneiform writing develops.' }],
    famous_maps: [{ name: 'Babylonian Map of the World', year: 'c. 600 BCE', description: 'The oldest known world map.', link: 'https://en.wikipedia.org/wiki/Babylonian_Map_of_the_World' }],
  },
  {
    id: 'contemporary', label: 'Contemporary World', years: '1991–present', emoji: '🌍',
    description: 'The world today.',
    regions: [{ name: 'United States (Washington D.C.)', lat: 38.9072, lng: -77.0369, note: 'Capital of the USA.' }],
    events: [{ year: '1991', event: 'The Soviet Union dissolves.' }],
    famous_maps: [{ name: 'Google Earth', year: '2005', description: 'Satellite mapping.', link: 'https://en.wikipedia.org/wiki/Google_Earth' }],
  },
];

beforeEach(() => {
  global.fetch = vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({ periods }) }));
});

describe('HistoricalWorldMap', () => {
  it('defaults to the first period and shows its events and famous maps', async () => {
    render(<HistoricalWorldMap />);
    expect(await screen.findByText(/Ancient Times/, { selector: 'p.font-bold' })).toBeInTheDocument();
    expect(screen.getByText('The earliest civilizations.')).toBeInTheDocument();
    expect(screen.getByText('Cuneiform writing develops.')).toBeInTheDocument();
    const mapLink = screen.getByRole('link', { name: /Babylonian Map of the World/ });
    expect(mapLink).toHaveAttribute('href', 'https://en.wikipedia.org/wiki/Babylonian_Map_of_the_World');
  });

  it('lets the user switch time periods via the dropdown', async () => {
    render(<HistoricalWorldMap />);
    await screen.findByText(/Ancient Times/, { selector: 'p.font-bold' });

    fireEvent.change(screen.getByLabelText('Choose a time period'), { target: { value: 'contemporary' } });

    await waitFor(() => expect(screen.getByText('The world today.')).toBeInTheDocument());
    expect(screen.getByText('The Soviet Union dissolves.')).toBeInTheDocument();
    expect(screen.queryByText('Cuneiform writing develops.')).not.toBeInTheDocument();
  });

  it('clicking a region marker shows its note', async () => {
    const { container } = render(<HistoricalWorldMap />);
    await screen.findByText(/Ancient Times/, { selector: 'p.font-bold' });

    const marker = container.querySelector('svg g.cursor-pointer');
    fireEvent.click(marker);

    expect(await screen.findByText('One of the first cities.')).toBeInTheDocument();
  });
});
