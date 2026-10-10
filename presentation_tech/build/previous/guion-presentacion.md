# Guion — Construir un escriba digital médico

Borrador del **09/10/2026**. Acompaña a [main.pdf](build/main.pdf): **24 diapositivas principales, unos 30 minutos**, más tres anexos para preguntas. Los tiempos incluyen explicar y señalar las figuras; son una pauta para ensayar, todavía no un tiempo medido. Las preguntas quedan fuera de esos 30 minutos.

Hilo: **consulta y nota → evaluación → audio y hablantes → contexto, generación y verificación → experimento y despliegue → siguientes pasos**. La sección aparece en el pie de cada diapositiva. Los ejemplos clínicos son ficticios; los diagramas de arquitectura y experimentos son propuestas, no resultados del proyecto.

## Ritmo previsto

| Bloque | Diapositivas | Tiempo | Acumulado |
|---|---|---:|---:|
| Consulta y nota | 1–5 | 5:15 | 5:15 |
| Evaluación y datos | 6–7 | 3:00 | 8:15 |
| Audio y hablantes | 8–13 | 8:15 | 16:30 |
| De contexto a nota | 14–18 | 7:00 | 23:30 |
| Experimento y despliegue | 19–22 | 4:45 | 28:15 |
| Siguientes pasos | 23–24 | 1:45 | 30:00 |

## 1. Construir un escriba digital médico

**0:30 · acumulado 0:30**

Quiero recorrer las decisiones técnicas que aparecen al construir un escriba: qué recibe, qué produce y cómo sabemos si lo hace bien. Partimos de una consulta, añadimos el contexto clínico que esté disponible y queremos terminar con un borrador que el profesional pueda revisar. El recorrido nos llevará desde la señal del micrófono hasta una evaluación reproducible y una propuesta de despliegue local.

**Figura:** señalar audio y contexto entrando en la nota; terminar en la revisión clínica.

## 2. El objetivo: cerrar una nota útil con menos esfuerzo

**0:45 · acumulado 1:15**

El resultado que nos interesa es una nota cerrada y útil. Por eso hay que contar también la revisión y la edición: un borrador que exige corregir muchos detalles puede trasladar trabajo al final del proceso.

Vamos a seguir seis bloques. Primero definimos consulta y nota. Después establecemos la evaluación. Entramos en audio y hablantes, continuamos con contexto y generación, y terminamos con el experimento y el despliegue. La pregunta que organiza todo es qué necesita el sistema para producir una nota correcta y fácil de revisar.

**Figura:** recorrer el flujo completo; señalar revisión antes de enseñar los seis bloques.

## 3. La consulta produce tres fuentes de información

**1:15 · acumulado 2:30**

Usaremos un ejemplo sencillo. El paciente dice que tiene tos desde hace tres días y que no ha tenido fiebre. El clínico expresa que está en mejoría e indica una revisión en siete días. Esa información está en la conversación, con un hablante y un momento determinados.

Además, la historia recoge una alergia a penicilina registrada en 2019. Debemos conservar de dónde viene y cuándo se registró; quizá haya que confirmarla. Y hoy se mide una temperatura de 36,7 grados, que podría llegar por una observación o una entrada manual.

Las tres entradas aportan cosas diferentes. El acceso al contexto depende del conector y del flujo de trabajo. Su flecha es discontinua porque no podemos dar por hecho que todas las aplicaciones lean la historia completa.

**Figura:** señalar un hecho por columna y después el nodo de procedencia. Pausar para distinguir «niega fiebre» de la medición objetiva.

## 4. SOAP organiza hechos, valoración y decisiones

**1:30 · acumulado 4:00**

Ahora distribuimos la información en una nota SOAP. En subjetivo queda lo que refiere el paciente: tos de tres días y ausencia de fiebre según su relato. En objetivo aparece la temperatura medida hoy. Son dos afirmaciones relacionadas, pero con una procedencia distinta.

En valoración documentamos el juicio que expresó el clínico: está en mejoría. En el plan recogemos la revisión que indicó. El generador tiene que preservar esas decisiones, quién las tomó y cómo se expresaron.

La alergia previa puede ir en una sección específica y seguir marcada como pendiente de confirmar. SOAP es una estructura habitual, pero una especialidad puede necesitar otra plantilla, listas o campos adicionales. Antes de entrenar o evaluar hay que fijar qué contenido esperamos y cómo distinguiremos una omisión de algo que simplemente no corresponde a esa nota.

**Figura:** recorrer S→O→A→P. Dejar unos segundos para leer la columna de procedencia. La finalidad es documentar el ejemplo, no explicar un tratamiento.

## 5. Una pipeline con entradas y salidas explícitas

**1:15 · acumulado 5:15**

El audio se convierte en texto y atribución de hablantes. Después interpretamos la información clínica: entidades, negación, temporalidad y quién experimenta cada síntoma. Esa información, junto con contexto y observaciones, permite generar el borrador.

Luego comprobamos soporte y posibles errores, lo revisa el profesional y se incorpora al HCIS. El contexto puede intervenir al seleccionar hechos y al escribir la nota; por eso aparece conectado con ambas funciones.

Estas cajas describen funciones. Podemos tener modelos separados o un modelo que resuelva varias tareas. Mantener explícitas las entradas y salidas permite saber qué estamos evaluando y qué tendríamos que sustituir si un componente falla.

**Figura:** seguir el recorrido horizontal; después las entradas superior e inferior y el cierre clínico→HCIS.

## 6. Cada nivel responde a una pregunta distinta

**1:30 · acumulado 6:45**

Hay tres niveles de evaluación. En el componente preguntamos si se reconocieron las palabras o se asignó bien el hablante. WER mide errores por palabras; DER mide errores de actividad y atribución de hablantes. cpWER y tcpWER permiten evaluar texto con hablantes, añadiendo en el segundo caso restricciones temporales.

En la nota miramos qué hechos se conservaron, qué falta y qué se añadió sin soporte. También importan negación, atribución y fecha. Las métricas de similitud textual pueden ayudar a comparar sistemas, pero necesitamos saber qué significa clínicamente la diferencia.

En el uso real medimos revisión, edición, tiempo total e incidencias del flujo. Una mejora de ASR no demuestra por sí sola una reducción de trabajo. Y separaremos métricas de loss: la loss es la función que optimizamos al entrenar; la evaluación comprueba qué comportamiento produjo ese entrenamiento.

**Figura:** bajar por los tres niveles. No desarrollar todas las siglas; reservar DER y cpWER para sus ejemplos posteriores.

## 7. Del benchmark general al caso clínico español

**1:30 · acumulado 8:15**

Empezaría con referencias conocidas. LibriSpeech tiene 960 horas de entrenamiento de habla leída en inglés. AMI aporta unas cien horas de reuniones multihablante. FLEURS permite un control multilingüe que incluye español. Sirven para comprobar componentes y entender sus límites.

Para consultas, PriMock57 reúne 57 encuentros simulados en inglés, unas ocho horas y media de audio, con turnos y notas. ACI-Bench aporta 207 encuentros textuales; su publicación no ofrece audio para toda la pipeline. MTS-Dialog tiene 1.701 pares breves de diálogo y sección, que tampoco equivalen a consultas completas.

En español, TEME reúne 90 diálogos y unas cuatro horas de voz sintética. Aunque tiene dos voces y etiquetas de hablante, no dispone de tiempos de referencia suficientes para calcular DER directamente. Es un primer recurso del dominio; la consulta real del centro necesita otra referencia. Las horas y los pares describen modalidades distintas, no una clasificación de calidad.

**Figura:** recorrer las columnas de izquierda a derecha; detenerse en las modalidades y en el límite de TEME.

## 8. Del micrófono a una representación acústica

**1:00 · acumulado 9:15**

La primera figura muestra amplitud a lo largo del tiempo. Al mirar ventanas cortas obtenemos un espectrograma: energía en distintas frecuencias y momentos. Después podemos transformar esa energía a bandas Mel y usar su logaritmo, como hacen muchas arquitecturas.

Aquí la ventana dura 25 milisegundos y avanza cada diez; es una ilustración sintética. Otros modelos aprenden representaciones desde la onda. En cualquier caso hay que respetar el muestreo, los canales y la preparación que espera el modelo. La captura añade ruido, saturación y cortes que no se resuelven cambiando únicamente el decoder.

**Figura:** señalar ventana en la onda, estructura temporal del espectrograma y bandas en log-Mel. No explicar la transformada completa.

## 9. ASR: tres formas de aprender audio→texto

**1:45 · acumulado 11:00**

CTC produce distribuciones de tokens por frame, incluyendo un símbolo vacío. Para obtener una secuencia de palabras colapsamos repeticiones y vacíos. Su loss suma la probabilidad de todos los alineamientos que generan la referencia; así podemos entrenar sin etiquetar exactamente dónde empieza cada letra o subpalabra.

En un encoder–decoder, como Whisper, el encoder representa el audio y el decoder predice el siguiente token atendiendo a esa representación y a los tokens anteriores. El objetivo habitual es entropía cruzada, o log-verosimilitud negativa, sobre la transcripción de referencia.

Un transducer combina representación acústica y un predictor condicionado al texto previo. Su objetivo también marginaliza alineamientos, con una organización diferente que se usa mucho en reconocimiento en streaming.

HuBERT corresponde a otra decisión: aprender representaciones mediante predicción enmascarada antes de adaptarlas a una tarea supervisada. Y Conformer describe una familia de encoders. Conviene separar preentrenamiento, arquitectura y loss para comparar alternativas sin mezclar categorías.

**Figura:** dedicar unos veinte segundos por columna y el resto a las distinciones del pie. Las fórmulas ilustran la diferencia; no derivarlas.

## 10. El mismo WER puede ocultar errores muy distintos

**1:30 · acumulado 12:30**

La referencia tiene siete palabras. En la primera hipótesis cambiamos «el» por «este»: una sustitución. En la segunda perdemos «no»: una eliminación. Ambas dan un WER del 14,3 por ciento.

Sin embargo, la segunda cambia el significado clínico. Si esa transcripción alimenta al generador, puede acabar afirmando que el paciente refiere fiebre. Por eso conservaría WER para comparar ASR y añadiría un análisis específico de negaciones, medicación, dosis, fechas y otras entidades importantes para el caso de uso.

También hay que fijar cómo normalizamos números, abreviaturas, puntuación y variantes de escritura. Parte de la diferencia puede ser de transcripción y parte de significado. Los recursos médicos proponen formas de revisar errores con impacto, pero tenemos que comprobar que ese criterio sea adecuado para nuestro idioma y especialidad.

**Figura:** leer primero las dos hipótesis; mostrar después que el contador de errores coincide. Dejar una pausa para la pérdida de «no».

## 11. Voz, palabras y rol son etiquetas diferentes

**1:15 · acumulado 13:45**

La línea temporal tiene dos voces y algunos intervalos en los que hablan a la vez. Diarización responde quién habla y cuándo, usando identificadores como S1 y S2. Esos identificadores son arbitrarios: pueden permutarse entre una referencia y una predicción.

La transcripción aporta qué dijo cada voz. La asignación de rol añade que S1 es el clínico y S2 el paciente, si lo hemos validado. Un acompañante introduce otro rol, aunque su voz se separe correctamente.

La nota depende de esa distinción. «Mi madre toma este medicamento» y «tomo este medicamento» no describen lo mismo. Un sistema puede reconocer todas las palabras y aun así atribuir un antecedente a la persona equivocada. La evaluación de DER no cubre por sí sola esa interpretación clínica.

**Figura:** señalar solapamiento, después texto y por último rol. Evitar presentar S1 como identidad biométrica.

## 12. Diarización: agrupar voces o predecir actividad

**1:30 · acumulado 15:15**

La ruta modular detecta voz o segmentos, obtiene embeddings que caracterizan la voz y agrupa segmentos similares. Podemos inspeccionar cada etapa y cambiarla. La segmentación y los embeddings tienen sus propios entrenamientos; el clustering no necesariamente usa una loss aprendida.

EEND plantea una predicción directa de actividad por frame y hablante. Como no existe un orden natural de los hablantes, usa un entrenamiento invariante a permutación. En su formulación habitual combina esa asignación con entropía cruzada binaria, permitiendo que varios hablantes estén activos a la vez.

La formulación powerset representa combinaciones de hablantes activos como clases y utiliza entropía cruzada multiclase. Son alternativas que hay que evaluar con solapamiento y turnos breves. Para comparar DER fijaremos el margen temporal de tolerancia, o collar, y si contamos el solapamiento. Dos cifras con protocolos distintos pueden resultar engañosas.

**Figura:** seguir la ruta modular y luego leer el frame donde S1 y S2 están activos en EEND.

## 13. Reconocer texto y hablantes en una misma salida

**1:15 · acumulado 16:30**

Podemos ejecutar ASR y diarización por separado y alinear sus resultados. También existen modelos conjuntos que producen una transcripción con hablantes y tiempos. MOSS-Transcribe-Diarize es un ejemplo reciente; SOT es otra línea para serializar el reconocimiento multihablante.

La salida nos permite recuperar qué se dijo, quién lo dijo y cuándo. cpWER evalúa palabras con atribución de hablante, permitiendo la permutación de identificadores. tcpWER introduce restricciones temporales para evitar correspondencias que no respeten el tiempo.

Estos modelos son candidatos interesantes para comparar con la pipeline modular. Su resultado en benchmarks generales no acredita calidad clínica en español. Y producir texto diarizado no implica que el mismo modelo genere una nota médica o identifique el rol clínico correctamente.

**Figura:** comparar las dos rutas hacia una salida común. La sintaxis de los tokens es ilustrativa.

## 14. Recuperar contexto exige paciente, fecha y procedencia

**1:30 · acumulado 18:00**

Supongamos que recuperamos un registro que dice que una medicación estaba activa en 2021 y otro que indica su suspensión en 2025. Hay que interpretar esa evolución y comprobar que pertenece al paciente y al encuentro adecuados. Un documento de otro paciente se excluye antes de generar.

La recuperación puede seleccionar documentos o fragmentos mediante búsqueda y reranking. Medimos si encuentra evidencia relevante con Recall@k o nDCG. Después evaluamos cómo usa esa evidencia: si conserva la fecha, interpreta el estado y evita presentar un antecedente antiguo como actual.

La fecha más reciente ayuda, pero no resuelve automáticamente toda discrepancia. Si el diálogo y la historia se contradicen, necesitamos una forma de señalarlo y revisarlo. El objeto útil para la generación es un hecho con fuente, fecha y estado, no una concatenación de texto sin esa información.

**Figura:** recorrer identidad→recuperación→reconciliación; señalar el documento excluido y el conflicto.

## 15. Generar una nota también exige seleccionar información

**1:15 · acumulado 19:15**

Una estrategia es pasar diálogo, contexto y observaciones a un modelo de generación con instrucciones y una plantilla. Otra selecciona y agrupa hechos antes de generar por sección. T5, BART y los LLM actuales permiten explorar la primera; CLUSTER2SENT ilustra una ruta con organización intermedia.

Seleccionar implica distinguir información relevante de conversación incidental, conservar negación y temporalidad, y saber a quién corresponde cada hecho. Una lista intermedia facilita inspeccionar la selección, aunque también puede omitir matices que el generador ya no podrá recuperar.

Compararía ambas rutas con las mismas entradas y los mismos criterios. Al principio podemos probar un modelo disponible mediante prompting. Entrenarlo o adaptarlo requiere pares de referencia y un problema observado que queramos corregir.

**Figura:** señalar dónde se toma la decisión de selección en cada ruta; terminar en la misma salida SOAP.

## 16. Entrenar generación: del token al resumen candidato

**1:30 · acumulado 20:45**

El trabajo de Singh y colaboradores, de Nuance, ayuda a responder qué losses se han usado para la nota. Entrenan sobre aproximadamente 900.000 encuentros privados en inglés. La entrada del generador es una transcripción diarizada: el entrenamiento descrito aquí va de texto a nota.

La entropía cruzada enseña a predecir los tokens de la referencia. Añaden ranking de resúmenes candidatos siguiendo BRIO, con una ordenación basada en ROUGE-L. El esquema combina aprender la referencia y preferir ciertos candidatos completos.

Otros trabajos ponderan términos médicos o introducen mecanismos para negación y conceptos. Son formas de acercar el objetivo al contenido clínico, pero optimizar similitud o dar más peso a términos no garantiza soporte factual. Para audio→nota tampoco hay una única loss estándar: depende de si entrenamos componentes separados o una arquitectura conjunta, y de qué referencias tenemos.

**Figura:** explicar CE arriba, ranking abajo y la combinación. Los 900.000 encuentros contextualizan el trabajo; no son datos públicos disponibles para nuestro entrenamiento.

## 17. Verificar hechos y buscar omisiones

**1:30 · acumulado 22:15**

Podemos descomponer la nota en afirmaciones y buscar su evidencia. «Niega fiebre» tiene soporte en el relato del paciente. «Toma actualmente X» entra en conflicto con un registro de suspensión. «Auscultación normal» carece de soporte en las entradas de este ejemplo.

Sin soporte no equivale necesariamente a falso: puede haber información que no capturamos. Sí es una razón para que el sistema lo señale y el clínico lo revise. Hay trabajos de verificación sobre EHR y datasets de inferencia clínica que sirven para explorar estos mecanismos, con dominios diferentes de nuestra consulta.

La otra dirección busca omisiones: de los hechos relevantes de la consulta, cuáles no llegaron a la nota. Por ejemplo, si desaparece el seguimiento indicado. El verificador puede equivocarse, así que necesita evaluación propia, especialmente de fallos que deja pasar y de alertas que añaden carga de revisión.

**Figura:** recorrer los tres estados y volver desde la evidencia a la nota para explicar omisiones.

## 18. Un fallo temprano puede cambiar la nota final

**1:15 · acumulado 23:30**

Volvemos a la negación. La ruta superior recibe una transcripción de referencia y puede producir «niega fiebre». En la inferior, ASR pierde «no» y el mismo generador puede producir «refiere fiebre». La redacción final puede ser fluida en ambos casos.

El generador podría corregir algunos errores o amplificar otros; el dibujo ilustra una posibilidad, no una tasa medida. Para saber cuánto aporta la entrada, compararemos la nota generada desde la transcripción revisada con la nota generada desde ASR.

La verificación también depende de sus fuentes. Si comprueba la nota únicamente contra el texto erróneo, puede considerar soportado el fallo. Por eso interesa conservar la trazabilidad hasta el audio y construir una evaluación que localice dónde apareció el error.

**Figura:** mostrar las dos rutas con el mismo generador; señalar que ambas frases finales resultan naturales.

## 19. Un experimento común permite localizar los fallos

**1:30 · acumulado 25:00**

Propongo cuatro condiciones. En A damos texto, hablantes y contexto revisados. En B sustituimos el texto por ASR. En C incorporamos hablantes predichos. En D usamos el contexto recuperado automáticamente. Manteniendo casos y generador, las diferencias ayudan a estudiar cada sustitución.

Necesitamos referencias compatibles con cada condición, por ejemplo hablantes alineados con el texto. Estas comparaciones dependen del resto de la configuración y de sus interacciones; no son porcentajes universales de responsabilidad.

Separaremos entrenamiento, desarrollo y test evitando repetir encuentros o pacientes entre ellos, y controlaremos hablantes cuando corresponda. Usaremos revisión clínica con un criterio común, preferiblemente ciega al sistema: omisiones, contradicciones, atribución, edición y tiempo. Registraremos versiones y parámetros para poder repetir el experimento. Este sería el primer diseño a concretar, antes de una evaluación grande.

**Figura:** bajar A→D; explicar cada cambio en la última columna. No presentar la tabla como resultados.

## 20. Entrenamiento y ejecución tienen restricciones distintas

**1:15 · acumulado 26:15**

Entrenar necesita datos, etiquetas, un objetivo y recursos para optimizar pesos. Ejecutar necesita atender una consulta con una latencia, memoria y concurrencia aceptables. Podemos entrenar en una infraestructura y desplegar en otra.

Entre ambas hay un artefacto versionado: pesos, tokenizer, preparación del audio, prompt, parámetros de decodificación y precisión. Ese conjunto define lo que probamos. La cuantización puede ayudar a servir el modelo con menos recursos, pero hay que medir su efecto.

No empezaría entrenando todo. Primero establecería un baseline con modelos disponibles. Los errores observados nos dirán si necesitamos adaptar vocabulario, hablantes, selección de hechos o estilo de nota. Así el coste de entrenamiento responde a una necesidad concreta.

**Figura:** recorrer entrenamiento→artefacto→ejecución; distinguir memoria de entrenamiento y de inferencia.

## 21. Arquitectura propuesta para un prototipo local

**1:15 · acumulado 27:30**

El cliente web o móvil captura el audio, con paciente y episodio confirmados. Lo transmite a servicios del centro que realizan transcripción y atribución de hablantes, y después generación y verificación. El contexto se lee a través de un conector y se filtra antes de usarlo.

El borrador vuelve al profesional para su revisión. Guardar la nota en HCIS es una integración que hay que concretar con el entorno disponible. Esta figura propone funciones y límites; todavía no representa un conector implementado.

La plataforma también decide cómo gestionamos permisos del micrófono, canales, interrupciones y conectividad. WebRTC o un WebSocket seguro son opciones de transporte según el flujo. Hay que definir qué datos se conservan y registrar versiones, tiempos, recursos y fallos para evaluar la ejecución y detectar incidencias.

**Figura:** señalar el límite del centro, la lectura de contexto y la escritura tras revisión.

## 22. Medir con la configuración que se desplegará

**0:45 · acumulado 28:15**

Pasamos los mismos casos por dos configuraciones. Podrían diferir en motor, dispositivo o precisión, por ejemplo FP16 e INT8 si está soportado. Comparamos calidad junto con latencia, memoria y concurrencia.

Mediría percentiles de latencia y factor de tiempo real, además de los errores clínicos. La versión que funciona en un notebook no demuestra el comportamiento del servicio desplegado. La configuración objetivo debe repetir la evaluación; de momento este dibujo es un protocolo y no contiene resultados de rendimiento.

**Figura:** señalar las dos configuraciones y la comparación común. No detenerse en las herramientas concretas.

## 23. Siguientes pasos: un baseline y evidencia comparable

**1:00 · acumulado 29:15**

Primero concretamos especialidad, idioma, plantilla y referencias. Después montamos una pipeline local sencilla y, si podemos acceder, incorporamos candidatos comerciales a la comparación.

Los proveedores que lleguen a ese punto deben haber pasado la revisión de seguridad, protección de datos, coste e integración HCIS. La calidad se evalúa sobre los mismos casos y con el mismo criterio, para que el trabajo sirva a las dos vías.

La comparación debería producir un mapa de errores y carga de revisión. Con esa evidencia decidimos qué mejorar y qué merece un piloto supervisado. En el piloto añadimos el flujo real, integración y seguimiento; sus resultados pueden cambiar la decisión inicial.

**Figura:** recorrer las cuatro fases; dejar claro que la tercera aporta la evidencia para pasar a la cuarta.

## 24. El primer entregable es una evaluación reproducible

**0:45 · acumulado 30:00**

El primer entregable sería un baseline en español sobre casos revisados, con errores que podamos explicar. Para conseguirlo necesitamos entradas trazables, criterios que localicen errores y una ejecución reproducible.

Eso conecta las tres ideas del recorrido: la nota usa varias fuentes, cada tarea requiere su propia evaluación y el sistema se mide en las condiciones de uso. La siguiente decisión —adaptar un componente, incorporar un proveedor o iniciar un piloto— debe responder a fallos y necesidades observados.

**Figura:** señalar las tres tarjetas y terminar en la frase inferior. Pausa breve de cierre antes de preguntas.

## Anexos, fuera del recorrido de 30 minutos

- **A · Datasets adicionales:** consultar volúmenes y límites de Common Voice, DIHARD, VoxConverse, MedAlign, MedNLI, MIMIC-IV-Note y FactEHR. No leer la tabla completa en la exposición.
- **B · Tarea, métrica y loss:** volver aquí si preguntan por objetivos de entrenamiento o qué cubre cada métrica.
- **C · Lecturas:** punto de entrada a la bibliografía; el [catálogo de fuentes](README.md) conserva descripciones, enlaces, versiones y más detalle.

## Apoyos para preparar la exposición

- [The anatomy of clinical documentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/) — Contenido, organización y relaciones que hay que conservar en una nota.
- [Safe use of the EHR](https://doi.org/10.1093/jamia/ocaa199) — Revisión y flujo con escribas humanos; usar para contexto organizativo.
- [Jurafsky y Martin, cap. 15](https://web.stanford.edu/~jurafsky/slp3/15.pdf) y [cap. 16](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — Señal, representaciones y familias de ASR.
- [Singh et al. (2023)](https://aclanthology.org/2023.clinicalnlp-1.18/) — Caso de generación de notas con CE y ranking de candidatos; datos privados en inglés.
- [Moramarco et al. (2022)](https://aclanthology.org/2022.acl-long.394/) — Relación entre evaluación automática, revisión clínica y edición.
- [Robust SOAP (2026)](https://proceedings.mlr.press/v333/latif26a.html) — Efecto de errores de entrada y fallos de las notas.
- [MedAlign](https://arxiv.org/abs/2308.14089) y [VeriFact](https://arxiv.org/abs/2501.16672) — Recuperación de contexto clínico y comprobación de soporte.

Si el ensayo se alarga, abreviar nombres de modelos en 9 y 13 y las cifras secundarias de 7. Mantener el ejemplo SOAP, el error de negación, el protocolo común y los siguientes pasos.
