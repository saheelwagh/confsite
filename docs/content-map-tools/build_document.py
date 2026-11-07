import json
import math
import re
from pathlib import Path
from PIL import Image
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

WORK=Path(__file__).parent
OUTPUT=Path('/Users/saheelwagh/coding/hackathon/confsite/docs/ACBLPE-2027-Site-Content-and-Visual-Map.docx')
data=json.loads((WORK/'inventory.json').read_text())
doc=Document()
section=doc.sections[0]
section.page_width=Inches(8.5)
section.page_height=Inches(11)
section.top_margin=Inches(.68)
section.bottom_margin=Inches(.65)
section.left_margin=Inches(.7)
section.right_margin=Inches(.7)
section.header_distance=Inches(.26)
section.footer_distance=Inches(.28)

styles=doc.styles
for name in ['Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3','Caption']:
    styles[name].font.name='Arial'
    styles[name].font.color.rgb=RGBColor(0,0,0)
    styles[name].paragraph_format.line_spacing=1.08
styles['Normal'].font.size=Pt(11)
styles['Normal'].paragraph_format.space_after=Pt(5)
styles['Title'].font.size=Pt(29)
styles['Title'].font.bold=True
styles['Title'].paragraph_format.space_after=Pt(12)
for style_name in ['Title','Subtitle']:
    for border in list(styles[style_name]._element.iter(qn('w:pBdr'))):
        border.getparent().remove(border)
    styles[style_name].font.underline=False
styles['Subtitle'].font.size=Pt(15)
for name,size,before,after in [('Heading 1',22,18,12),('Heading 2',16,15,8),('Heading 3',12,10,5)]:
    styles[name].font.size=Pt(size)
    styles[name].font.bold=True
    styles[name].paragraph_format.space_before=Pt(before)
    styles[name].paragraph_format.space_after=Pt(after)
    styles[name].paragraph_format.keep_with_next=True
for name,size,bold in [('Map block',10.5,True),('Map note',10,False),('Correction',10.5,False)]:
    style=styles.add_style(name,1)
    style.base_style=styles['Normal']
    style.font.name='Arial'
    style.font.size=Pt(size)
    style.font.bold=bold
    style.font.color.rgb=RGBColor(0,0,0)
    style.paragraph_format.space_after=Pt(3)
styles['Map block'].paragraph_format.space_before=Pt(6)
styles['Map block'].paragraph_format.keep_with_next=True
styles['Map note'].font.color.rgb=RGBColor.from_string('4E5663')
styles['Caption'].font.size=Pt(10)

header=section.header.paragraphs[0]
header.text='ACBLPE 2027   Site content and visual map'
header.runs[0].font.name='Arial'
header.runs[0].font.size=Pt(9)
header.runs[0].font.color.rgb=RGBColor(0,0,0)
footer=section.footer.paragraphs[0]
footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
footer.add_run('Page ').font.size=Pt(9)
field=OxmlElement('w:fldSimple')
field.set(qn('w:instr'),'PAGE')
footer._p.append(field)

text_count=0
image_count=0
def para(text='',style=None,indent=0):
    p=doc.add_paragraph(text,style)
    p.paragraph_format.left_indent=Inches(min(indent,5)*.15)
    return p

def text_item(text,role,depth=0):
    global text_count
    text_count+=1
    rolep=para(role,'Map note',depth)
    rolep.paragraph_format.keep_with_next=True
    p=para(indent=depth)
    p.add_run('existing content : ').bold=True
    p.add_run(text)
    p.paragraph_format.keep_with_next=True
    p.paragraph_format.space_after=Pt(3)
    p=para('Corrected text (if any):','Correction',depth)
    p.paragraph_format.keep_with_next=True
    p=para('',indent=depth)
    p.paragraph_format.space_after=Pt(6)
    p.paragraph_format.line_spacing=1
    p.paragraph_format.keep_with_next=False
    p.add_run(' ').font.size=Pt(11)

def meaningful(nodes):
    out=[]
    for node in nodes:
        if node['kind']=='block' and node['label']=='Block':out.extend(meaningful(node.get('children',[])))
        else:out.append(node)
    return out

def render_nodes(nodes,depth=0,prefix=''):
    global image_count
    for index,node in enumerate(meaningful(nodes),1):
        path=f'{prefix}.{index}' if prefix else str(index)
        kind=node['kind']
        if kind=='block':
            para(f'{path}  {node["label"]}','Map block',depth)
            if node.get('note'):para(node['note'],'Map note',depth)
            render_nodes(node.get('children',[]),depth+1,path)
        elif kind=='text':text_item(node['text'],f'{path}  {node["label"]}',depth)
        elif kind=='image':
            image_count+=1
            p=para(indent=depth)
            p.add_run(f'{path}  Image  ').bold=True
            p.add_run(node['label'])
            p.paragraph_format.keep_with_next=True
            para(f'Image source: {node.get("source","Inline SVG")}', 'Map note',depth)
            if node.get('note'):para(node['note'],'Map note',depth)
        else:
            para(f'{path}  {node["label"]}','Map block',depth)
            para(node.get('note',''),'Map note',depth)

def chapter(title):
    p=doc.add_heading(title,level=1)
    p.paragraph_format.page_break_before=True

def table(headers,rows,widths):
    t=doc.add_table(rows=1,cols=len(headers))
    t.autofit=False
    for c,w in zip(t.columns,widths):c.width=Inches(w)
    for c,s in zip(t.rows[0].cells,headers):c.text=s
    for row in rows:
        for c,s in zip(t.add_row().cells,row):c.text=str(s)
    for ri,row in enumerate(t.rows):
        for ci,c in enumerate(row.cells):
            c.width=Inches(widths[ci])
            tcpr=c._tc.get_or_add_tcPr()
            borders=OxmlElement('w:tcBorders')
            for edge in ['top','left','bottom','right']:
                e=OxmlElement('w:'+edge)
                for k,v in [('val','single'),('sz','4'),('color','D9D9D9')]:e.set(qn('w:'+k),v)
                borders.append(e)
            tcpr.append(borders)
            margins=OxmlElement('w:tcMar')
            for edge in ['top','left','bottom','right']:
                e=OxmlElement('w:'+edge);e.set(qn('w:w'),'100');e.set(qn('w:type'),'dxa');margins.append(e)
            tcpr.append(margins)
            shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'17365D' if ri==0 else ('F3F6FA' if ri%2==0 else 'FFFFFF'));tcpr.append(shade)
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(0)
                for r in p.runs:r.font.size=Pt(10);r.font.bold=ri==0;r.font.color.rgb=RGBColor.from_string('FFFFFF' if ri==0 else '000000')
    repeat=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(repeat)
    return t

doc.add_paragraph('ACBLPE 2027 Site Content and Visual Map','Title')
doc.add_paragraph('Content review workbook','Subtitle')
para('Content updated from the local site source on 7 November 2026')
para('This workbook maps every published page to its components, nested blocks, text and images. Use the blank space after each text item to enter a correction. Existing wording is reproduced without editorial changes. Header and footer content appears once under common components.')
para('The visual map follows the complete content map. Each page is shown in site order at desktop, tablet and mobile widths. Long components continue across numbered image parts. Screenshots reflect the current local site preview. Browser controls and the floating duplicate section tracker are omitted.')
doc.add_heading('Site scope',level=1)
table(['Page','Route','Main components'],[(p['name'],p['route'],len(p['components'])) for p in data['pages']],[2.1,2.7,2.3])
p=para('The root route / redirects to /landing and has no separate page content. Navigation and footer are common to all five pages. Font loading and document head resources are infrastructure rather than visible content blocks.','Map note')
p.paragraph_format.space_before=Pt(7)
doc.add_heading('Reading the map',level=1)
para('The hierarchy runs from page to component to block and finally to a text item or image. The numbered paths preserve nesting and order. Link destinations and image sources are recorded as supporting details. Accessible labels are included even when they are not visible in the default screenshot.')
para('All correction areas are intentionally blank. Text casing follows the source content rather than CSS uppercase styling. Decorative arrows and icons are listed as imagery instead of editable wording. The Upcoming timeline label is time dependent.')

chapter('Content map')
para('Pages appear in navigation order, followed by the call for papers page. Shared header and footer content follows the page maps.')
codes=['L','R','P','V','C']
for page,code in zip(data['pages'],codes):
    if code=='L':doc.add_heading(page['name']+' page',level=1)
    else:chapter(page['name']+' page')
    para('Route: '+page['route'],'Map note')
    doc.add_heading('Page metadata',level=2)
    text_item(page['title'],'Browser title')
    text_item(page['description'],'Meta description')
    para('Infrastructure: LandingFonts loads the shared Inter and Libre Baskerville font faces. SectionTracker repeats the active section label while scrolling; its common behavior is mapped after the footer.','Map note')
    for i,component in enumerate(page['components'],1):
        doc.add_heading(f'{code}{i:02d} {component["name"]}',level=2)
        render_nodes(component['tree'])
        if component['name']=='RegistrationFees':
            text_item('Conference registration fees','Accessible table label')
        if component['name']=='ReviewPresentationGuidance':
            text_item('Accepted abstract languages','Accessible language list label')

chapter('Common components')
para('These components are shared across all published pages and are excluded from the individual page maps above.')
for component in data['common']:
    doc.add_heading(component['name'],level=2)
    render_nodes(component['tree'])
    if component['name']=='Navigation':text_item('Main navigation','Accessible navigation label')
doc.add_heading('SectionTracker',level=2)
text_item('Current section','Accessible region label')
para('Displays a duplicate of the number and label from the current SectionLabel. All possible label values are already mapped inside their page components. It adds no independent visible copy.','Map note')
doc.add_heading('SectionLabel',level=2)
para('A reusable section number, rule and label. Its actual text values are listed at every usage in the page map. The rule is decorative.','Map note')
doc.add_heading('AzulejoFlipCard and AzulejoTileArtwork',level=2)
para('The landing page date and Goa cards use an ornamental SVG face and a quiet bordered content face. Text and icons remain HTML over SVG. The cards reveal content on entry and return to ornament on exit. Reduced motion shows content immediately. Both card instances and their images are mapped under Satellite and ConferenceVenue.','Map note')
doc.add_heading('Document head resources',level=2)
para('Image source: /favicon.svg with /favicon.ico as the fallback favicon. These small browser icons are shared by all pages.','Map note')

# Screenshots are split only when necessary to keep the rendered text readable.
(WORK/'slices').mkdir(exist_ok=True)
visual_parts=[]
def split_image(record):
    image=Image.open(record['file']).convert('RGB')
    width,height=image.size
    display_width=3.3 if record['device']=='Mobile' else 7.0
    max_height=7.75
    max_px=int(width*max_height/display_width)
    # A modest reduction avoids a separate page for only a trailing margin.
    if height<=max_px*1.16:
        display_width=min(display_width,width*max_height/height)
        max_px=height
    count=math.ceil(height/max_px)
    result=[];top=0
    while top<height:
        remaining_parts=count-len(result)
        bottom=height if remaining_parts==1 else round(top+(height-top)/remaining_parts)
        if bottom<height:
            # DOM text line boxes protect both columns from being sliced through.
            bands=record.get('textBands',[])
            protected=bands+record.get('keepTogether',[])
            candidates=range(max(top+100,bottom-250),min(top+max_px,bottom+250,height-100))
            safe=[y for y in candidates if all(not lo<=y<=hi for lo,hi in protected)]
            if safe:bottom=min(safe,key=lambda y:abs(y-bottom))
        path=WORK/'slices'/f'{Path(record["file"]).stem}-part-{len(result)+1}.png'
        image.crop((0,top,width,bottom)).save(path)
        result.append((path,display_width,width,bottom-top,top,bottom))
        top=bottom
    return result

chapter('Visual map')
para('Screenshots are ordered by page, then desktop 1440 by 1000 pixels, tablet 768 by 1024 pixels and mobile 390 by 844 pixels. Within each device size, components follow their order on the page. Screenshot heights expand to include the full component. Shared Navigation and MinimalFooter screenshots appear separately at the end.')
para('Screenshots use reduced motion, a hidden duplicate section tracker, and an unpinned abstract introduction.','Map note')

for page in data['pages']:
    for device,viewport_width,viewport_height in data['viewports']:
        records=[r for r in data['screenshots'] if r['page']==page['name'] and r['device']==device and not r['common']]
        for record in records:
            parts=split_image(record)
            for index,(path,display_width,w,h,top,bottom) in enumerate(parts,1):
                p=doc.add_heading(page['name']+' page '+device.lower(),level=2)
                p.paragraph_format.page_break_before=True
                doc.add_heading(record['component'],level=3)
                info=f'Route /{record["route"]}  |  Viewport {viewport_width} × {viewport_height} px'
                if record.get('pending'):info+='  |  Updated screenshot pending local preview'
                if len(parts)>1:info+=f'  |  Part {index} of {len(parts)}'
                p=para(info,'Caption');p.paragraph_format.keep_with_next=True
                p=para()
                p.alignment=WD_ALIGN_PARAGRAPH.CENTER
                run=p.add_run();shape=run.add_picture(str(path),width=Inches(display_width))
                shape._inline.docPr.set('descr',f'{page["name"]} page {record["component"]} at {device.lower()} width {viewport_width} pixels'+(f' part {index} of {len(parts)}' if len(parts)>1 else ''))
                p.paragraph_format.space_after=Pt(0)
                p.paragraph_format.line_spacing=1
                visual_parts.append({'page':page['name'],'device':device,'component':record['component'],'part':index,'parts':len(parts),'file':str(path)})

for device,viewport_width,viewport_height in data['viewports']:
    for record in [r for r in data['screenshots'] if r['common'] and r['device']==device]:
        p=doc.add_heading('Common components '+device.lower(),level=2)
        p.paragraph_format.page_break_before=True
        doc.add_heading(record['component'],level=3)
        p=para(f'Shared by all pages  |  Viewport {viewport_width} × {viewport_height} px','Caption');p.paragraph_format.keep_with_next=True
        p=para();p.alignment=WD_ALIGN_PARAGRAPH.CENTER
        shape=p.add_run().add_picture(record['file'],width=Inches(3.3 if device=='Mobile' else 7.0))
        shape._inline.docPr.set('descr',f'Shared {record["component"]} at {device.lower()} width {viewport_width} pixels')
        visual_parts.append({'page':'Common','device':device,'component':record['component'],'part':1,'parts':1,'file':record['file']})

doc.core_properties.title='ACBLPE 2027 Site Content and Visual Map'
doc.core_properties.subject='Whole site content review workbook and responsive component screenshots'
doc.core_properties.author=''
doc.core_properties.keywords='ACBLPE 2027, content map, visual map, review'
OUTPUT.parent.mkdir(exist_ok=True)
doc.save(OUTPUT)
(WORK/'visual-parts.json').write_text(json.dumps(visual_parts,indent=2))
(WORK/'build-summary.json').write_text(json.dumps({'textItems':text_count,'mappedImages':image_count,'screenshots':len(data['screenshots']),'visualPages':len(visual_parts),'output':str(OUTPUT)},indent=2))
print(json.dumps({'textItems':text_count,'mappedImages':image_count,'screenshots':len(data['screenshots']),'visualPages':len(visual_parts),'output':str(OUTPUT)},indent=2))
