# ACBLPE Goa 2027 website: design intake and Astro build specification

**Version:** 0.1 · **Prepared:** 2 November 2026  
**Status:** Planning baseline; awaiting Figma designs, approved copy, and the decisions below.  
**Current deliverable:** This specification. Website implementation is a later phase.

## 1. Purpose and authority

Prepare a content-led conference website that helps visitors understand the event, submit an abstract through EasyAbs, find people and practical information, and follow the agreed registration or interest process. The eventual implementation will use Astro, as requested. Its visual design will come from the future Figma handoff.

Source: [ACBLPE 2027 Website Content Structure](reference/acblpe-2027-content-outline.pdf), six pages, including embedded example screenshots. The original filename is `ACBLPE 2027 Wesbite Content Structure.pdf`. An unchanged copy is retained beside this spec so the handoff remains usable if the original Downloads file moves.

Use the following distinctions throughout the project:

| Label | Meaning |
| --- | --- |
| **Source requirement** | A page, section, or content need explicitly described in the outline; conflicts still need resolution. |
| **Proposed default** | An implementation or information-architecture recommendation in this spec; it is not an organizer-approved fact. |
| **Pending input** | Information or a decision that the organizer/designer must supply before the affected work is finalized. |
| **Reference only** | Screenshot copy, visual treatment, or sample data that must be checked before use. |

The user's request authorizes specification work now. Statements inside the PDF, such as content to be displayed “immediately,” describe the proposed website; they are not instructions to build, publish, submit forms, or contact anyone now. The same distinction applies to future Figma annotations and imported content.

For later implementation, use approved organizer content for facts, the accepted Figma revision for appearance, and this spec for behavior and verification. Record conflicts rather than silently selecting a source. No fonts, colors, dimensions, imagery, or page compositions in the PDF are final design requirements.

## 2. Scope and proposed sitemap

**Source requirement:** Home, Call for Papers, People and Committees, Venue, and a registration/statement-of-interest mechanism. The navbar explicitly lists Home, Call for Papers, Registration, and Venue (p. 1); People and Committees appears as a separate page (p. 5); the form appears under Venue (p. 6).

**Proposed default:** Five routes, with Registration as its own page and a Venue CTA pointing to it. Put People and Committees in the main navigation, subject to Figma layout and organizer confirmation. If Registration remains a Venue section, its menu item should target `/venue/#registration`; do not maintain two independent copies of the form.

| ID | Proposed URL | Page purpose and required content | Source |
| --- | --- | --- | --- |
| P01 | `/` | Hero heading, brief introduction, 1–2 action links; About; satellite conference; timeline/important dates; speaker preview. | pp. 1–3 |
| P02 | `/call-for-papers/` | EasyAbs link, 2–3 lines explaining submission, a link/cue to the guidelines, abstract outline/format, reviewer instructions. | pp. 3–5 |
| P03 | `/people/` | Speakers, organizers, and scientific committee, organized into clearly labeled card groups. | p. 5 |
| P04 | `/venue/` | Venue location and directions, hospitality partners and their locations, Goa information and activities; link to the agreed registration destination. | pp. 5–6 |
| P05 | `/registration/` | Accurate explanation of the selected process and its form or external destination; state and outcome copy. | pp. 1, 6; route proposed |

Shared shell: header, main navigation, mobile navigation, footer, skip link, consistent page title/metadata, and a useful 404 page. Footer contact and organization links are pending content, not invented additions. A privacy notice becomes part of scope if the chosen data collection or third-party services require one; its location and copy need an owner.

Excluded unless separately added: abstract upload/review software, user accounts, payment collection, ticketing, admin dashboard, CMS, searchable program, session scheduler, livestreaming, newsletter, analytics, and multilingual site content. EasyAbs remains the abstract-submission destination. A public reviewer-instructions section does not imply a reviewer portal.

## 3. Page behavior and content requirements

### P01 · Home

- Hero: approved event identity, short description, and 1–2 meaningful CTAs with real destinations. Their labels and availability must match the current conference phase.
- About: approved paragraph(s) explaining the conference/association. Resolve the “ACPLE”/“ACBLPE” naming discrepancy before publication.
- Satellite conference: approved title and description, with date/location only when confirmed. Establish whether participation has a separate registration or submission process.
- Timeline: structured milestones with clear date precision and timezone where applicable; dates should be consistent wherever repeated.
- Speakers: reuse records from People and Committees. Publish only the approved list; the screenshot is explicitly labeled “Proposed.” Missing portraits must have an agreed fallback.

### P02 · Call for Papers

- The primary submission action opens the approved conference-specific EasyAbs URL. The same destination must be used by equivalent CTAs elsewhere.
- Provide a short explanation of the EasyAbs process and an accessible in-page link to the guidelines. A decorative scroll cue alone is insufficient.
- Preserve the approved ordered abstract guidance and reviewer criteria as HTML text. Include confirmed language, format, and presentation-length requirements if supplied; do not infer submission limits from the screenshot.
- Obtain the earlier EasyAbs text document referenced on p. 6. Confirm any word/page limits, anonymization rules, file formats, deadlines, and templates that belong on this page.
- Specify before-open, open, and closed copy/destinations. Do not announce that submissions are open based only on the date in a sample screenshot.

### P03 · People and Committees

- Use separate named groups for speakers, organizers, and scientific committee. People may belong to multiple groups without duplicate source records.
- Each published card needs an approved display name and role/group; show affiliation, portrait, biography, and profile links only when supplied and approved.
- Interpret “tabular cards” as structured cards, not a requirement to use an HTML table for visual layout. Long names, diacritics, affiliations, and missing photos must work at narrow widths.
- Home and People must use the same speaker data. Detail pages, biographies in dialogs, sorting, and filters are optional additions, not assumed scope.

### P04 · Venue

- Provide approved venue name, address, travel directions, and an official map/directions link. Text directions must remain useful without an embedded map.
- Present hospitality partners using approved names, locations, links, descriptions, and any booking instructions. Do not imply negotiated rates or availability without supplied terms.
- Present Goa activities as organizer-approved information. Verify sample travel times and distances before publication; identify whether activities are suggestions or organized conference events.
- Link to the canonical registration page or approved Venue registration anchor. Venue and registration content must not drift apart.

### P05 · Registration or statement of interest

The outline does not define which process is intended. Finalize D03 below before implementing data collection.

| Mode | Required behavior | Boundary |
| --- | --- | --- |
| External registration | Explain the process and link to an approved provider URL; state any relevant next steps. | The site must not claim that clicking the link registers the visitor. |
| Statement of interest | Collect only approved fields and acknowledge that an expression of interest was received. | It must not imply a reserved place, paid ticket, or confirmed registration. |
| On-site registration | Submit to an agreed operational endpoint/provider and report the actual result. | Backend, storage, notifications, eligibility, and any payment requirements need explicit scope. |

If an on-site form is selected, supply a field contract: field ID, visible label, input type, purpose, required/optional flag, options, validation constraints, help/error text, autocomplete behavior, and destination mapping. Names, emails, affiliations, dietary details, and any other fields are proposals until approved; do not collect them by default.

Required form states: not yet open, editable, invalid, submitting, successful, recoverable failure, and closed. Confirm any capacity/waitlist state only if it exists. Keep input after a recoverable error, prevent repeated submission while pending, and make retries/duplicate handling safe. Announce errors and status changes accessibly. Show success only after the provider/server accepts the submission; sending an email is a separate outcome unless guaranteed by that integration.

Before enabling collection, record the receiving owner/system, server-side validation, abuse controls, access and retention rules, privacy/consent copy, support contact, and a verified test submission. Secrets and submission records must never enter public bundles, content files, or repository history. A static page alone is not a form-processing backend. If integration details remain unresolved, affected work stays in preview with an explicit pending state; unrelated pages can proceed.

## 4. Figma intake contract

The handoff must describe appearance **and** behavior. Screenshot exports alone are not enough for faithful implementation.

| Intake item | Designer/content-owner supplies | Developer verifies |
| --- | --- | --- |
| Design identity | Figma file URL, page/frame links or node IDs, named owner, handoff date/version, approved vs exploratory status. | Access to the correct revision and a stable record of what was accepted. Dev Mode is useful if available, not a prerequisite. |
| Page coverage | Desktop and mobile frames for each distinct template; tablet/intermediate layout notes. | Every approved route and shared shell maps to frames or an explicitly accepted reuse pattern. |
| Responsive rules | Content widths, fluid/fixed sizing, grid changes, stacking/reading order, navigation collapse, overflow and image-crop behavior. | Reference frame widths are recorded; CSS breakpoints follow behavior rather than blindly copying those widths. |
| Tokens | Semantic colors, typography roles, spacing scale, containers, radii, borders, shadows, layers, and motion settings. | Values and variable modes are inspectable; inconsistencies and missing tokens are logged. No style values are invented from the old PDF. |
| Fonts | Family names, weights/styles, files or approved source, fallback stack, license/hosting permission. | Required glyphs, diacritics, and any linguistic notation render; only needed weights are loaded. |
| Components | Named reusable components, variants, sizing rules, examples with real and long content. | Shared behavior is consistent across routes and can be implemented without unnecessary page duplication. |
| Interaction states | Focus, hover, active navigation, expanded mobile menu, unavailable/closed CTAs, and all applicable form states. | Click destinations, keyboard behavior, dismissal/focus return, loading/error behavior, and reduced-motion treatment are specified. |
| Assets | Original logo/vector and raster files, intended use, dimensions, crop/focal point, alt text/decorative designation, credit and usage rights. | Assets can be exported at sufficient quality; no production dependency on temporary Figma image URLs. |
| Content | Approved copy linked to section IDs, people/date records, final URLs, and permitted fallback/empty-state copy. | Text is selectable and complete; important wording is not trapped inside an image. |
| Review | Named design/content approvers, review channel, and the chosen revision. | Differences and exceptions have owners; later design changes are recorded against the accepted revision. |

Expected component inventory: `SiteHeader`, `PrimaryNavigation`, `MobileNavigation`, `SiteFooter`, `Hero`, `ButtonLink`, `SectionHeading`, `RichText`, `SatelliteSection`, `Timeline`, `PersonCard`, `PeopleGroup`, `GuidelineList`, `VenueDetails`, `HospitalityCard`, `ActivityList`, and registration/status components appropriate to the chosen mode. These are planning names, not a mandated component hierarchy. The design may support fewer shared primitives.

### Copyable intake record

Complete one record for each design delivery. Keep large file exports in an agreed asset location and link them here.

```text
Handoff ID / date:
Figma file and accepted revision:
Design owner / content owner / implementation owner:
Approved routes and languages:
Frame links by route (desktop / mobile / other):
Reference viewport dimensions:
Token and component-library links:
Assets and font package / licenses:
Approved copy and data revision:
Interaction and responsive notes:
Missing items and accepted defaults:
Decisions resolved (Dxx):
Reviewers / acceptance date:
Changes since the previous handoff:
```

Maintain a route/frame tracking table during intake:

| Route ID | Figma frames/revision | Content revision | Missing states/assets | Implementer | Review evidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P01–P05, one row each | Pending | Pending | Pending | Unassigned | Pending | Awaiting intake |

**Ready for implementation, per page/component:** approved reference frames or reuse rules, responsive behavior, required assets, content sufficient to exercise the layout, known interactions, and resolved decisions affecting that work. Approved provisional copy may support preview work, but it does not satisfy publication readiness. Missing registration details should not block the static page shell or unrelated content pages.

## 5. Content model and publication rules

**Proposed default:** Repository-managed content with validation, avoiding a CMS until editor needs justify one. Separate content from presentation so a copy update does not require editing layout components.

All publishable records carry a stable ID, source reference, owner, approval status (`draft`, `approved`, `withheld`), and last-reviewed date. Approval status is separate from event state such as submissions-open or registration-closed. Draft/withheld records stay out of production. Preview placeholders must be clearly marked; required missing content blocks release of the affected route, while optional omissions follow an agreed fallback.

| Entity | Minimum content contract | Reuse / validation |
| --- | --- | --- |
| Event/site | Approved name and acronym, year, short description, locale(s), event date range and timezone when confirmed, location, contact, production URL. | One source for titles, hero, footer, metadata, and structured data. Production URL can remain unset until deployment. |
| Navigation / CTA | ID, label, destination, internal/external type, order, visibility, phase/state. | Validate destinations; links must not use `#` as a placeholder action. Use anchors for navigation and buttons for actions. |
| Page/section | Route or section ID, heading, body, display order, metadata, applicable asset references. | Home About, satellite description, and page introductions use approved copy. Stable section anchors support deep links. |
| Satellite event | ID, title, description, optional confirmed date/location, relationship to main event, relevant CTA. | Do not assume its dates or participation process equal the main conference. |
| Milestone | ID, label, date precision, start/end value, timezone for timed deadlines, display order, confirmation status. | Use date-only values for calendar dates; use timestamp plus explicit zone/offset for exact deadlines. Never invent a midnight cutoff. |
| Person | ID, name, group memberships/roles, affiliation if supplied, portrait/alt policy, optional bio/links, order, home-feature flag. | Home references People records by ID. Only approved people may be featured. |
| Submission guidance | EasyAbs URL, introduction, ordered outline steps, reviewer criteria, approved language/format rules, optional downloads, revision date. | Guidelines and CTA state remain consistent with approved deadlines. |
| Venue / hospitality | ID, name, address/location, directions or description, official/map/booking URLs where applicable, image/credit, order. | Validate supplied links; avoid unapproved booking or travel claims. |
| Activity | ID, title, description, optional location/link/image, suggested vs organized status, order. | Reference screenshot activities require organizer review before publication. |
| Registration | Mode, open/closed/pending state, explanatory/outcome copy, approved external URL or endpoint configuration, field contract if needed. | Server secrets are separate environment configuration. No submissions are stored in site content. |
| Asset / download | ID, path, type, dimensions where relevant, alt/decorative designation, focal point, credit/license, display label. | Detect missing files; label downloads with format and size where useful. |

Preserve Unicode names and linguistic notation. Never parse an ambiguous date string such as `02-11-2026` as a runtime deadline. The document date is interpreted here as 2 November 2026; conference dates still need confirmation. Confirm the event/deadline timezone independently of the developer's machine timezone.

For static output, changes to deadlines, visibility, registration status, or content require a rebuild. Assign an update owner and schedule deployments for transitions, or explicitly add an automated rebuild mechanism. A date displayed on a page does not itself close an external form. If automatic behavior is selected, test it at the boundary in the approved timezone.

## 6. Astro implementation baseline

These are proposed engineering defaults. Recheck current official documentation when implementation begins, select a stable Astro release and compatible Node/package-manager versions, then pin them and commit the lockfile. This planning document deliberately does not freeze dependency versions months ahead of the build.

| Concern | Planned approach | Technical reference |
| --- | --- | --- |
| Rendering/routes | Static output, `.astro` routes in `src/pages/`, shared layouts, ordinary links. Request-time rendering only if the accepted requirements need it. | [Astro routing](https://docs.astro.build/en/guides/routing/) |
| Content | Build-time collections with schemas/loaders in `src/content.config.ts` for repeated records and long-form content; typed singleton configuration for site-wide data. Validate IDs, required fields, dates, and referenced records. | [Content collections](https://docs.astro.build/en/guides/content-collections/) |
| Interactivity | `.astro` components and small scripts for simple controls. Add a UI framework only for an interaction that benefits from it; hydrate individual components deliberately. | [Template directives](https://docs.astro.build/en/reference/directives-reference/) |
| Styling | CSS custom properties for accepted Figma tokens, shared styles for foundations, component styles for local behavior. CSS framework choice remains open; none is required by this spec. | Project convention to establish at intake. |
| Images | Keep optimizable originals under `src/` and use Astro image facilities with suitable responsive sizes. Reserve `public/` for assets requiring unchanged stable URLs. Specify dimensions and lazy-load suitable below-fold media. | [Astro images](https://docs.astro.build/en/guides/images/) |
| Languages | Proposed initial site language: English, pending confirmation. Abstract/presentation languages do not automatically create translated website routes. Decide locales and fallback behavior before adding translations. | [Internationalization routing](https://docs.astro.build/en/guides/internationalization/) |
| Deployment | Host undecided. Build static output for deployment; add an adapter only if on-demand rendering is selected. Document production and preview environments. | [Deploy an Astro site](https://docs.astro.build/en/guides/deploy/) |

Indicative future structure; these files are not being scaffolded now:

```text
src/
  pages/                 # Five agreed routes and 404 page
  layouts/               # Shared document shell and metadata
  components/            # Shared UI and section components
  content/               # Approved copy and repeatable records
  content.config.ts      # Collection loaders and validation schemas
  data/                  # Site/navigation and other singleton configuration
  assets/                # Images processed by Astro
  styles/                # Tokens, typography, global styles
public/                  # Stable downloads, favicon, unchanged assets
docs/                    # Spec, intake decisions, maintenance notes
```

Do not require a client-side application runtime for reading conference information. If JavaScript is unavailable, essential copy and destination links must remain accessible; provide a usable navigation fallback. Integrations should not make static content depend on a third party responding at page load. Prefer a simple map link unless an embedded map is specifically accepted.

## 7. Quality and acceptance criteria

These criteria apply to the later implementation, not to the current document-only task. The designer and developer should agree on any exceptions during intake, with an owner and resolution recorded.

| ID | Acceptance condition | Evidence |
| --- | --- | --- |
| A01 · Coverage | Every accepted P01–P05 page/section exists; agreed navigation, CTA destinations, and direct route visits work. | Route/content checklist and link check; no unintended placeholders or broken assets. |
| A02 · Fidelity | Implementation follows the accepted Figma revision for hierarchy, typography, spacing, colors, imagery, and interactions. | Side-by-side screenshots at supplied frame sizes, using the same copy/assets; deviations logged and resolved or accepted. Do not set an arbitrary pixel-difference tolerance before seeing designs. |
| A03 · Responsive behavior | No clipping or unwanted horizontal scrolling at 320, 375, 768, 1024, and 1440 CSS px, plus actual supplied frame widths. Long names/content and image fallbacks work. | Manual checks at target and intermediate widths, portrait/landscape as relevant, and zoom/reflow checks. These are test widths, not fixed breakpoints. |
| A04 · Accessibility | Target WCAG 2.2 AA: semantic landmarks/headings, skip link, keyboard access, visible focus, sufficient contrast, useful labels/alt text, accessible errors and status messages. Respect reduced-motion preferences. | Automated checks plus manual keyboard, zoom, and screen-reader smoke review of navigation, content, and any form. Automated scores alone do not establish conformance. |
| A05 · Content integrity | Approved names, dates, guidance, links, permissions, and venue information are used consistently; provisional screenshot data is not silently published. | Content owner checks each route against approved records; build validation catches schema and reference errors. |
| A06 · Integrations | EasyAbs and any registration destination work. If a form is selected, validation, success, failure, retry, duplicate behavior, and downstream receipt are verified. | Tests in an agreed test environment and operational-owner confirmation; no real participant data used for test fixtures. |
| A07 · Performance | Proposed lab target: Lighthouse mobile Performance ≥90 on each route using a production build and documented settings; review three runs and record the median. Investigate image/font/third-party costs. | Saved report and device/network settings. Aim for field LCP ≤2.5 s, INP ≤200 ms, and CLS ≤0.1 at the 75th percentile once sufficient field data exists; do not claim field compliance from Lighthouse. |
| A08 · Metadata | Unique title/description per route, correct canonical URLs, favicon/social preview assets, sitemap, robots behavior, and useful 404. | Inspect generated production HTML and deployed paths. Event structured data is optional and uses confirmed facts only. |
| A09 · Reliability | Clean install, schema/type checks, and production build pass; supported-browser flows work. | Document actual project commands. Proposed scripts: `dev`, `check`, `build`, `preview`; add meaningful automated tests for custom logic/integrations, not static copy duplication. |
| A10 · Operations | Domain/HTTPS, deployment owner, content-update workflow, rollback, form ownership where relevant, and handover notes are established. | Preview and production smoke checks; known-good release can be restored. |

Accessibility target reference: [W3C WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/). Performance metric reference: [Web Vitals](https://web.dev/articles/vitals). The Lighthouse threshold is a proposed project target, not a requirement from the PDF.

Proposed browser coverage: current Chrome, Firefox, Safari, and Edge at build time, plus iOS Safari and Android Chrome. Record actual tested versions/devices; agree on any older-browser requirement before implementation. Preview deployments should be kept out of search indexing; access control is needed if they contain non-public content, since `noindex` is not access control.

## 8. Delivery sequence and review gates

| Phase | Work | Exit evidence |
| --- | --- | --- |
| 0 · Specification, now | Preserve outline, define scope and content model, record open decisions. | This document and source copy. No site, integration, or deployment is created in this phase. |
| 1 · Design/content intake | Complete the intake record, map routes to frames, inventory tokens/assets, resolve affected D-items. | Accepted design revision, page readiness table, content source and owners. |
| 2 · Foundation | Pin tools, initialize Astro, configure content validation, implement tokens and shared shell. | Working responsive shell; basic navigation and build checks pass. |
| 3 · Pages/content | Implement accepted page templates and reusable components; connect approved records. | Each route reviewed against its design and content checklist. |
| 4 · Confirmed integrations | Wire EasyAbs CTAs and the selected registration mechanism; implement required states. | Verified destinations or end-to-end test submission, accurate outcomes, operational owner. |
| 5 · Acceptance | Complete A01–A10, design comparison, content approval, and launch checklist. | Review evidence, resolved blocking issues, named release owner. |
| 6 · Release/handover | Deploy within the later agreed release scope; verify live site and provide maintenance notes. | Live checks, rollback reference, update instructions, and ownership recorded. |

Design or content changes after intake must record the changed frames/records, affected components/routes, any new behavior, and the required rechecks. Review the changed scope instead of silently mixing design revisions. Parallel work can proceed on ready pages while unresolved integrations remain isolated in preview.

Handover must explain how to update dates, people, guidelines, CTA status, and assets; how to build/preview/deploy; where configuration and secrets live; how to verify form delivery; and how to restore a previous release. Assign an owner for changes during the conference and for closing forms or archiving content afterward.

## 9. Open decisions and missing inputs

All items are **open** at v0.1. Roles below are proposed ownership, not assigned individuals. Resolve each before its dependency is finalized; none prevents preparing this specification.

| ID | Decision/input | Proposed owner | Needed before |
| --- | --- | --- | --- |
| D01 | Official event name, acronym, capitalization, and association description; resolve “ACPLE” vs “ACBLPE.” | Organizer/content lead | Public copy and metadata |
| D02 | Accept five routes and People navigation placement; choose dedicated Registration page or Venue anchor. | Organizer + designer | Final route/nav implementation |
| D03 | Registration vs interest vs external service; audience, fields, provider/endpoint, process/outcome, owner and privacy text. | Organizer + registration operator | Data collection and final CTA copy |
| D04 | Earlier EasyAbs document, exact conference URL, approved guidelines/reviewer criteria and downloadable files if any. | Scientific/content lead | Call for Papers release |
| D05 | Confirm every milestone, main/satellite event dates, timezone and deadline cutoff; explain overlapping example date ranges. | Organizer | Date/phase-dependent behavior and publication |
| D06 | Approved speakers, organizers, committee membership/ordering, affiliations, biographies, images, and publication permissions. | Organizer | People and speaker content release |
| D07 | Venue/address, travel directions, hospitality partners/booking terms, approved Goa activity copy and links. | Local organizing team | Venue release |
| D08 | Figma access/revision, all page frames, states, responsive rules, tokens, font/asset package and licenses. | Designer | Faithful UI implementation |
| D09 | Website language(s), translation owner and route/fallback strategy; distinguish these from presentation languages. | Organizer | Route/content schema finalization |
| D10 | Hero CTA priority, before/open/closed content, missing-content fallbacks, and date-transition update process. | Organizer + developer | CTA behavior and release |
| D11 | Domain, hosting, preview access, deployment method, production configuration, and rollback/update owner. | Project owner + developer | Deployment |
| D12 | Contact details, footer links, metadata/social assets, any required notices; analytics only if specifically requested. | Organizer/content lead | Launch review |
| D13 | Any additional pages or features beyond this outline and their content/design ownership. | Project owner | Scope baseline changes |

## 10. Reference screenshot inventory: confirm before use

These are observations from the PDF, not verified conference facts or the future visual brief. Their purpose is to keep useful source material visible while preventing accidental publication of provisional details.

| Source | Observed material | Follow-up |
| --- | --- | --- |
| p. 1 | Example hero “Creoles across the Indian Ocean,” references to Goa University/India and the 25th annual conference, abstract and registration CTAs. | Confirm event title/theme, edition, affiliation, copy, and CTA targets. |
| p. 2 | About text and a satellite example titled “Linguistic Encounters in South Asia,” labeled 31 August 2027. | Obtain approved editable copy and satellite details. |
| p. 3 | Timeline example: submissions open 30 October 2026; close 15 January 2027; review 16 January–15 February 2027; satellite 31 August 2027; main conference 31 August–3 September 2027. | Confirm all dates and cutoffs; clarify shared start date. Do not derive live status from this example. |
| p. 3 | “Proposed” keynote speakers: Hugo C. Cardoso, J. Clancy Clements, Eeva Sippola, Sonal Kulkarni-Joshi, Anvita Abbi. | Confirm participation, names/titles, affiliations, order, portraits, and permission to announce. |
| p. 4 | Eight suggested abstract-outline steps covering title, topic, prior work, linguistic data/glosses, abbreviations, provisional results/method, relation to prior work/analysis, and contribution. | Obtain editable approved text and any actual submission-format rules. |
| p. 5 | Three reviewer criteria; example languages: Creole, English, French, Portuguese, Spanish; 30-minute session shown as 20-minute presentation + 10-minute discussion. | Confirm policy wording, exact language labels, and timings against the EasyAbs text. |
| p. 6 | Activity examples: Fontainhas heritage walk, Old Goa monuments, Mandovi river cruise, Divar and Chorao islands. | Confirm inclusions, descriptions, logistics, links, and suggested vs organized status. |
| p. 6 | Requests for additional copy, images/logos/media, form data fields, and any extra pages; earlier EasyAbs text is referenced but absent. | Treat these as missing inputs in D03, D04, D08, and D13. |

## 11. Source and revision record

- Source PDF: [preserved reference](reference/acblpe-2027-content-outline.pdf), all six pages visually reviewed as well as text-extracted.
- Source SHA-256: `1714462535b45b192231962cfc286a8f87ff0a9e095ba22e2b4eb4cc5162a14c`.
- Official technical references in sections 6–7 were checked on 2 November 2026. Revalidate version-sensitive APIs and integration behavior when building.
- No Figma file, earlier EasyAbs text, approved final content package, hosting choice, or registration integration was supplied for this version.
- v0.1: Initial specification derived from the outline and the user's request for a later Figma-to-Astro build.
