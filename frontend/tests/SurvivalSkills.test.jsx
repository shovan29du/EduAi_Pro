import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import SurvivalSkills from '../src/components/SurvivalSkills.jsx';

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
    if (String(url).startsWith('/api/museum/thumbnail')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: 'https://example.com/compass.jpg' }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
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
