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

  it('shows no picture box (and no error) when nothing matches', async () => {
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
    expect(screen.queryByTestId('skill-picture')).not.toBeInTheDocument();
  });
});
