"""Extract two teaching figures from the 19 August 2026 draft of SLP ch. 15.

The input book is not copied into this repository. Crops preserve the source
vector graphics and the spectrogram's embedded image; Ghostscript removes
content outside the visible page. See README.md for attribution.
"""

from pathlib import Path
import argparse
import subprocess
import tempfile

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject


DEFAULT_SOURCE = Path("/mnt/c/Users/rodri/Zotero/storage/VKDA3U4Q/15.pdf")
# Coordinates in points from the top-left of the original 612 × 792 pt page.
CROPS = [
    ("jurafsky-wave", 15, (118.0, 462.0, 478.0, 557.0)),
    ("jurafsky-spectrogram", 19, (148.0, 125.0, 445.0, 228.0)),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, nargs="?", default=DEFAULT_SOURCE)
    args = parser.parse_args()
    destination = Path(__file__).resolve().parent
    reader = PdfReader(args.source)
    with tempfile.TemporaryDirectory(prefix="jurafsky-crops-") as temporary:
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
