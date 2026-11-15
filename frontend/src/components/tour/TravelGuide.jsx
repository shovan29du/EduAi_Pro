import React, { useEffect, useState } from 'react';
import { getExchangeRate, getLiveWeather } from '../../api/virtualTour.js';
import { LinkChip } from './TourBits.jsx';

export const TIERS = {
  $: { label: 'Budget', detail: 'roughly under US$50 a day' },
  $$: { label: 'Moderate', detail: 'about US$50-120 a day' },
  $$$: { label: 'High', detail: 'about US$120-250 a day' },
  $$$$: { label: 'Very high', detail: 'over US$250 a day' },
};

function Section({ icon, title, children }) {
  return (
    <section className="rounded-xl border bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
      <h4 className="mb-1 font-semibold">{icon} {title}</h4>
      {children}
    </section>
  );
}

export function LiveWeather({ code }) {
  const [state, setState] = useState({ status: 'loading' });

  useEffect(() => {
    let active = true;
    setState({ status: 'loading' });
    getLiveWeather(code)
      .then((data) => { if (active) setState(data.available ? { status: 'ok', data } : { status: 'unavailable' }); })
      .catch(() => { if (active) setState({ status: 'unavailable' }); });
    return () => { active = false; };
  }, [code]);

  if (state.status === 'loading') return <p className="text-sm text-gray-500">Loading live weather…</p>;
  if (state.status === 'unavailable') return <p className="text-sm text-gray-500">Live weather is not available right now.</p>;
  const { data } = state;
  return (
    <div className="space-y-2" aria-label="Live weather">
      <p className="text-sm">
        <span className="text-2xl font-bold">{Math.round(data.current.temperature_c)}°C</span>{' '}
        in {data.place} now · {data.current.summary} · wind {Math.round(data.current.wind_kmh)} km/h
      </p>
      <ul className="grid gap-1 text-xs sm:grid-cols-7">
        {data.daily.map((day) => (
          <li key={day.date} className="rounded-lg bg-gray-50 p-2 text-center dark:bg-gray-800">
            <p className="font-medium">{new Date(`${day.date}T12:00:00`).toLocaleDateString(undefined, { weekday: 'short', day: 'numeric' })}</p>
            <p>{Math.round(day.max_c)}° / {Math.round(day.min_c)}°</p>
            <p className="text-gray-500">{day.summary}</p>
            {day.rain_mm > 0 && <p className="text-blue-600">{day.rain_mm} mm</p>}
          </li>
        ))}
      </ul>
      <p className="text-[11px] text-gray-400">Live forecast from {data.source}.</p>
    </div>
  );
}

export function LiveRate({ code }) {
  const [rate, setRate] = useState(null);

  useEffect(() => {
    let active = true;
    setRate(null);
    getExchangeRate(code)
      .then((data) => { if (active && data.available) setRate(data); })
      .catch(() => {});
    return () => { active = false; };
  }, [code]);

  if (!rate) return null;
  const value = rate.per_usd >= 100 ? Math.round(rate.per_usd).toLocaleString() : Number(rate.per_usd).toPrecision(4);
  return (
    <p className="mt-2 rounded-lg bg-emerald-50 p-2 text-sm text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200">
      💱 Today: <strong>1 US dollar ≈ {value} {rate.currency}</strong>
      {rate.updated && <span className="text-xs text-emerald-700"> (rates updated {rate.updated.replace(/ \+0000$/, '')})</span>}
    </p>
  );
}

export default function TravelGuide({ guide, links, code, countryName }) {
  if (!guide) return <p className="text-gray-500">No travel guide is available for this country yet.</p>;
  const tier = TIERS[guide.tier] || TIERS.$$;
  return (
    <div className="space-y-3">
      <p className="rounded-lg border border-amber-200 bg-amber-50 p-3 text-xs text-amber-900 dark:border-amber-800 dark:bg-amber-950 dark:text-amber-200">
        This guide was last reviewed in November 2026. Prices, entry rules and safety advice change, so use the live
        weather, exchange rate and official advice links below to check the latest before you travel.
      </p>

      <Section icon="🌤️" title={`Weather in ${countryName}`}>
        <p className="mb-2 text-sm text-gray-700 dark:text-gray-300">{guide.climate}</p>
        <LiveWeather code={code} />
      </Section>

      <Section icon="💰" title="Cost">
        <p className="text-sm">
          <span className="mr-2 rounded-full bg-emerald-600 px-2 py-0.5 text-xs font-bold text-white" aria-label={`Cost level ${tier.label}`}>{guide.tier}</span>
          <strong>{tier.label}</strong> ({tier.detail}, comfortable solo traveller, excluding flights)
        </p>
        <p className="mt-1 text-sm text-gray-700 dark:text-gray-300">{guide.cost}</p>
        <LiveRate code={code} />
        <div className="mt-2 flex flex-wrap gap-1.5">
          <LinkChip href={links.cost_of_living} kind="map" icon="📊">Cost of living (Numbeo)</LinkChip>
        </div>
      </Section>

      <Section icon="🚆" title="Getting around">
        <p className="text-sm text-gray-700 dark:text-gray-300">{guide.transport}</p>
      </Section>

      <Section icon="🏨" title="Where to stay">
        <p className="text-sm text-gray-700 dark:text-gray-300">{guide.stay}</p>
        <div className="mt-2 flex flex-wrap gap-1.5">
          <LinkChip href={links.hotels} kind="hotels" icon="🏨">Find hotels (Booking.com)</LinkChip>
        </div>
      </Section>

      <Section icon="🍽️" title="Food to try">
        <p className="text-sm text-gray-700 dark:text-gray-300">{guide.food}</p>
        <div className="mt-2 flex flex-wrap gap-1.5">
          <LinkChip href={links.street_food} kind="video" icon="▶">Street food videos</LinkChip>
        </div>
      </Section>

      <Section icon="🛍️" title="What to buy">
        <p className="text-sm text-gray-700 dark:text-gray-300">{guide.buy}</p>
      </Section>

      <Section icon="⚠️" title="Common warnings">
        <p className="text-sm text-gray-700 dark:text-gray-300">{guide.warn}</p>
        <p className="mt-2 text-xs text-gray-500">Always check current official advice for {countryName}:</p>
        <div className="mt-1 flex flex-wrap gap-1.5">
          <LinkChip href={links.advisory} kind="blog" icon="🔎">Latest travel advisories</LinkChip>
          <LinkChip href={links.advisory_uk} kind="map" icon="🇬🇧">UK travel advice</LinkChip>
          <LinkChip href={links.advisory_us} kind="map" icon="🇺🇸">US travel advisories</LinkChip>
          <LinkChip href={links.stay_safe} kind="map" icon="🛡️">Stay safe (Wikivoyage)</LinkChip>
        </div>
      </Section>
    </div>
  );
}
