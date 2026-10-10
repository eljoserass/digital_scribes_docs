# Escribas digitales: decisión para un hospital con HCIS

Preparado: **10/09/2026**. Corte de evidencia pública: **09/09/2026**. Base inicial: 42 proveedores de [certificaciones y estudios](certificaciones-escribas-digitales.md), [integraciones HCIS](integraciones-hcis.md) y [precios](precios-escribas-digitales.md). Es una comparación documental, no una evaluación de productos en el hospital.

**Actualización de literatura, 11/09/2026:** la [revisión de Zotero](README.md) añade un estudio ambulatorio de Quirónsalud con más de 2,33 millones de usos. Refuerza la evidencia de despliegue español, pero su similitud semántica no demuestra exactitud clínica y no observa menor duración global de consulta. No cambia la falta de confirmación conjunta de HCIS ambiental y ENS ALTA. [Métodos y resultados](https://doi.org/10.3389/fdgth.2026.1874919).

**Resultado:** con **ENS ALTA e integración ambiental operativa con Dedalus HCIS como requisitos obligatorios**, no hay un ganador confirmado con la evidencia revisada. **Tandem encabeza la selección documental condicionada**; **Invox es la pista más concreta para HCIS, pero lo publicado corresponde a dictado**. Esto orienta la siguiente comprobación, no una adjudicación. Fuentes y condiciones en la tabla siguiente.

**Ampliación de mercado, 17/09/2026:** AWS HealthScribe eleva el inventario a **43 proveedores**. Transcribe figura en el alcance ENS ALTA publicado por AWS; la cobertura de HealthScribe se infiere de su regla de funciones, pendiente del certificado completo. No modifica la selección corta: la guía limita el servicio a inglés de EE. UU. y Virginia, sin conector HCIS identificado. [Alcance ENS](https://aws.amazon.com/compliance/services-in-scope/ENS-High/), [guía técnica](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html), [expediente y partners](additional/aws-healthscribe.md).

## Metodología

La tarea comparada es **conversación en español → borrador de nota → revisión profesional → incorporación al episodio correcto en HCIS**. Codificación, recomendaciones clínicas y otras funciones se consideran aparte. Una API o un dictador no equivalen por sí solos a ese flujo completo.

1. **Primero, requisitos que no se compensan entre sí.** ENS ALTA del sistema contratado e integración HCIS del producto ambiental. Distingo disponible, declarado, pendiente y no localizado. Una página comercial no demuestra que funcione en nuestra instalación; un certificado de la nube tampoco certifica automáticamente al escriba.
2. **Después, suficiencia de la evidencia.** Para certificados: documento, entidad, emisor, alcance, vigencia y salvedades. Para datos: países de almacenamiento **y procesamiento**, subencargados, retención, entrenamiento y contrato. Para calidad: producto/versión, idioma, contexto, muestra, comparación, errores clínicos y resultados operativos.
3. **Finalmente, coste y viabilidad.** Comparar propuestas para el mismo volumen, incluyendo conector y mantenimiento. Valorar por separado precio y transparencia del cobro. Priorizar pilotos que puedan resolver las incertidumbres decisivas.

No sumo insignias ni asigno una nota numérica: no hay medidas homogéneas para justificarla. ISO 14001 no mejora por sí misma la calidad clínica; publicar errores no resta transparencia. **No localizado significa incertidumbre documental, no mala calidad demostrada.** Peer review, independencia del proveedor y relevancia para español son propiedades distintas. Definiciones y documentos: [glosario y fichas](certificaciones-escribas-digitales.md).

## Los dos requisitos decisivos

| Candidato | ENS ALTA | HCIS para el escriba ambiental | Resultado provisional |
| --- | --- | --- | --- |
| **Tandem** | Certificado de Bureau Veritas revisado; copia pública de **una de dos páginas**, alcance completo por cerrar. | El proveedor dice **no disponible**. | Mejor punto de partida documental; no cumple todavía la condición HCIS. [Expediente](https://trust.tandemhealth.ai/), [HCIS](https://tandemhealth.ai/es/producto/integraciones/hp-his-hp-hcis). |
| **Invox Genesis** | Obtención anunciada; certificado íntegro, emisor, vigencia y alcance Genesis no verificados. | **Dictation sí lo anuncia; Genesis no confirmado.** | Prioridad para aclarar ambos extremos, sin convertir el dictado en prueba del escriba. [ENS](https://www.invoxmedical.com/blog/invox-medical-refuerza-su-compromiso-con-la-seguridad-de-la-informacion-con-la-obtencion-de-la-certificacion-iso-27001-y-el-ens-nivel-alto), [Dictation–HCIS](https://dictation.invoxmedical.com/software-medico/dedalus-hcis/). |
| **Solventum Align** | Cumplimiento ALTA anunciado; certificado no inspeccionado. | No localizado para Align. | Tercera vía de comprobación; todavía sin documentación suficiente para pasar ambos requisitos. [Producto y ENS](https://www.solventum.com/es-es/home/health-information-technology/solutions/fluency-align/). |
| **Otros 39 del corte inicial** | No localicé ENS ALTA propio con alcance verificado para estos productos. | No confirmé integración ambiental disponible. | Ninguno queda habilitado documentalmente bajo ambos requisitos. El detalle y las páginas consultadas permanecen en las [fichas del inventario](certificaciones-escribas-digitales.md) y la [tabla HCIS](integraciones-hcis.md). |

ENS ALTA se trata aquí como **requisito de esta selección**, no como afirmación de que sea obligatorio para cualquier escriba. Tampoco se descarta que un proveedor aporte mañana el documento o conector que hoy falta.

## Qué candidatos destacan y por qué

Selección explicativa, no clasificación exhaustiva: los tres anteriores por ENS/HCIS; Heidi por evidencia específica en español; Nabla por ensayo comparativo; Tortus por documentación sanitaria; Corti por la alternativa de construir. Los 42 iniciales y AWS siguen incluidos en los inventarios.

| Candidato | Certificaciones y datos: evidencia útil | Limitación que pesa en la decisión |
| --- | --- | --- |
| **Tandem** | PDFs de seguridad, gestión de IA y producto sanitario; regiones y subencargados publicados. | El dictamen C5 tiene **salvedades**; hay que revisar su resolución. No basta contar certificados. [Documentos y límites](certificaciones-escribas-digitales.md#5-tandem-health). |
| **Invox** | Anuncios ISO/ENS y adopción española identificada. | Menor verificabilidad pública de certificados y cadena de tratamiento de Genesis. Precio no localizado. [Ficha](certificaciones-escribas-digitales.md#2-invox-medical--invox-genesis--vócali), [precio](precios-escribas-digitales.md). |
| **Solventum** | Declara almacenamiento y procesamiento UE. | Expediente de Align, retención y subencargados incompletos en lo público. No trasladar estudios de Fluency Direct. [Ficha](certificaciones-escribas-digitales.md#4-solventum--fluency-align). |
| **Heidi** | ISO 27001 y otras credenciales con documentos revisados; condiciones UE y subencargados publicados. | ISO 42001 no inspeccionada; Remote añade almacenamiento local hasta sincronización. ENS/HCIS pendientes. [Documentos y datos](certificaciones-escribas-digitales.md#3-heidi--scribe-y-remote). |
| **Nabla** | DPA público con región y reutilización condicionada; ensayo aleatorizado. | Informes de certificación bajo solicitud; evidencia del ensayo en inglés. [Ficha](certificaciones-escribas-digitales.md#7-nabla). |
| **Tortus** | Certificados 27001/13485 revisados y estudio de seguridad en simulación. | Infraestructura UK: no demuestra residencia íntegra UE. UKCA IIa anunciado, certificado no inspeccionado; no validación española localizada. [Ficha](certificaciones-escribas-digitales.md#15-tortus). |
| **Corti** | DPA y mecanismo de entrenamiento por autorización expresa; consumo API publicado. | Añade desarrollo y operación propios. Certificaciones de componentes no se trasladan automáticamente a nuestra aplicación. [Ficha](certificaciones-escribas-digitales.md#13-corti--plataformaapi-y-assistant-md), [API y precios](https://corti.ai/pricing). |

## Español y calidad: qué sabemos realmente

| Evidencia localizada | Qué aporta | Qué no permite concluir |
| --- | --- | --- |
| **Heidi: simulación multinacional con centro de Barcelona**, preprint de agosto de 2026. | Comparación directa de notas que incluye español; candidato útil para una prueba local. | No es revisión por pares ni despliegue real; financiación del proveedor. Las cifras agregadas no son rendimiento exclusivo del español. [Estudio](https://www.medrxiv.org/content/10.64898/2026.08.18.26360701v1). |
| **Quirónsalud: 48 hospitales españoles**, estudio observacional revisado por pares. | Referencia particularmente pertinente de implantación a escala en España. | El resumen no desglosa calidad por idioma; no demuestra causalidad ni oferta comercial para terceros. [Artículo](https://doi.org/10.1016/j.ijmedinf.2026.106584). |
| **Invox Genesis en Alcorcón**, confirmado por Comunidad de Madrid. | Uso real en un entorno hospitalario español. | No aporta comparación clínica publicada, tasa de errores ni prueba de integración Genesis–HCIS. [Hospital](https://www.comunidad.madrid/noticias/2025/06/10/hospital-publico-fundacion-alcorcon-incorpora-aplicacion-ia-optimizar-generacion-documentacion-clinica-partir-entrevistas). |
| **Tandem: estudio sueco** y caso comercial de Recoletas. | Evidencia operativa y referencia española, respectivamente. | El estudio sueco no valida español; el caso comercial no sustituye a una evaluación controlada. [Estudio](https://doi.org/10.2196/90052), [Recoletas](https://tandemhealth.ai/product/customer-stories/recoletas-salud). |
| **Nabla/DAX: ensayo aleatorizado, 238 médicos**. | Mejor apoyo causal para resultados de documentación que una encuesta antes/después; efecto modesto de Nabla. | Consultas en inglés; DAX tampoco equivale a toda la versión actual de Dragon. [Ensayo](https://doi.org/10.1056/AIoa2501000). |

No hay comparación directa suficiente para afirmar quién genera **las mejores notas clínicas en español**. Abridge y Ambience aportan estudios relevantes de carga e implementación; eso no demuestra rendimiento español ni compatibilidad HCIS. [Abridge](https://jamanetwork.com/jamanetworkopen/fullarticle/2839542), [Ambience](https://www.nature.com/articles/s44401-026-00144-6). El ensayo de Heidi y la evaluación de Suki también documentan errores: beneficios operativos y fallos clínicos pueden coexistir. No deben compararse sus porcentajes como si usaran el mismo protocolo. [Heidi](https://doi.org/10.1016/j.arth.2026.03.069), [Suki](https://doi.org/10.3389/frai.2025.1691499).

## Precio y elección por escenario

Tandem Pro publica **125 €/usuario/mes con anualidad**, pero la integración corresponde a una propuesta Enterprise. Noa publica **30 €/mes + IVA en España**, sin resolver por ello el coste HCIS. Invox y Align no aportan una tarifa pública cuantificable en lo revisado. No hay ganador defendible en **coste total hospitalario**. [Tandem](https://tandemhealth.ai/es/producto/precios), [Noa](https://noa.ai/es-es/precio), [comparación de cobro de los 43](precios-escribas-digitales.md).

| Escenario | Recomendación propia |
| --- | --- |
| **ENS ALTA + HCIS ambiental ya operativo** | Ningún ganador confirmado. Solicitar prueba documental y demostración antes de seleccionar. |
| **ENS ALTA, aceptando desarrollar HCIS** | **Tandem primero para evaluación**, condicionado al certificado completo, salvedades, contrato, conector y calidad española. |
| **Se acepta dictado como solución intermedia** | **Invox primero para comprobar compatibilidad**, cerrando ENS y alcance contractual. Resuelve una tarea más limitada. |
| **Se relajan temporalmente ambos requisitos para estudiar calidad** | Incluir **Heidi como comparador en español**; usar estudios de otros proveedores para diseñar la evaluación, sin declarar un ganador clínico. |
| **Se contempla desarrollo propio** | Evaluar API/componentes como proyecto distinto, con coste y responsabilidades propios. Corti es una vía documentada; aquí no se ha comparado exhaustivamente código abierto. |

**Siguiente paso recomendado:** comprobación paralela de Tandem, Invox y Align, seguida de piloto solo con candidatos que superen los requisitos acordados. Pedir certificado y anexos, mapa contractual de datos, propuesta económica y demostración en la versión de HCIS del hospital. En el piloto, medir notas y revisión en español, omisiones/errores clínicos, tiempo total hasta guardar en HCIS y experiencia profesional/paciente. Fijar umbrales y criterio de parada antes de observar resultados; este documento no presupone que el piloto vaya a salir favorable.
