import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import AssessmentCentre from '../src/components/AssessmentCentre.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

const ageGroups = { age_groups: [{ id: '7-9', label: 'Ages 7-9', description: 'desc', icon: '📋' }] };
const history = {
  attempts: [
    {
      age_group: '7-9', score: 2, total: 4, percentage: 50, badge: null,
      areas_to_develop: ['shape knowledge'], weak_skills: ['shape_knowledge'],
      timestamp: '2026-01-01T00:00:00Z',
    },
  ],
};

function mockFetch() {
  global.fetch = vi.fn((url) => {
    if (url.includes('/age-groups')) return Promise.resolve({ ok: true, json: () => Promise.resolve(ageGroups) });
    if (url.includes('/history')) return Promise.resolve({ ok: true, json: () => Promise.resolve(history) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  mockFetch();
});

describe('AssessmentCentre', () => {
  it('shows a learning-profile history with a retake action for weak spots', async () => {
    render(
      <ChildProvider>
        <AssessmentCentre />
      </ChildProvider>
    );
    await waitFor(() => screen.getByText('Ages 7-9'));

    fireEvent.click(screen.getByText(/Show learning-profile history/i));
    await waitFor(() => {
      expect(screen.getByText(/shape knowledge/i)).toBeInTheDocument();
    });
    expect(screen.getByText(/Retake these/i)).toBeInTheDocument();
  });

  it('loads a filtered retake assessment when "Retake these" is clicked', async () => {
    render(
      <ChildProvider>
        <AssessmentCentre />
      </ChildProvider>
    );
    await waitFor(() => screen.getByText('Ages 7-9'));
    fireEvent.click(screen.getByText(/Show learning-profile history/i));
    await waitFor(() => screen.getByText(/Retake these/i));

    global.fetch = vi.fn((url) => {
      if (url.includes('/retake')) {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({ label: 'Ages 7-9', is_retake: true, sections: [] }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    fireEvent.click(screen.getByText(/Retake these/i));
    await waitFor(() => {
      expect(screen.getByText(/Focus retake/i)).toBeInTheDocument();
    });
  });
});
