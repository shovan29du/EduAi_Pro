import React, { useEffect, useState } from 'react';
import { SpeakButton } from '../utils/tts.jsx';

const API_URL = '/api/art-of-the-day';

export default function ArtOfTheDay() {
  const [piece, setPiece] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);
    fetch(API_URL)
      .then((res) => {
        if (!res.ok) throw new Error('Could not load art of the day right now.');
        return res.json();
      })
      .then((data) => {
        if (data && data.title) setPiece(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <section
      aria-label="Art of the day"
      className="rounded border bg-rose-50 p-4 dark:border-gray-700 dark:bg-gray-800"
    >
      <h2 className="mb-2 text-lg font-bold">🖼️ Art of the Day</h2>
      {loading && <p className="text-sm text-gray-600 dark:text-gray-300">Loading…</p>}
      {error && <p role="alert" className="text-red-600">{error}</p>}
      {piece && (
        <>
          <div className="flex items-start gap-2">
            <p className="font-medium flex-1">{piece.title.replace(/^Famous (Painting|Photograph|Sculpture): /, '')}</p>
            <SpeakButton text={`${piece.title}. ${piece.fact}`} lang="en" />
          </div>
          <p className="text-sm text-gray-700 dark:text-gray-300">{piece.fact}</p>
        </>
      )}
      <p className="mt-3 text-xs text-gray-500 dark:text-gray-400">
        A different famous painting, photograph, or sculpture each day.
      </p>
    </section>
  );
}
