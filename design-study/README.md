# ACBLPE Goa 2027 — design notebook

A local, buildless visual playground for the later Figma design. Plain HTML, CSS, JavaScript, and original inline SVG artwork; no Astro, package installation, build step, external fonts, analytics, or backend.

## Open

Open `index.html` directly in a modern browser, or serve this directory:

```sh
cd /Users/saheelwagh/coding/hackathon/confsite/design-study
python3 -m http.server 4173 --bind 127.0.0.1
```

Then visit [the local preview](http://127.0.0.1:4173). Stop the server with Ctrl+C when finished.

## Explore

- Four palettes apply to the entire notebook: **Azulejo azul**, **Fontainhas afternoon**, **Monsoon garden**, and **Indian Ocean atlas**. Each has five named hex colours and a Copy CSS action with a manual fallback. The selected palette is remembered in local browser storage when available.
- Five conference page previews: Home, Call for Papers, People, Venue, and Registration. Tab controls support arrow keys and Home/End. Sample dates/speakers are explicitly provisional. The form uses fixed sample values and never sends data.
- Five finite animation demos: diagonal tile assembly, ceramic glaze, line drawing, timeline progression, and linked-card feedback. Each has replay; there are shared playback-speed and motion controls. Reduced-motion preferences initialize the study with motion off; explicit opt-in is available for comparison.
- All illustrations are original decorative studies. Building art is not a picture of the conference venue; chart art is not a geographic map. External links are reading references, not required runtime resources.

## Design recommendation

Start with **Azulejo azul**: cobalt `#214EA2`, ceramic `#F7F4EA`, ink `#132847`, mist `#DAE5F0`, and decorative brass `#C19A53`. Use the hero mural as the signature and keep reading surfaces quiet. Combine one tile entrance with restrained timeline and link feedback; glaze and line drawing can remain optional.

Fontainhas offers a warmer social tone; monsoon offers a calm botanical tone; atlas makes connections across the Indian Ocean the visual idea. Palette values are design proposals, not historically sampled pigments. Accent colours are decorative; body text and buttons use the dark ink/primary pairs.

## Files

- `index.html`: notebook structure and motion stages.
- `styles.css`: responsive layout, theme roles, and finite CSS animations.
- `study.js`: palette switching/export, page previews, keyboard tabs, and motion controls.
- `art.js`: original palette-responsive SVG illustrations exposed by `window.StudyArt`.
- `../docs/acblpe-2027-website-spec.md`: requirements and unresolved decisions for the later production site.

## Inspiration

- [AzulejosGoa: Portuguese Azulejo Tiles in Goa](https://azulejosgoa.com/blog-azulejo-history-goa.html): the user's starting reference for cobalt/floral/geometric tile language; used as a visual reference, not as an independently verified history.
- [Goa Tourism: Experience Fontainhas](https://goa-tourism.com/popular-destination/experience-fontainhas/): colourful architecture as a related direction.
- [UNESCO: Churches and Convents of Goa](https://whc.unesco.org/en/list/234/): architectural context and adaptation to local materials and practices.

The notebook's copy and sample data refer to the supplied outline. Exact event copy, participants, dates, form scope, and visuals remain subject to organizer and Figma approval.
