interface Phase {
  start: string;
  end?: string;
}

/** Compare calendar days in the conference's timezone, independent of the visitor's timezone. */
export function conferenceDay(now = new Date()): string {
  const parts = new Intl.DateTimeFormat('en', {
    timeZone: 'Asia/Kolkata', year: 'numeric', month: '2-digit', day: '2-digit',
  }).formatToParts(now);
  const part = (type: string) => parts.find((item) => item.type === type)!.value;
  return `${part('year')}-${part('month')}-${part('day')}`;
}

/** Ranges include their final day; undated gaps have no active phase. */
export function activePhaseIndexes(phases: Phase[], today: string): number[] {
  return phases.flatMap((phase, index) => {
    if (today < phase.start) return [];
    const nextStart = phases[index + 1]?.start;
    const active = phase.end
      ? today <= phase.end
      : nextStart && nextStart > phase.start
        ? today < nextStart
        : today === phase.start;
    return active ? [index] : [];
  });
}
