import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ProfessionalWorkspace from '../src/components/ProfessionalWorkspace.jsx';

const user = { id: 'user1', display_name: 'Shovan' };

function mockFetch() {
  return vi.fn((url, options = {}) => {
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
    if (u === '/api/pro/resume/draft' && options.method === 'POST') {
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({
          summary: 'Results-driven analyst who ships dashboards.',
          skills: ['Python', 'SQL'],
          experience: ['Built a sales dashboard that cut reporting time by 40%'],
        }),
      });
    }
    if (u === '/api/pro/resume/export' && options.method === 'POST') {
      return Promise.resolve({
        ok: true,
        headers: { get: () => 'attachment; filename="shovan.pdf"' },
        blob: () => Promise.resolve(new Blob(['pdf-bytes'])),
      });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
  global.URL.createObjectURL = vi.fn(() => 'blob:mock');
  global.URL.revokeObjectURL = vi.fn();
});

async function goToCareerSection() {
  render(<ProfessionalWorkspace />);
  await screen.findByRole('button', { name: 'Career' });
  fireEvent.click(screen.getByRole('button', { name: 'Career' }));
  await screen.findByText('Resume Builder');
}

function resumeSkillsField() {
  return screen.getAllByPlaceholderText('Skills, comma separated').find((el) => el.tagName === 'TEXTAREA');
}

describe('ProfessionalWorkspace Resume Builder', () => {
  it('drafts a resume from skills and experience notes', async () => {
    await goToCareerSection();

    fireEvent.change(resumeSkillsField(), {
      target: { value: 'Python, SQL' },
    });
    fireEvent.change(screen.getByPlaceholderText('Experience or portfolio notes, one per line'), {
      target: { value: 'Built a sales dashboard' },
    });
    fireEvent.click(screen.getByRole('button', { name: 'Draft resume' }));

    expect(await screen.findByText('Results-driven analyst who ships dashboards.')).toBeInTheDocument();
    expect(screen.getByText('Python, SQL', { selector: 'p' })).toBeInTheDocument();
    expect(screen.getByText('Built a sales dashboard that cut reporting time by 40%')).toBeInTheDocument();

    const call = global.fetch.mock.calls.find(([url]) => url === '/api/pro/resume/draft');
    const body = JSON.parse(call[1].body);
    expect(body.skills).toEqual(['Python', 'SQL']);
    expect(body.experience).toEqual(['Built a sales dashboard']);
  });

  it('disables the draft button until skills or experience are entered', async () => {
    await goToCareerSection();
    expect(screen.getByRole('button', { name: 'Draft resume' })).toBeDisabled();

    fireEvent.change(resumeSkillsField(), {
      target: { value: 'Python' },
    });
    expect(screen.getByRole('button', { name: 'Draft resume' })).not.toBeDisabled();
  });

  it('exports the drafted resume as a PDF download', async () => {
    await goToCareerSection();

    fireEvent.change(resumeSkillsField(), {
      target: { value: 'Python' },
    });
    fireEvent.click(screen.getByRole('button', { name: 'Draft resume' }));
    await screen.findByText('Results-driven analyst who ships dashboards.');

    fireEvent.click(screen.getByRole('button', { name: 'Download PDF' }));

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        '/api/pro/resume/export',
        expect.objectContaining({ method: 'POST' })
      );
    });
    const call = global.fetch.mock.calls.find(([url]) => url === '/api/pro/resume/export');
    const body = JSON.parse(call[1].body);
    expect(body.format).toBe('pdf');
    expect(body.summary).toBe('Results-driven analyst who ships dashboards.');
  });
});
