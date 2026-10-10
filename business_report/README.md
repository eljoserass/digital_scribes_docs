# Informe ejecutivo: escribas digitales y HCIS

Entrada: [main.tex](main.tex). PDF compilado: [build/main.pdf](build/main.pdf).

El cuerpo desarrolla las siete secciones del borrador ejecutivo: introducción, motivación, alcance, criterios de adecuación, opciones y selección corta, despliegues y piloto, y decisiones solicitadas. El protocolo de evaluación, los servicios, la arquitectura y el presupuesto siguen pendientes de definición institucional. La revisión es documental; no se han probado productos ni aprobado una compra.

Las [opciones de evaluación](notes/opciones-evaluacion-piloto.md) se sintetizan en el [apéndice F](appendices/06_evaluacion_piloto.tex), como propuestas para discutir, con referencias y límites. La nota y el apéndice se editan manualmente. Las [fuentes adicionales](notes/additional/README.md) documentan las ampliaciones selectivas. El **18/09/2026** se añadieron la guía australiana TGA (sección 3) y el seguimiento de Permanente publicado en NEJM Catalyst (sección 6), localizado mediante una noticia de AMA; la noticia no se contabiliza como otro estudio.

## Organización

- [Declaración de uso de IA](sections/declaracion_uso_ia.tex): apartado sin numeración, al final del cuerpo y antes de las referencias. Identifica herramientas, tareas y responsabilidad del autor, siguiendo los elementos comunes de [ICMJE](https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html) y [Elsevier](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals), consultados el 12/09/2026. La redacción no presupone que la revisión humana final del borrador haya concluido.
- `sections/`: fuente editable del cuerpo.
- `appendices/`: glosario de certificaciones, inventario y fichas de **43 proveedores**, tablas completas de HCIS y precios, consideraciones sobre desarrollo propio y opciones metodológicas para evaluar el piloto.
- [notes/README.md](notes/README.md): índice de **47 fichas de Zotero**, con material consultado, aportación, límites y propuesta de uso.
- `notes/catalog.json`: metadatos de la colección revisada, claves y procedencia. No contiene la base de datos de Zotero ni copias de los PDF.
- `bibliography/references.bib`: referencias con claves de Zotero; se conserva el preprint duplicado pero se cita preferentemente la versión publicada. Incluye además la referencia externa del preprint español de Heidi ya utilizado en la investigación de mercado.
- `scripts/sync_market_appendices.py`: conversión reproducible de los inventarios Markdown a LaTeX; biblioteca estándar de Python.

## Editar y visualizar en VS Code

La configuración del proyecto en [`.vscode/settings.json`](../../.vscode/settings.json) utiliza **LaTeX Workshop** con XeLaTeX y latexmk. No requiere Make. En el entorno WSL están instalados los compiladores necesarios; abrir el proyecto con VS Code conectado a WSL.

1. Editar `main.tex` o cualquier archivo de `sections/` y guardar. La compilación se ejecuta al guardar; las secciones y apéndices indican `main.tex` como documento raíz.
2. Abrir la vista previa con **Ctrl+Alt+V** (comando **LaTeX Workshop: View LaTeX PDF file**). El PDF se muestra en una pestaña del editor y se actualiza tras compilar.
3. Para forzar la compilación, usar **Ctrl+Alt+B** (comando **LaTeX Workshop: Build LaTeX project**). SyncTeX permite navegar entre el texto y su posición en el PDF.

La receta produce `build/main.pdf` y resuelve la bibliografía con Biber automáticamente. Estos atajos son los predeterminados de la extensión; si se han reasignado, pueden usarse los comandos desde la paleta de VS Code.

## Compilar desde terminal

Desde esta carpeta:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error -outdir=build main.tex
```

Requiere XeLaTeX, latexmk, Biber y los paquetes indicados en `preamble.tex`. Produce `build/main.pdf`; incluye todos los apéndices. Los archivos `.tex` y `.bib` necesarios están dentro de esta carpeta y pueden copiarse juntos a otro entorno LaTeX.

Para actualizar los apéndices después de editar los inventarios del proyecto:

```bash
python3 scripts/sync_market_appendices.py
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error -outdir=build main.tex
```

Los cuatro primeros apéndices se generan desde [certificaciones](notes/certificaciones-escribas-digitales.md), [HCIS](notes/integraciones-hcis.md) y [precios](notes/precios-escribas-digitales.md). Editar esos Markdown y regenerar; las secciones del cuerpo y las fichas de lectura se editan directamente. La compilación normal no regenera ni sobrescribe el texto.

También hay un `Makefile` con los atajos `make` y `make appendices` para entornos que dispongan de Make; no es necesario para compilar.

**Verificación realizada (12/09/2026):** compilación con SyncTeX; sin citas indefinidas ni desbordamientos de texto. Se revisó visualmente una muestra del cuerpo y las tablas. TeX Live 2025 imprime en algunas tablas el mensaje informativo `ignored error: Infinite glue shrinkage…`; es un [comportamiento conocido de LaTeX/longtable](https://github.com/latex3/latex2e/issues/1907) y no impide generar el PDF.

## Corte y límites

Mercado revisado el **09/09/2026**; literatura y notas de Zotero revisadas el **11/09/2026**, con actualización del estudio ambulatorio de Quirónsalud. El 12/09/2026 se amplió selectivamente la fundamentación del cuerpo (carga documental, regulación, experiencia británica y opciones de evaluación); las 42 fichas iniciales conservan su fecha de corte. El **17/09/2026** se incorporó [AWS HealthScribe y sus partners](notes/additional/aws-healthscribe.md) como ficha 43, con actualización de los apéndices de certificaciones, HCIS y precios. La presentación conserva su versión anterior. No se presenta el corte bibliográfico como nueva verificación de todos los precios y certificados. No se modificó Zotero ni el borrador anterior `latex/hello.tex`.

La colección contiene cinco capturas Reddit asociadas al hilo equivocado; se consultaron las URL correctas y se documentó cada incidencia. Hay un manuscrito no publicado, un dataset tipado como artículo y dos versiones del mismo estudio ACL. Véase el índice de notas para el detalle. Esas incidencias no se convierten en evidencia clínica del informe.

**Verificación de la ampliación (18/09/2026):** regeneración de las 43 fichas y filas de HCIS/precios, compilación con bibliografía resuelta y revisión visual de las incorporaciones. Sin citas indefinidas ni desbordamientos registrados.
