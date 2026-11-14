import React, { useState } from 'react';
import { shuffle, randInt } from '../utils/gameUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

const SIZE = 8;
// A slightly smaller-than-standard fleet to suit an 8x8 board.
const FLEET = [
  { name: 'Carrier', size: 5 },
  { name: 'Battleship', size: 4 },
  { name: 'Cruiser', size: 3 },
  { name: 'Submarine', size: 3 },
  { name: 'Destroyer', size: 2 },
];

function emptyGrid() {
  return Array.from({ length: SIZE }, () => Array(SIZE).fill(null));
}

function placeFleet() {
  const grid = emptyGrid();
  const ships = [];
  for (const { name, size } of FLEET) {
    let placed = false;
    let guard = 0;
    while (!placed && guard < 500) {
      guard++;
      const horizontal = Math.random() < 0.5;
      const r = randInt(0, SIZE - (horizontal ? 1 : size));
      const c = randInt(0, SIZE - (horizontal ? size : 1));
      const cells = [];
      for (let i = 0; i < size; i++) cells.push(horizontal ? [r, c + i] : [r + i, c]);
      if (cells.every(([rr, cc]) => !grid[rr][cc])) {
        for (const [rr, cc] of cells) grid[rr][cc] = name;
        ships.push({ name, cells, hits: 0, size });
        placed = true;
      }
    }
  }
  return { grid, ships };
}

function cellKey(r, c) {
  return `${r},${c}`;
}

export default function BattleshipGame({ onComplete, stats }) {
  const [cpuFleet, setCpuFleet] = useState(placeFleet);
  const [playerFleet, setPlayerFleet] = useState(placeFleet);
  const [playerShots, setPlayerShots] = useState({}); // key -> 'hit' | 'miss'
  const [cpuShots, setCpuShots] = useState({});
  const [cpuTargetQueue, setCpuTargetQueue] = useState([]);
  const [turn, setTurn] = useState('player');
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('Fire at the computer\'s grid to find its fleet.');

  function sunkCount(fleet, shots) {
    return fleet.ships.filter((ship) => ship.cells.every(([r, c]) => shots[cellKey(r, c)] === 'hit')).length;
  }

  function finish(playerWon) {
    setFinished(true);
    if (onComplete) {
      onComplete({
        score: playerWon ? 1 : 0,
        maxScore: 1,
        label: `Battleship — ${playerWon ? 'you sank the whole enemy fleet!' : 'the computer sank your fleet'}`,
      });
    }
  }

  function fireAtCpu(r, c) {
    if (finished || turn !== 'player' || playerShots[cellKey(r, c)]) return;
    const hitShip = cpuFleet.grid[r][c];
    const nextShots = { ...playerShots, [cellKey(r, c)]: hitShip ? 'hit' : 'miss' };
    setPlayerShots(nextShots);
    if (hitShip) {
      setMessage(`Hit! You struck the ${hitShip}.`);
      if (sunkCount(cpuFleet, nextShots) === FLEET.length) {
        finish(true);
        return;
      }
    } else {
      setMessage('Miss.');
    }
    setTurn('cpu');
    setTimeout(() => cpuFire(nextShots), 400);
  }

  function cpuFire() {
    setCpuShots((shots) => {
      let r, c;
      const key = (rr, cc) => `${rr},${cc}`;
      let queue = cpuTargetQueue.filter((t) => !shots[key(t[0], t[1])]);
      if (queue.length > 0) {
        [r, c] = queue[0];
        queue = queue.slice(1);
      } else {
        do {
          r = randInt(0, SIZE - 1);
          c = randInt(0, SIZE - 1);
        } while (shots[key(r, c)]);
      }
      const hitShip = playerFleet.grid[r][c];
      const nextShots = { ...shots, [key(r, c)]: hitShip ? 'hit' : 'miss' };
      let nextQueue = queue;
      if (hitShip) {
        setMessage(`The computer hit your ${hitShip}!`);
        const adjacent = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]].filter(
          ([rr, cc]) => rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE && !nextShots[key(rr, cc)]
        );
        nextQueue = [...queue, ...adjacent];
      } else {
        setMessage('The computer missed.');
      }
      setCpuTargetQueue(nextQueue);
      if (hitShip && sunkCount(playerFleet, nextShots) === FLEET.length) {
        setTimeout(() => finish(false), 0);
      } else {
        setTurn('player');
      }
      return nextShots;
    });
  }

  function restart() {
    setCpuFleet(placeFleet());
    setPlayerFleet(placeFleet());
    setPlayerShots({});
    setCpuShots({});
    setCpuTargetQueue([]);
    setTurn('player');
    setFinished(false);
    setMessage("Fire at the computer's grid to find its fleet.");
  }

  const playerSunk = sunkCount(cpuFleet, playerShots);
  const cpuSunk = sunkCount(playerFleet, cpuShots);

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🚢 Battleship</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Take turns firing. Sink all {FLEET.length} enemy ships before it sinks yours.</p>

      <div className="flex justify-center gap-6 text-sm font-semibold">
        <span>🎯 Enemy ships sunk: {playerSunk}/{FLEET.length}</span>
        <span>🛟 Your ships sunk: {cpuSunk}/{FLEET.length}</span>
      </div>

      <div className="grid sm:grid-cols-2 gap-6">
        <div>
          <p className="text-xs font-semibold text-gray-500 uppercase mb-2 text-center">Enemy Waters — click to fire</p>
          <div className="grid grid-cols-8 gap-0.5 bg-blue-800 p-1 rounded-lg mx-auto" style={{ width: 'min(80vw, 280px)' }}>
            {cpuFleet.grid.map((row, r) =>
              row.map((_, c) => {
                const shot = playerShots[cellKey(r, c)];
                return (
                  <button
                    key={`${r}-${c}`}
                    onClick={() => fireAtCpu(r, c)}
                    disabled={finished || turn !== 'player' || !!shot}
                    className={`aspect-square rounded-sm ${shot === 'hit' ? 'bg-red-500' : shot === 'miss' ? 'bg-blue-300' : 'bg-blue-500 hover:bg-blue-400'}`}
                  />
                );
              })
            )}
          </div>
        </div>
        <div>
          <p className="text-xs font-semibold text-gray-500 uppercase mb-2 text-center">Your Waters</p>
          <div className="grid grid-cols-8 gap-0.5 bg-gray-700 p-1 rounded-lg mx-auto" style={{ width: 'min(80vw, 280px)' }}>
            {playerFleet.grid.map((row, r) =>
              row.map((ship, c) => {
                const shot = cpuShots[cellKey(r, c)];
                return (
                  <div
                    key={`${r}-${c}`}
                    className={`aspect-square rounded-sm ${
                      shot === 'hit' ? 'bg-red-500' : shot === 'miss' ? 'bg-gray-400' : ship ? 'bg-gray-500' : 'bg-gray-600'
                    }`}
                  />
                );
              })
            )}
          </div>
        </div>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
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
