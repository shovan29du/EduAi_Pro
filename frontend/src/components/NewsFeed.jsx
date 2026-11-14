import { useCallback, useEffect, useMemo, useState } from 'react';
import { getNews, getNewsPreferences, getNewsSources, saveNewsPreferences } from '../api/news.js';

const AUTO_REFRESH_MS = 10 * 60 * 1000; // headlines are cached server-side for 15 min anyway

function timeAgo(iso) {
  if (!iso) return '';
  const published = new Date(iso);
  if (Number.isNaN(published.getTime())) return '';
  const minutes = Math.max(0, Math.round((Date.now() - published.getTime()) / 60000));
  if (minutes < 1) return 'just now';
  if (minutes < 60) return `${minutes}m ago`;
  const hours = Math.round(minutes / 60);
  if (hours < 24) return `${hours}h ago`;
  return `${Math.round(hours / 24)}d ago`;
}

export default function NewsFeed() {
  const [sources, setSources] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedSources, setSelectedSources] = useState([]);
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [customizing, setCustomizing] = useState(false);
  const [savingPrefs, setSavingPrefs] = useState(false);

  const categoryEmoji = useMemo(() => {
    const map = {};
    categories.forEach((c) => { map[c.id] = c.emoji; });
    return map;
  }, [categories]);

  const loadNews = useCallback((cats, srcs) => {
    setLoading(true);
    setError('');
    getNews({ categories: cats, sources: srcs, limit: 30 })
      .then((data) => setArticles(data.articles || []))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    Promise.all([getNewsSources(), getNewsPreferences()])
      .then(([sourceData, prefs]) => {
        setSources(sourceData.sources || []);
        setCategories(sourceData.categories || []);
        setSelectedCategories(prefs.categories || []);
        setSelectedSources(prefs.sources || []);
        loadNews(prefs.categories || [], prefs.sources || []);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [loadNews]);

  useEffect(() => {
    if (!selectedCategories.length && !selectedSources.length) return undefined;
    const id = setInterval(() => loadNews(selectedCategories, selectedSources), AUTO_REFRESH_MS);
    return () => clearInterval(id);
  }, [selectedCategories, selectedSources, loadNews]);

  function toggle(list, setList, id) {
    setList(list.includes(id) ? list.filter((x) => x !== id) : [...list, id]);
  }

  async function handleSavePreferences() {
    setSavingPrefs(true);
    try {
      const saved = await saveNewsPreferences(selectedCategories, selectedSources);
      setSelectedCategories(saved.categories);
      setSelectedSources(saved.sources);
      loadNews(saved.categories, saved.sources);
      setCustomizing(false);
    } catch (err) {
      setError(err.message);
    } finally {
      setSavingPrefs(false);
    }
  }

  const [lead, ...rest] = articles;

  return (
    <section
      aria-label="World news"
      className="overflow-hidden rounded-2xl border bg-white dark:border-gray-700 dark:bg-gray-900"
    >
      <header className="flex flex-wrap items-center justify-between gap-2 border-b bg-gradient-to-r from-slate-900 to-slate-700 p-4 text-white dark:border-gray-700">
        <div>
          <h3 className="text-xl font-bold">🗞️ Your Daily Paper</h3>
          <p className="text-xs text-slate-300">Latest headlines from around the world, customized by you.</p>
        </div>
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={() => loadNews(selectedCategories, selectedSources)}
            className="rounded-full border border-white/30 px-3 py-1.5 text-sm font-medium hover:bg-white/10 focus:outline focus:outline-2 focus:outline-blue-400"
          >
            🔄 Refresh
          </button>
          <button
            type="button"
            onClick={() => setCustomizing((v) => !v)}
            aria-expanded={customizing}
            className="rounded-full border border-white/30 px-3 py-1.5 text-sm font-medium hover:bg-white/10 focus:outline focus:outline-2 focus:outline-blue-400"
          >
            ⚙️ Customize
          </button>
        </div>
      </header>

      {customizing && (
        <div className="border-b bg-slate-50 p-4 dark:border-gray-700 dark:bg-gray-800">
          <div className="grid gap-4 sm:grid-cols-2">
            <fieldset>
              <legend className="mb-2 text-sm font-semibold">Topics</legend>
              <div className="flex flex-wrap gap-2">
                {categories.map((cat) => (
                  <label
                    key={cat.id}
                    className={`cursor-pointer rounded-full border px-3 py-1 text-sm ${
                      selectedCategories.includes(cat.id)
                        ? 'border-indigo-500 bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200'
                        : 'border-gray-300 bg-white text-gray-700 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300'
                    }`}
                  >
                    <input
                      type="checkbox"
                      className="sr-only"
                      checked={selectedCategories.includes(cat.id)}
                      onChange={() => toggle(selectedCategories, setSelectedCategories, cat.id)}
                    />
                    {cat.emoji} {cat.label}
                  </label>
                ))}
              </div>
            </fieldset>
            <fieldset>
              <legend className="mb-2 text-sm font-semibold">Outlets</legend>
              <div className="flex flex-wrap gap-2">
                {sources.map((src) => (
                  <label
                    key={src.id}
                    className={`cursor-pointer rounded-full border px-3 py-1 text-sm ${
                      selectedSources.includes(src.id)
                        ? 'border-indigo-500 bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200'
                        : 'border-gray-300 bg-white text-gray-700 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300'
                    }`}
                  >
                    <input
                      type="checkbox"
                      className="sr-only"
                      checked={selectedSources.includes(src.id)}
                      onChange={() => toggle(selectedSources, setSelectedSources, src.id)}
                    />
                    {src.name}
                  </label>
                ))}
              </div>
            </fieldset>
          </div>
          <button
            type="button"
            onClick={handleSavePreferences}
            disabled={savingPrefs}
            className="mt-3 rounded-lg bg-indigo-600 px-4 py-1.5 text-sm font-semibold text-white hover:bg-indigo-700 disabled:opacity-60"
          >
            {savingPrefs ? 'Saving…' : 'Save my paper'}
          </button>
        </div>
      )}

      <div className="p-4">
        {loading && <p className="text-sm text-gray-500 dark:text-gray-400">Fetching the latest headlines…</p>}
        {error && (
          <p role="alert" className="rounded-lg bg-red-50 p-3 text-sm text-red-700 dark:bg-red-950 dark:text-red-300">
            {error}
          </p>
        )}
        {!loading && !error && articles.length === 0 && (
          <p className="text-sm text-gray-500 dark:text-gray-400">
            No headlines available right now -- try Refresh in a moment, or pick different outlets under Customize.
          </p>
        )}

        {!loading && lead && (
          <a
            href={lead.link}
            target="_blank"
            rel="noopener noreferrer"
            className="mb-4 block overflow-hidden rounded-xl border transition-colors hover:border-indigo-400 dark:border-gray-700"
          >
            <div className="flex flex-col sm:flex-row">
              <div className="flex h-44 w-full items-center justify-center bg-gradient-to-br from-slate-200 to-indigo-100 dark:from-slate-800 dark:to-indigo-950 sm:h-48 sm:w-64 sm:flex-shrink-0">
                {lead.image
                  ? <img src={lead.image} alt="" className="h-full w-full object-cover" onError={(e) => { e.target.style.display = 'none'; }} />
                  : <span className="text-5xl opacity-70">{categoryEmoji[lead.category] || '📰'}</span>}
              </div>
              <div className="p-4">
                <div className="mb-1 flex items-center gap-2 text-xs font-semibold uppercase tracking-wide text-indigo-600 dark:text-indigo-400">
                  <span>{categoryEmoji[lead.category] || '📰'} {lead.category}</span>
                  <span>·</span>
                  <span>{lead.source_name}</span>
                  <span>·</span>
                  <span>{timeAgo(lead.published)}</span>
                </div>
                <h4 className="text-lg font-bold leading-snug">{lead.title}</h4>
                <p className="mt-1 text-sm text-gray-600 dark:text-gray-300">{lead.summary}</p>
              </div>
            </div>
          </a>
        )}

        {rest.length > 0 && (
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {rest.map((article) => (
              <a
                key={article.link}
                href={article.link}
                target="_blank"
                rel="noopener noreferrer"
                className="flex flex-col overflow-hidden rounded-xl border transition-colors hover:border-indigo-400 dark:border-gray-700"
              >
                <div className="flex h-28 items-center justify-center bg-gradient-to-br from-slate-100 to-indigo-50 dark:from-slate-800 dark:to-indigo-950">
                  {article.image
                    ? <img src={article.image} alt="" className="h-full w-full object-cover" onError={(e) => { e.target.style.display = 'none'; }} />
                    : <span className="text-3xl opacity-70">{categoryEmoji[article.category] || '📰'}</span>}
                </div>
                <div className="flex flex-1 flex-col p-3">
                  <div className="mb-1 flex items-center gap-1.5 text-[11px] font-semibold uppercase tracking-wide text-indigo-600 dark:text-indigo-400">
                    <span>{article.source_name}</span>
                    <span>·</span>
                    <span>{timeAgo(article.published)}</span>
                  </div>
                  <h5 className="text-sm font-semibold leading-snug">{article.title}</h5>
                  <p className="mt-1 line-clamp-3 text-xs text-gray-600 dark:text-gray-300">{article.summary}</p>
                </div>
              </a>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}
