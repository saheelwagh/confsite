# Timeline animation and phase behavior

This is the restoration reference for future redesigns. Preserve these behaviors unless deliberately changing them.

## Implementation

- Component, milestone content, browser initialization, and CSS: [Timeline.astro](../production/src/components/Timeline.astro).
- Date calculations: [timeline.ts](../production/src/lib/timeline.ts).
- Date-boundary tests: [timeline.test.mjs](../production/src/lib/timeline.test.mjs).

## Visual behavior

The active phase has **only a small blue pointer** to its left. Do not recolor its heading or highlight the entire row.

| Detail | Value |
| --- | --- |
| Pointer | CSS triangle, 6px wide × 8px high, `#0f33c2` |
| Position | 20px outside the row's left edge, vertically centered |
| Animation | `phase-pointer`, 2.2 seconds, `ease-in-out`, two cycles (4.4 seconds total) |
| Movement | 0 → 4px right → 0 |
| Opacity | 1 → 0.5 → 1 |
| Final state | Pointer stays visible and still |

The next future phase receives a small uppercase **Upcoming** label beside its heading. Only that phase's **date** gets a delayed highlight:

- `upcoming-date`: 1.8 seconds, `ease`, **5-second delay** from viewport entry, `forwards` fill.
- The delay lets the pointer's two cycles finish first.
- Date text changes from `#566984` to `#0f33c2`.
- Background fades from transparent to blue at 6% opacity, with a matching 6px spread shadow and 2px corners.
- The final date highlight remains; it does not pulse continuously or change the row's geometry.

## Viewport trigger and accessibility

- An `IntersectionObserver` watches `.milestones` with threshold `0.1`.
- On first intersection, add `.is-revealed` to `.timeline`, then disconnect the observer. Scrolling away and back must not restart the entry animation.
- `.is-active` and `.is-upcoming` come from the date calculation. The Upcoming label can appear before viewport entry; the visual effects wait for `.is-revealed`.
- Active rows use `aria-current="step"`. Decorative row numbers and pointers must not add screen-reader announcements.
- With `prefers-reduced-motion: reduce`, the pointer stays still and the upcoming date receives its final highlight immediately on reveal, with no animation or delay.
- If IntersectionObserver is unavailable, reveal immediately. Without JavaScript, the static timeline remains readable, without dynamic phase labels or effects.

## Calendar rules

Use **Asia/Kolkata** calendar days, independent of the visitor's timezone. Calculate in the browser, not only during Astro's static build. Refresh at the next midnight in India and when a background tab becomes visible again.

| Phase | Active dates, inclusive |
| --- | --- |
| Submissions open | 30 October 2026–14 January 2027 |
| Submissions close | 15 January 2027 |
| Review Completed | 16 January–15 February 2027 |
| Satellite Conference | 31 August 2027 |
| Main Conference | 31 August–3 September 2027 |

**Intentional display distinction:** the third phase reads “Review Completed — 15 February 2027,” but retains its original active window of 16 January–15 February, as requested when only its wording was changed. Do not silently change its active dates to match the single displayed completion date.

- Explicit `end` dates are inclusive. Without an end, a phase runs until the next row's later start date, exclusive; if there is no later start, it is active only on its own start day.
- Milestones must remain in chronological order.
- Both conference rows are active on 31 August because their dates overlap.
- No phase is active in gaps after an explicit end, before the schedule, or after all events end.
- Upcoming means the first future row after the last active row. During a gap, use the first future row. After the final event, there is no upcoming phase.
- Show full month names in visible dates. Keep machine-readable `datetime` attributes in ISO format.

## Verification after rework

1. Run `node --experimental-strip-types --test src/lib/timeline.test.mjs` from the production folder, then `pnpm build`.
2. Check current and upcoming labels around 14/15/16 January and 15/16 February, including India's midnight boundary.
3. Load above the timeline, then scroll into it: pointer begins first, upcoming date highlight starts at 5 seconds, and both settle.
4. Scroll away and back: no replay. Check reduced motion: no animated movement or delayed highlight.
5. Check overlapping events, empty date gaps, no upcoming event, and a tab left open over midnight.
6. Use a visible browser tab for the viewport check; hidden tabs can defer IntersectionObserver callbacks.
