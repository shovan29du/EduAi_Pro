import { useState, useEffect, useRef } from 'react';

// Module-level cache shared across every BookCover instance, keyed by
// "title|author", so the same book only triggers one network request per
// page session (mirrors the WikiThumbnail pattern used in VirtualMuseum.jsx).
const coverCache = {};

async function findCoverUrl(title, author) {
  // Try Google Books first -- it has the broadest cover coverage and its
  // public volumes.list endpoint needs no API key for basic queries.
  try {
    const q = author ? `intitle:${title} inauthor:${author}` : `intitle:${title}`;
    const res = await fetch(`https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(q)}&maxResults=1`);
    if (res.ok) {
      const data = await res.json();
      const links = data?.items?.[0]?.volumeInfo?.imageLinks;
      const url = links?.thumbnail || links?.smallThumbnail;
      if (url) return url.replace(/^http:/, 'https:');
    }
  } catch {
    // fall through to Open Library
  }

  // Fall back to the Open Library Search API, which returns a cover_i id
  // when a matching edition has a real cover on file.
  try {
    const params = new URLSearchParams({ title, limit: '1', fields: 'cover_i' });
    if (author) params.set('author', author);
    const res = await fetch(`https://openlibrary.org/search.json?${params.toString()}`);
    if (res.ok) {
      const data = await res.json();
      const coverId = data?.docs?.[0]?.cover_i;
      if (coverId) return `https://covers.openlibrary.org/b/id/${coverId}-M.jpg`;
    }
  } catch {
    // no cover found anywhere
  }

  return null;
}

/**
 * Renders a real book cover fetched live from the Google Books API, falling
 * back to the Open Library Search API -- both real, public, no-key-required
 * services -- rather than guessing an ISBN or direct image URL. If neither
 * has a match, a plain book-emoji placeholder is shown instead.
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
    findCoverUrl(title, author)
      .then((url) => {
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
