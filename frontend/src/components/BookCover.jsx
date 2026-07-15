import { useState, useEffect, useRef } from 'react';

// Module-level cache shared across every BookCover instance, keyed by
// "title|author", so the same book only triggers one network request per
// page session (mirrors the WikiThumbnail pattern used in VirtualMuseum.jsx).
const coverCache = {};

/**
 * Renders a real book cover fetched live from the Open Library Search API
 * (https://openlibrary.org/search.json), which returns a cover_i id when a
 * matching edition has a real cover on file; that id is turned into a real
 * Open Library Covers API image URL. No cover URL or ISBN is guessed or
 * fabricated -- if Open Library has no match, a plain book-emoji
 * placeholder is shown instead.
 */
export default function BookCover({ title, author, size = 'list' }) {
  const key = `${title || ''}|${author || ''}`;
  const [src, setSrc] = useState(coverCache[key] && coverCache[key] !== 'loading' ? coverCache[key] : null);
  const mounted = useRef(true);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; }; }, []);

  useEffect(() => {
    if (!title) return;
    if (coverCache[key] && coverCache[key] !== 'loading') {
      setSrc(coverCache[key] || null);
      return;
    }
    coverCache[key] = 'loading';
    const params = new URLSearchParams({ title, limit: '1', fields: 'cover_i' });
    if (author) params.set('author', author);
    fetch(`https://openlibrary.org/search.json?${params.toString()}`)
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        const coverId = d?.docs?.[0]?.cover_i;
        const url = coverId ? `https://covers.openlibrary.org/b/id/${coverId}-M.jpg` : null;
        coverCache[key] = url || '';
        if (mounted.current && url) setSrc(url);
      })
      .catch(() => { coverCache[key] = ''; });
  }, [key, title, author]);

  const dims = size === 'hero' ? 'w-28 h-40' : 'w-14 h-20';

  return (
    <div className={`${dims} flex-shrink-0 rounded-md overflow-hidden bg-gray-100 border border-gray-200 flex items-center justify-center`}>
      {src
        ? <img src={src} alt="" className="w-full h-full object-cover" onError={() => setSrc(null)} />
        : <span className={size === 'hero' ? 'text-4xl' : 'text-2xl'}>📕</span>
      }
    </div>
  );
}
