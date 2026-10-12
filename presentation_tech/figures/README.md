# Figuras del borrador técnico

Los esquemas del sistema son propios y editables en TikZ, dentro de [main.tex](../main.tex) o en archivos incluidos desde esta carpeta. Las fuentes de cada esquema aparecen en el pie de su diapositiva. Los diagramas de prototipo y comparación muestran propuestas, sin resultados del proyecto ni un conector HCIS implementado.

## Audio con texto alineado: Jurafsky y Martin

Los dos recortes muestran la **misma frase de Switchboard**, con palabras y fonemas alineados. Así se relacionan la onda, su estructura espectral y el texto sin atribuir fronteras inventadas a nuestro audio.

| Archivo | Figura y página del original | Contenido |
|---|---|---|
| [jurafsky-wave.pdf](jurafsky-wave.pdf) · [PNG](jurafsky-wave.png) | **15.15, p. 15** | Onda de una frase, con filas de palabras y fonemas. |
| [jurafsky-spectrogram.pdf](jurafsky-spectrogram.pdf) · [PNG](jurafsky-spectrogram.png) | **15.22, p. 19** | Espectrograma de la misma frase, con las mismas etiquetas. |

**Fuente:** Daniel Jurafsky y James H. Martin, *Speech and Language Processing*, 3.ª edición, borrador del **19 de agosto de 2026**, capítulo 15, *Phonetics and Speech Feature Extraction*. [PDF de Stanford](https://web.stanford.edu/~jurafsky/slp3/15.pdf); [copia de Zotero usada](/mnt/c/Users/rodri/Zotero/storage/VKDA3U4Q/15.pdf). © 2026 Daniel Jurafsky y James H. Martin. Las figuras originales son de los autores; los recortes no son figuras propias ni nuevas anotaciones nuestras.

Se han excluido el texto del libro, los captions y el marco exterior. Se conservan los trazos vectoriales y, en el espectrograma, la imagen original. La figura muestra inglés conversacional, no una consulta médica ni una representación log-Mel. El eje vertical del espectrograma corresponde a frecuencia; el original no aporta ticks de frecuencia en esa imagen.

Para regenerar los PDF y las previews desde `presentation_tech/`:

```bash
python3 figures/extract_jurafsky_figures.py
# O pasar la ruta de otro ejemplar de ese mismo borrador:
python3 figures/extract_jurafsky_figures.py /ruta/al/capitulo15.pdf
```

[extract_jurafsky_figures.py](extract_jurafsky_figures.py) registra páginas y coordenadas del recorte. Necesita `pypdf`, Ghostscript y `pdftoppm`. No copia el libro completo al repositorio. Se comprobó visualmente el recorte y que el PDF resultante no contiene los párrafos adyacentes.

## Tres familias de ASR

[asr-architectures.tex](asr-architectures.tex) es un **esquema propio** para incluir dentro de `figurecanvas[4.3]` (14 × 4,3 cm). Muestra cómo sale el texto, con mecanismos, antecedentes y ejemplos actuales:

- **CTC:** etiquetas por frame, blank y colapso; ejemplo actual Parakeet CTC.
- **RNN-T:** estado acústico y predictor del texto; emisión de tokens y avance temporal. Parakeet TDT es un derivado actual que predice duraciones, no el RNN-T original.
- **Atención:** audio codificado y texto previo condicionan el siguiente token; ejemplos Whisper y Canary. La diapositiva siguiente abre el decoder Transformer de Whisper y separa red neuronal de greedy/beam search.

Las fechas son hitos bibliográficos, no una cronología de sustitución. Las tres familias siguen en uso.

Referencias para el dibujo: [Jurafsky y Martin, cap. 16](https://web.stanford.edu/~jurafsky/slp3/16.pdf), mismo borrador, **fig. 16.5/p. 8, fig. 16.13/p. 18 y fig. 16.17/p. 22**; [copia de Zotero](/mnt/c/Users/rodri/Zotero/storage/2DGXGMAU/16.pdf). Apoyo para las diferencias y las variantes en streaming: [Prabhavalkar et al., *End-to-End Speech Recognition: A Survey*](https://arxiv.org/abs/2303.03329), §II. Para Whisper: [Radford et al.](https://arxiv.org/abs/2212.04356), §2.2 y fig. 1.

## Figura sintética del primer borrador

[signal_features.pdf](signal_features.pdf) y [PNG](signal_features.png), generados con [render_signal.py](render_signal.py), se conservan como material auxiliar. Muestran una señal armónica sintética a 16 kHz, STFT (ventana de 25 ms, avance de 10 ms) y 40 bandas log-Mel. **No son voz ni audio clínico.** Desde `presentation_tech/`: `python3 figures/render_signal.py`.

## Robust SOAP: tablas originales

[Tabla 1](robust-soap-table1.pdf) (p. 454 / página 7 del PDF) contiene la taxonomía de perturbaciones; [tabla 2](robust-soap-table2.pdf) (p. 456 / página 9) contiene los resultados publicados. **Latif et al., CHIL 2026, PMLR 333**, © autores. [Artículo y PDF original](https://proceedings.mlr.press/v333/latif26a.html).

Son recortes vectoriales sin modificar celdas, flechas ni captions. Se usa la copia proporcionada en Zotero; no se incluye el artículo completo. La tabla 1 está en el cuerpo y la 2 en el anexo F. La interpretación y las limitaciones están en [robust-soap.md](../robust-soap.md).

Regenerar con `python3 figures/extract_robust_soap_tables.py /ruta/al/articulo.pdf`. El script registra páginas y coordenadas, elimina contenido externo al recorte con Ghostscript y genera PNG de revisión. La figura del decoder y los ejemplos DER/cpWER son propios; los valores ilustrativos no son resultados de modelos.
