import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import UpdatePrompt from '../src/components/UpdatePrompt.jsx';

const state = { needRefresh: false, offlineReady: false };
let capturedOnRegisteredSW;
let updateServiceWorkerMock;

vi.mock('virtual:pwa-register/react', () => ({
  useRegisterSW: (opts) => {
    capturedOnRegisteredSW = opts?.onRegisteredSW;
    updateServiceWorkerMock = vi.fn();
    return {
      needRefresh: [state.needRefresh, (v) => { state.needRefresh = v; }],
      offlineReady: [state.offlineReady, (v) => { state.offlineReady = v; }],
      updateServiceWorker: updateServiceWorkerMock,
    };
  },
}));

beforeEach(() => {
  state.needRefresh = false;
  state.offlineReady = false;
  vi.useRealTimers();
});

describe('UpdatePrompt', () => {
  it('renders nothing when no update is available and the app is not freshly offline-ready', () => {
    const { container } = render(<UpdatePrompt />);
    expect(container).toBeEmptyDOMElement();
  });

  it('shows an update banner and calls updateServiceWorker(true) on click', () => {
    state.needRefresh = true;
    render(<UpdatePrompt />);
    expect(screen.getByText(/new version of EduAi_Pro is available/i)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: /update now/i }));
    expect(updateServiceWorkerMock).toHaveBeenCalledWith(true);
  });

  it('dismisses the update banner via "Later"', () => {
    state.needRefresh = true;
    render(<UpdatePrompt />);
    fireEvent.click(screen.getByRole('button', { name: /later/i }));
    expect(screen.queryByText(/new version of EduAi_Pro is available/i)).not.toBeInTheDocument();
  });

  it('shows an offline-ready toast', () => {
    state.offlineReady = true;
    render(<UpdatePrompt />);
    expect(screen.getByText(/ready to work offline/i)).toBeInTheDocument();
  });

  it('registers a listener that re-checks for updates on the eduai-check-for-updates event', () => {
    render(<UpdatePrompt />);
    const registration = { update: vi.fn().mockResolvedValue(undefined) };
    act(() => {
      capturedOnRegisteredSW('/sw.js', registration);
    });
    window.dispatchEvent(new Event('eduai-check-for-updates'));
    expect(registration.update).toHaveBeenCalled();
  });
});
