import { useEffect, useReducer, useRef, useState } from 'react';

const API = '/api';
export const MAX_PICTURE_BYTES = 8 * 1024 * 1024;
export const PICTURE_TYPES = 'image/jpeg,image/png,image/webp,image/gif';

// What the owner has changed this session, so the gallery grid, the search
// results and "Featured today" update straight away instead of showing the
// old picture or a deleted object until the page is reloaded.
const deleted = new Set();
const pictures = new Map();
const listeners = new Set();
const announce = () => listeners.forEach((fn) => fn());

export function resetMuseumChanges() { // for tests
  deleted.clear();
  pictures.clear();
}

export function useMuseumChanges() {
  const [, rerender] = useReducer((n) => n + 1, 0);
  useEffect(() => { listeners.add(rerender); return () => { listeners.delete(rerender); }; }, []);
  return {
    isDeleted: (gallery, id) => deleted.has(`${gallery}/${id}`),
    withPicture: (obj) => (pictures.has(obj.id) ? { ...obj, thumbnail_local: pictures.get(obj.id) } : obj),
  };
}

async function errorText(response, fallback) {
  if (response.status === 405) return 'The app is still running its old version. Close the black EduAi_Pro window, then open the EduAi_Pro shortcut again.';
  try {
    const body = await response.json();
    return typeof body.detail === 'string' ? body.detail : fallback;
  } catch {
    return fallback;
  }
}

// Download / Upload / Delete for one museum object. Download searches every free image
// collection (not only Wikipedia); pressing it again gives the next different picture. Pictures are saved in the
// database (not as loose files), and deleting asks first.
export default function MuseumObjectControls({ gallery, obj, onPictureChanged, onDeleted }) {
  const [busy, setBusy] = useState('');
  const [message, setMessage] = useState(null); // { kind: 'ok' | 'error', text }
  const [confirming, setConfirming] = useState(false);
  const fileInput = useRef(null);
  const base = `${API}/museum/${encodeURIComponent(gallery)}/${encodeURIComponent(obj.id)}`;

  const pictureChanged = (updated) => {
    if (updated?.thumbnail_local) pictures.set(obj.id, updated.thumbnail_local);
    announce();
    onPictureChanged?.(updated);
  };

  async function download() {
    if (obj.picture_source === 'upload'
      && !window.confirm('Replace the picture you uploaded with one from the Internet?')) return;
    setBusy('download');
    setMessage(null);
    try {
      const response = await fetch(`${base}/picture/download`, { method: 'POST' });
      if (!response.ok) throw new Error(await errorText(response, 'Could not download a picture.'));
      pictureChanged(await response.json());
      setMessage({ kind: 'ok', text: 'Picture downloaded and saved in the database.' });
    } catch (err) {
      setMessage({ kind: 'error', text: err.message || 'Could not download a picture.' });
    } finally {
      setBusy('');
    }
  }

  async function upload(event) {
    const file = event.target.files?.[0];
    event.target.value = '';
    if (!file) return;
    if (!/^image\/(jpeg|png|webp|gif)$/.test(file.type)) {
      setMessage({ kind: 'error', text: 'Choose a JPEG, PNG, WebP or GIF picture.' });
      return;
    }
    if (file.size > MAX_PICTURE_BYTES) {
      setMessage({ kind: 'error', text: 'That picture is too large (limit 8 MB).' });
      return;
    }
    setBusy('upload');
    setMessage(null);
    try {
      const response = await fetch(`${base}/picture`, {
        method: 'PUT',
        headers: { 'Content-Type': file.type, 'X-Filename': encodeURIComponent(file.name) },
        body: file,
      });
      if (!response.ok) throw new Error(await errorText(response, 'Could not upload the picture.'));
      pictureChanged(await response.json());
      setMessage({ kind: 'ok', text: 'Picture uploaded and saved in the database.' });
    } catch (err) {
      setMessage({ kind: 'error', text: err.message || 'Could not upload the picture.' });
    } finally {
      setBusy('');
    }
  }

  async function remove() {
    setBusy('delete');
    setMessage(null);
    try {
      const response = await fetch(`${base}?confirm=true`, { method: 'DELETE' });
      if (!response.ok) throw new Error(await errorText(response, 'Could not delete this object.'));
      deleted.add(`${gallery}/${obj.id}`);
      announce();
      onDeleted?.();
    } catch (err) {
      setConfirming(false);
      setMessage({ kind: 'error', text: err.message || 'Could not delete this object.' });
      setBusy('');
    }
  }

  const button = 'rounded-lg border px-3 py-1.5 text-sm font-medium disabled:opacity-50';
  return (
    <section aria-label="Picture and object controls" className="my-4">
      <div className="flex flex-wrap gap-2">
        <button type="button" onClick={download} disabled={!!busy}
          className={`${button} border-indigo-300 bg-indigo-50 text-indigo-700 hover:bg-indigo-100`}>
          {busy === 'download' ? 'Downloading…' : obj.picture_source === 'download' ? '⬇ Download another picture' : '⬇ Download picture'}
        </button>
        <button type="button" onClick={() => fileInput.current?.click()} disabled={!!busy}
          className={`${button} border-emerald-300 bg-emerald-50 text-emerald-700 hover:bg-emerald-100`}>
          {busy === 'upload' ? 'Uploading…' : '⬆ Upload picture'}
        </button>
        <input ref={fileInput} type="file" accept={PICTURE_TYPES} onChange={upload} className="hidden"
          aria-label="Choose a picture to upload" data-testid="picture-file-input" />
        <button type="button" onClick={() => { setConfirming(true); setMessage(null); }} disabled={!!busy || confirming}
          className={`${button} border-red-300 bg-red-50 text-red-700 hover:bg-red-100`}>
          🗑 Delete
        </button>
      </div>
      {confirming && (
        <div role="alertdialog" aria-label="Confirm delete" className="mt-3 rounded-lg border border-red-300 bg-red-50 p-3 text-sm text-red-800">
          <p>Delete “{obj.name}” from the museum? Its picture is deleted too. This cannot be undone.</p>
          <div className="mt-2 flex gap-2">
            <button type="button" onClick={remove} disabled={busy === 'delete'}
              className="rounded-lg bg-red-600 px-3 py-1.5 font-medium text-white hover:bg-red-700 disabled:opacity-50">
              {busy === 'delete' ? 'Deleting…' : 'Yes, delete'}
            </button>
            <button type="button" onClick={() => setConfirming(false)} disabled={busy === 'delete'}
              className="rounded-lg border border-gray-300 bg-white px-3 py-1.5 font-medium text-gray-700 hover:bg-gray-50">
              Cancel
            </button>
          </div>
        </div>
      )}
      {message && (
        <p role={message.kind === 'error' ? 'alert' : 'status'}
          className={`mt-2 text-sm ${message.kind === 'error' ? 'text-red-600' : 'text-emerald-700'}`}>
          {message.text}
        </p>
      )}
    </section>
  );
}
