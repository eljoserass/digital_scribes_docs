"""Original explanatory SVGs, not reproductions of published diagrams.

Run with Python 3; export PNGs separately with Inkscape. Examples are fictional.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
NAVY = '#18394a'
GREEN = '#267b65'
BLUE = '#e8f1f5'
PALE = '#e9f4ed'


def diagram(name, title, subtitle, height, body):
    header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10" fill="{NAVY}"/></marker></defs>
<rect width="1280" height="{height}" fill="white"/>
<g font-family="DejaVu Sans, Arial, sans-serif" fill="{NAVY}">
<text x="48" y="49" font-size="28" font-weight="bold">{escape(title)}</text>
<text x="48" y="80" font-size="17">{escape(subtitle)}</text>
'''
    (ROOT / f'{name}.svg').write_text(header + body + '</g></svg>\n')


def text(x, y, lines, size=20, bold=False):
    spans = ''.join(f'<tspan x="{x}" dy="{0 if i == 0 else 30}">{escape(line)}</tspan>' for i, line in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{"bold" if bold else "normal"}">{spans}</text>'


def box(x, y, width, height, title, lines, fill=BLUE):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="14" fill="{fill}" stroke="{NAVY}" stroke-width="1.5"/>' + text(x+18, y+33, [title], 20, True) + text(x+18, y+68, lines, 17)


def arrow(x1, y1, x2, y2, dashed=False):
    dash_style = 'stroke-dasharray="8 6"' if dashed else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="2.5" {dash_style} marker-end="url(#arrow)"/>'


body = box(48, 120, 550, 162, '¿Lo recoge la referencia?', ['Nota gold: «Tos de tres días».', 'Nota generada: «Tos de tres días, sin fiebre».', '«Sin fiebre» no figura en el gold.'])
body += box(680, 120, 550, 162, '¿Lo respalda la conversación?', ['Paciente: «Llevo tres días con tos.', 'No he tenido fiebre».', 'El dato extra sí tiene evidencia.'], PALE)
body += arrow(598, 202, 680, 202)
body += text(48, 334, ['Ausente del gold ≠ inventado'], 26, True)
body += text(48, 372, ['La segunda comparación separa elaboración válida de contenido sin respaldo.'], 19)
body += box(48, 411, 550, 115, 'Si falta evidencia', ['«Auscultación normal» sin exploración documentada:', 'contenido no respaldado.'])
body += box(680, 411, 550, 115, 'Si la contradice', ['«Tiene fiebre» frente a «No he tenido fiebre»:', 'conflicto con la conversación.'])
body += text(48, 567, ['Ejemplo propio para explicar el protocolo de dos fases de Latif et al. (2026).'], 15)
diagram('robust-soap-intuicion', 'Robust SOAP: comparar con gold y volver a la evidencia', 'La nota de referencia ayuda a medir cobertura; la conversación ayuda a comprobar adiciones.', 595, body)

body = box(48, 115, 370, 172, 'Transcripción con turnos', ['T4 · Paciente: «Antes tomaba', '500 mg de metformina».', 'T9 · Médico: «Desde hoy,', '1000 mg al día».'])
body += box(486, 115, 370, 172, 'Nodos con atributos', ['Metformina · régimen previo', 'dosis: 500 mg · fuente: T4', 'Metformina · régimen nuevo', 'dosis: 1000 mg/día · fuente: T9'], PALE)
body += arrow(418, 201, 486, 201)
body += box(930, 115, 302, 172, 'Relaciones', ['Paciente → régimen previo', 'Médico → prescribe', '           régimen nuevo'])
body += arrow(856, 201, 930, 201)
body += box(270, 366, 760, 143, 'Generación conservando la transcripción', ['Texto original + nodos (o grafo) → nota con citas.', '«Se modifica metformina a 1000 mg/día» [T9].', 'Comparar texto solo / texto + nodos / texto + grafo.'], PALE)
body += arrow(650, 287, 650, 366)
body += text(48, 562, ['Separar dos regímenes evita mezclar una dosis antigua con un plan actual.'], 21, True)
body += text(48, 597, ['Esquema propio inspirado en KOSMOS; ejemplo ficticio, sin códigos UMLS ni extracción real.'], 15)
diagram('kosmos-intuicion', 'KOSMOS: hacer visibles entidades, atributos y relaciones', 'El grafo se construye desde la consulta; no es la historia clínica recuperada de otro sistema.', 630, body)

body = box(48, 120, 335, 148, '1 · Conversación', ['Hechos dispersos en turnos.', 'Ejemplo: «Me salió una', 'reacción al tomar X».'])
body += box(447, 120, 380, 148, '2 · Hecho + fuente + relevancia', ['«Refiere reacción tras X».', 'Conservar el fragmento de soporte.', 'Asignar relevancia clínica.'], PALE)
body += box(890, 120, 340, 148, '3 · Nota', ['Generar SOAP usando el', 'diálogo y los hechos previos.', 'No diagnosticar por defecto.'])
body += arrow(383, 195, 447, 195) + arrow(827, 195, 890, 195)
body += text(48, 316, ['Dos usos del mismo formato'], 24, True)
body += box(48, 353, 550, 152, 'Prompting: pedir esa secuencia', ['Instrucciones → hechos + etiquetas → nota.', 'No se modifican los pesos del modelo.', 'Se compara con pedir directamente SOAP.'])
body += box(680, 353, 550, 152, 'Entrenamiento: puntuar y actualizar', ['Varias salidas → rewards → actualización GRPO.', 'Puntuar hechos, relevancia, completitud,', 'respaldo y estructura SOAP.'], PALE)
body += text(48, 552, ['El juez da una señal de entrenamiento; no convierte sus decisiones en verdad clínica.'], 20, True)
body += text(48, 589, ['Esquema propio del método ASCRIBE (Kalavantavanich et al., 2026). Ejemplo ficticio.'], 15)
diagram('ascribe-intuicion', 'ASCRIBE: explicitar qué información conservar', 'Tailandés: hechos atómicos, evidencia y seis niveles de relevancia antes de generar la nota.', 620, body)
