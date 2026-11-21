import React from 'react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ExampleQuiz, { conceptsUsed } from '../src/components/ExampleQuiz.jsx';
import ExampleReviewPanel from '../src/components/ExampleReviewPanel.jsx';
import { RealWorldExample } from '../src/components/SubjectLessons.jsx';

afterEach(() => vi.unstubAllGlobals());
const ok = (body) => Promise.resolve({ ok: true, json: () => Promise.resolve(body) });
const EXAMPLE = 'A baker doubles a recipe that needs three quarters of a cup of sugar, which is multiplying a fraction by two.';
const QUESTIONS = [
  { question: 'What does the baker double?', options: { A: 'Sugar', B: 'Salt', C: 'Flour' }, answer: 'A', explanation: 'The recipe amount.' },
  { question: 'What maths is used?', options: { A: 'Addition', B: 'Multiplying fractions', C: 'Division' }, answer: 'B', explanation: '' },
];

describe('conceptsUsed', () => {
  it('matches concepts by word, ignoring case, plurals and punctuation', () => {
    const r = conceptsUsed('You multiply the Fractions together!', ['fraction', 'common denominator', 'product']);
    expect(r.matched).toEqual(['fraction']);
    expect(r.missed).toEqual(['common denominator', 'product']);
  });
});

describe('ExampleQuiz', () => {
  it('runs an AI-generated quiz and scores it', async () => {
    const fetchMock = vi.fn(() => ok({ questions: QUESTIONS }));
    vi.stubGlobal('fetch', fetchMock);
    render(<ExampleQuiz example={EXAMPLE} title="Multiplying Fractions" subject="Math" level="5" concepts={['fraction']} />);
    fireEvent.click(screen.getByRole('button', { name: /test yourself/i }));
    expect(await screen.findByText(/What does the baker double/)).toBeTruthy();
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toMatchObject({ example: EXAMPLE, level: '5' });
    const check = screen.getByRole('button', { name: /check answers/i });
    expect(check.disabled).toBe(true);
    fireEvent.click(screen.getByLabelText('Sugar'));
    fireEvent.click(screen.getByLabelText('Addition'));
    fireEvent.click(check);
    expect(screen.getByRole('status').textContent).toMatch(/1 \/ 2 correct/);
    fireEvent.click(screen.getByRole('button', { name: /try again/i }));
    expect(screen.getByRole('button', { name: /check answers/i })).toBeTruthy();
  });

  it('falls back to a key-concept self-check when no quiz can be made', async () => {
    vi.stubGlobal('fetch', vi.fn(() => ok({ questions: [], unavailable: true })));
    render(<ExampleQuiz example={EXAMPLE} title="Multiplying Fractions" concepts={['fraction', 'product']} />);
    fireEvent.click(screen.getByRole('button', { name: /test yourself/i }));
    const box = await screen.findByRole('textbox');
    fireEvent.change(box, { target: { value: 'She multiplies the fraction by two' } });
    fireEvent.click(screen.getByRole('button', { name: /check my answer/i }));
    expect(screen.getByRole('status').textContent).toMatch(/You used: fraction/);
    expect(screen.getByRole('status').textContent).toMatch(/mention: product/);
  });

  it('also falls back when the request fails', async () => {
    vi.stubGlobal('fetch', vi.fn(() => Promise.reject(new Error('offline'))));
    render(<ExampleQuiz example={EXAMPLE} title="Fractions" concepts={[]} />);
    fireEvent.click(screen.getByRole('button', { name: /test yourself/i }));
    expect(await screen.findByRole('textbox')).toBeTruthy();
  });
});

describe('RealWorldExample badges and quiz entry', () => {
  it('shows a Reviewed badge for vetted text and offers the quiz', async () => {
    vi.stubGlobal('fetch', vi.fn(() => ok({ example: EXAMPLE, vetted: true })));
    render(<RealWorldExample lesson={{ id: 'l1', title: 'Fractions' }} subjectName="Math" levelId="5" />);
    fireEvent.click(screen.getByRole('button', { name: /show a real-world example/i }));
    expect(await screen.findByText('Reviewed')).toBeTruthy();
    expect(screen.getByRole('button', { name: /test yourself/i })).toBeTruthy();
  });

  it('does not badge unreviewed AI text', async () => {
    vi.stubGlobal('fetch', vi.fn(() => ok({ example: EXAMPLE, vetted: false })));
    render(<RealWorldExample lesson={{ id: 'l1', title: 'Fractions' }} subjectName="Math" levelId="5" />);
    fireEvent.click(screen.getByRole('button', { name: /show a real-world example/i }));
    await screen.findByText(EXAMPLE);
    expect(screen.queryByText('Reviewed')).toBeNull();
  });
});

describe('ExampleReviewPanel', () => {
  it('approves an edited draft and reloads the queue', async () => {
    const item = { lesson_id: 'math-g5-l9', title: 'Multiplying Fractions', subject: 'Math', example: EXAMPLE, flags: ['contains a year - check it'] };
    let reviewed = false;
    const fetchMock = vi.fn((url, options = {}) => {
      if (String(url).startsWith('/api/lesson-example/review')) { reviewed = true; return ok({ status: 'approved' }); }
      return ok(reviewed ? { pending_count: 0, vetted_count: 1, items: [] } : { pending_count: 1, vetted_count: 0, items: [item] });
    });
    vi.stubGlobal('fetch', fetchMock);
    render(<ExampleReviewPanel />);
    const box = await screen.findByLabelText('Example for Multiplying Fractions');
    expect(screen.getByText(/contains a year/)).toBeTruthy();
    fireEvent.change(box, { target: { value: EXAMPLE + ' Edited.' } });
    fireEvent.click(screen.getByRole('button', { name: 'Approve' }));
    await waitFor(() => expect(screen.getByText(/nothing is waiting for review/i)).toBeTruthy());
    const call = fetchMock.mock.calls.find(([u]) => String(u).startsWith('/api/lesson-example/review'));
    expect(JSON.parse(call[1].body)).toEqual({ level: '5', lesson_id: 'math-g5-l9', action: 'approve', example: EXAMPLE + ' Edited.' });
  });
});
