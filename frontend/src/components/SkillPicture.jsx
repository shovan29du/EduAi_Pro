import { useEffect, useRef, useState } from 'react';
import {
  getRelatedArticle, removeLessonPicture, saveLessonPictures, searchLessonPictures, uploadLessonPicture,
} from '../api/lessonEnrichment.js';
import ImageCredit from './ImageCredit.jsx';

// Pictures for a lesson (Survival Skills, Practical Skills, subject lessons).
//
// By default it is the closest Wikipedia article's freely licensed picture. With
// `pictureKey` the owner can give the lesson pictures of their own, as many as they like:
//   Download pictures - searches many free collections (Wikimedia Commons, Openverse, museum
//                       collections, NASA, the Library of Congress, Wikipedia), shows what it
//                       found with a "Good / Possible / Weak match" label for how well each fits
//                       the lesson's topic and description, and saves the ones that are ticked.
//   Upload pictures   - saves pictures from the owner's computer.
// Saved pictures are kept in the database and shown instead of the automatic one.
const cache = new Map();
export const clearSkillPictureCache = () => cache.clear(); // for tests
export const MAX_PICTURE_BYTES = 8 * 1024 * 1024;

function useArticle(title, query, context, pictureKey, enabled) {
  const key = `${title}|${query}|${context}|${pictureKey}`;
  const [article, setArticleState] = useState(cache.get(key) ?? undefined);
  const [reload, setReload] = useState(0);
  useEffect(() => {
    if (!enabled) return undefined;
    if (cache.has(key)) { setArticleState(cache.get(key)); return undefined; }
    let active = true;
    getRelatedArticle({ title, query, context, key: pictureKey })
      .then((a) => {
        const found = a?.available && a.thumbnail_url ? a : null;
        cache.set(key, found);
        if (active) setArticleState(found);
      })
      .catch(() => { if (active) setArticleState(null); }); // not cached: a dropped connection can retry
    return () => { active = false; };
  }, [key, title, query, context, pictureKey, enabled, reload]);
  const setArticle = (next) => { cache.set(key, next); setArticleState(next); };
  const refresh = () => { cache.delete(key); setArticleState(undefined); setReload((n) => n + 1); };
  return [article, setArticle, refresh];
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

const BADGE = {
  'Good match': 'bg-green-100 text-green-800',
  'Possible match': 'bg-amber-100 text-amber-800',
  'Weak match': 'bg-gray-200 text-gray-700',
};

function Credit({ credit }) {
  return credit?.line ? <p className="text-xs text-gray-500 dark:text-gray-400" data-testid="image-credit">Photo: {credit.line}</p> : null;
}

function SavedPicture({ picture, onRemove, busy }) {
  const upload = picture.source === 'upload';
  const label = /wikipedia\.org/.test(picture.page_url || '') ? 'Wikipedia' : 'Source';
  return (
    <figure className="min-w-0" data-testid="saved-picture">
      <img src={picture.url} alt={picture.title} loading="lazy"
        className="h-40 w-full rounded-lg bg-gray-50 object-contain dark:bg-gray-800" />
      <figcaption className="mt-1 text-xs text-gray-600 dark:text-gray-400">
        {upload ? `Your uploaded picture: ${picture.title}` : `Saved picture: ${picture.title}`}
        {picture.source_name ? ` · from ${picture.source_name}` : ''}
        {picture.page_url && <> · <a href={picture.page_url} target="_blank" rel="noopener noreferrer" className="underline">{label}</a></>}
      </figcaption>
      <Credit credit={picture.credit} />
      {onRemove && (
        <button type="button" onClick={() => onRemove(picture)} disabled={busy}
          className="mt-1 text-xs text-red-600 underline disabled:opacity-50" aria-label={`Remove picture ${picture.title}`}>
          Remove
        </button>
      )}
    </figure>
  );
}

function Picker({ search, onClose, onSaved, savedCount, max }) {
  const [state, setState] = useState({ status: 'loading', candidates: [], error: '' });
  const [chosen, setChosen] = useState(new Set());
  const [saving, setSaving] = useState(false);
  const [more, setMore] = useState(false);
  const [broken, setBroken] = useState(new Set());
  const seen = useRef([]);

  async function load(append) {
    if (append) setMore(true); else setState({ status: 'loading', candidates: [], error: '' });
    try {
      const result = await search(append ? seen.current : []);
      seen.current = [...seen.current, ...result.candidates.map((c) => c.url)];
      setState((prev) => ({ status: 'ready', error: '', candidates: append ? [...prev.candidates, ...result.candidates] : result.candidates }));
    } catch (err) {
      setState((prev) => ({ ...prev, status: 'error', error: err.message || 'Could not search for pictures.' }));
    } finally {
      setMore(false);
    }
  }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => { seen.current = []; load(false); }, []);

  const toggle = (url) => setChosen((prev) => { const next = new Set(prev); if (next.has(url)) next.delete(url); else next.add(url); return next; });
  const visible = state.candidates.filter((c) => !broken.has(c.url));
  const room = max - savedCount;

  async function save() {
    setSaving(true);
    try {
      const picked = state.candidates.filter((c) => chosen.has(c.url));
      const result = await onSaved(picked);
      if (result?.ok) onClose();
      else setState((prev) => ({ ...prev, error: result?.error || '' }));
    } finally {
      setSaving(false);
    }
  }

  return (
    <section aria-label="Pictures found" className="mt-3 rounded-xl border border-indigo-200 bg-indigo-50/50 p-3 dark:border-indigo-800 dark:bg-gray-900">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h6 className="text-sm font-semibold">Pictures found for this lesson — tick the ones you want to keep</h6>
        <button type="button" onClick={onClose} className="text-sm underline">Close</button>
      </div>
      <p className="mt-1 text-xs text-gray-600 dark:text-gray-400">
        Each picture is marked for how well it fits the lesson&apos;s topic and description. Check the picture before you keep it.
      </p>
      {state.status === 'loading' && <p role="status" className="mt-3 text-sm text-gray-600">Searching Wikipedia, Wikimedia Commons, Openverse, museums, NASA and more…</p>}
      {state.status === 'error' && state.candidates.length === 0 && <p role="alert" className="mt-3 text-sm text-red-600">{state.error}</p>}
      {state.status === 'ready' && visible.length === 0 && (
        <p className="mt-3 text-sm text-gray-600">No pictures were found. You can upload one instead.</p>
      )}
      {visible.length > 0 && (
        <ul className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">
          {visible.map((c) => (
            <li key={c.url} className={`rounded-lg border bg-white p-2 dark:bg-gray-800 ${chosen.has(c.url) ? 'border-indigo-500 ring-2 ring-indigo-300' : 'border-gray-200 dark:border-gray-700'}`}>
              <label className="block cursor-pointer">
                <img src={c.url} alt={c.title} loading="lazy" referrerPolicy="no-referrer"
                  onError={() => setBroken((prev) => new Set(prev).add(c.url))}
                  className="h-32 w-full rounded bg-gray-50 object-contain dark:bg-gray-700" />
                <span className="mt-1 flex items-start gap-1.5 text-xs">
                  <input type="checkbox" checked={chosen.has(c.url)} onChange={() => toggle(c.url)} aria-label={`Keep ${c.title}`}
                    disabled={!chosen.has(c.url) && chosen.size >= room} className="mt-0.5" />
                  <span className="min-w-0">
                    <span className="block truncate font-medium" title={c.title}>{c.title}</span>
                    <span className={`inline-block rounded-full px-1.5 py-0.5 text-[10px] font-semibold ${BADGE[c.match] || BADGE['Weak match']}`}>{c.match}</span>
                    <span className="block text-gray-500">from {c.source}</span>
                    {c.credit?.line && <span className="block truncate text-gray-500" title={c.credit.line}>{c.credit.line}</span>}
                  </span>
                </span>
              </label>
            </li>
          ))}
        </ul>
      )}
      {state.error && state.candidates.length > 0 && <p role="alert" className="mt-2 text-sm text-red-600">{state.error}</p>}
      <div className="mt-3 flex flex-wrap items-center gap-2">
        <button type="button" onClick={save} disabled={chosen.size === 0 || saving}
          className="rounded-lg bg-indigo-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-indigo-700 disabled:opacity-50">
          {saving ? 'Saving…' : `Save selected (${chosen.size})`}
        </button>
        <button type="button" onClick={() => load(true)} disabled={more || state.status === 'loading'}
          className="rounded-lg border border-gray-300 px-3 py-1.5 text-sm font-medium hover:bg-gray-50 disabled:opacity-50 dark:border-gray-600">
          {more ? 'Searching…' : 'Show more pictures'}
        </button>
        <span className="text-xs text-gray-500">{savedCount} of {max} saved</span>
      </div>
    </section>
  );
}

function PictureControls({ pictureKey, title, context, wikiTitle, description, saved, onChange }) {
  const [busy, setBusy] = useState('');
  const [message, setMessage] = useState(null);
  const [picking, setPicking] = useState(false);
  const fileInput = useRef(null);
  const max = 12;

  async function upload(event) {
    const files = Array.from(event.target.files || []);
    event.target.value = '';
    if (files.length === 0) return;
    const bad = files.find((f) => !/^image\/(jpeg|png|webp|gif)$/.test(f.type));
    if (bad) { setMessage({ kind: 'error', text: 'Choose JPEG, PNG, WebP or GIF pictures.' }); return; }
    if (files.some((f) => f.size > MAX_PICTURE_BYTES)) { setMessage({ kind: 'error', text: 'A picture is too large (limit 8 MB each).' }); return; }
    setBusy('upload');
    setMessage(null);
    let latest = null;
    let added = 0;
    try {
      for (const file of files) {
        latest = await uploadLessonPicture(pictureKey, file);
        if (latest.added) added += 1;
      }
      onChange(latest);
      setMessage({ kind: 'ok', text: added === 0 ? 'Those pictures were already saved.' : `${added === 1 ? 'Picture' : `${added} pictures`} uploaded and saved in the database.` });
    } catch (err) {
      if (latest) onChange(latest);
      setMessage({ kind: 'error', text: err.message || 'Could not upload the picture.' });
    } finally {
      setBusy('');
    }
  }

  async function saveChosen(candidates) {
    try {
      const result = await saveLessonPictures(pictureKey, candidates);
      onChange(result);
      const failed = result.failed?.length || 0;
      setMessage({
        kind: failed ? 'error' : 'ok',
        text: `${result.saved} ${result.saved === 1 ? 'picture' : 'pictures'} saved in the database.`
          + (result.already_saved ? ` ${result.already_saved} already saved.` : '')
          + (failed ? ` ${failed} could not be downloaded.` : ''),
      });
      return { ok: true };
    } catch (err) {
      return { ok: false, error: err.message || 'Could not save the pictures.' };
    }
  }

  async function remove(picture) {
    if (!window.confirm(`Remove “${picture.title}” from this lesson?`)) return;
    setBusy('remove');
    setMessage(null);
    try {
      onChange(await removeLessonPicture(picture.id), true);
      setMessage({ kind: 'ok', text: 'Picture removed.' });
    } catch (err) {
      setMessage({ kind: 'error', text: err.message || 'Could not remove the picture.' });
    } finally {
      setBusy('');
    }
  }

  const button = 'rounded-lg border px-3 py-1.5 text-sm font-medium disabled:opacity-50';
  return (
    <div className="mt-2" aria-label="Picture controls">
      {saved.length > 0 && (
        <div className="mb-3 grid grid-cols-2 gap-3 sm:grid-cols-3">
          {saved.map((p) => <SavedPicture key={p.id} picture={p} onRemove={remove} busy={!!busy} />)}
        </div>
      )}
      <div className="flex flex-wrap gap-2">
        <button type="button" onClick={() => { setPicking(true); setMessage(null); }} disabled={!!busy || picking}
          className={`${button} border-indigo-300 bg-indigo-50 text-indigo-700 hover:bg-indigo-100`}>
          ⬇ Download pictures
        </button>
        <button type="button" onClick={() => fileInput.current?.click()} disabled={!!busy}
          className={`${button} border-emerald-300 bg-emerald-50 text-emerald-700 hover:bg-emerald-100`}>
          {busy === 'upload' ? 'Uploading…' : '⬆ Upload pictures'}
        </button>
        <input ref={fileInput} type="file" multiple accept="image/jpeg,image/png,image/webp,image/gif" onChange={upload}
          className="hidden" aria-label="Choose pictures to upload" data-testid="picture-file-input" />
      </div>
      {picking && (
        <Picker max={max} savedCount={saved.length} onClose={() => setPicking(false)} onSaved={saveChosen}
          search={(exclude) => searchLessonPictures({ key: pictureKey, title, context, wikiTitle, description, exclude })} />
      )}
      {message && (
        <p role={message.kind === 'error' ? 'alert' : 'status'}
          className={`mt-2 text-sm ${message.kind === 'error' ? 'text-red-600' : 'text-emerald-700'}`}>
          {message.text}
        </p>
      )}
    </div>
  );
}

export default function SkillPicture({ title, wikiTitle = '', context = '', description = '', size = 'hero', pictureKey = '', controls = false }) {
  const ref = useRef(null);
  const visible = useVisible(ref, size === 'hero');
  const [article, setArticle, refresh] = useArticle(wikiTitle, title, context, pictureKey, visible && !!title);
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
  const saved = found?.stored ? found.pictures || [] : [];
  const onChange = (next, mayBeEmpty) => {
    setBroken(false);
    if (next?.stored) setArticle(next);
    else if (mayBeEmpty) refresh(); // the last saved picture was removed: back to the automatic one
  };
  return (
    <figure ref={ref} className="mt-3" data-testid="skill-picture">
      {found && !found.stored && (
        <>
          <img src={found.thumbnail_url} alt={found.title} onError={() => setBroken(true)}
            className="max-h-64 w-full rounded-xl bg-gray-50 object-contain dark:bg-gray-800" />
          <ImageCredit src={found.thumbnail_url} />
          <figcaption className="-mt-2 text-xs text-gray-600 dark:text-gray-400">
            Picture: {found.title}{found.description ? ` — ${found.description}` : ''}
            {found.page_url && <> · <a href={found.page_url} target="_blank" rel="noopener noreferrer" className="underline">{/wikipedia\.org/.test(found.page_url) ? 'Wikipedia' : 'Source'}</a></>}
          </figcaption>
        </>
      )}
      {!found && (
        <p className="rounded-xl border border-dashed p-4 text-center text-sm text-gray-500 dark:border-gray-700">
          No picture found for this lesson yet. Use Download or Upload below.
        </p>
      )}
      {showControls && (
        <PictureControls pictureKey={pictureKey} title={title} context={context} wikiTitle={wikiTitle} description={description}
          saved={saved} onChange={onChange} />
      )}
    </figure>
  );
}
