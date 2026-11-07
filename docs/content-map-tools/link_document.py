import json
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

WORK=Path(__file__).parent
SOURCE=Path('/Users/saheelwagh/coding/hackathon/confsite/docs/ACBLPE-2027-Site-Content-and-Visual-Map.docx')
OUTPUT=SOURCE.with_name(SOURCE.stem+'-Linked.docx')
inventory=json.loads((WORK/'inventory.json').read_text())
parts=json.loads((WORK/'visual-parts.json').read_text())
doc=Document(SOURCE)

components={}
for code,page in zip(['L','R','P','V','C'],inventory['pages']):
    for i,component in enumerate(page['components'],1):
        components[f'{code}{i:02d} {component["name"]}']=(page['name'],component['name'])
for name in ['Navigation','MinimalFooter']:components[name]=('Common',name)

content={}
screenshots=[]
visual=False
for p in doc.paragraphs:
    if p.text=='Visual map' and p.style.name=='Heading 1':visual=True
    if not visual and p.style.name=='Heading 2' and p.text in components:
        content[components[p.text]]=p
    elif visual and p.style.name=='Heading 3':screenshots.append(p)
assert len(content)==23, len(content)
assert len(screenshots)==len(parts), (len(screenshots),len(parts))
for p,part in zip(screenshots,parts):assert p.text==part['component'],(p.text,part)

existing_ids=[int(e.get(qn('w:id'))) for e in doc._element.iter(qn('w:bookmarkStart'))]
bookmark_id=max(existing_ids,default=0)+1
def bookmark(p,name):
    global bookmark_id
    start=OxmlElement('w:bookmarkStart');start.set(qn('w:id'),str(bookmark_id));start.set(qn('w:name'),name)
    end=OxmlElement('w:bookmarkEnd');end.set(qn('w:id'),str(bookmark_id))
    bookmark_id+=1
    ppr=p._p.find(qn('w:pPr'))
    p._p.insert(1 if ppr is not None else 0,start)
    p._p.append(end)

def link(p,text,anchor,tooltip):
    hyperlink=OxmlElement('w:hyperlink')
    hyperlink.set(qn('w:anchor'),anchor)
    hyperlink.set(qn('w:history'),'1')
    hyperlink.set(qn('w:tooltip'),tooltip)
    run=OxmlElement('w:r');props=OxmlElement('w:rPr')
    for tag,attrs in [
        ('rFonts',{'ascii':'Arial','hAnsi':'Arial'}),
        ('color',{'val':'214CB5'}),('u',{'val':'single'}),
        ('sz',{'val':'19'}),('szCs',{'val':'19'}),('b',{'val':'0'}),
    ]:
        el=OxmlElement('w:'+tag)
        for key,value in attrs.items():el.set(qn('w:'+key),value)
        props.append(el)
    run.append(props)
    t=OxmlElement('w:t');t.text=text;run.append(t)
    hyperlink.append(run)
    p._p.append(hyperlink)

def gap(p,text='   '):
    run=p.add_run(text)
    from docx.shared import Pt
    run.font.size=Pt(9.5)
    run.bold=False

text_anchors={}
shot_anchors={}
for i,(key,p) in enumerate(content.items(),1):
    anchor=f'cm_text_{i:02d}'
    bookmark(p,anchor)
    text_anchors[key]=anchor

for i,(p,part) in enumerate(zip(screenshots,parts),1):
    key=(part['page'],part['component'])
    assert key in text_anchors,key
    anchor=f'cm_shot_{i:03d}'
    bookmark(p,anchor)
    shot_anchors.setdefault((key,part['device']),anchor)
    gap(p)
    link(p,'edit text',text_anchors[key],f'Edit {part["page"]} {part["component"]} text')

for key,p in content.items():
    for device in ['Desktop','Tablet','Mobile']:
        gap(p)
        link(p,f'view screenshot ({device.lower()})',shot_anchors[(key,device)],f'View {key[0]} {key[1]} {device.lower()} screenshot')

assert len(doc.inline_shapes)==len(parts)
assert sum(p.text=='Corrected text (if any):' for p in doc.paragraphs)>0
doc.save(OUTPUT)

# Audit every link target and every component/device pairing in the saved OOXML.
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with ZipFile(OUTPUT) as z:
    root=etree.fromstring(z.read('word/document.xml'))
    names=root.xpath('//w:bookmarkStart/@w:name',namespaces=ns)
    ids=root.xpath('//w:bookmarkStart/@w:id',namespaces=ns)
    links=root.xpath('//w:hyperlink',namespaces=ns)
    missing=[h.get(qn('w:anchor')) for h in links if h.get(qn('w:anchor')) not in names]
    assert not missing,missing
    assert len(names)==len(set(names)), 'Duplicate bookmark names'
    assert len(ids)==len(set(ids)), 'Duplicate bookmark IDs'
    assert len(links)==len(shot_anchors)+len(parts),len(links)
    assert all(int(s.get(qn('w:sz'),'19'))==19 for h in links for s in h.iter(qn('w:sz')))

summary={'componentsLinked':len(content),'screenshotViewsLinked':len(shot_anchors),'viewScreenshotLinks':len(shot_anchors),'editTextLinks':len(parts),'brokenLinks':missing,'output':str(OUTPUT)}
(WORK/'link-audit.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
