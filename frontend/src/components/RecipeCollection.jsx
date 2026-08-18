import React, { useState, useEffect, useRef } from 'react';

const API = '/api/cuisine-detail/recipes';
const PAGE_SIZE = 60;

const CATEGORY_OPTIONS = [
  ['', 'All Categories'], ['main', 'Main Course'], ['stew', 'Curry & Stew'],
  ['grill', 'Grilled / BBQ'], ['rice', 'Rice Dish'], ['noodle', 'Noodles & Pasta'],
  ['dumpling', 'Dumplings & Wraps'], ['bread', 'Bread'], ['soup', 'Soup'],
  ['salad', 'Salad'], ['street', 'Street Food'], ['fried', 'Fried'],
  ['pickle', 'Fermented / Pickled'], ['breakfast', 'Breakfast'], ['dessert', 'Dessert'],
  ['beverage', 'Beverage'],
];

const PROTEIN_OPTIONS = ['', 'Chicken', 'Beef', 'Lamb', 'Mutton/Goat', 'Fish/Seafood', 'Egg', 'Vegetarian', 'Mixed'];

// Lazy Wikipedia thumbnail, same server-side-cached endpoint pattern as VirtualMuseum's WikiThumbnail.
const thumbCache = {};
function RecipeThumbnail({ wikiTitle, emoji }) {
  const [src, setSrc] = useState(thumbCache[wikiTitle] || null);
  const mounted = useRef(true);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; }; }, []);
  useEffect(() => {
    if (!wikiTitle || (thumbCache[wikiTitle] && thumbCache[wikiTitle] !== 'loading')) {
      if (thumbCache[wikiTitle]) setSrc(thumbCache[wikiTitle]);
      return;
    }
    thumbCache[wikiTitle] = 'loading';
    fetch(`/api/cuisine/thumbnail?wiki_title=${encodeURIComponent(wikiTitle)}`)
      .then(r => (r.ok ? r.json() : null))
      .then(d => {
        const url = d?.thumbnail_url ?? null;
        thumbCache[wikiTitle] = url || '';
        if (mounted.current && url) setSrc(url);
      })
      .catch(() => { thumbCache[wikiTitle] = ''; });
  }, [wikiTitle]);

  return (
    <div className="absolute inset-0 bg-gradient-to-br from-orange-200 to-amber-100 dark:from-orange-900 dark:to-amber-950 flex items-center justify-center">
      {src ? <img src={src} alt="" className="w-full h-full object-cover" onError={() => setSrc('')} /> : <span className="text-5xl opacity-70">{emoji}</span>}
    </div>
  );
}

function RecipeCard({ recipe, onOpen }) {
  return (
    <button onClick={() => onOpen(recipe)}
      className="group relative aspect-square rounded-xl overflow-hidden shadow-sm hover:shadow-lg hover:-translate-y-0.5 transition-all text-left">
      <RecipeThumbnail wikiTitle={recipe.wiki_title} emoji={recipe.emoji} />
      <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/85 via-black/35 to-transparent px-2.5 pb-2 pt-8">
        <p className="text-white font-semibold text-xs sm:text-sm leading-tight line-clamp-2">{recipe.name}</p>
        <p className="text-white/75 text-[11px] mt-0.5 truncate">{recipe.cuisine} · {recipe.protein}</p>
      </div>
    </button>
  );
}

function RecipeDetailModal({ recipe, onClose }) {
  if (!recipe) return null;
  return (
    <div className="fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4" onClick={onClose}>
      <div className="bg-white dark:bg-gray-800 rounded-2xl max-w-lg w-full shadow-2xl overflow-hidden" onClick={e => e.stopPropagation()}>
        <div className="relative h-48 bg-gradient-to-br from-orange-300 to-amber-200 dark:from-orange-900 dark:to-amber-950">
          <RecipeThumbnail wikiTitle={recipe.wiki_title} emoji={recipe.emoji} />
          <button onClick={onClose} className="absolute top-2 right-2 w-8 h-8 rounded-full bg-black/50 text-white flex items-center justify-center hover:bg-black/70">✕</button>
        </div>
        <div className="p-5 space-y-3">
          <div>
            <h2 className="text-xl font-bold text-gray-800 dark:text-gray-100">{recipe.name}</h2>
            <p className="text-sm text-gray-500 dark:text-gray-400">{recipe.cuisine} · {recipe.category} · {recipe.protein}</p>
          </div>
          <p className="text-sm text-gray-700 dark:text-gray-300">{recipe.description}</p>
          {recipe.historical_fact && (
            <div className="rounded-lg bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3">
              <p className="text-xs text-indigo-800 dark:text-indigo-200">📜 {recipe.historical_fact}</p>
            </div>
          )}
          <p className="text-xs text-gray-500 dark:text-gray-400">🔥 Cooking technique: <span className="font-medium">{recipe.cooking_technique}</span></p>
          {recipe.substitution_note && (
            <div className="rounded-lg bg-amber-50 dark:bg-amber-950 border border-amber-200 dark:border-amber-800 p-3">
              <p className="text-xs text-amber-800 dark:text-amber-200">🐄 {recipe.substitution_note}</p>
            </div>
          )}
          <div className="flex flex-wrap gap-2 pt-2 border-t dark:border-gray-700">
            {recipe.links?.text_guide && (
              <a href={recipe.links.text_guide} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 px-3 py-1.5 rounded-full border text-xs font-medium bg-indigo-100 text-indigo-700 border-indigo-200 hover:opacity-80">📖 Recipe Guide</a>
            )}
            {recipe.links?.video && (
              <a href={recipe.links.video} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 px-3 py-1.5 rounded-full border text-xs font-medium bg-red-100 text-red-700 border-red-200 hover:opacity-80">▶ YouTube Video</a>
            )}
            {recipe.links?.image_search && (
              <a href={recipe.links.image_search} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 px-3 py-1.5 rounded-full border text-xs font-medium bg-blue-100 text-blue-700 border-blue-200 hover:opacity-80">🖼 Pictures</a>
            )}
            {recipe.links?.wikipedia && (
              <a href={recipe.links.wikipedia} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 px-3 py-1.5 rounded-full border text-xs font-medium bg-gray-100 text-gray-700 border-gray-200 hover:opacity-80">ℹ Wikipedia</a>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default function RecipeCollection() {
  const [q, setQ] = useState('');
  const [cuisine, setCuisine] = useState('');
  const [category, setCategory] = useState('');
  const [protein, setProtein] = useState('');
  const [offset, setOffset] = useState(0);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [openRecipe, setOpenRecipe] = useState(null);
  const [cuisineOptions, setCuisineOptions] = useState([]);

  // Build the cuisine filter dropdown from the recipe collection itself (23 cuisines),
  // which is broader than the 13 cuisines with full landing pages.
  useEffect(() => {
    fetch('/api/cuisine-detail/recipe-cuisines').then(r => r.json()).then(d => {
      setCuisineOptions((d.cuisines || []).map(c => [c.id, c.label]));
    }).catch(() => {});
  }, []);

  useEffect(() => {
    setOffset(0);
  }, [q, cuisine, category, protein]);

  useEffect(() => {
    setLoading(true);
    const params = new URLSearchParams({ q, cuisine, category, protein, limit: String(PAGE_SIZE), offset: String(offset) });
    fetch(`${API}?${params}`).then(r => r.json()).then(d => { setData(d); setLoading(false); }).catch(e => { setError(e.message); setLoading(false); });
  }, [q, cuisine, category, protein, offset]);

  const total = data?.total ?? 0;
  const recipes = data?.recipes ?? [];
  const pageCount = Math.ceil(total / PAGE_SIZE) || 1;
  const currentPage = Math.floor(offset / PAGE_SIZE) + 1;

  return (
    <div className="space-y-5">
      <div className="rounded-2xl p-5 text-white shadow-lg" style={{ background: 'linear-gradient(135deg, #ea580c, #c2410c)' }}>
        <h2 className="text-2xl font-extrabold">🍽️ World Recipe Collection</h2>
        <p className="text-white/90 text-sm mt-1">1,700+ real, named dishes across 39 world cuisines — pork-free throughout, with a picture, a video link, and a recipe guide link for each.</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        <div className="relative sm:col-span-2 lg:col-span-1">
          <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">🔍</span>
          <input type="text" value={q} onChange={e => setQ(e.target.value)} placeholder="Search dishes..."
            className="w-full rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 pl-9 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400 dark:text-white" />
        </div>
        <select value={cuisine} onChange={e => setCuisine(e.target.value)}
          className="rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 px-4 py-2 text-sm dark:text-white">
          <option value="">All Cuisines</option>
          {cuisineOptions.map(([id, label]) => <option key={id} value={id}>{label}</option>)}
        </select>
        <select value={category} onChange={e => setCategory(e.target.value)}
          className="rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 px-4 py-2 text-sm dark:text-white">
          {CATEGORY_OPTIONS.map(([id, label]) => <option key={id} value={id}>{label}</option>)}
        </select>
        <select value={protein} onChange={e => setProtein(e.target.value)}
          className="rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 px-4 py-2 text-sm dark:text-white">
          <option value="">All Proteins</option>
          {PROTEIN_OPTIONS.filter(Boolean).map(p => <option key={p} value={p}>{p}</option>)}
        </select>
      </div>

      <p className="text-xs text-gray-500 dark:text-gray-400">{total.toLocaleString()} dish{total !== 1 ? 'es' : ''} found</p>

      {error && (
        <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
          <p className="font-bold">Could not load recipes</p><p className="text-sm mt-1">{error}</p>
        </div>
      )}

      {loading ? (
        <div className="flex justify-center items-center py-16">
          <div className="flex gap-2">
            {[0, 1, 2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-orange-500 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}
          </div>
        </div>
      ) : recipes.length === 0 ? (
        <div className="text-center py-10 text-gray-500 dark:text-gray-400">
          <p className="text-4xl mb-2">🔍</p><p className="font-semibold">No dishes match your filters</p>
        </div>
      ) : (
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
          {recipes.map(r => <RecipeCard key={r.id} recipe={r} onOpen={setOpenRecipe} />)}
        </div>
      )}

      {pageCount > 1 && (
        <div className="flex items-center justify-center gap-3 pt-2">
          <button disabled={offset === 0} onClick={() => setOffset(o => Math.max(0, o - PAGE_SIZE))}
            className="px-4 py-1.5 rounded-full text-sm font-semibold bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 disabled:opacity-40">← Prev</button>
          <span className="text-sm text-gray-500 dark:text-gray-400">Page {currentPage} of {pageCount}</span>
          <button disabled={offset + PAGE_SIZE >= total} onClick={() => setOffset(o => o + PAGE_SIZE)}
            className="px-4 py-1.5 rounded-full text-sm font-semibold bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 disabled:opacity-40">Next →</button>
        </div>
      )}

      <RecipeDetailModal recipe={openRecipe} onClose={() => setOpenRecipe(null)} />
    </div>
  );
}
