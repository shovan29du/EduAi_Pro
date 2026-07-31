import { useState, useEffect, useRef, useCallback } from 'react';
import CMACollection from './CMACollection.jsx';
import FavoriteButton from './FavoriteButton.jsx';
import { useChild } from '../contexts/ChildContext.jsx';
import { postProgress } from '../api/progress.js';
import './VirtualMuseum.css';

const API = '/api';
export const MUSEUM_DESIGN_VERSION = 'open-museum-v1';

// Category → emoji fallback for when Wikipedia thumbnail isn't available
const CAT_EMOJI = {
  painting: '🖼️', sculpture: '🗿', architecture: '🏛️', archaeology: '🏺',
  manuscript: '📜', fossil: '🦕', palaeontology: '🦴', technology: '⚙️',
  engineering: '🔧', astronomy: '🔭', ceremonial: '🪬', jewelry: '💎',
  'ritual object': '🪬', textile: '🧵', weapon: '⚔️', coin: '🪙',
  instrument: '🎵', map: '🗺️', default: '🏛️',
};
function catEmoji(cat) {
  if (!cat) return CAT_EMOJI.default;
  const key = cat.toLowerCase();
  return Object.entries(CAT_EMOJI).find(([k]) => key.includes(k))?.[1] ?? CAT_EMOJI.default;
}

// Soft pastel tile backgrounds (Google Arts & Culture-style colour-block
// placeholders for objects that don't have a photo loaded yet).
const TILE_COLORS = [
  'from-rose-100 to-rose-200', 'from-amber-100 to-amber-200', 'from-emerald-100 to-emerald-200',
  'from-sky-100 to-sky-200', 'from-violet-100 to-violet-200', 'from-fuchsia-100 to-fuchsia-200',
  'from-lime-100 to-lime-200', 'from-cyan-100 to-cyan-200', 'from-orange-100 to-orange-200',
  'from-indigo-100 to-indigo-200',
];
function tileColor(key) {
  let hash = 0;
  for (const c of key || '') hash = (hash * 31 + c.charCodeAt(0)) >>> 0;
  return TILE_COLORS[hash % TILE_COLORS.length];
}

// ── Museum quiz score tracking ──────────────────────────────────────────────
// A running "N/M correct this session" score, kept in sessionStorage (per
// child, cleared when the browser session ends) and broadcast via a custom
// window event so the score badge and the quiz itself stay in sync without
// prop-drilling through GalleryView/SearchView/ObjectDetail.
const QUIZ_STATS_EVENT = 'museum-quiz-stats-changed';
function quizStatsKey(child) {
  return `museum_quiz_stats_${child}`;
}
function readQuizStats(child) {
  try {
    return JSON.parse(sessionStorage.getItem(quizStatsKey(child))) || { correct: 0, total: 0 };
  } catch {
    return { correct: 0, total: 0 };
  }
}
function useMuseumQuizStats() {
  const { child } = useChild();
  const [stats, setStats] = useState(() => readQuizStats(child));
  useEffect(() => {
    setStats(readQuizStats(child));
    const handle = () => setStats(readQuizStats(child));
    window.addEventListener(QUIZ_STATS_EVENT, handle);
    return () => window.removeEventListener(QUIZ_STATS_EVENT, handle);
  }, [child]);
  const recordAnswer = useCallback((correct) => {
    const prev = readQuizStats(child);
    const next = { correct: prev.correct + (correct ? 1 : 0), total: prev.total + 1 };
    sessionStorage.setItem(quizStatsKey(child), JSON.stringify(next));
    window.dispatchEvent(new Event(QUIZ_STATS_EVENT));
    return next;
  }, [child]);
  return { stats, recordAnswer };
}

function QuizScoreBadge() {
  const { stats } = useMuseumQuizStats();
  if (!stats.total) return null;
  return (
    <span className="inline-flex items-center gap-1 text-xs font-medium px-2.5 py-1 rounded-full bg-green-100 text-green-700 border border-green-200">
      🧠 {stats.correct}/{stats.total} correct this session
    </span>
  );
}

// ── Sorting ────────────────────────────────────────────────────────────────
const SORT_OPTIONS = [
  { id: 'default', label: 'Sort: Default' },
  { id: 'name-asc', label: 'Name (A–Z)' },
  { id: 'name-desc', label: 'Name (Z–A)' },
  { id: 'year-asc', label: 'Year (Oldest first)' },
  { id: 'year-desc', label: 'Year (Newest first)' },
];

// Best-effort numeric year from messy museum date strings like "196 BCE",
// "c. 1503–1519", "c. 67 million years ago", or "9th–10th century CE".
// Larger = more recent; BCE / "years ago" values come back negative.
function parseYearValue(value) {
  if (!value) return null;
  const s = String(value).toLowerCase();
  const m = s.match(/[\d,]+(\.\d+)?/);
  if (!m) return null;
  let num = parseFloat(m[0].replace(/,/g, ''));
  if (Number.isNaN(num)) return null;
  if (s.includes('billion')) num *= 1e9;
  else if (s.includes('million')) num *= 1e6;
  else if (s.includes('century')) num *= 100;
  const isBCE = /\bbce\b|\bbc\b/.test(s) || s.includes('ago');
  return isBCE ? -num : num;
}

function sortObjects(objects, sortBy) {
  if (!sortBy || sortBy === 'default') return objects;
  const sorted = [...objects];
  if (sortBy === 'name-asc') sorted.sort((a, b) => (a.name || '').localeCompare(b.name || ''));
  else if (sortBy === 'name-desc') sorted.sort((a, b) => (b.name || '').localeCompare(a.name || ''));
  else if (sortBy === 'year-asc' || sortBy === 'year-desc') {
    sorted.sort((a, b) => {
      const ay = parseYearValue(a.year || a.period);
      const by = parseYearValue(b.year || b.period);
      if (ay === null && by === null) return 0;
      if (ay === null) return 1; // objects with no date sort to the end
      if (by === null) return -1;
      return sortBy === 'year-asc' ? ay - by : by - ay;
    });
  }
  return sorted;
}

function SortControl({ value, onChange }) {
  return (
    <select
      value={value}
      onChange={e => onChange(e.target.value)}
      aria-label="Sort objects"
      className="border rounded-lg px-2 py-1.5 text-xs sm:text-sm text-gray-600 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-300"
    >
      {SORT_OPTIONS.map(opt => <option key={opt.id} value={opt.id}>{opt.label}</option>)}
    </select>
  );
}

// ── Lazy Wikipedia thumbnail ──────────────────────────────────────────────────
// Fetches once per wiki_title and caches in module-level map so sibling cards share results.
const thumbCache = {};

function WikiThumbnail({ wikiTitle, thumbnailLocal, category, size = 'list' }) {
  const cacheKey = thumbnailLocal || wikiTitle || '';
  const [src, setSrc] = useState(thumbnailLocal || thumbCache[wikiTitle] || null);
  const mounted = useRef(true);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; }; }, []);

  useEffect(() => {
    // Local SVG is already set as initial state; try to upgrade to real Wikipedia photo
    if (!wikiTitle) return;
    if (thumbCache[wikiTitle] && thumbCache[wikiTitle] !== 'loading') {
      if (thumbCache[wikiTitle]) setSrc(thumbCache[wikiTitle]);
      return;
    }
    thumbCache[wikiTitle] = 'loading';
    // Resolved server-side (and cached to disk there) rather than hitting
    // Wikipedia directly from the browser on every view — see
    // GET /api/museum/thumbnail in backend/app/main.py.
    fetch(`${API}/museum/thumbnail?wiki_title=${encodeURIComponent(wikiTitle)}`)
      .then(r => r.ok ? r.json() : null)
      .then(d => {
        const url = d?.thumbnail_url ?? null;
        thumbCache[wikiTitle] = url || '';
        if (mounted.current && url) setSrc(url);
      })
      .catch(() => { thumbCache[wikiTitle] = ''; });
  }, [wikiTitle]);

  const emoji = catEmoji(category);

  if (size === 'tile') {
    return (
      <div className={`absolute inset-0 bg-gradient-to-br ${tileColor(cacheKey || category)} flex items-center justify-center`}>
        {src
          ? <img src={src} alt="" className="w-full h-full object-cover" onError={() => setSrc('')} />
          : <span className="text-5xl opacity-70">{emoji}</span>
        }
      </div>
    );
  }
  if (size === 'list') {
    return (
      <div className="w-16 h-16 flex-shrink-0 rounded-lg overflow-hidden bg-indigo-100 flex items-center justify-center">
        {src
          ? <img src={src} alt="" className="w-full h-full object-cover" onError={() => setSrc('')} />
          : <span className="text-2xl">{emoji}</span>
        }
      </div>
    );
  }
  // hero size for detail view — full-bleed, Google Arts & Culture-style viewer
  return (
    <div className={`h-64 sm:h-96 -mx-4 sm:mx-0 sm:rounded-2xl overflow-hidden bg-gradient-to-br ${tileColor(cacheKey || category)} flex items-center justify-center mb-4`}>
      {src
        ? <img src={src} alt="" className="w-full h-full object-contain" onError={() => setSrc('')} />
        : <span className="text-7xl opacity-70">{emoji}</span>
      }
    </div>
  );
}

// ── Explanation video banner (for paintings, sculptures, architecture) ─────────
function ExplanationVideoBanner({ links, name }) {
  if (!links?.explanation_video) return null;
  return (
    <a href={links.explanation_video} target="_blank" rel="noopener noreferrer"
      className="flex items-center gap-3 rounded-xl bg-red-600 text-white p-4 mb-4 hover:bg-red-700 transition-colors">
      <span className="text-3xl flex-shrink-0">▶️</span>
      <div>
        <p className="font-bold text-sm">Watch: {name} — Explained</p>
        <p className="text-xs text-red-200 mt-0.5">Art history · Museum analysis · Documentary</p>
      </div>
      <span className="ml-auto text-red-200 text-lg">↗</span>
    </a>
  );
}

// ── All links section ─────────────────────────────────────────────────────────
function ObjectLinks({ links }) {
  if (!links) return null;
  const items = [
    links.museum_object && { href: links.museum_object, label: 'Official Museum Record', color: 'bg-indigo-100 text-indigo-700 border-indigo-200' },
    links.wikipedia && { href: links.wikipedia, label: 'ℹ Wikipedia', color: 'bg-gray-100 text-gray-700 border-gray-200' },
    links.image_search && { href: links.image_search, label: '🖼 Images (Wikimedia)', color: 'bg-blue-100 text-blue-700 border-blue-200' },
    links.google_image_search && { href: links.google_image_search, label: '🔍 Images (Google)', color: 'bg-yellow-100 text-yellow-700 border-yellow-200' },
    links.video && { href: links.video, label: '▶ Documentary Search', color: 'bg-red-100 text-red-700 border-red-200' },
    links.smarthistory && { href: links.smarthistory, label: '📚 Smarthistory', color: 'bg-emerald-100 text-emerald-700 border-emerald-200' },
    links.podcast && { href: links.podcast, label: '🎙 BBC Podcast', color: 'bg-purple-100 text-purple-700 border-purple-200' },
    links.museum_channel && { href: links.museum_channel, label: '🏛 Museum Channel', color: 'bg-indigo-100 text-indigo-700 border-indigo-200' },
  ].filter(Boolean);
  if (!items.length) return null;
  return (
    <div className="mt-5 border-t pt-4">
      <h3 className="text-sm font-semibold text-gray-600 mb-2">🔗 Explore Further</h3>
      <div className="flex flex-wrap gap-2">
        {items.map(({ href, label, color }) => (
          <a key={href} href={href} target="_blank" rel="noopener noreferrer"
            className={`inline-flex items-center gap-1 px-3 py-1.5 rounded-full border text-xs font-medium hover:opacity-80 transition-opacity ${color}`}>
            {label}
          </a>
        ))}
      </div>
      <p className="text-xs text-gray-400 mt-2">Links open YouTube, Wikipedia, Wikimedia Commons, Smarthistory, and BBC podcasts.</p>
    </div>
  );
}

// ── Quick Quiz ────────────────────────────────────────────────────────────────
function ObjectQuiz({ quiz }) {
  const [selected, setSelected] = useState(null);
  const { child } = useChild();
  const { recordAnswer } = useMuseumQuizStats();
  if (!quiz?.question) return null;

  function handleSelect(i) {
    if (selected !== null) return;
    setSelected(i);
    const next = recordAnswer(i === quiz.answer);
    const percentage = next.total > 0 ? Math.round((next.correct / next.total) * 100) : 0;
    // Save cumulative museum quiz performance to the child's progress record
    // so it isn't lost between sessions (same pattern as Exam.jsx).
    postProgress(child, { scores: { museum: percentage } }).catch(() => {});
  }

  return (
    <div className="rounded-xl bg-green-50 border border-green-200 p-4 mb-4">
      <h3 className="font-semibold text-green-800 mb-3">🧠 Quick Quiz</h3>
      <p className="text-sm font-medium text-green-900 mb-3">{quiz.question}</p>
      <div className="grid grid-cols-2 gap-2">
        {quiz.options?.map((opt, i) => {
          let cls = 'text-left px-3 py-2 rounded-lg text-sm border transition-colors ';
          if (selected === null) cls += 'bg-white border-green-300 hover:bg-green-100 text-green-800 cursor-pointer';
          else if (i === quiz.answer) cls += 'bg-green-500 text-white border-green-500 font-semibold';
          else if (i === selected) cls += 'bg-red-100 border-red-400 text-red-700';
          else cls += 'bg-gray-50 border-gray-200 text-gray-400';
          return (
            <button key={i} className={cls} disabled={selected !== null} onClick={() => handleSelect(i)}>
              {opt}
            </button>
          );
        })}
      </div>
      {selected !== null && (
        <p className={`mt-3 text-sm font-semibold ${selected === quiz.answer ? 'text-green-700' : 'text-red-600'}`}>
          {selected === quiz.answer ? '✅ Correct!' : `❌ The answer is: ${quiz.options[quiz.answer]}`}
        </p>
      )}
    </div>
  );
}

// ── Object detail view ────────────────────────────────────────────────────────
function ObjectDetail({ gallery, objectId, onBack }) {
  const [obj, setObj] = useState(null);
  useEffect(() => {
    fetch(`${API}/museum/${gallery}/${objectId}`).then(r => r.json()).then(setObj);
  }, [gallery, objectId]);
  if (!obj) return <div className="p-4 text-gray-500">Loading…</div>;

  return (
    <div>
      <button onClick={onBack} className="mb-4 text-sm text-indigo-600 hover:underline">← Back</button>

      {/* Hero thumbnail */}
      <WikiThumbnail wikiTitle={obj.wiki_title} thumbnailLocal={obj.thumbnail_local} category={obj.category} size="hero" />

      <div className="flex items-start justify-between gap-3">
        <h2 className="text-2xl font-bold text-gray-800 mb-1">{obj.name}</h2>
        <FavoriteButton resource={{
          title: obj.name,
          link: obj.links?.wikipedia || obj.links?.image_search || obj.links?.google_image_search || '',
          type: 'museum',
          category: obj.category,
        }} />
      </div>
      {(obj.artist || obj.architect) && (
        <p className="text-sm text-gray-500 mb-2 italic">{obj.artist || obj.architect}</p>
      )}
      <div className="flex flex-wrap gap-2 mb-4">
        {obj.origin && <span className="text-xs px-2 py-0.5 rounded-full bg-blue-100 text-blue-700">📍 {obj.origin}</span>}
        {(obj.year || obj.period) && <span className="text-xs px-2 py-0.5 rounded-full bg-amber-100 text-amber-700">📅 {obj.year || obj.period}</span>}
        {obj.material && <span className="text-xs px-2 py-0.5 rounded-full bg-green-100 text-green-700">🪨 {obj.material}</span>}
        {obj.category && <span className="text-xs px-2 py-0.5 rounded-full bg-purple-100 text-purple-700 capitalize">{obj.category}</span>}
        {obj.museum && <span className="text-xs px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-700">🏛 {obj.museum}</span>}
      </div>

      {/* Prominent explanation video for art/sculpture/architecture */}
      <ExplanationVideoBanner links={obj.links} name={obj.name} />

      {/* Wikimedia image link */}
      {obj.image_hint && (
        <div className="rounded-xl bg-gray-50 border border-gray-200 p-3 mb-4 flex items-center gap-3">
          <span className="text-2xl">🖼️</span>
          <div>
            <p className="text-xs text-gray-400 italic">{obj.image_hint}</p>
            {obj.links?.image_search && (
              <a href={obj.links.image_search} target="_blank" rel="noopener noreferrer"
                className="text-xs text-blue-600 hover:underline mt-0.5 block">View images on Wikimedia Commons →</a>
            )}
          </div>
        </div>
      )}

      <p className="text-gray-700 leading-relaxed mb-4">{obj.description}</p>

      <div className="rounded-xl bg-indigo-50 border border-indigo-200 p-4 mb-4">
        <h3 className="font-semibold text-indigo-800 mb-1">⭐ Why It Matters</h3>
        <p className="text-sm text-indigo-900">{obj.significance}</p>
      </div>

      {obj.educational_importance && (
        <div className="rounded-xl bg-blue-50 border border-blue-200 p-4 mb-4">
          <h3 className="font-semibold text-blue-800 mb-1">🎓 Educational Importance</h3>
          <p className="text-sm text-blue-900">{obj.educational_importance}</p>
        </div>
      )}

      {obj.fun_fact && (
        <div className="rounded-xl bg-yellow-50 border border-yellow-200 p-4 mb-4">
          <h3 className="font-semibold text-yellow-800 mb-1">💡 Fun Fact</h3>
          <p className="text-sm text-yellow-900">{obj.fun_fact}</p>
        </div>
      )}

      {obj.activity && (
        <div className="rounded-xl bg-pink-50 border border-pink-200 p-4 mb-4">
          <h3 className="font-semibold text-pink-800 mb-1">✏️ Activity</h3>
          <p className="text-sm text-pink-900">{obj.activity}</p>
        </div>
      )}

      <ObjectQuiz quiz={obj.quiz} />

      {obj.related_subjects?.length > 0 && (
        <div className="flex flex-wrap gap-1 mt-2 mb-2">
          <span className="text-xs text-gray-500 mr-1">Related:</span>
          {obj.related_subjects.map(s => (
            <span key={s} className="px-2 py-0.5 rounded-full text-xs bg-gray-100 border text-gray-600">{s}</span>
          ))}
        </div>
      )}

      <ObjectLinks links={obj.links} />
    </div>
  );
}

// ── Object tile — Google Arts & Culture-style photo grid card ─────────────────
function ObjectTile({ obj, onClick }) {
  return (
    <button onClick={onClick}
      className="group relative aspect-square rounded-xl overflow-hidden shadow-sm hover:shadow-lg hover:-translate-y-0.5 transition-all text-left">
      <WikiThumbnail wikiTitle={obj.wiki_title} thumbnailLocal={obj.thumbnail_local} category={obj.category} size="tile" />
      <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent px-2.5 pb-2 pt-8">
        <p className="text-white font-semibold text-xs sm:text-sm leading-tight line-clamp-2">{obj.name}</p>
        {(obj.artist || obj.architect) && (
          <p className="text-white/75 text-[11px] mt-0.5 truncate">{obj.artist || obj.architect}</p>
        )}
      </div>
      {obj.links?.explanation_video && (
        <span className="absolute top-2 right-2 text-[10px] px-1.5 py-0.5 rounded-full bg-red-600/90 text-white font-semibold">▶</span>
      )}
    </button>
  );
}

// ── Gallery view (list of objects) ────────────────────────────────────────────
function GalleryView({ gallery, onBack }) {
  const [data, setData] = useState(null);
  const [selectedObj, setSelectedObj] = useState(null);
  const [page, setPage] = useState(0);
  const [sortBy, setSortBy] = useState('default');
  const PAGE_SIZE = 24;

  useEffect(() => {
    fetch(`${API}/museum/${gallery.id}`).then(r => r.json()).then(setData);
    setPage(0);
  }, [gallery.id]);

  if (selectedObj) return (
    <div className="max-w-3xl mx-auto">
      <ObjectDetail gallery={gallery.id} objectId={selectedObj} onBack={() => setSelectedObj(null)} />
    </div>
  );

  const objects = sortObjects(data?.objects ?? [], sortBy);
  const pageCount = Math.ceil(objects.length / PAGE_SIZE);
  const visible = objects.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);

  return (
    <div>
      <button onClick={onBack} className="mb-3 text-sm text-indigo-600 hover:underline">← All Galleries</button>
      <h2 className="text-2xl font-bold mb-1">{gallery.emoji} {gallery.label}</h2>
      <div className="flex flex-wrap items-center justify-between gap-2 mb-4">
        <p className="text-xs text-gray-400">{objects.length} objects · thumbnails from Wikipedia</p>
        <div className="flex items-center gap-2">
          <QuizScoreBadge />
          <SortControl value={sortBy} onChange={(v) => { setSortBy(v); setPage(0); }} />
        </div>
      </div>
      {!data ? <p className="text-gray-400">Loading…</p> : (
        <>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
            {visible.map(obj => (
              <ObjectTile key={obj.id} obj={obj} onClick={() => setSelectedObj(obj.id)} />
            ))}
          </div>
          {pageCount > 1 && (
            <div className="flex gap-2 mt-4 justify-center flex-wrap">
              {Array.from({ length: pageCount }, (_, i) => (
                <button key={i} onClick={() => setPage(i)}
                  className={`w-8 h-8 rounded-full text-xs font-medium border transition-colors ${i === page ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-gray-600 border-gray-300 hover:border-indigo-400'}`}>
                  {i + 1}
                </button>
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}

// ── Search view ───────────────────────────────────────────────────────────────
function SearchView() {
  const [q, setQ] = useState('');
  const [results, setResults] = useState([]);
  const [searched, setSearched] = useState(false);
  const [selectedObj, setSelectedObj] = useState(null);
  const [sortBy, setSortBy] = useState('default');
  const search = () => {
    if (q.length < 2) return;
    fetch(`${API}/museum/search?q=${encodeURIComponent(q)}`).then(r => r.json())
      .then(d => { setResults(d.results || []); setSearched(true); });
  };
  if (selectedObj) return (
    <div className="max-w-3xl mx-auto">
      <ObjectDetail gallery={selectedObj.gallery} objectId={selectedObj.id} onBack={() => setSelectedObj(null)} />
    </div>
  );
  const sortedResults = sortObjects(results, sortBy);
  return (
    <div>
      <div className="flex gap-2 mb-4">
        <input value={q} onChange={e => setQ(e.target.value)} onKeyDown={e => e.key === 'Enter' && search()}
          placeholder="Search objects, places, periods…"
          className="flex-1 border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-300" />
        <button onClick={search} className="px-4 py-2 bg-indigo-600 text-white text-sm rounded-lg hover:bg-indigo-700">Search</button>
      </div>
      <div className="flex flex-wrap items-center justify-between gap-2 mb-4">
        <QuizScoreBadge />
        {results.length > 0 && <SortControl value={sortBy} onChange={setSortBy} />}
      </div>
      {searched && results.length === 0 && <p className="text-gray-500 text-sm">No results found.</p>}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
        {sortedResults.map(obj => (
          <div key={obj.id} className="relative">
            <ObjectTile obj={obj} onClick={() => setSelectedObj(obj)} />
            {obj.gallery_label && (
              <span className="absolute top-2 left-2 text-[10px] px-1.5 py-0.5 rounded-full bg-white/90 text-indigo-700 font-medium">{obj.gallery_label}</span>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

// ── Root component ────────────────────────────────────────────────────────────
export default function VirtualMuseum() {
  const [overview, setOverview] = useState(null);
  const [fetchError, setFetchError] = useState(false);
  const [retryCount, setRetryCount] = useState(0);
  const [selectedGallery, setSelectedGallery] = useState(null);
  const [tab, setTab] = useState('galleries');
  useEffect(() => {
    setFetchError(false);
    fetch(`${API}/museum`)
      .then(r => {
        if (!r.ok) throw new Error('fetch failed');
        return r.json();
      })
      .then(setOverview)
      .catch(() => setFetchError(true));
  }, [retryCount]);
  if (fetchError) return (
    <div className="p-8 text-center">
      <p className="text-red-600">Could not load the museum. Make sure the backend is running.</p>
      <button onClick={() => setRetryCount(count => count + 1)} className="mt-3 text-sm font-medium text-indigo-600 underline">
        Retry
      </button>
    </div>
  );
  if (!overview) return <div className="p-8 text-center text-gray-500">Loading…</div>;
  if (selectedGallery) return (
    <div className="museum-shell max-w-6xl mx-auto p-4" data-museum-theme={MUSEUM_DESIGN_VERSION}>
      <GalleryView gallery={selectedGallery} onBack={() => setSelectedGallery(null)} />
    </div>
  );
  return (
    <div className="museum-shell max-w-6xl mx-auto p-4" data-museum-theme={MUSEUM_DESIGN_VERSION}>
      <header className="museum-hero">
        <div>
          <p className="museum-eyebrow">EDUAI PRO · OPEN MUSEUM</p>
          <h1>Explore art, history and human creativity</h1>
          <p>{overview.description}</p>
          <p className="museum-count">
            {(overview.total_objects ?? overview.galleries?.reduce((s, g) => s + (g.object_count || 0), 0) ?? 0).toLocaleString()} objects · trusted learning links · open-access art
          </p>
        </div>
        <div className="museum-hero-mark" aria-hidden="true">🏛️</div>
      </header>
      <div className="museum-nav flex gap-2 mb-8 sticky top-0 backdrop-blur z-10 -mx-4 px-4 py-3 sm:mx-0 sm:px-0 sm:static">
        {[['galleries', '🏛 Categories'], ['search', '🔍 Search'], ['open-art', '🖼️ Open Art']].map(([t, label]) => (
          <button key={t} onClick={() => setTab(t)}
            className={`px-4 py-2 text-sm font-medium rounded-full border transition-colors ${tab === t ? 'museum-nav-active' : 'museum-nav-idle'}`}>
            {label}
          </button>
        ))}
      </div>
      {tab === 'search' && <SearchView />}
      {tab === 'open-art' && <CMACollection />}
      {tab === 'galleries' && (
        <section aria-label="Museum collections">
          <div className="mb-4 flex items-end justify-between gap-3">
            <div><p className="museum-eyebrow">BROWSE THE COLLECTION</p><h2 className="museum-section-title">Stories across time and place</h2></div>
            <span className="text-sm text-gray-500">{overview.galleries.length} collections</span>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-4">
          {overview.galleries.map(gallery => (
            <button key={gallery.id} onClick={() => setSelectedGallery(gallery)}
              className={`museum-collection-card group relative aspect-[4/3] overflow-hidden bg-gradient-to-br ${tileColor(gallery.id)} text-left`}>
              <div className="absolute inset-0 flex items-center justify-center">
                <span className="text-6xl opacity-80 group-hover:scale-110 transition-transform">{gallery.emoji}</span>
              </div>
              <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent px-3 pb-2.5 pt-10">
                <p className="text-white font-bold text-sm leading-tight">{gallery.label}</p>
                <p className="text-white/80 text-xs mt-0.5">{gallery.object_count.toLocaleString()} object{gallery.object_count !== 1 ? 's' : ''}</p>
              </div>
            </button>
          ))}
          </div>
        </section>
      )}
    </div>
  );
}
