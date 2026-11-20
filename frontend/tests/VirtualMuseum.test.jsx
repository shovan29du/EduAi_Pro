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
  links: {
    wikipedia: 'https://en.wikipedia.org/wiki/Ancient_Amphora',
    virtual_tour: 'https://artsandculture.google.com/search?q=Test+Museum',
  },
  quiz: null,
};

const featuredObject = {
  id: 'obj_f',
  name: 'The Featured Piece',
  gallery: 'ancient_world',
  museum: 'Test Museum',
  category: 'archaeology',
  wiki_title: 'The Featured Piece',
  links: { virtual_tour: 'https://artsandculture.google.com/search?q=Test+Museum' },
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/museum') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (u === '/api/museum/featured') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(featuredObject) });
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
    if (u === '/api/museum/ancient_world/obj_f') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(featuredObject) });
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

  it('shows a virtual tour link in the object detail view', async () => {
    render(
      <ChildProvider>
        <VirtualMuseum />
      </ChildProvider>
    );

    fireEvent.click(await screen.findByText('Ancient World'));
    fireEvent.click(await screen.findByText('Ancient Amphora'));

    const tourLinks = await screen.findAllByRole('link', { name: /Virtual Tour/ });
    expect(tourLinks.length).toBeGreaterThan(0);
    tourLinks.forEach((link) => {
      expect(link).toHaveAttribute('href', 'https://artsandculture.google.com/search?q=Test+Museum');
    });
  });

  it('shows a Featured Today card on the homepage and opens it on click', async () => {
    render(
      <ChildProvider>
        <VirtualMuseum />
      </ChildProvider>
    );

    fireEvent.click(await screen.findByText('The Featured Piece'));
    expect(await screen.findByRole('heading', { name: 'The Featured Piece' })).toBeInTheDocument();
  });

  describe('pictures', () => {
    const metObject = { id: 'met_436532', name: 'Wheat Field with Cypresses by Vincent van Gogh', category: 'painting', year: '1889', met_id: 436532, links: {} };
    const openGallery = async (objects, detail) => {
      global.fetch = vi.fn((url) => {
        const u = String(url);
        if (u === '/api/museum') return Promise.resolve({ ok: true, json: () => Promise.resolve({ ...overview, galleries: [{ id: 'ancient_world', label: 'Ancient World', emoji: '🏺', object_count: objects.length }] }) });
        if (u === '/api/museum/featured') return Promise.resolve({ ok: true, json: () => Promise.resolve(featuredObject) });
        if (u === '/api/museum/ancient_world') return Promise.resolve({ ok: true, json: () => Promise.resolve({ ...galleryObjects, objects }) });
        if (u.startsWith('/api/museum/thumbnail')) {
          return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: u.includes('met_id=436532') ? 'https://images.metmuseum.org/CRDImages/ep/web-large/DT1567.jpg' : null }) });
        }
        if (u === '/api/museum/ancient_world/' + objects[0].id) return Promise.resolve({ ok: true, json: () => Promise.resolve(detail || objects[0]) });
        return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
      });
      render(<ChildProvider><VirtualMuseum /></ChildProvider>);
      fireEvent.click(await screen.findByText('Ancient World'));
      await screen.findByText(/Wheat Field with Cypresses/);
    };

    it('finds a Met object picture by its Met ID, never by guessing from its name', async () => {
      await openGallery([metObject]);
      await waitFor(() => expect(global.fetch.mock.calls.some((c) => String(c[0]).includes('/museum/thumbnail?met_id=436532'))).toBe(true));
      const thumbCalls = global.fetch.mock.calls.map((c) => String(c[0])).filter((u) => u.includes('/museum/thumbnail'));
      expect(thumbCalls.some((u) => u.includes('Wheat') || u.includes('Gogh'))).toBe(false); // no lookup by name
      await waitFor(() => expect(document.querySelector('img[src*="images.metmuseum.org"]')).not.toBeNull());
    });

    it('shows a downloaded local picture with its credit and does not look it up again', async () => {
      const local = { ...metObject, thumbnail_local: '/museum-resource/images/met_436532.jpg', image_credit: { line: 'The Metropolitan Museum of Art · CC0 1.0 (Open Access)' } };
      await openGallery([local]);
      fireEvent.click(await screen.findByText(/Wheat Field with Cypresses/));
      expect(await screen.findByText(/Photo: The Metropolitan Museum of Art · CC0 1.0/)).toBeInTheDocument();
      expect(document.querySelector('img[src="/museum-resource/images/met_436532.jpg"]')).not.toBeNull();
      const lookups = global.fetch.mock.calls.map((c) => String(c[0])).filter((u) => u.includes('/museum/thumbnail'));
      expect(lookups.some((u) => u.includes('met_id=436532') || u.includes('Wheat'))).toBe(false);
    });
  });
});
