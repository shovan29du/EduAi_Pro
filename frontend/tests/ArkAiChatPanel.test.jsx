import React from 'react';
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ArkAiChatPanel, { ARK_AI_AGENTS_ALL } from '../src/components/ArkAiChatPanel.jsx';

class MockRecognition {
  start() {
    this.onresult?.({ results: [[{ transcript: 'Hola, como estas?' }]] });
    this.onend?.();
  }
  stop() {
    this.onend?.();
  }
}

beforeEach(() => {
  global.fetch = vi.fn((url, options = {}) => {
    if (url === '/api/ark-ai/chat' && options.method === 'POST') {
      const body = JSON.parse(options.body);
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ reply: `[${body.agent}] (${body.context}) echo: ${body.message}` }),
      });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

afterEach(() => {
  delete window.SpeechRecognition;
  delete window.speechSynthesis;
  delete global.SpeechSynthesisUtterance;
});

describe('ArkAiChatPanel', () => {
  it('renders only the given agents and defaults to the requested one', async () => {
    render(
      <ArkAiChatPanel
        agents={[['partner', '🗣️ Spanish Partner']]}
        defaultAgent="partner"
        context="Learner practicing Spanish."
        emptyHint="Say hello!"
      />
    );
    expect(screen.getByText('Say hello!')).toBeInTheDocument();
    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Hola' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));

    expect(await screen.findByText('[partner] (Learner practicing Spanish.) echo: Hola')).toBeInTheDocument();
  });

  it('shows all agents including Singing Partner when given the full set', () => {
    render(<ArkAiChatPanel agents={ARK_AI_AGENTS_ALL} />);
    expect(screen.getByRole('button', { name: '🎤 Singing Partner' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: '🗣️ Partner' })).toBeInTheDocument();
  });

  it('fills and auto-sends the message from a voice command', async () => {
    window.SpeechRecognition = MockRecognition;
    render(<ArkAiChatPanel />);

    fireEvent.click(screen.getByLabelText('Speak a voice command to Ark AI'));

    expect(await screen.findByText('Hola, como estas?')).toBeInTheDocument();
    const call = global.fetch.mock.calls.find(([url]) => url === '/api/ark-ai/chat');
    const body = JSON.parse(call[1].body);
    expect(body.message).toBe('Hola, como estas?');
  });

  it('does not show the mic button when speech recognition is unsupported', () => {
    render(<ArkAiChatPanel />);
    expect(screen.queryByLabelText('Speak a voice command to Ark AI')).not.toBeInTheDocument();
  });

  it('speaks replies aloud when the voice-reply toggle is on', async () => {
    window.speechSynthesis = { speak: vi.fn(), cancel: vi.fn() };
    global.SpeechSynthesisUtterance = class SpeechSynthesisUtterance {
      constructor(text) { this.text = text; }
    };
    render(<ArkAiChatPanel />);

    fireEvent.click(screen.getByTitle('Read replies aloud'));
    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Hi' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));

    await waitFor(() => expect(window.speechSynthesis.speak).toHaveBeenCalled());
  });

  it('does not show the voice-reply toggle when speech synthesis is unsupported', () => {
    render(<ArkAiChatPanel />);
    expect(screen.queryByTitle('Read replies aloud')).not.toBeInTheDocument();
  });

  it('clears messages on New', async () => {
    render(<ArkAiChatPanel />);
    fireEvent.change(screen.getByPlaceholderText('Message Ark AI…'), { target: { value: 'Hi' } });
    fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    await screen.findByText('Hi');

    fireEvent.click(screen.getByRole('button', { name: 'New' }));
    expect(screen.queryByText('Hi')).not.toBeInTheDocument();
  });
});
