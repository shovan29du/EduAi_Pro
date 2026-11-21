import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import SurvivalSkills from '../src/components/SurvivalSkills.jsx';
import { clearSkillPictureCache } from '../src/components/SkillPicture.jsx';

const overview = {
  description: 'Essential life and safety skills.',
  categories: [{ id: 'outdoor_and_navigation', label: 'Outdoor & Navigation', emoji: '🧭', skill_count: 1 }],
};

const categoryData = {
  skills: [
    {
      name: 'Using a Compass',
      grade_range: '5-8',
      adult_supervision_required: false,
      wiki_title: 'Using a Compass',
      key_steps: ['Hold the compass flat', 'Align the needle with north'],
      practice_activities: ['Find north in your backyard'],
      data_table: { headers: ['Direction', 'Bearing'], rows: [['North', '0° / 360°'], ['East', '90°']] },
      formulae: ['A full circle is 360 degrees'],
      quiz: [{ q: 'What bearing is North?', a: '0 degrees' }],
    },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    if (url === '/api/survival-skills') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (url === '/api/survival-skills/outdoor_and_navigation') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(categoryData) });
    }
    if (String(url).startsWith('/api/lesson-enrichment/wiki')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ available: true, title: 'Picture of compass', description: 'A test article', page_url: 'https://en.wikipedia.org/wiki/Test', thumbnail_url: 'https://example.com/compass.jpg' }) });
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

describe('SurvivalSkills', () => {
  it('browses into a category and shows a skill card with a real photo thumbnail', async () => {
    const { container } = render(<SurvivalSkills />);
    await waitFor(() => expect(screen.getByText('Outdoor & Navigation')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Outdoor & Navigation'));

    await waitFor(() => expect(screen.getByText('Using a Compass')).toBeInTheDocument());
    await waitFor(() => expect(container.querySelector('img[src="https://example.com/compass.jpg"]')).toBeInTheDocument());
  });

  it('opens a skill and shows Quick Facts, a reference table, and key facts', async () => {
    render(<SurvivalSkills />);
    await waitFor(() => expect(screen.getByText('Outdoor & Navigation')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Outdoor & Navigation'));
    await waitFor(() => expect(screen.getByText('Using a Compass')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Using a Compass'));

    await waitFor(() => expect(screen.getByRole('heading', { name: 'Using a Compass' })).toBeInTheDocument());

    // Quick Facts infographic (derived from existing fields)
    expect(screen.getByText('Supervision')).toBeInTheDocument();
    expect(screen.getByText('Not required')).toBeInTheDocument();

    // Reference table
    expect(screen.getByRole('columnheader', { name: 'Bearing' })).toBeInTheDocument();
    expect(screen.getByRole('cell', { name: '0° / 360°' })).toBeInTheDocument();

    // Key facts (formulae)
    expect(screen.getByText('A full circle is 360 degrees')).toBeInTheDocument();
  });
});


describe('SurvivalSkills lesson picture', () => {
  it('shows a captioned, credited picture on the lesson page and searches with the subject', async () => {
    render(<SurvivalSkills />);
    await waitFor(() => expect(screen.getByText('Outdoor & Navigation')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Outdoor & Navigation'));
    await waitFor(() => expect(screen.getByText('Using a Compass')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Using a Compass'));

    const figure = await screen.findByTestId('skill-picture');
    expect(figure.querySelector('img').getAttribute('src')).toMatch(/^https:\/\/example\.com\/.+\.jpg$/);
    expect(figure).toHaveTextContent('Picture: Picture of');
    expect(screen.getAllByRole('link', { name: 'Wikipedia' })[0]).toHaveAttribute('href', 'https://en.wikipedia.org/wiki/Test');
    const lookup = global.fetch.mock.calls.map((c) => String(c[0])).find((u) => u.startsWith('/api/lesson-enrichment/wiki'));
    const params = new URLSearchParams(lookup.split('?')[1]);
    expect(params.get('q')).toBe('Using a Compass');
    expect(params.get('ctx')).toBe('Outdoor & Navigation');
  });

  it('shows a placeholder with Download and Upload when nothing matches', async () => {
    const base = global.fetch;
    global.fetch = vi.fn((url, ...rest) => String(url).startsWith('/api/lesson-enrichment/wiki')
      ? Promise.resolve({ ok: true, json: () => Promise.resolve({ available: false }) })
      : base(url, ...rest));
    render(<SurvivalSkills />);
    await waitFor(() => expect(screen.getByText('Outdoor & Navigation')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Outdoor & Navigation'));
    await waitFor(() => expect(screen.getByText('Using a Compass')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Using a Compass'));
    await screen.findByRole('heading', { name: 'Using a Compass' });
    expect(screen.getByText(/No picture found for this lesson yet/)).toBeInTheDocument(); // placeholder, so Download/Upload are still there
    expect(screen.getByRole('button', { name: /Download picture/ })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Upload picture/ })).toBeInTheDocument();
  });
});


describe('SurvivalSkills Download and Upload', () => {
  const stored = (source) => ({ available: true, stored: true, source, title: source === 'upload' ? 'Your uploaded picture' : 'Stranger danger', description: '', page_url: '', credit: { line: source === 'upload' ? 'Picture uploaded by the owner of this app' : 'A. Photographer · CC BY-SA 4.0' }, thumbnail_url: `/api/lesson-picture?key=k&v=${source === 'upload' ? 2 : 1}` });

  async function openLesson(handler) {
    const base = global.fetch;
    global.fetch = vi.fn((url, init) => (init?.method && String(url).startsWith('/api/lesson-picture') ? Promise.resolve(handler(String(url), init)) : base(url, init)));
    render(<SurvivalSkills />);
    await waitFor(() => expect(screen.getByText('Outdoor & Navigation')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Outdoor & Navigation'));
    await waitFor(() => expect(screen.getByText('Using a Compass')).toBeInTheDocument());
    fireEvent.click(screen.getByText('Using a Compass'));
    await screen.findByRole('button', { name: /Download (another )?picture/ });
  }

  it('Download saves a picture in the database and shows it with its credit', async () => {
    await openLesson(() => ({ ok: true, json: () => Promise.resolve(stored('download')) }));
    fireEvent.click(screen.getByRole('button', { name: /Download (another )?picture/ }));
    expect(await screen.findByText(/Picture downloaded and saved in the database/)).toBeInTheDocument();
    const post = global.fetch.mock.calls.find((c) => c[1]?.method === 'POST');
    expect(JSON.parse(post[1].body).key).toBe('survival/outdoor_and_navigation/Using a Compass');
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
    expect(decodeURIComponent(put[0])).toBe('/api/lesson-picture?key=survival/outdoor_and_navigation/Using a Compass');
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
