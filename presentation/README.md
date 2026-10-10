# Presentación para médicos y gestores

- [PDF: 17 slides principales + 3 apoyos](build/main.pdf).
- [Estructura, tiempos, guion y fuentes](guion-presentacion.md).
- [Contenido editable](main.tex) y [estilo](preamble.tex).

Versión del **18/09/2026**, en LaTeX Beamer, formato 16:9. Recorrido de **33 minutos**, más preguntas para una sesión de 40–45 minutos; el guion propone también una versión de 30 minutos. Las tablas y figuras son editables y las fuentes están enlazadas en el PDF.

## Editar y compilar

La configuración de LaTeX Workshop sirve para esta presentación. Abrir `docs/presentation/main.tex`, editar y guardar. Vista PDF: **Ctrl+Alt+V**; compilación: **Ctrl+Alt+B**. Su `main.tex` y directorio `build` son independientes del informe.

Desde esta carpeta:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error -outdir=build main.tex
```

Requiere XeLaTeX, latexmk, Beamer, TikZ y TeX Gyre Heros; no usa Biber. Numeración principal 1–17; apoyos A1–A3 después de «Gracias». El total principal se define en `preamble.tex`.

## Alcance de la revisión

El mercado conserva su corte inicial del **09/09/2026**, con AWS añadido el **17/09**: 43 proveedores. Literatura y ampliaciones del informe hasta el **18/09**. Ese día se comprobaron selectivamente las páginas de producto/precios de Tandem, Genesis y Align, las prestaciones de Oracle y los README de OpenScribe y Phlox. No supone revisar de nuevo todos los certificados y conectores.

El código abierto se integra en «Comprar, adaptar o desarrollar». Los repositorios son referencias exploratorias, sin instalación ni auditoría; no se presentan como alternativas hospitalarias validadas ni como una muestra exhaustiva. El guion contiene los nombres y límites para preguntas.

Los costes mostrados corresponden a ofertas publicadas; no hay presupuesto total HCIS. Se distingue ahorro documental, experiencia, calidad clínica y capacidad asistencial. El piloto sigue siendo una propuesta abierta.

**Verificación:** PDF de 20 páginas; títulos, numeración y tiempos del guion comprobados. Enlaces locales revisados. Compilación sin avisos ni desbordamientos; revisión visual de todas las slides y de las tablas modificadas.
