import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor, within } from '@testing-library/react';
import VirtualMuseum from '../src/components/VirtualMuseum.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

const overview = {
  title: 'Virtual Museum',
  description: 'Explore the world',
  total_objects: 2,
  galleries: [{ id: 'ancient_world', label: 'Ancient World', emoji: '🏺', object_count: 2 }],
};

const galleryObjects = {
  id: 'ancient_world',
  label: 'Ancient World',
  emoji: '🏺',
  objects: [
    { id: 'obj_z', name: 'Zebra Mosaic', category: 'archaeology', year: '1200', wiki_title: 'Zebra Mosaic' },
    { id: 'obj_a', name: 'Ancient Amphora', category: 'archaeology', year: '400 BCE', wiki_title: 'Ancient Amphora' },
  ],
};

const objectDetail = {
  id: 'obj_a',
  name: 'Ancient Amphora',
  category: 'archaeology',
  year: '400 BCE',
  description: 'A clay vessel.',
  significance: 'Everyday life artifact.',
  wiki_title: 'Ancient Amphora',
  links: { wikipedia: 'https://en.wikipedia.org/wiki/Ancient_Amphora' },
  quiz: null,
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/museum') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (u === '/api/museum/ancient_world') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(galleryObjects) });
    }
    if (u.startsWith('/api/museum/thumbnail')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: null }) });
    }
    if (u === '/api/museum/ancient_world/obj_a') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(objectDetail) });
    }
    if (u.startsWith('/api/progress/')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  localStorage.clear();
  sessionStorage.clear();
  global.fetch = mockFetch();
});

describe('VirtualMuseum', () => {
  it('sorts gallery objects alphabetically when the sort control is changed', async () => {
    render(
      <ChildProvider>
        <VirtualMuseum />
      </ChildProvider>
    );

    fireEvent.click(await screen.findByText('Ancient World'));

    await waitFor(() => {
      expect(screen.getByText('Zebra Mosaic')).toBeInTheDocument();
    });

    // Default order matches the API response: Zebra Mosaic, then Ancient Amphora.
    let names = screen.getAllByText(/Mosaic|Amphora/).map((el) => el.textContent);
    expect(names).toEqual(['Zebra Mosaic', 'Ancient Amphora']);

    fireEvent.change(screen.getByLabelText('Sort objects'), { target: { value: 'name-asc' } });

    await waitFor(() => {
      names = screen.getAllByText(/Mosaic|Amphora/).map((el) => el.textContent);
      expect(names).toEqual(['Ancient Amphora', 'Zebra Mosaic']);
    });
  });

  it('lets a child favourite a museum object from the detail view', async () => {
    render(
      <ChildProvider>
        <VirtualMuseum />
      </ChildProvider>
    );

    fireEvent.click(await screen.findByText('Ancient World'));
    fireEvent.click(await screen.findByText('Ancient Amphora'));

    const favButton = await screen.findByRole('button', { name: /Add Ancient Amphora to favourites/ });
    fireEvent.click(favButton);

    await waitFor(() => {
      const stored = JSON.parse(localStorage.getItem('favorites_Shovan'));
      expect(stored).toHaveLength(1);
      expect(stored[0].title).toBe('Ancient Amphora');
      expect(stored[0].link).toBe('https://en.wikipedia.org/wiki/Ancient_Amphora');
    });
  });
});
