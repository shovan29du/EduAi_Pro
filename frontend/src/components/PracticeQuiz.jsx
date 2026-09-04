import React, { useEffect, useMemo, useState } from 'react';
import { useChild } from '../contexts/ChildContext.jsx';
import { fetchPersonalizedProfile, recordLearningEvidence } from '../api/personalized.js';

// SM-2-lite spaced repetition: each question gets an interval (in days) that
// grows on a correct answer and resets on a miss, with a "due" timestamp
// used to prioritize what to show next.
const INTERVALS_DAYS = [0, 1, 3, 7, 14, 30];

function storageKey(child, subjectName) {
  return `practiceSchedule:${child}:${subjectName}`;
}

function loadSchedule(child, subjectName) {
  try {
    return JSON.parse(localStorage.getItem(storageKey(child, subjectName)) || '{}');
  } catch {
    return {};
  }
}

function saveSchedule(child, subjectName, schedule) {
  localStorage.setItem(storageKey(child, subjectName), JSON.stringify(schedule));
}

function nextIntervalIndex(record, correct) {
  if (!correct) return 0;
  const current = record?.intervalIndex ?? -1;
  return Math.min(current + 1, INTERVALS_DAYS.length - 1);
}

function dueDate(intervalIndex) {
  const days = INTERVALS_DAYS[intervalIndex];
  return Date.now() + days * 24 * 60 * 60 * 1000;
}

function orderBySchedule(questions, schedule) {
  const now = Date.now();
  return [...questions].sort((a, b) => {
    const ra = schedule[a.question];
    const rb = schedule[b.question];
    const dueA = ra ? ra.due : now;
    const dueB = rb ? rb.due : now;
    return dueA - dueB;
  });
}

function questionText(question) {
  return question.question || question.q || question.prompt || 'Practice question';
}

function inferConcept(question, concepts) {
  const explicit = question.concept || question.skill || question.topic;
  if (explicit) return explicit;
  const prompt = questionText(question).toLowerCase();
  return concepts.find((concept) => prompt.includes(concept.toLowerCase())) || concepts[0] || 'General practice';
}

export default function PracticeQuiz({ subjectName, questions, levelId = '1', concepts = [] }) {
  const { child } = useChild();
  const [schedule, setSchedule] = useState(() => loadSchedule(child, subjectName));
  const [answers, setAnswers] = useState({});
  const [feedback, setFeedback] = useState({});
  const [targetDifficulty, setTargetDifficulty] = useState(1);
  const safeQuestions = questions || [];

  useEffect(() => {
    fetchPersonalizedProfile(child, levelId, subjectName)
      .then((profile) => setTargetDifficulty(profile.next_lesson?.difficulty || 1))
      .catch(() => setTargetDifficulty(1));
  }, [child, levelId, subjectName]);

  const ordered = useMemo(() => {
    const scheduled = orderBySchedule(safeQuestions, schedule);
    return scheduled.sort((a, b) => {
      const aDifficulty = Number(a.difficulty || targetDifficulty);
      const bDifficulty = Number(b.difficulty || targetDifficulty);
      return Math.abs(aDifficulty - targetDifficulty) - Math.abs(bDifficulty - targetDifficulty);
    });
  }, [safeQuestions, schedule, targetDifficulty]);
  const now = Date.now();

  if (!safeQuestions.length) return null;

  function checkAnswer(question, given) {
    const correct = String(given).trim().toLowerCase() === String(question.answer).trim().toLowerCase();
    const prompt = questionText(question);
    setFeedback((prev) => ({ ...prev, [prompt]: correct ? 'correct' : 'incorrect' }));
    setSchedule((prev) => {
      const intervalIndex = nextIntervalIndex(prev[prompt], correct);
      const next = {
        ...prev,
        [prompt]: { intervalIndex, due: dueDate(intervalIndex), lastCorrect: correct },
      };
      saveSchedule(child, subjectName, next);
      return next;
    });
    recordLearningEvidence(child, {
      level_id: String(levelId),
      subject: subjectName,
      concept: inferConcept(question, concepts),
      correct,
      question_id: prompt,
      answer: String(given),
      expected_answer: String(question.answer),
      confidence: 1,
    }).then((result) => setTargetDifficulty(result.difficulty)).catch(() => {});
  }

  return (
    <div className="space-y-3">
      <p className="text-sm text-gray-600 dark:text-gray-400">
        Questions are shown in review order: ones you missed (or haven't tried) come first, and
        ones you've gotten right recently are spaced further apart. Current adaptive difficulty:
        {' '}{targetDifficulty}/5.
      </p>
      {ordered.map((q) => {
        const prompt = questionText(q);
        const record = schedule[prompt];
        const isDueReview = record && !record.lastCorrect;
        const isFutureReview = record && record.lastCorrect && record.due > now;
        const result = feedback[prompt];
        return (
          <div
            key={prompt}
            className={`rounded border p-3 dark:border-gray-700 ${isDueReview ? 'border-orange-500' : ''}`}
          >
            <p className="font-medium">
              Practice Question: {prompt}{' '}
              {isDueReview && <span className="text-orange-600">(due for review)</span>}
              {isFutureReview && <span className="text-green-600">(reviewed — spaced out)</span>}
            </p>
            {q.type === 'multiple_choice' && q.options?.length > 0 ? (
              <div className="mt-2 space-y-1">
                {q.options.map((opt) => (
                  <label key={opt} className="block text-sm">
                    <input
                      type="radio"
                      name={`practice-${prompt}`}
                      value={opt}
                      checked={answers[prompt] === opt}
                      onChange={() => {
                        setAnswers((prev) => ({ ...prev, [prompt]: opt }));
                        checkAnswer(q, opt);
                      }}
                    />{' '}
                    {opt}
                  </label>
                ))}
              </div>
            ) : (
              <form
                className="mt-2 flex items-center gap-2"
                onSubmit={(e) => {
                  e.preventDefault();
                  checkAnswer(q, answers[prompt] || '');
                }}
              >
                <input
                  type="text"
                  value={answers[prompt] || ''}
                  onChange={(e) => setAnswers((prev) => ({ ...prev, [prompt]: e.target.value }))}
                  className="rounded border px-2 py-1 text-sm dark:bg-gray-800 dark:text-white"
                />
                <button type="submit" className="rounded border px-2 py-1 text-sm">
                  Check
                </button>
              </form>
            )}
            {result === 'correct' && <p className="mt-1 text-sm text-green-600">Correct! ✓</p>}
            {result === 'incorrect' && (
              <p className="mt-1 text-sm text-red-600">Not quite. Answer: {q.answer}</p>
            )}
          </div>
        );
      })}
    </div>
  );
}
