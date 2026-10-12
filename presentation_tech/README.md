# Source list — escribas digitales médicos

La [presentación renovada](build/main.pdf), del **12/10/2026**, tiene **31 diapositivas principales para unos 30 minutos**, con figuras, fuentes enlazadas y cinco anexos. [Guion con hilo, transiciones y tiempos](guion-presentacion.md) · [fuente editable](main.tex) · [plan de tiempos](slide-plan.json).

Para compilar desde esta carpeta: `make` (XeLaTeX y latexmk). `make previews` exporta las páginas a JPEG en `build/previews/`. Las figuras acústicas son recortes atribuidos de Jurafsky; los esquemas son TikZ en `main.tex` y `figures/asr-architectures.tex`. [Origen y regeneración de las figuras](figures/README.md) e [identidad IRYCIS](assets/README.md).

El recorrido es **consulta y nota → evaluación y datos → audio y hablantes → diálogo, contexto y nota → adaptación y despliegue → primer experimento**. La selección de hechos, la recuperación de historia y las comprobaciones se explican como funciones con límites propios. Los experimentos y el cliente de Scribnic son propuestas, sin resultados clínicos del proyecto. Las losses y las ideas adicionales quedan en los anexos.

Selección inicial de fuentes primarias consultadas el **08/10/2026**. Cada entrada incluye una descripción breve y un enlace original. La [estructura y las lecturas por sección](estructura-presentacion.md) están en otro documento.

Notas breves: [common challenges](common_challenges.md) y [qué es una nota clínica y cómo se usa en el EHR](clinical_note_context.md).

[Bag of ideas](bag-of-ideas.md): historiales simulados, consultas sintéticas, PriMock57 en español, evaluación con médicos y jueces automáticos; referencias y primeros experimentos para ampliar el cierre.

Para el marco de evaluación: [SCRIBE, figura 1 y límites](scribe-evaluacion.md), con los paneles originales (a) y (b) en el PDF. [Robust SOAP](robust-soap.md) queda como lectura complementaria sobre hechos y perturbaciones.

**Empieza por la [guía de intuición con figuras y GIF](guia-intuicion.md):** CTC/RNN-T/atención, métricas, p50/p95, generación, verificación y papers. La [estimación local](recursos-locales.md) documenta RAM y benchmarks de la slide 26.

Para preparar la revisión: [conversación, contexto y hechos clínicos](comprension-clinica.md), con dos métodos recientes y límites de verificación; [preguntas de defensa y mini examen](preguntas-defensa.md). Scribnic y su estado actual se recogen en el [bag de ideas](bag-of-ideas.md#9-scribnic-núcleo-local-reutilizable-y-clientes-separados).

Se indica cuándo el recurso es clínico, general, simulado o solo textual. Las losses son objetivos de entrenamiento; las métricas evalúan resultados. Los métodos generales son componentes candidatos, no validaciones de un escriba médico en español.

Orden de lectura: **estándares generales de la tarea → referencias clínicas → adaptación al español médico**. «Estándar» significa aquí benchmark o método habitual, no norma obligatoria ni ranking de SOTA. Los recursos complementarios quedan para una segunda pasada.

Los volúmenes distinguen horas de grabación, consultas, documentos y pares anotados; no son intercambiables. Se fija versión cuando corresponde. No sumamos canales ni variantes sintéticas como si fueran consultas nuevas; donde faltan cifras se indica.

## Base para entender las tareas — Jurafsky y Martin

- [Cap. 15: Phonetics and Speech Feature Extraction](https://web.stanford.edu/~jurafsky/slp3/15.pdf) — Leer especialmente §§15.4–15.6: señal, muestreo, espectrograma, log-Mel y MFCC; revisar también sus referencias y corpora.
- [Cap. 16: Automatic Speech Recognition](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — Base para WER, encoder–decoder, CTC, RNN-T y aprendizaje autosupervisado; conecta las características acústicas con los modelos.
- [End-to-End Speech Recognition: A Survey](https://arxiv.org/abs/2303.03329) — Lectura de apoyo de tu Zotero para comparar CTC, transducers, atención, entrenamiento, decoding y restricciones de ejecución.
- [Davis y Mermelstein, 1980](https://doi.org/10.1109/TASSP.1980.1163420) — Referencia del cap. 15 sobre representaciones cepstrales; útil para explicar MFCC y compararlo con log-Mel.
- [TIMIT — LDC93S1](https://catalog.ldc.upenn.edu/LDC93S1) — ≈5 h, 6.300 frases y 630 hablantes en inglés con alineamiento fonético; recurso del cap. 15 para ilustrar sonido, palabra y tiempo.
- [Buckeye Corpus](https://buckeyecorpus.osu.edu/) — 40 hablantes y ≈300.000 palabras de conversación espontánea en inglés, con etiquetas fonéticas; útil para reducciones y disfluencias, también citado en el cap. 15.

Numeración del [borrador del 19/08/2026](https://web.stanford.edu/~jurafsky/slp3/); las ediciones anteriores pueden numerar estos temas de otra forma. TIMIT y Buckeye son lecturas de fundamentos, no benchmarks clínicos principales.

## Datasets, metrics y loss

### Transcription

**Datasets — estándares generales**

- [LibriSpeech](https://www.openslr.org/12) — ≈1.000 h de audiolibros en inglés; 960 h de entrenamiento en bloques de 100/360/500 h, referencia habitual de ASR leído.
- [Switchboard-1, Release 2](https://catalog.ldc.upenn.edu/LDC97S62) — ≈260 h, 2.400 conversaciones telefónicas y 543 hablantes en inglés; añade habla conversacional y disfluencias, con licencia LDC.
- [FLEURS](https://arxiv.org/abs/2205.12446) — ≈12 h por idioma en 102 idiomas, incluido español; habla leída y comparación multilingüe general.
- [Common Voice 17.0, español](https://aclanthology.org/2025.resourceful-1.12/) — ≈2.220 h totales, de las que ≈562 h estaban validadas por usuarios; versión fija de habla leída general, no todo el total es referencia validada.

**Datasets — clínicos y español médico**

- [PriMock57](https://arxiv.org/abs/2204.00333) — 57 consultas simuladas en inglés, **8 h 38 min** de consulta, 7 clínicos y 57 pacientes representados por actores; audio, turnos temporizados y notas.
- [AfriSpeech-200](https://github.com/intron-innovation/AfriSpeech-200) — **196 h** con 120 acentos africanos, mezclando inglés clínico y general; las horas son del corpus completo, no solo de su parte médica.
- [TEME-v1](https://zenodo.org/records/17280661) — **90 diálogos, 10 especialidades, 90 MP3 y 90 JSON** en español con hablantes por turno; volumen de audio medido y límites de diarización al final de este documento.

Para español clínico, FLEURS/Common Voice sirven como controles generales y TEME como primer recurso del dominio; falta establecer una referencia de consultas locales reales con anotación clínica. No se asume que estos conjuntos sean equivalentes.

**Metrics**

- [WER / CER — JiWER](https://github.com/jitsi/jiwer) — Error por palabras o caracteres respecto a una transcripción, con sustituciones, inserciones y eliminaciones.
- [Medical WER / medical NE recall](https://arxiv.org/abs/2406.12387) — Evaluación de errores y recuperación de entidades médicas en inglés con acentos; complementa el WER global.
- [Clinical BERTScore](https://arxiv.org/abs/2303.05737) — Métrica semántica adaptada al dominio clínico, estudiada frente a preferencias de clínicos sobre transcripciones.
- [TEME: framework de evaluación, AAMAS 2026](https://doi.org/10.65109/RHNT7438) — Evalúa medicación, dosis y coherencia con jueces LLM y reglas de gravedad en 90 diálogos; propuesta española específica, distinta del dataset TEME-v1.

**Loss**

- [CTC — Graves et al.](https://www.cs.toronto.edu/~graves/icml_2006.pdf) — Suma las probabilidades de alineamientos audio–texto sin exigir una etiqueta temporal para cada token.
- [NLL / cross-entropy autoregresiva — Whisper](https://arxiv.org/abs/2212.04356) — Predicción del siguiente token de transcripción condicionada por el audio y los tokens previos.
- [RNN-T / transducer loss](https://arxiv.org/abs/1211.3711) — Objetivo de transducción que combina representaciones acústicas y contexto de salida, relevante para ASR incremental.
- [Masked prediction — HuBERT](https://arxiv.org/abs/2106.07447) — Preentrenamiento autosupervisado que predice unidades acústicas agrupadas en regiones enmascaradas; después se adapta a ASR.
- [Contrastive + diversity loss — wav2vec 2.0](https://arxiv.org/abs/2006.11477) — Preentrenamiento de representaciones acústicas con objetivos contrastivos y cuantización; el ajuste ASR usa CTC.

### Diarization

**Datasets — estándares generales**

- [AMI Meeting Corpus](https://groups.inf.ed.ac.uk/ami/corpus/) — **≈100 h** de reuniones, normalmente de cuatro participantes, con transcripciones y micrófonos cercanos/lejanos; no sumar las duraciones de cada micrófono.
- [DIHARD III](https://arxiv.org/abs/2012.01477) — **34,15 h / 254 grabaciones dev y 33,01 h / 259 eval** en las particiones completas; 11 dominios, incluyendo entrevistas clínicas, sin constituir un corpus español de consultas.
- [VoxConverse](https://www.robots.ox.ac.uk/~vgg/data/voxconverse/) — **Más de 50 h**, según la ficha de los autores, de clips multihablante con tiempos, ruido y solapamiento; fijar release antes de comparar resultados.

**Datasets — aplicación clínica / español**

- [PriMock57: transcripciones](https://github.com/babylonhealth/primock57/tree/main/transcripts) — **57 consultas / 8 h 38 min**, con tiempos y roles clínico/paciente; adaptar el formato y mezclar canales si se evalúa diarización desde un solo micrófono.
- [TEME-v1](https://zenodo.org/records/17280661) — **90 diálogos españoles** con hablantes por turno; candidato a estudiar atribución, pero sus estimaciones temporales no son gold para DER/JER.

**Metrics**

- [DER — dscore](https://github.com/nryant/dscore) — Combina habla omitida, falsas detecciones y confusión de hablantes; reportar tratamiento del solapamiento y collar temporal.
- [JER — dscore](https://github.com/nryant/dscore) — Error basado en intersección/unión de los segmentos de cada hablante, tras resolver la correspondencia entre etiquetas.
- [Benchmarking Diarization Models](https://arxiv.org/abs/2509.26177) — Compara modelos sobre **196,6 h** de cuatro corpora multilingües y desglosa fallos de DER; leer versiones y protocolo antes de reutilizar su ranking.
- [EER — TitaNet](https://arxiv.org/abs/2110.04410) — Evalúa verificación de identidad vocal por embeddings; es una tarea distinta de separar turnos con diarización.

**Loss**

- [PIT + binary cross-entropy — EEND](https://arxiv.org/abs/1909.05952) — Clasificación de actividad por hablante con entrenamiento invariante a permutaciones, incluyendo habla simultánea.
- [Powerset cross-entropy](https://www.isca-archive.org/interspeech_2023/plaquet23_interspeech.html) — Convierte combinaciones de hablantes activos en clases para modelar turnos y solapamientos.
- [Additive angular margin — TitaNet](https://arxiv.org/abs/2110.04410) — Entrena embeddings discriminativos de hablantes usados en verificación y pipelines con clustering.
- [Sort Loss + PIT — Streaming Sortformer](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) — Combina objetivos de orden de aparición e invariancia a permutaciones para seguimiento de hablantes.

### Diarized transcription

**Datasets — estándares generales**

- [AMI Meeting Corpus](https://groups.inf.ed.ac.uk/ami/corpus/) — **≈100 h** de reuniones con texto, tiempos y hablantes; conecta evaluación de ASR y diarización sobre el mismo audio.
- [LibriSpeechMix](https://github.com/NaoyukiKanda/LibriSpeechMix) — **2.703 mezclas dev y 2.620 test por condición** de 2/3 hablantes; horas calculadas desde los manifiestos al final, con solapamiento artificial de audiolibros.

**Datasets — aplicación clínica / español**

- [PriMock57](https://github.com/babylonhealth/primock57) — **57 consultas / 8 h 38 min** en inglés, con texto y roles; permite enlazar atribución de palabras y generación de nota.
- [TEME-v1](https://zenodo.org/records/17280661) — **90 diálogos españoles** con texto y hablantes por turno; comprobar la correspondencia audio–texto antes de usar cpWER, y anotar tiempos para tcpWER.

**Metrics**

- [cpWER — MeetEval](https://github.com/fgnt/meeteval) — Error de transcripción por hablante, minimizado sobre permutaciones de etiquetas para penalizar atribuciones incorrectas.
- [tcpWER — MeetEval](https://github.com/fgnt/meeteval/blob/main/doc/tcpwer.md) — Añade restricciones temporales a cpWER para evaluar texto, hablantes y correspondencia en el tiempo.
- [cpCER y Δcp — MOSS](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize) — Métricas publicadas por MOSS para texto atribuido a hablantes; Δcp es cpCER menos CER, y no equivale a DER.

**Loss**

- [Cross-entropy sobre salida serializada — SOT](https://www.isca-archive.org/interspeech_2020/kanda20b_interspeech.html) — Predicción autoregresiva de texto con separadores de hablante; SOT organiza la secuencia objetivo, no define una loss clínica.
- [Losses por componente — EEND](https://arxiv.org/abs/1909.05952) — En una pipeline modular se entrena la diarización con su objetivo y el ASR con el suyo; propuesta de composición, no una loss única.

### Note generation

**Datasets — estándar general de resumen**

- [CNN/Daily Mail — See et al.](https://aclanthology.org/P17-1099/) — **≈300.000 pares artículo–resumen** en inglés; referencia de resumen abstractivo y copia, con una salida distinta de la nota clínica.

**Datasets — referencias clínicas principales**

- [ACI-Bench](https://github.com/microsoft/clinical_visit_note_summarization_corpus) — **207 encuentros** en inglés: 67 train, 20 validación y tres tests de 40; diálogo–nota y variantes ASR, distribución textual de encuentros simulados.
- [MTS-Dialog](https://github.com/abachaa/MTS-Dialog) — **1.701 pares** de diálogo corto–sección clínica: 1.201 train, 100 validación y 400 test; en inglés, sin audio español grabado.
- [PriMock57](https://github.com/babylonhealth/primock57) — **57 consultas / notas y 8 h 38 min de audio**; notas de los clínicos que hicieron las consultas simuladas en inglés.

**Complementarios — contexto hospitalario y entrenamiento a gran escala**

- [MIMIC-IV-Note v2.2](https://physionet.org/content/mimic-iv-note/2.2/) — **331.794 informes de alta y 2.321.355 informes radiológicos** en inglés; acceso acreditado y sin parejas consulta oral–nota.
- [Corpus privado de Nuance, 2023](https://aclanthology.org/2023.clinicalnlp-1.18/) — **≈900.000 encuentros** en inglés, ≈1.800 profesionales y 27 especialidades; entrenamiento no reproducible con datos abiertos.

**Metrics**

- [ROUGE-1/2/L](https://aclanthology.org/W04-1013/) — Solapamiento léxico y de secuencias con una referencia; mide similitud de redacción, no seguridad clínica.
- [BERTScore](https://arxiv.org/abs/1904.09675) — Compara tokens mediante embeddings contextuales para recoger similitud semántica entre nota y referencia.
- [BLEURT](https://aclanthology.org/2020.acl-main.704/) — Evaluador aprendido de calidad textual, utilizado también en comparaciones de generación de notas.
- [MEDCON — ACI-Bench](https://www.nature.com/articles/s41597-023-02487-3) — Compara conceptos médicos identificados mediante QuickUMLS entre notas generadas y de referencia.
- [PDQI-9 en español](https://pubmed.ncbi.nlm.nih.gov/32570451/) — Instrumento de valoración humana de calidad documental estudiado en notas clínicas españolas; no detecta por sí solo todas las alucinaciones.
- [Evaluación humana y post-edición](https://aclanthology.org/2022.acl-long.394/) — Estudia errores, juicio clínico y tiempo de edición, junto con la correlación de métricas automáticas.
- [Factualidad, omisiones y alucinaciones](https://arxiv.org/abs/2305.17364) — Compara métricas automáticas con hechos clínicos anotados y errores relevantes en generación de notas.

**Loss**

- [Cross-entropy / NLL condicionada — T5](https://jmlr.org/papers/v21/20-074.html) — Objetivo de generación supervisada de texto; aplicable a pares diálogo–nota cuando se adapta un generador.
- [NLL + coverage — pointer-generator](https://aclanthology.org/P17-1099/) — Objetivo general que combina predicción de tokens y penalización de atención repetida; coverage reduce repetición, no certifica factualidad.
- [BRIO](https://aclanthology.org/2022.acl-long.207/) — Objetivo general de ranking contrastivo combinado con CE; antecedente de la loss usada por Nuance para ordenar probabilidades de candidatos según calidad.
- [Loss ponderada de términos médicos — MedicalSum](https://aclanthology.org/2022.findings-emnlp.349/) — Refuerza la predicción de palabras con significado médico en un generador de resúmenes guiado por UMLS.
- [Penalizaciones clínicas — Dr. Summarize](https://aclanthology.org/2020.findings-emnlp.335/) — Añade a NLL/coverage supervisión de atención a conceptos y negaciones y una variante de selección copy/generate/negate.
- [CE + contraste — Nuance](https://aclanthology.org/2023.clinicalnlp-1.18/) — Teacher forcing y ranking de candidatos según ROUGE-L; contrastar su mejora con calidad clínica.
- [DPO, para ampliar después](https://arxiv.org/abs/2305.18290) — Opción de ajuste por preferencias si se recogen pares de notas preferida/rechazada; no es un estándar clínico de partida.

### Context integration / retrieval

**Datasets — estándar general de retrieval**

- [BEIR](https://arxiv.org/abs/2104.08663) — **18 datasets** en la propuesta original, con volúmenes por colección; referencia de recuperación heterogénea, no un único corpus clínico.
- [SciFact dentro de BEIR](https://github.com/beir-cellar/beir) — **≈5.000 documentos y 300 consultas de test**; ejemplo manejable de retrieval científico con relevancia anotada, distinto de recuperar la historia de un paciente.

**Datasets — contexto clínico, por ahora complementarios**

- [MedAlign](https://arxiv.org/abs/2308.14089) — **983 instrucciones, 303 respuestas de referencia y 276 historias longitudinales**; selección y uso de contexto clínico, con acceso condicionado.
- [EHRNoteQA](https://arxiv.org/abs/2402.16040) — **962 pares pregunta–respuesta** ligados a informes de alta de pacientes distintos, revisados por tres clínicos; comprensión de contexto, sin audio.
- [MIMIC-IV-Note v2.2](https://physionet.org/content/mimic-iv-note/2.2/) — **331.794 altas y 2.321.355 informes radiológicos** para experimentar con contexto; preparar relevancia y respetar la fecha del encuentro.

**Metrics**

- [Recall@k / MRR / nDCG — BEIR](https://github.com/beir-cellar/beir) — Métricas generales para comprobar si se recupera y ordena la evidencia necesaria; necesitan relevancia anotada para el caso clínico.
- [Evaluación clínica de respuestas — MedAlign](https://arxiv.org/abs/2308.14089) — Juicio de clínicos sobre respuestas apoyadas en historias, complementario a medir la recuperación de documentos.
- [Procedencia — FHIR Provenance](https://hl7.org/fhir/R4/provenance.html) — Base para proponer comprobaciones locales de origen, fecha y autoría del contexto; es un estándar, no una métrica publicada.

**Loss, si se entrena**

- [Contraste con negativos — DPR](https://arxiv.org/abs/2004.04906) — Optimiza la probabilidad del pasaje relevante frente a pasajes negativos al entrenar un recuperador denso.
- [Objetivo de generación con recuperación — RAG](https://arxiv.org/abs/2005.11401) — Aprende generación condicionada por documentos recuperados; alternativa general, sin validación médica implícita.

### Verification

**Datasets — estándar general de inferencia textual**

- [SNLI v1.0](https://nlp.stanford.edu/projects/snli/) — **≈570.000 pares** de frases en inglés con inferencia/contradicción/neutralidad; introduce la formulación NLI, sin dominio clínico.

**Datasets — referencias clínicas**

- [MedNLI](https://aclanthology.org/D18-1187/) — **14.049 pares**: 11.232 train, 1.395 dev y 1.422 test, anotados clínicamente; acceso mediante PhysioNet y dominio inglés.
- [FactEHR](https://github.com/som-shahlab/factehr) — **2.168 notas, 8.665 descomposiciones, 987.266 pares de entailment y 1.036 ejemplos humanos**; distinguir datos generados y anotación humana, con acceso condicionado.
- [VeriFact-BHC](https://arxiv.org/abs/2501.16672) — **100 pacientes**, con un resumen hospitalario humano y uno generado por paciente; evalúa afirmaciones contra la historia, con anotaciones clínicas y condiciones de acceso.

**Metrics**

- [Clasificación NLI — MedNLI](https://aclanthology.org/D18-1187/) — Evalúa la clasificación entre inferencia, contradicción y neutralidad; su resultado no garantiza completitud de una nota.
- [Respaldo factual y acuerdo clínico — VeriFact](https://arxiv.org/abs/2501.16672) — Compara veredictos de respaldo de afirmaciones contra anotaciones clínicas sobre la historia del paciente.
- [Checklists derivados de feedback](https://aclanthology.org/2025.emnlp-industry.104/) — Convierte comentarios de clínicos en comprobaciones específicas de las notas para una evaluación repetible.
- [Errores SOAP: adiciones, omisiones y contradicciones](https://proceedings.mlr.press/v333/latif26a.html) — Estudio de escribas que contrasta notas generadas con conversación y nota de referencia.

**Loss, si se entrena**

- [Clasificación supervisada — MedNLI](https://aclanthology.org/D18-1187/) — Como opción de diseño, cross-entropy para las tres clases NLI; la verificación mediante prompting no necesita entrenar un clasificador propio.

### End-to-end — evaluación y entrenamiento

Separar tres sentidos: **diálogo textual→nota** (generador seq2seq), **audio + contexto→nota** (modelo con entrada acústica) y **evaluación de todo el flujo** (captura, revisión clínica y HCIS). Evaluar el flujo completo no obliga a entrenarlo con una única loss.

**Datasets / protocolos**

- [PriMock57](https://github.com/babylonhealth/primock57) — **57 consultas / 8 h 38 min**, conectando audio, texto y nota; punto de partida para propagación de errores, sin validar HCIS ni español.
- [ACI-Bench](https://github.com/microsoft/clinical_visit_note_summarization_corpus) — **207 encuentros textuales** con distintas transcripciones; evalúa diálogo→nota y efecto del ASR, sin probar captura ni integración.
- [MedMosaic, para ampliar después](https://proceedings.mlr.press/v306/rajgarhia26a.html) — **46.701 pares pregunta–respuesta** sobre audio médico diverso; no son 46.701 consultas ni notas, y la salida es QA.
- [Evaluación con consultas simuladas](https://www.jmir.org/2025/1/e64993/) — **44 borradores, 22 por producto**, obtenidos de lecturas de guiones clínicos; protocolo de errores, sin dataset público completo anunciado.
- [Framework clínico de evaluación — npj Digital Medicine, 2025](https://doi.org/10.1038/s41746-025-01622-1) — Aplicado a **40 visitas prenatales reales**, de 6–35 min; cubre ASR, diarización y notas, sin anunciar un corpus público de audio listo para usar.

**Metrics**

- [Calidad y tiempo de post-edición](https://aclanthology.org/2022.acl-long.394/) — Combina evaluación de la nota con el trabajo necesario para corregirla, más cercano al objetivo del escriba.
- [Tiempo documental en uso real](https://jamanetwork.com/journals/jama/fullarticle/2847319) — Ejemplo observacional de medición mediante registros de HCE; el ahorro requiere evaluar el flujo asistencial.
- [Evaluación local propuesta](../business_report/appendices/06_evaluacion_piloto.tex) — Calidad, gravedad de errores, contexto y tiempo hasta cierre; propuesta del proyecto, pendiente de protocolo y umbrales.
- [Framework clínico por etapas](https://doi.org/10.1038/s41746-025-01622-1) — Combina métricas automáticas, revisión humana y simulaciones para localizar fallos y probar casos adversos.

**Loss — qué está publicado y qué propondríamos**

- [Diálogo→nota: CE + contraste — Nuance](https://aclanthology.org/2023.clinicalnlp-1.18/) — Seq2seq sobre transcripciones diarizadas, con copia y ranking; sin entrada acústica.
- [Diálogo textual→resumen: términos médicos — MedicalSum](https://aclanthology.org/2022.findings-emnlp.349/) — Ejemplo de objetivo clínico ponderado, frente a tratar todos los tokens por igual.
- [Diálogo textual→resumen: conceptos y negación — Dr. Summarize](https://aclanthology.org/2020.findings-emnlp.335/) — Ejemplo temprano de supervisión clínica adicional; su alcance no equivale a una loss de toda la aplicación.
- [Audio + contexto→nota: NLL condicional, propuesta basada en seq2seq](https://jmlr.org/papers/v21/20-074.html) — Minimizar `−Σ log p(nota_t | nota_<t, audio, contexto)` requeriría pares audio–contexto–nota; esta entrada acústica es una propuesta, no un resultado demostrado por T5.
- [Pipeline modular: objetivos separados — CTC](https://www.cs.toronto.edu/~graves/icml_2006.pdf) / [EEND](https://arxiv.org/abs/1909.05952) / [T5](https://jmlr.org/papers/v21/20-074.html) — ASR, hablantes y generación conservan sus losses; sumar términos solo sirve para entrenamiento conjunto si hay una arquitectura y supervisión que lo permitan.

ROUGE, MEDCON, tiempo de edición y seguridad clínica son medidas de evaluación; usarlas para elegir candidatos o construir preferencias no las convierte automáticamente en losses diferenciables. No hemos establecido una loss universal para el escriba.

## Model architectures

### For transcription

- [Whisper: encoder–decoder Transformer](https://arxiv.org/abs/2212.04356) — Convierte características acústicas en texto autoregresivo; modelo multilingüe general candidato a adaptación clínica.
- [HuBERT](https://arxiv.org/abs/2106.07447) / [wav2vec 2.0](https://arxiv.org/abs/2006.11477) — Encoders preentrenados con autosupervisión; son representaciones que se adaptan a tareas, no escribas completos.
- [Conformer](https://arxiv.org/abs/2005.08100) — Encoder que combina convoluciones y atención; puede integrarse con distintos objetivos y decoders de ASR.
- [MedASR](https://developers.google.com/health-ai-developer-foundations/medasr/model-card) — Conformer con CTC especializado en dictado médico en inglés; esa especialización no acredita conversación clínica en español.
- [Qwen3-ASR](https://arxiv.org/abs/2601.21337) — ASR multilingüe de la familia Qwen, con variantes streaming/offline y alineador aparte; candidato general para evaluar en español médico.

### For diarization

- [pyannote Community-1](https://huggingface.co/pyannote/speaker-diarization-community-1) — Pipeline de segmentación y embeddings/clustering, con ejecución offline y salida exclusiva para facilitar alineación con ASR.
- [EEND](https://arxiv.org/abs/1909.05952) — Red que predice directamente actividad de varios hablantes, incluyendo solapamientos, sin clustering separado.
- [Streaming Sortformer](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) — Diarización incremental con seguimiento de hablantes según orden de aparición.
- [TitaNet](https://arxiv.org/abs/2110.04410) — Encoder convolucional de embeddings para verificación y agrupación de hablantes; componente de una pipeline.

### For diarized transcription

- [MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize) — Audio encoder + LLM autoregresivo para texto, tiempos y hablantes anónimos; las etiquetas no identifican personas reales.
- [VibeVoice-ASR](https://github.com/microsoft/VibeVoice) — Modelo conjunto de transcripción, hablantes y tiempos para audio largo; separar su variante ASR de las variantes TTS.
- [VibeVoice-ASR-Streaming](https://www.microsoft.com/en-us/research/publication/vibevoice-asr-streaming-technical-report/) — Variante de transcripción atribuida a hablantes mientras llega el audio, relevante para latencia y seguimiento incremental.
- [Serialized Output Training](https://www.isca-archive.org/interspeech_2020/kanda20b_interspeech.html) — Familia encoder–decoder que serializa las salidas de varios hablantes para reconocer habla solapada.

### For generation

- [LLMs y baselines de ACI-Bench](https://www.nature.com/articles/s41597-023-02487-3) — Generación de notas desde diálogo con modelos de lenguaje; sirve para discutir prompting y rendimiento por secciones.
- [T5](https://jmlr.org/papers/v21/20-074.html) — Encoder–decoder text-to-text como base para adaptar generación de diálogo a nota.
- [BART](https://aclanthology.org/2020.acl-main.703/) — Encoder–decoder con preentrenamiento por reconstrucción de texto, utilizado para resumen abstractivo.
- [CLUSTER2SENT](https://aclanthology.org/2021.acl-long.384/) — Enfoque clínico modular que selecciona intervenciones, agrupa información y genera frases por sección SOAP.
- [Seq2seq clínico — Nuance](https://aclanthology.org/2023.clinicalnlp-1.18/) — Transformer con copia, condicionado por especialidad y profesional.
- [MedicalSum](https://aclanthology.org/2022.findings-emnlp.349/) — Generación guiada por conceptos/tipos semánticos UMLS y loss médica ponderada; antecedente para discutir relevancia y copia.
- [LoRA](https://arxiv.org/abs/2106.09685) — Método de adaptación eficiente de parámetros, aplicable a un generador; no es una arquitectura ni una loss distinta.

### For context integration / retrieval

- [DPR: dual encoder](https://arxiv.org/abs/2004.04906) — Recuperación de pasajes mediante embeddings; componente general para seleccionar contexto de una historia extensa.
- [RAG](https://arxiv.org/abs/2005.11401) — Combina recuperador y generador para condicionar la salida en fuentes externas.
- [MedAlign](https://arxiv.org/abs/2308.14089) — Experimentos con instrucciones e historias longitudinales para estudiar cuánto contexto necesita el modelo y cómo lo utiliza.
- [FHIR DocumentReference](https://hl7.org/fhir/R4/documentreference.html) — Estándar para documentos y metadatos clínicos; la compatibilidad efectiva con HCIS necesita comprobarse aparte.

### For verification

- [VeriFact](https://arxiv.org/abs/2501.16672) — Descompone texto en afirmaciones, recupera evidencia de la historia y verifica su respaldo mediante LLMs.
- [MedNLI](https://aclanthology.org/D18-1187/) — Formulación de verificación como inferencia/contradicción/neutralidad; cubre relaciones textuales, no toda la calidad clínica.
- [Evaluación mediante checklists](https://aclanthology.org/2025.emnlp-industry.104/) — Comprobaciones generadas a partir de feedback clínico para evaluar el contenido de cada nota.

### For everything — audio + contexto → nota

- [Qwen3-Omni](https://arxiv.org/abs/2509.17765) — Modelo multimodal Thinker–Talker MoE que admite audio y texto; sus benchmarks generales no establecen calidad de notas médicas españolas.
- [Qwen3.5-Omni](https://arxiv.org/abs/2604.15804) — Informe posterior de la misma línea, relevante para actualizar la comparación de capacidades multimodales.
- [MOSS: alcance de la tarea](https://arxiv.org/abs/2601.01554) — Su tarea publicada es transcripción con hablantes y tiempos; la generación y verificación de la nota requieren una etapa adicional.

## Deployment — fuentes para el bloque técnico

- [getUserMedia — MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) — Captura de micrófono en navegador, permisos y restricciones del dispositivo.
- [AudioWorklet — MDN](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet) — Procesamiento de audio fuera del hilo principal para construir captura y envío con baja latencia.
- [WebRTC — W3C](https://www.w3.org/TR/webrtc/) — Estándar de comunicación multimedia en tiempo real para estudiar transporte de audio y comportamiento de la conexión.
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) — Runtime de Whisper para ejecución local en distintas plataformas, con opciones de cuantización.
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) — Inferencia de Whisper mediante CTranslate2, útil para comparar precisión, memoria y velocidad con el runtime final.
- [vLLM](https://github.com/vllm-project/vllm) — Serving de LLMs con batching y formatos de cuantización; compatibilidad según modelo, hardware y versión.
- [FHIR Provenance](https://hl7.org/fhir/R4/provenance.html) — Registro de procedencia y actividades sobre documentos, útil para trazabilidad de contexto y notas.
- [OpenTelemetry: Gen AI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) — Convenciones de telemetría para identificar modelo, operación y uso de tokens en sistemas generativos.
- [Guía NHS sobre escribas ambientales](https://www.england.nhs.uk/long-read/guidance-on-the-use-of-ai-enabled-ambient-scribing-products-in-health-and-care-settings/) — Implementación, revisión clínica y gobierno de datos de escribas; marco británico, no normativa española.

## Comprobaciones de volumen y anotaciones

- **TEME-v1:** inspección del [ZIP original](https://zenodo.org/records/17280661) el 08/10/2026: 90 MP3, 90 JSON, 2.330 turnos y dos hablantes por diálogo; **3,96 h de audio** sumando `format.duration` de `ffprobe` (media ≈2 min 38 s, rango ≈1 min 24 s–5 min 4 s). Es una medición nuestra, no una cifra publicada por los autores.
- **TEME y diarización:** los turnos contienen `speaker`, `text`, `duration_estimate` y `voice_characteristics`; no contienen inicios/finales temporales. La ficha describe configuración de síntesis: tratarlo como recurso construido, sin asumir consultas espontáneas grabadas. Sí interesa para ASR clínico español y texto con hablantes; para DER/JER habría que producir y revisar un alineamiento temporal, y para cpWER comprobar fidelidad audio–texto. `context` es un resumen del escenario, no una nota SOAP ni una historia HCIS.
- **Origen del audio TEME:** el [paper de AAMAS](https://doi.org/10.65109/RHNT7438), recuperado de tu Zotero, especifica 23 consultas reales anonimizadas y 67 diálogos sintéticos como origen del texto; **el audio se generó con Gemini TTS**. La degradación a 8 bits/8 kHz pertenece a su experimento, no se presupone como formato de todos los MP3 publicados. Multihablante sí; acústica espontánea real, no.
- **LibriSpeechMix:** recuento propio de los [manifiestos oficiales](https://github.com/NaoyukiKanda/LibriSpeechMix/tree/master/list): 2.703 mezclas dev y 2.620 test en cada condición. Sumando `max(delay + duration)` por mezcla: **2 hablantes ≈8,60 h dev / 8,72 h test; 3 hablantes ≈11,77 h dev / 11,81 h test**. Son duraciones calculadas de mezclas, no horas independientes de nuevos hablantes; ambas condiciones reutilizan LibriSpeech.

Las entradas repetidas en distintas tareas corresponden al mismo corpus. Los datasets de contexto/verificación son mayormente textuales y en inglés; sus unidades se conservan como documentos, pacientes o pares, sin inventar equivalencias en horas.

## Revisión de tu Zotero de Windows

Revisión en lectura de la colección **Digital Escriber (`YYTP79GR`)** el 08/10/2026: **75 entradas**, frente a las 47 del catálogo del 11/09/2026; **28 claves añadidas y ninguna ausente**. No equivalen a 28 estudios únicos: hay duplicados y PDF independientes. Se consultó una copia consistente de la base actual y los adjuntos relevantes, sin modificar Zotero.

El seq2seq que mencionabas es [Singh et al., 2023, de **Nuance Communications**](https://aclanthology.org/2023.clinicalnlp-1.18/) (`9KBENXJ5`, añadido el 07/10/2026). Sirve como antecedente de entrenamiento, sin acreditar rendimiento actual.

El [inventario de añadidos y la revisión de material](zotero-revision.md) indica qué fuentes conviene leer para cada bloque, cuáles solo se revisaron por metadatos y qué incidencias bibliográficas aparecieron.

## Referencias incorporadas en la revisión del 12/10/2026

- [Parakeet TDT 0.6B v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) — Ejemplo actual de transducer con predicción de duraciones; no todas las familias ASR han sido sustituidas por atención.
- [Qwen3-0.6B GGUF oficial](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/tree/main) — Archivo Q8_0 de 639 MB como candidato pequeño; tamaño en disco, no RAM total ni validación clínica.
- [MOSS: selección de dispositivo](https://github.com/OpenMOSS/MOSS-Transcribe-Diarize/blob/main/moss_transcribe_diarize/inference_utils.py) — Ruta CPU/GPU verificable en código; queda pendiente medir rendimiento en el PC objetivo.
- [Contexto longitudinal frente a audio solo](https://doi.org/10.1101/2025.11.07.25339620) — Preprint con 354 encuentros y mayor completitud; límites en la ficha de comprensión clínica.
- [Tandem: dirección de producto](https://tandemhealth.ai/resources/news/building-the-ai-native-operating-system-for-european-clinics) — Preparación, documentación, apoyo clínico, codificación y seguimiento como expansión comercial; distinguir roadmap de disponibilidad y eficacia.
