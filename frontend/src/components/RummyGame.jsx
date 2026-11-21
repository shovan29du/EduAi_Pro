import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import { buildDeck, RANKS, cardLabel } from '../utils/cardUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

// A real Gin Rummy: 10-card hands, draw from stock or the discard pile, then
// discard. Meld cards into sets (same rank, 3-4 cards) or runs (3+ same-suit
// consecutive ranks) to lower your deadwood. Knock once your deadwood is 10
// or under, or go Gin with zero deadwood for a bonus.

function rankIndex(rank) {
  return RANKS.indexOf(rank) + 1; // A=1 ... K=13
}

function cardPoints(rank) {
  if (rank === 'A') return 1;
  if (['J', 'Q', 'K'].includes(rank)) return 10;
  return parseInt(rank, 10);
}

function deal() {
  const deck = shuffle(buildDeck());
  const player = deck.slice(0, 10);
  const cpu = deck.slice(10, 20);
  const discard = [deck[20]];
  const stock = deck.slice(21);
  return { stock, discard, player, cpu, phase: 'player-draw' };
}

// Finds the best (highest-value) set of non-overlapping melds in a hand via
// a small greedy-then-best search — hands are only 10-11 cards so this is cheap.
function bestMelds(hand) {
  const bySuit = {};
  const byRank = {};
  hand.forEach((c, i) => {
    (bySuit[c.suit] = bySuit[c.suit] || []).push({ ...c, i });
    (byRank[c.rank] = byRank[c.rank] || []).push({ ...c, i });
  });

  const candidateMelds = [];
  for (const rank in byRank) {
    if (byRank[rank].length >= 3) candidateMelds.push(byRank[rank].map((c) => c.i));
  }
  for (const suit in bySuit) {
    const sorted = bySuit[suit].slice().sort((a, b) => rankIndex(a.rank) - rankIndex(b.rank));
    let run = [sorted[0]];
    for (let k = 1; k <= sorted.length; k++) {
      const cur = sorted[k];
      const prev = sorted[k - 1];
      if (cur && rankIndex(cur.rank) === rankIndex(prev.rank) + 1) {
        run.push(cur);
      } else {
        if (run.length >= 3) candidateMelds.push(run.map((c) => c.i));
        run = cur ? [cur] : [];
      }
    }
  }

  // Greedily pick the largest, non-overlapping melds first.
  candidateMelds.sort((a, b) => b.length - a.length);
  const used = new Set();
  const chosen = [];
  for (const meld of candidateMelds) {
    if (meld.some((i) => used.has(i))) continue;
    meld.forEach((i) => used.add(i));
    chosen.push(meld);
  }
  return chosen;
}

function deadwood(hand) {
  const melds = bestMelds(hand);
  const meldedIndices = new Set(melds.flat());
  const unmelded = hand.filter((_, i) => !meldedIndices.has(i));
  return { melds, deadwoodValue: unmelded.reduce((sum, c) => sum + cardPoints(c.rank), 0), unmelded };
}

export default function RummyGame({ onComplete, stats }) {
  const [state, setState] = useState(deal);
  const [selected, setSelected] = useState(null);
  const [message, setMessage] = useState('Draw from the stock or the discard pile.');
  const [finished, setFinished] = useState(false);

  const { melds: playerMelds, deadwoodValue: playerDeadwood } = deadwood(state.player);

  function finish(text, playerWon, marginScore) {
    setFinished(true);
    setMessage(text);
    if (onComplete) onComplete({ score: playerWon ? 1 : 0, maxScore: 1, label: `Rummy — ${text}` });
  }

  function refillStockIfNeeded(s) {
    if (s.stock.length > 0) return s;
    const top = s.discard[s.discard.length - 1];
    const rest = s.discard.slice(0, -1);
    return { ...s, stock: shuffle(rest), discard: [top] };
  }

  function drawFromStock() {
    if (finished || state.phase !== 'player-draw') return;
    const s = refillStockIfNeeded(state);
    if (s.stock.length === 0) {
      finish("Stock ran out — it's a draw.", false);
      return;
    }
    const [card, ...rest] = s.stock;
    setState({ ...s, stock: rest, player: [...s.player, card], phase: 'player-discard' });
    setMessage('Discard a card to end your turn.');
  }

  function drawFromDiscard() {
    if (finished || state.phase !== 'player-draw' || state.discard.length === 0) return;
    const card = state.discard[state.discard.length - 1];
    setState({ ...state, discard: state.discard.slice(0, -1), player: [...state.player, card], phase: 'player-discard' });
    setMessage('Discard a card to end your turn.');
  }

  function discardCard(card) {
    if (finished || state.phase !== 'player-discard') return;
    const remaining = state.player.filter((c) => c.id !== card.id);
    const { deadwoodValue } = deadwood(remaining);
    const next = { ...state, player: remaining, discard: [...state.discard, card], phase: 'cpu' };
    setState(next);
    setSelected(null);
    if (deadwoodValue <= 10) {
      const { deadwoodValue: cpuDeadwood } = deadwood(state.cpu);
      const gin = deadwoodValue === 0;
      const won = deadwoodValue < cpuDeadwood || gin;
      finish(
        gin
          ? `Gin! Your deadwood 0 vs computer's ${cpuDeadwood}.`
          : won
          ? `You knock with ${deadwoodValue} vs computer's ${cpuDeadwood} — you win!`
          : `You knock with ${deadwoodValue}, but the computer had ${cpuDeadwood} — undercut, computer wins.`,
        won
      );
      return;
    }
    setMessage("Computer's turn…");
    setTimeout(() => runCpuTurn(next), 500);
  }

  function runCpuTurn(current) {
    let s = refillStockIfNeeded(current);
    if (s.stock.length === 0) {
      finish("Stock ran out — it's a draw.", false);
      return;
    }
    const topDiscard = s.discard[s.discard.length - 1];
    const { deadwoodValue: withoutDraw } = deadwood(s.cpu);
    const handWithDiscard = [...s.cpu, topDiscard];
    const { deadwoodValue: withDiscardDraw } = deadwood(handWithDiscard);
    let hand;
    if (topDiscard && withDiscardDraw < withoutDraw) {
      hand = handWithDiscard;
      s = { ...s, discard: s.discard.slice(0, -1) };
    } else {
      const [card, ...rest] = s.stock;
      hand = [...s.cpu, card];
      s = { ...s, stock: rest };
    }
    // Discard the highest-value card not part of any meld.
    const { melds, unmelded } = deadwood(hand);
    const meldedIndices = new Set(melds.flat());
    const worst = hand
      .map((c, i) => ({ c, i }))
      .filter(({ i }) => !meldedIndices.has(i))
      .sort((a, b) => cardPoints(b.c.rank) - cardPoints(a.c.rank))[0] || { c: hand[hand.length - 1] };
    const finalHand = hand.filter((c) => c.id !== worst.c.id);
    const next = { ...s, cpu: finalHand, discard: [...s.discard, worst.c], phase: 'player-draw' };
    setState(next);
    const { deadwoodValue: cpuFinalDeadwood } = deadwood(finalHand);
    if (cpuFinalDeadwood <= 10) {
      const { deadwoodValue: playerFinalDeadwood } = deadwood(next.player);
      const gin = cpuFinalDeadwood === 0;
      const playerWon = playerFinalDeadwood < cpuFinalDeadwood && !gin;
      finish(
        gin
          ? `Computer went Gin with 0 deadwood vs your ${playerFinalDeadwood}.`
          : playerWon
          ? `Computer knocks with ${cpuFinalDeadwood}, but you had ${playerFinalDeadwood} — undercut, you win!`
          : `Computer knocks with ${cpuFinalDeadwood} vs your ${playerFinalDeadwood} — computer wins.`,
        playerWon
      );
      return;
    }
    setMessage('Your turn — draw from the stock or the discard pile.');
  }

  function restart() {
    setState(deal());
    setSelected(null);
    setFinished(false);
    setMessage('Draw from the stock or the discard pile.');
  }

  const meldedIndices = new Set(playerMelds.flat());
  const topDiscard = state.discard[state.discard.length - 1];

  return (
    <div className="max-w-3xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🃏 Rummy</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Gin Rummy: meld sets and runs to cut your deadwood. Knock at 10 or under, or go Gin at 0 for the best result.</p>

      <div className="flex items-center justify-center gap-6">
        <div className="text-center">
          <button
            onClick={drawFromStock}
            disabled={finished || state.phase !== 'player-draw'}
            className="w-14 h-20 rounded-lg border-2 border-indigo-600 bg-indigo-600 disabled:opacity-40 flex items-center justify-center text-white font-bold"
          >
            🂠
          </button>
          <p className="text-[10px] text-gray-400 mt-1">Stock ({state.stock.length})</p>
        </div>
        <div className="text-center">
          <button
            onClick={drawFromDiscard}
            disabled={finished || state.phase !== 'player-draw' || !topDiscard}
            className={`w-14 h-20 rounded-lg border-2 bg-white flex items-center justify-center font-bold disabled:opacity-40 ${topDiscard?.red ? 'text-red-600' : 'text-gray-800'}`}
          >
            {topDiscard ? cardLabel(topDiscard) : '—'}
          </button>
          <p className="text-[10px] text-gray-400 mt-1">Discard</p>
        </div>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      <div>
        <p className="text-xs font-semibold text-gray-500 uppercase mb-2">Your Hand — deadwood: {playerDeadwood}</p>
        <div className="flex flex-wrap gap-2 justify-center">
          {state.player.map((card, i) => (
            <button
              key={card.id}
              disabled={finished || state.phase !== 'player-discard'}
              onClick={() => discardCard(card)}
              className={`w-12 h-16 rounded-lg border-2 bg-white flex items-center justify-center font-bold disabled:cursor-not-allowed ${
                card.red ? 'text-red-600' : 'text-gray-800'
              } ${meldedIndices.has(i) ? 'border-emerald-500 ring-2 ring-emerald-300' : 'border-gray-300'}`}
              title={state.phase === 'player-discard' ? 'Click to discard' : ''}
            >
              {cardLabel(card)}
            </button>
          ))}
        </div>
        <p className="text-[10px] text-gray-400 text-center mt-1">Green-ringed cards are already melded. {state.phase === 'player-discard' ? 'Click a card to discard it.' : ''}</p>
      </div>

      {finished && (
        <div className="flex justify-center">
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        </div>
      )}
    </div>
  );
}
