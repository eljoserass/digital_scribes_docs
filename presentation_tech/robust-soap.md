# Robust SOAP: qué podemos adaptar

[Latif et al., CHIL 2026 — artículo y PDF](https://proceedings.mlr.press/v333/latif26a.html). Lectura para las diapositivas de verificación, propagación y experimento. Revisado el 12/10/2026 sobre el PDF de Zotero.

## El experimento

1. **Preparar referencias:** auditan PriMock57, corrigen inconsistencias y excluyen casos problemáticos; quedan **51 consultas**, frente a las 57 originales. Esta limpieza puede favorecer casos más consistentes.
2. **Generar y evaluar:** extraen hechos de nota generada, nota de referencia y diálogo. Comparan con la referencia; los hechos adicionales se contrastan con la conversación. Algo ausente de una nota gold no es necesariamente inventado.
3. **Introducir errores:** alteran el texto con una perturbación por transcripción; analizan **44 errores inducidos** y comparan la nota resultante con la generada desde el texto original. La tabla 1 enumera seis tipos: términos, cifras, diagnóstico, síntomas, negación y términos fonéticamente parecidos.

**No ejecutan ASR ni evalúan diarización.** Estudian generación desde transcripciones y perturbaciones textuales. Eso no demuestra que las etiquetas de rol sean innecesarias: el paper no compara explícitamente con/sin atribución. No lo describiría como evaluación completa audio→nota.

## Qué significan las columnas de la tabla 2

| Columna | Lectura |
|---|---|
| Coverage | Hechos de referencia cubiertos por la nota generada. |
| Omission | Hechos de referencia que faltan. |
| Contradiction | Conflictos con hechos de referencia. |
| Addition | Contenido adicional no respaldado tras contrastarlo con el diálogo. |
| Elaboration | Información extra respecto al gold, pero respaldada por la conversación. No equivale a alucinación. |

La flecha descendente de **Elaboration** es del original. No la convertiría en un objetivo universal de minimizar información respaldada. Las columnas no son una partición con un único denominador; revisar las fórmulas del §4 antes de implementarlas.

## Qué reproduciríamos y qué añadiríamos

Conservaríamos la comparación por hechos, la comprobación de adiciones contra el diálogo y las perturbaciones controladas. Primero comprobaríamos el protocolo con datos públicos; después, con nuestras referencias españolas y rúbrica clínica.

Añadiríamos audio procesado por nuestros modelos, atribución de hablantes, casos con historia fechada y ejecución local. Registraríamos memoria y tiempo, además de contenido. El esfuerzo de edición por médicos sería otra evaluación: el artículo no incluye un estudio de usuarios finales sobre tiempo de revisión.

**Límites:** evaluación con LLM para extracción/comparación, errores aislados en texto, inglés simulado y sin evaluación de uso clínico final. El apéndice A.1/tabla 5 repite el identificador `gpt-5-mini-preview` para filas de modelos distintos, incluida GPT-5.2: habría que resolver esa inconsistencia antes de reproducir literalmente sus configuraciones. Adoptar el método no implica aceptar sin revisión el ranking.

**Leer primero:** figura 1; §§4.1 y 5.1 para las dos fases; tabla 1 y §5.1.2 para robustez; §7 para límites. Tabla 2 para interpretar resultados, no para elegir nuestro modelo local.

Los [recortes originales](figures/README.md) conservan las tablas sin editar; tabla 1 en el cuerpo, tabla 2 en el anexo F.
