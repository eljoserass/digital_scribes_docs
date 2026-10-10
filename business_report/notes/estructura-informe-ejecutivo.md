# Propuesta de informe ejecutivo: escriba ambiental para un hospital con HCIS

**Enfoque propuesto · 10/09/2026.** Destinatario: dirección de innovación, con apoyo de clínica, sistemas y seguridad. Extensión orientativa: **6–8 páginas de cuerpo**, con fichas y detalle técnico en anexos. Este documento organiza el informe; no sustituye a la revisión de artículos y notas de Zotero pendiente.

**Pregunta que debe resolver:** ¿merece la pena preparar un piloto de documentación clínica ambiental en este hospital, qué candidatos permiten hacerlo y qué falta demostrar?

El alcance principal es **audio en español → borrador de nota clínica → revisión y aprobación profesional → registro en Dedalus HCIS**. La selección no presupone que algún producto cumpla ya todos los requisitos. Punto de partida documental: [análisis provisional](analisis-escribas-digitales.md).

## Estructura del cuerpo

| Apartado | Qué debe contar | Resultado para el lector |
| --- | --- | --- |
| **1. Resumen ejecutivo** · ½ página | Oportunidad, conclusión provisional, principal impedimento y siguiente decisión. Se escribe al final, se lee primero. | Entender qué se propone autorizar: exploración, comprobación técnica o piloto; no confundirlo con compra. |
| **2. Por qué considerarlo y para qué** · ¾ página | Carga de documentación y beneficios observados/prometidos: tiempo, experiencia profesional y atención al paciente. Introducir incertidumbres junto a los beneficios. Acotar servicio y tarea inicial. | Entender el problema que se quiere resolver, sin necesitar una historia completa del mercado. |
| **3. Qué se implantaría** · ¾ página | Una definición breve y un esquema de entrada/salida. Captura por móvil, web o dispositivo; generación; revisión; incorporación a HCIS. Distinguir dictado, escriba ambiental y funciones adicionales. | Visualizar el cambio en una consulta y las tareas que conserva el profesional. |
| **4. Cómo decidimos si encaja** · 1 página | Requisitos de entrada y criterios de evaluación: HCIS, ENS, datos, español, calidad, operación y coste. Explicar qué cuenta como evidencia y cómo se trata lo desconocido. | Poder interpretar la comparación y sus límites. |
| **5. Opciones y selección corta** · 1½–2 páginas | Comparar 3–5 candidatos con la misma tabla. Explicar por qué entran y por qué no pasan todavía. Incluir referencias de hospitales y socios solo cuando resuelvan una cuestión concreta. | Saber a quién comprobar primero y qué pedirle. |
| **6. Lecciones de despliegues y propuesta de piloto** · 1–1½ páginas | Qué beneficios se han medido, qué fallos o fricciones aparecieron y cómo comprobarlos aquí. Conectar cada lección con una decisión de evaluación o implantación. | Entender cómo comprobar utilidad y seguridad antes de escalar. |
| **7. Decisión solicitada** · ½ página | Acción recomendada, responsables, información pendiente y condiciones de avance/parada. Presupuesto solo cuando haya propuesta comparable. | Terminar con una decisión concreta y revisable. |

La motivación, definición y adopción caben juntas al inicio: no necesitan tres capítulos. Los estudios sustentan beneficios y lecciones; evitar resumirlos dos veces. El resumen ejecutivo debe poder leerse sin los anexos.

## Qué significa «bueno» en este informe

Conviene separar tres preguntas. **¿Podemos usarlo aquí?** requiere alcance contractual, datos, ENS e integración. **¿Hace bien la tarea?** requiere evaluar la nota en español. **¿Mejora el trabajo?** requiere medir el proceso completo, incluida la revisión y el guardado. Un resultado favorable en una pregunta no responde las otras.

| Dimensión | Qué comprobar | Qué no tomar como sustituto |
| --- | --- | --- |
| **Calidad clínica en español** | Omisiones e invenciones, negaciones, fármacos/dosis, atribución de hablantes, correcciones y relevancia clínica; audio y nota de salida en español. Acentos y especialidades pertinentes para el hospital. | «Soporta español», una tasa de acierto de transcripción o un estudio exclusivamente en inglés. |
| **Utilidad operativa** | Tiempo total hasta dejar la nota aprobada en HCIS; trabajo fuera de horario, uso sostenido y experiencia de profesionales/pacientes. | Tiempo de generación aislado, volumen de notas o satisfacción como prueba de exactitud. |
| **Seguridad y datos** | Certificado, emisor, alcance y vigencia; países de tratamiento, subencargados, retención, reutilización y compromisos del contrato. | Logotipos, una política genérica o asumir que almacenamiento UE significa todo el procesamiento UE. |
| **Integración y operación** | Versión de HCIS, identificación del paciente/episodio, transferencia aprobada, trazabilidad y gestión de errores. Dispositivo, red, autenticación y soporte necesarios. | Una alianza con Dedalus, API/HL7/FHIR genéricos o el funcionamiento de otro producto del mismo fabricante. |
| **Coste** | Unidad facturable, límites, compromiso, extras y coste total de implantación/operación para el mismo escenario. | Comparar una API por minuto con una licencia clínica completa, o anualidad con mensualidad cancelable. |

Estos son criterios propuestos, no resultados ya medidos. Su aplicación documental está en el [análisis](analisis-escribas-digitales.md), con los [estudios y certificados](certificaciones-escribas-digitales.md), [integraciones](integraciones-hcis.md) y [precios](precios-escribas-digitales.md) de apoyo.

**Ausencia de una métrica:** reduce lo que podemos concluir y obliga a verificar; no demuestra que el producto funcione mal. **Peer review:** informa sobre revisión científica, pero no garantiza independencia, buen diseño o aplicabilidad al hospital. Para cada estudio anotar producto/versión, escenario, idioma, tamaño, resultado y limitación principal. Evitar un porcentaje único de «performance» que mezcle tareas distintas.

## Cómo presentar proveedores y estudios

Para dirección usar una tabla breve: **candidato · HCIS y vía · ENS y prueba documental · datos · evaluación en español · coste/cobro · condición pendiente**. Cada celda debe remitir a su fuente o ficha. Usar «confirmado documentalmente», «declarado», «no localizado» y «no disponible»; reservar «probado» para una prueba efectivamente realizada.

La selección corta se justifica por ajuste al problema, no por popularidad o cantidad de publicaciones. Los 42 proveedores quedan en anexos. Las alianzas y clientes se incorporan a la columna pertinente: un hospital español puede aportar una referencia de uso; un integrador puede aportar capacidad técnica. Ninguno demuestra por sí solo validación clínica o un conector HCIS operativo. [Revisión de HCIS y límites](integraciones-hcis.md).

Para las lecciones, usar **hallazgo → limitación → implicación para nuestro piloto**. Por ejemplo, el ensayo de Nabla/DAX mide resultados de documentación; el estudio de Heidi también registra errores; Quirón aporta experiencia de despliegue español a escala. Sirven para preguntas distintas y no permiten ordenar proveedores por porcentajes directamente. [Nabla/DAX](https://doi.org/10.1056/AIoa2501000), [Heidi](https://doi.org/10.1016/j.arth.2026.03.069), [Quirón](https://doi.org/10.1016/j.ijmedinf.2026.106584).

## Qué dejar fuera del cuerpo principal

- **Código abierto y desarrollo propio:** anexo «comprar o construir», con alcance, esfuerzo y responsabilidades. Distinguir una aplicación completa de componentes para montarla. No hay todavía una revisión suficiente para afirmar aquí que exista —o no exista— un sustituto abierto adecuado.
- **Arquitectura y componentes:** transcripción, generación, modelos, datasets y métricas por etapa, cuando ayuden a evaluar una alternativa técnica. El cuerpo solo necesita explicar las fronteras de datos y el trabajo del usuario.
- **Codificación y otras funciones:** tabla opcional, separada de la tarea principal. Plantillas sí entran cuando afectan a la nota que debe recibir HCIS; codificación automática requiere evaluación propia si se incorpora.
- **Inventario completo:** conservar los documentos de certificaciones, integración y precios como anexos vivos, sin duplicarlos en el informe.

## Ajustes al borrador actual

[hello.tex](latex/hello.tex) ya plantea la tensión útil entre beneficios y corrección de errores. Para convertirlo en introducción ejecutiva:

- Sustituir provisionalmente «aplicación dominante» y «adopción más rápida de la historia» por una formulación prudente, hasta tener fuentes y ámbito definidos.
- No generalizar «la mitad del tiempo» sin concretar población, actividad y estudio.
- Tratar posible inhibición del paciente y «deuda cognitiva» como preguntas pendientes de evidencia; no como efectos demostrados.
- Formular la motivación como **comprobar si reduce la carga documental manteniendo calidad y viabilidad local**, sin dar el beneficio por conseguido.

El siguiente trabajo editorial sería redactar resumen, alcance y criterios con esta estructura; después incorporar Zotero para afinar las afirmaciones y las lecciones de implantación. No hace falta esperar a una revisión exhaustiva de arquitectura para producir ese primer informe.
