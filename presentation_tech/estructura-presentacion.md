# Estructura provisional — construir un escriba digital médico

Draft de trabajo, actualizado el **12/10/2026**. Aquí está el hilo y una bolsa de lecturas por sección; el [catálogo de datasets, métricas, losses y arquitecturas](README.md) queda separado. La [presentación renovada](build/main.pdf) concreta este material en **31 diapositivas / unos 30 minutos**, más cinco anexos; [guion con mensajes, transiciones y tiempos](guion-presentacion.md).

Hilo: **consulta y nota → evaluación y datos → audio y hablantes → diálogo, contexto y nota → adaptación y despliegue → primer experimento**. En cada tarea, explicar qué se resuelve, cómo se modela y cómo se mide. Los modelos recientes sirven para comparar alternativas, sin asumir SOTA clínica.

| Bloque | Diapositivas | Tiempo | Acumulado |
|---|---|---:|---:|
| Consulta y nota | 1–6 | 3:40 | 3:40 |
| Evaluación y datos | 7–8 | 1:55 | 5:35 |
| Audio y hablantes | 9–17 | 9:25 | 15:00 |
| Diálogo, contexto y nota | 18–24 | 7:40 | 22:40 |
| Adaptación y despliegue | 25–29 | 5:25 | 28:05 |
| Plan de trabajo | 30–31 | 1:55 | 30:00 |



Las secciones siguientes son una bolsa de lectura más amplia que el PDF. Las losses quedan en el anexo B; los hechos intermedios en C y la ampliación de datos en D.

Apoyos breves para preparar estos bloques: [common challenges](common_challenges.md) y [contexto de la nota clínica](clinical_note_context.md).

## 1. Contexto: por qué y qué es un escriba

- Carga documental y trabajo que queremos reducir.
- Borrador de nota a partir de consulta y contexto clínico, con revisión del profesional.
- Distinguir dictado, transcripción y documentación clínica; definir dónde empieza y termina nuestra aplicación.

**Lecturas para empezar**

- [Guía NHS sobre escribas ambientales](https://www.england.nhs.uk/long-read/guidance-on-the-use-of-ai-enabled-ambient-scribing-products-in-health-and-care-settings/) — Da una definición operativa y sitúa la revisión clínica y el flujo de trabajo; usar como guía británica, no como norma española.
- [Tiempo documental en uso real — JAMA](https://jamanetwork.com/journals/jama/fullarticle/2847319) — Ayuda a elegir una medida de utilidad asistencial; separar asociación observacional de efecto causal.
- [Informe business del proyecto](../business_report/notes/analisis-escribas-digitales.md) — Recuperar el contexto y la evidencia ya trabajados para dedicar el bloque técnico a las decisiones de construcción.

## 2. Caracterizar la consulta y la nota

- Plataforma: web, móvil, escritorio; dónde y con qué micrófono se consulta.
- Entrada: participantes, lenguaje coloquial/médico, duración, disfluencias, silencios y solapamientos.
- Contexto adicional: antecedentes, medicación, resultados y observaciones; procedencia, fecha y disponibilidad.
- Salida: qué seleccionar, cómo escribirlo y qué corresponde a S/O/A/P; no atribuir al modelo diagnósticos que el clínico no expresó.

**Lecturas para empezar**

- [PriMock57](https://arxiv.org/abs/2204.00333) — Sus **57 consultas / 8 h 38 min** y notas permiten ver una entrada y una salida concretas, con turnos y variación de longitud.
- [Jurafsky y Martin, cap. 15](https://web.stanford.edu/~jurafsky/slp3/15.pdf) — Fonética, prosodia y variación de habla dan contexto a lo que el micrófono captura; mirar ejemplos de habla espontánea.
- [ACI-Bench](https://github.com/microsoft/clinical_visit_note_summarization_corpus) — **207 encuentros textuales** para comparar diálogo y secciones de la nota, teniendo presente que son simulados y en inglés.
- [SOAP Notes](https://www.ncbi.nlm.nih.gov/books/NBK482263/) — Referencia de tu Zotero para definir S/O/A/P antes de mostrar el ejemplo de nota.
- [The anatomy of clinical documentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/) — Análisis de **80 notas** de primaria y especialidades; justifica que contenido y formato de salida necesitan una definición concreta.

**Para ampliar después**

- [Buckeye Corpus](https://buckeyecorpus.osu.edu/) — **40 hablantes / ≈300.000 palabras**: ejemplo general de reducción fonética y disfluencias, citado por Jurafsky, útil para entender la diferencia con habla leída.
- [Communication in Medical Care](https://doi.org/10.1017/CBO9780511607172) / [RIAS](https://doi.org/10.1016/S0738-3991(02)00012-5) — Fuentes de tu Zotero para caracterizar fases y funciones del diálogo médico, más allá de contar palabras y turnos.
- [MedAlign](https://arxiv.org/abs/2308.14089) — **983 instrucciones / 276 historias / 303 respuestas** para explorar la complejidad de incorporar contexto longitudinal.

## 3. Cómo saber si funciona

- Evaluar la nota y el flujo completo; evaluar las partes para localizar errores.
- Mostrar controles generales y referencias clínicas, aclarando qué contiene cada dataset y cuánto dato aporta.
- WER/CER, DER/JER, cpWER/tcpWER y métricas de nota; no comparar números calculados con protocolos diferentes.
- Calidad clínica: adiciones, omisiones, contradicciones, negación, dosis, temporalidad y atribución.
- Contexto: paciente correcto, fuente/fecha, datos antiguos y discrepancias; tiempo de revisión y cierre.
- Separar inglés clínico, español general y español clínico; reservar evaluación local para el uso objetivo.

**Lecturas para empezar**

- [Evaluación humana y post-edición — Moramarco et al.](https://aclanthology.org/2022.acl-long.394/) — Leer primero para entender por qué una nota que se parece a la referencia puede requerir mucho trabajo clínico.
- [Framework clínico de evaluación — npj Digital Medicine](https://doi.org/10.1038/s41746-025-01622-1) — **40 visitas prenatales reales**: conecta métricas por etapa, evaluación humana y simulaciones en un diseño de evaluación de escriba.
- [PriMock57](https://arxiv.org/abs/2204.00333) — **57 consultas / 8 h 38 min**: enlaza evaluación de ASR, conceptos clínicos y nota en los mismos casos.
- [ACI-Bench](https://github.com/microsoft/clinical_visit_note_summarization_corpus) — **207 encuentros**: estudiar sus baselines y evaluación por secciones antes de decidir una métrica única de generación.
- [DIHARD III](https://arxiv.org/abs/2012.01477) — **34,15 h dev / 33,01 h eval** en full: ejemplo claro de cómo collar, solapamiento y segmentación de referencia cambian el DER.
- [MeetEval](https://github.com/fgnt/meeteval) — Aclara cómo medir conjuntamente palabras y hablantes, y por qué WER y DER separados no cuentan toda la historia.

**Para ampliar después**

- [TEME-v1](https://zenodo.org/records/17280661) — **90 diálogos / ≈3,96 h medidas por nosotros**: primer recurso español médico, con límites de anotación explicados en el catálogo.
- [VeriFact](https://arxiv.org/abs/2501.16672) — **100 pacientes con resúmenes humanos/generados** para evaluar respaldo en EHR y distinguir falta de evidencia de contradicción.
- [Protocolo de errores en escribas — JMIR](https://www.jmir.org/2025/1/e64993/) — **44 borradores** evaluados: ayuda a definir una taxonomía de errores para nuestra comparación local.
- [TEME: evaluación de ASR español](https://doi.org/10.65109/RHNT7438) — Distinguir su juez clínico LLM del corpus de **90 diálogos**; leer como propuesta específica después de las métricas habituales.

## 4. Cómo pasar de audio y contexto a una nota

Modelo de trabajo: **audio → ASR/atribución de hablantes → selección y generación → comprobación del borrador → revisión clínica → HCIS**, incorporando contexto clínico y observaciones en la generación. La selección puede producir hechos explícitos o quedar dentro del LLM. La comprobación aporta señales de soporte/conflicto y necesita evaluación propia.

### 4.1 Captura y representación acústica

- Señal, muestreo, canales, ruido, frames, espectrograma y log-Mel; qué recibe realmente el modelo.
- VAD/segmentación y pérdida de información al recortar o transmitir audio.

**Lecturas**

- [Jurafsky y Martin, cap. 15, §§15.4–15.6](https://web.stanford.edu/~jurafsky/slp3/15.pdf) — Lectura principal para dibujar waveform→frames→espectrograma→características sin convertirlo en un curso de DSP.
- [Davis y Mermelstein, 1980](https://doi.org/10.1109/TASSP.1980.1163420) — Antecedente citado en el capítulo para explicar MFCC; opcional si necesitamos profundizar en features.
- [getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) / [AudioWorklet](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet) — Conecta la señal ideal del modelo con captura y procesamiento real en una web.

### 4.2 Transcripción

- Definir audio→texto y su alineamiento; separar architecture, loss y decoding.
- CTC, encoder–decoder autoregresivo y transducer; autosupervisión como preentrenamiento.
- Qué cambia en consulta: acentos, nombres de fármacos, cifras, unidades y coloquialismos.

**Lecturas**

- [Jurafsky y Martin, cap. 16](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — Primera lectura para comparar las familias de ASR y entender WER y alineamientos.
- [End-to-End Speech Recognition: A Survey](https://arxiv.org/abs/2303.03329) — Segunda lectura de tu Zotero para profundizar en alineamiento, losses, decoding y streaming.
- [CTC — Graves et al.](https://www.cs.toronto.edu/~graves/icml_2006.pdf) / [Whisper](https://arxiv.org/abs/2212.04356) — Dos formulaciones centrales de entrenamiento; leer sus entradas, salidas y objetivos antes de comparar tamaños.
- [HuBERT](https://arxiv.org/abs/2106.07447) — Entender cómo se aprende del audio sin transcripción y por qué eso aún requiere adaptación para ASR.
- [Medical WER y recuperación de entidades](https://arxiv.org/abs/2406.12387) — Explica qué puede ocultar un buen WER global cuando se transcriben términos médicos.

### 4.3 Quién dice qué y cuándo

- Diarización, transcripción con hablantes, rol médico/paciente e identidad son tareas diferentes.
- Segmentación→embeddings→clustering frente a predicción conjunta; solapamiento y cambios de turno.
- Atribuir mal un síntoma o una recomendación puede cambiar el significado de la nota.

**Lecturas**

- [pyannote Community-1](https://huggingface.co/pyannote/speaker-diarization-community-1) — Baseline modular ejecutable para conectar segmentación, embeddings y agrupación.
- [EEND](https://arxiv.org/abs/1909.05952) / [powerset](https://www.isca-archive.org/interspeech_2023/plaquet23_interspeech.html) — Entender PIT/BCE y clasificación de combinaciones de hablantes, sobre todo para solapamientos.
- [Serialized Output Training](https://www.isca-archive.org/interspeech_2020/kanda20b_interspeech.html) — Puente hacia reconocimiento conjunto: el texto incluye cambios de hablante en su secuencia objetivo.
- [MOSS-Transcribe-Diarize](https://arxiv.org/abs/2601.01554) — Comparar una alternativa reciente conjunta; sus hablantes son etiquetas anónimas y su salida publicada es transcripción, tiempos y hablantes.
- [Benchmarking Diarization Models](https://arxiv.org/abs/2509.26177) — **196,6 h** de cuatro conjuntos: leer su descomposición de errores y límites por número de hablantes antes de elegir una pipeline.

### 4.4 Selección de hechos y contexto clínico

- Distinguir extracción de hechos del diálogo y recuperación de registros externos.
- Contexto corto: consulta estructurada o selección fija; historia extensa: comparar recuperación de fragmentos.
- Relevancia, fecha, paciente, negación, incertidumbre y origen de cada hecho; qué hacer cuando las fuentes discrepan.

**Lecturas**

- [Ficha de conversación, contexto y hechos](comprension-clinica.md) — Leer primero: separa tareas y explica qué prueban las referencias siguientes.
- [ASCRIBE](https://arxiv.org/abs/2610.01234) — Hechos, fragmentos de soporte y relevancia antes de SOAP; estudiar §3.1 y prompt A.3, teniendo presentes sus límites de idioma y evaluación.
- [KOSMOS](https://doi.org/10.3390/info17040355) — Entidades, atributos y relaciones con procedencia; comparar nodos frente a grafo y revisar las mejoras modestas.
- [Nuance, §3.1.2](https://aclanthology.org/2023.clinicalnlp-1.18/) — Chain-of-Clinical-Facts como prefijo generativo; ≈900.000 encuentros privados, sin retrieval HCIS.
- [DPR](https://arxiv.org/abs/2004.04906) / [RAG](https://arxiv.org/abs/2005.11401) — Estándares generales para separar recuperación y generación; leerlos antes de diseñar retrieval específico de HCIS.
- [MedAlign](https://arxiv.org/abs/2308.14089) — **983 instrucciones / 276 historias / 303 respuestas**: referencia clínica para ver que más contexto no implica necesariamente mejor uso del contexto.
- [FHIR DocumentReference](https://hl7.org/fhir/R4/documentreference.html) / [Provenance](https://hl7.org/fhir/R4/provenance.html) — Fundamenta metadatos y trazabilidad; no demuestra que un proveedor tenga conector con nuestro HCIS.

### 4.5 De diálogo a nota

- Selección de información, extracción/copia y generación; estructura SOAP y estilo del servicio.
- Encoder–decoder y LLMs; prompting frente a adaptación; qué supervisión tenemos.

**Lecturas**

- [T5](https://jmlr.org/papers/v21/20-074.html) / [BART](https://aclanthology.org/2020.acl-main.703/) — Bases de generación textual para entender seq2seq antes de aplicar el método a notas.
- [Pointer-generator](https://aclanthology.org/P17-1099/) — Copia y coverage como respuesta a nombres raros y repetición; útil como antecedente, sin confundir copia con seguridad clínica.
- [CLUSTER2SENT](https://aclanthology.org/2021.acl-long.384/) — Alternativa que selecciona y agrupa intervenciones antes de generar frases SOAP; muestra que hay opciones intermedias entre extracción y LLM directo.
- [Nuance: seq2seq clínico](https://aclanthology.org/2023.clinicalnlp-1.18/) — **≈900.000 encuentros privados**: leer copia y cadena de hechos sobre transcripción ASR.

### 4.6 Verificación y revisión clínica

- Verificar contra conversación y contexto: respaldo de hechos, contradicciones y omisiones.
- Verificación automática y esfuerzo del clínico; una nota respaldada puede seguir siendo incompleta.

**Lecturas**

- [MedNLI](https://aclanthology.org/D18-1187/) — **14.049 pares clínicos**: formulación básica para entender inferencia, contradicción y neutralidad.
- [VeriFact](https://arxiv.org/abs/2501.16672) — Recuperación de evidencia y verificación por afirmaciones; ayuda a concretar el bloque de comprobación.
- [Checklists derivados de feedback clínico](https://aclanthology.org/2025.emnlp-industry.104/) — Conecta las correcciones de usuarios con comprobaciones repetibles de contenido.

## 5. Cómo entrenar y dónde ejecutar

- Qué necesitamos adaptar y qué podemos usar ya; volumen, disponibilidad y calidad de las etiquetas.
- Loss por componente frente a entrenamiento conjunto; distinguir texto→nota y audio→nota.
- Entrenamiento e inferencia pueden ocurrir en lugares distintos; hardware, memoria, latencia, cuantización y streaming.
- Evaluar el artefacto con el runtime, versión y configuración que desplegaremos; medir calidad junto a velocidad/memoria.

**Lecturas para empezar**

- [Nuance: CE + contraste](https://aclanthology.org/2023.clinicalnlp-1.18/) — Revisar su ranking con ROUGE-L frente a los criterios clínicos finales.
- [BRIO](https://aclanthology.org/2022.acl-long.207/) — Lectura base si queremos entender la loss de ranking que ese trabajo combina con CE.
- [MedicalSum](https://aclanthology.org/2022.findings-emnlp.349/) / [Dr. Summarize](https://aclanthology.org/2020.findings-emnlp.335/) — Objetivos que priorizan términos, conceptos y negación; antecedentes para responder qué aporta una loss clínica.
- [LoRA](https://arxiv.org/abs/2106.09685) — Adaptación de pocos parámetros; leer para decidir qué entrenar con nuestros recursos, manteniendo clara su diferencia con una loss.
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) / [faster-whisper](https://github.com/SYSTRAN/faster-whisper) — Dos runtimes para hacer concretas las restricciones locales y la evaluación de la configuración final.
- [vLLM](https://github.com/vllm-project/vllm) — Referencia de serving para discutir batching, memoria y cuantización del generador.

**Para ampliar después**

- [Qwen3-Omni](https://arxiv.org/abs/2509.17765) — Explorar la alternativa audio+texto→salida textual; el informe no acredita notas clínicas españolas ni elimina la necesidad de evaluar cada fallo.
- [DPO](https://arxiv.org/abs/2305.18290) — Solo profundizar si decidimos recopilar preferencias clínicas con las que ajustar el generador.

## 6. Despliegue, integración y operación

- Elegir plataforma y captura: web, móvil, escritorio, micrófono USB/Bluetooth, teléfono; canales y ruido.
- Transporte: WebRTC/WebSocket; tolerancia a interrupciones y latencia del flujo completo.
- Ejecución local, remota o mixta; qué se transmite, almacena y elimina.
- Lectura de contexto y escritura de borrador aprobado en HCIS; versiones y trazabilidad.
- Monitoring: latencia, fallos, cambios de modelo y calidad sobre casos revisados; evitar registrar texto clínico innecesario.

**Lecturas para empezar**

- [getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) / [WebRTC](https://www.w3.org/TR/webrtc/) — Base de captura y transporte web; comprobar qué parte del flujo depende de navegador, dispositivo y conexión.
- [FHIR DocumentReference](https://hl7.org/fhir/R4/documentreference.html) / [Provenance](https://hl7.org/fhir/R4/provenance.html) — Modelo de documento y procedencia para formular requisitos concretos del conector HCIS.
- [OpenTelemetry: Gen AI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) — Campos de telemetría para rastrear modelo y operaciones; tomar una selección mínima adecuada a datos clínicos.
- [Guía NHS sobre escribas](https://www.england.nhs.uk/long-read/guidance-on-the-use-of-ai-enabled-ambient-scribing-products-in-health-and-care-settings/) — Une gobierno de datos, responsabilidad y seguimiento de la calidad con el uso asistencial.

## 7. Cierre: qué construir y evaluar primero

- Elegir un caso de uso local y formato de nota; fijar entrada, contexto y salida esperada.
- Baseline modular, datasets estándar y evaluación clínica de un conjunto español preparado para el caso de uso.
- Comparar variantes con el mismo protocolo; decidir qué adaptar según los fallos medidos.
- Pilotar con revisión clínica y registrar calidad, edición y comportamiento operativo.

Primer conjunto propuesto: TEME para explorar ASR español, PriMock57 para comprobar el protocolo end-to-end en inglés, diez casos con contexto y cinco adaptaciones al español revisadas. Son cantidades de viabilidad, no validación clínica. El runner de evaluación ampliaría el core de Scribnic; contexto HCIS y cliente de revisión siguen pendientes.

Ampliación del cierre: [bag of ideas](bag-of-ideas.md), con simulación de historia/contexto, audio y consulta, adaptación de PriMock57 y evaluación de revisiones; una síntesis aparece en el anexo D.

**Lecturas**

- [Propuesta de evaluación del proyecto](../business_report/notes/opciones-evaluacion-piloto.md) — Recuperar los criterios del trabajo business y convertirlos en un protocolo técnico.
- [Catálogo técnico](README.md) — Elegir de aquí el primer corpus, métrica, modelo y objetivo por tarea; dejar los recursos complementarios para los fallos que aparezcan.

La [revisión de Zotero](zotero-revision.md) compara la biblioteca actual de Windows con el catálogo antiguo: identifica 28 entradas añadidas, los duplicados y el material efectivamente revisado. Las fuentes nuevas prioritarias ya aparecen en las bolsas de lectura anteriores.
