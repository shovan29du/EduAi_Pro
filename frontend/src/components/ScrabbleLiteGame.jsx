import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import { LETTER_VALUES, buildTileBag, VALID_WORDS } from '../data/scrabbleWords.js';
import GameScoreBadge from './GameScoreBadge.jsx';

const RACK_SIZE = 7;

function drawTiles(bag, count) {
  const drawn = bag.slice(0, count);
  return { drawn, rest: bag.slice(count) };
}

function initialState() {
  const bag = shuffle(buildTileBag());
  const { drawn, rest } = drawTiles(bag, RACK_SIZE);
  return { bag: rest, rack: drawn, score: 0, wordsPlayed: [] };
}

export default function ScrabbleLiteGame({ onComplete, stats }) {
  const [state, setState] = useState(initialState);
  const [pick, setPick] = useState([]); // [{ rackIndex, letter, isBlank }]
  const [message, setMessage] = useState('Tap rack tiles to spell a real word, then submit it.');
  const [finished, setFinished] = useState(false);

  const usedIndices = new Set(pick.map((p) => p.rackIndex));

  function tapTile(rackIndex) {
    if (finished || usedIndices.has(rackIndex)) return;
    const tile = state.rack[rackIndex];
    if (tile === '_') {
      const chosen = (window.prompt('Blank tile — which letter should it be? (A-Z)', 'E') || '').trim().toUpperCase();
      if (!/^[A-Z]$/.test(chosen)) return;
      setPick((p) => [...p, { rackIndex, letter: chosen, isBlank: true }]);
      return;
    }
    setPick((p) => [...p, { rackIndex, letter: tile, isBlank: false }]);
  }

  function clearPick() {
    setPick([]);
  }

  function submitWord() {
    if (finished || pick.length < 2) return;
    const word = pick.map((p) => p.letter).join('');
    if (!VALID_WORDS.has(word)) {
      setMessage(`"${word}" isn't in this game's word list — try another combination.`);
      setPick([]);
      return;
    }
    const base = pick.reduce((sum, p) => sum + (p.isBlank ? 0 : LETTER_VALUES[p.letter] || 0), 0);
    const bingo = pick.length === RACK_SIZE ? 50 : 0;
    const points = base + bingo;

    const usedRackIndices = new Set(pick.map((p) => p.rackIndex));
    const remainingRack = state.rack.filter((_, i) => !usedRackIndices.has(i));
    const { drawn, rest } = drawTiles(state.bag, RACK_SIZE - remainingRack.length);
    setState((s) => ({
      bag: rest,
      rack: [...remainingRack, ...drawn],
      score: s.score + points,
      wordsPlayed: [...s.wordsPlayed, { word, points }],
    }));
    setMessage(`"${word}" scored ${points} points${bingo ? ' (+50 bingo — used all 7 tiles!)' : ''}!`);
    setPick([]);
  }

  function finish() {
    setFinished(true);
    if (onComplete) {
      onComplete({
        score: state.score,
        maxScore: null,
        label: `Scrabble Lite — ${state.score} points across ${state.wordsPlayed.length} word${state.wordsPlayed.length === 1 ? '' : 's'}`,
      });
    }
  }

  function restart() {
    setState(initialState());
    setPick([]);
    setFinished(false);
    setMessage('Tap rack tiles to spell a real word, then submit it.');
  }

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🔤 Scrabble Lite</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Real Scrabble letter values and tile bag. Spell real words from your rack — use all 7 tiles in one word for a 50-point bingo bonus.</p>

      <div className="flex items-center justify-center gap-4 text-sm font-semibold text-gray-600 dark:text-gray-300">
        <span>Score: <span className="text-indigo-600 dark:text-indigo-400">{state.score}</span></span>
        <span>Tiles left in bag: {state.bag.length}</span>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center min-h-[48px] flex items-center justify-center gap-1">
        {pick.length === 0 && <span className="text-sm text-indigo-400">Your word will appear here</span>}
        {pick.map((p, i) => (
          <span key={i} className="w-9 h-9 rounded bg-amber-200 border-2 border-amber-400 flex items-center justify-center font-bold text-amber-900">
            {p.letter}
          </span>
        ))}
      </div>

      <div>
        <p className="text-xs font-semibold text-gray-500 uppercase mb-2">Your Rack</p>
        <div className="flex flex-wrap gap-2 justify-center">
          {state.rack.map((tile, i) => (
            <button
              key={i}
              disabled={finished || usedIndices.has(i)}
              onClick={() => tapTile(i)}
              className="relative w-12 h-12 rounded-lg border-2 border-gray-300 bg-white dark:bg-gray-800 disabled:opacity-30 flex items-center justify-center font-bold text-lg text-gray-800 dark:text-gray-100"
            >
              {tile === '_' ? '?' : tile}
              <span className="absolute bottom-0.5 right-1 text-[9px] font-normal text-gray-400">{LETTER_VALUES[tile]}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="flex justify-center gap-3">
        <button onClick={clearPick} disabled={finished || pick.length === 0} className="rounded-full bg-gray-300 hover:bg-gray-400 disabled:opacity-40 text-gray-800 font-semibold px-4 py-2 text-sm">
          Clear
        </button>
        <button onClick={submitWord} disabled={finished || pick.length < 2} className="rounded-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white font-semibold px-4 py-2 text-sm">
          Submit Word
        </button>
      </div>

      <p className="text-center text-sm text-gray-600 dark:text-gray-300">{message}</p>

      {state.wordsPlayed.length > 0 && (
        <div className="flex flex-wrap gap-1.5 justify-center">
          {state.wordsPlayed.map((w, i) => (
            <span key={i} className="text-xs rounded-full px-2.5 py-0.5 bg-emerald-100 text-emerald-700 dark:bg-emerald-900 dark:text-emerald-300">{w.word} +{w.points}</span>
          ))}
        </div>
      )}

      <div className="flex justify-center gap-3">
        {!finished ? (
          <button onClick={finish} className="rounded-full bg-amber-500 hover:bg-amber-600 text-white font-semibold px-6 py-2.5">
            Finish &amp; Score
          </button>
        ) : (
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        )}
      </div>
    </div>
  );
}
