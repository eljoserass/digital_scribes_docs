# Guion — Construir un escriba digital médico

Versión renovada del **12/10/2026**. Acompaña a [main.pdf](build/main.pdf): **31 diapositivas principales, 30 minutos previstos y cinco anexos**. Los tiempos incluyen señalar figuras y pausas; falta ensayarlos. Las preguntas quedan fuera de los 30 minutos.

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
| Consulta y nota | 1–6 | 3:40 | 3:40 |
| Evaluación y datos | 7–8 | 1:55 | 5:35 |
| Audio y hablantes | 9–17 | 9:25 | 15:00 |
| Diálogo, contexto y nota | 18–24 | 7:40 | 22:40 |
| Adaptación y despliegue | 25–29 | 5:25 | 28:05 |
| Plan de trabajo | 30–31 | 1:55 | 30:00 |

## 1. Construir un escriba digital médico

**0:20 · acumulado 0:20 · 1 · Consulta y nota**

**Mensaje:** Seguir la información del encuentro hasta una nota revisada.

Quiero recorrer qué hay que resolver para construir un escriba digital médico. La entrada incluye una conversación y, cuando estén disponibles, contexto clínico y observaciones. La salida es un borrador que el profesional revisa antes de incorporarlo a la historia.

El recorrido conecta la tarea clínica con modelos, datos, evaluación y ejecución local. Terminaré con un primer experimento y con la base que ya estoy construyendo en Scribnic.

**Figura:** Audio y contexto → borrador → revisión.

**Transición:** Primero fijamos el objetivo y el alcance.

## 2. Objetivo y alcance

**0:30 · acumulado 0:50 · 1 · Consulta y nota**

**Mensaje:** Medir el trabajo completo, incluida la revisión.

Un escriba humano puede documentar bajo supervisión del profesional. El digital automatiza parte de ese trabajo. Algunas aplicaciones añaden informes, codificación o ayuda a decisiones; esas funciones tienen sus propios requisitos. Aquí vamos a centrarnos en documentar el encuentro.

Queremos una nota correcta que reduzca el esfuerzo de cerrarla. Contaremos también revisión y edición: un borrador rápido puede dar mucho trabajo después. El recorrido es consulta y nota, evaluación, audio y hablantes, generación con contexto, adaptación y despliegue, y plan de trabajo.

**Figura:** Recorrer consulta → nota cerrada; señalar la revisión.

**Transición:** Para definir la tarea necesitamos saber qué información tenemos.

## 3. Información del encuentro

**0:40 · acumulado 1:30 · 1 · Consulta y nota**

**Mensaje:** Conversación, historia y observaciones aportan datos distintos.

Seguiremos este ejemplo ficticio. El paciente refiere tos de tres días y niega fiebre. El clínico expresa que está en mejoría e indica una revisión en siete días. La conversación aporta esos hechos, quién los dijo y cuándo.

La historia añade una alergia registrada en 2019. No equivale a una confirmación actual. Y hoy se mide una temperatura de 36,7 grados, que podría entrar por una observación o un campo manual.

El bloque inferior reúne las entradas para generar, todavía no es la nota. La flecha del contexto es discontinua porque su disponibilidad depende del flujo y del conector.

**Figura:** Señalar un dato de cada fuente; distinguir negación referida de medición.

**Transición:** Veamos qué hacemos con estas entradas al escribir una nota.

## 4. La nota SOAP

**0:55 · acumulado 2:25 · 1 · Consulta y nota**

**Mensaje:** La nota selecciona y organiza información con una función clínica.

SOAP separa subjetivo, objetivo, valoración y plan. En subjetivo documentamos el relato del paciente: tos y ausencia de fiebre según refiere. En objetivo aparece la temperatura medida. Son afirmaciones relacionadas, pero proceden de fuentes distintas.

Valoración recoge el juicio expresado por el clínico y plan recoge su decisión de seguimiento. En este alcance, el modelo documenta esas decisiones; no inventa una nueva valoración clínica. La alergia antigua puede ir en una sección de antecedentes, conservando su fecha y necesidad de confirmación.

SOAP es un ejemplo. Cada servicio puede necesitar otros campos y estilos. Definirlos permite distinguir una omisión importante de algo que no corresponde incluir.

**Figura:** Recorrer S, O, A, P y su procedencia.

**Transición:** Ya tenemos entrada y salida; ahora podemos abrir el proceso.

## 5. Pipeline del escriba

**0:35 · acumulado 3:00 · 1 · Consulta y nota**

**Mensaje:** Cada etapa necesita entradas y salidas inspeccionables.

El audio pasa a texto con tiempos y hablantes. Con ese texto, el contexto disponible y las observaciones seleccionamos información y generamos un borrador.

La selección puede ocurrir dentro del LLM o producir hechos intermedios: después compararé ambas rutas. La caja de comprobación busca soporte y conflictos para ayudar a revisar. Su presencia no garantiza calidad; también tendremos que medir sus errores. Finalmente revisa el profesional y se guarda la nota aprobada.

El esquema describe funciones. No implica que todas estén implementadas ni que cada caja necesite un modelo independiente.

**Figura:** Seguir el flujo horizontal y después las dos entradas adicionales.

**Transición:** Antes de evaluarlo, situemos el producto dentro del flujo clínico.

## 6. Del escriba al flujo clínico

**0:40 · acumulado 3:40 · 1 · Consulta y nota**

**Mensaje:** La nota es el punto de entrada a un flujo clínico más amplio.

Tandem presenta su dirección de producto como un sistema operativo para clínicas: preparar la consulta con la historia, documentar, facilitar acceso a evidencia, codificar y organizar seguimiento. Abridge también anuncia funciones antes, durante y después del encuentro. Hay funcionalidades disponibles y otras sujetas a despliegue y mercado; son fuentes comerciales, no evidencia de eficacia.

Apoyar decisiones puede incluir consultar guías en el contexto del paciente. No lo equiparemos con diagnosticar autónomamente. Nuestro alcance sigue siendo documentar y revisar la nota; cada ampliación necesita datos y evaluación propios.

**Figura:** Recorrer antes, durante y después; señalar la nota como alcance actual.

**Transición:** Para construir esa parte necesitamos definir cómo sabremos que funciona.

## 7. Evaluación

**0:50 · acumulado 4:30 · 2 · Evaluación y datos**

**Mensaje:** Evaluar componentes, contenido y utilidad responde a preguntas diferentes.

En audio y hablantes medimos palabras reconocidas y atribución. Eso ayuda a localizar fallos concretos.

En la nota preguntamos qué hechos faltan, cuáles se añadieron sin soporte y cuáles cambiaron de sentido. Nos interesan negación, sujeto, fecha y decisiones documentadas. Una métrica de similitud textual puede complementar esta evaluación, pero no sustituye una rúbrica de contenido.

En el uso clínico medimos correcciones, esfuerzo de revisión y tiempo total. Una reducción de WER no demuestra por sí sola una mejora de trabajo. Para medir errores necesitamos referencias; para valorar su importancia necesitamos criterio clínico.

**Figura:** Bajar por los tres niveles, sin desarrollar siglas todavía.

**Transición:** La siguiente pregunta es con qué datos podemos medir cada nivel.

## 8. Datos de evaluación

**1:05 · acumulado 5:35 · 2 · Evaluación y datos**

**Mensaje:** No tenemos un único corpus público que cubra todo nuestro caso de uso.

Las referencias generales comprueban componentes: LibriSpeech tiene 960 horas de entrenamiento en inglés leído; AMI unas cien horas de reuniones; FLEURS incluye español entre sus 102 idiomas.

PriMock57 aporta 57 consultas simuladas en inglés, ocho horas y 38 minutos de duración clínica, con audio, turnos y notas. ACI-Bench contiene 207 encuentros textuales y MTS-Dialog 1.701 pares breves; no sirven para evaluar toda la entrada acústica.

TEME aporta 90 diálogos médicos en español y unas cuatro horas de audio TTS. Tiene voces y etiquetas por turno, pero sus estimaciones temporales no son una referencia gold para DER. Será un control exploratorio, no prueba de calidad en consultas espontáneas. Al final concretaré cómo cubrir los huecos.

**Figura:** Comparar columnas: modalidad, idioma y dominio.

**Transición:** Entramos ahora en el audio, empezando por lo que ve el modelo.

## 9. Señal y representación acústica

**1:00 · acumulado 6:35 · 3 · Audio y hablantes**

**Mensaje:** La representación acústica conserva información distinta del texto.

Estas figuras de Jurafsky muestran la misma frase de conversación espontánea en inglés. Arriba en la onda vemos cambios de amplitud y alineamiento con palabras y fonemas. Los límites no son tan limpios como en el texto.

El espectrograma representa energía por frecuencia y tiempo, calculada sobre ventanas. Podemos transformarlo a una escala Mel y usar log-Mel, como Whisper, o aprender representaciones desde la onda en otras arquitecturas.

Antes del modelo ya importan micrófono, canales, muestreo, ruido y compresión. Remuestrear a una frecuencia más alta no recupera información perdida. Hay que usar la preparación que espera el modelo y reproducirla en evaluación y despliegue.

**Figura:** Alinear una palabra entre las dos figuras; señalar ejes de tiempo y frecuencia.

**Transición:** Con esa secuencia acústica, ¿cómo se producen las palabras?

## 10. CTC, transducer y atención

**1:20 · acumulado 7:55 · 3 · Audio y hablantes**

**Mensaje:** CTC, transducer y atención conviven; las fechas no son una sucesión de reemplazos.

Las tres rutas convierten representaciones del audio en tokens. CTC predice etiquetas por paso acústico y colapsa repeticiones y blancos. Es sencillo de decodificar, pero su salida básica no condiciona cada etiqueta en el texto anterior.

RNN-T significa Recurrent Neural Network Transducer. Combina el encoder acústico con un predictor del texto previo y una red conjunta. Puede emitir un token sin avanzar el audio; el blanco avanza el tiempo. Esto permite aprender el alineamiento y usar contexto textual. Que sea incremental depende también del encoder. Los derivados siguen vigentes: Parakeet TDT predice además duraciones para saltar pasos, así que no es idéntico al RNN-T original.

El encoder–decoder con atención, como Whisper, consulta el audio y los tokens anteriores al generar cada token. Hay modelos actuales en las tres familias. «Encoder–decoder» en sentido amplio no basta para distinguirlas: aquí hablamos específicamente del basado en atención.

**Figura:** Comparar cómo cada ruta produce texto; las fechas sitúan antecedentes.

**Transición:** Abramos ese decoder con un ejemplo de Whisper.

## 11. Qué hace el decoder

**1:10 · acumulado 9:05 · 3 · Audio y hablantes**

**Mensaje:** El decoder neuronal y el algoritmo de decoding son cosas distintas.

En Whisper, el decoder es un Transformer. Recibe los tokens anteriores, aplica atención sobre ese texto y sobre la representación del audio, y devuelve probabilidades para el siguiente token. Incluye capas de atención y redes feed-forward; no es simplemente una convolución. Las probabilidades de la figura son inventadas para ilustrar el mecanismo.

Después hay que elegir una secuencia. Greedy toma el token más probable en cada paso; beam search mantiene varias hipótesis. Ese procedimiento es el decoding. En CTC también decodificamos, aunque no haya un decoder autoregresivo como el de Whisper. En un transducer intervienen el predictor del prefijo y la red conjunta. Los tres producen texto, con mecanismos distintos.

El contexto textual ayuda a resolver ambigüedad, pero una salida plausible puede ser incorrecta respecto al audio.

**Figura:** Seguir audio y prefijo → distribución → elección → realimentación.

**Transición:** Midamos primero las palabras y después qué errores importan clínicamente.

## 12. WER y errores clínicos

**1:00 · acumulado 10:05 · 3 · Audio y hablantes**

**Mensaje:** WER cuenta ediciones; la gravedad clínica necesita otra lectura.

Word Error Rate suma sustituciones, eliminaciones e inserciones, dividido por las palabras de referencia. En estos ejemplos cambia una palabra de siete. El valor es el mismo, pero perder una negación cambia el hecho clínico.

¿Qué hacemos con ello? Desglosar nombres de fármacos, dosis, negación y omisiones con referencias revisadas. Para vocabulario raro podemos probar hotwords si el modelo los admite. Si persisten fallos sistemáticos, considerar fine-tuning con audio y texto clínico español, manteniendo un test separado. No asumimos que una corrección con LLM recupere lo que no se oyó: también puede inventarlo.

**Figura:** Señalar S, D, I y N; comparar el significado de ambos errores.

**Transición:** Aunque las palabras estén bien, todavía podemos atribuirlas a otra persona.

## 13. Diarización: tiempo, hablante y rol

**0:45 · acumulado 10:50 · 3 · Audio y hablantes**

**Mensaje:** Hablante anónimo, rol clínico e identidad son etiquetas diferentes.

Diarización responde quién habla y cuándo, usando etiquetas anónimas como S1 y S2. Las barras muestran actividad y los intervalos señalados muestran solapamiento.

Después atribuimos palabras a esos hablantes. Por separado podemos asignar roles como clínico y paciente, usando información del diálogo o del flujo y comprobando que acierta. S1 por sí solo no identifica una persona ni establece un rol.

La diferencia importa para la nota: una pregunta del clínico no equivale a un síntoma afirmado por el paciente. Y «mi madre toma X» necesita además atribución semántica del hecho, aunque sepamos quién pronunció la frase.

**Figura:** Tiempo → palabras → rol, en ese orden.

**Transición:** Veamos dos maneras de estimar la actividad de hablantes.

## 14. Modelos de diarización

**1:05 · acumulado 11:55 · 3 · Audio y hablantes**

**Mensaje:** Agrupar voces y predecir actividad conjunta son dos formas de resolver la tarea.

En una pipeline modular detectamos regiones de habla, calculamos vectores que describen la voz y agrupamos los parecidos. La segmentación es localizar intervalos; el embedding representa características de la voz. Podemos sustituir o adaptar esos módulos, pero sus errores se acumulan.

EEND recibe una secuencia de características acústicas y aprende, por paso temporal, qué hablantes están activos; varios pueden estarlo a la vez. «Red temporal» quería decir una red que procesa secuencias, por ejemplo un Transformer, no una arquitectura concreta. Aprender actividad conjunta ayuda a representar solapamientos. La duración y el número de hablantes admitidos dependen de la variante.

**Figura:** Comparar las dos rutas hasta llegar a intervalos con hablantes.

**Transición:** Para evaluarlos, contemos segundos de habla atribuidos incorrectamente.

## 15. DER: cuánto tiempo se atribuyó mal

**1:05 · acumulado 13:00 · 3 · Audio y hablantes**

**Mensaje:** DER mide tiempo, no palabras.

Diarization Error Rate suma habla omitida, falsa alarma y confusión de hablante, dividido por el tiempo de habla de referencia. Antes se emparejan las etiquetas arbitrarias: llamar S1 a quien la referencia llama S2 no es por sí solo un error.

Aquí hay diez segundos de habla, sin solapamiento. El cambio correcto ocurre en el segundo cinco, pero el modelo lo retrasa al seis: un segundo de confusión, DER del diez por ciento. No hay omisiones ni falsas alarmas en este ejemplo.

Hay que declarar si se puntúan solapamientos y qué margen se excluye alrededor de los límites, el collar. Cambiar ese protocolo cambia el resultado. DER no sabe si la palabra mal atribuida era una alergia o una despedida.

**Figura:** Señalar el intervalo rojo y el denominador de diez segundos.

**Transición:** Cuando obtenemos texto y hablantes juntos, necesitamos medir también las palabras atribuidas.

## 16. Transcripción con hablantes

**0:40 · acumulado 13:40 · 3 · Audio y hablantes**

**Mensaje:** Texto y hablantes pueden salir de módulos separados o de un modelo conjunto.

La ruta modular alinea texto ASR con segmentos de diarización. Otra ruta genera texto, tiempos y etiquetas de hablante conjuntamente, como MOSS. Una salida común permite comparar ambas sin cambiar el resto del sistema: inicio, fin, hablante y texto.

SOT, Serialized Output Training, es una forma de ordenar texto y separadores en una secuencia objetivo. No hace falta desarrollar aquí su entrenamiento. Lo relevante es comprobar qué información entrega el modelo y cómo falla.

**Figura:** Seguir ambas rutas hacia el mismo formato de turnos.

**Transición:** Este ejemplo muestra por qué WER solo no basta para compararlas.

## 17. Palabras correctas, hablante equivocado

**1:20 · acumulado 15:00 · 3 · Audio y hablantes**

**Mensaje:** Una transcripción puede tener todas las palabras y atribuirlas mal.

La referencia dice S1: «tengo tos» y S2: «desde cuándo». La predicción contiene las mismas palabras en orden, pero asigna «desde» a S1. WER global da cero.

cpWER significa Concatenated minimum-Permutation Word Error Rate. Concatenamos el texto de cada hablante y buscamos el mejor emparejamiento de etiquetas. En este caso hay una inserción en S1 y una eliminación en S2: dos errores entre cuatro palabras, cincuenta por ciento. La permutación evita penalizar un simple cambio de nombres de hablante.

tcpWER significa Time-Constrained minimum-Permutation Word Error Rate. Añade límites temporales a qué palabras pueden alinearse, con una tolerancia fijada en el protocolo. Así dificulta emparejar una palabra con otra repetición muy lejana en la consulta. Necesitamos tiempos fiables para calcularlo.

**Figura:** Seguir la palabra «desde»; explicar sus dos efectos en el cálculo.

**Transición:** Ya tenemos diálogo atribuido. Convertirlo en nota exige seleccionar y organizar información.

## 18. Generación de notas

**0:45 · acumulado 15:45 · 4 · Diálogo, contexto y nota**

**Mensaje:** El baseline generativo necesita un contrato clínico antes que una arquitectura sofisticada.

La primera ruta es un LLM que recibe transcripción con hablantes, contexto disponible, observaciones y una plantilla. Define las secciones y conserva los hechos y decisiones documentadas.

El equipo clínico aporta algo concreto: contenido que debe aparecer, información que sobra, estilo del servicio y ejemplos de errores. Esas decisiones se convierten en instrucciones y en una rúbrica, no solo en un prompt que parece funcionar.

Podemos comparar plantillas y prompts sobre encuentros fijados. Si encontramos errores persistentes, decidiremos si hace falta extracción adicional, mejores entradas o adaptación de pesos. Ahora vamos a abrir la selección de información.

**Figura:** Entradas → generador con criterios → borrador.

**Transición:** ¿Se selecciona lo relevante mientras se redacta o antes?

## 19. Selección de hechos

**1:25 · acumulado 17:10 · 4 · Diálogo, contexto y nota**

**Mensaje:** Los hechos intermedios son una hipótesis que comparar, no una garantía.

La ruta directa decide relevancia al escribir. La alternativa hace explícitos hechos con fuente, sujeto, negación y momento antes de generar. Mantendría también el diálogo original para reducir el riesgo de que una extracción incompleta cierre el acceso a evidencia.

En «mi madre toma X», hay que conservar que la persona es la madre. Una lista que extraiga solo medicamento y verbo ya perdió información.

ASCRIBE genera hechos, fragmentos de soporte y relevancia antes de SOAP; estudia prompting y adaptación en tailandés. Es un preprint reciente con evaluación clínica limitada. KOSMOS construye entidades, atributos y relaciones; las mejoras son modestas y la extracción no se evalúa de forma independiente.

Nuance, en 2023, es un antecedente de planificación con hechos. Ninguno de estos métodos resuelve por sí mismo el acceso al HCIS. Nuestra comparación sería directo frente a hechos con fuente más diálogo, con el resto fijado.

**Figura:** Recorrer las dos rutas y analizar el sujeto del ejemplo.

**Transición:** Extraer del diálogo es distinto de seleccionar información de la historia.

## 20. Qué aporta la historia clínica

**1:40 · acumulado 18:50 · 4 · Diálogo, contexto y nota**

**Mensaje:** La historia aporta información que puede no repetirse durante la consulta.

«Mantenemos el tratamiento habitual» no contiene el nombre ni la dosis. Un registro reciente puede aportar esa información, conservando fecha y procedencia. Si no hay un estado fiable, no debemos completar por intuición. El contexto también puede estar obsoleto o contradecir lo dicho hoy.

Primero fijamos paciente y corte temporal. Después seleccionamos registros pertinentes, con consultas estructuradas o retrieval; una historia corta puede entrar directamente. RAG es una opción para seleccionar contexto, no un requisito universal ni una garantía de mejora.

Hay evidencia inicial: Zuckerman y colaboradores comparan documentación con y sin historia en 354 encuentros y encuentran mayor completitud. Es un preprint con evaluación principalmente automática, revisión humana limitada y autores vinculados al proveedor. Nos sirve para justificar una comparación, no para prometer el mismo efecto en español o con nuestro modelo.

**Figura:** Mostrar qué dato falta en la conversación y qué fuente permite añadirlo.

**Transición:** Una vez generado el borrador, podemos comprobar qué afirmaciones están respaldadas.

## 21. Qué comprueba el verificador

**1:25 · acumulado 20:15 · 4 · Diálogo, contexto y nota**

**Mensaje:** Ejecutar un chequeo y demostrar que acierta requieren información distinta.

Durante el uso, un verificador puede contrastar cada afirmación de la nota con la transcripción y la historia disponible. La salida distingue soporte, contradicción o evidencia insuficiente, idealmente con el fragmento correspondiente. No necesita una nota de referencia para cada consulta.

Para evaluar ese verificador sí necesitamos casos anotados: médicos revisan afirmaciones y evidencia, y medimos qué errores detecta y qué falsas alarmas produce. La comprobación automática también puede fallar. Además, verificar solo lo escrito no detecta todos los hechos importantes que faltan.

Robust SOAP ilustra otra distinción útil para evaluación: algo ausente de la nota de referencia puede estar respaldado por el diálogo. No debemos llamar alucinación a cualquier diferencia respecto a una única nota.

**Figura:** Recorrer las tres afirmaciones y separar «en uso» de «para evaluarlo».

**Transición:** Si se pierde información antes de generar, estos controles pueden compartir el mismo error.

## 22. Propagación de errores

**0:45 · acumulado 21:00 · 4 · Diálogo, contexto y nota**

**Mensaje:** Los errores de entrada pueden sobrevivir a la generación y la comprobación.

El audio dice «no he tenido fiebre». Con una transcripción correcta, el generador puede escribir «niega fiebre». Si ASR pierde «no», puede escribir una nota fluida con el sentido opuesto.

Un verificador que solo lee ese ASR puede considerar respaldada la frase incorrecta. Una segunda pasada de LLM no constituye una comprobación independiente del audio.

Conservar transcripción, tiempos y vínculo con audio facilita localizar el fallo. Un modelo directo audio a nota también puede evaluarse con referencias externas, pero exige diseñar esa trazabilidad. Para estudiar sensibilidad vamos a controlar las entradas por etapas.

**Figura:** Contrastar las dos rutas del mismo audio.

**Transición:** Podemos convertir ese ejemplo en un experimento.

## 23. Evaluar cada etapa: SCRIBE

**1:05 · acumulado 22:05 · 4 · Diálogo, contexto y nota**

**Mensaje:** SCRIBE conecta cada componente del escriba con una evaluación concreta.

Esta es la figura original de Wang y colaboradores. Evalúan un escriba propio con 40 grabaciones reales de consultas prenatales. El diagrama sigue audio, transcripción, atribución de hablantes y nota; debajo muestra cómo comprobar cada salida y cómo introducir errores para estudiar qué llega al documento final.

Señalaré tres zonas: evaluación de transcripción, evaluación de atribución y evaluación de nota. En esta última combinan revisión, métricas, jueces y simulaciones. Nuestro plan se parece a ese marco, adaptado a nuestros datos, español y ejecución local; aún no es una réplica realizada.

**Aclaración oral si surge:** Sí tratan diarización, pero su método asigna hablantes sobre el texto con LLM tras transcribir. No es la misma operación que agrupar voces acústicamente. También simulan errores de atribución. No confundamos este paper con Robust SOAP, que se centra en notas y perturbaciones textuales.

**Figura:** Recorrer la fila superior y las tres zonas inferiores, sin leer todas las celdas. El stack es el de los autores, no el nuestro.

**Transición:** El segundo panel explica por qué combinan varias formas de evaluar.

## 24. Combinar evaluadores

**0:35 · acumulado 22:40 · 4 · Diálogo, contexto y nota**

**Mensaje:** Cada evaluador aporta una perspectiva y tiene límites.

La revisión clínica aporta criterio y referencias, pero consume tiempo. Las métricas facilitan comparaciones repetibles; no capturan toda la importancia clínica. Un juez LLM puede ampliar la escala, pero necesitamos contrastarlo con revisores y medir sus propios errores.

El Venn es una propuesta conceptual del paper, no una garantía de que los LLM entiendan correctamente todos los casos. Para nosotros, la pregunta práctica es qué automatizar después de comprobar su acuerdo con los médicos.

**Figura:** Señalar los tres círculos, sin leer cada intersección.

**Transición:** Esas evaluaciones orientan qué adaptar; además mediremos tiempo y memoria en el equipo de uso.

## 25. Qué adaptar y con qué datos

**1:00 · acumulado 23:40 · 5 · Adaptación y despliegue**

**Mensaje:** El diagnóstico del fallo orienta qué adaptar y qué medir después.

Si el ASR falla en términos o acentos, podemos probar vocabulario y, si hace falta, ajustar con audio y texto revisado. Si la nota omite hechos o tiene un formato inadecuado, probamos plantilla, prompt o selección de información, con referencias clínicas.

También puede ser correcta pero tardar demasiado o no caber en memoria. Ahí probamos un modelo menor, otro motor o cuantización. La evaluación incorpora calidad, tiempo y recursos en el equipo de uso: una optimización es útil si conserva calidad suficiente.

**Figura:** Recorrer las tres filas como fallo → intervención → datos necesarios.

**Transición:** Concretemos una configuración candidata para el PC del médico.

## 26. Un escriba en el PC del médico

**1:20 · acumulado 25:00 · 5 · Adaptación y despliegue**

**Mensaje:** Hay candidatos pequeños para probar en local; falta medir el sistema completo.

MOSS-Transcribe-Diarize de 0.9B produce texto y hablantes. Su código contempla CPU y GPU. Eso demuestra una ruta de ejecución, no que vaya suficientemente rápido en cualquier PC.

Para la nota podemos empezar con Qwen3-0.6B en llama.cpp, que admite CPU y aceleración GPU si existe. El archivo oficial GGUF Q8_0 ocupa 639 MB en disco. La memoria de ejecución será mayor por buffers, contexto y estados; no es una cifra de RAM total del escriba. Un modelo tan pequeño es un candidato para medir, no una garantía de calidad clínica.

Fijaremos equipo, versiones, duración de consulta, contexto y concurrencia. Mediremos memoria máxima, tiempo y contenido de la nota. Si no da calidad o velocidad suficiente, esa evidencia dirá qué componente cambiar.

**Figura:** Señalar los dos modelos dentro del PC y las tres medidas pendientes.

**Transición:** Scribnic permite probar componentes y reutilizar después la pipeline desde una interfaz.

## 27. Scribnic: de la CLI a una aplicación

**1:00 · acumulado 26:00 · 5 · Adaptación y despliegue**

**Mensaje:** La interfaz puede cambiar mientras el núcleo y los datos siguen siendo reutilizables.

Hoy Scribnic tiene un núcleo Python, modelos intercambiables, configuración y una CLI. Los datos principales son el audio, los turnos con tiempo y hablante, y el borrador. Esa estructura permite probar backends sin ligar la lógica a una pantalla.

La propuesta es que una aplicación de escritorio o web use ese mismo núcleo para grabar o cargar, revisar y editar. La CLI sigue sirviendo para experimentos. El cliente clínico, la integración de historia y la evaluación clínica aún están pendientes; no estamos mostrando un producto terminado.

**Figura:** De terminal a aplicación; ambos apuntan al mismo núcleo y formato de datos.

**Transición:** La plataforma elegida determinará la captura y cómo llega el resultado al profesional.

## 28. Captura e integración

**1:05 · acumulado 27:05 · 5 · Adaptación y despliegue**

**Mensaje:** La plataforma y el flujo pueden cambiar las entradas y el trabajo de revisión.

Podemos capturar desde PC, navegador, móvil, USB o un dispositivo Bluetooth. Una teleconsulta, por ejemplo en Teams, tiene canales y rutas de captura diferentes. Debemos comprobar qué llega realmente: codec, muestreo, interrupciones y pérdidas.

En procesamiento distinguimos ejecución local, servidor o mixta, y archivos o streaming. Streaming añade gestión de fragmentos y resultados parciales; tendremos que evaluar también su estabilidad. Definimos qué audio, texto y registros se conservan, dónde y durante cuánto tiempo.

En revisión puede haber ediciones por sección o instrucciones por voz. Eso genera una nueva versión que debe conservar trazabilidad. Integrar una interfaz, incluso embebida, o escribir la nota en HCIS no significa disponer de lectura de historia para generación. Son contratos y capacidades diferentes.

**Figura:** Seguir las tres columnas y sus restricciones inferiores.

**Transición:** El sistema final debe volver a medirse en ese entorno.

## 29. Evaluación del sistema desplegado

**1:00 · acumulado 28:05 · 5 · Adaptación y despliegue**

**Mensaje:** La configuración desplegada forma parte del sistema evaluado.

Fijamos casos y referencias y comparamos el entorno experimental con el destino: motor, precisión, hardware, preparación y captura. Debemos registrar también modelo, prompt y decodificación.

Medimos contenido y atribución junto con latencia mediana y percentil 95, memoria y concurrencia. El factor de tiempo real es tiempo de procesamiento dividido por duración de audio; depende de qué etapas incluyamos.

Tras cambiar motor o cuantización repetimos calidad. En un piloto añadimos fallos de operación, ediciones y una muestra revisada de notas. Las ediciones son señales útiles, pero no equivalen por sí solas a etiquetas de todos los errores: un profesional puede aceptar algo incorrecto.

**Figura:** Mismos casos → dos entornos → calidad y recursos.

**Transición:** Nos queda concretar los datos para poner en marcha ese protocolo.

## 30. Datos del primer experimento

**1:05 · acumulado 29:10 · 6 · Plan de trabajo**

**Mensaje:** Adaptamos el marco SCRIBE a nuestros datos y a la ejecución local.

La idea es reproducir la lógica de evaluación por etapas y de la nota completa, con revisión clínica, métricas, jueces contrastados y simulaciones. Español, contexto longitudinal y restricciones del PC son aspectos que debemos concretar. Primero podemos comprobar partes del protocolo con PriMock y explorar ASR español sintético con TEME.

Proponemos diez casos controlados con contexto y cinco consultas adaptadas al español y revisadas. Son cantidades de viabilidad, no validación del producto. Necesitamos hechos esperados, fuentes, rúbrica y acuerdo entre revisores; separar los casos de ajuste de los de test.

Los autores usan datos clínicos que no son públicos. Tendremos que preparar nuestras referencias y evaluar con clínicos. Datos sintéticos y traducciones no sustituyen una evaluación posterior del escenario real.

**Figura:** Recorrer componentes, contexto y protocolo clínico.

**Transición:** El primer entregable será un baseline medible y un informe de dónde falla.

## 31. Propuesta de trabajo

**0:50 · acumulado 30:00 · 6 · Plan de trabajo**

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

Para las figuras de evaluación: [ficha SCRIBE](scribe-evaluacion.md), figura 1 y Methods del artículo.

Lectura mínima para defender el bloque de generación: [comprension-clinica.md](comprension-clinica.md), después **ASCRIBE §3.1 y prompt A.3**, **KOSMOS §2 y limitaciones**, y **Nuance §3.1.2**. Para verificación: **VeriFact, esquema y evaluación**, y **Robust SOAP, método de hechos/omisiones y perturbación de ASR**. Las fuentes originales están enlazadas en la ficha.

Practicar con [preguntas de defensa y mini examen](preguntas-defensa.md). Si no podemos explicar entrada, salida, mecanismo, datos de evaluación y un límite de un método, hay que releer esa parte antes de presentarla.

## Supuestos del primer experimento

Los **10 casos con contexto y cinco adaptaciones** son una propuesta de trabajo, no datos ya preparados ni un cálculo de potencia. El experimento de contexto puede usar historias controladas separadas de los corpora acústicos. Solo podrá hacerse la ablación completa donde existan referencias compatibles de todas las entradas.

Para concretar el baseline: elegir un ASR multilingüe disponible, un backend de diarización y un generador local que quepan en el hardware; fijar versiones y configuración. MOSS 0.9B + Qwen3-0.6B con plantilla es una configuración candidata, pendiente de medir frente a otras opciones. No se presenta aquí un ranking propio.

Las observaciones del vídeo de Tandem sirvieron para pensar en flujo y producto. No se ha obtenido una transcripción completa verificable del vídeo: no atribuimos como hechos comprobados su stack, fine-tuning ni resultados. Las funcionalidades citadas vienen de documentación primaria del producto.
