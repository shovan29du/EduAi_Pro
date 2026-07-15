import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import SubjectLessons from '../src/components/SubjectLessons.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

vi.mock('../src/components/MediaSection.jsx', () => ({
  default: ({ title }) => <div>{title}</div>,
}));

const subject = {
  books: [{ id: 'b1', title: 'A Book', link: 'https://example.com', safe: true }],
  video_resources: [{ title: 'A Video', url: 'https://www.youtube.com/watch?v=abc123', safe: true }],
  info_cards: [{ title: 'A Card', fact: 'A fact', safe: true }],
};

beforeEach(() => {
  localStorage.clear();
  global.fetch = vi.fn((url) => {
    if (url === '/api/progress/Parent') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ completed_lessons: {} }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('SubjectLessons', () => {
  it('shows every lesson open from the start, with no lock on later lessons', async () => {
    render(
      <ChildProvider>
        <SubjectLessons subjectName="Math" subject={subject} />
      </ChildProvider>
    );

    await waitFor(() => {
      expect(screen.getByText('Lesson 1: Learn')).toBeInTheDocument();
    });
    // All lessons are visible and unlocked immediately -- no "Complete X first" gating.
    expect(screen.queryByText(/first to unlock/)).not.toBeInTheDocument();
    expect(screen.getByText('Lesson 2: Watch')).toBeInTheDocument();

    fireEvent.click(screen.getAllByRole('button', { name: 'Mark lesson complete' })[0]);

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        '/api/progress/Parent',
        expect.objectContaining({ method: 'POST' })
      );
    });
    // Lesson 2 remains visible and was never gated behind lesson 1's completion.
    expect(screen.getByText('Lesson 2: Watch')).toBeInTheDocument();
  });
});
