import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

function buildTiles() {
  const tiles = [];
  for (let a = 0; a <= 6; a++) {
    for (let b = a; b <= 6; b++) tiles.push({ id: `${a}-${b}`, a, b });
  }
  return tiles;
}

function pipTotal(hand) {
  return hand.reduce((sum, t) => sum + t.a + t.b, 0);
}

function fits(tile, end) {
  return tile.a === end || tile.b === end;
}

function deal() {
  const tiles = shuffle(buildTiles());
  const player = tiles.slice(0, 7);
  const cpu = tiles.slice(7, 14);
  const boneyard = tiles.slice(14);

  // Whoever holds the highest double opens; otherwise the highest-pip tile.
  const bestOpener = (hand) => {
    const doubles = hand.filter((t) => t.a === t.b).sort((x, y) => y.a - x.a);
    if (doubles.length) return doubles[0];
    return [...hand].sort((x, y) => y.a + y.b - (x.a + x.b))[0];
  };
  const playerBest = bestOpener(player);
  const cpuBest = bestOpener(cpu);
  const playerStarts = playerBest.a + playerBest.b >= cpuBest.a + cpuBest.b;

  return { player, cpu, boneyard, board: [], leftEnd: null, rightEnd: null, turn: playerStarts ? 'player' : 'cpu', passes: 0 };
}

export default function DominoGame({ onComplete, stats }) {
  const [state, setState] = useState(deal);
  const [selectedTile, setSelectedTile] = useState(null);
  const [message, setMessage] = useState('Match a number on either end of the line.');
  const [finished, setFinished] = useState(false);

  function finish(reason, playerWon) {
    setFinished(true);
    setMessage(reason);
    if (onComplete) {
      onComplete({
        score: playerWon ? 1 : 0,
        maxScore: 1,
        label: `Dominoes — ${playerWon ? 'won' : 'lost'} (you: ${pipTotal(state.player)} pips, computer: ${pipTotal(state.cpu)} pips)`,
      });
    }
  }

  function playTile(hand, tile, board, leftEnd, rightEnd, side) {
    const newHand = hand.filter((t) => t.id !== tile.id);
    let newBoard, newLeft, newRight;
    if (board.length === 0) {
      newBoard = [tile];
      newLeft = tile.a;
      newRight = tile.b;
    } else if (side === 'left') {
      const oriented = tile.b === leftEnd ? tile : { a: tile.b, b: tile.a };
      newBoard = [oriented, ...board];
      newLeft = oriented.a;
      newRight = rightEnd;
    } else {
      const oriented = tile.a === rightEnd ? tile : { a: tile.b, b: tile.a };
      newBoard = [...board, oriented];
      newLeft = leftEnd;
      newRight = oriented.b;
    }
    return { newHand, newBoard, newLeft, newRight };
  }

  function cpuStep(current) {
    let s = current;
    const end0 = s.leftEnd;
    const end1 = s.rightEnd;
    const playable = s.cpu.find((t) => s.board.length === 0 || fits(t, end0) || fits(t, end1));
    if (playable) {
      const side = s.board.length === 0 || fits(playable, end0) ? 'left' : 'right';
      const { newHand, newBoard, newLeft, newRight } = playTile(s.cpu, playable, s.board, end0, end1, side);
      s = { ...s, cpu: newHand, board: newBoard, leftEnd: newLeft, rightEnd: newRight, passes: 0, turn: 'player' };
      setMessage(`Computer played ${playable.a}|${playable.b}.`);
      return s;
    }
    if (s.boneyard.length > 0) {
      const [drawn, ...rest] = s.boneyard;
      s = { ...s, cpu: [...s.cpu, drawn], boneyard: rest };
      setMessage('Computer drew a tile.');
      return cpuStep(s);
    }
    setMessage('Computer has no move and passes.');
    return { ...s, passes: s.passes + 1, turn: 'player' };
  }

  function afterPlayerMove(s) {
    if (s.player.length === 0) {
      finish('🎉 You played your last tile — you win!', true);
      setState(s);
      return;
    }
    const afterCpu = cpuStep({ ...s, turn: 'cpu' });
    if (afterCpu.cpu.length === 0) {
      finish('The computer played its last tile — it wins.', false);
      setState(afterCpu);
      return;
    }
    if (afterCpu.passes >= 2) {
      const playerPips = pipTotal(afterCpu.player);
      const cpuPips = pipTotal(afterCpu.cpu);
      finish(
        playerPips <= cpuPips ? `Game blocked — you win with fewer pips (${playerPips} vs ${cpuPips}).` : `Game blocked — the computer wins with fewer pips (${cpuPips} vs ${playerPips}).`,
        playerPips <= cpuPips
      );
    }
    setState(afterCpu);
  }

  function playSelected(side) {
    if (finished || !selectedTile) return;
    const tile = state.player.find((t) => t.id === selectedTile);
    if (!tile) return;
    const canPlay = state.board.length === 0 || fits(tile, side === 'left' ? state.leftEnd : state.rightEnd);
    if (!canPlay) {
      setMessage('That tile does not match that end.');
      return;
    }
    const { newHand, newBoard, newLeft, newRight } = playTile(state.player, tile, state.board, state.leftEnd, state.rightEnd, side);
    setSelectedTile(null);
    afterPlayerMove({ ...state, player: newHand, board: newBoard, leftEnd: newLeft, rightEnd: newRight, passes: 0 });
  }

  function drawOrPass() {
    if (finished) return;
    if (state.boneyard.length > 0) {
      const [drawn, ...rest] = state.boneyard;
      setState((s) => ({ ...s, player: [...s.player, drawn], boneyard: rest }));
      setMessage('You drew a tile from the boneyard.');
      return;
    }
    afterPlayerMove({ ...state, passes: state.passes + 1 });
  }

  function restart() {
    setState(deal());
    setSelectedTile(null);
    setFinished(false);
    setMessage('Match a number on either end of the line.');
  }

  const canPlayAny = state.board.length === 0 || state.player.some((t) => fits(t, state.leftEnd) || fits(t, state.rightEnd));

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🁫 Dominoes</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Play a tile that matches either open end. Empty your hand first to win.</p>

      <div className="flex flex-wrap gap-1 justify-center rounded-xl bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-3 min-h-[60px]">
        {state.board.length === 0 && <p className="text-sm text-gray-400">No tiles played yet.</p>}
        {state.board.map((t, i) => (
          <span key={i} className="inline-flex items-center rounded border border-gray-400 bg-white px-2 py-1 text-sm font-bold text-gray-800">
            {t.a}|{t.b}
          </span>
        ))}
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-2 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      <div>
        <p className="text-xs font-semibold text-gray-500 uppercase mb-2">Your Hand ({state.player.length}) · Boneyard ({state.boneyard.length})</p>
        <div className="flex flex-wrap gap-2">
          {state.player.map((t) => (
            <button
              key={t.id}
              disabled={finished}
              onClick={() => setSelectedTile(selectedTile === t.id ? null : t.id)}
              className={`rounded-lg border-2 px-3 py-2 text-sm font-bold ${
                selectedTile === t.id ? 'border-amber-500 bg-amber-50 text-amber-800' : 'border-gray-300 bg-white text-gray-800 hover:border-indigo-300'
              }`}
            >
              {t.a}|{t.b}
            </button>
          ))}
        </div>
      </div>

      <div className="flex flex-wrap justify-center gap-3">
        <button disabled={finished || !selectedTile} onClick={() => playSelected('left')} className="rounded-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white font-semibold px-4 py-2 text-sm">
          Play on Left ({state.leftEnd ?? '—'})
        </button>
        <button disabled={finished || !selectedTile} onClick={() => playSelected('right')} className="rounded-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white font-semibold px-4 py-2 text-sm">
          Play on Right ({state.rightEnd ?? '—'})
        </button>
        {!canPlayAny && !finished && (
          <button onClick={drawOrPass} className="rounded-full bg-amber-500 hover:bg-amber-600 text-white font-semibold px-4 py-2 text-sm">
            {state.boneyard.length > 0 ? 'Draw Tile' : 'Pass'}
          </button>
        )}
        {finished && (
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-4 py-2 text-sm">
            Play Again
          </button>
        )}
      </div>
    </div>
  );
}
