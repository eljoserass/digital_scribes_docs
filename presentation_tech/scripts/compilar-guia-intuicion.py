"""Build a single reading guide from the three editable Markdown chapters."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
intro='''# Guía de intuición: de la consulta a la nota

12/10/2026 · Acompaña a la presentación técnica. **Este es el archivo para leer y entender el recorrido.** Las figuras y el GIF explican los mecanismos; los ejemplos clínicos y números ilustrativos se distinguen de resultados publicados.

Puedes leer por bloques. Primero mira la figura, recorre el ejemplo y después lee el límite. No hace falta memorizar losses ni todos los resultados de los artículos para explicar el sistema.

| Lo que quieres entender | Dónde ir | Slides |
|---|---|---|
| CTC, RNN-T, atención y decoder | [Audio y hablantes](#audio-y-hablantes) | 9–11 |
| WER, DER, cpWER y tcpWER | [Audio y hablantes](#audio-y-hablantes) | 12–17 |
| p50, p95, latencia y RTF | [Audio y hablantes](#audio-y-hablantes) | 26 y 29 |
| Hechos, generador, historia y verificador | [De la consulta a la nota](#de-la-consulta-a-la-nota) | 18–22 |
| SCRIBE: médicos, métricas calibradas y juez | [De la consulta a la nota](#de-la-consulta-a-la-nota) | 23–24 |
| Robust SOAP, KOSMOS, ASCRIBE y Nuance | [Qué hace cada paper](#qué-hace-cada-paper) | 19 y lecturas |
| Cálculo local de RAM y tiempos | [RAM y latencia](#ram-y-latencia) | 26 |

El hilo: **reconocer qué se dijo → atribuirlo → seleccionar información → redactar → comprobar respaldo y cobertura → medir utilidad y ejecución**. Cada etapa puede introducir errores. Una salida intermedia visible permite localizarlos; no garantiza que desaparezcan.

Los capítulos también se conservan por separado: [audio/métricas](intuicion-audio-metricas.md), [generación/verificación](intuicion-generacion-verificacion.md), [papers](intuicion-papers.md). Fuentes enlazadas junto a cada explicación.

'''
chapters=[('Audio y hablantes','intuicion-audio-metricas.md','## 1.'),('De la consulta a la nota','intuicion-generacion-verificacion.md','## 1.'),('Qué hace cada paper','intuicion-papers.md','Primero ubica')]
out=intro
for title,filename,start in chapters:
 body=(ROOT/filename).read_text();body=body[body.index(start):]
 body=re.sub(r'^(#{2,5}) ',r'\1# ',body,flags=re.M)
 body=re.sub(r'(!\[[^\]]*\]\([^\n)]*)\.svg\)',r'\1.png)',body)
 out+=f'## {title}\n\n'+body.rstrip()+'\n\n'
out+='''## RAM y latencia

La slide 26 es un cálculo inicial, con **4–8 GB de RAM para procesos** bajo hipótesis concretas y un PC de 16 GB para comenzar a medir. Ese presupuesto cambia con duración, contexto, runtime y cuantización.

Las referencias de velocidad no son de nuestra pipeline: un port de MOSS tarda **21 s para 35 s de audio** en CPU Ryzen 7 PRO 4750U; un experimento de Qwen en Ember ronda **7 tokens/s en i5-1135G7**. A ese ritmo, 500 tokens son unos **72 s de decode**, antes de procesar el prompt. Son clips/motores distintos: no sumar como si fuese una consulta completa medida.

La [ficha de recursos locales](recursos-locales.md) contiene fuentes, cálculo y límites. Recuerda separar **carga → prefill → decode**, y **RAM del proceso** de **RAM total del PC**.

## Para comprobar que tienes el recorrido

- ¿Podrías reconocer todas las palabras y atribuir una alergia al acompañante equivocado? Sí; WER solo puede no verlo.
- ¿Puede una lista de hechos perder información antes de generar? Sí; por eso comparamos y conservamos las entradas.
- ¿Puede una nota tener todas sus frases respaldadas y omitir un dato importante? Sí; respaldo y cobertura se comprueban en direcciones distintas.
- ¿Un juez con 90 % de acuerdo humano garantiza seguridad? No: hay que saber qué categorías falla, la muestra, las referencias y la independencia del test.
- ¿Un modelo que cabe en memoria tiene latencia útil? No necesariamente; medir con la consulta y el equipo de uso.

Si una respuesta te cuesta, vuelve al ejemplo de ese bloque. Después practica con [preguntas de defensa](preguntas-defensa.md).
'''
(ROOT/'guia-intuicion.md').write_text(out)
print('Guide words:',len(out.split()))
