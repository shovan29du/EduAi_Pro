import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import { buildDeck, rankValue, cardLabel } from '../utils/cardUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

const MAX_ROUNDS = 200; // War can loop forever with unlucky splits; cap it.

function deal() {
  const deck = shuffle(buildDeck());
  return { player: deck.slice(0, 26), cpu: deck.slice(26) };
}

function CardFace({ card, hidden }) {
  if (!card) return <div className="w-16 h-24 rounded-lg border-2 border-dashed border-gray-300 dark:border-gray-600" />;
  return (
    <div
      className={`w-16 h-24 rounded-lg border-2 flex items-center justify-center text-2xl font-bold shadow-sm ${
        hidden
          ? 'bg-indigo-600 border-indigo-700 text-indigo-200'
          : `bg-white border-gray-300 ${card.red ? 'text-red-600' : 'text-gray-800'}`
      }`}
    >
      {hidden ? '🂠' : cardLabel(card)}
    </div>
  );
}

export default function WarCardGame({ onComplete, stats }) {
  const [piles, setPiles] = useState(deal);
  const [table, setTable] = useState({ player: null, cpu: null });
  const [warPile, setWarPile] = useState([]);
  const [message, setMessage] = useState('Flip a card to battle the computer.');
  const [rounds, setRounds] = useState(0);
  const [finished, setFinished] = useState(false);

  function finish(reason) {
    setFinished(true);
    const score = piles.player.length > piles.cpu.length ? 1 : 0;
    setMessage(reason);
    if (onComplete) {
      onComplete({
        score,
        maxScore: 1,
        label: `War — ${score ? 'won' : 'lost'} with ${piles.player.length} cards`,
      });
    }
  }

  function playRound(warStake = []) {
    if (finished) return;
    if (piles.player.length === 0) return finish('Out of cards — the computer wins!');
    if (piles.cpu.length === 0) return finish('The computer is out of cards — you win!');

    const playerCard = piles.player[0];
    const cpuCard = piles.cpu[0];
    const nextPlayer = piles.player.slice(1);
    const nextCpu = piles.cpu.slice(1);
    setTable({ player: playerCard, cpu: cpuCard });
    setRounds((r) => r + 1);

    const pv = rankValue(playerCard.rank);
    const cv = rankValue(cpuCard.rank);
    const pot = [...warStake, playerCard, cpuCard];

    if (rounds + 1 >= MAX_ROUNDS) {
      setPiles({ player: nextPlayer, cpu: nextCpu });
      return finish(`Round limit reached — most cards wins!`);
    }

    if (pv === cv) {
      // War: each side stakes up to 3 face-down cards, then battle continues
      // on the next click with everything on the table.
      const playerStake = nextPlayer.slice(0, 3);
      const cpuStake = nextCpu.slice(0, 3);
      const afterPlayer = nextPlayer.slice(playerStake.length);
      const afterCpu = nextCpu.slice(cpuStake.length);
      setWarPile([...pot, ...playerStake, ...cpuStake]);
      setPiles({ player: afterPlayer, cpu: afterCpu });
      setMessage(`⚔️ War! Both cards tied at ${playerCard.rank}. Flip again to battle it out.`);
      return;
    }

    const winnerIsPlayer = pv > cv;
    const wonPile = shuffle([...pot, ...warPile]);
    setWarPile([]);
    setPiles(
      winnerIsPlayer
        ? { player: [...nextPlayer, ...wonPile], cpu: nextCpu }
        : { player: nextPlayer, cpu: [...nextCpu, ...wonPile] }
    );
    setMessage(
      winnerIsPlayer
        ? `You win the round with ${playerCard.rank} over ${cpuCard.rank}!`
        : `The computer wins the round with ${cpuCard.rank} over ${playerCard.rank}.`
    );
  }

  function restart() {
    setPiles(deal());
    setTable({ player: null, cpu: null });
    setWarPile([]);
    setRounds(0);
    setFinished(false);
    setMessage('Flip a card to battle the computer.');
  }

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🃏 War</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Highest card wins both. Ties go to war — three cards down, one card up.</p>

      <div className="grid grid-cols-2 gap-6 items-center">
        <div className="text-center space-y-2">
          <p className="text-xs font-semibold text-gray-500 uppercase">You — {piles.player.length} cards</p>
          <div className="flex justify-center"><CardFace card={table.player} /></div>
        </div>
        <div className="text-center space-y-2">
          <p className="text-xs font-semibold text-gray-500 uppercase">Computer — {piles.cpu.length} cards</p>
          <div className="flex justify-center"><CardFace card={table.cpu} hidden={false} /></div>
        </div>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      <div className="flex justify-center gap-3">
        {!finished ? (
          <button onClick={() => playRound(warPile)} className="rounded-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-6 py-2.5">
            {warPile.length ? 'Battle! ⚔️' : 'Flip Cards'}
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
