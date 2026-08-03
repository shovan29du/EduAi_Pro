import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ArkAiWidget from '../src/components/ArkAiWidget.jsx';

beforeEach(() => {
  global.fetch = vi.fn((url, options = {}) => {
    if (url === '/api/ark-ai/chat' && options.method === 'POST') {
      const body = JSON.parse(options.body);
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ reply: `[${body.mode}] echo: ${body.message}` }),
      });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('ArkAiWidget', () => {
  it('is closed by default and opens the chat panel on click', () => {
    render(<ArkAiWidget level="1" />);
    expect(screen.queryByText('✨ Ark AI')).not.toBeInTheDocument();

    fireEvent.click(screen.getByLabelText('Open Ark AI'));
    expect(screen.getByText('✨ Ark AI')).toBeInTheDocument();
  });

  it('sends a message and displays the reply', async () => {
    render(<ArkAiWidget level="1" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Hello there' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));

    expect(await screen.findByText('Hello there')).toBeInTheDocument();
    expect(await screen.findByText('[chat] echo: Hello there')).toBeInTheDocument();

    const call = global.fetch.mock.calls.find(([url]) => url === '/api/ark-ai/chat');
    const body = JSON.parse(call[1].body);
    expect(body).toEqual({ message: 'Hello there', history: [], mode: 'chat', level: '1' });
  });

  it('switches to Learn mode and includes prior turns as history', async () => {
    render(<ArkAiWidget level="5" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'First' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    await screen.findByText('[chat] echo: First');

    fireEvent.click(screen.getByRole('button', { name: '🎓 Learn' }));
    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Second' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    await screen.findByText('[learn] echo: Second');

    const calls = global.fetch.mock.calls.filter(([url]) => url === '/api/ark-ai/chat');
    const secondBody = JSON.parse(calls[1][1].body);
    expect(secondBody.mode).toBe('learn');
    expect(secondBody.history).toEqual([
      { role: 'user', content: 'First' },
      { role: 'assistant', content: '[chat] echo: First' },
    ]);
  });

  it('clears the conversation when New is clicked', async () => {
    render(<ArkAiWidget level="1" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Hello' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    await screen.findByText('[chat] echo: Hello');

    fireEvent.click(screen.getByRole('button', { name: 'New' }));
    expect(screen.queryByText('Hello')).not.toBeInTheDocument();
  });

  it('shows an error message when the request fails', async () => {
    global.fetch = vi.fn(() => Promise.resolve({ ok: false, status: 400, json: () => Promise.resolve({ detail: 'message is required' }) }));
    render(<ArkAiWidget level="1" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'x' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));

    expect(await screen.findByText('message is required')).toBeInTheDocument();
  });
});
