async function get(path) {
  const response = await fetch(`/api/lesson-enrichment${path}`);
  if (!response.ok) throw new Error(`Request failed (${response.status})`);
  return response.json();
}

// School Grades 6-10, College 1-2, Undergraduate 1-4 and Master's 1-2 (earlier grades are not enriched).
export const ENRICHED_LEVELS = ['6', '7', '8', '9', '10', 'C1', 'C2', 'UG1', 'UG2', 'UG3', 'UG4', 'M1', 'M2'];
export const isEnrichedLevel = (level) => ENRICHED_LEVELS.includes(String(level || '').toUpperCase());

export const getLessonEnrichment = (level, lessonId) =>
  get(`/${encodeURIComponent(String(level).toUpperCase())}/${encodeURIComponent(lessonId)}`);

export function getRelatedArticle({ title, query, context, key }) {
  const params = new URLSearchParams();
  if (title) params.set('title', title);
  if (query) params.set('q', query);
  if (context) params.set('ctx', context);
  if (key) params.set('key', key);
  return get(`/wiki?${params}`);
}

// ── The owner's own picture for a lesson (Download / Upload), kept in the database ──
export const STALE_SERVER_MESSAGE = 'The app is still running its old version. Close the black EduAi_Pro window, then open the EduAi_Pro shortcut again.';

async function readError(response, fallback) {
  if (response.status === 405) return STALE_SERVER_MESSAGE; // the running server predates this feature
  try {
    const body = await response.json();
    return typeof body.detail === 'string' ? body.detail : fallback;
  } catch {
    return fallback;
  }
}

async function send(url, init, fallback) {
  const response = await fetch(url, init);
  if (!response.ok) throw new Error(await readError(response, fallback));
  return response.json();
}

const json = (body) => ({ method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });

// Pictures found across many free collections, best fit first (nothing is saved yet).
export const searchLessonPictures = ({ key, title, context, wikiTitle, description, exclude }) =>
  send('/api/lesson-picture/search', json({
    key, title, context: context || '', wiki_title: wikiTitle || '', description: (description || '').slice(0, 800), exclude: exclude || [],
  }), 'Could not search for pictures.');

// Save the pictures the owner picked (the candidates exactly as the search returned them).
export const saveLessonPictures = (key, candidates) =>
  send('/api/lesson-picture/save', json({ key, pictures: candidates }), 'Could not save the pictures.');

export const uploadLessonPicture = (key, file) =>
  send(`/api/lesson-picture?key=${encodeURIComponent(key)}`, {
    method: 'PUT',
    headers: { 'Content-Type': file.type, 'X-Filename': encodeURIComponent(file.name) },
    body: file,
  }, 'Could not upload the picture.');

export const removeLessonPicture = (id) =>
  send(`/api/lesson-picture/${encodeURIComponent(id)}`, { method: 'DELETE' }, 'Could not remove the picture.');
