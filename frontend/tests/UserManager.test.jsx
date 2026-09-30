import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import UserManager from '../src/components/UserManager.jsx';

const users = {
  users: [
    { name: 'Shovan', role: 'parent' },
  ],
};

function mockFetch() {
  return vi.fn((url, options = {}) => {
    const u = String(url);
    if (u === '/api/users' && (!options.method || options.method === 'GET')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(users) });
    }
    if (u === '/api/users/Shovan' && options.method === 'PUT') {
      return Promise.resolve({ ok: false, json: () => Promise.resolve({ detail: 'Cannot rename the Parent account' }) });
    }
    if (u === '/api/users/Shovan' && options.method === 'DELETE') {
      return Promise.resolve({ ok: false, json: () => Promise.resolve({ detail: 'Cannot delete the Parent account' }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('UserManager', () => {
  it('does not render an Add User form, since new users cannot be created', async () => {
    render(<UserManager />);
    await screen.findByText('Shovan');
    expect(screen.queryByText('+ Add User')).not.toBeInTheDocument();
    expect(screen.getByText(/single-administrator installation/i)).toBeInTheDocument();
  });

  it('marks the actual protected user (Shovan) as Protected and disables Edit/Delete for them', async () => {
    render(<UserManager />);
    await screen.findByText('Shovan');

    expect(screen.getByText('Protected')).toBeInTheDocument();
    expect(screen.queryByRole('button', { name: 'Edit' })).not.toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Delete' })).toBeDisabled();
  });
});
