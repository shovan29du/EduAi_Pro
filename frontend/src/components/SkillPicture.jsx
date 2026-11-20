import { useEffect, useRef, useState } from 'react';
import { getRelatedArticle } from '../api/lessonEnrichment.js';
import ImageCredit from './ImageCredit.jsx';

// A picture for a Survival or Practical Skills lesson.
//
// Lesson titles such as "Stranger Awareness" or "Single-Leg Takedown" are not
// Wikipedia article names, so a plain title lookup found no picture for most
// of them. This asks the server for the closest matching article instead: it
// tries the lesson's own `wiki_title`, then searches for the title (with the
// bracket words split out), then for the title plus its subject, and last of
// all for the subject on its own, so every lesson shows something related.
// The article's name is shown under the picture, so a student can tell what
// the picture is, and the photographer and licence are credited.
const cache = new Map();
export const clearSkillPictureCache = () => cache.clear(); // for tests

function useArticle(title, query, context, enabled) {
  const key = `${title}|${query}|${context}`;
  const [article, setArticle] = useState(cache.get(key) ?? undefined);
  useEffect(() => {
    if (!enabled) return undefined;
    if (cache.has(key)) { setArticle(cache.get(key)); return undefined; }
    let active = true;
    getRelatedArticle({ title, query, context })
      .then((a) => {
        const found = a?.available && a.thumbnail_url ? a : null;
        cache.set(key, found);
        if (active) setArticle(found);
      })
      .catch(() => { if (active) setArticle(null); }); // not cached: a dropped connection can retry
    return () => { active = false; };
  }, [key, title, query, context, enabled]);
  return article;
}

// Small list thumbnails only start loading once they scroll into view, so
// opening a category of 50 lessons does not make 50 lookups at once.
function useVisible(ref, disabled) {
  const [visible, setVisible] = useState(disabled || typeof IntersectionObserver === 'undefined');
  useEffect(() => {
    if (visible || !ref.current) return undefined;
    const observer = new IntersectionObserver((entries) => {
      if (entries.some((e) => e.isIntersecting)) { setVisible(true); observer.disconnect(); }
    }, { rootMargin: '200px' });
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, [visible, ref]);
  return visible;
}

export default function SkillPicture({ title, wikiTitle = '', context = '', size = 'hero' }) {
  const ref = useRef(null);
  const visible = useVisible(ref, size === 'hero');
  const article = useArticle(wikiTitle, title, context, visible && !!title);
  const [broken, setBroken] = useState(false);
  const found = article && !broken ? article : null;

  if (size === 'thumb') {
    // The wrapper stays (empty) so the observer has something to watch.
    return (
      <span ref={ref} className={found ? 'flex-shrink-0' : 'hidden'}>
        {found && (
          <img src={found.thumbnail_url} alt="" loading="lazy" onError={() => setBroken(true)}
            className="h-14 w-14 rounded-lg object-cover" />
        )}
      </span>
    );
  }
  if (!found) return <span ref={ref} />;
  return (
    <figure ref={ref} className="mt-3" data-testid="skill-picture">
      <img src={found.thumbnail_url} alt={found.title} onError={() => setBroken(true)}
        className="max-h-64 w-full rounded-xl bg-gray-50 object-contain dark:bg-gray-800" />
      <ImageCredit src={found.thumbnail_url} />
      <figcaption className="-mt-2 text-xs text-gray-600 dark:text-gray-400">
        Picture: {found.title}{found.description ? ` — ${found.description}` : ''} ·{' '}
        <a href={found.page_url} target="_blank" rel="noopener noreferrer" className="underline">Wikipedia</a>
      </figcaption>
    </figure>
  );
}
