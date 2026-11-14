import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import WorldLiteratureLibrary from '../src/components/WorldLiteratureLibrary.jsx';

const overview = {
  description: 'test',
  sections: [{ id: 'local', label: 'My Local Library', emoji: '🏠', age_range: 'All ages', book_count: 1 }],
};

const section = {
  label: 'My Local Library', emoji: '🏠', age_range: 'All ages',
  books: [{
    id: 'my-book', title: 'My Local Book', author: 'Some Author', year: '', origin: '',
    summary: 'A synopsis.', links: { read_online: '/api/local-library/files/abc', local_copy: true },
  }],
};

const bookDetail = {
  id: 'my-book', title: 'My Local Book', author: 'Some Author', summary: 'A synopsis.',
  links: { read_online: '/api/local-library/files/abc', local_copy: true },
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/world-literature') return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    if (u === '/api/world-literature/local') return Promise.resolve({ ok: true, json: () => Promise.resolve(section) });
    if (u === '/api/world-literature/local/my-book') return Promise.resolve({ ok: true, json: () => Promise.resolve(bookDetail) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('WorldLiteratureLibrary local-copy indicator', () => {
  it('shows a Local Copy badge on the book card instead of Free', async () => {
    global.fetch = mockFetch();
    render(<WorldLiteratureLibrary />);
    fireEvent.click(await screen.findByText('My Local Library'));
    expect(await screen.findByText('🏠 Local Copy')).toBeInTheDocument();
    expect(screen.queryByText('📖 Free')).not.toBeInTheDocument();
  });

  it('shows a "Read My Local Copy" link on the book detail page', async () => {
    global.fetch = mockFetch();
    render(<WorldLiteratureLibrary />);
    fireEvent.click(await screen.findByText('My Local Library'));
    // BookCover's generated placeholder also repeats the title text, so
    // click via the summary (unique to the card body) instead.
    fireEvent.click((await screen.findByText(/A synopsis\./)).closest('button'));
    const link = await screen.findByText('🏠 Read My Local Copy');
    expect(link.closest('a')).toHaveAttribute('href', '/api/local-library/files/abc');
  });
});
