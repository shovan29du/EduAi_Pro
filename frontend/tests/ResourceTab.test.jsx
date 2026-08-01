import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ResourceTab from '../src/components/ResourceTab.jsx';

const doc1 = { id: 'doc1', filename: 'notes1.txt', summary: 'Cell biology notes.' };
const doc2 = { id: 'doc2', filename: 'notes2.txt', summary: 'Photosynthesis notes.' };

function mockFetch({ documents = [] } = {}) {
  return vi.fn((url, options = {}) => {
    const u = String(url);
    if (u === '/api/resource-tab' && (!options.method || options.method === 'GET')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(documents) });
    }
    if (u === '/api/resource-tab/course-assistant/ask' && options.method === 'POST') {
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({
          answer: "Mitochondria produce energy. (from notes1.txt)",
          documents: ['notes1.txt', 'notes2.txt'],
        }),
      });
    }
    if (u.match(/\/api\/resource-tab\/doc1$/) && options.method === 'DELETE') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ ok: true }) });
    }
    if (u === '/api/course-providers?query=') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
    }
    if (u === '/api/local-library?') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ files: [] }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch({ documents: [doc1, doc2] });
});

describe('ResourceTab Course Assistant', () => {
  it('does not show the Course Assistant panel when there are no documents', async () => {
    global.fetch = mockFetch({ documents: [] });
    render(<ResourceTab />);
    await screen.findByText('No uploaded copies yet.');
    expect(screen.queryByText('Course Assistant')).not.toBeInTheDocument();
  });

  it('selects documents via checkboxes and asks a grounded question', async () => {
    render(<ResourceTab />);
    await screen.findByText('notes1.txt');

    expect(screen.getByText('No documents selected.')).toBeInTheDocument();

    fireEvent.click(screen.getByLabelText('Include notes1.txt in Course Assistant'));
    fireEvent.click(screen.getByLabelText('Include notes2.txt in Course Assistant'));

    expect(await screen.findByText('2 documents selected.')).toBeInTheDocument();

    fireEvent.change(screen.getByPlaceholderText('Ask a question about the selected documents…'), {
      target: { value: 'What is the powerhouse of the cell?' },
    });
    fireEvent.click(screen.getByText('Ask'));

    expect(await screen.findByText('Mitochondria produce energy. (from notes1.txt)')).toBeInTheDocument();
    expect(screen.getByText('Sources: notes1.txt, notes2.txt')).toBeInTheDocument();
  });

  it('shows an error message when the course assistant request fails', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/resource-tab' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve([doc1, doc2]) });
      }
      if (u === '/api/resource-tab/course-assistant/ask' && options.method === 'POST') {
        return Promise.resolve({ ok: false, status: 400, json: () => Promise.resolve({ detail: 'question is required' }) });
      }
      if (u === '/api/course-providers?query=') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
      }
      if (u === '/api/local-library?') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ files: [] }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ResourceTab />);
    await screen.findByText('notes1.txt');

    fireEvent.click(screen.getByLabelText('Include notes1.txt in Course Assistant'));
    fireEvent.change(screen.getByPlaceholderText('Ask a question about the selected documents…'), {
      target: { value: 'x' },
    });
    fireEvent.click(screen.getByText('Ask'));

    expect(await screen.findByText('question is required')).toBeInTheDocument();
  });

  it('removes a deleted document from the current selection', async () => {
    render(<ResourceTab />);
    await screen.findByText('notes1.txt');

    fireEvent.click(screen.getByLabelText('Include notes1.txt in Course Assistant'));
    expect(await screen.findByText('1 document selected.')).toBeInTheDocument();

    const removeButtons = screen.getAllByText('Remove');
    fireEvent.click(removeButtons[0]);

    await waitFor(() => {
      expect(screen.queryByText('notes1.txt')).not.toBeInTheDocument();
    });
    expect(screen.getByText('No documents selected.')).toBeInTheDocument();
  });
});
