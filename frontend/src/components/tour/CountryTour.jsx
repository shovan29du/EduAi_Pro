import React, { useEffect, useMemo, useState } from 'react';
import { getCountryTour } from '../../api/virtualTour.js';
import LoadingSpinner from '../LoadingSpinner.jsx';
import { CountryProfile } from '../CountryParts.jsx';
import TravelGuide from './TravelGuide.jsx';
import { CityCard, LinkChip, PLACE_TYPES, PlaceCard, RoadTripCard } from './TourBits.jsx';

const SECTIONS = [
  ['overview', 'Overview'],
  ['places', 'Places to visit'],
  ['cities', 'Major cities'],
  ['roadtrips', 'Road trips'],
  ['guide', 'Travel guide'],
];

function Places({ tour }) {
  const [type, setType] = useState('all');
  const counts = useMemo(() => {
    const result = { all: tour.places.length };
    for (const place of tour.places) result[place.type] = (result[place.type] || 0) + 1;
    return result;
  }, [tour]);
  const shown = type === 'all' ? tour.places : tour.places.filter((p) => p.type === type);
  const country = tour.profile.name.replace(/\s*\([^)]*\)/, '');

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap gap-2" role="group" aria-label="Filter places">
        {['all', ...Object.keys(PLACE_TYPES)].filter((t) => t === 'all' || counts[t]).map((t) => (
          <button
            key={t}
            type="button"
            aria-pressed={type === t}
            onClick={() => setType(t)}
            className={`rounded-full border px-3 py-1 text-sm ${type === t ? 'border-blue-600 bg-blue-600 text-white' : 'bg-white hover:bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700'}`}
          >
            {t === 'all' ? 'All places' : `${PLACE_TYPES[t].emoji} ${PLACE_TYPES[t].label}`} ({counts[t]})
          </button>
        ))}
      </div>
      <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {shown.map((place) => <PlaceCard key={place.name} place={place} country={country} />)}
      </ul>
    </div>
  );
}

export default function CountryTour({ code, onBack, backLabel = '← All countries' }) {
  const [tour, setTour] = useState(null);
  const [error, setError] = useState(null);
  const [section, setSection] = useState('overview');

  useEffect(() => {
    let active = true;
    setTour(null);
    setError(null);
    setSection('overview');
    getCountryTour(code)
      .then((data) => { if (active) setTour(data); })
      .catch(() => { if (active) setError('Could not load this country right now. Please try again.'); });
    return () => { active = false; };
  }, [code]);

  if (error) {
    return (
      <div className="space-y-3">
        <button type="button" onClick={onBack} className="text-sm text-blue-600 hover:underline">{backLabel}</button>
        <p className="rounded-lg bg-red-50 p-3 text-sm text-red-700" role="alert">{error}</p>
      </div>
    );
  }
  if (!tour) return <LoadingSpinner />;

  const { profile } = tour;
  const name = profile.name.replace(/\s*\([^)]*\)/, '');
  const counts = { places: tour.places.length, cities: tour.cities.length, roadtrips: tour.road_trips.length };

  return (
    <div className="space-y-4">
      <button type="button" onClick={onBack} className="text-sm text-blue-600 hover:underline">{backLabel}</button>
      <header className="flex flex-wrap items-center gap-3 rounded-xl bg-gradient-to-r from-blue-600 to-cyan-500 p-4 text-white">
        <span className="text-4xl" aria-hidden="true">{profile.flag_emoji}</span>
        <div className="min-w-0 flex-1">
          <h2 className="text-2xl font-bold">{profile.name}</h2>
          <p className="text-sm opacity-90">{tour.continent} · Capital {profile.capital}</p>
        </div>
        <div className="flex flex-wrap gap-1.5">
          <LinkChip href={tour.links.video} kind="video" icon="▶">Country video tour</LinkChip>
          <LinkChip href={tour.links.blog} kind="blog" icon="📝">Travel blogs</LinkChip>
          <LinkChip href={tour.links.photos} kind="photos" icon="📷">Photos</LinkChip>
        </div>
      </header>

      <nav className="flex flex-wrap gap-2" aria-label="Country sections">
        {SECTIONS.map(([id, label]) => (
          <button
            key={id}
            type="button"
            aria-pressed={section === id}
            onClick={() => setSection(id)}
            className={`rounded-lg border px-3 py-1.5 text-sm font-medium ${section === id ? 'border-blue-600 bg-blue-600 text-white' : 'bg-white hover:bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700'}`}
          >
            {label}{counts[id] !== undefined ? ` (${counts[id]})` : ''}
          </button>
        ))}
      </nav>

      {section === 'overview' && (
        <div className="space-y-3">
          <CountryProfile country={{ ...profile, continent: tour.continent }} />
          <p className="text-xs text-gray-500">
            More: <a className="underline" href={tour.links.wikivoyage} target="_blank" rel="noopener noreferrer">Wikivoyage travel guide</a>
          </p>
        </div>
      )}
      {section === 'places' && <Places tour={tour} />}
      {section === 'cities' && (
        <ul className="grid gap-3 sm:grid-cols-2">
          {tour.cities.map((city) => <CityCard key={city.name} city={city} />)}
        </ul>
      )}
      {section === 'roadtrips' && (
        tour.road_trips.length
          ? <ul className="grid gap-3 lg:grid-cols-2">{tour.road_trips.map((trip) => <RoadTripCard key={trip.id} trip={trip} />)}</ul>
          : <p className="text-gray-500">No famous road trips are listed for {name} yet. Browse the Road Trips view for trips elsewhere.</p>
      )}
      {section === 'guide' && <TravelGuide guide={tour.guide} links={tour.links} code={profile.code} countryName={name} />}
    </div>
  );
}
