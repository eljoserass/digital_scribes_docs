# De conversación a nota: generación, jueces y verificación

Guía para entender las diapositivas, 12/10/2026. Los ejemplos son inventados para explicar el mecanismo; no son recomendaciones clínicas. Para ASR y métricas de hablantes, seguir el índice de la [guía de intuición](guia-intuicion.md). Para Robust SOAP, KOSMOS y el estudio tailandés, ver [los papers explicados](intuicion-papers.md).

## 1. Qué hace cada pieza

| Pieza | Pregunta que resuelve | Qué devuelve |
|---|---|---|
| **Generador** | ¿Cómo documento este encuentro? | Un borrador de nota. |
| **Retriever / recuperador** | ¿Qué fragmentos de la historia hacen falta aquí? | Registros seleccionados con paciente, fecha y procedencia. |
| **Extractor de hechos** | ¿Qué afirmaciones aparecen en estas entradas? | Hechos con sujeto, negación, momento y fuente. |
| **Verificador** | ¿Esta afirmación del borrador tiene respaldo en las fuentes disponibles? | Un veredicto y su evidencia. |
| **LLM juez** | ¿Qué calidad tiene este resultado según estos criterios? | Puntuaciones, decisiones o comentarios. |
| **Rúbrica** | ¿Qué significa hacerlo bien o mal? | Criterios y ejemplos de puntuación. Es una instrucción, no un modelo. |
| **Nota gold** | ¿Qué documento usamos como referencia en este caso? | Una nota revisada por clínicos; no la única redacción válida. |

Un verificador puede implementarse con un LLM juez. Y generador y juez pueden usar el mismo modelo con instrucciones diferentes. Lo que distingue sus funciones es **qué información reciben y qué decisión toman**, no el nombre del modelo.

## 2. Generar directamente o escribir primero los hechos

![Generación directa y generación con hechos intermedios](figures/intuicion-generacion/generacion.png)

La ruta directa manda al modelo el diálogo, el contexto disponible y una plantilla. El modelo selecciona y escribe en la misma generación. Es un buen baseline: pocas piezas y pocos puntos donde perder información.

La segunda ruta hace explícito un paso intermedio. Primero obtiene algo como `paciente · niega fiebre · hoy · turno 4`; después convierte los hechos seleccionados en la nota. Podemos hacerlo en dos llamadas o pedir hechos y nota dentro de una misma secuencia. Conservar el diálogo original permite que la segunda fase vuelva a consultar información que el extractor se haya saltado.

El posible beneficio es poder inspeccionar **qué se seleccionó y de dónde salió**. El coste es otro paso que puede omitir, atribuir mal o deformar un hecho. Una lista de hechos puede parecer ordenada y estar equivocada. La mejora respecto a generación directa hay que medirla.

El antecedente de **Nuance/Singh** genera un prefijo *Chain-of-Clinical-Facts* antes de la nota. Durante entrenamiento, los hechos se extraen de las notas de referencia; durante inferencia, se predicen desde la conversación. Esto es planificación de la generación, no recuperar la historia del paciente. [Singh et al., §3.1.2](https://aclanthology.org/2023.clinicalnlp-1.18/).

### Historia recuperada y hechos del encuentro son entradas distintas

Si el médico dice «mantenemos el tratamiento habitual», el diálogo puede no contener el nombre del medicamento. La historia podría aportarlo. Recuperar esa historia significa seleccionar un registro externo; extraer hechos del diálogo significa representar lo que se acaba de decir.

Para una historia pequeña puede bastar una consulta estructurada o una selección fija. Para una historia extensa podemos buscar fragmentos y pasarlos al generador: esa es la idea de RAG. Antes de buscar por similitud, hay que limitar **paciente, episodio y fecha**. Una mención muy parecida del paciente incorrecto no sirve.

La historia tampoco debe borrar una actualización del encuentro: «tratamiento activo» hace un mes y «lo dejé hace dos semanas» hoy constituyen un cambio documentado o una discrepancia que conservar.

## 3. Un ejemplo de principio a fin

**Entradas disponibles:**

```text
HCIS, hace un mes: enalapril registrado como tratamiento activo.
Paciente, turno 1: «Tengo tos desde hace tres días, pero fiebre no».
Paciente, turno 2: «Dejé el enalapril hace dos semanas».
Paciente, turno 3: «Con amoxicilina me salió una erupción».
Médico, turno 4: «Revisaremos el tratamiento. Vuelve en 48 horas».
Observación manual de hoy: temperatura 36,8 °C.
No se aporta una descripción de auscultación ni una valoración diagnóstica.
```

**Hechos que querríamos conservar:**

| Hecho | Atributo que cambia su significado | Fuente |
|---|---|---|
| Tos de tres días | Síntoma referido por el paciente | Turno 1 |
| Niega fiebre | Negación; no equivale a una medición | Turno 1 |
| Suspendió enalapril hace dos semanas | Estado actual referido, distinto del registro anterior | Turno 2 + HCIS |
| Refiere erupción con amoxicilina | Antecedente referido; no inventar mecanismo ni gravedad | Turno 3 |
| Temperatura 36,8 °C | Dato observado hoy | Entrada manual |
| Revisar tratamiento y volver en 48 h | Plan expresado por el médico | Turno 4 |

Una nota posible —en un producto real, adaptaríamos la plantilla con médicos— sería:

```text
S: Tos de tres días. Niega fiebre. Refiere suspensión de enalapril hace
dos semanas y antecedente de erupción con amoxicilina.
O: Temperatura 36,8 °C, según registro de hoy.
A: No se aporta valoración diagnóstica en las entradas disponibles.
P: Revisar tratamiento y realizar nueva valoración en 48 horas.
```

Ahora imaginemos un borrador erróneo:

```text
Tos de tres días con fiebre. Auscultación normal. Continúa enalapril.
Nueva valoración en 48 horas.
```

Un verificador por afirmaciones podría devolver:

| Afirmación escrita | Comprobación | Resultado |
|---|---|---|
| Tos de tres días | Coincide con turno 1 | Respaldada |
| Tiene fiebre | Turno 1 la niega | Contradicción |
| Auscultación normal | No aparece en ninguna entrada | Evidencia insuficiente |
| Continúa enalapril | El registro previo no incorpora la suspensión comunicada hoy | Conflicto de estado/fecha; revisar |
| Nueva valoración en 48 h | Coincide con turno 4 | Respaldada |

**La erupción con amoxicilina no aparece en el borrador.** Un verificador que recorre solo lo escrito nunca encontrará esa omisión. Hace falta otra dirección de comprobación: desde los hechos que deberían documentarse hacia la nota.

![Dos comprobaciones: respaldo de lo escrito y cobertura de lo importante](figures/intuicion-generacion/verificacion.png)

Podemos medir por separado `afirmaciones respaldadas / afirmaciones escritas` y `hechos relevantes conservados / hechos relevantes esperados`. Son ejemplos de métricas para nuestro protocolo: hace falta acordar qué es un hecho, cómo se empareja y qué relevancia le asignan los clínicos. No equivalen automáticamente a LINK/CORRECT de otro paper.

## 4. Verificar en uso y evaluar al verificador

En uso no tenemos una nota perfecta para cada paciente. Podemos comparar el borrador con conversación y contexto, recuperar evidencia y pedir un veredicto. **Tener fuentes permite ejecutar el chequeo; no demuestra que el chequeo acierte.**

Para evaluar al verificador, clínicos anotan una muestra con las mismas fuentes. Comparamos sus etiquetas con las del sistema: ¿qué errores detectó?, ¿cuáles dejó pasar?, ¿cuántas alertas eran falsas? Hay que mirar cada categoría, además de accuracy: un sistema que aprueba casi todo puede acertar mucho si la muestra contiene pocas notas incorrectas y fallar en los errores que importan.

**VeriFact** aplica recuperación de evidencia del EHR y un juez LLM a afirmaciones descompuestas del texto. Usa las etiquetas *Supported*, *Not Supported* y *Not Addressed*: la segunda incluye respaldo parcial y contradicción, y la tercera indica que la historia no trata ese dato. Su dataset contiene **100 pacientes y 13.290 proposiciones**, anotadas por tres clínicos por proposición. Estudia resúmenes hospitalarios, no nuestro escriba de consulta. [VeriFact](https://arxiv.org/abs/2501.16672), [método y etiquetas](https://arxiv.org/html/2501.16672v1#S2).

Nuestro dibujo de «respaldada / contradicción / evidencia insuficiente» es una simplificación pedagógica. Un registro ausente puede ser una alucinación o información nueva que el médico conoce: no significa automáticamente falsedad.

**Respaldo es distinto de verdad sobre el paciente.** Si ASR transcribe «tengo fiebre» cuando se dijo «no tengo fiebre», el generador y el verificador pueden coincidir perfectamente sobre la transcripción equivocada. Auditar el audio y conservar enlaces temporales ayuda a localizar ese fallo.

## 5. SCRIBE: cómo combinan métricas, médicos y jueces

**SCRIBE es un marco de evaluación**, demostrado sobre un escriba propio. Wang et al. estudian **40 grabaciones de consultas prenatales**, de 6–35 minutos, con media de 16,7 minutos. Transcriben con Whisper; atribuyen hablantes sobre texto con GPT-4o; generan SOAP con GPT-4o y comparan con LLaMA 3.1 8B. Eso explica por qué su «diarización» no es idéntica a un diarizador acústico de voces. [Artículo](https://doi.org/10.1038/s41746-025-01622-1), Methods; revisado también en la copia de Zotero del proyecto.

![Cuatro vías de evaluación en SCRIBE y qué aprende la calibración](figures/intuicion-generacion/evaluacion-scribe.png)

### A. Revisión clínica: el criterio que queremos aproximar

Dos médicos puntúan independientemente las 40 notas con una rúbrica de 1 a 5. Cada uno corrige 20 notas para construir las 40 referencias. Promedian puntuaciones; los desacuerdos se revisan con apoyo de un tercer clínico. El acuerdo entre los dos evaluadores ronda el **53,8 %**, así que la etiqueta humana tampoco es completamente estable.

La rúbrica separa lenguaje —fluidez, coherencia, claridad, brevedad y estructura—, contenido —relevancia, completitud, factualidad y comprensión— y confianza —prudencia y toxicidad—. Una nota puede sonar excelente y conservar mal un tratamiento. Esa es la razón de evaluar dimensiones por separado. [Wang et al., Human assessment](https://doi.org/10.1038/s41746-025-01622-1).

### B. Métricas automáticas: señales reproducibles de partes de la calidad

| Señal usada o propuesta en SCRIBE | Intuición | Límite |
|---|---|---|
| WER | Cuántas palabras cambiaron respecto a una transcripción corregida | No pondera daño clínico. |
| ROUGE / BLEU / METEOR | Coincidencia de palabras y secuencias con la referencia; METEOR añade emparejamiento más flexible | Una paráfrasis válida puede puntuar peor; una negación cambia poco texto. |
| BERTScore | Coincidencia mediante representaciones contextuales de tokens | Parecido semántico no prueba fidelidad clínica. |
| Perplexity con GPT-2 | Cuán probable parece el texto a ese modelo de lenguaje | Texto falso puede ser muy probable y fluido. No está acotada a 0–1. |
| Lecturabilidad, compresión y estructura | Facilidad de lectura, longitud relativa y organización | Proxies; más corto no equivale a mejor. |
| Toxic-BERT | Señales de lenguaje ofensivo | No es una medida general de seguridad clínica. |

La tabla 2 organiza las señales por criterio; Methods describe las métricas empleadas. Conviene distinguir el repertorio del marco de las métricas cuyos resultados se presentan. Ninguna puntuación aislada resuelve la calidad de la nota. [Wang et al., tabla 2 y Auto evaluation](https://doi.org/10.1038/s41746-025-01622-1).

**LINK/CORRECT añaden un LLM dentro de una métrica por hechos.** Extraen información de referencias, transcripciones y notas generadas; LINK comprueba qué hechos aparecen en la referencia y en la nota, y CORRECT si conservan significado y contexto. Lo implementan con GPT-4o, adaptando el procedimiento de Sezgin. Para intuirlo: «¿está el dato?» y «¿está bien expresado?». Eso ya puede fallar en la extracción o en el emparejamiento, aunque el resultado final sea un porcentaje. [Wang et al., Auto evaluation](https://doi.org/10.1038/s41746-025-01622-1).

### C. Trained auto evaluation: aprender cómo combinar métricas

Aquí **entrenan una combinación de métricas**, no el generador ni el juez GPT. La tabla 2 especifica regresión supervisada: las entradas son puntuaciones automáticas y la salida que se intenta aproximar es la puntuación humana.

```text
Nota → [ROUGE, BERTScore, perplexity, ...] → combinación aprendida
                                                    ↓
                                          puntuación humana estimada

Para aprender esa combinación necesitas notas puntuadas por médicos.
```

La regresión ajusta pesos para reducir la diferencia entre lo que predice la combinación y las puntuaciones clínicas de los ejemplos de ajuste. Dos notas con ROUGE parecido pueden recibir notas clínicas distintas; combinar señales puede acercarse más al criterio de los médicos. El artículo informa mayor correlación tras calibrar —por ejemplo, **claridad 0,69**—, frente a correlaciones de métricas crudas entre −0,16 y 0,28. **No encuentro descrito un test independiente de la calibración que permita leer esos números como generalización a casos nuevos.** No debemos inventar split, loss o arquitectura más concretos que lo publicado. [Wang et al., tabla 2, Trained auto evaluation y Discussion](https://doi.org/10.1038/s41746-025-01622-1).

Para nuestro proyecto: acordar rúbrica, recoger puntuaciones, ajustar en un subconjunto y comprobar en encuentros/pacientes separados. Esto último es el diseño que proponemos, no un resultado nuestro.

### D. LLM juez: pasar la rúbrica al modelo

Le dan a GPT-4o la nota que se evalúa, criterios y texto de referencia. El modelo asigna puntuaciones y explica sus deducciones. El suplemento compara dos referencias: **transcripción completa** frente a **nota gold**. No describe fine-tuning del juez; es evaluación mediante prompting, con temperatura 0,7. [Suplemento, Additional Information on Methods, pp. 25–26](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41746-025-01622-1/MediaObjects/41746_2025_1622_MOESM1_ESM.pdf).

La primera referencia pregunta fidelidad al encuentro; la segunda aproxima la nota que se esperaba. Si la gold omitió algo importante, la comparación también puede heredarlo. Si la referencia contiene información que nunca se proporcionó al generador, podemos penalizar al generador por un dato que no podía conocer.

El juez global se parece a un médico rellenando una ficha; el verificador por afirmaciones se parece a revisar el respaldo de cada frase. Podemos combinar ambos, pero una valoración global alta no certifica cada afirmación.

### Qué límites hay que recordar

La muestra de SCRIBE es pequeña y de una especialidad; los datos reales no son públicos. El juez usa la misma familia de modelos que uno de los generadores, y algunas gold parten de notas GPT corregidas: los autores reconocen posible sesgo favorable. Regenerar notas cinco veces no elimina ese parentesco entre referencia y generación. [Wang et al., Discussion y Auto evaluation](https://doi.org/10.1038/s41746-025-01622-1).

Un ejemplo útil de cautela: el suplemento muestra que pasar de escala 1–5 a 1–3 aumenta el acuerdo medio juez–humano de **57,3 % a 85,7 %**, pero reduce la correlación media de Spearman de **0,15 a 0,08**. Agrupar puntuaciones hace más fácil coincidir; no necesariamente mejora la discriminación entre notas. [Suplemento, tabla 3](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41746-025-01622-1/MediaObjects/41746_2025_1622_MOESM1_ESM.pdf).

## 6. Aplicarlo a nuestro ejemplo

Podemos diseñar una rúbrica sencilla: **fidelidad** —niega fiebre, suspensión bien representada—; **completitud** —conserva reacción referida y plan—; **procedencia** —distingue medicación previa y actualización—; **uso práctico** —cuánto tarda el médico en corregirlo—.

Una métrica de parecido podría dar un resultado razonable al borrador erróneo porque contiene «tos», «enalapril» y «48 horas». Un juez con la conversación debería deducir puntos y citar por qué. Un verificador debería señalar fiebre, auscultación y tratamiento. La revisión de cobertura debería detectar la erupción omitida. **No son cuatro votos equivalentes: cada método observa una parte del problema.**

Lo defendible hoy es proponer una comparación con mismos casos y rúbrica, revisar errores con médicos y comprobar si el juez reproduce sus decisiones en casos separados. Sigue siendo hipótesis que los hechos intermedios mejoren nuestra nota, que el recuperador elija siempre el contexto correcto o que un juez calibrado en un idioma funcione igual en español.

Para comprobar que lo tienes: si una nota solo dice «tos de tres días», ¿puede tener todas sus frases respaldadas y seguir siendo mala? Sí: en este ejemplo faltan negación de fiebre, actualización de tratamiento, reacción referida, temperatura y plan. **Factualidad y completitud son preguntas distintas.**

Las tres figuras de esta ficha son esquemas originales del proyecto, no figuras de los papers. El detalle de métodos y resultados de Robust SOAP, KOSMOS y ASCRIBE está en [intuicion-papers.md](intuicion-papers.md).
