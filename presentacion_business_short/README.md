# Presentación business short

Versión visual del **09/10/2026**: **13 diapositivas para unos 10 minutos**, en LaTeX Beamer 16:9. Las diapositivas 1–3 mantienen el recorrido; explican HCIS y escriben completas las siglas clínicas. Desde la 4, figuras breves sustituyen listas y tablas; los detalles quedan en el guion y en el informe.

- [PDF de la presentación](build/main.pdf).
- [Guion con tiempos y notas para preguntas](guion-presentacion.md).
- [Contexto, investigación y fuentes](contexto-investigacion.md).
- [Contenido editable](main.tex) y [estilo](preamble.tex).
- Diagramas editables: [flujo con contexto HCIS](figures/flujo-hcis.tex) y [ejemplo SOAP](figures/nota-soap.tex).
- Las diez figuras añadidas están en [main.tex](main.tex), con [iconos y estilos TikZ](figures/visual-style.tex). El gráfico de mercado es original, basado en las cifras de Menlo 2025.
- Imágenes reutilizables: [flujo HCIS PNG](figures/flujo-hcis.png) y [nota SOAP PNG](figures/nota-soap.png); originales vectoriales en [flujo PDF](build/flujo-hcis-standalone.pdf) y [SOAP PDF](build/nota-soap-standalone.pdf).

Identidad visual de IRYCIS: [logo oficial](assets/logo-irycis-oficial.png) en portada y pie de las demás diapositivas, con azul y verde basados en el archivo publicado por el instituto. Los diagramas y sus exportaciones comparten esa paleta. [Procedencia del logo y colores](assets/README.md).

La cifra **≈5 h/mes menos de documentación** se integra en la diapositiva de beneficios. Es una proyección propia por profesional, si se mantiene el efecto observado con ocho horas de consulta programada al día y 220 días/año; el resultado base de 16 minutos por ocho horas y las hipótesis aparecen junto a la cifra. Los escenarios de seis meses y un año quedan en las [notas de cálculo](contexto-investigacion.md). Quirónsalud queda como proyecto propio, separado de APIs comerciales. La rapidez de adopción se atribuye a PHTI; el crecimiento de ingresos, a Menlo.

## Recorrido

1. Qué es: flujo completo con conversación, contexto HCIS y observaciones; ejemplo SOAP con procedencia de los datos.
2. Por qué importa: carga documental, oportunidad y ahorro neto que evaluar.
3. Mercado y encaje: expansión con cifras, familias de ofertas, cuatro requisitos locales y estado HCIS de los tres candidatos.
4. Discusión: proveedor y posible prototipo local; los mismos casos y criterios para elegir qué pilotar.
5. Conclusión y siguientes pasos: condiciones → casos → comparación → piloto. Decisión propuesta: iniciar una evaluación local acotada.

El índice se comparte con la apertura. Cada diapositiva conserva su sección numerada en el pie, incluida la discusión y conclusión. Los tiempos del [plan](slide-plan.json) y del guion suman **10:00**; las preguntas se dejan para después.

## Editar y compilar

Desde esta carpeta:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error -outdir=build main.tex
```

Requiere XeLaTeX, latexmk, Beamer, TikZ y TeX Gyre Heros. No requiere Biber. PDF en `build/main.pdf`. En LaTeX Workshop, abrir `main.tex`: **Ctrl+Alt+B** para compilar y **Ctrl+Alt+V** para ver el PDF.

Para regenerar también las imágenes y sus PDF independientes:

```bash
python3 scripts/exportar-figuras.py
```

Requiere además Python 3, el paquete LaTeX `standalone` y `pdftoppm` (Poppler). Los diagramas de las slides y las imágenes utilizan la misma fuente TikZ.

## Fechas y alcance

El inventario de 43 soluciones y proyectos conserva sus cortes de septiembre de 2026. Las comprobaciones comerciales del 07/10 y 09/10 son selectivas y están documentadas en la investigación; no constituyen una auditoría de todos los certificados ni una prueba funcional de conectores. El encaje pendiente se refiere a los requisitos del hospital y a la evidencia revisada.

La cifra de mercado procede de Menlo Ventures 2025: 600 M$ y ×2,4 interanual. La barra de 2024 (250 M$) es una base derivada, marcada como tal. Se presenta como estimación de una fuente inversora en un informe centrado en EE. UU.; no se extrapola a España ni se confunde con el recuento propio de proveedores.

La selección comercial prioriza datos, seguridad, coste total e integración HCIS; la calidad local queda como siguiente trabajo a medir. El prototipo local es una opción para discutir y evaluar como comparador, con infraestructura, desarrollo y mantenimiento por estimar. El ejemplo SOAP es ficticio. No se han instalado ni validado aplicaciones clínicas.

La elaboración utiliza apoyo de IA; la revisión humana final del autor está pendiente. Las fuentes están enlazadas en el PDF y ampliadas en la investigación.

**Verificación técnica:** PDF de 13 páginas, guion de 600 segundos y cinco secciones. Compilación sin avisos ni desbordamientos. Revisión visual de las diapositivas; el tiempo de exposición sigue pendiente de ensayo.
