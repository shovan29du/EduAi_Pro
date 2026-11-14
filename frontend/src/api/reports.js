async function request(path, options) {
  const response = await fetch(`/api/reports${path}`, options);
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(typeof body.detail === 'string' ? body.detail : `Request failed (${response.status})`);
  }
  return response.json();
}

const jsonOptions = (method, body) => ({
  method,
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(body),
});

export const submitReport = (report) => request('', jsonOptions('POST', report));
export const listReports = (status = '') => request(status ? `?status=${encodeURIComponent(status)}` : '');
export const setReportStatus = (id, status) => request(`/${encodeURIComponent(id)}`, jsonOptions('PATCH', { status }));
