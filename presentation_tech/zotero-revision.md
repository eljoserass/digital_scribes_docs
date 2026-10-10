# Revisión de Zotero — Digital Escriber

**08/10/2026.** Biblioteca de Windows en `/mnt/c/Users/rodri/Zotero/zotero.sqlite`, colección **Digital Escriber**, clave `YYTP79GR`. Lectura sobre una copia consistente de SQLite y adjuntos originales; Zotero no se modificó.

Comparación por clave de ítem con [catalog.json del business report](../business_report/notes/catalog.json), revisado el **11/09/2026**: **47 → 75 entradas; 28 añadidas, 0 ausentes**. «Añadida» significa clave nueva frente a ese inventario, no paper nuevo ni estudio único. No se ha hecho una comparación completa de cambios en metadatos o anotaciones de las 47 entradas previas.

Se revisaron metadatos y resúmenes disponibles de las 28 entradas. Para las referencias técnicas prioritarias se consultaron las partes indicadas del PDF, no se afirma lectura íntegra de todos los trabajos. Los capítulos 15/16 se contrastaron con el borrador público del 19/08/2026. Para las fuentes previas se reutilizaron las fichas del informe, especialmente PriMock57, evaluación humana, validación y descomposición funcional.

## Qué cambia en el draft

- **Seq2seq:** `9KBENXJ5`, añadido el 07/10/2026, es [Singh et al., 2023, de **Nuance Communications**](https://aclanthology.org/2023.clinicalnlp-1.18/). Incorporado como antecedente de generación y entrenamiento.
- **TEME:** el [extended abstract de AAMAS](https://doi.org/10.65109/RHNT7438) aporta el origen que faltaba en la ficha del corpus: texto de 23 consultas anonimizadas y 67 diálogos sintéticos, con audio generado por Gemini TTS. Es un recurso de ASR médico español con turnos; no trae gold temporal de diarización. Su juez LLM de errores es una propuesta de evaluación, no una loss.
- **Entrada y salida:** [Communication in Medical Care](https://doi.org/10.1017/CBO9780511607172), [RIAS](https://doi.org/10.1016/S0738-3991(02)00012-5), [SOAP Notes](https://www.ncbi.nlm.nih.gov/books/NBK482263/) y [The anatomy of clinical documentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/) ayudan a definir consulta y nota antes de escoger modelos.
- **Evaluación:** el [framework clínico de 2025](https://doi.org/10.1038/s41746-025-01622-1) y [Benchmarking Diarization Models](https://arxiv.org/abs/2509.26177) dan protocolos por etapa y ejemplos de fallos; incorporados como lecturas prioritarias.
- **Fundamentos:** [End-to-End Speech Recognition: A Survey](https://arxiv.org/abs/2303.03329) complementa Jurafsky para profundizar en objetivos y decoding; MOSS y speaker targeting quedan como alternativas conjuntas, sin convertirlas en validaciones clínicas.

## Las 28 entradas añadidas

La columna «Material» describe esta revisión: **metadatos/resumen**, **PDF focalizado** o **capítulo público**. «Después» conserva la referencia para una ampliación futura; no implica que haya que incluirla en las diapositivas.

| Clave | Fuente y por qué mirarla | Bloque sugerido | Material |
| --- | --- | --- | --- |
| `AWH83W73` | [Towards autonomous medical artificial intelligence agents](https://doi.org/10.1038/s41586-026-10675-5) — Acciones en EHR y agentes; una tarea mucho más amplia que documentar una consulta. | Contexto/HCIS; simulación en [bag of ideas](bag-of-ideas.md) | Metadatos/resumen; ampliación 09/10: PDF, métodos de curación/simulación y disponibilidad; repositorio |
| `XSWTCT9P` | [Digital scribes — TGA](https://www.tga.gov.au/products/medical-devices/software-and-artificial-intelligence-ai/overview/types-software-based-medical-devices/digital-scribes) — Uso previsto y encaje regulatorio australiano; no sustituye fuentes españolas. | Despliegue, después | Metadatos |
| `62Q9JQNG` | [AI scribes save 15,000 hours — AMA](https://www.ama-assn.org/practice-management/digital-health/ai-scribes-save-15000-hours-and-restore-human-side-medicine) — Contexto de adopción; acudir al estudio primario antes de usar sus cifras. | Contexto, después | Metadatos/resumen |
| `LTA2E8PR` | [Benchmarking Diarization Models](https://arxiv.org/abs/2509.26177) — **196,6 h** de cuatro corpora; versiones, collar, solapamiento y causas de error. | Evaluación/diarización | PDF: metodología y resultados seleccionados |
| `H3IVL94A` | [TEME: A Multi-Agent Evaluation Framework for Spanish Medical Speech Recognition](https://doi.org/10.65109/RHNT7438) — Evaluación clínica del ASR sobre **90 diálogos**; separar framework y corpus. | ASR médico/evaluación | PDF: método, origen del corpus y tabla; dos anotaciones tuyas |
| `IQ5KTX5M` | [Communication in Medical Care](https://doi.org/10.1017/CBO9780511607172) — Fases y organización de la consulta, para caracterizar la entrada. | Caso de uso | Metadatos/resumen; no lectura del libro completo |
| `J5MZNLPV` | [The Roter interaction analysis system (RIAS)](https://doi.org/10.1016/S0738-3991(02)00012-5) — Funciones del diálogo médico para pensar relevancia y selección de contenido. | Consulta/comprensión | PDF: resumen e introducción |
| `HCG5VHZT` | [Beyond ‘doctor and patient’](https://doi.org/10.1111/j.1467-9566.2009.01194.x) — Interacciones sanitarias más amplias; útil cuando haya acompañantes, equipos o tecnología. | Caso de uso, después | Metadatos/resumen |
| `8JAQ3TRT` | [Taking note](https://pmc.ncbi.nlm.nih.gov/articles/PMC6694617/) — Implantación del escriba humano como cambio de práctica del equipo, no solo cambio de herramienta. | Operación, después | Metadatos/resumen |
| `TYZXMWDY` | [Safe use of the EHR by medical scribes](https://doi.org/10.1093/jamia/ocaa199) — Organización, supervisión y uso del EHR por escribas humanos. | Operación, después | Metadatos/resumen |
| `9PZGZR2Y` | [Speaker Targeting via Self-Speaker Adaptation for Multi-talker ASR](https://arxiv.org/abs/2506.22646) — Alternativa de ASR por hablante para solapamientos y streaming; no específica de medicina. | Transcripción con hablantes, después | PDF: resumen e introducción |
| `MLC7RM2X` | [Evaluating Robustness of LLM-Based Ambient Scribes for SOAP Note Generation](https://proceedings.mlr.press/v333/latif26a.html) — Hechos clínicos, omisiones y efecto de ruido ASR; ya figuraba en nuestra búsqueda web. | Evaluación/verificación | Metadatos/resumen; fuente pública consultada previamente |
| `KN7WEPL6` | [Benchmarking And Datasets For Ambient Clinical Documentation](https://www.medrxiv.org/content/10.1101/2025.01.29.25320859v1) — Scoping review preliminar de métricas y benchmarks; marco para buscar, no inventario exhaustivo actual. | Evaluación, después | PDF: resumen, alcance y resultados generales |
| `8Y52UVZT` | [An evaluation framework for ambient digital scribing tools in clinical applications](https://doi.org/10.1038/s41746-025-01622-1) — **40 visitas prenatales**, 6–35 min; evaluación de tareas y casos simulados. | Evaluación end-to-end | PDF: dataset, método y resultados seleccionados |
| `E4UNJ27M` | [ACI-Bench](https://doi.org/10.1038/s41597-023-02487-3) — **207 encuentros textuales**, splits y evaluación por sección; ya estaba en el catálogo técnico por búsqueda web. | Datasets/generación | PDF: tabla de splits y comparación de baselines |
| `C594NIA6` | [End-to-End Speech Recognition: A Survey](https://arxiv.org/abs/2303.03329) — Taxonomía de ASR, objetivos, alineamiento y decoding. | ASR/entrenamiento | PDF: introducción y formulaciones; nota bibliográfica |
| `M3Z69WVL` | [SOAP Notes](https://www.ncbi.nlm.nih.gov/books/NBK482263/) — Define el formato de salida y su función documental. | Caso de uso/nota | Metadatos/resumen; web bloqueada por captcha en esta revisión |
| `VKDA3U4Q` | [Jurafsky y Martin, cap. 15](https://web.stanford.edu/~jurafsky/slp3/15.pdf) — Fonética y features, incluyendo referencias de TIMIT, Buckeye y MFCC. | Señal/fundamentos | Capítulo público: partes acústicas, features y referencias |
| `2DGXGMAU` | [Jurafsky y Martin, cap. 16](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — ASR, evaluación y objetivos; ambos ítems son PDF independientes en Zotero. | ASR/fundamentos | Capítulo público: modelos, objetivos y referencias |
| `NLF7JVVI` | [Adjunto real: Jurafsky, cap. 17](https://web.stanford.edu/~jurafsky/slp3/17.pdf) — El título bibliográfico anuncia «Language Models are Zero-Shot Text o Speech Synthesizers», pero el PDF adjunto es otro documento. | Incidencia; TTS opcional | Portada del PDF local |
| `AZJX6A3J` | [MOSS Transcribe Diarize Technical Report](https://arxiv.org/abs/2601.01554) — Modelo conjunto de texto, tiempos y hablantes; no genera la nota médica en su tarea publicada. | Transcripción con hablantes | PDF: arquitectura y datos; fuente pública ya consultada |
| `5RWGQ8MR` | [Operationalizing Trustworthy AI Requirements for Digital Scribes](zotero://select/library/items/5RWGQ8MR) — Mismo título que `EI2RV8NV`; no se ha comprobado si los adjuntos son versiones diferentes. | Pipeline/operación, después | Metadatos y ficha previa |
| `KXDC2XL9` | [Effect of a generative AI digital scribe on pediatric providers](https://doi.org/10.1093/jamiaopen/ooaf068) — Tiempo, carga cognitiva y burnout como resultados distintos. | Utilidad/operación, después | Metadatos/resumen |
| `DXZS5VZK` | [Shapley value explanations for clinical prediction models](https://doi.org/10.1038/s41746-026-03324-8) — Explicabilidad de predicción tabular; relación indirecta con la pipeline de escriba. | Fuera del núcleo actual | Metadatos/resumen |
| `T6SB4C4U` | [Shapley value explanations for clinical prediction models](https://doi.org/10.1038/s41746-026-03324-8) — Mismo DOI que `DXZS5VZK`; conservar como una referencia al contar trabajos. | Duplicado | Metadatos/resumen |
| `9KBENXJ5` | [Seq2seq clínico — Nuance](https://aclanthology.org/2023.clinicalnlp-1.18/) — Generación supervisada y CE+BRIO. | Generación/loss | PDF: afiliación, datos, arquitectura y loss |
| `HIY3N7FM` | [The anatomy of clinical documentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/) — **80 notas**, con análisis de HPI e impresión/plan; concreta contenido y variación de formato. | Definir salida/generación | PDF: resumen y selección del corpus |
| `9N255BSB` | [Safe use of the EHR by medical scribes](https://doi.org/10.1093/jamia/ocaa199) — Mismo DOI que `TYZXMWDY`, añadido en otra entrada. | Duplicado | Metadatos/resumen |

## Incidencias y límites

- Duplicados por DOI: `TYZXMWDY`/`9N255BSB` y `DXZS5VZK`/`T6SB4C4U`. Coincidencia de título: `EI2RV8NV`/`5RWGQ8MR`; falta comparar versiones. El preprint/publicación ACL de evaluación humana ya estaba identificado en el informe anterior.
- `NLF7JVVI` tiene un adjunto que no corresponde a su título: no usar ese PDF como evidencia del paper bibliográfico. No se corrigió ni eliminó nada en la biblioteca.
- Las anotaciones de TEME expresan dudas sobre el origen del dato y la identificación del ASR. El método sí describe texto/TTS y la tabla nombra Whisper y Omniloy-medical-voice; faltan detalles suficientes para asumir una reproducción exacta de las configuraciones.
- Las cifras y conclusiones de los artículos de mercado, regulación y agentes no se incorporaron al núcleo técnico solo por estar en la colección. Pueden servir después si ampliamos esos bloques.

Para decidir qué leer primero, usar las [bolsas por sección](estructura-presentacion.md); para elegir datos y objetivos, usar el [catálogo técnico](README.md).
