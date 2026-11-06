(function () {
  'use strict';

  const paint = {
    primary: 'var(--primary)',
    accent: 'var(--accent)',
    paper: 'var(--paper)',
    ink: 'var(--ink)',
    soft: 'var(--soft)'
  };

  function svg(viewBox, content, kind) {
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + viewBox + '" aria-hidden="true" focusable="false" class="study-art study-art--' + kind + '">' + content + '</svg>';
  }

  function turn(content, count, start) {
    return Array.from({ length: count }, function (_, i) {
      return '<g transform="rotate(' + ((start || 0) + i * 360 / count) + ' 50 50)">' + content + '</g>';
    }).join('');
  }

  function tileFrame(content) {
    return '<rect width="100" height="100" fill="' + paint.paper + '"/>' +
      '<rect x="1.5" y="1.5" width="97" height="97" fill="none" stroke="' + paint.primary + '" stroke-width="1.2"/>' +
      '<rect x="4.5" y="4.5" width="91" height="91" fill="none" stroke="' + paint.primary + '" stroke-width=".45"/>' +
      content;
  }

  function rosette() {
    const corners = turn(
      '<path d="M8 8C20 9 22 17 19 22C13 23 9 17 8 8Z" fill="' + paint.primary + '"/>' +
      '<path d="M10 10L18 20M9 29C19 30 27 25 28 16" fill="none" stroke="' + paint.accent + '" stroke-width="1.1"/>' +
      '<circle cx="29" cy="10" r="1.6" fill="' + paint.primary + '"/>', 4
    );
    const outer = turn(
      '<path d="M50 46C38 37 35 20 50 9C65 20 62 37 50 46Z" fill="' + paint.primary + '"/>' +
      '<path d="M50 39C43 30 44 20 50 15C56 20 57 30 50 39Z" fill="' + paint.paper + '"/>' +
      '<path d="M50 34Q44 26 50 20Q56 26 50 34Z" fill="' + paint.accent + '"/>', 8
    );
    return corners + outer +
      '<circle cx="50" cy="50" r="14.5" fill="' + paint.paper + '" stroke="' + paint.primary + '" stroke-width="1.2"/>' +
      turn('<path d="M50 48C42 44 44 37 50 39C56 37 58 44 50 48Z" fill="' + paint.accent + '"/>', 8) +
      '<circle cx="50" cy="50" r="5" fill="' + paint.primary + '"/>' +
      '<circle cx="50" cy="50" r="1.7" fill="' + paint.paper + '"/>';
  }

  function quarterFlower() {
    const quarters = turn(
      '<path d="M5 43A38 38 0 0 0 43 5" fill="none" stroke="' + paint.primary + '" stroke-width="2.5"/>' +
      '<path d="M5 37A32 32 0 0 0 37 5" fill="none" stroke="' + paint.accent + '" stroke-width=".8"/>' +
      '<path d="M5 7C18 5 25 8 24 15C17 21 9 17 5 7Z" fill="' + paint.primary + '"/>' +
      '<path d="M7 5C5 18 8 25 15 24C21 17 17 9 7 5Z" fill="' + paint.primary + '"/>' +
      '<path d="M11 11C27 10 32 20 27 27C20 32 10 27 11 11Z" fill="' + paint.accent + '"/>' +
      '<path d="M14 14L25 25M9 9L21 12M9 9L12 21" fill="none" stroke="' + paint.paper + '" stroke-width="1.1"/>' +
      '<circle cx="8" cy="8" r="3.7" fill="' + paint.primary + '"/>' +
      '<path d="M42 16C47 20 48 27 44 31C38 29 38 23 42 16Z" fill="' + paint.soft + '"/>' +
      '<path d="M16 42C20 47 27 48 31 44C29 38 23 38 16 42Z" fill="' + paint.soft + '"/>', 4
    );
    return quarters +
      '<path d="M50 27C52 39 61 48 73 50C61 52 52 61 50 73C48 61 39 52 27 50C39 48 48 39 50 27Z" fill="' + paint.primary + '"/>' +
      '<path d="M50 37L63 50L50 63L37 50Z" fill="' + paint.paper + '"/>' +
      '<path d="M50 43L57 50L50 57L43 50Z" fill="' + paint.accent + '"/>';
  }

  function compass() {
    return turn(
      '<path d="M8 8H29L20 17L17 20L8 29Z" fill="' + paint.soft + '"/>' +
      '<path d="M10 10H22L16 16L10 22Z" fill="' + paint.primary + '"/>' +
      '<path d="M36 7L50 13L64 7M7 36L13 50L7 64" fill="none" stroke="' + paint.accent + '" stroke-width="1"/>', 4
    ) +
      '<path d="M50 8L62 27L84 16L73 38L92 50L73 62L84 84L62 73L50 92L38 73L16 84L27 62L8 50L27 38L16 16L38 27Z" fill="' + paint.primary + '"/>' +
      '<path d="M50 19L59 35L75 25L65 41L81 50L65 59L75 75L59 65L50 81L41 65L25 75L35 59L19 50L35 41L25 25L41 35Z" fill="' + paint.paper + '"/>' +
      turn('<path d="M50 24L56 44L50 50L44 44Z" fill="' + paint.accent + '"/><path d="M50 24V50L44 44Z" fill="' + paint.primary + '"/>', 4) +
      '<path d="M50 39L61 50L50 61L39 50Z" fill="' + paint.primary + '" stroke="' + paint.paper + '" stroke-width="1.2"/>' +
      '<circle cx="50" cy="50" r="3.2" fill="' + paint.paper + '"/>';
  }

  function leaves() {
    return turn(
      '<path d="M50 49C33 48 18 37 21 23C23 13 36 13 38 22C40 29 33 32 29 27" fill="none" stroke="' + paint.primary + '" stroke-width="2" stroke-linecap="round"/>' +
      '<path d="M22 35C12 35 10 26 12 19C21 22 26 27 22 35Z" fill="' + paint.primary + '"/>' +
      '<path d="M31 42C21 49 12 43 9 36C18 34 25 35 31 42Z" fill="' + paint.accent + '"/>' +
      '<path d="M39 46C31 57 22 55 17 49C25 44 31 43 39 46Z" fill="' + paint.primary + '"/>' +
      '<path d="M22 35L15 24M30 42L15 39M38 46L24 50" fill="none" stroke="' + paint.paper + '" stroke-width=".8"/>' +
      '<path d="M43 31C39 21 43 13 50 9C55 19 52 27 43 31Z" fill="' + paint.accent + '"/>' +
      '<path d="M43 31L49 16" fill="none" stroke="' + paint.paper + '" stroke-width=".8"/>' +
      '<path d="M8 8H18M8 8V18" fill="none" stroke="' + paint.primary + '" stroke-width="1"/>' +
      '<circle cx="12" cy="12" r="1.3" fill="' + paint.accent + '"/>', 4
    ) +
      '<path d="M50 39C55 42 58 45 61 50C58 55 55 58 50 61C45 58 42 55 39 50C42 45 45 42 50 39Z" fill="' + paint.paper + '" stroke="' + paint.primary + '" stroke-width="1"/>' +
      '<circle cx="50" cy="50" r="4.3" fill="' + paint.accent + '"/>';
  }

  function tile(index) {
    const number = Number(index);
    const variant = Number.isFinite(number) ? ((Math.floor(number) % 4) + 4) % 4 : 0;
    return svg('0 0 100 100', tileFrame([rosette, quarterFlower, compass, leaves][variant]()), 'tile');
  }

  function facade() {
    return svg('0 0 300 220',
      '<path d="M20 189H280" stroke="' + paint.ink + '" stroke-width="1" opacity=".25"/>' +
      '<circle cx="241" cy="48" r="21" fill="' + paint.soft + '"/>' +
      '<path d="M34 96L61 70L118 70L135 96Z" fill="' + paint.primary + '"/>' +
      '<path d="M165 96L184 70H242L268 96Z" fill="' + paint.primary + '"/>' +
      '<path d="M44 96H125V182H44Z" fill="' + paint.accent + '"/>' +
      '<path d="M175 96H256V182H175Z" fill="' + paint.accent + '"/>' +
      '<path d="M112 83V182H188V83L150 40Z" fill="' + paint.paper + '" stroke="' + paint.primary + '" stroke-width="1.8"/>' +
      '<path d="M103 84L150 31L197 84" fill="none" stroke="' + paint.primary + '" stroke-width="5" stroke-linejoin="round"/>' +
      '<path d="M117 85L150 48L183 85" fill="none" stroke="' + paint.accent + '" stroke-width="1.4"/>' +
      '<path d="M39 95H112M188 95H261M39 102H112M188 102H261" stroke="' + paint.paper + '" stroke-width="3"/>' +
      '<circle cx="150" cy="77" r="10" fill="' + paint.primary + '"/>' +
      '<circle cx="150" cy="77" r="6.6" fill="' + paint.paper + '"/>' +
      '<path d="M150 71V83M144 77H156" stroke="' + paint.primary + '" stroke-width="1"/>' +
      '<path d="M128 182V130A22 22 0 0 1 172 130V182Z" fill="' + paint.accent + '" stroke="' + paint.primary + '" stroke-width="2"/>' +
      '<path d="M135 182V132A15 15 0 0 1 165 132V182Z" fill="' + paint.primary + '"/>' +
      '<path d="M150 118V181M138 137H162M140 145V173M160 145V173" stroke="' + paint.paper + '" stroke-width="1" opacity=".55"/>' +
      '<circle cx="146" cy="158" r="1.5" fill="' + paint.paper + '"/><circle cx="154" cy="158" r="1.5" fill="' + paint.paper + '"/>' +
      '<path d="M59 151V125A16 16 0 0 1 91 125V151Z M209 151V125A16 16 0 0 1 241 125V151Z" fill="' + paint.paper + '"/>' +
      '<path d="M64 147V126A11 11 0 0 1 86 126V147Z M214 147V126A11 11 0 0 1 236 126V147Z" fill="' + paint.primary + '"/>' +
      '<path d="M75 115V148M64 128H86M64 135H86M64 142H86M225 115V148M214 128H236M214 135H236M214 142H236" stroke="' + paint.paper + '" stroke-width=".9" opacity=".7"/>' +
      '<path d="M55 153H95M205 153H245" stroke="' + paint.primary + '" stroke-width="3"/>' +
      '<path d="M44 173H112M188 173H256" stroke="' + paint.paper + '" stroke-width="2"/>' +
      '<path d="M124 182H176V187H124Z" fill="' + paint.primary + '"/>' +
      '<path d="M118 187H182V191H118Z" fill="' + paint.soft + '"/>' +
      '<path d="M28 181Q30 137 20 113M28 153C12 146 9 135 12 128C26 134 30 142 28 153Z M27 163C41 155 45 141 40 133C29 142 25 153 27 163Z" fill="' + paint.primary + '" stroke="' + paint.primary + '" stroke-width="1.2"/>' +
      '<path d="M18 176H39L35 190H22Z" fill="' + paint.accent + '"/>' +
      '<path d="M270 182Q268 162 276 148M272 170C261 165 259 157 262 152C271 157 273 164 272 170Z M272 162C282 160 287 151 285 145C276 149 272 155 272 162Z" fill="' + paint.primary + '" stroke="' + paint.primary + '" stroke-width="1"/>' +
      '<path d="M263 177H282L279 190H266Z" fill="' + paint.accent + '"/>', 'facade'
    );
  }

  function botanical() {
    const leaves = [
      ['M150 171C118 175 91 157 93 134C122 135 145 149 150 171Z', 'M100 141L150 171'],
      ['M150 155C173 153 198 134 198 112C171 115 153 132 150 155Z', 'M190 120L150 155'],
      ['M145 132C119 131 103 114 106 91C132 97 145 113 145 132Z', 'M112 100L145 132'],
      ['M144 114C167 111 181 92 177 72C154 80 144 95 144 114Z', 'M171 81L144 114'],
      ['M147 91C125 84 119 64 128 47C146 58 152 73 147 91Z', 'M130 56L147 91'],
      ['M151 73C171 66 178 47 168 31C153 41 146 57 151 73Z', 'M166 40L151 73']
    ].map(function (leaf, index) {
      return '<path d="' + leaf[0] + '" fill="' + (index % 2 ? paint.primary : paint.accent) + '"/>' +
        '<path d="' + leaf[1] + '" fill="none" stroke="' + paint.paper + '" stroke-width="1.1" opacity=".8"/>';
    }).join('');
    return svg('0 0 300 220',
      '<circle cx="151" cy="110" r="79" fill="' + paint.soft + '" opacity=".45"/>' +
      '<path d="M100 202H200" stroke="' + paint.ink + '" stroke-width=".7" opacity=".3"/>' +
      '<path d="M150 200C158 164 135 123 148 83C152 68 162 50 167 37" fill="none" stroke="' + paint.primary + '" stroke-width="2" stroke-linecap="round"/>' + leaves +
      '<path d="M151 195C124 188 105 178 83 154C69 139 64 115 66 93M151 195C182 187 205 173 220 147C228 132 233 114 231 96" fill="none" stroke="' + paint.primary + '" stroke-width="1.1"/>' +
      '<path d="M81 153C64 154 48 143 48 130C65 132 76 140 81 153Z M72 135C58 129 54 115 59 105C71 113 74 123 72 135Z M67 114C77 107 79 94 73 85C65 95 63 105 67 114Z M95 166C93 149 101 139 111 137C113 151 107 161 95 166Z" fill="' + paint.primary + '" opacity=".7"/>' +
      '<path d="M219 150C235 149 248 139 248 126C232 130 222 139 219 150Z M227 131C217 121 217 109 224 101C234 111 233 122 227 131Z M232 110C244 104 248 92 243 82C232 89 229 99 232 110Z M205 168C208 151 202 139 191 136C186 151 192 163 205 168Z" fill="' + paint.accent + '" opacity=".85"/>' +
      '<circle cx="66" cy="88" r="3.2" fill="' + paint.accent + '"/><circle cx="231" cy="91" r="3" fill="' + paint.primary + '"/>' +
      '<path d="M83 58V66M79 62H87M214 59V67M210 63H218" stroke="' + paint.accent + '" stroke-width="1"/>' +
      '<circle cx="200" cy="37" r="1.5" fill="' + paint.primary + '"/><circle cx="96" cy="102" r="1.5" fill="' + paint.primary + '"/>', 'botanical'
    );
  }

  function chart() {
    const waves = Array.from({ length: 5 }, function (_, index) {
      const y = 143 + index * 12;
      return '<path d="M24 ' + y + 'Q37 ' + (y - 8) + ' 50 ' + y + 'T76 ' + y + 'T102 ' + y + 'T128 ' + y + 'T154 ' + y + 'T180 ' + y + 'T206 ' + y + 'T232 ' + y + 'T258 ' + y + 'T284 ' + y + '" fill="none" stroke="' + (index % 2 ? paint.accent : paint.primary) + '" stroke-width="' + (index === 0 ? 1.5 : .9) + '" opacity="' + (1 - index * .13) + '"/>';
    }).join('');
    return svg('0 0 300 220',
      '<circle cx="150" cy="85" r="56" fill="' + paint.soft + '" opacity=".55"/>' +
      '<circle cx="150" cy="85" r="48" fill="none" stroke="' + paint.primary + '" stroke-width=".8"/>' +
      '<circle cx="150" cy="85" r="41" fill="none" stroke="' + paint.primary + '" stroke-width=".6" stroke-dasharray="1 5.44"/>' +
      '<path d="M150 18V31M150 139V152M83 85H96M204 85H217M108 43L115 50M185 120L192 127M108 127L115 120M185 50L192 43" stroke="' + paint.primary + '" stroke-width="1"/>' +
      '<path d="M150 34L161 74L201 85L161 96L150 136L139 96L99 85L139 74Z" fill="' + paint.primary + '"/>' +
      '<path d="M150 34V85L161 74Z M201 85H150L161 96Z M150 136V85L139 96Z M99 85H150L139 74Z" fill="' + paint.accent + '"/>' +
      '<path d="M119 54L150 75L181 54L160 85L181 116L150 95L119 116L140 85Z" fill="' + paint.paper + '" stroke="' + paint.primary + '" stroke-width="1"/>' +
      '<path d="M150 63L156 79L172 85L156 91L150 107L144 91L128 85L144 79Z" fill="' + paint.primary + '"/>' +
      '<circle cx="150" cy="85" r="6" fill="' + paint.paper + '" stroke="' + paint.accent + '" stroke-width="1.5"/>' +
      '<circle cx="150" cy="85" r="1.5" fill="' + paint.primary + '"/>' +
      '<path d="M29 83C38 72 49 72 58 82C67 72 78 72 87 83M217 109C225 101 233 101 241 109C249 101 257 101 265 109" fill="none" stroke="' + paint.accent + '" stroke-width="1.2" stroke-linecap="round"/>' +
      '<path d="M40 51H69M54.5 37V65" stroke="' + paint.primary + '" stroke-width=".7" opacity=".5"/>' +
      '<circle cx="54.5" cy="51" r="8" fill="none" stroke="' + paint.primary + '" stroke-width=".7"/>' +
      '<path d="M238 38V52M231 45H245" stroke="' + paint.accent + '" stroke-width="1"/>' +
      '<circle cx="263" cy="67" r="2" fill="' + paint.primary + '"/>' + waves,
      'chart'
    );
  }

  window.StudyArt = Object.freeze({ tile: tile, facade: facade, botanical: botanical, chart: chart });
}());
