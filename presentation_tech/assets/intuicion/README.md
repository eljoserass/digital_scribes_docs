# Visuales de la guía de intuición

Figuras propias para [intuicion-audio-metricas.md](../../intuicion-audio-metricas.md). Los diálogos, probabilidades y tiempos son ejemplos inventados, no resultados experimentales.

| Archivo | Idea |
|---|---|
| [ctc.gif](ctc.gif) · [imagen final](ctc-poster.png) | Predecir etiquetas, colapsar repeticiones y eliminar blanks. |
| [rnnt.svg](rnnt.svg) | Emitir texto o avanzar por el audio; encoder, predictor y joiner. |
| [decoder.svg](decoder.svg) | Separar red neuronal de greedy/beam search. |
| [metricas.svg](metricas.svg) | DER, cpWER y tcpWER con ejemplos diferentes. |
| [percentiles.svg](percentiles.svg) | Cien latencias ordenadas, p50, p95 y máximo. |

Los SVG incluyen título y descripción accesibles. El Markdown añade texto alternativo. El GIF tiene una imagen estática para lectores que no reproducen animaciones.

Regenerar con Python y Pillow:

```bash
python generar_visuales.py
```

El script guarda las figuras en su propia carpeta. No necesita Manim, servicios externos ni descargas. Las referencias de los conceptos aparecen junto a las explicaciones en el Markdown; no se han copiado figuras de terceros.
