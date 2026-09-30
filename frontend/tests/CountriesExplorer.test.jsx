import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import CountriesExplorer from '../src/components/CountriesExplorer.jsx';

const listCountries = [
  {
    code: 'FR', name: 'France', capital: 'Paris', continent: 'Europe', flag_emoji: '🇫🇷',
    coordinates: { lat: 48.8566, lng: 2.3522 },
    links: { google_maps: 'https://www.google.com/maps/@48.8566,2.3522,12z', google_earth: 'https://earth.google.com/web/@48.8566,2.3522,0a,20000d,35y,0h,0t,0r' },
  },
  {
    code: 'JP', name: 'Japan', capital: 'Tokyo', continent: 'Asia', flag_emoji: '🇯🇵',
    coordinates: { lat: 35.6762, lng: 139.6503 },
    links: { google_maps: 'https://www.google.com/maps/@35.6762,139.6503,12z', google_earth: 'https://earth.google.com/web/@35.6762,139.6503,0a,20000d,35y,0h,0t,0r' },
  },
];

const franceDetail = {
  code: 'FR', name: 'France', capital: 'Paris', continent: 'Europe', population: 68000000,
  currency: 'Euro (EUR)', language: 'French', flag_emoji: '🇫🇷',
  coordinates: { lat: 48.8566, lng: 2.3522 },
  links: {
    google_maps: 'https://www.google.com/maps/@48.8566,2.3522,12z',
    google_earth: 'https://earth.google.com/web/@48.8566,2.3522,0a,20000d,35y,0h,0t,0r',
    text_wikipedia: 'https://en.wikipedia.org/wiki/France',
  },
};

function mockFetch() {
  return vi.fn((url) => {
    if (url === '/api/countries') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ countries: listCountries, total: listCountries.length }) });
    }
    if (url === '/api/countries/FR') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(franceDetail) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('CountriesExplorer', () => {
  it('loads countries and defaults to the World Map view with a pin per country', async () => {
    const { container } = render(<CountriesExplorer />);
    await waitFor(() => expect(screen.getByText('2 countries')).toBeInTheDocument());
    expect(screen.getByRole('img', { name: 'World map of country capitals' })).toBeInTheDocument();
    expect(container.querySelectorAll('svg circle[stroke="white"]')).toHaveLength(2);
  });

  it('clicking a pin shows the country card with Google Maps and Google Earth links', async () => {
    const { container } = render(<CountriesExplorer />);
    await waitFor(() => expect(screen.getByText('2 countries')).toBeInTheDocument());

    const pin = container.querySelector('svg g.cursor-pointer');
    fireEvent.click(pin);

    expect(await screen.findByText('France')).toBeInTheDocument();
    const mapsLink = screen.getByRole('link', { name: /Google Maps/ });
    const earthLink = screen.getByRole('link', { name: /Google Earth/ });
    expect(mapsLink).toHaveAttribute('href', 'https://www.google.com/maps/@48.8566,2.3522,12z');
    expect(earthLink).toHaveAttribute('href', 'https://earth.google.com/web/@48.8566,2.3522,0a,20000d,35y,0h,0t,0r');
  });

  it('switches to List view and opens full country details with map links', async () => {
    render(<CountriesExplorer />);
    await waitFor(() => expect(screen.getByText('2 countries')).toBeInTheDocument());

    fireEvent.click(screen.getByRole('button', { name: '📋 List' }));
    fireEvent.click(screen.getByText('France'));

    expect(await screen.findByRole('heading', { name: 'France' })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /Open in Google Maps/ })).toHaveAttribute(
      'href',
      'https://www.google.com/maps/@48.8566,2.3522,12z'
    );
    expect(screen.getByRole('link', { name: /Open in Google Earth/ })).toHaveAttribute(
      'href',
      'https://earth.google.com/web/@48.8566,2.3522,0a,20000d,35y,0h,0t,0r'
    );
  });
});
