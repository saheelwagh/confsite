import asyncio
import json
import sys
from pathlib import Path
from playwright.async_api import async_playwright

WORK = Path(__file__).parent
BASE = 'http://localhost:4321'
PAGES = [
    ('Landing', 'landing', [('Hero', '.conference-hero'), ('AboutACBLPE', '.about-acblpe'), ('Satellite', '.satellite'), ('ConferenceVenue', '.conference-venue'), ('KeynoteIntro', '.keynote-intro'), ('Timeline', '.timeline'), ('AzulejoArtwork', '.azulejo-artwork')]),
    ('Registration', 'registration', [('RegistrationFees', '.registration-fees'), ('RegistrationNotice', '#registration-notice'), ('AzulejoArtwork', '.azulejo-artwork')]),
    ('People', 'people', [('OrganisationCommittee', '.organisation-section'), ('ScientificCommittee', '.scientific-committee'), ('AzulejoArtwork', '.azulejo-artwork')]),
    ('Venue', 'venue', [('AboutGoa', '.about-goa'), ('ThingsToDo', '.things-to-do'), ('ReachingGoaUniversity', '.reaching-goa'), ('AzulejoArtwork', '.azulejo-artwork')]),
    ('Call for Papers', 'call-for-papers', [('CallForPapersHero', '.papers-hero'), ('SubmissionInstructions', '.submission-instructions'), ('ReviewPresentationGuidance', '.review-guidance'), ('AzulejoArtwork', '.azulejo-artwork')]),
]
VIEWPORTS = [('Desktop', 1440, 1000), ('Tablet', 768, 1024), ('Mobile', 390, 844)]

EXTRACT = r'''root => {
  const clean = s => s.replace(/\s+/g, ' ').trim();
  const names = {
    'hero-meta':'Conference status and location', 'hero-footer':'Introduction and actions',
    'hero-actions':'Call to action buttons', 'about-copy':'Association description',
    'satellite-introduction':'Conference introduction', 'satellite-date':'SatelliteDatePanel',
    'location-card':'Goa location card', 'location-meta':'Region and compass',
    'venue-details':'Venue details', 'speaker-grid':'Speaker list', 'speaker-card':'Speaker',
    'milestones':'Milestone list', 'milestone':'Milestone', 'organisations':'Organising institutions',
    'organising-committee':'Organising committee', 'members':'Scientific committee members',
    'proposal-notice':'Proposal notice', 'fees-copy':'Fee introduction and inclusions',
    'fee-table':'Registration fee table', 'text-fields':'Text input fields', 'field':'Form field',
    'category-field':'Participant category field', 'facts':'Goa facts', 'fact':'Fact card',
    'activities':'Activities list', 'connections':'Travel connections', 'transport-group':'Transport category',
    'instruction-list':'Abstract checklist', 'instruction':'Checklist item',
    'instructions-introduction':'Abstract guidance introduction', 'checklist-note':'Submission reminder',
    'criteria':'Review criteria', 'criterion':'Review criterion', 'language-guidance':'Language guidance',
    'languages':'Accepted languages', 'session-card':'Session timing card',
    'session-breakdown':'Timing breakdown', 'session-part':'Session part',
    'conference':'Conference identity', 'organisers':'Organiser credit', 'navigation-links':'Navigation links',
    'tile-ornament':'Ornamental face', 'tile-content':'Content face', 'tile-border':'Decorative content border',
  };
  const transparent = new Set(['content','hero-content','about-layout','about-heading','satellite-layout','venue-content','venue-layout','keynote-content','timeline-content','organisation-layout','fees-layout','form-layout','form-introduction','instructions-content','instructions-layout','guidance-content','presentation-layout','section-helper','landing-label','responsive-label','footer-content','tile-turn','tile-writing']);
  const label = el => {
    if (el.matches('azulejo-flip-card')) return 'AzulejoFlipCard';
    if (el.matches('[data-section-label]')) return 'SectionLabel';
    for (const c of el.classList) if (names[c]) return names[c];
    return ({H1:'Page heading',H2:'Section heading',H3:'Subheading',H4:'Item heading',P:'Paragraph',A:'Link',BUTTON:'Button',LABEL:'Field label',INPUT:'Input',SELECT:'Select',OPTION:'Option',TIME:'Date',UL:'List',OL:'Ordered list',LI:'List item',TABLE:'Table',THEAD:'Table header',TBODY:'Table body',TR:'Row',TH:'Header cell',TD:'Fee cell',FORM:'Form',NAV:'Navigation',HEADER:'Header',FOOTER:'Footer',ARTICLE:'Card',ASIDE:'Supporting information',SPAN:'Text',DIV:'Block'})[el.tagName] || 'Block';
  };
  const textOf = el => {
    const copy = el.cloneNode(true);
    copy.querySelectorAll('svg,img,picture,script,style,.responsive-arrow,.visually-hidden,.upcoming-label').forEach(n=>n.remove());
    copy.querySelectorAll('br').forEach(n=>n.replaceWith(' '));
    return clean(copy.textContent).replace(/-\s+(?=[a-z])/g,'-');
  };
  function walk(el) {
    if (['SCRIPT','STYLE','SOURCE'].includes(el.tagName) || el.matches('section-tracker,.astro-dev-toolbar,.rule,.date-rule')) return [];
    if (el.matches('svg')) {
      const icon = el.classList.contains('azulejo-tile-artwork') ? 'AzulejoTileArtwork inline SVG' : el.closest('.location-meta') ? 'Compass inline SVG' : el.closest('.explore-link') ? 'Right arrow inline SVG' : el.closest('.accommodation') ? 'Information icon inline SVG' : 'Inline SVG icon';
      return [{kind:'image',label:icon,source:'Inline SVG in the component',note:el.getAttribute('aria-hidden') === 'true' ? 'Decorative image; hidden from assistive technology.' : ''}];
    }
    if (el.matches('picture,img')) {
      const img = el.matches('img') ? el : el.querySelector('img');
      return img ? [{kind:'image',label:img.getAttribute('alt') || 'Decorative image',source:img.getAttribute('src'),note:[...el.querySelectorAll('source')].map(s=>`${s.media}: ${s.getAttribute('srcset')}`).join('; ') || 'Alt text is empty for decorative imagery.'}] : [];
    }
    if (el.matches('input')) return [{kind:'control',label:label(el),note:`Type: ${el.type}; name: ${el.name}; initial value: blank; ${el.required ? 'required' : 'optional'}.`}];
    let children=[];
    const aggregate = el.matches('h1,h2,h3,h4,p,a,button,label,option,th,td') && !el.matches('[data-section-label]') && !(el.matches('p') && el.querySelector('a'));
    if (aggregate) {
      const text=textOf(el);
      if (text) children.push({kind:'text',label:label(el),text});
      el.querySelectorAll('picture,img,svg').forEach(n=>{if(n.matches('img')&&n.closest('picture'))return;children.push(...walk(n));});
      const hidden=[...el.querySelectorAll('.visually-hidden')].map(n=>clean(n.textContent));
      for (const text of hidden) children.push({kind:'text',label:'Accessible supporting text',text});
      for (const badge of el.querySelectorAll('.upcoming-label:not([hidden])')) children.push({kind:'text',label:'Current timeline status badge',text:clean(badge.textContent)});
    } else {
      for (const node of el.childNodes) {
        if (node.nodeType===Node.TEXT_NODE && clean(node.textContent)) children.push({kind:'text',label:'Text',text:clean(node.textContent)});
        else if(node.nodeType===Node.ELEMENT_NODE)children.push(...walk(node));
      }
    }
    const style=getComputedStyle(el);
    const images=[...style.backgroundImage.matchAll(/url\(["']?([^"')]+)["']?\)/g)].map(m=>new URL(m[1],location.href).pathname);
    for (const source of images) children.unshift({kind:'image',label:'Decorative background image',source,note:'CSS background image.'});
    if(!children.length)return [];
    let note='';
    if (el.matches('a')) note=`Destination: ${el.getAttribute('href')}${el.target==='_blank' ? '; opens in a new tab' : ''}.`;
    if (el.matches('button')&&el.disabled)note='Disabled in the current site.';
    if (el.matches('option')&&el.disabled)note='Disabled default prompt.';
    if (el.matches('a')&&el.hasAttribute('aria-label'))children.push({kind:'text',label:'Accessible link label',text:el.getAttribute('aria-label')});
    if (el.matches('option')||el.matches('time')&&!el.children.length||el.matches('span')&&el.children.length===0) return children;
    if ([...el.classList].some(c=>transparent.has(c))&&!el.matches('[data-section-label]'))return children;
    if (children.length===1&&aggregate&&!note)return children;
    return [{kind:'block',label:label(el),note,children}];
  }
  return walk(root);
}'''

async def main():
    (WORK/'screenshots').mkdir(parents=True,exist_ok=True)
    inventory={'date':'7 November 2026','viewports':VIEWPORTS,'pages':[],'common':[],'screenshots':[]}
    inventory_only='--inventory-only' in sys.argv
    cuts_only='--cuts-only' in sys.argv
    if cuts_only:inventory=json.loads((WORK/'inventory.json').read_text())
    if inventory_only:inventory['screenshots']=json.loads((WORK/'inventory.json').read_text())['screenshots']
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True,args=['--disable-dev-shm-usage'])
        context=await browser.new_context(viewport={'width':1440,'height':1000},device_scale_factor=1,reduced_motion='reduce')
        page=await context.new_page()
        if cuts_only:
            for page_name,route,components in PAGES:
                for device,width,height in VIEWPORTS:
                    await page.set_viewport_size({'width':width,'height':height})
                    await page.goto(f'{BASE}/{route}',wait_until='networkidle')
                    await page.evaluate('document.fonts.ready')
                    await page.add_style_tag(content='section-tracker, astro-dev-toolbar {display:none!important} main[data-section-tracker-pinned] [data-section-label]{visibility:visible!important} .instructions-introduction{position:static!important}')
                    for name,selector in components:
                        bands=await page.locator(selector).evaluate('''root=>{const top=root.getBoundingClientRect().top;const bands=[];const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let node;while(node=walker.nextNode()){if(!node.textContent.trim()||node.parentElement.closest('svg,script,style,[hidden]'))continue;if(getComputedStyle(node.parentElement).display==='none')continue;const range=document.createRange();range.selectNodeContents(node);for(const rect of range.getClientRects())if(rect.width>1&&rect.height>1)bands.push([Math.floor(rect.top-top)-5,Math.ceil(rect.bottom-top)+5]);}return bands;}''')
                        keep_together=await page.locator(selector).evaluate('''root=>{const top=root.getBoundingClientRect().top;const ranges=[];const add=(first,last=first)=>{if(!first||!last||getComputedStyle(first).display==='none')return;const a=first.getBoundingClientRect(),b=last.getBoundingClientRect();if(b.bottom-a.top>600)return;ranges.push([Math.floor(a.top-top)+10,Math.ceil(b.bottom-top)-10]);};root.querySelectorAll('li,table tbody tr').forEach(el=>add(el));add(root.querySelector('table thead'),root.querySelector('table tbody tr:first-child'));return ranges;}''')
                        record=next(r for r in inventory['screenshots'] if r['route']==route and r['device']==device and r['component']==name)
                        record['textBands']=bands
                        record['keepTogether']=keep_together
                print(f'Checked split boundaries {page_name}',flush=True)
            (WORK/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
            await browser.close()
            return
        for page_name,route,components in PAGES:
            await page.goto(f'{BASE}/{route}',wait_until='networkidle')
            await page.evaluate('document.fonts.ready')
            entry={'name':page_name,'route':f'/{route}','title':await page.title(),'description':await page.locator('meta[name=description]').get_attribute('content'),'components':[]}
            for name,selector in components:
                tree=await page.locator(selector).evaluate(EXTRACT)
                entry['components'].append({'name':name,'selector':selector,'tree':tree})
            inventory['pages'].append(entry)
            print(f'Mapped {page_name}',flush=True)
            if route=='landing':
                for name,selector in [('Navigation','header.site-header'),('MinimalFooter','footer.minimal-footer')]:
                    inventory['common'].append({'name':name,'selector':selector,'tree':await page.locator(selector).evaluate(EXTRACT)})
            if inventory_only:
                (WORK/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
                continue
            for device,width,height in VIEWPORTS:
                await page.set_viewport_size({'width':width,'height':height})
                await page.goto(f'{BASE}/{route}',wait_until='networkidle')
                await page.evaluate('document.fonts.ready')
                # Hide the floating duplicate label, retaining the original in every section.
                await page.add_style_tag(content='section-tracker, astro-dev-toolbar {display:none!important} main[data-section-tracker-pinned] [data-section-label]{visibility:visible!important} .instructions-introduction{position:static!important} *{caret-color:transparent!important}')
                selections=components+([('Navigation','header.site-header'),('MinimalFooter','footer.minimal-footer')] if route=='landing' else [])
                for order,(name,selector) in enumerate(selections,1):
                    locator=page.locator(selector)
                    file=WORK/'screenshots'/f'{route}-{device.lower()}-{order:02d}-{name}.png'
                    await locator.screenshot(path=str(file),animations='disabled',timeout=30000)
                    box=await locator.bounding_box()
                    inventory['screenshots'].append({'page':page_name,'route':route,'device':device,'width':width,'height':height,'component':name,'order':order,'file':str(file),'box':box,'common':name in ['Navigation','MinimalFooter']})
                print(f'Captured {page_name} {device}',flush=True)
            (WORK/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
        await browser.close()
    print(f'Complete: {len(inventory["screenshots"])} screenshots',flush=True)

asyncio.run(main())
