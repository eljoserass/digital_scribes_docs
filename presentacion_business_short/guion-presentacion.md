# Escribas digitales · guion de 10 minutos

Versión visual: **12/10/2026**. [PDF](build/main.pdf) · [Fuente editable](main.tex) · [Investigación](contexto-investigacion.md).

**13 diapositivas, cinco secciones, 10 minutos aproximados.** El ahorro mensual se integra en la figura de beneficios, con el resultado base y las hipótesis a la vista. Las ideas se reparten en figuras breves; los detalles comerciales quedan en el informe y en estas notas. Los tiempos incluyen señalar las figuras y hacer pausas; son una pauta pendiente de ensayo. Preguntas después.

| Diapositiva | Idea | Tiempo | Acumulado |
| --- | --- | ---: | ---: |
| 1 | Escribas digitales | 0:25 | 0:25 |
| 2 | Un asistente para documentar la consulta | 0:55 | 1:20 |
| 3 | Ejemplo: de tres fuentes a una nota SOAP | 1:00 | 2:20 |
| 4 | El beneficio que buscamos: menos carga documental | 1:05 | 3:25 |
| 5 | Hay que medir hasta que la nota queda cerrada | 0:50 | 4:15 |
| 6 | El mercado de escribas crece con rapidez | 0:50 | 5:05 |
| 7 | Muchas ofertas; varias formas de llegar al hospital | 0:25 | 5:30 |
| 8 | El encaje que buscamos tiene cuatro piezas | 0:35 | 6:05 |
| 9 | Hay candidatos; el encaje sigue por demostrar | 0:55 | 7:00 |
| 10 | Dos vías que podemos poner a prueba | 0:45 | 7:45 |
| 11 | Los mismos casos permiten una comparación justa | 0:55 | 8:40 |
| 12 | Siguiente paso: comparar antes de pilotar | 0:45 | 9:25 |
| 13 | La decisión ahora: iniciar una evaluación local | 0:35 | 10:00 |

## 1. Escribas digitales · 0:25

«Queremos entender qué es un escriba digital, por qué está generando tanto interés y qué opciones merecen una evaluación para nuestro hospital. El contexto es atención en español y Dedalus HCIS. Recorreremos cinco bloques: funcionamiento, importancia, mercado, discusión y siguientes pasos. La propuesta final será comprobar calidad y utilidad local para decidir qué solución pilotar».

**Transición:** señalar el bloque 1 del índice y abrir el funcionamiento.

## 2. Un asistente para documentar la consulta · 0:55

«Podemos imaginar al escriba como un asistente que toma notas mientras el médico y el paciente conversan. El robot es una metáfora del software. El sistema recoge la conversación y, cuando están disponibles, la historia clínica y las observaciones del profesional.

Con esa información prepara un borrador estructurado. Después el médico revisa los datos, corrige lo necesario y aprueba la nota antes de guardarla en HCIS. Ese es el recorrido que nos interesa: información del encuentro, borrador y revisión. Para valorar un producto tendremos que comprobar cuánto contexto recibe y cuánto trabajo exige cerrar la nota».

**Señalar:** primero la conversación y el asistente de la ilustración; después las tres cajas. Las etapas internas de transcripción, atribución y generación se agrupan para esta audiencia. HCIS puede aportar contexto y recibir la nota aprobada; el acceso depende de la integración.

**Transición:** veamos un ejemplo concreto de qué información entra y cómo aparece en la nota.

**Base:** [NHS England, funciones de entrada y salida](https://www.england.nhs.uk/long-read/guidance-on-the-use-of-ai-enabled-ambient-scribing-products-in-health-and-care-settings/), [Nabla, generación con contexto](https://docs.nabla.com/core-api/reference/2026-04-24/user/generate-note). Ilustración conceptual generada con IA.

## 3. Ejemplo: de tres fuentes a una nota SOAP · 1:00

«Este caso es ficticio y sirve para ver la procedencia de la información. El paciente dice que se encuentra bien y comenta su tensión en casa. En la historia constan hipertensión y losartán; la tensión medida hoy se añade como observación. El médico expresa su valoración y el seguimiento.

La nota SOAP organiza esto en cuatro partes: subjetivo, lo que refiere el paciente; objetivo, lo medido y documentado; valoración; y plan. Fijémonos en que el tratamiento procede de HCIS, mientras que la valoración y el plan proceden de lo que ha dicho el médico. Antes de firmar, hay que confirmar que el tratamiento registrado sigue vigente. Si la historia y la conversación discrepan, esa discrepancia debe resolverse en la revisión».

**Señalar:** las tres entradas y las etiquetas de origen de cada apartado. La tensión domiciliaria es referida; la de consulta es medida. La medicación puede figurar en S u O según la plantilla. El ejemplo no atribuye al escriba la decisión de tratamiento.

**Base:** [estructura SOAP](https://www.ncbi.nlm.nih.gov/books/NBK482263/). El contenido del caso y su representación son propios.

## 4. El beneficio que buscamos: menos carga documental · 1:05

«Buscamos menos teclado, más atención al paciente y menos notas pendientes. Para dimensionar el posible beneficio, pensemos en unas cinco horas menos de documentación al mes por profesional. Es una proyección: supone ocho horas de consulta programada al día, doscientos veinte días de actividad al año y que se mantiene el efecto observado.

La base es un estudio de cinco centros estadounidenses: adoptar el escriba se asoció con dieciséis minutos menos de documentación por cada ocho horas de consulta programada. Hay que contar las horas de agenda, que pueden ocupar solo parte de la jornada. Con seis horas diarias, la proyección sería de unas cuatro horas al mes. Para nuestro servicio usaríamos su actividad real y comprobaríamos qué ahorro deja la revisión».

**Señalar:** los tres objetivos, después la cifra mensual y sus hipótesis. Los iconos son beneficios que evaluar, no tres resultados del mismo estudio. La reducción observada de documentación es 16,0 minutos (IC 95%: 13,7–18,3) por ocho horas de atención programada. También se observan 13,4 minutos menos de uso total del EHR; no se suman a los 16, porque documentación está incluida en el uso EHR. No hubo cambio significativo fuera del horario. [Rotenstein et al., JAMA, 2026](https://jamanetwork.com/journals/jama/fullarticle/2847319).

**Para preguntas:** fórmula mensual `16 min × (horas de consulta al día / 8) × (220 / 12) / 60`. Con ocho horas: 4,89 h/mes; con seis: 3,67 h/mes. Mes medio repartiendo la actividad anual, no mes observado. A ocho horas corresponden 29,33 h en seis meses y 58,67 h/año. Son cálculos propios, no seguimiento longitudinal ni reducción demostrada de jornada. [Hipótesis y escenarios](contexto-investigacion.md).

## 5. Hay que medir hasta que la nota queda cerrada · 0:50

«El trabajo continúa después de generar el borrador. Hay que revisar los hechos, corregir lo necesario y llevar la nota a HCIS. Por eso mediremos todo ese recorrido y lo compararemos con el flujo habitual. Una nota bien redactada puede contener errores o usar antecedentes antiguos como si fueran actuales. Queremos saber cuánto trabajo queda, si la información es correcta y si el proceso completo resulta más útil al profesional.

La comparación debe llegar a la nota cerrada. Si revisar, corregir e incorporar el borrador consume el tiempo que ahorramos al escribir, el beneficio desaparece. En el piloto registraremos tanto las correcciones como el tiempo total, usando la misma definición en el flujo habitual y con el escriba».

**Señalar:** seguir las flechas hasta “nota cerrada” y volver al corchete del tiempo total. [Biro et al., evaluación de errores](https://www.jmir.org/2025/1/e64993/).

## 6. El mercado de escribas crece con rapidez · 0:50

«Menlo estima seiscientos millones de dólares de ingresos en 2025, dos coma cuatro veces el año anterior. Además, PHTI sitúa la adopción de escribas entre las más rápidas de la sanidad reciente, a partir de su trabajo con organizaciones y expertos. Son dos evidencias distintas: crecimiento comercial y expansión en uso. Los escribas ya son una gran categoría de IA clínica, con ofertas que cambian deprisa».

**Señalar:** barra y multiplicador de ingresos; después PHTI. El valor de 2024 es un cálculo propio, `600 / 2,4 = 250`, marcado con asterisco. [Menlo Ventures, 2025](https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare/). La rapidez de adopción es una valoración atribuida a [PHTI, 25/03/2025](https://www.phti.org/announcement/ai-scribes-reduce-clinician-burnout/), sin ranking histórico cuantitativo. Para preguntas: el piloto TPMG/Kaiser registró 3.442 médicos usuarios y 303.266 encuentros en diez semanas ([Tierney et al., 2024](https://doi.org/10.1056/CAT.23.0404); [abstract institucional](https://divisionofresearch.kaiserpermanente.org/research/health-care-delivery-and-policy/health-care-delivery-and-policy-publications/)). El crecimiento de ingresos no mide adopción.

## 7. Muchas ofertas; varias formas de llegar al hospital · 0:25

«El inventario recoge cuarenta y tres soluciones y proyectos. Hay productos individuales, ofertas hospitalarias, soluciones ligadas a la historia clínica y componentes para construir. Quirónsalud es una referencia de proyecto propio implantado en su red; lo separamos de las APIs comerciales. Las familias se solapan y sirven para orientarnos».

**Señalar:** recorrer los bloques sin leer marcas. Una API permite integrar un servicio en otra aplicación. Corti y AWS son ejemplos de esa vía; no hemos acreditado una oferta API comercial de Quirónsalud. El inventario no es un censo. [Proyecto Scribe de Quirónsalud](https://www.quironsalud.com/en/communication/current-events/quironsalud-redisena-modelo-asistencial-reafirmandose-human).

## 8. El encaje que buscamos tiene cuatro piezas · 0:35

«Para nuestro hospital, el encaje requiere cuatro cosas a la vez. Condiciones verificadas de datos y seguridad. Calidad clínica en español, con nuestras especialidades y formas de hablar. Un flujo con HCIS que permita leer contexto y devolver la nota al paciente y episodio correctos. Y viabilidad: coste total, soporte y mantenimiento. Estos criterios nos permiten pasar de una demo atractiva a una evaluación concreta».

**Señalar:** cada pieza antes de apuntar al centro. Precio y seguridad siguen siendo condiciones necesarias; no puntuaciones que ya hayamos cerrado.

## 9. Hay candidatos; el encaje sigue por demostrar · 0:55

«La revisión dejó tres candidatos para seguir comprobando. En Tandem, la ficha de HCIS indica que la integración no está disponible. Invox Genesis ofrece una API, pero falta demostrar el conector HCIS para este flujo. Solventum Align declara integración con historias clínicas, sin que la información revisada confirme el caso concreto de HCIS. Además, tenemos que completar expedientes y presupuestos, y medir calidad clínica local en los tres.

Eso explica la conclusión: todavía no tenemos un candidato con todo el encaje acreditado. Algunas incógnitas pueden resolverse con una demostración o documentación del proveedor».

**Señalar:** los enlaces incompletos y después la banda común. No hay un ranking de calidad ni una prueba funcional realizada. “No confirmado” no significa “imposible”. [Tandem HCIS](https://tandemhealth.ai/es/producto/integraciones/hp-his-hp-hcis), [Invox API](https://developer.invoxmedical.com/), [Align](https://www.solventum.com/es-es/home/health-information-technology/solutions/fluency-align/).

## 10. Dos vías que podemos poner a prueba · 0:45

«Podemos avanzar por dos vías. La primera es evaluar a los proveedores preseleccionados: productos con soporte, cuyas condiciones e integración hay que concretar. La segunda, si contamos con recursos, es construir un prototipo que ejecute y guarde los datos dentro del hospital. Nos daría control de versiones y permitiría repetir muchas pruebas, pero exige desarrollo, infraestructura y mantenimiento.

El prototipo puede empezar como comparador de investigación. Ambas vías deben demostrar calidad y esfuerzo de revisión con criterios equivalentes».

**Señalar:** los dos bloques y su convergencia. La ejecución íntegramente local es un objetivo de arquitectura por comprobar; no una propiedad garantizada por usar código abierto. [Opciones exploratorias ya documentadas](contexto-investigacion.md#una-alternativa-local-como-comparador).

## 11. Los mismos casos permiten una comparación justa · 0:55

«El banco común es una colección de consultas que podemos repetir. Damos a cada solución el mismo audio, el mismo contexto fechado y las mismas observaciones. Después evaluamos sus borradores con los mismos criterios clínicos: qué falta, qué aparece sin respaldo, cómo utilizan la historia y qué habría que corregir.

Así sabemos si las diferencias vienen de la solución y podemos repetir las pruebas cuando cambie una versión. Los procesos automáticos ayudan a ampliar la evaluación; los clínicos revisan muestras y casos relevantes. El resultado sirve para elegir qué pilotar. El ahorro de trabajo real se medirá después en consulta».

**Señalar:** entradas → alternativas → revisión → decisión. Si una solución no admite las mismas entradas, se registra la diferencia y se compara en condiciones compatibles. Una demo elegida por cada proveedor no ofrece esta comparabilidad. [Biro et al.](https://www.jmir.org/2025/1/e64993/), [Zhou et al., listas de evaluación](https://aclanthology.org/2025.emnlp-industry.104/).

## 12. Siguiente paso: comparar antes de pilotar · 0:45

«El siguiente paso se divide en cuatro resultados. Primero, cerrar condiciones de datos, integración y coste con la selección corta. Segundo, preparar casos representativos en español y acordar cómo juzgarlos; podemos comenzar con simulaciones. Tercero, comparar las notas y el esfuerzo de corrección, incluyendo un prototipo local si es viable. Con esos resultados elegiremos qué solución merece un piloto supervisado. Allí mediremos el uso cotidiano, el ahorro neto y los fallos del flujo completo».

**Señalar:** cada hito al nombrarlo; detenerse en la banda inferior. Antes de comparar se fijan criterios de éxito. El paso al piloto depende de los resultados.

## 13. La decisión ahora: iniciar una evaluación local · 0:35

«Propongo iniciar una evaluación local acotada: un servicio, responsables clínico y técnico y recursos definidos. Necesitamos demostrar si las soluciones producen notas fiables, reducen trabajo y se integran en nuestra historia clínica. El entregable será una comparación que permita elegir qué pilotar y con qué condiciones. Esa es la decisión que convierte el interés por la tecnología en evidencia útil para el hospital».

**Cierre:** dejar visible “Elegir qué pilotar con evidencia propia”. Abrir preguntas después de la pausa final.

## Detalles para preguntas

- **Siglas:** HTA = hipertensión arterial; TA = tensión arterial. Se escriben completas en la nueva figura. HCIS es el sistema de información clínica del hospital de Dedalus; HCE = historia clínica electrónica; ASR = reconocimiento automático del habla; mmHg = milímetros de mercurio, unidad de presión. SOAP se explica como subjetivo, objetivo, valoración y plan. «HTCI» no aparece en la fuente de las diapositivas.
- **Seguridad:** la preselección del informe incluye ENS, datos, alojamiento y condiciones contractuales. No se ha realizado una auditoría nueva ni revisado de nuevo cada certificado íntegro. [Investigación comercial](contexto-investigacion.md#encaje-comercial-comprobaciones-selectivas).
- **Precio:** comparar el mismo escenario de usuarios y actividad, incluyendo conector, soporte, infraestructura y mantenimiento. La tarifa individual publicada no representa el coste hospitalario.
- **HCIS:** comprobar por separado lectura de contexto y escritura de nota revisada, paciente/episodio y firma. Una API o una integración HCE genérica no demuestran ese flujo.
- **Evaluación:** separar casos de ajuste y prueba, documentar versiones, incluir casos no señalados en la revisión clínica y resolver discrepancias entre revisores. El banco por sí solo no mide ahorro asistencial.
