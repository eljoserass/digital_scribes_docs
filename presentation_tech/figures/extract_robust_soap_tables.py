"""Extract original tables 1 and 2 from Latif et al., CHIL 2026 (PMLR 333).

The input article is not copied into this repository. Crops preserve the
original table text and vector graphics; Ghostscript removes content outside
the visible page. See README.md for attribution.
"""

from pathlib import Path
import argparse
import subprocess
import tempfile

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject


DEFAULT_SOURCE = Path("/mnt/c/Users/rodri/Zotero/storage/HCUJ5NDM/Latif et al. - 2026 - Evaluating Robustness of LLM-Based Ambient Scribes for SOAP Note Generation.pdf")
# Coordinates in points from the top-left of the original 612 × 792 pt page.
CROPS = [
    ("robust-soap-table1", 7, (70, 88, 542, 269)),
    ("robust-soap-table2", 9, (70, 88, 542, 247)),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, nargs="?", default=DEFAULT_SOURCE)
    args = parser.parse_args()
    destination = Path(__file__).resolve().parent
    reader = PdfReader(args.source)
    with tempfile.TemporaryDirectory(prefix="robust-soap-crops-") as temporary:
        for name, number, (left, top, right, bottom) in CROPS:
            page = reader.pages[number - 1]
            height = float(page.mediabox.height)
            page.cropbox = RectangleObject((left, height - bottom, right, height - top))
            writer = PdfWriter()
            writer.add_page(page)
            raw = Path(temporary) / f"{name}.pdf"
            writer.write(raw)
            output = destination / f"{name}.pdf"
            subprocess.run([
                "gs", "-q", "-dSAFER", "-dBATCH", "-dNOPAUSE",
                "-dUseCropBox", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.7",
                f"-sOutputFile={output}", str(raw),
            ], check=True)
            subprocess.run([
                "pdftoppm", "-png", "-singlefile", "-scale-to", "1800",
                str(output), str(destination / name),
            ], check=True)
            print(f"{output.name}: figure from PDF page {number}")


if __name__ == "__main__":
    main()
