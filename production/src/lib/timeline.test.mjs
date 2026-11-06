import assert from 'node:assert/strict';
import { test } from 'node:test';
import { activePhaseIndexes, conferenceDay } from './timeline.ts';

const phases = [
  { start: '2026-10-30' },
  { start: '2027-01-15' },
  { start: '2027-01-16', end: '2027-02-15' },
  { start: '2027-08-31' },
  { start: '2027-08-31', end: '2027-09-03' },
];

test('switches submission and review phases on the requested calendar days', () => {
  for (const [day, expected] of [
    ['2026-10-29', []], ['2026-10-30', [0]], ['2026-11-06', [0]],
    ['2027-01-14', [0]], ['2027-01-15', [1]], ['2027-01-16', [2]],
    ['2027-02-15', [2]], ['2027-02-16', []], ['2027-08-30', []],
  ]) assert.deepEqual(activePhaseIndexes(phases, day), expected, day);
});

test('handles overlapping conference dates and the end of the schedule', () => {
  assert.deepEqual(activePhaseIndexes(phases, '2027-08-31'), [3, 4]);
  assert.deepEqual(activePhaseIndexes(phases, '2027-09-01'), [4]);
  assert.deepEqual(activePhaseIndexes(phases, '2027-09-03'), [4]);
  assert.deepEqual(activePhaseIndexes(phases, '2027-09-04'), []);
  assert.deepEqual(activePhaseIndexes([], '2027-01-15'), []);
});

test('changes the conference day at midnight in India rather than midnight UTC', () => {
  assert.equal(conferenceDay(new Date('2027-01-14T18:29:59Z')), '2027-01-14');
  assert.equal(conferenceDay(new Date('2027-01-14T18:30:00Z')), '2027-01-15');
});
