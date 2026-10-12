# Preguntas para preparar la técnica

Draft del **12/10/2026**. Para ensayar ante el grupo de data science; acompaña a la [presentación renovada y su guion](guion-presentacion.md). Las respuestas distinguen lo publicado, el diseño que proponemos y lo que todavía necesitamos medir.

## Preguntas que podrían hacernos

**1. ¿Qué estamos construyendo exactamente?**

Un sistema que transforma información del encuentro en un borrador revisable: conversación, contexto disponible y observaciones → nota. Hay que fijar especialidad, idioma, formato y responsabilidad de revisión. Codificar diagnósticos o recomendar tratamientos serían funciones adicionales, con evaluación propia.

**2. ¿Qué hace la selección de hechos? ¿Es otro modelo?**

Por ahora representa funciones: identificar hechos, sujeto, negación, fecha, incertidumbre y relevancia. Podrían resolverse dentro del prompt de generación o mediante extracción intermedia. Una lista de hechos con fuentes permite inspección, pero también puede perder información; esa arquitectura sigue siendo una hipótesis. En [Nuance, Singh et al., 2023, §3.1.2](https://aclanthology.org/2023.clinicalnlp-1.18/), el decoder aprende a generar un prefijo de hechos antes de la nota, a partir de la transcripción; eso no es recuperar una historia HCIS.

**3. ¿Por qué RAG? ¿No basta con incluir la historia en el prompt?**

Un contexto corto y seleccionado puede bastar como baseline. Retrieval cobra sentido cuando hay más historia de la que conviene introducir o necesitamos seleccionar evidencia. Identificamos paciente/encuentro y corte temporal, conservando antecedentes longitudinales relevantes; después recuperamos y evaluamos relevancia. [MedAlign](https://arxiv.org/abs/2308.14089) es un benchmark de instrucciones sobre EHR, no una validación de nuestro recuperador ni de audio→nota.

**4. ¿Cómo evaluáis quién dijo cada cosa y su efecto sobre la nota?**

DER/JER evalúan actividad y asignación de hablantes; cpWER/tcpWER evalúan palabras con atribución. Hay que fijar tolerancia temporal y tratamiento del solapamiento. S1/S2 son etiquetas anónimas, no médico/paciente: evaluar también roles y errores de la nota, por ejemplo convertir una pregunta del clínico en un síntoma afirmado por el paciente.

**5. ¿Cómo verificáis una nota sin etiquetas?**

Podemos contrastar afirmaciones con las entradas y señalar soporte, contradicción o falta de evidencia; [VeriFact](https://arxiv.org/abs/2501.16672) estudia esa formulación sobre EHR. Para saber si el verificador acierta sí necesitamos una muestra anotada. Además, todas las frases pueden estar respaldadas y aun así faltar una información importante. Si solo miramos un ASR erróneo, podemos validar su mismo error.

**6. ¿Qué datos españoles tenemos y qué demostrarían?**

El [catálogo](README.md) distingue español general, TEME con audio TTS y consultas clínicas en inglés. Tenemos rutas para explorar componentes y producir casos controlados; todavía necesitamos concretar una muestra próxima al uso local y sus anotaciones. Traducir PriMock o generar casos sintéticos permite ensayos repetibles, pero la transferencia a consulta real sigue siendo una pregunta. El [bag de ideas](bag-of-ideas.md) propone cómo avanzar.

**7. ¿Por qué entrenar algo si Whisper + un LLM ya funciona?**

Ese puede ser el baseline. Adaptaríamos después de localizar un fallo repetido: ASR para vocabulario/acústica, selección de contexto para omisiones de historia, instrucciones/plantilla para formato, generación para fidelidad persistente. Una transcripción correcta ayuda a separar errores del ASR y del generador. No podemos decidir qué fine-tunear mirando solo una nota final mala.

**8. ¿Qué necesita para correr local? ¿Podemos dar cifras?**

La configuración candidata es [MOSS 0.9B](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize) para texto/hablantes y [Qwen3-0.6B GGUF](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/tree/main) para nota mediante llama.cpp. Ambos tienen rutas CPU; aceleración GPU si existe. El archivo oficial Qwen Q8_0 ocupa 639 MB, pero eso no incluye memoria de ejecución. No tenemos aún medidas que permitan prometer una RAM mínima ni tiempo de respuesta. Hay que fijar PC, modelos, contexto y concurrencia y medir calidad, memoria máxima y tiempo por consulta.

**9. ¿Cuál sería nuestra aportación frente a productos existentes?**

La hipótesis es combinar un núcleo reutilizable de pipeline/evaluación con criterios y revisión clínica del hospital. En Scribnic hay contratos/backends para transcripción y hablantes y una CLI separable; evaluación clínica, contexto HCIS y aplicación de escritorio quedan por construir. Enseñar ese estado concreto permite explicar el siguiente paso. La calidad, utilidad y mantenimiento requieren evidencia.

**10. ¿Cómo demostraríais utilidad clínica?**

Con calidad de contenido y con tiempo hasta una nota aprobada, incluyendo revisión, correcciones e incidencias. Una nota más parecida a la referencia o con menos WER no prueba ahorro de trabajo. [Moramarco et al.](https://aclanthology.org/2022.acl-long.394/) evaluaron errores y post-edición con clínicos; nos sirve para diseñar esa parte, sin trasladar automáticamente sus resultados al español o a nuestro flujo.

## Mini examen — primero sin mirar las respuestas

Unos **25–35 minutos**. Contestar con un ejemplo o un experimento; reconocer una sigla no basta.

1. **Definir la tarea.** En cinco líneas: entradas disponibles, salida, papel del médico, criterio de éxito y una función fuera del alcance inicial.
2. **WER.** Una referencia de 10 palabras tiene 1 sustitución, 1 eliminación y 1 inserción. Calcula WER. ¿Qué cambiaría si la eliminación fuese «no»? ¿Cómo lo detectarías además del WER?
3. **Hablantes.** La referencia usa S1/S2 y la predicción intercambia ambas etiquetas sin cambiar los intervalos. ¿Debe aumentar DER? ¿Qué pasa si, tras eso, asignamos médico/paciente al revés?
4. **Contexto.** Distingue recuperar un registro, extraer un hecho, resolver su estado temporal y escribirlo en una nota. Pon una entrada/salida para cada operación y explica dónde podría intervenir un LLM.
5. **Sin gold.** El audio dice «no toma X», el ASR escribe «toma X» y la nota dice «toma X». El juez solo ve ASR y nota. ¿Qué puede detectar? ¿Qué necesitas para saber si su dictamen es correcto?
6. **Datos y splits.** Generas 100 versiones de audio a partir de 10 casos. ¿Son 100 consultas independientes? Diseña train/dev/test sin compartir el mismo caso. ¿Qué afirmación necesitaría datos humanos reales?
7. **Decidir qué mejorar.** El sistema falla con nombres de fármacos y con el formato SOAP. Propón pruebas que separen ambos problemas y una intervención para cada uno, antes de entrenar.
8. **Ablación.** Diseña una comparación para medir el efecto del ASR y otra para medir el contexto. ¿Qué mantienes fijo? ¿Por qué esas diferencias no son un reparto universal del error?
9. **Ejecución.** ASR procesa 10 minutos de audio en 45 segundos. Calcula RTF. ¿Demuestra eso que la nota completa estará disponible en 45 segundos? Enumera tres medidas más y cómo compararías FP16 con una versión cuantizada.
10. **Juez y validación.** Un juez coincide con médicos en el 95 % de ejemplos. ¿Qué falta saber antes de usarlo para filtrar revisión? Propón una prueba de utilidad del escriba que no se reduzca a esa cifra.

<details>
<summary>Respuestas orientativas — abrir después</summary>

1. Audio/conversación, contexto identificado y observaciones → borrador del formato elegido → aprobación médica. Éxito: calidad y menor esfuerzo total de cierre. Recomendación terapéutica autónoma sería otro alcance.
2. `(S + D + I) / N = 3 / 10 = 30 %`. El contador no pondera el significado de perder una negación. Añadir revisión de hechos, negaciones, medicación/dosis y gravedad con criterio clínico; fijar también la normalización textual.
3. La permutación de nombres se resuelve al puntuar diarización: por sí sola no añade confusión. El rol es otra etiqueta; invertirlo puede atribuir síntomas o decisiones a quien no corresponde aunque la diarización sea perfecta. Fijar collar y tratamiento del solapamiento para interpretar DER.
4. Recuperación: consulta → registros relevantes; extracción: texto → hecho con sujeto/fecha/fuente; reconciliación: afirmaciones de distintas fechas → estado o discrepancia; generación: hechos y reglas de documentación → nota. Introducir todo en un prompt puede combinar funciones, pero no elimina sus criterios de evaluación.
5. Puede comprobar consistencia entre esos textos, no recuperar de ahí la negación perdida. Necesitamos volver al audio o a una transcripción revisada y anotar el resultado para evaluar al juez. «Consistente con ASR» y «correcto respecto a la consulta» son resultados diferentes.
6. Son variantes correlacionadas de 10 casos. Separar familias de caso/pacientes antes de crear traducciones, ruido o TTS; reservar voces según la generalización que queramos medir. El rendimiento sobre conversación espontánea local y el esfuerzo real de edición necesitan contraste humano.
7. Revisar audio y transcripción para localizar errores de nombres; comparar ASR con otras configuraciones/modelos y ayudas de vocabulario cuando las soporten. Dar texto correcto al generador para probar plantilla/prompt por separado. Fine-tuning sería posterior si persiste un fallo y tenemos ejemplos supervisados adecuados.
8. Mismos casos, generador y contexto: texto revisado frente a ASR. Después mantener texto/roles y comparar contexto seleccionado con contexto recuperado o ausente. Validar que las referencias de roles sean compatibles con cada texto. Las interacciones y el orden de sustituciones afectan las diferencias.
9. `RTF = 45 / 600 = 0,075`. Falta generación, captura/transporte, colas y revisión. Medir memoria máxima, tiempos por etapa y latencia del flujo/concurrencia. Comparar configuraciones en los mismos casos, registrando runtime/hardware/decoding y calidad, además de velocidad.
10. Distribución de errores, gravedad, falsos negativos, falsos positivos, acuerdo entre médicos y rendimiento en casos nuevos; el agregado puede estar dominado por casos fáciles. Auditar también notas que el juez acepta. Para utilidad: comparación de calidad y tiempo hasta aprobación con un flujo habitual y casos equivalentes, controlando aprendizaje/orden.

</details>

## Cómo interpretar el resultado y qué leer

Por pregunta: **0** no la puedes explicar; **1** entiendes la idea pero no sabes concretar la prueba; **2** la explicas con ejemplo, protocolo y límite. La suma orienta el estudio; no certifica dominio completo. Priorizar cualquier fallo en contexto, verificación, datos o validación, aunque salga una puntuación alta.

| Si te atascas en… | Lee primero | Qué deberías poder explicar después |
|---|---|---|
| 1 · tarea y nota | [Contexto de la nota](clinical_note_context.md) | Qué viene de la conversación, de observaciones y de historia; qué se espera de A/P. |
| 2 · ASR y WER | [Jurafsky, cap. 16](https://web.stanford.edu/~jurafsky/slp3/16.pdf); [JiWER](https://github.com/jitsi/jiwer) | Un alineamiento con S/D/I y por qué un mismo WER puede ocultar distinto daño. |
| 3 · diarización | [dscore](https://github.com/nryant/dscore); [EEND](https://arxiv.org/abs/1909.05952) | Permutaciones, actividad, solapamiento y por qué rol no equivale a voz. |
| 4–5 · contexto/verificación | [Ficha de hechos y contexto](comprension-clinica.md); después [VeriFact](https://arxiv.org/abs/2501.16672) | Distinguir retrieval, extracción, generación y verificación; qué referencia necesita su evaluador. |
| 6 y 8 · datos/experimento | [Catálogo](README.md), [bag de ideas](bag-of-ideas.md), [ACI-Bench](https://www.nature.com/articles/s41597-023-02487-3) | Modalidades disponibles, splits y una comparación con entradas controladas. |
| 7 y 9 · adaptar/ejecutar | [Guion 24–28](guion-presentacion.md); [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Qué error aborda cada intervención y cómo medir el runtime final. |
| 10 · clínicos y juez | [Moramarco et al.](https://aclanthology.org/2022.acl-long.394/); [checklists de feedback](https://aclanthology.org/2025.emnlp-industry.104/) | Calidad, edición, acuerdo humano y errores que un juez deja pasar. |

Para cada paper que llevemos a la charla, poder decir **entrada → método → evaluación → límite para nuestro caso**. Si una respuesta está pendiente, terminar con el experimento que la resolvería y el dato que falta.

## Tres comprobaciones adicionales

- **¿Todo ASR actual es encoder–decoder con atención?** No. Explica CTC, predictor/joiner de transducer y decoder de atención; cita Parakeet TDT como derivado vigente. No confundas decoder neuronal con greedy/beam search.
- **¿Puede haber WER 0 y cpWER mayor que 0?** Sí: en el ejemplo de «tengo tos / desde cuándo», mover «desde» al otro hablante genera una inserción y una eliminación sobre cuatro palabras: cpWER 50 %.
- **¿Replicamos Robust SOAP?** Adaptamos el protocolo por hechos y perturbaciones. Español, audio, hablantes, historia y medidas del PC son extensiones. Su estudio no ejecuta ASR ni permite concluir que diarización sea inútil; [ficha breve](robust-soap.md).
