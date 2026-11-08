import assert from 'node:assert/strict';
import { test } from 'node:test';
import { activePhaseIndexes, conferenceDay, submissionNotice } from './timeline.ts';
import { conferenceMilestones as phases } from '../data/conference.ts';

test('switches submission and review phases on the requested calendar days', () => {
  for (const [day, expected] of [
    ['2026-11-09', []], ['2026-11-10', [0]], ['2026-11-11', [0]],
    ['2027-02-09', [0]], ['2027-02-10', [1]], ['2027-02-11', [2]],
    ['2027-03-09', [2]], ['2027-03-10', [3]], ['2027-03-11', []],
    ['2027-08-30', []],
  ]) assert.deepEqual(activePhaseIndexes(phases, day), expected, day);
});

test('keeps the satellite and main conference dates and ends the schedule', () => {
  assert.deepEqual(activePhaseIndexes(phases, '2027-08-31'), [4]);
  assert.deepEqual(activePhaseIndexes(phases, '2027-09-01'), [5]);
  assert.deepEqual(activePhaseIndexes(phases, '2027-09-03'), [5]);
  assert.deepEqual(activePhaseIndexes(phases, '2027-09-04'), []);
  assert.deepEqual(activePhaseIndexes([], '2027-02-10'), []);
});

test('supports overlapping event ranges', () => {
  const overlapping = [
    { start: '2027-08-31', end: '2027-08-31' },
    { start: '2027-08-31', end: '2027-09-03' },
  ];
  assert.deepEqual(activePhaseIndexes(overlapping, '2027-08-31'), [0, 1]);
  assert.deepEqual(activePhaseIndexes(overlapping, '2027-09-01'), [1]);
});

test('changes the conference day at midnight in India rather than midnight UTC', () => {
  assert.equal(conferenceDay(new Date('2026-11-09T18:29:59Z')), '2026-11-09');
  assert.equal(conferenceDay(new Date('2026-11-09T18:30:00Z')), '2026-11-10');
});

test('shows the correct submission notice before opening and through the closing day in India', () => {
  for (const [instant, status] of [
    ['2026-11-09T18:29:59Z', 'CFP Opening soon'],
    ['2026-11-09T18:30:00Z', 'Call for abstracts open'],
    ['2027-02-10T18:29:59Z', 'Call for abstracts open'],
    ['2027-02-10T18:30:00Z', 'Call for abstracts closed'],
  ]) assert.equal(submissionNotice(conferenceDay(new Date(instant))).status, status, instant);
  assert.match(submissionNotice('2026-11-08').message, /10 November 2026/);
  assert.match(submissionNotice('2026-11-10').message, /10 February 2027/);
});
