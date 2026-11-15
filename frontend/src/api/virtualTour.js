async function get(path) {
  const response = await fetch(`/api/virtual-tour${path}`);
  if (!response.ok) throw new Error(`Request failed (${response.status})`);
  return response.json();
}

export const getTourOverview = () => get('');
export const getTourCountries = () => get('/countries');
export const getCountryTour = (code) => get(`/countries/${encodeURIComponent(code)}`);
export const searchTour = (query) => get(`/search?q=${encodeURIComponent(query)}`);
export const getLiveWeather = (code) => get(`/weather/${encodeURIComponent(code)}`);
export const getExchangeRate = (code) => get(`/rates/${encodeURIComponent(code)}`);

export function getRoadTrips({ continent = '', country = '', kind = '', q = '' } = {}) {
  const params = new URLSearchParams();
  if (continent) params.set('continent', continent);
  if (country) params.set('country', country);
  if (kind) params.set('kind', kind);
  if (q) params.set('q', q);
  const query = params.toString();
  return get(`/road-trips${query ? `?${query}` : ''}`);
}
