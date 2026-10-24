import { describe, it, expect } from 'vitest';
import { computeDailyStreak } from '../src/hooks/useGameCentreProgress.js';

function daysAgo(n) {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d.toISOString().slice(0, 10);
}

describe('computeDailyStreak', () => {
  it('returns 0 for no completed days', () => {
    expect(computeDailyStreak([])).toBe(0);
    expect(computeDailyStreak(undefined)).toBe(0);
  });

  it('counts consecutive days ending today', () => {
    const dates = [daysAgo(2), daysAgo(1), daysAgo(0)];
    expect(computeDailyStreak(dates)).toBe(3);
  });

  it('still counts a streak that ended yesterday (today not played yet)', () => {
    const dates = [daysAgo(2), daysAgo(1)];
    expect(computeDailyStreak(dates)).toBe(2);
  });

  it('resets when there is a gap', () => {
    const dates = [daysAgo(5), daysAgo(1), daysAgo(0)];
    expect(computeDailyStreak(dates)).toBe(2);
  });

  it('returns 0 once the streak is broken for more than a day', () => {
    const dates = [daysAgo(3), daysAgo(2)];
    expect(computeDailyStreak(dates)).toBe(0);
  });
});
