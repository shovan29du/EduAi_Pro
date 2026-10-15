import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import ProfessionalWorkspace from '../src/components/ProfessionalWorkspace.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

const user = { id: 'user1', display_name: 'Shovan' };

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/pro/users/ensure') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(user) });
    }
    if (u === `/api/pro/dashboard/${user.id}`) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    }
    if (u === `/api/pro/research/projects/${user.id}`) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (u === '/api/pro/assessments') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (u === `/api/pro/portfolio/${user.id}`) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (u === `/api/pro/cpd/${user.id}`) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (u === '/api/pro/career/pathways') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ pathways: [] }) });
    }
    if (u === '/api/pro/organizations') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (u === '/api/pro/courses') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve([]) });
    }
    if (u === '/api/pro/lms/lti/config') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    }
    if (u === '/api/art-of-the-day') {
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ title: 'Famous Painting: Test Piece', fact: 'A test fact.' }),
      });
    }
    if (u.startsWith('https://api.wikimedia.org/')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ selected: [] }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('ProfessionalWorkspace Dashboard', () => {
  it('has no left side-nav panel -- sections are a single top row', async () => {
    render(<ProfessionalWorkspace />);
    const nav = await screen.findByRole('navigation', { name: 'Professional workspace' });
    expect(nav.className).not.toMatch(/border-r/);
  });

  it('shows the Study Coach favourite and navigates when clicked', async () => {
    const onNavigate = vi.fn();
    render(<ProfessionalWorkspace onNavigate={onNavigate} />);
    await screen.findByText('Welcome, Shovan');

    expect(screen.getByText('Study Coach')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Study Coach').closest('button'));
    expect(onNavigate).toHaveBeenCalledWith('Study Coach');
  });

  it('does not show favourites when no onNavigate handler is passed', async () => {
    render(<ProfessionalWorkspace />);
    await screen.findByText('Welcome, Shovan');
    expect(screen.queryByText('Study Coach')).not.toBeInTheDocument();
  });

  it('shows the Study Timer, History of the Day, and Art of the Day widgets', async () => {
    render(<ProfessionalWorkspace />);
    await screen.findByText('Welcome, Shovan');
    expect(screen.getByLabelText('Study timer')).toBeInTheDocument();
    expect(screen.getByLabelText('History of the day')).toBeInTheDocument();
    expect(await screen.findByText('Test Piece')).toBeInTheDocument();
  });

  it('shows Fact of the Day once fullGrade data is available', async () => {
    const fullGrade = {
      subjects: {
        Science: { info_cards: [{ title: 'Water', fact: 'Water boils at 100C.', safe: true }] },
      },
    };
    render(
      <ChildProvider>
        <ProfessionalWorkspace fullGrade={fullGrade} />
      </ChildProvider>
    );
    await screen.findByText('Welcome, Shovan');
    expect(screen.getByLabelText('Fact of the day')).toBeInTheDocument();
  });
});
