import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import SearchBar from '../src/components/SearchBar.jsx';

function mockFetch(searchResults) {
  return vi.fn((url) => {
    const u = String(url);
    if (u.startsWith('/api/search/')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(searchResults) });
    }
    if (u.startsWith('/api/ark-ai/prompts')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ prompts: [], tags: [] }) });
    }
    if (u.startsWith('/api/ark-ai/models')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ models: [] }) });
    }
    if (u.startsWith('/api/ark-ai/tools')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ tools: [], categories: [], kinds: [] }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch([
    { title: 'Phonics for Beginners', subject: 'English', resource_type: 'video_resources', url: 'https://example.com' },
  ]);
});

describe('SearchBar', () => {
  it('shows results only from safe backend search', async () => {
    render(<SearchBar standard={1} />);
    fireEvent.change(screen.getByLabelText('Search safe resources for this grade'), {
      target: { value: 'phonics' },
    });
    fireEvent.click(screen.getByRole('button', { name: 'Search' }));

    await waitFor(() => {
      expect(screen.getByText('Phonics for Beginners')).toBeInTheDocument();
    });
    expect(global.fetch).toHaveBeenCalledWith('/api/search/1?q=phonics');
  });

  it('shows a no-results message for empty search response', async () => {
    global.fetch = mockFetch([]);
    render(<SearchBar standard={1} />);
    fireEvent.change(screen.getByLabelText('Search safe resources for this grade'), {
      target: { value: 'xyz' },
    });
    fireEvent.click(screen.getByRole('button', { name: 'Search' }));

    await waitFor(() => {
      expect(screen.getByText('No safe results found.')).toBeInTheDocument();
    });
  });

  it('embeds the full Ark AI panel and library', async () => {
    render(<SearchBar standard={1} />);
    expect(await screen.findByText('Ark AI Library')).toBeInTheDocument();
    expect(screen.getByText(/Or ask Ark AI directly/)).toBeInTheDocument();
  });
});
