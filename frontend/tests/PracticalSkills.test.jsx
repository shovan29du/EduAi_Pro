import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
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


describe('PracticalSkills Download and Upload', () => {
  const stored = (source) => ({ available: true, stored: true, source, title: source === 'upload' ? 'Your uploaded picture' : 'Stranger danger', description: '', page_url: '', credit: { line: source === 'upload' ? 'Picture uploaded by the owner of this app' : 'A. Photographer · CC BY-SA 4.0' }, thumbnail_url: `/api/lesson-picture?key=k&v=${source === 'upload' ? 2 : 1}` });

  async function openLesson(handler) {
    const base = global.fetch;
    global.fetch = vi.fn((url, init) => (init?.method && String(url).startsWith('/api/lesson-picture') ? Promise.resolve(handler(String(url), init)) : base(url, init)));
    render(<PracticalSkills />);
    await waitFor(() => expect(screen.getByText('Cooking')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Cooking'));
    await waitFor(() => expect(screen.getByText('Kitchen Safety Basics')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Kitchen Safety Basics'));
    await screen.findByRole('button', { name: /Download (another )?picture/ });
  }

  it('Download saves a picture in the database and shows it with its credit', async () => {
    await openLesson(() => ({ ok: true, json: () => Promise.resolve(stored('download')) }));
    fireEvent.click(screen.getByRole('button', { name: /Download (another )?picture/ }));
    expect(await screen.findByText(/Picture downloaded and saved in the database/)).toBeInTheDocument();
    const post = global.fetch.mock.calls.find((c) => c[1]?.method === 'POST');
    expect(JSON.parse(post[1].body).key).toMatch(/^practical\/cooking\/Kitchen Safety Basics$/);
    await waitFor(() => expect(document.querySelector('img[src="/api/lesson-picture?key=k&v=1"]')).not.toBeNull());
    expect(screen.getByText(/Photo: A. Photographer/)).toBeInTheDocument();
    expect(screen.getByText(/Saved picture: Stranger danger/)).toBeInTheDocument();
  });

  it('Upload sends the file and shows the uploaded picture', async () => {
    await openLesson(() => ({ ok: true, json: () => Promise.resolve(stored('upload')) }));
    const file = new File([new Uint8Array(3000)], 'my photo.png', { type: 'image/png' });
    fireEvent.change(screen.getByTestId('picture-file-input'), { target: { files: [file] } });
    expect(await screen.findByText(/Picture uploaded and saved in the database/)).toBeInTheDocument();
    const put = global.fetch.mock.calls.find((c) => c[1]?.method === 'PUT');
    expect(decodeURIComponent(put[0])).toBe('/api/lesson-picture?key=practical/cooking/Kitchen Safety Basics');
    expect(put[1].body).toBe(file);
    expect(put[1].headers['X-Filename']).toBe('my%20photo.png');
    await waitFor(() => expect(document.querySelector('img[src="/api/lesson-picture?key=k&v=2"]')).not.toBeNull());
    expect(screen.getByText(/Your uploaded picture · saved in the database/)).toBeInTheDocument();
  });

  it('shows the server\'s reason when Download or Upload fails, and refuses non-pictures locally', async () => {
    await openLesson(() => ({ ok: false, status: 404, json: () => Promise.resolve({ detail: 'No picture was found for this lesson. You can upload one instead.' }) }));
    fireEvent.click(screen.getByRole('button', { name: /Download (another )?picture/ }));
    expect(await screen.findByRole('alert')).toHaveTextContent('You can upload one instead');
    fireEvent.change(screen.getByTestId('picture-file-input'), { target: { files: [new File(['x'], 'a.txt', { type: 'text/plain' })] } });
    await waitFor(() => expect(screen.getByRole('alert')).toHaveTextContent('JPEG, PNG, WebP or GIF'));
    expect(global.fetch.mock.calls.some((c) => c[1]?.method === 'PUT')).toBe(false);
  });
});
