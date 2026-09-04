import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import StudyCoach from '../src/components/StudyCoach.jsx';

const emptyStats = { total_questions: 0, due_today: 0, mastered: 0, topics: [] };

const generatedResponse = {
  questions: [
    {
      id: 'q1', child: 'TestChild', topic: 'basic math', type: 'mcq',
      question: 'What is 2+2?', options: { A: '3', B: '4', C: '5', D: '6' }, answer: 'B',
      explanation: '2+2=4', due_date: '2026-08-01',
    },
  ],
};

const statsAfterGenerate = { total_questions: 1, due_today: 1, mastered: 0, topics: ['basic math'] };

const dueResponse = {
  questions: [
    {
      id: 'q1', child: 'TestChild', topic: 'basic math', type: 'mcq',
      question: 'What is 2+2?', options: { A: '3', B: '4', C: '5', D: '6' }, answer: 'B',
      explanation: '2+2=4',
    },
  ],
};

const answerResponse = {
  correct: true, score: 100, feedback: '2+2=4', correct_answer: 'B', explanation: '2+2=4',
  next_due_date: '2026-08-02', interval_days: 1,
};

function mockFetch({ stats = emptyStats } = {}) {
  let currentStats = stats;
  return vi.fn((url, options = {}) => {
    const u = String(url);
    if (u.startsWith('/api/study-coach/stats')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(currentStats) });
    }
    if (u === '/api/study-coach/generate' && options.method === 'POST') {
      currentStats = statsAfterGenerate;
      return Promise.resolve({ ok: true, json: () => Promise.resolve(generatedResponse) });
    }
    if (u.startsWith('/api/study-coach/due')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(dueResponse) });
    }
    if (u === '/api/study-coach/q1/answer' && options.method === 'POST') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(answerResponse) });
    }
    if (u.startsWith('/api/levels')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ levels: [] }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('StudyCoach', () => {
  it('shows zeroed stats and no session button when there is nothing due', async () => {
    render(<StudyCoach child="TestChild" />);
    expect(await screen.findByText('Total questions')).toBeInTheDocument();
    expect(screen.queryByText(/Start review session/)).not.toBeInTheDocument();
  });

  it('generates study questions for a topic', async () => {
    render(<StudyCoach child="TestChild" />);
    await screen.findByText('Total questions');

    fireEvent.change(screen.getByPlaceholderText('Topic, e.g. the water cycle'), {
      target: { value: 'basic math' },
    });
    fireEvent.click(screen.getByText('Add questions to my deck'));

    expect(await screen.findByText('Start review session (1 due)')).toBeInTheDocument();
    expect(screen.getByText('basic math')).toBeInTheDocument();
  });

  it('runs a review session and shows AI feedback after answering', async () => {
    render(<StudyCoach child="TestChild" />);
    await screen.findByText('Total questions');
    fireEvent.change(screen.getByPlaceholderText('Topic, e.g. the water cycle'), {
      target: { value: 'basic math' },
    });
    fireEvent.click(screen.getByText('Add questions to my deck'));
    fireEvent.click(await screen.findByText('Start review session (1 due)'));

    expect(await screen.findByText('What is 2+2?')).toBeInTheDocument();

    fireEvent.click(screen.getByText('B) 4'));
    fireEvent.click(screen.getByText('Submit answer'));

    expect(await screen.findByText(/✅ Correct/)).toBeInTheDocument();
    expect(screen.getByText('Finish session')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Finish session'));

    await waitFor(() => {
      expect(screen.getByText('Total questions')).toBeInTheDocument();
    });
  });
});
