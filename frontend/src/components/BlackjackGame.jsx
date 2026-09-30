import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import { buildDeck, cardLabel } from '../utils/cardUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

function cardValue(card) {
  if (card.rank === 'A') return 11;
  if (['K', 'Q', 'J'].includes(card.rank)) return 10;
  return parseInt(card.rank, 10);
}

function handTotal(hand) {
  let total = hand.reduce((sum, c) => sum + cardValue(c), 0);
  let aces = hand.filter((c) => c.rank === 'A').length;
  while (total > 21 && aces > 0) {
    total -= 10;
    aces -= 1;
  }
  return total;
}

function isBlackjack(hand) {
  return hand.length === 2 && handTotal(hand) === 21;
}

function freshShoe() {
  return shuffle([...buildDeck(), ...buildDeck()]); // 2-deck shoe, real casino-style
}

function deal() {
  const shoe = freshShoe();
  const player = [shoe[0], shoe[2]];
  const dealer = [shoe[1], shoe[3]];
  return { shoe: shoe.slice(4), player, dealer };
}

export default function BlackjackGame({ onComplete, stats }) {
  const [state, setState] = useState(deal);
  const [phase, setPhase] = useState('player'); // player -> dealer -> done
  const [message, setMessage] = useState('Hit to take a card, or stand to hold your total.');
  const [rounds, setRounds] = useState({ wins: 0, losses: 0, pushes: 0 });
  const [finished, setFinished] = useState(false);

  const playerTotal = handTotal(state.player);
  const dealerTotal = handTotal(state.dealer);

  function settleRound(outcome, extraShoe) {
    const nextRounds = {
      wins: rounds.wins + (outcome === 'win' ? 1 : 0),
      losses: rounds.losses + (outcome === 'loss' ? 1 : 0),
      pushes: rounds.pushes + (outcome === 'push' ? 1 : 0),
    };
    setRounds(nextRounds);
    setPhase('done');
    return nextRounds;
  }

  function finishSession(nextRounds) {
    setFinished(true);
    const played = nextRounds.wins + nextRounds.losses + nextRounds.pushes;
    if (onComplete) {
      onComplete({
        score: nextRounds.wins,
        maxScore: played,
        label: `Blackjack — ${nextRounds.wins}W ${nextRounds.losses}L ${nextRounds.pushes}P across ${played} hands`,
      });
    }
  }

  function hit() {
    if (finished || phase !== 'player') return;
    const shoe = state.shoe.length > 4 ? state.shoe : freshShoe();
    const card = shoe[0];
    const nextPlayer = [...state.player, card];
    const nextState = { ...state, player: nextPlayer, shoe: shoe.slice(1) };
    setState(nextState);
    const total = handTotal(nextPlayer);
    if (total > 21) {
      setMessage(`Bust with ${total}! Dealer wins the hand.`);
      const nextRounds = settleRound('loss');
      setMessage(`Bust with ${total}! Dealer wins the hand. (${nextRounds.wins}W ${nextRounds.losses}L ${nextRounds.pushes}P)`);
    }
  }

  function dealerPlay(fromState) {
    let shoe = fromState.shoe.length > 4 ? fromState.shoe : freshShoe();
    let dealerHand = fromState.dealer;
    while (handTotal(dealerHand) < 17) {
      dealerHand = [...dealerHand, shoe[0]];
      shoe = shoe.slice(1);
    }
    const finalState = { ...fromState, dealer: dealerHand, shoe };
    setState(finalState);
    const pTotal = handTotal(fromState.player);
    const dTotal = handTotal(dealerHand);
    let outcome, text;
    if (dTotal > 21) {
      outcome = 'win';
      text = `Dealer busts with ${dTotal} — you win!`;
    } else if (dTotal > pTotal) {
      outcome = 'loss';
      text = `Dealer wins ${dTotal} to your ${pTotal}.`;
    } else if (dTotal < pTotal) {
      outcome = 'win';
      text = `You win ${pTotal} to the dealer's ${dTotal}!`;
    } else {
      outcome = 'push';
      text = `Push — both have ${pTotal}.`;
    }
    const nextRounds = settleRound(outcome);
    setMessage(`${text} (${nextRounds.wins}W ${nextRounds.losses}L ${nextRounds.pushes}P)`);
  }

  function stand() {
    if (finished || phase !== 'player') return;
    setPhase('dealer');
    dealerPlay(state);
  }

  function nextHand() {
    setState(deal());
    setPhase('player');
    setMessage('Hit to take a card, or stand to hold your total.');
  }

  function endSession() {
    finishSession(rounds);
  }

  function restart() {
    setState(deal());
    setPhase('player');
    setRounds({ wins: 0, losses: 0, pushes: 0 });
    setFinished(false);
    setMessage('Hit to take a card, or stand to hold your total.');
  }

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🂡 Blackjack</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Get closer to 21 than the dealer without going over. Dealer draws to 17 and stands.</p>

      <div className="grid grid-cols-2 gap-4 text-center">
        <div>
          <p className="text-xs font-semibold text-gray-500 uppercase mb-1">Dealer {phase !== 'player' ? `(${dealerTotal})` : ''}</p>
          <div className="flex justify-center gap-1 flex-wrap">
            {state.dealer.map((c, i) => (
              <span key={i} className={`w-10 h-14 rounded border-2 flex items-center justify-center font-bold text-sm ${c.red ? 'text-red-600' : 'text-gray-800'} bg-white`}>
                {phase === 'player' && i === 1 ? '🂠' : cardLabel(c)}
              </span>
            ))}
          </div>
        </div>
        <div>
          <p className="text-xs font-semibold text-gray-500 uppercase mb-1">You ({playerTotal}{isBlackjack(state.player) ? ' — Blackjack!' : ''})</p>
          <div className="flex justify-center gap-1 flex-wrap">
            {state.player.map((c, i) => (
              <span key={i} className={`w-10 h-14 rounded border-2 flex items-center justify-center font-bold text-sm ${c.red ? 'text-red-600' : 'text-gray-800'} bg-white`}>
                {cardLabel(c)}
              </span>
            ))}
          </div>
        </div>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      <p className="text-center text-xs text-gray-400">Session: {rounds.wins}W · {rounds.losses}L · {rounds.pushes}P</p>

      <div className="flex justify-center gap-3 flex-wrap">
        {phase === 'player' && !finished && (
          <>
            <button onClick={hit} className="rounded-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-5 py-2">Hit</button>
            <button onClick={stand} className="rounded-full bg-amber-500 hover:bg-amber-600 text-white font-semibold px-5 py-2">Stand</button>
          </>
        )}
        {phase === 'done' && !finished && (
          <>
            <button onClick={nextHand} className="rounded-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-5 py-2">Next Hand</button>
            <button onClick={endSession} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-5 py-2">Finish &amp; Score</button>
          </>
        )}
        {finished && (
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">Play Again</button>
        )}
      </div>
    </div>
  );
}
