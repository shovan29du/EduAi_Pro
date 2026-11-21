import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor, within } from '@testing-library/react';
import VirtualTour from '../src/components/VirtualTour.jsx';

const ok = (body) => Promise.resolve({ ok: true, json: () => Promise.resolve(body) });
const fail = (status = 500) => Promise.resolve({ ok: false, status, json: () => Promise.resolve({}) });

const OVERVIEW = {
  continents: [
    { id: 'europe', label: 'Europe', emoji: '🏰', country_count: 1, place_count: 3, road_trip_count: 1 },
    { id: 'asia', label: 'Asia', emoji: '🌏', country_count: 1, place_count: 2, road_trip_count: 0 },
  ],
  totals: { countries: 2, places: 5, cities: 3, road_trips: 1 },
};
const COUNTRIES = [
  { code: 'FR', name: 'France', capital: 'Paris', flag_emoji: '🇫🇷', continent_id: 'europe', place_count: 3, city_count: 2, coordinates: { lat: 48.8566, lng: 2.3522 } },
  { code: 'JP', name: 'Japan', capital: 'Tokyo', flag_emoji: '🇯🇵', continent_id: 'asia', place_count: 2, city_count: 1, coordinates: { lat: 35.6762, lng: 139.6503 } },
];
const link = (kind, name) => `https://example.org/${kind}/${encodeURIComponent(name)}`;
const placeLinks = (n) => ({ video: link('video', n), blog: link('blog', n), photos: link('photos', n), map: link('map', n), earth: link('earth', n) });
const TRIP = {
  id: 'route-napoleon', name: 'Route Napoleon', countries: ['FR'], country_names: ['France'], continent_ids: ['europe'],
  start: 'Golfe-Juan', end: 'Grenoble', km: 325, duration: '2 days', best_time: 'May to September', kind: 'historic',
  summary: "Follow Napoleon's 1815 return.", highlights: ['Grasse', 'Castellane', 'Gap'], tip: 'Passes can be icy.',
  links: { route: 'https://maps.example/route', video: link('video', 'rn'), blog: link('blog', 'rn'), photos: link('photos', 'rn'), earth: link('earth', 'rn') },
};
const FRANCE = {
  profile: { code: 'FR', name: 'France', capital: 'Paris', continent: 'Europe', population: 68000000, currency: 'Euro (EUR)', language: 'French', flag_emoji: '🇫🇷', landmarks: ['Eiffel Tower'], links: { google_maps: 'https://www.google.com/maps/@48.8566,2.3522,12z', google_earth: 'https://earth.google.com/web/@48.8566,2.3522,0a,20000d,35y,0h,0t,0r' } },
  continent: 'Europe', continent_id: 'europe',
  places: [
    { name: 'Eiffel Tower', type: 'architecture', links: placeLinks('Eiffel Tower') },
    { name: 'Louvre Museum', type: 'museum', links: placeLinks('Louvre Museum') },
    { name: 'Gorges du Verdon', type: 'nature', links: placeLinks('Gorges du Verdon') },
  ],
  cities: [
    { name: 'Paris', is_capital: true, links: { earth_3d: 'https://earth.google.com/web/search/Paris%2C%20France', map: link('map', 'Paris'), video: link('video', 'Paris'), blog: link('blog', 'Paris'), photos: link('photos', 'Paris'), hotels: link('hotels', 'Paris') } },
    { name: 'Lyon', is_capital: false, links: { earth_3d: link('earth', 'Lyon'), map: link('map', 'Lyon'), video: link('video', 'Lyon'), blog: link('blog', 'Lyon'), photos: link('photos', 'Lyon'), hotels: link('hotels', 'Lyon') } },
  ],
  road_trips: [TRIP],
  guide: { tier: '$$$', cost: 'Pricey in Paris.', transport: 'TGV trains link big cities.', stay: 'Hotels and gites.', food: 'Cheese and croissants.', buy: 'Perfume and wine.', warn: 'Pickpockets near major sights.', climate: 'Mild and temperate.' },
  links: { video: link('video', 'France'), blog: link('blog', 'France'), photos: link('photos', 'France'), street_food: link('food', 'France'), wikivoyage: 'https://en.wikivoyage.org/wiki/France', stay_safe: 'https://en.wikivoyage.org/wiki/France#Stay_safe', advisory: link('advisory', 'France'), advisory_uk: 'https://www.gov.uk/foreign-travel-advice', advisory_us: 'https://travel.state.gov/', cost_of_living: 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=France', hotels: link('hotels', 'France') },
  currency_code: 'EUR',
};
const WEATHER = { available: true, place: 'Paris', source: 'Open-Meteo', current: { temperature_c: 12.4, wind_kmh: 9, summary: 'Overcast' }, daily: [{ date: '2026-11-15', min_c: 8, max_c: 14, rain_mm: 2.5, summary: 'Light rain' }] };

function install(overrides = {}) {
  const routes = {
    '/api/virtual-tour': () => ok(OVERVIEW),
    '/api/virtual-tour/countries': () => ok({ countries: COUNTRIES }),
    '/api/virtual-tour/countries/FR': () => ok(FRANCE),
    '/api/virtual-tour/weather/FR': () => ok(WEATHER),
    '/api/virtual-tour/rates/FR': () => ok({ available: true, currency: 'EUR', per_usd: 0.92, updated: 'Sun, 15 Nov 2026 00:00:01 +0000' }),
    ...overrides,
  };
  global.fetch = vi.fn((url) => {
    const u = String(url);
    if (u.startsWith('/api/museum/thumbnail')) return ok({ thumbnail_url: null });
    if (u.startsWith('/api/virtual-tour/road-trips')) return (routes.roadtrips || (() => ok({ road_trips: [TRIP], total: 1, kinds: ['historic'] })))(u);
    if (u.startsWith('/api/virtual-tour/search')) return (routes.search || (() => ok({ countries: [], places: [], cities: [] })))(u);
    return (routes[u] || (() => fail(404)))(u);
  });
}

beforeEach(() => install());

describe('VirtualTour', () => {
  it('shows the world totals and a card for every country', async () => {
    render(<VirtualTour />);
    expect(await screen.findByText(/2 countries · 5 places/)).toBeInTheDocument();
    expect(screen.getByText(/3 major cities · 1 famous road trips/)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /France/ })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Japan/ })).toBeInTheDocument();
  });

  it('filters countries by continent', async () => {
    render(<VirtualTour />);
    await screen.findByRole('button', { name: /France/ });
    fireEvent.click(screen.getByRole('button', { name: /Asia/ }));
    expect(screen.queryByRole('button', { name: /France/ })).toBeNull();
    expect(screen.getByRole('button', { name: /Japan/ })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: /All \(2\)/ }));
    expect(screen.getByRole('button', { name: /France/ })).toBeInTheDocument();
  });

  it('keeps the world map from the Countries Explorer: a pin per country with Maps and Earth links', async () => {
    const { container } = render(<VirtualTour />);
    await screen.findByRole('button', { name: /France/ });
    fireEvent.click(screen.getByRole('button', { name: '🗺 Map' }));
    expect(screen.getByRole('img', { name: 'World map of country capitals' })).toBeInTheDocument();
    expect(container.querySelectorAll('svg circle[stroke="white"]')).toHaveLength(2);
    fireEvent.click(container.querySelector('svg g.cursor-pointer'));
    expect(screen.getByRole('link', { name: /Google Maps/ })).toHaveAttribute('href', 'https://www.google.com/maps/@48.8566,2.3522,6z');
    expect(screen.getByRole('link', { name: /Google Earth/ })).toHaveAttribute('href', expect.stringContaining('https://earth.google.com/web/@48.8566,2.3522'));
    fireEvent.click(screen.getByRole('button', { name: /Open Virtual Tour/ }));
    expect((await screen.findAllByRole('heading', { name: 'France' }))[0]).toBeInTheDocument();
  });

  it('country page: places have video, blog and photo links and can be filtered by kind', async () => {
    render(<VirtualTour />);
    fireEvent.click(await screen.findByRole('button', { name: /France/ }));
    expect((await screen.findAllByRole('heading', { name: 'France' }))[0]).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /Country video tour/ })).toHaveAttribute('href', link('video', 'France'));
    fireEvent.click(screen.getByRole('button', { name: /Places to visit \(3\)/ }));

    const eiffel = screen.getByRole('heading', { name: 'Eiffel Tower' }).closest('li');
    expect(within(eiffel).getByRole('link', { name: /Video/ })).toHaveAttribute('href', link('video', 'Eiffel Tower'));
    expect(within(eiffel).getByRole('link', { name: /Blog/ })).toHaveAttribute('href', link('blog', 'Eiffel Tower'));
    expect(within(eiffel).getByRole('link', { name: /Photos/ })).toHaveAttribute('href', link('photos', 'Eiffel Tower'));
    expect(within(eiffel).getByRole('link', { name: /3D/ })).toHaveAttribute('href', link('earth', 'Eiffel Tower'));

    fireEvent.click(screen.getByRole('button', { name: /Museums \(1\)/ }));
    expect(screen.getByRole('heading', { name: 'Louvre Museum' })).toBeInTheDocument();
    expect(screen.queryByRole('heading', { name: 'Eiffel Tower' })).toBeNull();
    fireEvent.click(screen.getByRole('button', { name: /Natural wonders \(1\)/ }));
    expect(screen.getByRole('heading', { name: 'Gorges du Verdon' })).toBeInTheDocument();
  });

  it('country page: major cities have a 3D Google Earth tour, video, blog, photos and hotels', async () => {
    render(<VirtualTour />);
    fireEvent.click(await screen.findByRole('button', { name: /France/ }));
    (await screen.findAllByRole('heading', { name: 'France' }))[0];
    fireEvent.click(screen.getByRole('button', { name: /Major cities \(2\)/ }));
    const paris = screen.getByRole('heading', { name: /Paris/ }).closest('li');
    expect(within(paris).getByText('Capital')).toBeInTheDocument();
    expect(within(paris).getByRole('link', { name: /3D city tour/ })).toHaveAttribute('href', 'https://earth.google.com/web/search/Paris%2C%20France');
    expect(within(paris).getByRole('link', { name: /Walking tour video/ })).toHaveAttribute('href', link('video', 'Paris'));
    expect(within(paris).getByRole('link', { name: /Hotels/ })).toHaveAttribute('href', link('hotels', 'Paris'));
  });

  it('country page: the travel guide covers every topic and shows live weather and the exchange rate', async () => {
    render(<VirtualTour />);
    fireEvent.click(await screen.findByRole('button', { name: /France/ }));
    (await screen.findAllByRole('heading', { name: 'France' }))[0];
    fireEvent.click(screen.getByRole('button', { name: 'Travel guide' }));
    for (const heading of [/Weather in France/, /^💰 Cost/, /Getting around/, /Where to stay/, /Food to try/, /What to buy/, /Common warnings/]) {
      expect(screen.getByRole('heading', { name: heading })).toBeInTheDocument();
    }
    expect(screen.getByText('TGV trains link big cities.')).toBeInTheDocument();
    expect(screen.getByText('Pickpockets near major sights.')).toBeInTheDocument();
    expect(await screen.findByText(/12°C/)).toBeInTheDocument();
    expect(screen.getByText(/in Paris now · Overcast/)).toBeInTheDocument();
    expect(await screen.findByText(/1 US dollar ≈ 0\.9200 EUR/)).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /Latest travel advisories/ })).toHaveAttribute('href', link('advisory', 'France'));
    expect(screen.getByRole('link', { name: /Find hotels/ })).toHaveAttribute('href', link('hotels', 'France'));
  });

  it('the guide still works when live weather and rates are unavailable', async () => {
    install({ '/api/virtual-tour/weather/FR': () => ok({ available: false }), '/api/virtual-tour/rates/FR': () => fail(500) });
    render(<VirtualTour />);
    fireEvent.click(await screen.findByRole('button', { name: /France/ }));
    (await screen.findAllByRole('heading', { name: 'France' }))[0];
    fireEvent.click(screen.getByRole('button', { name: 'Travel guide' }));
    expect(await screen.findByText('Live weather is not available right now.')).toBeInTheDocument();
    expect(screen.queryByText(/1 US dollar/)).toBeNull();
    expect(screen.getByText('Mild and temperate.')).toBeInTheDocument();
  });

  it('country page: road trips with a Google Maps route, video, blog and photos', async () => {
    render(<VirtualTour />);
    fireEvent.click(await screen.findByRole('button', { name: /France/ }));
    (await screen.findAllByRole('heading', { name: 'France' }))[0];
    fireEvent.click(screen.getByRole('button', { name: /Road trips \(1\)/ }));
    const card = screen.getByRole('heading', { name: /Route Napoleon/ }).closest('li');
    expect(within(card).getByText(/Golfe-Juan → Grenoble/)).toBeInTheDocument();
    expect(within(card).getByRole('link', { name: /Route in Google Maps/ })).toHaveAttribute('href', 'https://maps.example/route');
    expect(within(card).getByRole('link', { name: /Drive video/ })).toBeInTheDocument();
    expect(within(card).getByRole('link', { name: /Blog/ })).toBeInTheDocument();
    expect(within(card).getByRole('link', { name: /Photos/ })).toBeInTheDocument();
    expect(within(card).getByText('about 325 km')).toBeInTheDocument();
  });

  it('Road trips view lists trips and passes the continent filter to the API', async () => {
    render(<VirtualTour />);
    await screen.findByRole('button', { name: /France/ });
    fireEvent.click(screen.getByRole('button', { name: /Europe/ }));
    fireEvent.click(screen.getByRole('button', { name: /🚗 Road trips/ }));
    expect(await screen.findByRole('heading', { name: /Route Napoleon/ })).toBeInTheDocument();
    const calls = global.fetch.mock.calls.map((c) => String(c[0]));
    expect(calls.some((u) => u.startsWith('/api/virtual-tour/road-trips') && u.includes('continent=europe'))).toBe(true);
    fireEvent.click(screen.getByRole('button', { name: /Tour France/ }));
    expect((await screen.findAllByRole('heading', { name: 'France' }))[0]).toBeInTheDocument();
  });

  it('global search shows matching places and opens their country', async () => {
    install({
      search: () => ok({
        countries: [], cities: [],
        places: [{ name: 'Louvre Museum', type: 'museum', country: 'France', country_code: 'FR', links: placeLinks('Louvre Museum') }],
      }),
    });
    render(<VirtualTour />);
    await screen.findByRole('button', { name: /France/ });
    fireEvent.change(screen.getByLabelText('Search the Virtual Tour'), { target: { value: 'louvre' } });
    expect(await screen.findByRole('heading', { name: 'Louvre Museum' })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: /More in France/ }));
    expect((await screen.findAllByRole('heading', { name: 'France' }))[0]).toBeInTheDocument();
  });

  it('reports errors instead of loading forever', async () => {
    install({ '/api/virtual-tour': () => fail(500) });
    const { unmount } = render(<VirtualTour />);
    expect((await screen.findByRole('alert')).textContent).toMatch(/Could not load the Virtual Tour/);
    unmount();

    install({ '/api/virtual-tour/countries/FR': () => fail(500) });
    render(<VirtualTour />);
    fireEvent.click(await screen.findByRole('button', { name: /France/ }));
    expect((await screen.findByRole('alert')).textContent).toMatch(/Could not load this country/);
    fireEvent.click(screen.getByRole('button', { name: /Back to the Virtual Tour/ }));
    await waitFor(() => expect(screen.getByRole('button', { name: /France/ })).toBeInTheDocument());
  });
});
