// Offline lessons: copies of a level's overview and subject data kept in the
// browser's Cache Storage. The same cache name is used by the service worker
// (vite.config.js), so lessons opened online are available offline as well,
// and "Save for offline" simply fetches everything for a level ahead of time.

export const OFFLINE_CACHE = 'eduai-offline-lessons';
const MANIFEST_KEY = 'eduai.offline.levels';

export const offlineSupported = () => typeof caches !== 'undefined';

function readManifest() {
  try {
    return JSON.parse(localStorage.getItem(MANIFEST_KEY) || '{}') || {};
  } catch {
    return {};
  }
}

function writeManifest(manifest) {
  try {
    localStorage.setItem(MANIFEST_KEY, JSON.stringify(manifest));
  } catch {
    /* storage unavailable: downloads still work, they just aren't listed */
  }
}

export const getDownloads = () => readManifest();
export const isLevelSaved = (levelId) => Boolean(readManifest()[String(levelId)]);

async function cachePut(url, response) {
  if (!offlineSupported()) return;
  try {
    const cache = await caches.open(OFFLINE_CACHE);
    await cache.put(url, response);
  } catch {
    /* quota exceeded or private mode */
  }
}

export async function cachedResponse(url) {
  if (!offlineSupported()) return null;
  try {
    return (await caches.match(url, { cacheName: OFFLINE_CACHE })) || null;
  } catch {
    return null;
  }
}

// Network first; when the network is unreachable (or the server is down) fall
// back to the saved copy. Resolves to { ok: true, data } or { ok: false,
// status } so callers can raise their own error for a genuine 4xx.
export async function fetchJsonWithOffline(url, { keep = false } = {}) {
  let response;
  try {
    response = await fetch(url);
  } catch (networkError) {
    const saved = await cachedResponse(url);
    if (saved) return { ok: true, data: await saved.json(), offline: true };
    throw networkError;
  }
  if (response.ok) {
    if (keep && typeof response.clone === 'function') await cachePut(url, response.clone());
    return { ok: true, data: await response.json() };
  }
  if (response.status >= 500) {
    const saved = await cachedResponse(url);
    if (saved) return { ok: true, data: await saved.json(), offline: true };
  }
  return { ok: false, status: response.status };
}

const overviewUrl = (levelId) => `/api/level/${encodeURIComponent(levelId)}/overview`;
const subjectUrl = (levelId, name) => `/api/level/${encodeURIComponent(levelId)}/subjects/${encodeURIComponent(name)}`;

export async function downloadLevel(levelId, { onProgress } = {}) {
  if (!offlineSupported()) throw new Error('This browser cannot save lessons for offline use.');
  const overviewResponse = await fetch(overviewUrl(levelId));
  if (!overviewResponse.ok) throw new Error('Could not download this level.');
  await cachePut(overviewUrl(levelId), overviewResponse.clone());
  const overview = await overviewResponse.json();
  const names = Object.keys(overview.subjects || {});
  let done = 0;
  onProgress?.(done, names.length);
  for (const name of names) {
    const response = await fetch(subjectUrl(levelId, name));
    if (!response.ok) throw new Error(`Could not download ${name}.`);
    await cachePut(subjectUrl(levelId, name), response);
    done += 1;
    onProgress?.(done, names.length);
  }
  const manifest = readManifest();
  manifest[String(levelId)] = { savedAt: new Date().toISOString(), subjects: names.length };
  writeManifest(manifest);
  return manifest[String(levelId)];
}

export async function removeLevel(levelId) {
  if (offlineSupported()) {
    try {
      const cache = await caches.open(OFFLINE_CACHE);
      const prefix = `/api/level/${encodeURIComponent(levelId)}/`;
      for (const request of await cache.keys()) {
        if (new URL(request.url).pathname.startsWith(prefix)) await cache.delete(request);
      }
    } catch {
      /* nothing to remove */
    }
  }
  const manifest = readManifest();
  delete manifest[String(levelId)];
  writeManifest(manifest);
}
