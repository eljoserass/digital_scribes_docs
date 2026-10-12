"""Extract unchanged figure 1 panels from Wang et al., npj Digital Medicine 2025.

The input article is not copied into this repository. Crops preserve the
original figure text and vector graphics; Ghostscript removes content outside
the visible page. See README.md for attribution.
"""

from pathlib import Path
import argparse
import subprocess
import tempfile

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject


DEFAULT_SOURCE = Path("/mnt/c/Users/rodri/Zotero/storage/GBPDBELQ/Wang et al. - 2025 - An evaluation framework for ambient digital scribing tools in clinical applications.pdf")
# Coordinates in points from the top-left of the original 595.276 × 790.866 pt page.
CROPS = [
    ("scribe-figure1a", 3, (57, 47, 543, 330)),
    ("scribe-figure1b", 3, (57, 344, 444, 641)),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, nargs="?", default=DEFAULT_SOURCE)
    args = parser.parse_args()
    destination = Path(__file__).resolve().parent
    reader = PdfReader(args.source)
    with tempfile.TemporaryDirectory(prefix="scribe-figure-crops-") as temporary:
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
