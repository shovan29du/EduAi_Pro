import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import LessonPlanner from '../src/components/LessonPlanner.jsx';

const generatedPlan = {
  id: 'plan123',
  owner_id: 'owner1',
  subject: 'Algebra',
  term_name: 'Term 1',
  level: 'C1',
  start_date: '2026-08-03',
  lessons_per_week: 2,
  lessons: [
    { id: 'lesson1', title: 'Introduction', objectives: ['Define key terms'], content: 'Overview.', date: '2026-08-03' },
    { id: 'lesson2', title: 'Core concepts', objectives: ['Explain the core idea'], content: 'Deep dive.', date: '2026-08-04' },
  ],
};

function mockFetch({ plans = [] } = {}) {
  return vi.fn((url, options = {}) => {
    const u = String(url);
    if (u === '/api/lesson-planner/generate' && options.method === 'POST') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(generatedPlan) });
    }
    if (u.startsWith('/api/lesson-planner?owner_id=')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(plans) });
    }
    if (u.match(/\/api\/lesson-planner\/plan123$/) && options.method === 'DELETE') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ status: 'deleted' }) });
    }
    if (u.match(/\/api\/lesson-planner\/plan123\/lessons\/lesson1$/) && options.method === 'PATCH') {
      const updated = {
        ...generatedPlan,
        lessons: generatedPlan.lessons.map((l) => (l.id === 'lesson1' ? { ...l, date: '2026-09-01' } : l)),
      };
      return Promise.resolve({ ok: true, json: () => Promise.resolve(updated) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('LessonPlanner', () => {
  it('shows empty state when there are no plans', async () => {
    render(<LessonPlanner ownerId="owner1" />);
    expect(await screen.findByText('No lesson plans yet.')).toBeInTheDocument();
  });

  it('generates a plan and shows it in the list', async () => {
    render(<LessonPlanner ownerId="owner1" />);
    await screen.findByText('No lesson plans yet.');

    fireEvent.change(screen.getByPlaceholderText('Subject, e.g. Algebra'), { target: { value: 'Algebra' } });
    fireEvent.change(screen.getByPlaceholderText('Term name, e.g. Term 1'), { target: { value: 'Term 1' } });
    fireEvent.click(screen.getByText('Generate lesson plan'));

    expect(await screen.findByText('Algebra — Term 1')).toBeInTheDocument();
  });

  it('expands a plan to show its scheduled lessons', async () => {
    render(<LessonPlanner ownerId="owner1" />);
    await screen.findByText('No lesson plans yet.');
    fireEvent.change(screen.getByPlaceholderText('Subject, e.g. Algebra'), { target: { value: 'Algebra' } });
    fireEvent.change(screen.getByPlaceholderText('Term name, e.g. Term 1'), { target: { value: 'Term 1' } });
    fireEvent.click(screen.getByText('Generate lesson plan'));

    expect(await screen.findByText('Introduction')).toBeInTheDocument();
    expect(screen.getByText('Core concepts')).toBeInTheDocument();
    expect(screen.getByText('Define key terms')).toBeInTheDocument();
  });

  it('reschedules a lesson to a new date', async () => {
    render(<LessonPlanner ownerId="owner1" />);
    await screen.findByText('No lesson plans yet.');
    fireEvent.change(screen.getByPlaceholderText('Subject, e.g. Algebra'), { target: { value: 'Algebra' } });
    fireEvent.change(screen.getByPlaceholderText('Term name, e.g. Term 1'), { target: { value: 'Term 1' } });
    fireEvent.click(screen.getByText('Generate lesson plan'));
    await screen.findByText('Introduction');

    const dateInput = screen.getByLabelText('Date for Introduction');
    fireEvent.change(dateInput, { target: { value: '2026-09-01' } });

    await waitFor(() => {
      expect(screen.getByLabelText('Date for Introduction')).toHaveValue('2026-09-01');
    });
  });

  it('deletes a plan', async () => {
    render(<LessonPlanner ownerId="owner1" />);
    await screen.findByText('No lesson plans yet.');
    fireEvent.change(screen.getByPlaceholderText('Subject, e.g. Algebra'), { target: { value: 'Algebra' } });
    fireEvent.change(screen.getByPlaceholderText('Term name, e.g. Term 1'), { target: { value: 'Term 1' } });
    fireEvent.click(screen.getByText('Generate lesson plan'));
    await screen.findByText('Algebra — Term 1');

    fireEvent.click(screen.getByText('Delete plan'));

    await waitFor(() => {
      expect(screen.queryByText('Algebra — Term 1')).not.toBeInTheDocument();
    });
    expect(screen.getByText('No lesson plans yet.')).toBeInTheDocument();
  });
});
