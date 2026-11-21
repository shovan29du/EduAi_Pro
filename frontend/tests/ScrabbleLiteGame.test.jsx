import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import ScrabbleLiteGame from '../src/components/ScrabbleLiteGame.jsx';

// Make the rack deterministic so we can spell a known real word.
vi.mock('../src/utils/gameUtils.js', () => ({ shuffle: (arr) => arr }));
vi.mock('../src/data/scrabbleWords.js', () => ({
  LETTER_VALUES: { C: 3, A: 1, T: 1, X: 8 },
  buildTileBag: () => ['C', 'A', 'T', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
  VALID_WORDS: new Set(['CAT']),
}));

function rackTileButton(letter) {
  return screen.getAllByRole('button').find((b) => b.textContent.startsWith(letter) && /^[A-Z]\d+$/.test(b.textContent));
}

describe('ScrabbleLiteGame', () => {
  it('deals a 7-tile rack and lets the player spell and score a real word', () => {
    render(<ScrabbleLiteGame />);
    expect(screen.getByText('🔤 Scrabble Lite')).toBeInTheDocument();
    expect(screen.getByText('Tiles left in bag: 3')).toBeInTheDocument();

    fireEvent.click(rackTileButton('C'));
    fireEvent.click(rackTileButton('A'));
    fireEvent.click(rackTileButton('T'));
    fireEvent.click(screen.getByRole('button', { name: 'Submit Word' }));

    expect(screen.getByText(/"CAT" scored 5 points/)).toBeInTheDocument();
    expect(screen.getByText('5', { selector: 'span.text-indigo-600' })).toBeInTheDocument();
    expect(screen.getByText('CAT +5')).toBeInTheDocument();
  });

  it('rejects a word that is not in the word list', () => {
    render(<ScrabbleLiteGame />);
    const xButtons = screen.getAllByRole('button').filter((b) => /^X\d+$/.test(b.textContent));
    fireEvent.click(xButtons[0]);
    fireEvent.click(xButtons[1]);
    fireEvent.click(screen.getByRole('button', { name: 'Submit Word' }));
    expect(screen.getByText(/isn't in this game's word list/)).toBeInTheDocument();
    expect(screen.getByText('0', { selector: 'span.text-indigo-600' })).toBeInTheDocument();
  });
});
