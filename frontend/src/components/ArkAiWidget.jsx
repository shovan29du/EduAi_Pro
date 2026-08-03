import { useRef, useState, useEffect } from 'react';
import { sendArkAiMessage } from '../api/arkAi.js';

export default function ArkAiWidget({ level }) {
  const [open, setOpen] = useState(false);
  const [agent, setAgent] = useState('teacher');
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [sending, setSending] = useState(false);
  const [error, setError] = useState('');
  const listRef = useRef(null);

  useEffect(() => {
    if (listRef.current) {
      listRef.current.scrollTop = listRef.current.scrollHeight;
    }
  }, [messages, open]);

  async function handleSend(event) {
    event.preventDefault();
    const text = input.trim();
    if (!text || sending) return;
    const history = messages;
    const nextMessages = [...messages, { role: 'user', content: text }];
    setMessages(nextMessages);
    setInput('');
    setError('');
    setSending(true);
    try {
      const data = await sendArkAiMessage(text, history, { agent, level });
      setMessages((prev) => [...prev, { role: 'assistant', content: data.reply }]);
    } catch (err) {
      setError(err.message);
    } finally {
      setSending(false);
    }
  }

  function handleNewChat() {
    setMessages([]);
    setError('');
  }

  return (
    <div className="fixed bottom-4 right-4 z-50">
      {open && (
        <div className="mb-3 flex h-[28rem] w-[22rem] max-w-[90vw] flex-col overflow-hidden rounded-2xl border border-white/20 bg-white shadow-2xl dark:border-gray-700 dark:bg-gray-900">
          <div className="flex items-center justify-between gap-2 bg-gradient-to-r from-indigo-600 via-violet-600 to-pink-600 px-4 py-3 text-white">
            <div>
              <p className="text-sm font-bold">✨ Ark AI</p>
              <p className="text-[11px] opacity-90">Your teacher, instructor & helper — on every page</p>
            </div>
            <div className="flex items-center gap-1">
              <button
                type="button"
                onClick={handleNewChat}
                title="New chat"
                className="rounded-full bg-white/20 px-2 py-1 text-xs font-medium hover:bg-white/30"
              >
                New
              </button>
              <button
                type="button"
                onClick={() => setOpen(false)}
                aria-label="Close Ark AI"
                className="rounded-full bg-white/20 px-2 py-1 text-xs font-medium hover:bg-white/30"
              >
                ✕
              </button>
            </div>
          </div>

          <div className="flex gap-1 border-b bg-gray-50 px-3 py-2 dark:border-gray-700 dark:bg-gray-800" role="group" aria-label="Ark AI agent">
            {[
              ['teacher', '🧑‍🏫 Teacher'],
              ['instructor', '📋 Instructor'],
              ['helper', '🤝 Helper'],
            ].map(([value, label]) => (
              <button
                key={value}
                type="button"
                onClick={() => setAgent(value)}
                aria-pressed={agent === value}
                className={`rounded-full px-3 py-1 text-xs font-semibold transition ${
                  agent === value
                    ? 'bg-indigo-600 text-white'
                    : 'bg-white text-gray-600 dark:bg-gray-700 dark:text-gray-300'
                }`}
              >
                {label}
              </button>
            ))}
          </div>

          <div ref={listRef} className="flex-1 space-y-2 overflow-y-auto p-3">
            {messages.length === 0 && (
              <p className="text-sm text-gray-400">
                Ask Ark AI anything. Teacher explains and builds understanding, Instructor gives step-by-step
                guidance, and Helper gives fast, general-purpose assistance.
              </p>
            )}
            {messages.map((m, index) => (
              <div
                key={index}
                className={`max-w-[85%] whitespace-pre-wrap rounded-2xl px-3 py-2 text-sm ${
                  m.role === 'user'
                    ? 'ml-auto bg-indigo-600 text-white'
                    : 'bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-100'
                }`}
              >
                {m.content}
              </div>
            ))}
            {sending && <p className="text-xs text-gray-400">Ark AI is thinking…</p>}
          </div>

          {error && <p role="alert" className="mx-3 mb-2 rounded bg-red-50 p-2 text-xs text-red-700">{error}</p>}

          <form onSubmit={handleSend} className="flex gap-2 border-t p-2 dark:border-gray-700">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Message Ark AI…"
              className="min-w-0 flex-1 rounded-full border px-3 py-1.5 text-sm dark:border-gray-600 dark:bg-gray-800"
            />
            <button
              type="submit"
              disabled={sending || !input.trim()}
              className="rounded-full bg-indigo-600 px-4 py-1.5 text-sm font-semibold text-white disabled:opacity-50"
            >
              Send
            </button>
          </form>
        </div>
      )}

      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        aria-label={open ? 'Close Ark AI' : 'Open Ark AI'}
        className="flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-indigo-600 via-violet-600 to-pink-600 text-2xl text-white shadow-xl transition hover:scale-105"
      >
        {open ? '✕' : '✨'}
      </button>
    </div>
  );
}
