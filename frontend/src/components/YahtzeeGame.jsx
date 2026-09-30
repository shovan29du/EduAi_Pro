import React, { useState } from 'react';
import { randInt } from '../utils/gameUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

const CATEGORIES = [
  { id: 'ones', label: 'Ones', hint: 'Sum of all 1s' },
  { id: 'twos', label: 'Twos', hint: 'Sum of all 2s' },
  { id: 'threes', label: 'Threes', hint: 'Sum of all 3s' },
  { id: 'fours', label: 'Fours', hint: 'Sum of all 4s' },
  { id: 'fives', label: 'Fives', hint: 'Sum of all 5s' },
  { id: 'sixes', label: 'Sixes', hint: 'Sum of all 6s' },
  { id: 'threeKind', label: '3 of a Kind', hint: 'Sum of all dice if 3+ match' },
  { id: 'fourKind', label: '4 of a Kind', hint: 'Sum of all dice if 4+ match' },
  { id: 'fullHouse', label: 'Full House', hint: '25 pts for a triple + a pair' },
  { id: 'smallStraight', label: 'Small Straight', hint: '30 pts for 4 in a row' },
  { id: 'largeStraight', label: 'Large Straight', hint: '40 pts for 5 in a row' },
  { id: 'yahtzee', label: 'Yahtzee', hint: '50 pts for all 5 matching' },
  { id: 'chance', label: 'Chance', hint: 'Sum of all dice' },
];

function counts(dice) {
  const c = Array(7).fill(0);
  for (const d of dice) c[d] += 1;
  return c;
}

function sumOf(dice, face) {
  return dice.filter((d) => d === face).length * face;
}

function scoreFor(id, dice) {
  const c = counts(dice);
  const total = dice.reduce((a, b) => a + b, 0);
  switch (id) {
    case 'ones': return sumOf(dice, 1);
    case 'twos': return sumOf(dice, 2);
    case 'threes': return sumOf(dice, 3);
    case 'fours': return sumOf(dice, 4);
    case 'fives': return sumOf(dice, 5);
    case 'sixes': return sumOf(dice, 6);
    case 'threeKind': return c.some((n) => n >= 3) ? total : 0;
    case 'fourKind': return c.some((n) => n >= 4) ? total : 0;
    case 'fullHouse': return c.includes(3) && c.includes(2) ? 25 : 0;
    case 'smallStraight': {
      const set = new Set(dice);
      const runs = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]];
      return runs.some((r) => r.every((v) => set.has(v))) ? 30 : 0;
    }
    case 'largeStraight': {
      const sorted = [...new Set(dice)].sort().join('');
      return sorted === '12345' || sorted === '23456' ? 40 : 0;
    }
    case 'yahtzee': return c.some((n) => n === 5) ? 50 : 0;
    case 'chance': return total;
    default: return 0;
  }
}

function rollDice(count) {
  return Array.from({ length: count }, () => randInt(1, 6));
}

export default function YahtzeeGame({ onComplete, stats }) {
  const [dice, setDice] = useState(() => rollDice(5));
  const [held, setHeld] = useState([false, false, false, false, false]);
  const [rollsLeft, setRollsLeft] = useState(2);
  const [scores, setScores] = useState({});
  const [finished, setFinished] = useState(false);

  function toggleHold(i) {
    if (finished) return;
    setHeld((h) => h.map((v, idx) => (idx === i ? !v : v)));
  }

  function roll() {
    if (finished || rollsLeft === 0) return;
    setDice((d) => d.map((v, i) => (held[i] ? v : randInt(1, 6))));
    setRollsLeft((r) => r - 1);
  }

  function chooseCategory(id) {
    if (finished || scores[id] != null) return;
    const nextScores = { ...scores, [id]: scoreFor(id, dice) };
    setScores(nextScores);
    setHeld([false, false, false, false, false]);
    setRollsLeft(2);
    if (Object.keys(nextScores).length === CATEGORIES.length) {
      const total = Object.values(nextScores).reduce((a, b) => a + b, 0);
      setFinished(true);
      if (onComplete) onComplete({ score: total, maxScore: null, label: `Yahtzee — final score ${total}` });
    } else {
      setDice(rollDice(5));
    }
  }

  function restart() {
    setDice(rollDice(5));
    setHeld([false, false, false, false, false]);
    setRollsLeft(2);
    setScores({});
    setFinished(false);
  }

  const total = Object.values(scores).reduce((a, b) => a + b, 0);

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🎲 Yahtzee</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Roll up to 3 times per turn, holding any dice you like, then lock in one scoring category. Fill all 13 for your final score.</p>

      <div className="flex justify-center gap-3">
        {dice.map((d, i) => (
          <button
            key={i}
            onClick={() => toggleHold(i)}
            disabled={finished}
            className={`w-14 h-14 rounded-lg border-2 text-2xl font-bold flex items-center justify-center ${
              held[i] ? 'border-amber-500 bg-amber-100 dark:bg-amber-900' : 'border-gray-300 bg-white dark:bg-gray-800'
            }`}
          >
            {d}
          </button>
        ))}
      </div>

      <div className="flex justify-center items-center gap-4">
        <button
          onClick={roll}
          disabled={finished || rollsLeft === 0}
          className="rounded-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white font-semibold px-5 py-2"
        >
          Roll ({rollsLeft} left)
        </button>
        <span className="text-sm font-semibold text-gray-600 dark:text-gray-300">Total: {total}</span>
      </div>

      <div className="grid sm:grid-cols-2 gap-2">
        {CATEGORIES.map((cat) => {
          const used = scores[cat.id] != null;
          const preview = scoreFor(cat.id, dice);
          return (
            <button
              key={cat.id}
              disabled={finished || used}
              onClick={() => chooseCategory(cat.id)}
              className={`text-left rounded-lg border px-3 py-2 text-sm flex items-center justify-between ${
                used ? 'border-gray-200 bg-gray-50 dark:bg-gray-800 text-gray-400' : 'border-indigo-200 dark:border-indigo-800 hover:bg-indigo-50 dark:hover:bg-indigo-950'
              }`}
            >
              <span>
                <span className="font-semibold">{cat.label}</span>
                <span className="block text-[10px] text-gray-400">{cat.hint}</span>
              </span>
              <span className="font-bold">{used ? scores[cat.id] : preview}</span>
            </button>
          );
        })}
      </div>

      {finished && (
        <div className="text-center space-y-3">
          <p className="font-bold text-lg text-gray-800 dark:text-gray-100">🎉 Final score: {total}</p>
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        </div>
      )}
    </div>
  );
}
