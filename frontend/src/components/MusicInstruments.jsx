import { useState, useEffect } from 'react';
import { fetchSafeMusic } from '../api/safety.js';
import { isResourceSafe } from '../utils/safetyFilter.js';
import { useChild } from '../contexts/ChildContext.jsx';

const API = '/api/music-instruments';

function SafeMusicPlayer() {
  const { isRestricted } = useChild();
  const [songs, setSongs] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchSafeMusic()
      .then(setSongs)
      .catch((err) => setError(err.message));
  }, []);

  const visible = songs.filter((s) => !isRestricted || isResourceSafe(s));

  return (
    <section aria-label="Safe music library" className="mb-8 rounded border p-4 dark:border-gray-700">
      <h2 className="mb-3 text-lg font-semibold">🎧 Safe Music Library</h2>
      {error && <p role="alert" className="text-red-600">{error}</p>}
      {!error && visible.length === 0 && (
        <p className="text-gray-600 dark:text-gray-400">No songs available.</p>
      )}
      <ul className="space-y-3">
        {visible.map((song, i) => (
          <li key={i} className="rounded border p-3 dark:border-gray-700">
            <a
              href={song.videoUrl || song.audioUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="font-medium text-blue-600 hover:underline dark:text-blue-400"
            >
              {song.title}
            </a>
            {song.description && (
              <p className="text-sm text-gray-700 dark:text-gray-300">{song.description}</p>
            )}
            {song.source && (
              <p className="text-sm text-gray-600 dark:text-gray-400">{song.source}</p>
            )}
          </li>
        ))}
      </ul>
    </section>
  );
}

function LessonList({ title, lessons }) {
  if (!lessons?.length) return null;
  return (
    <div className="mb-4">
      <h4 className="font-semibold text-gray-700 dark:text-gray-200 mb-2">{title}</h4>
      <ul className="space-y-2">
        {lessons.map((lesson, i) => (
          <li key={i} className="rounded-lg border p-3 dark:border-gray-700">
            <p className="font-medium text-sm">{lesson.title}</p>
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">{lesson.description}</p>
            <a
              href={lesson.youtube_search_url}
              target="_blank"
              rel="noreferrer"
              className="mt-1 inline-block text-xs text-blue-600 hover:underline dark:text-blue-400"
            >
              ▶ Find lessons on YouTube
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

function InstrumentDetail({ instrumentId, onBack }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`${API}/instrument/${instrumentId}`)
      .then((r) => r.json())
      .then(setData);
  }, [instrumentId]);

  if (!data) return <div className="p-4 text-gray-500">Loading…</div>;

  return (
    <div>
      <button onClick={onBack} className="mb-3 text-sm text-blue-600 hover:underline dark:text-blue-400">
        ← Back to instruments
      </button>
      <div className="flex items-center gap-3 mb-4">
        <span className="text-4xl">{data.emoji}</span>
        <h2 className="text-2xl font-bold">{data.label}</h2>
      </div>

      <LessonList title="🌱 Beginner Lessons" lessons={data.beginner} />
      <LessonList title="🌿 Intermediate Lessons" lessons={data.intermediate} />
      <LessonList title="🌳 Advanced Lessons" lessons={data.advanced} />

      {data.practice_routines?.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-gray-700 dark:text-gray-200 mb-2">🗓️ Practice Routines</h4>
          <ul className="space-y-1 list-disc list-inside text-sm text-gray-600 dark:text-gray-300">
            {data.practice_routines.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>
        </div>
      )}

      {data.youtube_searches?.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-gray-700 dark:text-gray-200 mb-2">🔗 Curated Video Searches</h4>
          <div className="flex flex-wrap gap-2">
            {data.youtube_searches.map((link, i) => (
              <a
                key={i}
                href={link.url}
                target="_blank"
                rel="noreferrer"
                className="rounded-full border px-3 py-1 text-xs hover:bg-gray-50 dark:border-gray-600 dark:hover:bg-gray-800"
              >
                {link.title}
              </a>
            ))}
          </div>
        </div>
      )}

      {data.audio_resources?.length > 0 && (
        <div>
          <h4 className="font-semibold text-gray-700 dark:text-gray-200 mb-2">🎧 Audio & Sheet Music Resources</h4>
          <div className="flex flex-wrap gap-2">
            {data.audio_resources.map((link, i) => (
              <a
                key={i}
                href={link.url}
                target="_blank"
                rel="noreferrer"
                className="rounded-full border px-3 py-1 text-xs hover:bg-gray-50 dark:border-gray-600 dark:hover:bg-gray-800"
              >
                {link.title}
              </a>
            ))}
          </div>
        </div>
      )}

      {data.pinterest_search && (
        <a
          href={data.pinterest_search}
          target="_blank"
          rel="noreferrer"
          className="mt-3 inline-block rounded-full border px-3 py-1 text-xs hover:bg-gray-50 dark:border-gray-600 dark:hover:bg-gray-800"
        >
          📌 Pinterest — {data.label} charts & diagrams
        </a>
      )}
    </div>
  );
}

function CategoryDetail({ categoryId, onBack }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`${API}/category/${categoryId}`)
      .then((r) => r.json())
      .then(setData);
  }, [categoryId]);

  if (!data) return <div className="p-4 text-gray-500">Loading…</div>;

  return (
    <div>
      <button onClick={onBack} className="mb-3 text-sm text-blue-600 hover:underline dark:text-blue-400">
        ← Back
      </button>
      <div className="flex items-center gap-3 mb-2">
        <span className="text-4xl">{data.emoji}</span>
        <h2 className="text-2xl font-bold">{data.label}</h2>
      </div>
      <p className="text-gray-600 dark:text-gray-300 mb-4">{data.description}</p>

      {data.topics?.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-gray-700 dark:text-gray-200 mb-2">Topics covered</h4>
          <div className="flex flex-wrap gap-2">
            {data.topics.map((t, i) => (
              <span key={i} className="rounded-full bg-gray-100 dark:bg-gray-800 px-3 py-1 text-xs">
                {t}
              </span>
            ))}
          </div>
        </div>
      )}

      {data.resources?.length > 0 && (
        <div>
          <h4 className="font-semibold text-gray-700 dark:text-gray-200 mb-2">Recommended resources</h4>
          <ul className="space-y-1">
            {data.resources.map((r, i) => (
              <li key={i}>
                <a href={r.url} target="_blank" rel="noreferrer" className="text-sm text-blue-600 hover:underline dark:text-blue-400">
                  {r.title}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default function MusicInstruments() {
  const [overview, setOverview] = useState(null);
  const [selectedInstrument, setSelectedInstrument] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState(null);

  useEffect(() => {
    fetch(API)
      .then((r) => r.json())
      .then(setOverview);
  }, []);

  if (!overview) return <div className="p-8 text-center text-gray-500">Loading Music &amp; Instruments…</div>;

  if (selectedInstrument) {
    return (
      <div className="max-w-3xl mx-auto p-4">
        <InstrumentDetail instrumentId={selectedInstrument} onBack={() => setSelectedInstrument(null)} />
      </div>
    );
  }

  if (selectedCategory) {
    return (
      <div className="max-w-3xl mx-auto p-4">
        <CategoryDetail categoryId={selectedCategory} onBack={() => setSelectedCategory(null)} />
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-1">🎵 Music &amp; Instruments</h1>
      <p className="text-gray-500 dark:text-gray-400 mb-6">{overview.description}</p>

      <SafeMusicPlayer />

      <h2 className="text-lg font-semibold mb-2">Learning tracks</h2>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mb-8">
        {overview.categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            className="text-left rounded-xl border-2 p-4 hover:shadow-md transition-shadow dark:border-gray-700"
          >
            <p className="text-2xl mb-1">{cat.emoji}</p>
            <p className="font-bold">{cat.label}</p>
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">{cat.description}</p>
          </button>
        ))}
      </div>

      <h2 className="text-lg font-semibold mb-2">Instruments</h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
        {overview.instruments.map((inst) => (
          <button
            key={inst.id}
            onClick={() => setSelectedInstrument(inst.id)}
            className="text-left rounded-xl border-2 p-4 hover:shadow-md transition-shadow dark:border-gray-700"
          >
            <p className="text-3xl mb-1">{inst.emoji}</p>
            <p className="font-bold text-sm">{inst.label}</p>
          </button>
        ))}
      </div>
    </div>
  );
}
