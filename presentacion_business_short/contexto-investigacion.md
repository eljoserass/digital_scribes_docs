# Contexto e investigación adicional

Investigación realizada el **07/10/2026** para preparar la versión de diez minutos. Se utiliza el [informe completo](../business_report/main.tex), incluidas sus siete secciones, declaración de uso de IA y seis apéndices, el [guion original](../presentation/guion-presentacion.md) y su presentación. Las fuentes nuevas o comprobadas selectivamente se documentan aquí.

El inventario sigue siendo de **43 entradas de soluciones y proyectos**, con corte inicial del 09/09 y ampliación AWS del 17/09/2026. Esta investigación no vuelve a auditar todos sus certificados, contratos, precios ni conectores. No se han probado productos ni repositorios. Las siguientes conclusiones distinguen evidencia publicada, declaraciones comerciales e interpretación para el proyecto.

## Mercado: por qué ahora

**Actualización visual, 09/10/2026.** Menlo estima **600 millones de dólares en ingresos de escribas ambientales en 2025**, con un multiplicador interanual de **2,4**. La figura propia de la diapositiva 7 compara 2025 con una base 2024 calculada como `600 / 2,4 = 250`, identificada con asterisco. El informe se centra en EE. UU. y combina encuesta a más de 700 directivos, análisis de ingresos y perspectiva inversora; no estima aquí el mercado español. [Menlo Ventures, 2025](https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare/), ya incluido en [las referencias del informe](../business_report/notes/references/2INV3X9M.md).

PHTI describe, a partir de primeros adoptantes, una expansión excepcionalmente rápida y mejoras percibidas de carga documental; también identifica incertidumbre financiera. Es una valoración sectorial, no una medición mundial de cuota ni un récord histórico demostrado. [Comunicado y enlace al informe PHTI, marzo de 2025](https://www.phti.org/announcement/ai-scribes-reduce-clinician-burnout/).

La encuesta AMA de marzo de 2026 recoge 1.692 respuestas, con denominadores distintos por pregunta. En usos, documentación de códigos/historia/notas y resúmenes de historia alcanzan cada uno el 28%; resúmenes de investigación y estándares, el 39%. Son usos autodeclarados estadounidenses, no la tasa de adopción de escribas ambientales. El 81% destacado por AMA agrupa uso o conocimiento, incluida incertidumbre; por eso no se utiliza como cifra de adopción de escribas. [Informe AMA, páginas 2, 5–6 y metodología](https://www.ama-assn.org/sites/ama-assn.org/files/2026-03/physician-ai-sentiment-report_0.pdf).

El registro NHS permanece basado en autocertificación y evidencia aportada por el proveedor; la evaluación y decisión siguen correspondiendo a la organización compradora. Su existencia muestra un mercado organizado, sin sustituir validación local. [Registro NHS](https://digital.nhs.uk/services/ambient-scribing/ambient-voice-technology-self-certified-supplier-registry).

**Decisión editorial:** explicar amplitud de oferta y adopción rápida con fuentes y ámbito explícitos. Los 43 del informe son una muestra propia; no se comparan con otros inventarios para calcular crecimiento. Las categorías de oferta se solapan y no son cuotas de mercado.

## La nota utiliza conversación y contexto

La guía NHS, versión 3 de julio de 2026, incluye como entradas tanto habla como información adicional del usuario o de la historia clínica, y exige revisión de las salidas. Su ámbito es Inglaterra; sus funciones sirven como referencia técnica, sin trasladar sus requisitos nacionales a España. [Guía NHS, §2.2 y §1.4](https://www.england.nhs.uk/long-read/guidance-on-the-use-of-ai-enabled-ambient-scribing-products-in-health-and-care-settings/).

La API de Nabla recibe transcripción y contexto estructurado o libre del paciente y encuentro, además de una base para valoración y plan. Esto confirma que existe soporte explícito para generar notas con contexto; no demuestra que el dato se lea automáticamente de HCIS. [Generate a note, versión de API 2026-04-24](https://docs.nabla.com/core-api/reference/2026-04-24/user/generate-note).

Oracle describe generación de notas en urgencias e ingreso que combina información de su EHR, notas anteriores y conversación actual. Es una declaración de producto para esos entornos en EE. UU.; no acredita un conector Dedalus HCIS ni disponibilidad equivalente en España. [Oracle, 11/03/2026](https://www.oracle.com/news/announcement/health-clinical-ai-agent-helps-emergency-and-inpatient-doctors-2026-03-11/).

Microsoft documenta un flujo que aporta contexto de paciente y episodio antes de la grabación y devuelve transcripciones/notas asíncronamente. Distinguir metadatos de paciente de antecedentes clínicos completos evita asumir que cualquier API recibe toda la historia. [Dragon Copilot APIs para partners, actualizada el 28/09/2026](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/sdk/partner-apis/).

**Interpretación para el proyecto:** el flujo incluye selección del contexto, comprensión, generación, comprobaciones y revisión profesional. Es un modelo conceptual para discutir requisitos: el proveedor puede combinar fases o usar una arquitectura multimodal. La verificación representa una capacidad que comprobar, no una garantía común. Leer datos de HCIS y escribir la nota son dos capacidades que se deben demostrar por separado.

SOAP organiza información subjetiva, objetiva, valoración y plan. El formato permite visualizar distintas procedencias; la ubicación de medicación puede variar. [SOAP Notes, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK482263/). El caso ilustrado es propio y ficticio: sus decisiones están expresadas por el profesional y no constituyen una recomendación clínica.

## Beneficio: evidencia y límites

Rotenstein y colaboradores estudiaron 8.581 clínicos de cinco centros estadounidenses, con 1.809 adoptantes. Hallaron 16 minutos menos de documentación por ocho horas programadas y 0,49 visitas semanales adicionales; sin cambio significativo fuera de horario. Es una cohorte con análisis de diferencias en diferencias: informa asociaciones y variación por uso, no garantiza efecto local. [JAMA, 2026; DOI 10.1001/jama.2026.2253](https://jamanetwork.com/journals/jama/fullarticle/2847319).

El ensayo de UCLA del informe comparó 238 médicos asignados a Nabla, DAX o control. Nabla redujo modestamente el tiempo en notas; DAX no mostró diferencia significativa. Se conserva como apoyo metodológico; no se equipara el DAX estudiado a todo Dragon Copilot actual. [Ficha y material ya revisados en el proyecto](../business_report/notes/references/PR93N8FN.md).

La evidencia española de Quirónsalud permite discutir implantación y experiencia. Su similitud semántica entre borrador y texto editado no mide por sí sola exactitud clínica; sus estudios tienen diseños y muestras distintos. Los usos no se suman como pacientes independientes. [Ficha del estudio ambulatorio](../business_report/notes/references/U5GHQW86.md).

**Decisión editorial:** separar menos trabajo documental, experiencia, calidad y capacidad asistencial. La slide breve usa una sola cifra objetiva reciente, con su unidad y diseño; el proyecto debe medir revisión, corrección y cierre en HCIS.

## Encaje comercial: comprobaciones selectivas

**09/10/2026:** nueva lectura selectiva de las páginas enlazadas de Tandem HCIS, Invox Developers y Align para preparar las tarjetas visuales. Se mantienen los estados descritos debajo. No hay nueva revisión íntegra de certificados ni prueba de integración.

| Candidato o referencia | Comprobación de esta investigación | Consecuencia para la evaluación |
| --- | --- | --- |
| Tandem | La ficha HCIS mantiene integración no disponible. Pro publica 125 €/usuario/mes con facturación anual; la oferta empresarial es personalizada. [HCIS](https://tandemhealth.ai/es/producto/integraciones/hp-his-hp-hcis), [precio](https://tandemhealth.ai/es/producto/precios). | Completar el expediente ENS del informe y exigir demostración del flujo HCIS y presupuesto total. |
| Invox Genesis | El portal técnico publica APIs y una integración SOFT para abrir Genesis desde la HCE y devolver resultados; anuncia versión 2026-10-01. [Portal](https://developer.invoxmedical.com/), [integración SOFT](https://developer.invoxmedical.com/soft-integration/docs/open-genesis). | Existe una vía técnica de integración. No acredita un conector HCIS desplegado; el certificado y alcance Genesis siguen pendientes. |
| Solventum Align | La página española declara integración HCE genérica, ENS ALTA y nube UE; no nombra HCIS en el contenido revisado. [Producto](https://www.solventum.com/es-es/home/health-information-technology/solutions/fluency-align/). | Pedir certificado, cadena de datos, conector HCIS y propuesta comercial específica. |
| Nunsys / Dedalus / Vekai | El anuncio integra Vekai dentro de Dedalus Care HCIS, sin describir el flujo ambiental completo de captura de consulta y generación de nota. [Anuncio](https://www.nunsys.com/nunsys-group-y-dedalus-se-alian-para-impulsar-desde-la-comunitat-un-nuevo-modelo-de-historia-clinica-digital/). | Referencia para preguntar a Dedalus por capacidades y hoja de ruta. No se convierte en un cuarto candidato ambiental validado. |

El acceso directo a la ficha Invox Dictation–HCIS volvió a fallar; su declaración se conserva como evidencia del corte anterior, sin afirmar una nueva verificación funcional. No se han vuelto a examinar certificados íntegros ni expedientes privados. [Tabla HCIS original](../business_report/appendices/03_hcis.tex), [certificaciones originales](../business_report/appendices/01_certificaciones.tex).

**Interpretación:** «ningún candidato tiene todo el encaje acreditado» significa que faltan pruebas conjuntas para esta preselección y este hospital. La evidencia pública incompleta no demuestra imposibilidad técnica ni excluye otras ofertas. El precio funciona como criterio de viabilidad y coste total; no se afirma que haya sido cerrado como filtro cuantitativo previo.

## Calidad y evaluación a mayor escala

Biro y colaboradores evaluaron dos productos con encuentros simulados: 31 de 44 borradores contenían errores y predominaban omisiones. Es una muestra pequeña en condiciones controladas, no una tasa general del mercado ni del producto actual. Su procedimiento de clasificación y revisión independiente orienta los criterios locales. [JMIR, 2025; DOI 10.2196/64993](https://www.jmir.org/2025/1/e64993/).

Zhou y colaboradores convierten feedback clínico en listas de comprobación y estudian evaluadores automáticos con más de 21.000 encuentros desidentificados. Ofrecen una vía de evaluación repetible, pero el trabajo se vincula a un sistema desplegado y no acredita un evaluador universal para español ni ausencia de errores. [EMNLP Industry, 2025](https://aclanthology.org/2025.emnlp-industry.104/).

**Propuesta propia a partir de esos métodos y del apéndice F:** un banco común con audio, contexto fechado y observaciones; casos separados para ajuste y evaluación; notas de referencia y juicio clínico. Registrar producto, versión, plantilla, entradas y resultados. Comparar negaciones, hablantes, omisiones, adiciones, medicación/dosis y utilización de contexto antiguo o contradictorio.

La escala se obtiene automatizando ejecuciones y comprobaciones, manteniendo revisión clínica de una muestra representativa y de los casos señalados. Esa muestra debe incluir casos no señalados para detectar puntos ciegos. La identidad del candidato puede ocultarse a los revisores cuando sea viable. La revisión del borrador y la nota final deben distinguirse. Medir ahorro exige además observar el flujo asistencial con comparador adecuado; el banco por sí solo no lo estima.

Tamaño, cobertura de especialidades, precisión deseada, dos revisores/adjudicación y criterios de aceptación deben concretarse antes del piloto. El protocolo puede partir de [las opciones existentes](../business_report/notes/opciones-evaluacion-piloto.md), sin fijar ahora una muestra arbitraria.

## Una alternativa local como comparador

OpenScribe declara un modo web mixto con ASR local y generación externa, y una ruta de escritorio con inferencia local. Su configuración predeterminada de ASR usa un modelo de inglés; trabajar en español exige modificar y validar la configuración. No se ha comprobado su ejecución ni su integración con HCIS. [README OpenScribe](https://github.com/sammargolis/OpenScribe).

Phlox se presenta como proyecto local, pero advierte de su carácter experimental y de que la entrega no es apta para producción. Esa declaración limita su uso como referencia exploratoria. [README Phlox](https://github.com/bloodworks-io/phlox).

**Propuesta de alcance:** estudiar un prototipo con ASR, generación, almacenamiento y comprobaciones locales, inicialmente con casos simulados y sin escritura asistencial. Evaluar calidad en español, latencia, capacidad por lotes, infraestructura y tiempo de desarrollo/mantenimiento. Confirmar dependencias y llamadas externas; una interfaz alojada localmente no basta para considerar local toda la cadena. El flujo hacia HCIS requerirá desarrollo y pruebas propios.

El posible beneficio es controlar datos y versiones y repetir pruebas a mayor escala, sujeto a capacidad y recursos. Comprar y construir comparten la necesidad de seguridad, calidad, soporte e integración. [Consideraciones técnicas del informe](../business_report/appendices/05_construir.tex).

## Datos, seguridad y siguientes hitos

Mantener como dimensiones separadas protección de datos, seguridad del sistema, calidad clínica y coste. Para el proyecto: revisar procesamiento/almacenamiento, retención, subencargados, accesos y reutilización; verificar certificado, sistema y alcance ENS aplicable. ENS ALTA sigue siendo una prioridad propuesta del informe, pendiente de decisión institucional. [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [ENS, texto consolidado](https://www.boe.es/eli/es/rd/2022/05/03/311/con).

La comparación comercial necesita el mismo escenario de usuarios, actividad y duración, con licencias/consumo, conector, mantenimiento, equipos, formación y soporte. La tarifa Pro no estima la implantación hospitalaria. [Apéndice de precios](../business_report/appendices/04_precios.tex).

El próximo hito debe producir requisitos y presupuestos comparables, demostración HCIS, banco de casos y resultados de calidad/esfuerzo de corrección. Después se puede concretar un piloto asistencial con responsables, recursos y criterios de continuidad. Las propuestas no implican contratación ni que se haya ejecutado un piloto.

## Alcance de las fuentes y edición

Se priorizaron artículos originales, documentación oficial de productos, repositorios de sus autores y fuentes institucionales. Las declaraciones del proveedor se identifican como tales. Cuando una página no pudo abrirse, no se presenta como examinada íntegramente: el informe PHTI se contextualiza mediante su comunicado oficial y la revisión previa del proyecto; UCLA mediante su ficha local. La búsqueda es selectiva y no una revisión sistemática exhaustiva.

Codex y ChatGPT apoyaron la búsqueda, síntesis, redacción y construcción de diagramas. La selección final y la responsabilidad del material corresponden al autor; su revisión humana final sigue pendiente.


## Correcciones y ampliación de negocio — 09/10/2026

**Quirónsalud.** Se retira de «APIs para construir». Su [anuncio de Scribe](https://www.quironsalud.com/en/communication/current-events/quironsalud-redisena-modelo-asistencial-reafirmandose-human) describe un proyecto implantado en su red; las fuentes revisadas no acreditan una API comercial para terceros. Se conserva como referencia de implantación propia. El inventario incluye proyectos, no solo proveedores comerciales.

**Unidad del efecto.** [Rotenstein et al., JAMA](https://jamanetwork.com/journals/jama/fullarticle/2847319) normaliza las medidas por ocho horas de atención a pacientes programada (`scheduled patient hours`). Pueden ocupar solo parte de una jornada. La diferencia en documentación es 16,0 minutos (IC 95% 13,7–18,3); en uso total del EHR, 13,4 minutos. No se suman: documentación está incluida en la actividad EHR. No hubo cambio significativo fuera del horario; no se interpreta como reducción de jornada.

**Proyección ilustrativa por profesional.** Suponer efecto constante y 220 días activos/año. Fórmula: `16 min × horas de consulta/8 × días / 60`. Mes y semestre reparten un doceavo y la mitad de la actividad anual.

| Consulta programada/día | Mes medio | 6 meses | Año (220 días) |
| --- | ---: | ---: | ---: |
| 4 h | 2,44 h | 14,67 h | 29,33 h |
| 6 h | 3,67 h | 22,00 h | 44,00 h |
| 8 h | 4,89 h | 29,33 h | 58,67 h |

La diapositiva de beneficios integra la proyección mensual redondeada a **≈5 h/mes** junto a sus hipótesis y al efecto base de 16 minutos; se elimina la diapositiva independiente de ahorro acumulado. Los escenarios de seis meses y un año quedan en estas notas para preguntas. Son cálculos propios de tiempo de documentación, no resultados longitudinales observados ni reducción garantizada de jornada. Para el piloto, sustituir las hipótesis por horas programadas y días del servicio.

**Adopción.** El [comunicado PHTI de 25/03/2025](https://www.phti.org/announcement/ai-scribes-reduce-clinician-burnout/) describe a los escribas como encaminados a una de las adopciones más rápidas de la historia sanitaria reciente. Es una valoración de entrevistas y expertos, no una clasificación cuantitativa contra todas las tecnologías médicas. Se atribuye a PHTI en la diapositiva 6; el ×2,4 de Menlo se etiqueta como crecimiento de ingresos. Para preguntas: [Tierney et al., NEJM Catalyst 2024](https://doi.org/10.1056/CAT.23.0404) registró 3.442 médicos y 303.266 encuentros en diez semanas de implantación en TPMG/Kaiser; [abstract institucional](https://divisionofresearch.kaiserpermanente.org/research/health-care-delivery-and-policy/health-care-delivery-and-policy-publications/). Son médicos que lo utilizaron, no necesariamente usuarios diarios. El DOI directo respondió 403; se examinó el abstract institucional.

**Lenguaje del ejemplo.** «HTA» y «TA» se sustituyen por hipertensión y tensión. HCIS se explica al inicio como el sistema de historia clínica del hospital y la entrada del ejemplo se llama «Historia clínica registrada». Se conserva el significado del caso ficticio y las decisiones expresadas por el médico.
