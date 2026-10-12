# Figuras para la guía de papers

Usadas en [intuicion-papers.md](../../intuicion-papers.md). Revisadas visualmente el 12/10/2026.

- **robust-soap-intuicion**, **kosmos-intuicion**, **ascribe-intuicion**: esquemas propios SVG y PNG, con ejemplos ficticios en español. Elaboración a partir de los métodos citados; no son figuras ni resultados originales del artículo. No se generaron con IA raster.
- **robust-soap-figure1-original.pdf/png**: figura 1 original de [Latif et al., CHIL 2026, PMLR 333, p. 452](https://proceedings.mlr.press/v333/latif26a.html), copyright de los autores. Recorte del diagrama sin alterar textos, flechas o resultados; no se incluye el párrafo largo del pie. PDF vectorial y PNG de 2400 píxeles de ancho. Es una figura distinta de SCRIBE/Wang que aparece en la presentación.

Los PDFs completos de los artículos no se copiaron al repositorio. `extract_robust_figure.py` usa el ejemplar local de Zotero y Ghostscript elimina el contenido fuera del recorte. `create_figures.py` reproduce los SVG; los PNG se exportaron con Inkscape, por ejemplo:

```bash
python3 create_figures.py
inkscape kosmos-intuicion.svg --export-type=png --export-width=1800 --export-filename=kosmos-intuicion.png
```

Fuentes primarias: [Robust SOAP](https://proceedings.mlr.press/v333/latif26a.html), [KOSMOS](https://doi.org/10.3390/info17040355) y [código](https://github.com/ryanwaynehenry/KOSMOS), [ASCRIBE](https://arxiv.org/abs/2610.01234) y [prompts](https://github.com/loolootech/ascribe/tree/main/prompts). Los ejemplos sirven para comprender el mecanismo y no son recomendaciones de tratamiento.
