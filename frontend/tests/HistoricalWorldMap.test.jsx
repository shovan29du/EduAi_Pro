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
  it('shows a gallery collection of every century as cards', async () => {
    render(<HistoricalWorldMap />);
    await waitFor(() => expect(screen.getByText('2 time periods')).toBeInTheDocument());
    expect(screen.getByText('Ancient Times')).toBeInTheDocument();
    expect(screen.getByText('Contemporary World')).toBeInTheDocument();
    expect(screen.getByText(/A collection of 2 world maps/)).toBeInTheDocument();
  });

  it('opening a century card shows its map, events, and famous maps, with a way back to the gallery', async () => {
    render(<HistoricalWorldMap />);
    await waitFor(() => expect(screen.getByText('Ancient Times')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Ancient Times'));

    expect(await screen.findByText(/Ancient Times/, { selector: 'p.font-bold' })).toBeInTheDocument();
    expect(screen.getByText('The earliest civilizations.')).toBeInTheDocument();
    expect(screen.getByText('Cuneiform writing develops.')).toBeInTheDocument();
    const mapLink = screen.getByRole('link', { name: /Babylonian Map of the World/ });
    expect(mapLink).toHaveAttribute('href', 'https://en.wikipedia.org/wiki/Babylonian_Map_of_the_World');

    fireEvent.click(screen.getByText('← All Centuries'));
    await waitFor(() => expect(screen.getByText('2 time periods')).toBeInTheDocument());
  });

  it('lets the user jump to a different century via the in-page dropdown', async () => {
    render(<HistoricalWorldMap />);
    await waitFor(() => expect(screen.getByText('Ancient Times')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Ancient Times'));
    await screen.findByText(/Ancient Times/, { selector: 'p.font-bold' });

    fireEvent.change(screen.getByLabelText('Jump to a different time period'), { target: { value: 'contemporary' } });

    await waitFor(() => expect(screen.getByText('The world today.')).toBeInTheDocument());
    expect(screen.getByText('The Soviet Union dissolves.')).toBeInTheDocument();
    expect(screen.queryByText('Cuneiform writing develops.')).not.toBeInTheDocument();
  });

  it('clicking a region marker shows its note', async () => {
    const { container } = render(<HistoricalWorldMap />);
    await waitFor(() => expect(screen.getByText('Ancient Times')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Ancient Times'));
    await screen.findByText(/Ancient Times/, { selector: 'p.font-bold' });

    const marker = container.querySelector('svg g.cursor-pointer');
    fireEvent.click(marker);

    expect(await screen.findByText('One of the first cities.')).toBeInTheDocument();
  });

  it('filters the gallery by search', async () => {
    render(<HistoricalWorldMap />);
    await waitFor(() => expect(screen.getByText('2 time periods')).toBeInTheDocument());

    fireEvent.change(screen.getByLabelText('Search historical periods'), { target: { value: 'contemporary' } });

    expect(screen.getByText('1 time period')).toBeInTheDocument();
    expect(screen.getByText('Contemporary World')).toBeInTheDocument();
    expect(screen.queryByText('Ancient Times')).not.toBeInTheDocument();
  });
});
