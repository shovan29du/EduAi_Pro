import React, { useEffect, useState } from 'react';

const ROUND_SECONDS = 30;

export default function MathSprintGame({ title, blurb, generate }) {
  const [started, setStarted] = useState(false);
  const [finished, setFinished] = useState(false);
  const [score, setScore] = useState(0);
  const [total, setTotal] = useState(0);
  const [secondsLeft, setSecondsLeft] = useState(ROUND_SECONDS);
  const [current, setCurrent] = useState(null);

  useEffect(() => {
    if (!started || finished) return;
    if (secondsLeft <= 0) {
      setFinished(true);
      return;
    }
    const timer = setTimeout(() => setSecondsLeft((s) => s - 1), 1000);
    return () => clearTimeout(timer);
  }, [started, finished, secondsLeft]);

  function start() {
    setStarted(true);
    setFinished(false);
    setScore(0);
    setTotal(0);
    setSecondsLeft(ROUND_SECONDS);
    setCurrent(generate());
  }

  function answer(option) {
    setTotal((t) => t + 1);
    if (String(option) === String(current.answer)) {
      setScore((s) => s + 1);
    }
    setCurrent(generate());
  }

  return (
    <section aria-label={`${title} math sprint`} className="space-y-3 rounded border p-4 dark:border-gray-700">
      <h3 className="font-semibold">{title}</h3>
      {blurb && <p className="text-sm text-gray-600 dark:text-gray-400">{blurb}</p>}

      {!started && (
        <button type="button" onClick={start} className="rounded border px-3 py-1 text-sm">
          Start
        </button>
      )}

      {started && !finished && current && (
        <div className="space-y-2">
          <p className="text-sm">
            Time left: <span className="font-semibold">{secondsLeft}s</span> · Score:{' '}
            <span className="font-semibold">{score}</span> / {total}
          </p>
          <p className="text-2xl font-bold">{current.question}</p>
          <div className="flex flex-wrap gap-2">
            {current.options.map((opt, i) => (
              <button
                key={`${opt}-${i}`}
                type="button"
                onClick={() => answer(opt)}
                className="rounded border px-3 py-1 text-sm"
              >
                {opt}
              </button>
            ))}
          </div>
        </div>
      )}

      {finished && (
        <div className="space-y-2">
          <p className="font-medium">
            Time's up! Final score: {score} / {total}
          </p>
          <button type="button" onClick={start} className="rounded border px-3 py-1 text-sm">
            Play again
          </button>
        </div>
      )}
    </section>
  );
}
