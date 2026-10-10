#!/usr/bin/env python3
"""Compila las fuentes TikZ compartidas y exporta diagramas PNG a 220 dpi."""

from pathlib import Path
import subprocess


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    figures = root / "figures"
    build = root / "build"
    build.mkdir(exist_ok=True)

    for name in ("flujo-hcis", "nota-soap"):
        job = f"{name}-standalone"
        result = subprocess.run(
            [
                "latexmk", "-silent", "-xelatex", "-interaction=nonstopmode",
                "-file-line-error", "-halt-on-error", f"-outdir={build}",
                f"{job}.tex",
            ],
            cwd=figures,
            capture_output=True,
            text=True,
        )
        (build / f"{job}-compilacion.log").write_text(
            result.stdout + result.stderr, encoding="utf-8"
        )
        if result.returncode:
            raise RuntimeError(f"Error al compilar {job}; revisar build/{job}-compilacion.log")
        subprocess.run(
            [
                "pdftoppm", "-png", "-r", "220", "-singlefile",
                str(build / f"{job}.pdf"), str(figures / name),
            ],
            check=True,
        )
        print(f"Exportados {build / (job + '.pdf')} y {figures / (name + '.png')}")


if __name__ == "__main__":
    main()
