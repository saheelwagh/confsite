(() => {
  'use strict';
  const root = document.documentElement;
  const art = window.StudyArt;
  const $ = (selector) => document.querySelector(selector);
  const $$ = (selector) => [...document.querySelectorAll(selector)];
  const palettes = {
    azulejo: {
      number: '01', name: 'Azulejo azul', kicker: 'THE RECOMMENDED FOUNDATION',
      colours: { paper: '#F7F4EA', primary: '#214EA2', ink: '#132847', soft: '#DAE5F0', accent: '#C19A53' },
      names: ['Ceramic', 'Cobalt', 'Deep ink', 'Mist', 'Brass'],
      description: 'Use a tiled mural as the signature, then let generous ceramic-white space and cobalt typography carry the information. Ornament belongs at the edges, not behind the reading.',
      vocabulary: 'Floral geometry · fine borders · glazed surfaces',
      guidance: 'Paper for the canvas; cobalt for actions; ink for body text. Brass is a decorative accent.'
    },
    fontainhas: {
      number: '02', name: 'Fontainhas afternoon', kicker: 'A WARMER, MORE SOCIAL DIRECTION',
      colours: { paper: '#FAF1DF', primary: '#9E4237', ink: '#372B2A', soft: '#EBCFAC', accent: '#677A54' },
      names: ['Plaster', 'Terracotta', 'Umber', 'Ochre wash', 'Shutter green'],
      description: 'Translate the colourful façades of Fontainhas into warm surfaces, framed panels, and arch-shaped details. Keep the page structure crisp so the colour feels welcoming rather than busy.',
      vocabulary: 'Arched frames · painted façades · warm colour blocks',
      guidance: 'Plaster for the canvas; terracotta for actions; umber for text. Ochre and shutter green add character.'
    },
    monsoon: {
      number: '03', name: 'Monsoon garden', kicker: 'A QUIETER, BOTANICAL INTERPRETATION',
      colours: { paper: '#F2F1E7', primary: '#286052', ink: '#1C3A32', soft: '#D9E5D8', accent: '#B8A263' },
      names: ['Linen', 'Deep leaf', 'Forest ink', 'Sage', 'Seed gold'],
      description: 'Let botanical silhouettes soften the geometry. Deep green and pale linen give long academic content a calm setting, with leaf-like linework as a counterpoint to the tile grid.',
      vocabulary: 'Leaf silhouettes · organic lines · generous quiet space',
      guidance: 'Linen for the canvas; deep leaf for actions; forest ink for text. Gold is reserved for decorative details.'
    },
    ocean: {
      number: '04', name: 'Indian Ocean atlas', kicker: 'A DIRECTION BUILT AROUND CONNECTION',
      colours: { paper: '#F5EFE2', primary: '#225E70', ink: '#203842', soft: '#D1E4E2', accent: '#AE763F' },
      names: ['Parchment', 'Ocean teal', 'Chart ink', 'Sea glass', 'Weathered brass'],
      description: 'Borrow the visual language of an atlas: fine rules, compass geometry, and connected points. A fitting creative response to “Creoles across the Indian Ocean,” with no literal map required.',
      vocabulary: 'Compass geometry · connecting lines · tidal curves',
      guidance: 'Parchment for the canvas; ocean teal for actions; chart ink for text. Brass marks small points of emphasis.'
    }
  };
  let currentPalette = 'azulejo';
  let currentPage = 'home';
  let speed = 1;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let motionEnabled = !reducedMotion.matches;
  const timers = new Map();

  function tileMarkup(count, columns = 4) {
    return Array.from({ length: count }, (_, i) => `<span class="tile" style="--delay:${(Math.floor(i / columns) + i % columns) * 45}ms">${art.tile(i)}</span>`).join('');
  }
  $('#hero-mural').innerHTML = tileMarkup(16);
  $('#demo-mural').innerHTML = tileMarkup(16);
  $('#glaze-tile').innerHTML = art.tile(0);
  $$('[data-art]').forEach((container) => {
    container.innerHTML = container.dataset.art === 'tiles' ? tileMarkup(12, 3) : art[container.dataset.art]();
  });
  $$('.demo-timeline i').forEach((dot, i) => dot.style.setProperty('--delay', `${i * 180}ms`));
  $$('[data-swatches]').forEach((container) => {
    container.innerHTML = Object.values(palettes[container.dataset.swatches].colours).map((colour) => `<i style="background:${colour}"></i>`).join('');
  });

  function applyPalette(key, announce = true) {
    if (!palettes[key]) return;
    currentPalette = key;
    const palette = palettes[key];
    root.dataset.theme = key;
    Object.entries(palette.colours).forEach(([role, colour]) => root.style.setProperty(`--${role}`, colour));
    $('meta[name="theme-color"]').content = palette.colours.paper;
    $('#hero-theme-index').textContent = palette.number;
    $('#hero-theme-name').textContent = palette.name;
    $('#palette-kicker').textContent = palette.kicker;
    $('#palette-name').textContent = palette.name;
    $('#palette-description').textContent = palette.description;
    $('#palette-vocabulary').textContent = palette.vocabulary;
    $('#palette-guidance').textContent = palette.guidance;
    $('#preview-theme-label').textContent = palette.name.toUpperCase();
    $('#copy-status').textContent = '';
    $('#active-swatches').innerHTML = Object.entries(palette.colours).map(([role, colour], i) => `<div class="swatch-block"><i style="background:${colour}" aria-hidden="true"></i><strong>${palette.names[i]}</strong><span>${colour}</span><span class="sr-only">${role}</span></div>`).join('');
    $$('[data-palette]').forEach((button) => {
      const selected = button.dataset.palette === key;
      button.setAttribute('aria-pressed', String(selected));
      button.querySelector('.direction-select').innerHTML = selected ? 'Selected direction <span aria-hidden="true">✓</span>' : 'Try this direction <span aria-hidden="true">→</span>';
    });
    if (announce) $('#theme-announcement').textContent = `${palette.name} applied to the notebook and conference previews.`;
    try { localStorage.setItem('acblpe-study-palette', key); } catch { /* The study also works when browser storage is unavailable. */ }
  }
  $$('[data-palette]').forEach((button) => button.addEventListener('click', () => applyPalette(button.dataset.palette)));
  let savedPalette;
  try { savedPalette = localStorage.getItem('acblpe-study-palette'); } catch { /* File previews may disallow storage. */ }
  applyPalette(palettes[savedPalette] ? savedPalette : 'azulejo', false);

  $('#copy-palette').addEventListener('click', async () => {
    const palette = palettes[currentPalette];
    const code = `/* ACBLPE design study: ${palette.name} */\n:root {\n${Object.entries(palette.colours).map(([role, colour]) => `  --${role}: ${colour};`).join('\n')}\n}`;
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(code);
      $('#copy-status').textContent = `${palette.name} CSS tokens copied.`;
    } catch {
      $('#palette-code').value = code;
      $('#copy-dialog').showModal();
      $('#palette-code').focus();
      $('#palette-code').select();
    }
  });
  $('#copy-dialog').addEventListener('close', () => $('#copy-palette').focus());

  const previews = {
    home: () => `<div class="preview-hero"><div><p class="eyebrow">ACBLPE · GOA · 2027</p><h3>Creoles across<br>the <em>Indian Ocean.</em></h3><p>A meeting of languages, histories, and ideas. Join the conversation on Iberian-lexified creoles and linguistic encounters across the region.</p><button class="button primary" type="button" data-open-page="papers">Explore the call for papers <span aria-hidden="true">↗</span></button></div><div class="preview-tile-grid" aria-hidden="true">${tileMarkup(9, 3)}</div></div><div class="preview-satellite"><div><p class="eyebrow">SATELLITE CONFERENCE</p><h4>Linguistic Encounters<br>in South Asia</h4></div><p>A space for research and conversation about language contact in South Asia. Details and participation information will be confirmed.</p></div><div class="preview-dates"><div><small>SUBMISSIONS CLOSE · EXAMPLE</small><strong>15 January 2027</strong></div><div><small>SATELLITE · EXAMPLE</small><strong>31 August 2027</strong></div><div><small>MAIN CONFERENCE · EXAMPLE</small><strong>31 Aug – 3 Sep 2027</strong></div></div>`,
    papers: () => `<div class="preview-page-intro"><p class="eyebrow">CALL FOR PAPERS / DESIGN PREVIEW</p><h3>A place for<br><em>your research.</em></h3><p>Abstract submissions will be made through the conference’s EasyAbs page. The final submission link, deadlines, and instructions are awaiting confirmation.</p></div><div class="preview-columns"><ol class="guidelines"><li>Choose a clear title that identifies your paper’s topic.</li><li>State the topic and connect it to relevant prior work.</li><li>Present linguistic data and explain abbreviations.</li><li>Describe your analysis and contribution to the field.</li></ol><aside class="preview-note"><p class="eyebrow">HOW ABSTRACTS ARE ASSESSED</p><h4>Clarity. Relevance.<br>Contribution.</h4><p>A visual sample of the reviewer-guidance section. Complete wording will follow the approved EasyAbs document.</p><button class="text-button" type="button" data-preview-message="The conference-specific EasyAbs URL has not been supplied. This is a design preview.">Preview submission action ↗</button><p class="preview-feedback" role="status"></p></aside></div>`,
    people: () => `<div class="preview-page-intro"><p class="eyebrow">PEOPLE & COMMITTEES</p><h3>Different perspectives.<br><em>A shared curiosity.</em></h3><p>Sample keynote cards from the outline’s proposed speaker list. Participation, titles, and affiliations remain to be confirmed.</p></div><div class="preview-people"><article class="person-card"><span class="person-monogram" aria-hidden="true">HC</span><h4>Hugo C. Cardoso</h4><p>Proposed keynote speaker</p></article><article class="person-card"><span class="person-monogram" aria-hidden="true">JC</span><h4>J. Clancy Clements</h4><p>Proposed keynote speaker</p></article><article class="person-card"><span class="person-monogram" aria-hidden="true">ES</span><h4>Eeva Sippola</h4><p>Proposed keynote speaker</p></article><article class="person-card"><span class="person-monogram" aria-hidden="true">SK</span><h4>Sonal Kulkarni-Joshi</h4><p>Proposed keynote speaker</p></article><article class="person-card"><span class="person-monogram" aria-hidden="true">AA</span><h4>Anvita Abbi</h4><p>Proposed keynote speaker</p></article></div><p class="people-note">Organizers and scientific committee will use the same card language, grouped by role. Initials keep this study independent of unapproved portraits.</p>`,
    venue: () => `<div class="preview-venue"><div><p class="eyebrow">VENUE & GOA</p><h3>Beyond<br><em>the conversation.</em></h3><p>A place for practical travel information, hospitality partners, and ways to discover Goa between conference sessions.</p><p>The final venue, directions, and partner information are pending. The illustration is a visual study, not a drawing of the conference venue.</p></div><div class="venue-preview-art" aria-hidden="true">${art.facade()}</div></div><div class="venue-details"><div><h4>Find your way</h4><p>Venue address, travel directions, and a useful map link.</p></div><div><h4>Stay a little</h4><p>Hospitality partners and approved booking information.</p></div><div><h4>Explore Goa</h4><p>Fontainhas, Old Goa, and local activities from the outline.</p></div></div>`,
    registration: () => `<div class="registration-preview"><div><p class="eyebrow">REGISTRATION / VISUAL STUDY</p><h3>Begin with<br><em>a connection.</em></h3><p>A simple form treatment to explore the visual language. Whether this becomes registration, an expression of interest, or an external link is still an open decision.</p><p>These are illustrative fields with fixed sample values. This preview does not collect or send personal information.</p></div><form class="example-form" id="example-form"><p class="eyebrow">ILLUSTRATIVE INTEREST FORM</p><label>Full name<input readonly value="Alex Fernandes" autocomplete="off"></label><label>Email address<input readonly value="alex@example.org" autocomplete="off"></label><button class="button primary" type="submit">Preview confirmation <span aria-hidden="true">↗</span></button><p class="preview-feedback" id="form-feedback" role="status">Sample values only. Final fields to be agreed.</p></form></div>`
  };
  function setPage(page, focusTab = false) {
    if (!previews[page]) return;
    currentPage = page;
    const panel = $('#preview-panel');
    panel.innerHTML = previews[page]();
    panel.setAttribute('aria-labelledby', `tab-${page}`);
    $$('[data-page]').forEach((button) => {
      const selected = button.dataset.page === page;
      button.setAttribute('aria-selected', String(selected));
      button.tabIndex = selected ? 0 : -1;
      if (selected && focusTab) button.focus({ preventScroll: true });
    });
  }
  $$('[data-page]').forEach((button) => button.addEventListener('click', () => setPage(button.dataset.page)));
  $('.preview-tabs').addEventListener('keydown', (event) => {
    const tabs = $$('[data-page]');
    const index = tabs.indexOf(document.activeElement);
    if (index < 0) return;
    let next;
    if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
    if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
    if (event.key === 'Home') next = 0;
    if (event.key === 'End') next = tabs.length - 1;
    if (next === undefined) return;
    event.preventDefault();
    setPage(tabs[next].dataset.page, true);
  });
  $('#preview-panel').addEventListener('click', (event) => {
    const link = event.target.closest('[data-open-page]');
    if (link) setPage(link.dataset.openPage, true);
    const message = event.target.closest('[data-preview-message]');
    if (message) message.parentElement.querySelector('[role="status"]').textContent = message.dataset.previewMessage;
  });
  $('#preview-panel').addEventListener('submit', (event) => {
    event.preventDefault();
    if (event.target.id === 'example-form') {
      $('#form-feedback').textContent = 'Demo confirmation: your interest would be acknowledged here. No information was sent.';
    }
  });
  setPage(currentPage);

  function setMotion(enabled) {
    motionEnabled = enabled;
    root.dataset.motion = enabled ? 'on' : 'off';
    $('#motion-toggle').checked = enabled;
    $('#motion-status').textContent = enabled ? 'Motion is enabled. Replay a study or play them together; each runs once.' : 'Motion is off. Every study is shown in its finished state.';
    if (!enabled) {
      timers.forEach(clearTimeout);
      timers.clear();
      $$('.is-playing').forEach((element) => element.classList.remove('is-playing'));
    }
  }
  function replay(element, duration) {
    if (!motionEnabled) {
      $('#motion-status').textContent = 'Motion is off. Turn on “Enable motion” to play; the finished designs remain visible.';
      return;
    }
    if (timers.has(element)) clearTimeout(timers.get(element));
    element.classList.remove('is-playing');
    void element.offsetWidth;
    element.classList.add('is-playing');
    timers.set(element, setTimeout(() => {
      element.classList.remove('is-playing');
      timers.delete(element);
    }, duration * speed + 100));
  }
  const durations = { assemble: 850, glaze: 800, draw: 1100, timeline: 800, lift: 1000 };
  $$('[data-replay]').forEach((button) => button.addEventListener('click', () => {
    replay($(`[data-demo="${button.dataset.replay}"]`), durations[button.dataset.replay]);
    if (motionEnabled) $('#motion-status').textContent = `Playing ${button.getAttribute('aria-label').replace('Replay ', '')} once.`;
  }));
  $('#replay-hero').addEventListener('click', () => {
    replay($('#hero-mural'), 850);
    if (!motionEnabled) $('#theme-announcement').textContent = 'Motion is off. Enable it in Motion studies to replay the tiles.';
  });
  $('#play-all').addEventListener('click', () => {
    Object.entries(durations).forEach(([name, duration]) => replay($(`[data-demo="${name}"]`), duration));
    if (motionEnabled) $('#motion-status').textContent = 'Playing all five studies once.';
  });
  $('#motion-toggle').addEventListener('change', (event) => setMotion(event.target.checked));
  $('#motion-speed').addEventListener('change', (event) => {
    speed = Number(event.target.value);
    root.style.setProperty('--tempo', String(speed));
    timers.forEach(clearTimeout);
    timers.clear();
    $$('.is-playing').forEach((element) => element.classList.remove('is-playing'));
    $('#motion-status').textContent = `${speed === 1 ? 'Natural' : 'Slow study'} speed selected. ${motionEnabled ? 'Press replay to see the change.' : 'Enable motion to play.'}`;
  });
  reducedMotion.addEventListener('change', (event) => setMotion(!event.matches));
  setMotion(motionEnabled);
  if (motionEnabled) requestAnimationFrame(() => replay($('#hero-mural'), 850));
})();
