import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import { buildUnoDeck, cardLabel, canPlay, COLORS, COLOR_CLASSES } from '../data/unoDeck.js';
import GameScoreBadge from './GameScoreBadge.jsx';

// 2-player Uno: with only one opponent, Reverse behaves the same as Skip
// (it hands the turn straight back to the player who played it).

function deal() {
  let deck = shuffle(buildUnoDeck());
  const player = deck.slice(0, 7);
  const cpu = deck.slice(7, 14);
  let rest = deck.slice(14);
  let topIndex = rest.findIndex((c) => c.kind === 'number');
  const top = rest[topIndex];
  rest = [...rest.slice(0, topIndex), ...rest.slice(topIndex + 1)];
  return { deck: rest, discard: [top], player, cpu, activeColor: top.color, turn: 'player' };
}

function ensureDeck(state, needed) {
  if (state.deck.length >= needed) return state;
  const top = state.discard[state.discard.length - 1];
  const rest = state.discard.slice(0, -1);
  return { ...state, deck: shuffle([...state.deck, ...rest]), discard: [top] };
}

function drawN(state, n) {
  const s = ensureDeck(state, n);
  const cards = s.deck.slice(0, n);
  return { cards, deck: s.deck.slice(n), discard: s.discard };
}

function bestColorFor(hand) {
  const counts = { red: 0, yellow: 0, green: 0, blue: 0 };
  for (const c of hand) if (counts[c.color] != null) counts[c.color] += 1;
  return COLORS.reduce((best, c) => (counts[c] > counts[best] ? c : best), COLORS[0]);
}

export default function UnoGame({ onComplete, stats }) {
  const [state, setState] = useState(deal);
  const [message, setMessage] = useState('Match the colour, number, or symbol on top. Play a card or draw one.');
  const [finished, setFinished] = useState(false);

  const topCard = state.discard[state.discard.length - 1];

  function finish(playerWon) {
    setFinished(true);
    if (onComplete) {
      onComplete({
        score: playerWon ? 1 : 0,
        maxScore: 1,
        label: `Uno — ${playerWon ? 'you won!' : 'the computer won'}`,
      });
    }
  }

  function runCpuTurn(startState) {
    let s = startState;
    let guard = 0;
    while (guard < 10) {
      guard++;
      const top = s.discard[s.discard.length - 1];
      const playable = s.cpu.filter((c) => canPlay(c, top, s.activeColor));
      if (playable.length === 0) {
        const { cards, deck, discard } = drawN(s, 1);
        s = { ...s, deck, discard, cpu: [...s.cpu, ...cards] };
        if (cards.length && canPlay(cards[0], s.discard[s.discard.length - 1], s.activeColor)) {
          continue; // drew a playable card — play it on the next loop pass
        }
        setMessage('Computer drew a card and passed.');
        s = { ...s, turn: 'player' };
        break;
      }
      const nonWild = playable.filter((c) => c.color !== 'wild');
      const card = (nonWild.length ? nonWild : playable)[0];
      const restHand = s.cpu.filter((c) => c.id !== card.id);
      const nextColor = card.color === 'wild' ? bestColorFor(restHand) : card.color;
      let s2 = { ...s, cpu: restHand, discard: [...s.discard, card], activeColor: nextColor };

      if (restHand.length === 0) {
        setState(s2);
        finish(false);
        return;
      }
      if (card.kind === 'drawTwo' || card.kind === 'wildDrawFour') {
        const n = card.kind === 'drawTwo' ? 2 : 4;
        const { cards, deck, discard } = drawN(s2, n);
        s2 = { ...s2, deck, discard, player: [...s2.player, ...cards] };
        setMessage(`Computer played ${cardLabel(card)} — you draw ${n} and lose your turn.`);
        s = s2;
        continue; // cpu goes again
      }
      if (card.kind === 'skip' || card.kind === 'reverse') {
        setMessage(`Computer played ${card.kind === 'skip' ? 'Skip' : 'Reverse'} — you lose your turn.`);
        s = s2;
        continue; // cpu goes again
      }
      if (card.kind === 'wild') setMessage(`Computer played Wild and chose ${nextColor}.`);
      else setMessage(`Computer played ${cardLabel(card)}.`);
      s = { ...s2, turn: 'player' };
      break;
    }
    setState(s);
  }

  function playCard(card, chosenColor) {
    if (finished || state.turn !== 'player') return;
    if (!canPlay(card, topCard, state.activeColor)) return;
    if (card.color === 'wild' && !chosenColor) {
      const pick = (window.prompt('Choose a colour: red, yellow, green, or blue', 'red') || '').trim().toLowerCase();
      if (!COLORS.includes(pick)) return;
      playCard(card, pick);
      return;
    }
    const restHand = state.player.filter((c) => c.id !== card.id);
    const nextColor = card.color === 'wild' ? chosenColor : card.color;
    let next = { ...state, player: restHand, discard: [...state.discard, card], activeColor: nextColor };

    if (restHand.length === 0) {
      setState(next);
      finish(true);
      return;
    }
    if (card.kind === 'drawTwo' || card.kind === 'wildDrawFour') {
      const n = card.kind === 'drawTwo' ? 2 : 4;
      const { cards, deck, discard } = drawN(next, n);
      next = { ...next, deck, discard, cpu: [...next.cpu, ...cards] };
      setMessage(`You played ${cardLabel(card)} — computer draws ${n} and loses its turn.`);
      setState(next);
      setTimeout(() => runCpuTurn(next), 500);
      return;
    }
    if (card.kind === 'skip' || card.kind === 'reverse') {
      setMessage(`You played ${card.kind === 'skip' ? 'Skip' : 'Reverse'} — computer loses its turn.`);
      setState(next);
      setTimeout(() => runCpuTurn(next), 500);
      return;
    }
    setMessage(card.color === 'wild' ? `You played Wild and chose ${nextColor}.` : "Computer's turn…");
    next = { ...next, turn: 'cpu' };
    setState(next);
    setTimeout(() => runCpuTurn(next), 500);
  }

  function drawCard() {
    if (finished || state.turn !== 'player') return;
    const { cards, deck, discard } = drawN(state, 1);
    const next = { ...state, deck, discard, player: [...state.player, ...cards] };
    setState(next);
    if (cards.length && canPlay(cards[0], next.discard[next.discard.length - 1], next.activeColor)) {
      setMessage('You drew a playable card — play it or pass.');
    } else {
      setMessage("You can't play — turn passes to the computer.");
      const afterTurn = { ...next, turn: 'cpu' };
      setState(afterTurn);
      setTimeout(() => runCpuTurn(afterTurn), 500);
    }
  }

  function passTurn() {
    if (finished || state.turn !== 'player') return;
    const next = { ...state, turn: 'cpu' };
    setState(next);
    setMessage("Computer's turn…");
    setTimeout(() => runCpuTurn(next), 500);
  }

  function restart() {
    setState(deal());
    setFinished(false);
    setMessage('Match the colour, number, or symbol on top. Play a card or draw one.');
  }

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🌈 Uno</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Match the top card's colour, number, or symbol. First to empty their hand wins.</p>

      <div className="flex items-center justify-center gap-4">
        <div className={`w-16 h-24 rounded-lg border-2 flex items-center justify-center text-2xl font-bold ${COLOR_CLASSES[topCard.color]}`}>
          {cardLabel(topCard)}
        </div>
        <span className={`w-6 h-6 rounded-full ${COLOR_CLASSES[state.activeColor]}`} title="Active colour" />
      </div>

      <p className="text-center text-xs text-gray-400">Computer has {state.cpu.length} card{state.cpu.length === 1 ? '' : 's'} · Draw pile: {state.deck.length}</p>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      <div>
        <p className="text-xs font-semibold text-gray-500 uppercase mb-2">Your Hand</p>
        <div className="flex flex-wrap gap-2 justify-center">
          {state.player.map((card) => {
            const playable = !finished && state.turn === 'player' && canPlay(card, topCard, state.activeColor);
            return (
              <button
                key={card.id}
                disabled={!playable}
                onClick={() => playCard(card)}
                className={`w-12 h-16 rounded-lg border-2 flex items-center justify-center font-bold ${COLOR_CLASSES[card.color]} ${
                  playable ? 'hover:-translate-y-1 transition-transform' : 'opacity-40'
                }`}
              >
                {cardLabel(card)}
              </button>
            );
          })}
        </div>
      </div>

      <div className="flex justify-center gap-3">
        {!finished && state.turn === 'player' && (
          <>
            <button onClick={drawCard} className="rounded-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 text-sm">
              Draw Card
            </button>
            <button onClick={passTurn} className="rounded-full bg-gray-400 hover:bg-gray-500 text-white font-semibold px-4 py-2 text-sm">
              Pass
            </button>
          </>
        )}
        {finished && (
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        )}
      </div>
    </div>
  );
}
