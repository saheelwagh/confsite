"""Update the Word map source without claiming unavailable live screenshots."""

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WORK = Path(__file__).parent
SITE = Path('/Users/saheelwagh/coding/hackathon/confsite/production/src/components')
BASE_INVENTORY = WORK / 'inventory-before-site-update.json'
INVENTORY = WORK / 'inventory.json'
data = json.loads(BASE_INVENTORY.read_text())

notice_source = (SITE / 'RegistrationNotice.astro').read_text()
review_source = (SITE / 'ReviewPresentationGuidance.astro').read_text()
for exact in (
    'Registration update',
    'Registration to the conference will open soon.',
    'Kindly check the paper submission guidlines',
    '<a href="/call-for-papers">here</a>',
):
    assert exact in notice_source, exact
for exact in (
    "const languages = ['English', 'French', 'Portuguese', 'Spanish'];",
    '<h3>Accepted Langauges:</h3>',
    '<h3 id="session-title">Format</h3>',
    'Abstracts may be submitted in English, French, Portuguese or Spanish.',
    '.criterion:nth-child(2) { background: #214cb5;',
):
    assert exact in review_source, exact

registration = next(page for page in data['pages'] if page['name'] == 'Registration')
registration['description'] = 'Registration fees and opening status for the 25th ACBLPE Conference in Goa, 2027.'
form = next(component for component in registration['components'] if component['name'] == 'RegistrationForm')
form.update({
    'name': 'RegistrationNotice',
    'selector': '#registration-notice',
    'tree': [{
        'kind': 'block', 'label': 'Block', 'note': '',
        'children': [
            {'kind': 'block', 'label': 'SectionLabel', 'note': '', 'children': [
                {'kind': 'text', 'label': 'Text', 'text': '02'},
                {'kind': 'text', 'label': 'Text', 'text': 'Registration update'},
            ]},
            {'kind': 'text', 'label': 'Section heading', 'text': 'Registration to the conference will open soon.'},
            {'kind': 'block', 'label': 'Paragraph', 'note': '', 'children': [
                {'kind': 'text', 'label': 'Text', 'text': 'Kindly check the paper submission guidlines'},
                {'kind': 'block', 'label': 'Link', 'note': 'Destination: /call-for-papers.', 'children': [
                    {'kind': 'text', 'label': 'Link', 'text': 'here'},
                ]},
            ]},
        ],
    }],
})

papers = next(page for page in data['pages'] if page['name'] == 'Call for Papers')
guidance = next(component for component in papers['components'] if component['name'] == 'ReviewPresentationGuidance')

def visit(nodes):
    for node in nodes:
        yield node
        yield from visit(node.get('children', []))

nodes = list(visit(guidance['tree']))
replacements = {
    'Five languages. One scholarly conversation.': 'Accepted Langauges:',
    'Abstracts may be submitted in Creole, English, French, Portuguese or Spanish. Presentations should be delivered in the same language as the abstract, although the screen language and spoken language may differ.': 'Abstracts may be submitted in English, French, Portuguese or Spanish. Presentations should be delivered in the same language as the abstract, although the screen language and spoken language may differ.',
    'Each presenter · 30-minute session': 'Format',
}
for old, new in replacements.items():
    matches = [node for node in nodes if node.get('text') == old]
    assert len(matches) == 1, (old, len(matches))
    matches[0]['text'] = new

languages = next(node for node in nodes if node.get('kind') == 'block' and node.get('label') == 'Accepted languages')
assert [node['children'][0]['text'] for node in languages['children']] == ['Creole', 'English', 'French', 'Portuguese', 'Spanish']
languages['children'] = languages['children'][1:]
criteria = next(node for node in nodes if node.get('kind') == 'block' and node.get('label') == 'Review criteria')
assert criteria['children'][1]['children'][1]['text'] == 'Argumentation'
criteria['children'][1]['note'] = 'Blue background (#214cb5) with cream heading text, pale blue body text and a gold top border; this is the updated theme of the second criterion.'

def font(size, bold=False):
    path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf'
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()

for record in data['screenshots']:
    if record['component'] not in ('RegistrationForm', 'ReviewPresentationGuidance'):
        record['file'] = str(WORK / 'screenshots' / Path(record['file']).name)
        continue
    if record['component'] == 'RegistrationForm':
        record['component'] = 'RegistrationNotice'
    record['pending'] = True
    record['textBands'] = []
    width = record['width']
    height = 540 if width == 390 else 420
    target = WORK / 'screenshots' / f"pending-{record['route']}-{record['device'].lower()}-{record['component']}.png"
    image = Image.new('RGB', (width, height), '#fffdf8')
    draw = ImageDraw.Draw(image)
    pad = max(24, round(width * 0.055))
    draw.rectangle((pad, pad, width - pad, height - pad), outline='#9aabc0', width=2)
    draw.rectangle((pad, pad, width - pad, pad + 10), fill='#214cb5')
    title_size = 24 if width == 390 else 35
    body_size = 16 if width == 390 else 22
    lines = ['Updated screenshot', 'pending local preview']
    line_y = height * 0.34
    for line in lines:
        draw.text((pad * 1.7, line_y), line, fill='#152d53', font=font(title_size, True))
        line_y += title_size * 1.4
    supporting = ['Current wording is mapped', 'in the content section.'] if width == 390 else ['Current wording is mapped in the content section.']
    for line in supporting:
        draw.text((pad * 1.7, line_y + 14), line, fill='#586a81', font=font(body_size))
        line_y += body_size * 1.45
    image.save(target)
    record['file'] = str(target)
    record['box'] = {'x': 0, 'y': 0, 'width': width, 'height': height}

assert len([r for r in data['screenshots'] if r.get('pending')]) == 6
assert not any(node.get('text') == 'Creole' for node in visit(guidance['tree']))
INVENTORY.write_text(json.dumps(data, ensure_ascii=False, indent=2))
print('Updated content tree, six honest pending views, and source-checked CFP wording.')
