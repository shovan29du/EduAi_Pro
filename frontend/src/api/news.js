async function request(path, options) {
  const response = await fetch(`/api/news${path}`, options);
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.detail || `Request failed (${response.status})`);
  }
  return response.json();
}

export const getNewsSources = () => request('/sources');

export const getNewsPreferences = () => request('/preferences');

export const saveNewsPreferences = (categories, sources) =>
  request('/preferences', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ categories, sources }),
  });

export function getNews({ categories = [], sources = [], limit = 30 } = {}) {
  const params = new URLSearchParams();
  if (categories.length) params.set('categories', categories.join(','));
  if (sources.length) params.set('sources', sources.join(','));
  params.set('limit', String(limit));
  return request(`?${params.toString()}`);
}
