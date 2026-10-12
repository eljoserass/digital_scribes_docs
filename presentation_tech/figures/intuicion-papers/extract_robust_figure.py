"""Crop only Figure 1 of Latif et al. CHIL 2026, PMLR 333, page 452.

The complete input PDF stays outside this repository. Visible figure content
is preserved; Ghostscript removes content outside the crop before export.
"""
from pathlib import Path
import subprocess
import tempfile
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

SOURCE = Path('/mnt/c/Users/rodri/Zotero/storage/HCUJ5NDM/Latif et al. - 2026 - Evaluating Robustness of LLM-Based Ambient Scribes for SOAP Note Generation.pdf')
DEST = Path(__file__).resolve().parent
reader = PdfReader(SOURCE)
page = reader.pages[4]
height = float(page.mediabox.height)
# Top-left coordinates, points; diagram only, not the long caption.
left, top, right, bottom = 70, 86, 542, 180
page.cropbox = RectangleObject((left, height-bottom, right, height-top))
writer = PdfWriter()
writer.add_page(page)
with tempfile.TemporaryDirectory(prefix='robust-soap-figure-') as tmp:
    raw = Path(tmp) / 'raw.pdf'
    writer.write(raw)
    output = DEST / 'robust-soap-figure1-original.pdf'
    subprocess.run(['gs', '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-dUseCropBox', '-sDEVICE=pdfwrite', f'-sOutputFile={output}', str(raw)], check=True)
    subprocess.run(['pdftoppm', '-png', '-singlefile', '-scale-to', '2400', str(output), str(DEST / 'robust-soap-figure1-original')], check=True)
