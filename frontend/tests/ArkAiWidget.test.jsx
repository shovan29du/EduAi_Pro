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
        json: () => Promise.resolve({ reply: `[${body.agent}] echo: ${body.message}` }),
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

  it('sends a message with the default Teacher agent and displays the reply', async () => {
    render(<ArkAiWidget level="1" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Hello there' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));

    expect(await screen.findByText('Hello there')).toBeInTheDocument();
    expect(await screen.findByText('[teacher] echo: Hello there')).toBeInTheDocument();

    const call = global.fetch.mock.calls.find(([url]) => url === '/api/ark-ai/chat');
    const body = JSON.parse(call[1].body);
    expect(body).toEqual({ message: 'Hello there', history: [], agent: 'teacher', level: '1', context: '' });
  });

  it('switches to the Instructor agent and includes prior turns as history', async () => {
    render(<ArkAiWidget level="5" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'First' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    await screen.findByText('[teacher] echo: First');

    fireEvent.click(screen.getByRole('button', { name: '📋 Instructor' }));
    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Second' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    await screen.findByText('[instructor] echo: Second');

    const calls = global.fetch.mock.calls.filter(([url]) => url === '/api/ark-ai/chat');
    const secondBody = JSON.parse(calls[1][1].body);
    expect(secondBody.agent).toBe('instructor');
    expect(secondBody.history).toEqual([
      { role: 'user', content: 'First' },
      { role: 'assistant', content: '[teacher] echo: First' },
    ]);
  });

  it('switches to the Helper agent', async () => {
    render(<ArkAiWidget level="1" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.click(screen.getByRole('button', { name: '🤝 Helper' }));
    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Quick question' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));

    expect(await screen.findByText('[helper] echo: Quick question')).toBeInTheDocument();
  });

  it('clears the conversation when New is clicked', async () => {
    render(<ArkAiWidget level="1" />);
    fireEvent.click(screen.getByLabelText('Open Ark AI'));

    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Hello' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    await screen.findByText('[teacher] echo: Hello');

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
