import { useEffect, useRef, useState } from 'react';
import { downloadLessonPicture, getRelatedArticle, uploadLessonPicture } from '../api/lessonEnrichment.js';
import ImageCredit from './ImageCredit.jsx';

// A picture for a lesson (Survival Skills, Practical Skills, subject lessons).
//
// By default it is the closest Wikipedia article's freely licensed picture:
// lesson titles such as "Stranger Awareness" are not article names, so the
// server tries the lesson's own `wiki_title`, a title search, a full-text
// search, the title plus its subject, and last of all the subject alone. The
// article's name is shown under the picture, with the photographer and licence.
//
// With `pictureKey` the owner can replace it: Download saves a picture found on
// the web, Upload saves one from their computer. Both are kept in the database
// and then shown instead of the automatic one.
const cache = new Map();
export const clearSkillPictureCache = () => cache.clear(); // for tests
export const MAX_PICTURE_BYTES = 8 * 1024 * 1024;

function useArticle(title, query, context, pictureKey, enabled) {
  const key = `${title}|${query}|${context}|${pictureKey}`;
  const [article, setArticle] = useState(cache.get(key) ?? undefined);
  useEffect(() => {
    if (!enabled) return undefined;
    if (cache.has(key)) { setArticle(cache.get(key)); return undefined; }
    let active = true;
    getRelatedArticle({ title, query, context, key: pictureKey })
      .then((a) => {
        const found = a?.available && a.thumbnail_url ? a : null;
        cache.set(key, found);
        if (active) setArticle(found);
      })
      .catch(() => { if (active) setArticle(null); }); // not cached: a dropped connection can retry
    return () => { active = false; };
  }, [key, title, query, context, pictureKey, enabled]);
  const replace = (next) => { cache.set(key, next); setArticle(next); };
  return [article, replace];
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

function PictureControls({ pictureKey, title, context, wikiTitle, hasPicture, onSaved }) {
  const [busy, setBusy] = useState('');
  const [message, setMessage] = useState(null);
  const fileInput = useRef(null);

  async function run(kind, action, success) {
    setBusy(kind);
    setMessage(null);
    try {
      onSaved(await action());
      setMessage({ kind: 'ok', text: success });
    } catch (err) {
      setMessage({ kind: 'error', text: err.message || 'Something went wrong.' });
    } finally {
      setBusy('');
    }
  }

  function download() {
    return run('download', () => downloadLessonPicture({ key: pictureKey, title, context, wikiTitle }),
      'Picture downloaded and saved in the database.');
  }

  function upload(event) {
    const file = event.target.files?.[0];
    event.target.value = '';
    if (!file) return undefined;
    if (!/^image\/(jpeg|png|webp|gif)$/.test(file.type)) {
      setMessage({ kind: 'error', text: 'Choose a JPEG, PNG, WebP or GIF picture.' });
      return undefined;
    }
    if (file.size > MAX_PICTURE_BYTES) {
      setMessage({ kind: 'error', text: 'That picture is too large (limit 8 MB).' });
      return undefined;
    }
    return run('upload', () => uploadLessonPicture(pictureKey, file), 'Picture uploaded and saved in the database.');
  }

  const button = 'rounded-lg border px-3 py-1.5 text-sm font-medium disabled:opacity-50';
  return (
    <div className="mt-2" aria-label="Picture controls">
      <div className="flex flex-wrap gap-2">
        <button type="button" onClick={download} disabled={!!busy}
          className={`${button} border-indigo-300 bg-indigo-50 text-indigo-700 hover:bg-indigo-100`}>
          {busy === 'download' ? 'Downloading…' : hasPicture ? '⬇ Download another picture' : '⬇ Download picture'}
        </button>
        <button type="button" onClick={() => fileInput.current?.click()} disabled={!!busy}
          className={`${button} border-emerald-300 bg-emerald-50 text-emerald-700 hover:bg-emerald-100`}>
          {busy === 'upload' ? 'Uploading…' : '⬆ Upload picture'}
        </button>
        <input ref={fileInput} type="file" accept="image/jpeg,image/png,image/webp,image/gif" onChange={upload}
          className="hidden" aria-label="Choose a picture to upload" data-testid="picture-file-input" />
      </div>
      {message && (
        <p role={message.kind === 'error' ? 'alert' : 'status'}
          className={`mt-2 text-sm ${message.kind === 'error' ? 'text-red-600' : 'text-emerald-700'}`}>
          {message.text}
        </p>
      )}
    </div>
  );
}

function Caption({ article }) {
  if (article.stored && article.source === 'upload') {
    return <>Your uploaded picture · saved in the database</>;
  }
  return (
    <>
      {article.stored ? 'Saved picture' : 'Picture'}: {article.title}{article.description ? ` — ${article.description}` : ''}
      {article.page_url && (
        <> · <a href={article.page_url} target="_blank" rel="noopener noreferrer" className="underline">Wikipedia</a></>
      )}
    </>
  );
}

export default function SkillPicture({ title, wikiTitle = '', context = '', size = 'hero', pictureKey = '', controls = false }) {
  const ref = useRef(null);
  const visible = useVisible(ref, size === 'hero');
  const [article, setArticle] = useArticle(wikiTitle, title, context, pictureKey, visible && !!title);
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
  const showControls = controls && !!pictureKey;
  if (!found && !showControls) return <span ref={ref} />;
  return (
    <figure ref={ref} className="mt-3" data-testid="skill-picture">
      {found ? (
        <>
          <img src={found.thumbnail_url} alt={found.title} onError={() => setBroken(true)}
            className="max-h-64 w-full rounded-xl bg-gray-50 object-contain dark:bg-gray-800" />
          {found.stored
            ? found.credit?.line && (
              <p className="mt-1 text-xs text-gray-500 dark:text-gray-400" data-testid="image-credit">Photo: {found.credit.line}</p>
            )
            : <ImageCredit src={found.thumbnail_url} />}
          <figcaption className="-mt-2 text-xs text-gray-600 dark:text-gray-400"><Caption article={found} /></figcaption>
        </>
      ) : (
        <p className="rounded-xl border border-dashed p-4 text-center text-sm text-gray-500 dark:border-gray-700">
          No picture found for this lesson yet. Use Download or Upload below.
        </p>
      )}
      {showControls && (
        <PictureControls pictureKey={pictureKey} title={title} context={context} wikiTitle={wikiTitle}
          hasPicture={!!found} onSaved={(saved) => { setBroken(false); setArticle(saved); }} />
      )}
    </figure>
  );
}
