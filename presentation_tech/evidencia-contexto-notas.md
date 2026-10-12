# ¿Añadir historia clínica mejora la nota?

Revisión dirigida de fuentes primarias · 12/10/2026. **La hipótesis es razonable, pero no tenemos aquí una demostración limpia de su efecto en nuestro escriba.** Hay que separar historia longitudinal, hechos extraídos del propio encuentro y ejemplos de cómo escribir. Los tres pueden acabar en el prompt; aportan información diferente.

## Tres significados de «contexto»

| Entrada añadida | De dónde viene | Ejemplo propio | Qué habría que medir |
|---|---|---|---|
| **Historia longitudinal del paciente** | HCIS/EHR anterior al encuentro | Tratamiento activo y resultado previo, con fecha y fuente. | Si incorpora información pertinente y vigente sin arrastrar errores históricos. |
| **Hechos del encuentro** | Extracción de la misma conversación | Sujeto + síntoma + negación + momento + turno de evidencia. | Si reorganizar la entrada conserva mejor lo que ya estaba en ella. |
| **Ejemplos o instrucciones** | Otras consultas, plantillas, criterios clínicos | Cómo escribir una sección de valoración. | Formato y selección de contenido, sin trasladar hechos de otros pacientes. |

**Mejorar con hechos del diálogo o con ejemplos recuperados no demuestra que añadir historia del paciente mejore la nota.** Recuperar términos de UMLS tampoco equivale a recuperar su historia.

## Qué permite afirmar la evidencia revisada

| Fuente | Qué compara realmente | Contexto longitudinal independiente | Qué conclusión admite |
|---|---|---|---|
| [Zuckerman/Navina, 2025](https://doi.org/10.1101/2025.11.07.25339620) | Nota ambient del producto frente a consolidación posterior con EHR, selección clínica y Claude Sonnet 4. | **Sí.** | La pipeline enriquecida obtuvo mejores puntuaciones; el diseño publicado no aísla el efecto del historial. |
| [Nuance, Singh et al., 2023](https://aclanthology.org/2023.clinicalnlp-1.18/) | Entrenamiento incremental con prefijo Chain-of-Clinical-Facts generado antes de la nota. | **No.** | Señal a favor de planificación mediante hechos, en su corpus privado y sus métricas. |
| [ASCRIBE, 2026](https://arxiv.org/abs/2610.01234) | Mismo LLM con prompt directo, CoT o hechos/evidencia/relevancia; además, modelos adaptados con distintos rewards. | **No.** | Señal a favor de organizar hechos del diálogo en tailandés; no prueba beneficio de HCIS. |
| [KOSMOS, 2026](https://doi.org/10.3390/info17040355) | Transcripción sola frente a nodos/grafo extraídos del encuentro. | **No.** | Estructura intermedia puede ayudar; mejoras por hechos modestas y no significativas. |
| [Adaptive RAG, Shoumi et al., 2026](https://doi.org/10.3390/biomedinformatics6040047) | Seis condiciones de prompting/retrieval de ejemplos, con Qwen2.5-14B local. | **No.** | Evidencia controlada sobre ejemplos y adaptación de formato, no historia del paciente. |
| [Suki, Palm et al., 2025](https://doi.org/10.3389/frai.2025.1691499) | Notas LLM frente a notas redactadas por especialistas con entradas equivalentes. | No se aísla. | Valida calidad de un producto; declara que no hace ablaciones de componentes. |

### Zuckerman: el resultado corresponde a una pipeline completa

Estudio retrospectivo de **354 encuentros**, centrado en diabetes e hipertensión y su valoración/plan. La puntuación compuesta fue **94,8 frente a 80,1**. El brazo ambient procede del producto Navina; el consolidado combina esa documentación con EHR mediante RAG, un grafo de selección curado por médicos y Claude Sonnet 4. No identifican el modelo del brazo ambient ni muestran que prompt y número de pasadas sean constantes. **Por tanto, inferimos que el efecto de la historia no queda aislado de la selección, reescritura y generación.**

Evalúa principalmente GPT-5, con auditoría clínica limitada: métodos dicen **20 notas**; el abstract habla de **20 %**. Es un preprint con autores ligados al proveedor. Ni demuestra generalización al español ni equivale a mejora de toda la nota o del uso clínico. [Métodos completos](https://www.medrxiv.org/content/10.1101/2025.11.07.25339620v1.full).

No afirmaría que sabemos que cambiaron de modelo: **no documentan suficientemente que se mantuviera el mismo**. Sí documentan una consolidación adicional con un mecanismo de selección distinto.

### Nuance y ASCRIBE: aquí sí hay comparaciones útiles, pero sobre otra intervención

Nuance introduce Chain-of-Clinical-Facts sobre el modelo con tokenización mejorada. En AP de atención primaria, la tabla 2 pasa de **64,9 a 65,3 en ROUGE-L**, de **64,1 a 65,2 en Fact-C** y de **52,0 a 53,3 en Fact-F**. No son comparaciones contra el baseline inicial sin todas las mejoras. Cambia el entrenamiento; no son pesos fijos recibiendo historia adicional. Los hechos objetivo vienen del gold durante entrenamiento y se predicen desde el diálogo en inferencia. [§3.1.2 y tabla 2](https://aclanthology.org/2023.clinicalnlp-1.18/).

ASCRIBE sí mantiene GPT-5.4 al comparar sus prompts. En ThaiClinicBench, **CE 55,7→62,6** y **CE-Impact 64,3→74,6**: completitud estimada por juez LLM, no mejora clínica porcentual. La intervención combina hechos, evidencia, relevancia e instrucciones; no separa perfectamente cuánto aporta cada elemento. El trabajo es tailandés, con evaluación clínica limitada. [§3.1 y tabla 2](https://arxiv.org/abs/2610.01234).

Estas comparaciones justifican probar **generación directa frente a hechos intermedios**. No contestan la pregunta **con/sin historia longitudinal**. Para entender los mecanismos: [guía de papers](intuicion-papers.md).

### Una referencia adicional para evitar confundir RAG con historia

[Shoumi et al.](https://doi.org/10.3390/biomedinformatics6040047) mantienen un modelo local y comparan ejemplos fijos, aleatorios, semánticos, BM25 e híbridos. La recuperación busca **pares diálogo–nota de otros casos para enseñar formato**, no datos previos del paciente. Es útil para pensar controles: si añadir ejemplos o cambiar instrucciones mejora la nota, esa mejora puede explicar parte de una comparación entre pipelines aunque no se añada historia.

Sus baselines estáticos tampoco representan todas las plantillas optimizadas posibles; por ejemplo, el few-shot fijo usa ejemplos ingleses en el entorno japonés. No usaría sus grandes diferencias de cumplimiento estructural para vender cualquier RAG.

## Qué podemos evaluar con ACI-Bench, PriMock y MIMIC

| Recurso | Qué ofrece | Qué falta para contestar con/sin historia |
|---|---|---|
| [ACI-Bench](https://www.nature.com/articles/s41597-023-02487-3) | Pares diálogo–nota para el encuentro. | El artículo declara que no modela entradas EHR independientes ni enlaces a datos estructurados. Propone esas ablaciones como trabajo futuro. |
| [PriMock57](https://github.com/babylonhealth/primock57) | Audio, transcripción manual y nota de **57 consultas simuladas**; los actores usan fichas de caso. | Una ficha de personaje no equivale a una historia longitudinal fechada. El repositorio no presenta un benchmark de nota con/sin HCIS. |
| [MIMIC-IV-Note](https://physionet.org/content/mimic-iv-note/2.2/) + MIMIC-IV | Notas y datos clínicos vinculables por paciente/episodio. | No ofrece las conversaciones de consulta emparejadas para esta prueba ambient. Sintetizarlas cambia el tipo de evidencia. |

MIMIC puede servir para experimentar con recuperación y síntesis de historias, respetando el corte temporal. ACI-Bench/PriMock sirven para comparar generación desde diálogo. **No basta con juntar sus nombres para disponer de un dataset audio + historia + nota del mismo paciente.**

Sí hay un estudio español/catalán de atención primaria con Whisper y Claude: [Fuster-Casanovas et al., 2026](https://doi.org/10.2196/80549). Evalúa el flujo de escriba, satisfacción y revisión; no hace la ablación con/sin historia. No demuestra el efecto que buscamos.

**Resultado de esta búsqueda:** no encontré otra prueba directa y bien controlada del mismo generador con/sin historia longitudinal para notas ambient. Esto describe la búsqueda realizada, no demuestra que no exista ningún estudio.

## El experimento que contestaría nuestra pregunta

Propuesta, todavía sin resultados:

1. **Mismos encuentros y mismo generador:** versión, prompt, plantilla, ASR, parámetros y presupuesto de salida constantes.
2. **A:** transcripción sin historia. **B:** transcripción con historia pertinente seleccionada manualmente. **C:** la misma tarea con historia seleccionada por nuestro recuperador. B prueba el valor potencial de la información; C añade el efecto de recuperarla.
3. Si usamos consolidación en varias pasadas, incorporar **una segunda pasada sin historia** como control; así no atribuimos a HCIS el beneficio de reescribir.
4. Clínicos anotan qué hechos deberían documentarse y de qué fuente/fecha proceden. Separar hechos presentes en el diálogo de los disponibles solo en historia: una omisión por falta de entrada es distinta de perder información disponible. Revisión ciega de cobertura, omisiones, contradicciones, vigencia y contenido sin respaldo. Medir esfuerzo de edición y tiempo/memoria.
5. Separar encuentros donde la historia aporta algo de aquellos donde no hace falta. Incluir casos con cambios de tratamiento o datos antiguos para medir si el sistema confunde pasado y presente.

La frase defendible para la presentación es: **«La historia puede aportar información que no se verbaliza. Vamos a medir si añadir contexto pertinente mejora la nota, manteniendo el modelo y el resto del proceso constantes».**

No necesitamos afirmar que el contexto garantiza mejores notas ni que los productos actuales son incapaces de usarlo. Necesitamos entradas, referencias y controles que permitan responderlo en nuestro entorno.
