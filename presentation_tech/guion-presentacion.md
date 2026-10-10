# Guion — Construir un escriba digital médico

Versión renovada del **10/10/2026**. Acompaña a [main.pdf](build/main.pdf): **26 diapositivas principales, 30 minutos previstos y cinco anexos**. Los tiempos incluyen señalar figuras y pausas; falta ensayarlos. Las preguntas quedan fuera de los 30 minutos.

## El recorrido en un minuto

Queremos transformar información del encuentro en documentación clínica útil. Primero definimos entrada y nota. Fijamos qué significa hacerlo bien y qué datos permiten medirlo. Abrimos el proceso: reconocer audio, atribuir hablantes, seleccionar información, usar historia y generar. Las comprobaciones automáticas tienen límites y requieren evaluación. Después conectamos fallos observados con adaptación y ejecución local. Cerramos con los datos y el baseline que podemos construir.

**Consulta → criterios y datos → audio/hablantes → diálogo/contexto/nota → adaptación/despliegue → primer experimento.**

El ejemplo clínico es ficticio. Los esquemas de pipeline y experimentos son propuestas. Las figuras acústicas proceden de Jurafsky. El código de Scribnic se distingue de las ampliaciones pendientes. Las fuentes están enlazadas en las diapositivas; las fichas de lectura desarrollan métodos y límites.

## Qué debe transmitir cada bloque

| Bloque | Mensaje | Conexión con el siguiente |
|---|---|---|
| Consulta y nota | Definir qué información entra, qué se documenta y quién revisa. | La definición permite elegir criterios de éxito. |
| Evaluación y datos | Medir palabras, contenido y trabajo; reconocer huecos de los datasets. | Con referencias concretas podemos comparar componentes. |
| Audio y hablantes | Entender mecanismos y errores que cambian el diálogo disponible. | Una transcripción correcta aún necesita selección para convertirse en nota. |
| Diálogo, contexto y nota | Separar extracción, retrieval, generación y comprobación; comparar propuestas. | Los errores observados indican qué intervención probar. |
| Adaptación y despliegue | Elegir datos, modelos y ejecución según el fallo y las restricciones. | Hace falta un experimento viable con el código y los recursos disponibles. |
| Plan de trabajo | Crear referencias y un baseline reproducible antes del piloto. | Discutir prioridades con el grupo. |

## Ritmo previsto

| Bloque | Diapositivas | Tiempo | Acumulado |
|---|---|---:|---:|
| Consulta y nota | 1–5 | 4:20 | 4:20 |
| Evaluación y datos | 6–7 | 2:20 | 6:40 |
| Audio y hablantes | 8–13 | 7:00 | 13:40 |
| Diálogo, contexto y nota | 14–19 | 8:10 | 21:50 |
| Adaptación y despliegue | 20–24 | 5:50 | 27:40 |
| Plan de trabajo | 25–26 | 2:20 | 30:00 |

## 1. Construir un escriba digital médico

**0:30 · acumulado 0:30 · 1 · Consulta y nota**

**Mensaje:** Seguir la información del encuentro hasta una nota revisada.

Quiero recorrer qué hay que resolver para construir un escriba digital médico. La entrada incluye una conversación y, cuando estén disponibles, contexto clínico y observaciones. La salida es un borrador que el profesional revisa antes de incorporarlo a la historia.

El recorrido conecta la tarea clínica con modelos, datos, evaluación y ejecución local. Terminaré con un primer experimento y con la base que ya estoy construyendo en Scribnic.

**Figura:** Audio y contexto → borrador → revisión.

**Transición:** Primero fijamos el objetivo y el alcance.

## 2. Objetivo y alcance

**0:45 · acumulado 1:15 · 1 · Consulta y nota**

**Mensaje:** Medir el trabajo completo, incluida la revisión.

Un escriba humano puede documentar bajo supervisión del profesional. El digital automatiza parte de ese trabajo. Algunas aplicaciones añaden informes, codificación o ayuda a decisiones; esas funciones tienen sus propios requisitos. Aquí vamos a centrarnos en documentar el encuentro.

Queremos una nota correcta que reduzca el esfuerzo de cerrarla. Contaremos también revisión y edición: un borrador rápido puede dar mucho trabajo después. El recorrido es consulta y nota, evaluación, audio y hablantes, generación con contexto, adaptación y despliegue, y plan de trabajo.

**Figura:** Recorrer consulta → nota cerrada; señalar la revisión.

**Transición:** Para definir la tarea necesitamos saber qué información tenemos.

## 3. Información del encuentro

**1:00 · acumulado 2:15 · 1 · Consulta y nota**

**Mensaje:** Conversación, historia y observaciones aportan datos distintos.

Seguiremos este ejemplo ficticio. El paciente refiere tos de tres días y niega fiebre. El clínico expresa que está en mejoría e indica una revisión en siete días. La conversación aporta esos hechos, quién los dijo y cuándo.

La historia añade una alergia registrada en 2019. No equivale a una confirmación actual. Y hoy se mide una temperatura de 36,7 grados, que podría entrar por una observación o un campo manual.

El bloque inferior reúne las entradas para generar, todavía no es la nota. La flecha del contexto es discontinua porque su disponibilidad depende del flujo y del conector.

**Figura:** Señalar un dato de cada fuente; distinguir negación referida de medición.

**Transición:** Veamos qué hacemos con estas entradas al escribir una nota.

## 4. La nota SOAP

**1:15 · acumulado 3:30 · 1 · Consulta y nota**

**Mensaje:** La nota selecciona y organiza información con una función clínica.

SOAP separa subjetivo, objetivo, valoración y plan. En subjetivo documentamos el relato del paciente: tos y ausencia de fiebre según refiere. En objetivo aparece la temperatura medida. Son afirmaciones relacionadas, pero proceden de fuentes distintas.

Valoración recoge el juicio expresado por el clínico y plan recoge su decisión de seguimiento. En este alcance, el modelo documenta esas decisiones; no inventa una nueva valoración clínica. La alergia antigua puede ir en una sección de antecedentes, conservando su fecha y necesidad de confirmación.

SOAP es un ejemplo. Cada servicio puede necesitar otros campos y estilos. Definirlos permite distinguir una omisión importante de algo que no corresponde incluir.

**Figura:** Recorrer S, O, A, P y su procedencia.

**Transición:** Ya tenemos entrada y salida; ahora podemos abrir el proceso.

## 5. Pipeline del escriba

**0:50 · acumulado 4:20 · 1 · Consulta y nota**

**Mensaje:** Cada etapa necesita entradas y salidas inspeccionables.

El audio pasa a texto con tiempos y hablantes. Con ese texto, el contexto disponible y las observaciones seleccionamos información y generamos un borrador.

La selección puede ocurrir dentro del LLM o producir hechos intermedios: después compararé ambas rutas. La caja de comprobación busca soporte y conflictos para ayudar a revisar. Su presencia no garantiza calidad; también tendremos que medir sus errores. Finalmente revisa el profesional y se guarda la nota aprobada.

El esquema describe funciones. No implica que todas estén implementadas ni que cada caja necesite un modelo independiente.

**Figura:** Seguir el flujo horizontal y después las dos entradas adicionales.

**Transición:** Antes de elegir modelos, fijemos cómo detectar si el sistema funciona.

## 6. Evaluación

**1:00 · acumulado 5:20 · 2 · Evaluación y datos**

**Mensaje:** Evaluar componentes, contenido y utilidad responde a preguntas diferentes.

En audio y hablantes medimos palabras reconocidas y atribución. Eso ayuda a localizar fallos concretos.

En la nota preguntamos qué hechos faltan, cuáles se añadieron sin soporte y cuáles cambiaron de sentido. Nos interesan negación, sujeto, fecha y decisiones documentadas. Una métrica de similitud textual puede complementar esta evaluación, pero no sustituye una rúbrica de contenido.

En el uso clínico medimos correcciones, esfuerzo de revisión y tiempo total. Una reducción de WER no demuestra por sí sola una mejora de trabajo. Para medir errores necesitamos referencias; para valorar su importancia necesitamos criterio clínico.

**Figura:** Bajar por los tres niveles, sin desarrollar siglas todavía.

**Transición:** La siguiente pregunta es con qué datos podemos medir cada nivel.

## 7. Datos de evaluación

**1:20 · acumulado 6:40 · 2 · Evaluación y datos**

**Mensaje:** No tenemos un único corpus público que cubra todo nuestro caso de uso.

Las referencias generales comprueban componentes: LibriSpeech tiene 960 horas de entrenamiento en inglés leído; AMI unas cien horas de reuniones; FLEURS incluye español entre sus 102 idiomas.

PriMock57 aporta 57 consultas simuladas en inglés, ocho horas y 38 minutos de duración clínica, con audio, turnos y notas. ACI-Bench contiene 207 encuentros textuales y MTS-Dialog 1.701 pares breves; no sirven para evaluar toda la entrada acústica.

TEME aporta 90 diálogos médicos en español y unas cuatro horas de audio TTS. Tiene voces y etiquetas por turno, pero sus estimaciones temporales no son una referencia gold para DER. Será un control exploratorio, no prueba de calidad en consultas espontáneas. Al final concretaré cómo cubrir los huecos.

**Figura:** Comparar columnas: modalidad, idioma y dominio.

**Transición:** Entramos ahora en el audio, empezando por lo que ve el modelo.

## 8. Señal y representación acústica

**1:10 · acumulado 7:50 · 3 · Audio y hablantes**

**Mensaje:** La representación acústica conserva información distinta del texto.

Estas figuras de Jurafsky muestran la misma frase de conversación espontánea en inglés. Arriba en la onda vemos cambios de amplitud y alineamiento con palabras y fonemas. Los límites no son tan limpios como en el texto.

El espectrograma representa energía por frecuencia y tiempo, calculada sobre ventanas. Podemos transformarlo a una escala Mel y usar log-Mel, como Whisper, o aprender representaciones desde la onda en otras arquitecturas.

Antes del modelo ya importan micrófono, canales, muestreo, ruido y compresión. Remuestrear a una frecuencia más alta no recupera información perdida. Hay que usar la preparación que espera el modelo y reproducirla en evaluación y despliegue.

**Figura:** Alinear una palabra entre las dos figuras; señalar ejes de tiempo y frecuencia.

**Transición:** Con esa secuencia acústica, ¿cómo se producen las palabras?

## 9. Modelos de ASR

**1:30 · acumulado 9:20 · 3 · Audio y hablantes**

**Mensaje:** CTC, encoder–decoder y transducer producen texto de formas distintas.

CTC asigna etiquetas a frames acústicos. Repeticiones y blanks permiten que muchos alineamientos representen el mismo texto. En este ejemplo, colapsar la secuencia da «tos». El decoding greedy es sencillo; su factorización no condiciona cada etiqueta en el texto previo. Puede combinarse con decodificación más rica.

En encoder–decoder, el decoder usa texto previo y atención al audio para producir el siguiente token. Whisper atiende al segmento de audio y genera token a token. Eso integra contexto textual, con coste de decodificación autoregresiva.

En RNN-T, una red conjunta combina estado acústico y prefijo textual. Emitir un token avanza el texto; emitir blank avanza el audio. Puede funcionar incrementalmente con un encoder causal, pero la arquitectura concreta y el decoding importan.

Estos mecanismos explican opciones de entrenamiento e inferencia. Elegiremos modelos concretos midiendo calidad clínica en español, velocidad y memoria. Las losses quedan en el anexo.

**Figura:** CTC: leer secuencia y colapsar. AED: seguir bucle de texto. RNN-T: token frente a blank.

**Transición:** Pasamos del mecanismo a cómo medir su salida.

## 10. WER y errores clínicos

**1:10 · acumulado 10:30 · 3 · Audio y hablantes**

**Mensaje:** WER cuenta errores por palabras, no su gravedad clínica.

WER es sustituciones más eliminaciones más inserciones, dividido por el número de palabras de la referencia. Aquí hay siete.

Cambiar «el» por «este» produce un error; eliminar «no» también. Ambos dan 14,3 por ciento, aunque el segundo invierte un dato clínico.

Mantendríamos WER con una normalización documentada y añadiríamos análisis de términos, negación, dosis y fechas. Esas categorías permiten saber qué falla y seleccionar casos para revisión clínica. Para demostrar que una corrección de vocabulario o un fine-tuning ayuda, repetimos esa evaluación en un test separado; no basta con corregir los ejemplos que vimos.

**Figura:** Comparar las dos frases y explicar S, D, I y N.

**Transición:** Reconocer palabras deja otra pregunta: quién las dijo.

## 11. Diarización: tiempo, hablante y rol

**1:00 · acumulado 11:30 · 3 · Audio y hablantes**

**Mensaje:** Hablante anónimo, rol clínico e identidad son etiquetas diferentes.

Diarización responde quién habla y cuándo, usando etiquetas anónimas como S1 y S2. Las barras muestran actividad y los intervalos señalados muestran solapamiento.

Después atribuimos palabras a esos hablantes. Por separado podemos asignar roles como clínico y paciente, usando información del diálogo o del flujo y comprobando que acierta. S1 por sí solo no identifica una persona ni establece un rol.

La diferencia importa para la nota: una pregunta del clínico no equivale a un síntoma afirmado por el paciente. Y «mi madre toma X» necesita además atribución semántica del hecho, aunque sepamos quién pronunció la frase.

**Figura:** Tiempo → palabras → rol, en ese orden.

**Transición:** Veamos dos maneras de estimar la actividad de hablantes.

## 12. Modelos de diarización

**1:20 · acumulado 12:50 · 3 · Audio y hablantes**

**Mensaje:** Las familias de diarización cambian qué se modela y dónde se puede intervenir.

En una ruta modular detectamos o segmentamos voz, obtenemos embeddings y agrupamos intervalos. Podemos sustituir etapas y analizar dónde falla. El agrupamiento necesita suficiente evidencia acústica: turnos muy cortos o ruido pueden dificultar la representación y las asignaciones.

EEND predice actividad por frame y hablante; admite varios hablantes activos simultáneamente. La gestión del número de hablantes y de sesiones largas depende de la variante. No hay una superioridad automática por ser end-to-end.

DER suma voz omitida, falsas alarmas y confusión de hablante respecto al tiempo de habla de referencia. JER compara regiones por hablante. Fijamos tolerancia alrededor de límites, conocida como collar, y tratamiento del solapamiento. También evaluamos atribución de palabras: un error temporal puede afectar mucho o poco al contenido final.

**Figura:** Seguir ambas rutas; señalar la actividad simultánea de EEND.

**Transición:** Podemos obtener texto y hablantes por separado o en una salida conjunta.

## 13. Transcripción con hablantes

**0:50 · acumulado 13:40 · 3 · Audio y hablantes**

**Mensaje:** Comparar las rutas sobre una misma transcripción con hablantes.

La salida que queremos son palabras con tiempos y etiquetas de hablante. Podemos construirla combinando ASR, diarización y alineamiento, o con un modelo conjunto como MOSS.

cpWER concatena el texto por hablante y permite permutar las etiquetas, porque S1 y S2 son nombres arbitrarios. tcpWER incorpora restricciones temporales. Complementan WER y DER calculados por separado.

La comparación relevante será sobre consultas: reconocimiento, atribución, latencia y memoria. Un resultado en otro dominio no establece calidad clínica en español. La salida de la derecha es ilustrativa, no un resultado nuestro.

**Figura:** Dos rutas llegan al mismo contrato de salida.

**Transición:** Tenemos el diálogo documentado. Ahora toca decidir qué llevar a la nota.

## 14. Generación de notas

**1:00 · acumulado 14:40 · 4 · Diálogo, contexto y nota**

**Mensaje:** El baseline generativo necesita un contrato clínico antes que una arquitectura sofisticada.

La primera ruta es un LLM que recibe transcripción con hablantes, contexto disponible, observaciones y una plantilla. Define las secciones y conserva los hechos y decisiones documentadas.

El equipo clínico aporta algo concreto: contenido que debe aparecer, información que sobra, estilo del servicio y ejemplos de errores. Esas decisiones se convierten en instrucciones y en una rúbrica, no solo en un prompt que parece funcionar.

Podemos comparar plantillas y prompts sobre encuentros fijados. Si encontramos errores persistentes, decidiremos si hace falta extracción adicional, mejores entradas o adaptación de pesos. Ahora vamos a abrir la selección de información.

**Figura:** Entradas → generador con criterios → borrador.

**Transición:** ¿Se selecciona lo relevante mientras se redacta o antes?

## 15. Selección de hechos

**1:40 · acumulado 16:20 · 4 · Diálogo, contexto y nota**

**Mensaje:** Los hechos intermedios son una hipótesis que comparar, no una garantía.

La ruta directa decide relevancia al escribir. La alternativa hace explícitos hechos con fuente, sujeto, negación y momento antes de generar. Mantendría también el diálogo original para reducir el riesgo de que una extracción incompleta cierre el acceso a evidencia.

En «mi madre toma X», hay que conservar que la persona es la madre. Una lista que extraiga solo medicamento y verbo ya perdió información.

ASCRIBE genera hechos, fragmentos de soporte y relevancia antes de SOAP; estudia prompting y adaptación en tailandés. Es un preprint reciente con evaluación clínica limitada. KOSMOS construye entidades, atributos y relaciones; las mejoras son modestas y la extracción no se evalúa de forma independiente.

Nuance, en 2023, es un antecedente de planificación con hechos. Ninguno de estos métodos resuelve por sí mismo el acceso al HCIS. Nuestra comparación sería directo frente a hechos con fuente más diálogo, con el resto fijado.

**Figura:** Recorrer las dos rutas y analizar el sujeto del ejemplo.

**Transición:** Extraer del diálogo es distinto de seleccionar información de la historia.

## 16. Contexto de la historia clínica

**1:30 · acumulado 17:50 · 4 · Diálogo, contexto y nota**

**Mensaje:** Incorporar HCIS exige seleccionar registros y conservar su procedencia.

Primero identificamos paciente y encuentro y fijamos un corte temporal. Conservamos antecedentes relevantes de otros episodios: no limitamos la historia al encuentro actual. Si hay pocos campos relevantes, podemos usar una consulta estructurada y añadirlos al prompt. Si la historia es extensa, podemos recuperar fragmentos y comparar estrategias. RAG organiza ese acceso; no obliga a usar una base vectorial.

El ejemplo muestra medicación activa en 2021, suspendida en 2025 y una afirmación actual del paciente. Recuperar solo la frase más parecida puede dar una versión antigua. Debemos conservar fuentes, fechas y discrepancias para revisión.

Medimos relevancia de lo recuperado y efecto en la nota: datos vigentes, paciente correcto y contradicciones. MedAlign ayuda a estudiar instrucciones sobre historias, pero no valida nuestro recuperador. El conector y el protocolo todavía son trabajo pendiente.

**Figura:** Seguir historia → filtro → selección → contexto; terminar en la discrepancia.

**Transición:** Con esas entradas, ¿qué comprobaciones podemos hacer al borrador?

## 17. Comprobaciones de la nota

**1:30 · acumulado 19:20 · 4 · Diálogo, contexto y nota**

**Mensaje:** Comprobar soporte es posible sin gold por encuentro; evaluar el comprobador requiere anotación.

«Niega fiebre» tiene soporte en la conversación. «Toma actualmente X» puede entrar en conflicto con una suspensión. «Auscultación normal» no está respaldada por las entradas disponibles.

Podemos buscar esos estados sin una nota de referencia en cada encuentro. Pero para saber si el verificador acierta necesitamos una muestra anotada: medir falsos avisos, errores que deja pasar y calibración.

Además, todas las frases pueden tener soporte y aun así faltar un dato importante, como el seguimiento. La completitud necesita criterios de qué debía incluirse. VeriFact estudia verificación contra EHR; Robust SOAP analiza hechos y omisiones usando referencias y conversación.

El soporte en una fuente tampoco prueba verdad clínica ni vigencia. Es una señal de revisión con límites propios.

**Figura:** Nota → evidencia; después preguntar qué evidencia importante no llegó a la nota.

**Transición:** Hay otro límite: el verificador puede compartir el error de entrada.

## 18. Propagación de errores

**1:00 · acumulado 20:20 · 4 · Diálogo, contexto y nota**

**Mensaje:** Los errores de entrada pueden sobrevivir a la generación y la comprobación.

El audio dice «no he tenido fiebre». Con una transcripción correcta, el generador puede escribir «niega fiebre». Si ASR pierde «no», puede escribir una nota fluida con el sentido opuesto.

Un verificador que solo lee ese ASR puede considerar respaldada la frase incorrecta. Una segunda pasada de LLM no constituye una comprobación independiente del audio.

Conservar transcripción, tiempos y vínculo con audio facilita localizar el fallo. Un modelo directo audio a nota también puede evaluarse con referencias externas, pero exige diseñar esa trazabilidad. Para estudiar sensibilidad vamos a controlar las entradas por etapas.

**Figura:** Contrastar las dos rutas del mismo audio.

**Transición:** Podemos convertir ese ejemplo en un experimento.

## 19. Experimento por etapas

**1:30 · acumulado 21:50 · 4 · Diálogo, contexto y nota**

**Mensaje:** Las ablaciones necesitan casos con referencias compatibles, no solo una tabla.

Partimos de casos con texto, hablantes y contexto revisados. En A usamos esas referencias. En B sustituimos el texto por ASR; en C también cambiamos hablantes por predicciones; en D introducimos contexto recuperado.

Mantenemos generador, plantilla, casos y criterios. Comparamos errores de la nota y ediciones. Para B proyectamos palabras ASR sobre intervalos de hablante de referencia mediante tiempos, con una regla explícita para solapamientos y revisión de casos ambiguos. No copiamos etiquetas por correspondencia textual.

Las diferencias miden sensibilidad en esta configuración, no una fracción universal de culpa de cada componente: hay interacciones. Si no tenemos historia emparejada en un corpus, hacemos el experimento de contexto en casos controlados separados. Y variantes sintéticas del mismo paciente o caso permanecen en el mismo split para evitar fuga.

**Figura:** Leer A→B→C→D; señalar qué cambia cada vez.

**Transición:** Cuando un fallo aparece de forma consistente, elegimos una intervención.

## 20. Qué adaptar y con qué datos

**1:20 · acumulado 23:10 · 5 · Adaptación y despliegue**

**Mensaje:** Adaptar tiene sentido cuando hay un error definido y datos adecuados.

Si ASR falla en fármacos o acentos, probamos preparación, vocabulario o un baseline distinto. Si persiste, fine-tuning requiere audio y transcripción médica española revisada, con test separado.

Si el problema es estilo o selección, trabajamos sobre plantilla, instrucciones y hechos. Una adaptación del generador necesita ejemplos y un objetivo coherente con la evaluación; optimizar una loss textual no garantiza fidelidad.

Si falla latencia o memoria, cambiamos motor, tamaño o precisión y repetimos calidad. Entrenar y optimizar la ejecución son intervenciones diferentes. La tabla conecta cada decisión con la evidencia que necesitaríamos, antes de invertir en entrenamiento.

**Figura:** Leer cada fila desde problema hasta datos.

**Transición:** La ejecución local añade una restricción concreta: recursos disponibles.

## 21. Recursos para ejecución local

**1:05 · acumulado 24:15 · 5 · Adaptación y despliegue**

**Mensaje:** Estimar memoria orienta candidatos; el consumo real se mide.

El README de Whisper estima unas dos, cinco y diez gigas de VRAM para small, medium y large en su implementación. Son referencias aproximadas; otros motores y precisiones cambian el consumo. Tampoco dicen cómo funcionarán en nuestro audio médico español.

Para un LLM de siete mil millones de parámetros, los pesos nominales ocupan unos catorce gigas en FP16 o tres y medio a cuatro bits. Faltan sobrecostes de cuantización, KV cache, buffers y los otros componentes.

Procesar por etapas o mantener modelos residentes cambia el presupuesto. Mediremos calidad, memoria, tiempo y concurrencia con el hardware objetivo; estos números todavía no dimensionan un servicio clínico.

**Figura:** Comparar barras de ASR y después cálculo nominal del LLM.

**Transición:** ¿Dónde encajan los modelos en el código que ya existe?

## 22. Scribnic: núcleo y clientes

**1:05 · acumulado 25:20 · 5 · Adaptación y despliegue**

**Mensaje:** Scribnic tiene una base reutilizable, con evaluación y producto aún por construir.

Scribnic ya separa core Python, backends y CLI. Tiene contratos para audio, intervalos de texto, hablantes y salida de pipeline. Puede combinar transcripción y diarización, usar reconocimiento conjunto y añadir generación opcional.

Esa separación permite reutilizar el núcleo desde un runner o un cliente. Ahora mismo el frontend es la CLI. El runner de evaluación, el contrato de contexto clínico y una aplicación de revisión son ampliaciones propuestas.

Los tests de contratos y la existencia de adaptadores no prueban calidad clínica ni que cada modelo sea viable en nuestro hardware. El siguiente paso es usar esa base para ejecutar casos y producir resultados comparables, antes de construir toda la aplicación.

**Figura:** Distinguir bloques existentes y conexiones discontinuas propuestas.

**Transición:** Cuando diseñemos el cliente, captura e integración pasarán a primer plano.

## 23. Captura e integración

**1:15 · acumulado 26:35 · 5 · Adaptación y despliegue**

**Mensaje:** La plataforma y el flujo pueden cambiar las entradas y el trabajo de revisión.

Podemos capturar desde PC, navegador, móvil, USB o un dispositivo Bluetooth. Una teleconsulta, por ejemplo en Teams, tiene canales y rutas de captura diferentes. Debemos comprobar qué llega realmente: codec, muestreo, interrupciones y pérdidas.

En procesamiento distinguimos ejecución local, servidor o mixta, y archivos o streaming. Streaming añade gestión de fragmentos y resultados parciales; tendremos que evaluar también su estabilidad. Definimos qué audio, texto y registros se conservan, dónde y durante cuánto tiempo.

En revisión puede haber ediciones por sección o instrucciones por voz. Eso genera una nueva versión que debe conservar trazabilidad. Integrar una interfaz, incluso embebida, o escribir la nota en HCIS no significa disponer de lectura de historia para generación. Son contratos y capacidades diferentes.

**Figura:** Seguir las tres columnas y sus restricciones inferiores.

**Transición:** El sistema final debe volver a medirse en ese entorno.

## 24. Evaluación del sistema desplegado

**1:05 · acumulado 27:40 · 5 · Adaptación y despliegue**

**Mensaje:** La configuración desplegada forma parte del sistema evaluado.

Fijamos casos y referencias y comparamos el entorno experimental con el destino: motor, precisión, hardware, preparación y captura. Debemos registrar también modelo, prompt y decodificación.

Medimos contenido y atribución junto con latencia mediana y percentil 95, memoria y concurrencia. El factor de tiempo real es tiempo de procesamiento dividido por duración de audio; depende de qué etapas incluyamos.

Tras cambiar motor o cuantización repetimos calidad. En un piloto añadimos fallos de operación, ediciones y una muestra revisada de notas. Las ediciones son señales útiles, pero no equivalen por sí solas a etiquetas de todos los errores: un profesional puede aceptar algo incorrecto.

**Figura:** Mismos casos → dos entornos → calidad y recursos.

**Transición:** Nos queda concretar los datos para poner en marcha ese protocolo.

## 25. Datos del primer experimento

**1:15 · acumulado 28:55 · 6 · Plan de trabajo**

**Mensaje:** Empezar con una prueba pequeña revisada y declarar qué no puede demostrar.

Propongo dos niveles iniciales. TEME permite explorar ASR en español médico sintético. PriMock permite probar el protocolo con audio, turnos y notas en inglés.

Para acercarnos a la nota española, podríamos preparar diez casos con contexto y adaptar cinco consultas PriMock: traducir diálogo y nota, revisar consistencia y generar o grabar audio. Anotamos lo realmente pronunciado y sus tiempos, incluidos errores de TTS; el guion no es automáticamente la transcripción gold. Son números de viabilidad, no validación de seguridad.

Los clínicos revisan hechos esperados, fuentes y errores, y comprobamos acuerdo antes de ampliar. Separaremos ajuste y test por caso. Después necesitaremos consultas reales del escenario, con un circuito institucional de recogida y revisión. Simulación, actores y jueces calibrados quedan desarrollados en el anexo y el bag de ideas.

**Figura:** Distinguir corpus públicos, datos que crearíamos y anotación clínica.

**Transición:** El primer entregable puede quedar definido con estas piezas.

## 26. Propuesta de trabajo

**1:05 · acumulado 30:00 · 6 · Plan de trabajo**

**Mensaje:** Entregar una evaluación que permita decidir qué mejorar.

El primer resultado sería un baseline local reproducible: casos con contexto y fuentes, plantilla y rúbrica; configuración en Scribnic y runner; informe de contenido, atribución, ediciones, tiempo y memoria.

Con esa evidencia decidimos si adaptar ASR, mejorar selección de hechos, incorporar recuperación o ajustar ejecución. Lo que funcione con suficiente calidad y viabilidad podrá pasar a un piloto supervisado.

El hospital aporta profesionales capaces de definir una nota útil y revisar errores. Esa colaboración es central para un escriba abierto y local. La propuesta de hoy es convertirla en datos y evaluación, y construir el producto apoyándonos en esos resultados.

**Figura:** Entradas → baseline → informe; terminar en la decisión.

**Transición:** Abrir preguntas. Los anexos contienen datos, losses, métodos e ideas adicionales.

## Anexos y preparación

No recorrer los cinco anexos dentro de los 30 minutos. Usarlos si aparece una pregunta:

- **A · Datasets y volumen:** modalidades, tamaños y acceso; [catálogo con fuentes](README.md).
- **B · Tarea, métrica y loss:** explicar qué se optimiza frente a qué se evalúa. En Nuance se combina CE con ranking de candidatos basado en ROUGE-L; no es una loss de seguridad clínica.
- **C · Hechos intermedios:** Nuance, ASCRIBE y KOSMOS; [ficha que leer primero](comprension-clinica.md).
- **D · Ampliar los datos:** historia simulada, consulta, perturbaciones y revisión; [bag de ideas](bag-of-ideas.md).
- **E · Lecturas:** elegir método y limitaciones de cada referencia antes de profundizar.

Lectura mínima para defender el bloque nuevo: [comprension-clinica.md](comprension-clinica.md), después **ASCRIBE §3.1 y prompt A.3**, **KOSMOS §2 y limitaciones**, y **Nuance §3.1.2**. Para verificación: **VeriFact, esquema y evaluación**, y **Robust SOAP, método de hechos/omisiones y perturbación de ASR**. Las fuentes originales están enlazadas en la ficha.

Practicar con [preguntas de defensa y mini examen](preguntas-defensa.md). Si no podemos explicar entrada, salida, mecanismo, datos de evaluación y un límite de un método, hay que releer esa parte antes de presentarla.

## Supuestos del primer experimento

Los **10 casos con contexto y cinco adaptaciones** son una propuesta de trabajo, no datos ya preparados ni un cálculo de potencia. El experimento de contexto puede usar historias controladas separadas de los corpora acústicos. Solo podrá hacerse la ablación completa donde existan referencias compatibles de todas las entradas.

Para concretar el baseline: elegir un ASR multilingüe disponible, un backend de diarización y un generador local que quepan en el hardware; fijar versiones y configuración. Whisper + diarizador + LLM con plantilla es un punto de partida posible, pendiente de medir frente a los adaptadores actuales. No se presenta aquí un ranking propio.

Las observaciones del vídeo de Tandem sirvieron para pensar en flujo y producto. No se ha obtenido una transcripción completa verificable del vídeo: no atribuimos como hechos comprobados su stack, fine-tuning ni resultados. Las funcionalidades citadas vienen de documentación primaria del producto.
