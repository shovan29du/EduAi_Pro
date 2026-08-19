import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import { buildDeck, RANKS } from '../utils/cardUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

function extractBooks(hand) {
  const byRank = {};
  for (const card of hand) {
    byRank[card.rank] = byRank[card.rank] || [];
    byRank[card.rank].push(card);
  }
  const books = [];
  let remaining = [];
  for (const rank of Object.keys(byRank)) {
    if (byRank[rank].length === 4) books.push(rank);
    else remaining = remaining.concat(byRank[rank]);
  }
  return { books, remaining };
}

function ranksInHand(hand) {
  return [...new Set(hand.map((c) => c.rank))];
}

function deal() {
  const deck = shuffle(buildDeck());
  const player = deck.slice(0, 7);
  const cpu = deck.slice(7, 14);
  const pond = deck.slice(14);
  return { player, cpu, pond, playerBooks: [], cpuBooks: [] };
}

export default function GoFishGame({ onComplete, stats }) {
  const [state, setState] = useState(deal);
  const [turn, setTurn] = useState('player');
  const [log, setLog] = useState(['Ask the computer for a rank you hold.']);
  const [finished, setFinished] = useState(false);

  function pushLog(line) {
    setLog((l) => [line, ...l].slice(0, 6));
  }

  function checkGameOver(next) {
    const totalBooks = next.playerBooks.length + next.cpuBooks.length;
    if (totalBooks >= 13) {
      setFinished(true);
      if (onComplete) {
        onComplete({
          score: next.playerBooks.length,
          maxScore: 13,
          label: `Go Fish — ${next.playerBooks.length} books to the computer's ${next.cpuBooks.length}`,
        });
      }
      return true;
    }
    return false;
  }

  function cpuTurn(current) {
    let s = current;
    let guard = 0;
    while (guard < 20) {
      guard += 1;
      const cpuRanks = ranksInHand(s.cpu);
      if (cpuRanks.length === 0) break;
      const ask = cpuRanks[Math.floor(Math.random() * cpuRanks.length)];
      const matches = s.player.filter((c) => c.rank === ask);
      if (matches.length > 0) {
        pushLog(`Computer asked you for ${ask}s and got ${matches.length}.`);
        const newCpuHand = [...s.cpu, ...matches];
        const newPlayerHand = s.player.filter((c) => c.rank !== ask);
        const { books: newBooks, remaining } = extractBooks(newCpuHand);
        s = {
          ...s,
          cpu: remaining,
          player: newPlayerHand,
          cpuBooks: [...s.cpuBooks, ...newBooks],
        };
        if (checkGameOver(s)) return s;
        continue; // CPU goes again
      }
      pushLog(`Computer asked for ${ask}s — Go Fish!`);
      if (s.pond.length === 0) break;
      const [drawn, ...restPond] = s.pond;
      const newCpuHand = [...s.cpu, drawn];
      const { books: newBooks, remaining } = extractBooks(newCpuHand);
      s = { ...s, cpu: remaining, pond: restPond, cpuBooks: [...s.cpuBooks, ...newBooks] };
      if (checkGameOver(s)) return s;
      if (drawn.rank === ask) continue; // drew what it asked for, goes again
      break;
    }
    return s;
  }

  function askForRank(rank) {
    if (finished || turn !== 'player') return;
    const matches = state.cpu.filter((c) => c.rank === rank);
    let next = state;
    if (matches.length > 0) {
      pushLog(`You asked for ${rank}s and got ${matches.length}!`);
      const newPlayerHand = [...state.player, ...matches];
      const newCpuHand = state.cpu.filter((c) => c.rank !== rank);
      const { books: newBooks, remaining } = extractBooks(newPlayerHand);
      next = { ...state, player: remaining, cpu: newCpuHand, playerBooks: [...state.playerBooks, ...newBooks] };
      setState(next);
      if (checkGameOver(next)) return;
      return; // player goes again
    }
    pushLog(`You asked for ${rank}s — Go Fish!`);
    if (state.pond.length > 0) {
      const [drawn, ...restPond] = state.pond;
      const newPlayerHand = [...state.player, drawn];
      const { books: newBooks, remaining } = extractBooks(newPlayerHand);
      next = { ...state, player: remaining, pond: restPond, playerBooks: [...state.playerBooks, ...newBooks] };
      setState(next);
      if (checkGameOver(next)) return;
      if (drawn.rank === rank) return; // player goes again
    }
    setTurn('cpu');
    const afterCpu = cpuTurn(next);
    setState(afterCpu);
    setTurn('player');
  }

  function restart() {
    setState(deal());
    setTurn('player');
    setLog(['Ask the computer for a rank you hold.']);
    setFinished(false);
  }

  const askableRanks = ranksInHand(state.player);

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🎣 Go Fish</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Ask the computer for a rank. Collect all four of a kind to win a book. Most books wins.</p>

      <div className="grid grid-cols-3 gap-3 text-center">
        <div className="rounded-xl bg-emerald-50 dark:bg-emerald-950 border border-emerald-200 dark:border-emerald-800 p-3">
          <p className="text-xs font-semibold text-emerald-700 dark:text-emerald-300">Your Books</p>
          <p className="text-2xl font-bold text-emerald-800 dark:text-emerald-200">{state.playerBooks.length}</p>
        </div>
        <div className="rounded-xl bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-3">
          <p className="text-xs font-semibold text-gray-500">Pond</p>
          <p className="text-2xl font-bold text-gray-700 dark:text-gray-200">{state.pond.length}</p>
        </div>
        <div className="rounded-xl bg-rose-50 dark:bg-rose-950 border border-rose-200 dark:border-rose-800 p-3">
          <p className="text-xs font-semibold text-rose-700 dark:text-rose-300">Computer Books</p>
          <p className="text-2xl font-bold text-rose-800 dark:text-rose-200">{state.cpuBooks.length}</p>
        </div>
      </div>

      <div>
        <p className="text-xs font-semibold text-gray-500 uppercase mb-2">Your Hand — tap a rank to ask for it</p>
        <div className="flex flex-wrap gap-2">
          {askableRanks.length === 0 && <p className="text-sm text-gray-400">Your hand is empty.</p>}
          {askableRanks.map((rank) => (
            <button
              key={rank}
              disabled={finished || turn !== 'player'}
              onClick={() => askForRank(rank)}
              className="rounded-lg border-2 border-indigo-300 dark:border-indigo-700 bg-white dark:bg-gray-800 px-3 py-2 text-sm font-bold text-indigo-700 dark:text-indigo-300 hover:bg-indigo-50 dark:hover:bg-indigo-900 disabled:opacity-40"
            >
              {rank} <span className="text-gray-400 font-normal">×{state.player.filter((c) => c.rank === rank).length}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="rounded-xl bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-3 space-y-1 max-h-32 overflow-y-auto">
        {log.map((line, i) => (
          <p key={i} className="text-xs text-gray-600 dark:text-gray-300">{line}</p>
        ))}
      </div>

      {finished && (
        <div className="text-center space-y-3">
          <p className="font-bold text-lg text-gray-800 dark:text-gray-100">
            {state.playerBooks.length > state.cpuBooks.length ? '🎉 You win!' : state.playerBooks.length < state.cpuBooks.length ? 'The computer wins this time.' : "It's a tie!"}
          </p>
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        </div>
      )}
    </div>
  );
}
