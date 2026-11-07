import importlib.util
import sys
from pathlib import Path
import pypdfium2 as pdfium

SKILL=Path('/Users/saheelwagh/.codex/plugins/cache/openai-primary-runtime/documents/26.1104.22356/skills/documents')
spec=importlib.util.spec_from_file_location('render_docx',SKILL/'render_docx.py')
renderer=importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
renderer._resolve_soffice=lambda:'/tmp/confsite-libreoffice-mount/LibreOffice.app/Contents/MacOS/soffice'

def pdfinfo(path,**kwargs):
    pdf=pdfium.PdfDocument(path)
    w,h=pdf[0].get_size()
    return {'Pages':len(pdf),'Page size':f'{w} x {h} pts'}

def convert(path,dpi=150,output_folder=None,**kwargs):
    pdf=pdfium.PdfDocument(path)
    paths=[]
    for i in range(len(pdf)):
        image=pdf[i].render(scale=dpi/72).to_pil()
        output=Path(output_folder)/f'page0001-{i+1}.png'
        image.save(output)
        paths.append(str(output))
    return paths

# Keep the packaged DOCX renderer and LibreOffice conversion; substitute the
# available PDFium rasterizer for the otherwise unavailable Poppler utilities.
renderer.pdfinfo_from_path=pdfinfo
renderer.convert_from_path=convert
renderer.main()
