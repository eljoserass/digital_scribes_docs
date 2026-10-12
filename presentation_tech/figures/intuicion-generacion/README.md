# Figuras de generación y evaluación

Esquemas originales del proyecto, creados el 12/10/2026 para [la guía de generación y verificación](../../intuicion-generacion-verificacion.md). SVG editables y PNG para visualizar en Markdown. No reproducen figuras de los papers.

- `generacion`: compara el baseline directo con hechos intermedios y separa contexto externo de información del encuentro.
- `verificacion`: diferencia respaldo de afirmaciones y cobertura de hechos relevantes.
- `evaluacion-scribe`: explica revisión humana, métricas, regresión para calibrar métricas y juez LLM. Basado en [Wang et al., Methods y tabla 2](https://doi.org/10.1038/s41746-025-01622-1); la separación ajuste/evaluación es una recomendación para nuestro diseño, no un split documentado del artículo.

Regenerar un PNG: `inkscape generacion.svg --export-type=png --export-filename=generacion.png --export-width=1500`.
