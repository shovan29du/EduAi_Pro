export async function listResourceTabDocuments() {
  const res = await fetch('/api/resource-tab');
  if (!res.ok) throw new Error('Could not load uploaded documents');
  return res.json();
}

export async function uploadResourceTabDocument(file) {
  const formData = new FormData();
  formData.append('file', file);
  const res = await fetch('/api/resource-tab/upload', { method: 'POST', body: formData });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Upload failed');
  }
  return res.json();
}

export async function deleteResourceTabDocument(id) {
  const res = await fetch(`/api/resource-tab/${id}`, { method: 'DELETE' });
  if (!res.ok) throw new Error('Could not delete document');
  return res.json();
}

export function resourceTabDownloadUrl(id) {
  return `/api/resource-tab/${id}/download`;
}

export async function askCourseAssistant(documentIds, question, levelArgs = {}) {
  const res = await fetch('/api/resource-tab/course-assistant/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ document_ids: documentIds, question, ...levelArgs }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Could not ask the course assistant');
  }
  return res.json();
}

export async function listCourseProviders(query = '') {
  const res = await fetch(`/api/course-providers?query=${encodeURIComponent(query)}`);
  if (!res.ok) throw new Error('Could not load course providers');
  return res.json();
}

async function responseError(res, fallback) {
  const body = await res.json().catch(() => ({}));
  if (typeof body.detail === 'string' && body.detail.trim()) return body.detail;
  if (Array.isArray(body.detail)) {
    return body.detail.map((item) => item.msg || String(item)).join('; ');
  }
  return `${fallback} (HTTP ${res.status || 'error'})`;
}

export async function scanLocalLibrary(folder, analyseBooks = true) {
  let res;
  try {
    res = await fetch('/api/local-library/scan', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ folder, analyse_books: analyseBooks }),
    });
  } catch {
    throw new Error('Cannot reach EduAI_Pro. Make sure the backend is running, then try again');
  }
  if (!res.ok) {
    throw new Error(await responseError(res, 'Could not scan the folder'));
  }
  return res.json();
}

export async function selectLocalLibraryFolder() {
  let res;
  try {
    res = await fetch('/api/local-library/select-folder', { method: 'POST' });
  } catch {
    throw new Error('Cannot reach EduAI_Pro. Make sure the backend is running');
  }
  if (!res.ok) {
    throw new Error(await responseError(res, 'Could not open the folder picker'));
  }
  return res.json();
}

export async function listLocalLibrary(category = '', query = '') {
  const params = new URLSearchParams();
  if (category) params.set('category', category);
  if (query) params.set('query', query);
  const res = await fetch(`/api/local-library?${params}`);
  if (!res.ok) throw new Error('Could not load the local library');
  return res.json();
}

export async function analyzeLocalLibraryFile(id) {
  const res = await fetch(`/api/local-library/files/${id}/analyze`, { method: 'POST' });
  if (!res.ok) {
    throw new Error(await responseError(res, 'Could not analyze this book'));
  }
  return res.json();
}
