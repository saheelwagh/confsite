import ctypes
import json
from pathlib import Path
from PIL import Image,ImageDraw
import pypdfium2 as pdfium
import pypdfium2.raw as raw

WORK=Path(__file__).parent
RENDER=WORK/'render-linked'
parts=json.loads((WORK/'visual-parts.json').read_text())
pdf=pdfium.PdfDocument(RENDER/'ACBLPE-2027-Site-Content-and-Visual-Map-Linked.pdf')
page_texts=[]
links=[]
empty=[]
for i,page in enumerate(pdf):
    text=page.get_textpage().get_text_range()
    page_texts.append(text)
    if len(text.splitlines())<4:empty.append(i+1)
    position=ctypes.c_int(0)
    handle=raw.FPDF_LINK()
    while raw.FPDFLink_Enumerate(page.raw,ctypes.byref(position),ctypes.byref(handle)):
        destination=raw.FPDFLink_GetDest(pdf.raw,handle)
        if destination:
            target=raw.FPDFDest_GetDestPageIndex(pdf.raw,destination)
            rect=raw.FS_RECTF()
            raw.FPDFLink_GetAnnotRect(handle,ctypes.byref(rect))
            label=page.get_textpage().get_text_bounded(rect.left,rect.bottom,rect.right,rect.top).strip()
            links.append({'page':i+1,'target':target+1,'label':label})
visual_start=next(i+1 for i,text in enumerate(page_texts) if '\nVisual map\r' in '\n'+text)
bad=[link for link in links if not 1<=link['target']<=len(pdf)]
forward=[link for link in links if link['page']<visual_start and link['target']>visual_start]
backward=[link for link in links if link['page']>visual_start and link['target']<visual_start]
assert not bad,bad
assert len(forward)>=69,len(forward)
assert len(backward)>=len(parts),len(backward)
assert not empty,empty
summary={'pages':len(pdf),'visualMapStart':visual_start,'renderedInternalLinkAreas':len(links),'forwardScreenshotLinks':len(forward),'backToTextLinks':len(backward),'invalidDestinations':bad,'emptyPages':empty}
(WORK/'linked-render-audit.json').write_text(json.dumps(summary,indent=2))
(WORK/'linked-pdf-links.json').write_text(json.dumps(links,indent=2))
print(json.dumps(summary,indent=2))

(WORK/'linked-contact-sheets').mkdir(exist_ok=True)
for start in range(0,len(pdf),16):
    sheet=Image.new('RGB',(1304,1744),'#e7e9ec')
    draw=ImageDraw.Draw(sheet)
    for offset in range(min(16,len(pdf)-start)):
        n=start+offset+1
        im=Image.open(RENDER/f'page-{n}.png').convert('RGB')
        im.thumbnail((306,396))
        x=16+(offset%4)*322;y=16+(offset//4)*432
        sheet.paste(im,(x,y+20));draw.text((x,y),f'Page {n}',fill='black')
    sheet.save(WORK/'linked-contact-sheets'/f'pages-{start+1:03d}-{min(start+16,len(pdf)):03d}.png')
