async function get(path) {
  const response = await fetch(`/api/lesson-enrichment${path}`);
  if (!response.ok) throw new Error(`Request failed (${response.status})`);
  return response.json();
}

export const ENRICHED_LEVELS = ['UG1', 'UG2', 'UG3', 'UG4', 'M1', 'M2'];
export const isEnrichedLevel = (level) => ENRICHED_LEVELS.includes(String(level || '').toUpperCase());

export const getLessonEnrichment = (level, lessonId) =>
  get(`/${encodeURIComponent(String(level).toUpperCase())}/${encodeURIComponent(lessonId)}`);

export function getRelatedArticle({ title, query }) {
  const params = new URLSearchParams();
  if (title) params.set('title', title);
  if (query) params.set('q', query);
  return get(`/wiki?${params}`);
}
