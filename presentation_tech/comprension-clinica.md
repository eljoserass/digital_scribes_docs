# De la conversación y la historia a los hechos de la nota

Ficha de estudio del **10/10/2026**. La caja «comprensión clínica» del primer borrador agrupaba varias operaciones. La presentación renovada separa selección de hechos, acceso al contexto y comprobación del borrador. Todavía tenemos que decidir cuáles hacer explícitas y cuáles dejar al generador.

## Qué tarea hay dentro de esa caja

| Operación | Entrada → salida | Ejemplo |
|---|---|---|
| Obtener contexto | Paciente/episodio → registros disponibles | Medicación, alergias, resultados o notas previas. |
| Seleccionar evidencia | Consulta y registros → información pertinente | Elegir el estado reciente de un tratamiento, conservando su fuente. |
| Extraer y atribuir hechos | Texto → afirmaciones con atributos | «Mi madre toma X» corresponde a la madre, no al paciente. |
| Interpretar estado y discrepancias | Afirmaciones fechadas → estado documentado o conflicto | Tratamiento registrado como activo, pero el paciente dice haberlo suspendido. |
| Escribir la nota | Información seleccionada + plantilla → borrador | Ordenar lo referido, lo observado y la valoración/plan expresados. |

**Retrieval** selecciona registros o fragmentos. **Extracción** representa lo que dicen. **Generación** decide cómo documentarlo. Una sola llamada a un LLM puede combinar varias operaciones, pero seguimos necesitando comprobar cada comportamiento.

Incluir contexto en el prompt no exige siempre búsqueda vectorial: para una historia corta puede bastar una consulta estructurada o selección fija. RAG cobra sentido cuando necesitamos recuperar una parte de una historia extensa. Primero se identifica paciente y encuentro y se fija el corte temporal; se conservan antecedentes relevantes de otros episodios. La similitud semántica no debe decidir de quién es el registro.

## Un ejemplo que podríamos defender

Conversación: «Desde hace tres días tengo tos; fiebre no». El médico dice: «Está en mejoría; revisión en siete días». La historia aporta una alergia registrada en 2019. Una observación aporta temperatura de hoy.

Podemos representar cada dato con:

`hecho · persona · negación/incertidumbre · momento/estado · fuente`

Esto permite distinguir ausencia de fiebre referida y temperatura medida. El sistema conserva la valoración del médico y su plan. Cuando una fuente no determina si un dato sigue vigente, necesitamos conservar esa incertidumbre o pedir revisión.

Ese formato es una **propuesta de contrato**, no una representación clínica universal ni un módulo que ya tengamos implementado. Su ventaja potencial es poder inspeccionar qué se seleccionó; el coste es que una extracción incompleta puede perder información antes de generar.

## Tres formas de implementarlo

| Ruta | Cómo funciona | Qué comparar |
|---|---|---|
| Generación directa | Transcripción + contexto disponible + instrucciones/plantilla → nota. | Baseline sencillo; hechos conservados, añadidos y uso del contexto. |
| Hechos intermedios | Extraer hechos con fuentes → seleccionar/ordenar → nota; probar también conservando la transcripción original. | Si mejora fidelidad o inspección y cuánto añade de latencia, coste y omisiones de extracción. |
| Estructura más rica | Entidades, atributos y relaciones → representación estructurada + transcripción → nota. | Si las relaciones aportan algo frente a una lista de hechos más sencilla. |

Las dos últimas son hipótesis para comparar con la primera. Ni una lista ni un grafo garantizan que la nota sea correcta.

## Qué aporta realmente el antecedente de Nuance

[Singh et al., 2023, §3.1.2](https://aclanthology.org/2023.clinicalnlp-1.18/) es de **Nuance Communications**. Durante entrenamiento extraen hechos de las notas de referencia con una herramienta propietaria y los anteponen como objetivos. En inferencia, el decoder genera ese prefijo desde la transcripción y después la nota. **Chain-of-Clinical-Facts es planificación intermedia de generación; no retrieval de HCIS.**

El corpus de **≈900.000 encuentros es propietario**, no un dataset público disponible para nosotros. El trabajo sigue siendo útil para formular la comparación directo/frente a hechos, aunque no adoptaríamos automáticamente su arquitectura de 2023.

## Dos referencias recientes para estudiar ese paso

**[KOSMOS — Henry y Gong, 2026](https://doi.org/10.3390/info17040355)**, publicado en *Information*. Extrae menciones de la transcripción, las agrupa en entidades con atributos, normaliza con UMLS y añade relaciones y procedencia por turno. Compara grafo solo, transcripción + nodos y transcripción + grafo con baselines de generación. Es estructura extraída del encuentro, no recuperación de historia externa. Las mejoras son modestas; varias comparaciones no son significativas y la extracción no se evalúa independientemente. No demuestra ahorro de revisión clínica.

**Leer:** §2 y figuras 2–4 para entender entradas/artefactos; después discusión y limitaciones. Pregunta: ¿necesitamos relaciones o basta con nodos/hechos? [Código](https://github.com/ryanwaynehenry/KOSMOS).

**[ASCRIBE — Kalavantavanich et al., 2026](https://arxiv.org/abs/2610.01234)**, preprint del 1 de octubre. Genera hechos atómicos, fragmentos de soporte y niveles de relevancia clínica antes de la nota, en una misma secuencia. Estudia prompting y adaptación con rewards; incluye un benchmark externo de **44 encuentros tailandeses**. Es una referencia cercana a la pregunta «¿cómo seleccionamos lo importante?». La evaluación usa jueces LLM; su alineamiento clínico se valida con una muestra limitada y un solo médico, y parte de las métricas también se usa como reward. No trasladar sus resultados al español.

**Leer:** §3.1, figura 1 y prompt del apéndice A.3; después limitaciones. Pregunta: ¿qué decide el modelo y qué criterios aportaron médicos? [Prompts publicados](https://github.com/loolootech/ascribe/tree/main/prompts).

## ¿La historia mejora la nota?

Puede aportar información que no se repite en el encuentro, como el tratamiento al que se refiere «seguir igual». Recuperarla exige identificar paciente, fecha y estado; incluir más texto también puede introducir datos antiguos o contradictorios.

[Zuckerman et al., 2025 — Ambient Only vs. Longitudinal Data-Enhanced AI Documentation](https://doi.org/10.1101/2025.11.07.25339620) compara **354 encuentros de atención primaria**: nota ambient frente a una consolidación posterior que añade historia, selección de evidencia y generación con Claude Sonnet 4. Encuentra mejores puntuaciones de completitud, pero **no aísla el efecto de añadir historia** manteniendo el resto constante. Es un preprint con evaluación principalmente automática, auditoría humana limitada y autores vinculados al proveedor. No documenta suficientemente que se mantuviera el mismo generador. El resumen y el texto completo también difieren al describir el tamaño de la revisión humana.

Nuance y ASCRIBE sí comparan generación directa y planificación mediante hechos, pero extraídos del propio encuentro. ACI-Bench y PriMock no aportan un benchmark longitudinal con/sin HCIS; MIMIC tiene historia, pero no esas conversaciones emparejadas. **La pregunta sigue abierta para nuestro caso.** La [ficha de evidencia sobre contexto](evidencia-contexto-notas.md) reúne las comparaciones, resultados y límites de cada corpus.

Nuestro experimento tendría los mismos encuentros, generador y plantilla: sin historia, con historia pertinente seleccionada manualmente y con recuperación automática. Anotaríamos hechos esperados y comprobaríamos procedencia, vigencia, contradicciones y esfuerzo de revisión. Así separaríamos el valor de la información del comportamiento del recuperador.

## Dónde queda MedAlign

[MedAlign](https://arxiv.org/abs/2308.14089) contiene instrucciones de clínicos sobre historias longitudinales: **983 instrucciones, 303 respuestas de referencia y 276 historias**. Ayuda a estudiar tareas con contexto EHR. No ofrece una receta ya validada de audio + HCIS → nota ni resuelve nuestro recuperador. Leerlo si profundizamos en contexto longitudinal; no hace falta convertirlo en la referencia principal del bloque.

## Verificación sin una nota de referencia

Podemos preguntar si una afirmación del borrador está **respaldada, contradicha o sin evidencia suficiente** en conversación/contexto. [VeriFact](https://arxiv.org/abs/2501.16672) estudia verificación contra EHR; [Latif et al., 2026](https://proceedings.mlr.press/v333/latif26a.html) contrasta hechos de notas con referencias y conversación.

Ese chequeo se puede ejecutar sin una nota gold para cada caso. **Saber si el chequeo acierta requiere una muestra revisada/anotada.** Además:

- Una nota puede tener todas sus frases respaldadas y omitir un dato importante.
- Una cita puede ser del paciente correcto y estar desactualizada.
- Si ASR pierde «no» y el verificador usa solo ese texto, ambos pueden compartir el error.
- Un juez o una segunda pasada del LLM producen una evaluación automática que también necesita validación.

Conservar transcripción y vínculo temporal con audio facilita auditar esos errores. Un modelo audio→nota puede evaluarse con referencias externas y revisión clínica, pero hay que diseñar cómo localizar la evidencia y el origen del fallo.

## Qué podemos proponer sin vender una solución cerrada

Comparar dos baselines: **generación directa** y **hechos con fuente + transcripción → nota**, con los mismos casos, contexto, plantilla y generador. Evaluar selección de hechos, contenido final, discrepancias, esfuerzo de edición y coste/latencia. Introducir recuperación automática de historia como otro experimento, cuando tengamos entradas y referencias que permitan medirla.

Antes de presentar una arquitectura, poder responder: **qué información recibe, qué transforma, qué evidencia devuelve, qué pierde y cómo lo sabremos**. Practicarlo con las [preguntas y el mini examen](preguntas-defensa.md).

Para el experimento de perturbaciones y la lectura de sus tablas: [Robust SOAP](robust-soap.md).
