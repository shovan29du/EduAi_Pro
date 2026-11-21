import React, { useEffect, useMemo, useState } from 'react';
import LoadingSpinner from './LoadingSpinner.jsx';
import { WorldMap } from './CountryParts.jsx';
import CountryTour from './tour/CountryTour.jsx';
import { CityCard, PlaceCard, RoadTripCard } from './tour/TourBits.jsx';
import { getRoadTrips, getTourCountries, getTourOverview, searchTour } from '../api/virtualTour.js';

const VIEWS = [['explore', '🌍 Explore'], ['map', '🗺 Map'], ['roadtrips', '🚗 Road trips']];

function useDebounced(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);
  return debounced;
}

function CountryButton({ country, onOpen }) {
  return (
    <button
      type="button"
      onClick={() => onOpen(country.code)}
      className="flex items-center gap-3 rounded-xl border bg-white p-3 text-left shadow-sm transition hover:border-blue-400 dark:bg-gray-900"
    >
      <span className="text-2xl" aria-hidden="true">{country.flag_emoji}</span>
      <div className="min-w-0 flex-1">
        <p className="truncate font-medium">{country.name}</p>
        <p className="truncate text-xs text-gray-500">{country.capital} · {country.place_count} places</p>
      </div>
    </button>
  );
}

function SearchResults({ query, onOpen }) {
  const [state, setState] = useState({ status: 'loading' });

  useEffect(() => {
    let active = true;
    setState({ status: 'loading' });
    searchTour(query)
      .then((data) => { if (active) setState({ status: 'ok', data }); })
      .catch(() => { if (active) setState({ status: 'error' }); });
    return () => { active = false; };
  }, [query]);

  if (state.status === 'loading') return <p className="text-sm text-gray-500">Searching…</p>;
  if (state.status === 'error') return <p className="text-sm text-red-600" role="alert">Search is unavailable right now. Please try again.</p>;
  const { countries, places, cities } = state.data;
  if (!countries.length && !places.length && !cities.length) {
    return <p className="text-sm text-gray-500">Nothing matched “{query}”.</p>;
  }
  return (
    <div className="space-y-4">
      {countries.length > 0 && (
        <section>
          <h3 className="mb-2 font-semibold">Countries</h3>
          <div className="grid gap-2 sm:grid-cols-2 md:grid-cols-3">{countries.map((c) => <CountryButton key={c.code} country={c} onOpen={onOpen} />)}</div>
        </section>
      )}
      {places.length > 0 && (
        <section>
          <h3 className="mb-2 font-semibold">Places</h3>
          <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {places.map((p) => (
              <div key={`${p.country_code}-${p.name}`} className="space-y-1">
                <PlaceCard place={p} country={p.country.replace(/\s*\([^)]*\)/, '')} />
                <button type="button" onClick={() => onOpen(p.country_code)} className="text-xs text-blue-600 hover:underline">More in {p.country} →</button>
              </div>
            ))}
          </ul>
        </section>
      )}
      {cities.length > 0 && (
        <section>
          <h3 className="mb-2 font-semibold">Cities</h3>
          <ul className="grid gap-3 sm:grid-cols-2">
            {cities.map((c) => (
              <div key={`${c.country_code}-${c.name}`} className="space-y-1">
                <CityCard city={c} />
                <button type="button" onClick={() => onOpen(c.country_code)} className="text-xs text-blue-600 hover:underline">More in {c.country} →</button>
              </div>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}

function RoadTrips({ continent, onOpenCountry }) {
  const [kind, setKind] = useState('');
  const [text, setText] = useState('');
  const query = useDebounced(text);
  const [state, setState] = useState({ status: 'loading' });

  useEffect(() => {
    let active = true;
    setState((prev) => ({ ...prev, status: 'loading' }));
    getRoadTrips({ continent: continent === 'all' ? '' : continent, kind, q: query })
      .then((data) => { if (active) setState({ status: 'ok', data }); })
      .catch(() => { if (active) setState({ status: 'error' }); });
    return () => { active = false; };
  }, [continent, kind, query]);

  const kinds = state.data?.kinds || [];
  return (
    <div className="space-y-3">
      <div className="flex flex-col gap-2 sm:flex-row">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          aria-label="Search road trips"
          placeholder="Search road trips, places or countries…"
          className="flex-1 rounded-lg border px-3 py-2 dark:bg-gray-800"
        />
        <select value={kind} onChange={(e) => setKind(e.target.value)} aria-label="Road trip type" className="rounded-lg border px-3 py-2 capitalize dark:bg-gray-800">
          <option value="">All types</option>
          {kinds.map((k) => <option key={k} value={k}>{k}</option>)}
        </select>
      </div>
      {state.status === 'error' && <p className="text-sm text-red-600" role="alert">Could not load road trips right now. Please try again.</p>}
      {state.status === 'loading' && !state.data && <LoadingSpinner />}
      {state.data && (
        <>
          <p className="text-xs text-gray-500">{state.data.total} road trips</p>
          {state.data.road_trips.length === 0 && <p className="py-6 text-center text-gray-500">No road trips match.</p>}
          <ul className="grid gap-3 lg:grid-cols-2">
            {state.data.road_trips.map((trip) => (
              <div key={trip.id} className="space-y-1">
                <RoadTripCard trip={trip} />
                <p className="flex flex-wrap gap-2 text-xs">
                  {trip.countries.map((code, i) => (
                    <button key={code} type="button" onClick={() => onOpenCountry(code)} className="text-blue-600 hover:underline">
                      Tour {trip.country_names[i] || code}
                    </button>
                  ))}
                </p>
              </div>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default function VirtualTour() {
  const [overview, setOverview] = useState(null);
  const [countries, setCountries] = useState([]);
  const [error, setError] = useState(null);
  const [view, setView] = useState('explore');
  const [continent, setContinent] = useState('all');
  const [search, setSearch] = useState('');
  const [selectedCode, setSelectedCode] = useState(null);
  const [pinCode, setPinCode] = useState(null);
  const query = useDebounced(search.trim());

  useEffect(() => {
    let active = true;
    Promise.all([getTourOverview(), getTourCountries()])
      .then(([o, c]) => { if (active) { setOverview(o); setCountries(c.countries); } })
      .catch(() => { if (active) setError('Could not load the Virtual Tour. Make sure the app server is running, then try again.'); });
    return () => { active = false; };
  }, []);

  const continentLabel = useMemo(
    () => Object.fromEntries((overview?.continents || []).map((c) => [c.id, c.label])),
    [overview],
  );
  const visible = useMemo(
    () => countries.filter((c) => continent === 'all' || c.continent_id === continent),
    [countries, continent],
  );
  const mapCountries = useMemo(
    () => visible.filter((c) => c.coordinates).map((c) => ({
      ...c,
      continent: continentLabel[c.continent_id],
      links: {
        google_maps: `https://www.google.com/maps/@${c.coordinates.lat},${c.coordinates.lng},6z`,
        google_earth: `https://earth.google.com/web/@${c.coordinates.lat},${c.coordinates.lng},0a,2000000d,35y,0h,0t,0r`,
      },
    })),
    [visible, continentLabel],
  );
  const pinned = pinCode ? mapCountries.find((c) => c.code === pinCode) || null : null;

  if (error) return <p className="rounded-lg bg-red-50 p-4 text-red-700" role="alert">{error}</p>;
  if (!overview) return <LoadingSpinner />;

  if (selectedCode) {
    return <CountryTour code={selectedCode} onBack={() => setSelectedCode(null)} backLabel="← Back to the Virtual Tour" />;
  }

  const open = (code) => { setSelectedCode(code); setPinCode(null); };
  const totals = overview.totals;
  const searching = query.length >= 2;

  return (
    <div className="space-y-4">
      <div className="rounded-xl bg-gradient-to-r from-blue-600 to-cyan-500 p-4 text-white">
        <h2 className="text-xl font-bold">🌍 Virtual Tour</h2>
        <p className="text-sm opacity-90">
          Travel the world from your screen: {totals.countries} countries · {totals.places.toLocaleString()} places ·
          {' '}{totals.cities} major cities · {totals.road_trips} famous road trips. Every place has a video, a blog and photos,
          and every country has a travel guide.
        </p>
      </div>

      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        aria-label="Search the Virtual Tour"
        placeholder="Search a country, city, landmark, museum or natural wonder…"
        className="w-full rounded-lg border px-3 py-2 dark:bg-gray-800"
      />

      {searching ? (
        <SearchResults query={query} onOpen={open} />
      ) : (
        <>
          <div className="flex flex-wrap items-center gap-2">
            <div className="flex overflow-hidden rounded-lg border" role="group" aria-label="View">
              {VIEWS.map(([id, label]) => (
                <button
                  key={id}
                  type="button"
                  aria-pressed={view === id}
                  onClick={() => setView(id)}
                  className={`px-3 py-2 text-sm font-medium ${view === id ? 'bg-blue-600 text-white' : 'bg-white dark:bg-gray-800'}`}
                >
                  {label}
                </button>
              ))}
            </div>
          </div>

          <div className="flex flex-wrap gap-2" role="group" aria-label="Continent">
            <button
              type="button"
              aria-pressed={continent === 'all'}
              onClick={() => setContinent('all')}
              className={`rounded-full border px-3 py-1 text-sm ${continent === 'all' ? 'border-blue-600 bg-blue-600 text-white' : 'bg-white hover:bg-gray-100 dark:bg-gray-800'}`}
            >
              🌐 All ({totals.countries})
            </button>
            {overview.continents.map((c) => (
              <button
                key={c.id}
                type="button"
                aria-pressed={continent === c.id}
                onClick={() => { setContinent(c.id); setPinCode(null); }}
                className={`rounded-full border px-3 py-1 text-sm ${continent === c.id ? 'border-blue-600 bg-blue-600 text-white' : 'bg-white hover:bg-gray-100 dark:bg-gray-800'}`}
              >
                {c.emoji} {c.label} ({view === 'roadtrips' ? c.road_trip_count : c.country_count})
              </button>
            ))}
          </div>

          {view === 'explore' && (
            <>
              <p className="text-xs text-gray-500">{visible.length} countries</p>
              <div className="grid gap-2 sm:grid-cols-2 md:grid-cols-3">
                {visible.map((c) => <CountryButton key={c.code} country={c} onOpen={open} />)}
              </div>
            </>
          )}

          {view === 'map' && (
            <>
              <p className="text-xs text-gray-500">{visible.length} countries</p>
              <WorldMap
                countries={mapCountries}
                pinCode={pinCode}
                setPinCode={setPinCode}
                pinnedCountry={pinned}
                onOpenDetail={open}
              />
            </>
          )}

          {view === 'roadtrips' && <RoadTrips continent={continent} onOpenCountry={open} />}
        </>
      )}
    </div>
  );
}

