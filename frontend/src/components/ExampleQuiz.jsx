import React, { useEffect, useState } from 'react';
import { getExampleQuiz } from '../api/lessonExamples.js';

const norm = (text) => text.toLowerCase().replace(/[^a-z0-9 ]+/g, ' ');

// Offline / no-AI fallback: the student writes one sentence and we check it
// against the lesson's own key concepts, so the exercise still has feedback.
export function conceptsUsed(answer, concepts = []) {
  const words = new Set(norm(answer).split(/\s+/).filter(Boolean));
  const matched = [];
  const missed = [];
  for (const concept of concepts) {
    const parts = norm(concept).split(/\s+/).filter((w) => w.length > 2);
    const hit = parts.length > 0 && parts.some((w) => words.has(w) || words.has(w.replace(/s$/, '')) || words.has(`${w}s`));
    (hit ? matched : missed).push(concept);
  }
  return { matched, missed };
}

function Questions({ questions }) {
  const [picked, setPicked] = useState({});
  const [checked, setChecked] = useState(false);
  const score = questions.filter((q, i) => picked[i] === q.answer).length;

  return (
    <div className="mt-3 space-y-4">
      {questions.map((q, i) => (
        <fieldset key={i} disabled={checked}>
          <legend className="text-sm font-medium">{i + 1}. {q.question}</legend>
          <div className="mt-1 space-y-1">
            {Object.entries(q.options).map(([letter, text]) => {
              const isRight = checked && letter === q.answer;
              const isWrong = checked && picked[i] === letter && letter !== q.answer;
              return (
                <label
                  key={letter}
                  className={`flex items-center gap-2 rounded-lg border px-3 py-1.5 text-sm ${
                    isRight ? 'border-green-500 bg-green-50 text-green-800' : isWrong ? 'border-red-400 bg-red-50 text-red-700' : 'border-gray-200 dark:border-gray-700'
                  }`}
                >
                  <input type="radio" name={`example-q${i}`} checked={picked[i] === letter} onChange={() => setPicked((p) => ({ ...p, [i]: letter }))} />
                  {text}
                </label>
              );
            })}
          </div>
          {checked && q.explanation && <p className="mt-1 text-xs text-gray-600 dark:text-gray-300">{q.explanation}</p>}
        </fieldset>
      ))}
      {!checked ? (
        <button
          type="button"
          disabled={Object.keys(picked).length < questions.length}
          onClick={() => setChecked(true)}
          className="rounded-lg bg-emerald-600 px-4 py-2 text-sm font-medium text-white hover:bg-emerald-700 disabled:opacity-50"
        >
          Check answers
        </button>
      ) : (
        <p className="text-sm font-semibold" role="status">
          {score} / {questions.length} correct{score === questions.length ? ' — well done!' : ' — read the example again and try once more.'}
          <button type="button" onClick={() => { setPicked({}); setChecked(false); }} className="ml-3 text-xs font-normal text-emerald-700 underline">Try again</button>
        </p>
      )}
    </div>
  );
}

function SelfCheck({ concepts, title }) {
  const [answer, setAnswer] = useState('');
  const [result, setResult] = useState(null);
  const usable = (concepts || []).filter(Boolean);

  return (
    <div className="mt-3">
      <label className="block text-sm font-medium" htmlFor="example-self-check">
        In one or two sentences, explain how “{title}” shows up in this example.
      </label>
      <textarea
        id="example-self-check"
        value={answer}
        onChange={(e) => { setAnswer(e.target.value); setResult(null); }}
        rows={3}
        className="mt-1 w-full rounded-lg border px-3 py-2 text-sm dark:border-gray-600 dark:bg-gray-800"
      />
      <button
        type="button"
        disabled={answer.trim().length < 10}
        onClick={() => setResult(conceptsUsed(answer, usable))}
        className="mt-2 rounded-lg bg-emerald-600 px-4 py-2 text-sm font-medium text-white hover:bg-emerald-700 disabled:opacity-50"
      >
        Check my answer
      </button>
      {result && (
        <div className="mt-2 text-sm" role="status">
          {usable.length === 0 && <p>Nice work — compare your answer with the example above.</p>}
          {result.matched.length > 0 && <p className="text-green-700 dark:text-green-400">You used: {result.matched.join(', ')}.</p>}
          {result.missed.length > 0 && <p className="text-gray-700 dark:text-gray-300">Could you also mention: {result.missed.join(', ')}?</p>}
        </div>
      )}
    </div>
  );
}

export default function ExampleQuiz({ example, title, subject, level, concepts }) {
  const [state, setState] = useState({ status: 'idle', questions: [] });

  useEffect(() => { setState({ status: 'idle', questions: [] }); }, [example]);

  function start() {
    setState({ status: 'loading', questions: [] });
    getExampleQuiz({ example, title, subject, level })
      .then((data) => setState(data.questions?.length ? { status: 'quiz', questions: data.questions } : { status: 'selfcheck', questions: [] }))
      .catch(() => setState({ status: 'selfcheck', questions: [] }));
  }

  return (
    <div className="mt-4 border-t border-emerald-200 pt-3 dark:border-emerald-800">
      {state.status === 'idle' && (
        <button type="button" onClick={start} className="rounded-lg border border-emerald-600 px-4 py-2 text-sm font-medium text-emerald-700 hover:bg-emerald-100 dark:text-emerald-300 dark:hover:bg-emerald-900">
          Test yourself on this example
        </button>
      )}
      {state.status === 'loading' && <p className="text-sm text-gray-600 dark:text-gray-300">Preparing your questions…</p>}
      {state.status === 'quiz' && <Questions questions={state.questions} />}
      {state.status === 'selfcheck' && <SelfCheck concepts={concepts} title={title} />}
    </div>
  );
}
