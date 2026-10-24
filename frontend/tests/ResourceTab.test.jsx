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
    if (u.startsWith('/api/pdf-explainer')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
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

describe('ResourceTab Local Library Ark AI categorisation', () => {
  const scannedFiles = [
    {
      id: 'f1', filename: 'lecture_final_v2.mp4', path: '/home/me/Videos/lecture_final_v2.mp4',
      category: 'videos', size: 1024, open_url: '/api/local-library/files/f1',
      summary: '', matched_topics: [], ai_kind: 'Lecture recording', ai_genre: 'Biology', ai_title: 'Photosynthesis Lecture',
    },
    {
      id: 'f2', filename: 'book1.txt', path: '/home/me/Books/book1.txt',
      category: 'books', size: 2048, open_url: '/api/local-library/files/f2',
      summary: 'A summary about photosynthesis.', matched_topics: [], ai_kind: '', ai_genre: 'Science', ai_title: '',
    },
  ];

  function mockFetchWithScan() {
    return vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/resource-tab' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
      }
      if (u === '/api/course-providers?query=') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
      }
      if (u === '/api/local-library?') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ files: [] }) });
      }
      if (u === '/api/local-library/scan' && options.method === 'POST') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            root: '/home/me/Library', indexed: 2, books_analysed: 1, ai_analysed: 2,
            truncated_ai: false, skipped: 0, truncated: false, warnings: [], files: scannedFiles,
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });
  }

  beforeEach(() => {
    global.fetch = mockFetchWithScan();
  });

  it('shows the Ark AI kind/genre badge and cleaned-up title after a scan', async () => {
    render(<ResourceTab />);
    await screen.findByText('No local files indexed yet.');

    fireEvent.change(screen.getByLabelText('Folder to scan'), { target: { value: '/home/me/Library' } });
    fireEvent.click(screen.getByText('Scan folder'));

    expect(await screen.findByText('Photosynthesis Lecture')).toBeInTheDocument();
    expect(screen.getByText('lecture_final_v2.mp4')).toBeInTheDocument();
    expect(screen.getByText('✨ Lecture recording · Biology')).toBeInTheDocument();
    expect(screen.getByText('✨ Science')).toBeInTheDocument();
    expect(await screen.findByText(/Ark AI categorised 2 new or changed/)).toBeInTheDocument();
  });

  it('reports when Ark AI categorisation was capped for this scan', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/local-library/scan' && options.method === 'POST') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            root: '/home/me/Library', indexed: 5, books_analysed: 0, ai_analysed: 2,
            truncated_ai: true, skipped: 0, truncated: false, warnings: [], files: [],
          }),
        });
      }
      if (u === '/api/resource-tab' || u === '/api/local-library?') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve(u === '/api/local-library?' ? { files: [] } : []) });
      }
      if (u === '/api/course-providers?query=') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ResourceTab />);
    await screen.findByText('No local files indexed yet.');
    fireEvent.change(screen.getByLabelText('Folder to scan'), { target: { value: '/home/me/Library' } });
    fireEvent.click(screen.getByText('Scan folder'));

    expect(await screen.findByText(/stopped early for this scan/)).toBeInTheDocument();
  });

  it('analyzes a scanned book, replaces the World Literature link, and hides the button afterwards', async () => {
    let analyzeCalled = false;
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/resource-tab' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
      }
      if (u === '/api/course-providers?query=') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
      }
      if (u === '/api/local-library?') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ files: scannedFiles }) });
      }
      if (u === '/api/local-library/files/f2/analyze' && options.method === 'POST') {
        analyzeCalled = true;
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            file: { ...scannedFiles[1], author: 'Jane Austen', classification: 'literature', synopsis: 'A short new synopsis.' },
            analysis: { classification: 'literature', title: 'Pride and Prejudice', author: 'Jane Austen', subject: '', synopsis: 'A short new synopsis.' },
            world_literature: { section: 'childrens_classics', book_id: 'pride', title: 'Pride and Prejudice', created: false },
            lesson_matches: [{ file: 'grade8.json', subject: 'English', title: 'Pride and Prejudice' }],
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ResourceTab />);
    const analyzeButton = await screen.findByText('🔎 Analyze for library');
    fireEvent.click(analyzeButton);

    expect(await screen.findByText(/Replaced the link for "Pride and Prejudice" in World Literature/)).toBeInTheDocument();
    expect(screen.getByText(/Also updated 1 lesson resource/)).toBeInTheDocument();
    expect(screen.getByText('A short new synopsis.')).toBeInTheDocument();
    expect(screen.getByText(/📖 Literature · Jane Austen/)).toBeInTheDocument();
    expect(screen.queryByText('🔎 Analyze for library')).not.toBeInTheDocument();
    expect(analyzeCalled).toBe(true);
  });

  it('shows an error if analysis fails', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/resource-tab' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
      }
      if (u === '/api/course-providers?query=') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
      }
      if (u === '/api/local-library?') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ files: scannedFiles }) });
      }
      if (u === '/api/local-library/files/f2/analyze' && options.method === 'POST') {
        return Promise.resolve({ ok: false, status: 422, json: () => Promise.resolve({ detail: 'Could not extract readable text from this file' }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ResourceTab />);
    fireEvent.click(await screen.findByText('🔎 Analyze for library'));

    expect(await screen.findByText('Could not extract readable text from this file')).toBeInTheDocument();
  });

  it('analyzes a scanned book classified as non-fiction and syncs the Non-Fiction Library', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/resource-tab' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
      }
      if (u === '/api/course-providers?query=') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
      }
      if (u === '/api/local-library?') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ files: scannedFiles }) });
      }
      if (u === '/api/local-library/files/f2/analyze' && options.method === 'POST') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            file: { ...scannedFiles[1], author: 'Yuval Noah Harari', classification: 'non-fiction', synopsis: 'A long 800+ word synopsis.' },
            analysis: { classification: 'non-fiction', title: 'Sapiens', author: 'Yuval Noah Harari', subject: '', synopsis: 'A long 800+ word synopsis.' },
            world_literature: null,
            nonfiction: { category: 'science', book_id: 'sapiens', title: 'Sapiens', created: false },
            lesson_matches: [],
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ResourceTab />);
    fireEvent.click(await screen.findByText('🔎 Analyze for library'));

    expect(await screen.findByText(/Replaced the link for "Sapiens" in the Non-Fiction Library/)).toBeInTheDocument();
    expect(screen.getByText(/📗 Non-fiction · Yuval Noah Harari/)).toBeInTheDocument();
    expect(screen.queryByText(/Replaced the link for "Sapiens" in World Literature/)).not.toBeInTheDocument();
  });

  it('analyzes a scanned textbook and shows which lessons its content was linked to', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/resource-tab' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
      }
      if (u === '/api/course-providers?query=') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers: [] }) });
      }
      if (u === '/api/local-library?') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ files: scannedFiles }) });
      }
      if (u === '/api/local-library/files/f2/analyze' && options.method === 'POST') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            file: { ...scannedFiles[1], classification: 'textbook' },
            analysis: { classification: 'textbook', title: 'Algebra Basics', author: '', subject: 'Mathematics', synopsis: '' },
            world_literature: null,
            nonfiction: null,
            lesson_matches: [],
            topic_links: [
              { level: '5', subject: 'Math', lesson: 'Solving Equations' },
              { level: 'C1', subject: 'Mathematics', lesson: 'Linear Algebra Basics' },
            ],
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ResourceTab />);
    fireEvent.click(await screen.findByText('🔎 Analyze for library'));

    expect(await screen.findByText(/Linked to 2 lessons across the syllabus/)).toBeInTheDocument();
    expect(screen.getByText('Level 5 · Math: Solving Equations')).toBeInTheDocument();
    expect(screen.getByText('Level C1 · Mathematics: Linear Algebra Basics')).toBeInTheDocument();
    expect(screen.getByText(/📚 Reference textbook/)).toBeInTheDocument();
  });
});

describe('ResourceTab merged Curator and PDF Explainer sections', () => {
  it('shows the open-libraries content by default', async () => {
    render(<ResourceTab standard={5} level="5" child="Shovan" />);
    expect(await screen.findByText('Open libraries, multimedia and courses')).toBeInTheDocument();
    expect(screen.queryByText('Search web')).not.toBeInTheDocument();
  });

  it('switches to the Curator section and shows its upload form', async () => {
    render(<ResourceTab standard={5} level="5" child="Shovan" />);
    await screen.findByText('Open libraries, multimedia and courses');

    fireEvent.click(screen.getByRole('tab', { name: 'Curator' }));

    expect(await screen.findByText(/Curate New Resources — Standard 5/)).toBeInTheDocument();
    expect(screen.getByText('Upload & summarize')).toBeInTheDocument();
    expect(screen.queryByText('Open libraries, multimedia and courses')).not.toBeInTheDocument();
  });

  it('switches to the PDF Explainer section and shows its upload control', async () => {
    render(<ResourceTab standard={5} level="5" child="Shovan" />);
    await screen.findByText('Open libraries, multimedia and courses');

    fireEvent.click(screen.getByRole('tab', { name: 'PDF Explainer' }));

    await waitFor(() => {
      expect(screen.queryByText('Open libraries, multimedia and courses')).not.toBeInTheDocument();
    });
    expect(document.querySelector('input[type="file"]')).toBeInTheDocument();
  });
});
