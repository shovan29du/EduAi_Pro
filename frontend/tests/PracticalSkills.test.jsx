import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor, within } from '@testing-library/react';
import PracticalSkills from '../src/components/PracticalSkills.jsx';
import { clearSkillPictureCache } from '../src/components/SkillPicture.jsx';

const overview = {
  description: 'Real-world skills for every age.',
  pathways: [{ id: 'cooking', label: 'Cooking', emoji: '🍳', module_count: 1 }],
};

const pathwayData = {
  description: 'Learn to cook safely and well.',
  modules: [
    {
      title: 'Kitchen Safety Basics',
      description: 'Learn the basic rules to stay safe in the kitchen.',
      level: 'beginner',
      grade_range: '1-2',
      duration_minutes: 30,
      wiki_title: 'Kitchen Safety Basics',
      steps: ['Learn about hot surfaces', 'Wash hands before cooking'],
      materials_needed: ['cutting board', 'soap'],
      data_table: { headers: ['Hazard', 'Prevention'], rows: [['Hot pans', 'Use oven mitts']] },
      formulae: ['Wash hands for at least 20 seconds'],
      quiz: [{ q: 'Why wash hands?', a: 'To remove germs' }],
    },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    if (url === '/api/practical-skills') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (url === '/api/practical-skills/cooking') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(pathwayData) });
    }
    if (String(url).startsWith('/api/lesson-enrichment/wiki')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ available: true, title: 'Picture of kitchen', description: 'A test article', page_url: 'https://en.wikipedia.org/wiki/Test', thumbnail_url: 'https://example.com/kitchen.jpg' }) });
    }
    if (String(url).startsWith('/api/museum/credit')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ known: false }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  clearSkillPictureCache();
  global.fetch = mockFetch();
});

describe('PracticalSkills', () => {
  it('browses into a pathway and shows a module card with a real photo thumbnail', async () => {
    const { container } = render(<PracticalSkills />);
    await waitFor(() => expect(screen.getByText('Cooking')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Cooking'));

    await waitFor(() => expect(screen.getByText('Kitchen Safety Basics')).toBeInTheDocument());
    await waitFor(() => expect(container.querySelector('img[src="https://example.com/kitchen.jpg"]')).toBeInTheDocument());
  });

  it('opens a module and shows Quick Facts, a reference table, and key facts', async () => {
    render(<PracticalSkills />);
    await waitFor(() => expect(screen.getByText('Cooking')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Cooking'));
    await waitFor(() => expect(screen.getByText('Kitchen Safety Basics')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Kitchen Safety Basics'));

    await waitFor(() => expect(screen.getByRole('heading', { name: 'Kitchen Safety Basics' })).toBeInTheDocument());

    // Quick Facts infographic (derived from existing fields)
    expect(screen.getByText('Duration')).toBeInTheDocument();
    expect(screen.getByText('30 min')).toBeInTheDocument();
    expect(screen.getAllByText('Steps').length).toBeGreaterThan(0);

    // Reference table
    expect(screen.getByRole('columnheader', { name: 'Hazard' })).toBeInTheDocument();
    expect(screen.getByRole('cell', { name: 'Use oven mitts' })).toBeInTheDocument();

    // Key facts (formulae)
    expect(screen.getByText('Wash hands for at least 20 seconds')).toBeInTheDocument();
  });
});


describe('PracticalSkills lesson picture', () => {
  it('shows a captioned, credited picture on the lesson page and searches with the subject', async () => {
    render(<PracticalSkills />);
    await waitFor(() => expect(screen.getByText('Cooking')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Cooking'));
    await waitFor(() => expect(screen.getByText('Kitchen Safety Basics')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Kitchen Safety Basics'));

    const figure = await screen.findByTestId('skill-picture');
    expect(figure.querySelector('img').getAttribute('src')).toMatch(/^https:\/\/example\.com\/.+\.jpg$/);
    expect(figure).toHaveTextContent('Picture: Picture of');
    expect(screen.getAllByRole('link', { name: 'Wikipedia' })[0]).toHaveAttribute('href', 'https://en.wikipedia.org/wiki/Test');
    const lookup = global.fetch.mock.calls.map((c) => String(c[0])).find((u) => u.startsWith('/api/lesson-enrichment/wiki'));
    const params = new URLSearchParams(lookup.split('?')[1]);
    expect(params.get('q')).toBe('Kitchen Safety Basics');
    expect(params.get('ctx')).toBe('Cooking');
  });

  it('shows a placeholder with Download and Upload when nothing matches', async () => {
    const base = global.fetch;
    global.fetch = vi.fn((url, ...rest) => String(url).startsWith('/api/lesson-enrichment/wiki')
      ? Promise.resolve({ ok: true, json: () => Promise.resolve({ available: false }) })
      : base(url, ...rest));
    render(<PracticalSkills />);
    await waitFor(() => expect(screen.getByText('Cooking')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Cooking'));
    await waitFor(() => expect(screen.getByText('Kitchen Safety Basics')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Kitchen Safety Basics'));
    await screen.findByRole('heading', { name: 'Kitchen Safety Basics' });
    expect(screen.getByText(/No picture found for this lesson yet/)).toBeInTheDocument(); // placeholder, so Download/Upload are still there
    expect(screen.getByRole('button', { name: /Download picture/ })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Upload picture/ })).toBeInTheDocument();
  });
});

describe('PracticalSkills Download and Upload pictures', () => {
  const KEY = 'practical/cooking/Kitchen Safety Basics';
  const saved = (items) => ({ available: true, stored: true, source: items[0].source, title: items[0].title, thumbnail_url: items[0].url, pictures: items });
  const item = (n, source = 'download') => ({ id: `id${n}`, url: `/api/lesson-picture/id${n}/image?v=1`, source, title: `Photo ${n}`, source_name: source === 'upload' ? '' : 'Openverse (flickr)', page_url: source === 'upload' ? '' : `https://flickr.example/p/${n}`, credit: { line: `Person ${n} · CC BY 2.0` } });
  const candidate = (n, match, score) => ({ url: `https://img.example/${n}.jpg`, token: `t${n}`, fallback_url: '', fallback_token: '', title: `Candidate ${n}`, source: 'Wikimedia Commons', score, match, credit: { line: `Person ${n} · CC BY-SA 4.0` }, page_url: `https://page.example/${n}` });

  async function openLesson(handler) {
    const base = global.fetch;
    global.fetch = vi.fn((url, init) => (String(url).startsWith('/api/lesson-picture') ? Promise.resolve(handler(String(url), init || {})) : base(url, init)));
    render(<PracticalSkills />);
    await waitFor(() => expect(screen.getByText('Cooking')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Cooking'));
    await waitFor(() => expect(screen.getByText('Kitchen Safety Basics')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Kitchen Safety Basics'));
    await screen.findByRole('button', { name: /Download pictures/ });
  }
  const reply = (body, ok = true, status = 200) => ({ ok, status, json: () => Promise.resolve(body) });
  const calls = (method, fragment) => global.fetch.mock.calls.filter((c) => (c[1]?.method || 'GET') === method && String(c[0]).includes(fragment));

  it('Download shows several pictures, marked for how well they fit, and saves the ticked ones', async () => {
    await openLesson((url, init) => {
      if (url.endsWith('/search')) return reply({ candidates: [candidate(1, 'Good match', 0.9), candidate(2, 'Possible match', 0.4), candidate(3, 'Weak match', 0.05)], max: 12, saved: 0 });
      if (url.endsWith('/save')) return reply({ ...saved([item(1), item(2)]), saved: 2, already_saved: 0, failed: [] });
      return reply({});
    });
    fireEvent.click(screen.getByRole('button', { name: /Download pictures/ }));
    expect(await screen.findByText('Candidate 1')).toBeInTheDocument();
    expect(screen.getByText('Good match')).toBeInTheDocument();
    expect(screen.getByText('Possible match')).toBeInTheDocument();
    expect(screen.getByText('Weak match')).toBeInTheDocument();
    const search = JSON.parse(calls('POST', '/search')[0][1].body);
    expect(search.key).toBe(KEY);
    expect(search.title).toBe('Kitchen Safety Basics');
    expect(search.context).toBe('Cooking');
    expect(search.description.length).toBeGreaterThan(0);

    expect(screen.getByRole('button', { name: 'Save selected (0)' })).toBeDisabled();
    fireEvent.click(screen.getByRole('checkbox', { name: 'Keep Candidate 1' }));
    fireEvent.click(screen.getByRole('checkbox', { name: 'Keep Candidate 2' }));
    fireEvent.click(screen.getByRole('button', { name: 'Save selected (2)' }));
    expect(await screen.findByText(/2 pictures saved in the database/)).toBeInTheDocument();
    const sent = JSON.parse(calls('POST', '/save')[0][1].body);
    expect(sent.key).toBe(KEY);
    expect(sent.pictures.map((p) => p.url)).toEqual(['https://img.example/1.jpg', 'https://img.example/2.jpg']);
    expect(sent.pictures[0].token).toBe('t1');
    const shown = await screen.findAllByTestId('saved-picture');
    expect(shown).toHaveLength(2);
    expect(shown[0]).toHaveTextContent('Saved picture: Photo 1 · from Openverse (flickr)');
    expect(within(shown[0]).getByRole('link', { name: 'Source' })).toHaveAttribute('href', 'https://flickr.example/p/1');
    expect(screen.queryByText('Candidate 1')).not.toBeInTheDocument(); // the chooser closed
  });

  it('Show more pictures asks again without the ones already shown', async () => {
    let round = 0;
    await openLesson((url) => {
      if (url.endsWith('/search')) { round += 1; return reply({ candidates: round === 1 ? [candidate(1, 'Good match', 0.9)] : [candidate(2, 'Possible match', 0.5)], max: 12, saved: 0 }); }
      return reply({});
    });
    fireEvent.click(screen.getByRole('button', { name: /Download pictures/ }));
    await screen.findByText('Candidate 1');
    fireEvent.click(screen.getByRole('button', { name: 'Show more pictures' }));
    expect(await screen.findByText('Candidate 2')).toBeInTheDocument();
    expect(screen.getByText('Candidate 1')).toBeInTheDocument();
    expect(JSON.parse(calls('POST', '/search')[1][1].body).exclude).toEqual(['https://img.example/1.jpg']);
  });

  it('says so when nothing is found or the search fails', async () => {
    await openLesson(() => reply({ detail: 'Could not reach the picture sources. Check the Internet connection and try again.' }, false, 502));
    fireEvent.click(screen.getByRole('button', { name: /Download pictures/ }));
    expect(await screen.findByRole('alert')).toHaveTextContent('Could not reach the picture sources');
    fireEvent.click(screen.getByRole('button', { name: 'Close' }));
    await openLessonAgain();
  });

  async function openLessonAgain() {
    // nothing found (empty list), not an error
    global.fetch = vi.fn((url) => (String(url).endsWith('/search') ? Promise.resolve(reply({ candidates: [], max: 12, saved: 0 })) : Promise.resolve(reply({}))));
    fireEvent.click(screen.getByRole('button', { name: /Download pictures/ }));
    expect(await screen.findByText(/No pictures were found/)).toBeInTheDocument();
  }

  it('Upload sends every chosen file and shows them all', async () => {
    let n = 0;
    await openLesson((url, init) => {
      if (init.method === 'PUT') { n += 1; return reply({ added: true, ...saved(Array.from({ length: n }, (_, i) => item(i + 1, 'upload'))) }); }
      return reply({});
    });
    const files = [new File([new Uint8Array(3000)], 'my photo.png', { type: 'image/png' }), new File([new Uint8Array(3000)], 'two.jpg', { type: 'image/jpeg' })];
    fireEvent.change(screen.getByTestId('picture-file-input'), { target: { files } });
    expect(await screen.findByText(/2 pictures uploaded and saved in the database/)).toBeInTheDocument();
    const puts = calls('PUT', '/api/lesson-picture');
    expect(puts).toHaveLength(2);
    expect(decodeURIComponent(puts[0][0])).toBe(`/api/lesson-picture?key=${KEY}`);
    expect(puts[0][1].body).toBe(files[0]);
    expect(puts[0][1].headers['X-Filename']).toBe('my%20photo.png');
    expect(await screen.findAllByTestId('saved-picture')).toHaveLength(2);
    expect(screen.getAllByText(/Your uploaded picture: Photo/)).toHaveLength(2);
  });

  it('refuses files that are not pictures without calling the server', async () => {
    await openLesson(() => reply({}));
    fireEvent.change(screen.getByTestId('picture-file-input'), { target: { files: [new File(['x'], 'a.txt', { type: 'text/plain' })] } });
    expect(await screen.findByRole('alert')).toHaveTextContent('JPEG, PNG, WebP or GIF');
    expect(calls('PUT', '/api/lesson-picture')).toHaveLength(0);
  });

  it('a saved picture can be removed after confirming', async () => {
    let removed = false;
    await openLesson((url, init) => {
      if (init.method === 'PUT') return reply({ added: true, ...saved([item(1, 'upload'), item(2, 'upload')]) });
      if (init.method === 'DELETE') { removed = true; return reply({ removed: true, ...saved([item(2, 'upload')]) }); }
      return reply({});
    });
    fireEvent.change(screen.getByTestId('picture-file-input'), { target: { files: [new File([new Uint8Array(3000)], 'a.png', { type: 'image/png' })] } });
    await screen.findAllByTestId('saved-picture');
    const confirm = vi.spyOn(window, 'confirm').mockReturnValueOnce(false).mockReturnValueOnce(true);
    fireEvent.click(screen.getByRole('button', { name: 'Remove picture Photo 1' }));
    expect(removed).toBe(false); // cancelled
    fireEvent.click(screen.getByRole('button', { name: 'Remove picture Photo 1' }));
    await waitFor(() => expect(screen.getAllByTestId('saved-picture')).toHaveLength(1));
    expect(calls('DELETE', '/api/lesson-picture/id1')).toHaveLength(1);
    confirm.mockRestore();
  });

  it('explains how to fix it when the running server is an old version (405)', async () => {
    await openLesson(() => reply({ detail: 'Method Not Allowed' }, false, 405));
    fireEvent.click(screen.getByRole('button', { name: /Download pictures/ }));
    expect(await screen.findByRole('alert')).toHaveTextContent('Close the black EduAi_Pro window');
  });
});
