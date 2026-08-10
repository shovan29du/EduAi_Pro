import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import ProfessionalWorkspace from '../src/components/ProfessionalWorkspace.jsx';

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
});
