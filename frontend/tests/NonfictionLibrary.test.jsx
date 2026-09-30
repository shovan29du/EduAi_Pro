import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import NonfictionLibrary from '../src/components/NonfictionLibrary.jsx';

const overview = {
  description: 'test',
  categories: [{ id: 'local', label: 'My Local Library', emoji: '🏠', book_count: 1 }],
};

const category = {
  label: 'My Local Library', emoji: '🏠',
  books: [{
    id: 'my-book', title: 'My Local Book', author: 'Some Author', year: '',
    summary: 'A long synopsis.', links: { read_online: '/api/local-library/files/abc', local_copy: true },
  }],
};

const bookDetail = {
  id: 'my-book', title: 'My Local Book', author: 'Some Author', summary: 'A long synopsis.',
  links: { read_online: '/api/local-library/files/abc', local_copy: true },
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/nonfiction') return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    if (u === '/api/nonfiction/local') return Promise.resolve({ ok: true, json: () => Promise.resolve(category) });
    if (u === '/api/nonfiction/local/my-book') return Promise.resolve({ ok: true, json: () => Promise.resolve(bookDetail) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('NonfictionLibrary local-copy indicator', () => {
  it('shows a Local Copy badge on the book card instead of Free', async () => {
    global.fetch = mockFetch();
    render(<NonfictionLibrary />);
    fireEvent.click(await screen.findByText('My Local Library'));
    expect(await screen.findByText('🏠 Local Copy')).toBeInTheDocument();
    expect(screen.queryByText('📖 Free')).not.toBeInTheDocument();
  });

  it('shows a "Read My Local Copy" link on the book detail page', async () => {
    global.fetch = mockFetch();
    render(<NonfictionLibrary />);
    fireEvent.click(await screen.findByText('My Local Library'));
    fireEvent.click((await screen.findByText(/A long synopsis\./)).closest('button'));
    const link = await screen.findByText('🏠 Read My Local Copy');
    expect(link.closest('a')).toHaveAttribute('href', '/api/local-library/files/abc');
  });
});
