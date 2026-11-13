import React from 'react';
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import { downloadLevel, fetchJsonWithOffline, getDownloads, isLevelSaved, removeLevel, OFFLINE_CACHE } from '../src/utils/offlineLessons.js';
import { fetchLevelOverview, fetchLevelSubject } from '../src/api/level.js';
import OfflineDownload from '../src/components/OfflineDownload.jsx';

// Minimal in-memory Cache Storage: stores the JSON body per absolute URL.
function installFakeCaches() {
  const stores = new Map();
  const abs = (u) => new URL(String(u), 'http://localhost').href;
  const makeCache = (name) => {
    if (!stores.has(name)) stores.set(name, new Map());
    const map = stores.get(name);
    return {
      put: async (url, response) => { map.set(abs(url), await response.text()); },
      match: async (url) => (map.has(abs(url)) ? { json: async () => JSON.parse(map.get(abs(url))) } : undefined),
      keys: async () => [...map.keys()].map((url) => ({ url })),
      delete: async (request) => map.delete(request.url),
    };
  };
  globalThis.caches = {
    open: async (name) => makeCache(name),
    match: async (url, opts = {}) => (opts.cacheName ? makeCache(opts.cacheName).match(url) : undefined),
  };
  return { stores, abs };
}

const jsonResponse = (body, status = 200) => ({
  ok: status < 400, status,
  json: async () => body,
  text: async () => JSON.stringify(body),
  clone() { return this; },
});

const OVERVIEW = { level: '5', subjects: { Math: { lesson_count: 2 }, 'Physical Education & Self-Defense': { lesson_count: 1 } } };
const EMPTY_OVERVIEW = { level: '5', subjects: {} };
const SUBJECT = (name) => ({ level: '5', subject_name: name, subject: { __name: name, lessons: [{ id: `${name}-1`, title: 'L1' }] } });

function serverFor(routes) {
  return vi.fn(async (url) => {
    const key = String(url);
    if (!(key in routes)) return jsonResponse({ detail: 'nope' }, 404);
    const value = routes[key];
    if (value instanceof Error) throw value;
    return typeof value === 'number' ? jsonResponse({}, value) : jsonResponse(value);
  });
}

let fake;
beforeEach(() => { fake = installFakeCaches(); localStorage.clear(); });
afterEach(() => { vi.unstubAllGlobals(); delete globalThis.caches; });

describe('downloadLevel / removeLevel', () => {
  it('saves the overview and every subject, reports progress and records the download', async () => {
    vi.stubGlobal('fetch', serverFor({
      '/api/level/5/overview': OVERVIEW,
      '/api/level/5/subjects/Math': SUBJECT('Math'),
      '/api/level/5/subjects/Physical%20Education%20%26%20Self-Defense': SUBJECT('PE'),
    }));
    const progress = [];
    const entry = await downloadLevel('5', { onProgress: (d, t) => progress.push([d, t]) });
    expect(entry.subjects).toBe(2);
    expect(progress).toEqual([[0, 2], [1, 2], [2, 2]]);
    expect(isLevelSaved('5')).toBe(true);
    expect(getDownloads()['5'].subjects).toBe(2);
    expect([...fake.stores.get(OFFLINE_CACHE).keys()]).toHaveLength(3);
  });

  it('does not record a download when a subject fails', async () => {
    vi.stubGlobal('fetch', serverFor({ '/api/level/5/overview': OVERVIEW, '/api/level/5/subjects/Math': SUBJECT('Math') }));
    await expect(downloadLevel('5')).rejects.toThrow(/Could not download/);
    expect(isLevelSaved('5')).toBe(false);
  });

  it('removes only the chosen level', async () => {
    vi.stubGlobal('fetch', serverFor({
      '/api/level/5/overview': { subjects: {} }, '/api/level/6/overview': { subjects: {} },
    }));
    await downloadLevel('5');
    await downloadLevel('6');
    await removeLevel('5');
    const keys = [...fake.stores.get(OFFLINE_CACHE).keys()].map((k) => new URL(k).pathname);
    expect(keys).toEqual(['/api/level/6/overview']);
    expect(isLevelSaved('5')).toBe(false);
    expect(isLevelSaved('6')).toBe(true);
  });
});

describe('fetchJsonWithOffline and the level API', () => {
  it('uses the saved copy when the network is down, and errors when nothing is saved', async () => {
    vi.stubGlobal('fetch', serverFor({ '/api/level/5/overview': OVERVIEW, '/api/level/5/subjects/Math': SUBJECT('Math') }));
    await downloadLevel('5').catch(() => {});
    vi.stubGlobal('fetch', vi.fn(async () => { throw new TypeError('Failed to fetch'); }));
    expect((await fetchLevelOverview('5')).level).toBe('5');
    expect((await fetchLevelSubject('5', 'Math')).subject.__name).toBe('Math');
    await expect(fetchLevelSubject('5', 'Art')).rejects.toThrow(/Failed to fetch/);
  });

  it('serves the saved copy on a 5xx but reports a real 404', async () => {
    vi.stubGlobal('fetch', serverFor({ '/api/level/5/overview': EMPTY_OVERVIEW }));
    await downloadLevel('5');
    vi.stubGlobal('fetch', serverFor({ '/api/level/5/overview': 503, '/api/level/9/overview': 404 }));
    expect((await fetchLevelOverview('5')).level).toBe('5');
    await expect(fetchLevelOverview('9')).rejects.toThrow(/not available/);
  });

  it('keeps a saved level fresh when it is fetched online, but does not cache other levels', async () => {
    vi.stubGlobal('fetch', serverFor({ '/api/level/5/overview': EMPTY_OVERVIEW }));
    await downloadLevel('5');
    vi.stubGlobal('fetch', serverFor({ '/api/level/5/overview': { ...EMPTY_OVERVIEW, level: 'updated' }, '/api/level/6/overview': { level: '6', subjects: {} } }));
    await fetchLevelOverview('5');
    await fetchLevelOverview('6');
    const store = fake.stores.get(OFFLINE_CACHE);
    expect(JSON.parse(store.get(fake.abs('/api/level/5/overview'))).level).toBe('updated');
    expect(store.has(fake.abs('/api/level/6/overview'))).toBe(false);
  });

  it('plain fetchJsonWithOffline reports non-OK without data', async () => {
    vi.stubGlobal('fetch', serverFor({ '/x': 404 }));
    expect(await fetchJsonWithOffline('/x')).toEqual({ ok: false, status: 404 });
  });
});

describe('OfflineDownload', () => {
  it('saves a level, shows it as saved, and can remove it', async () => {
    vi.stubGlobal('fetch', serverFor({ '/api/level/5/overview': { subjects: { Math: {} } }, '/api/level/5/subjects/Math': SUBJECT('Math') }));
    render(<OfflineDownload level="5" levelLabel="Grade 5" />);
    fireEvent.click(screen.getByRole('button', { name: /save grade 5 for offline use/i }));
    expect((await screen.findByRole('status')).textContent).toMatch(/Grade 5 is saved for offline use \(1 subjects/);
    fireEvent.click(screen.getByRole('button', { name: 'Remove' }));
    expect(await screen.findByRole('button', { name: /save grade 5/i })).toBeTruthy();
    expect(isLevelSaved('5')).toBe(false);
  });

  it('shows an offline notice and disables saving while offline', async () => {
    render(<OfflineDownload level="5" levelLabel="Grade 5" />);
    act(() => { window.dispatchEvent(new Event('offline')); });
    expect(screen.getByRole('status').textContent).toMatch(/You are offline/);
    expect(screen.getByRole('button', { name: /save grade 5/i }).disabled).toBe(true);
    act(() => { window.dispatchEvent(new Event('online')); });
    expect(screen.queryByText(/You are offline/)).toBeNull();
  });

  it('shows an error if the download fails', async () => {
    vi.stubGlobal('fetch', serverFor({}));
    render(<OfflineDownload level="5" levelLabel="Grade 5" />);
    fireEvent.click(screen.getByRole('button', { name: /save grade 5/i }));
    expect((await screen.findByRole('alert')).textContent).toMatch(/could not download/i);
  });
});
