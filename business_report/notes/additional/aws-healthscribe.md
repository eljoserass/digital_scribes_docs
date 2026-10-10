# AWS HealthScribe: revisión de producto y ecosistema

Consulta: **17/09/2026**. Ampliación puntual del inventario; no actualiza las otras 42 fichas. Fuentes oficiales de AWS y de los partners, sin acceso a AWS Artifact, contratos privados ni pruebas del servicio.

## Aportación al informe

Proveedor **43**, incorporado a los apéndices de certificaciones, catálogo, HCIS y precios. Ilustra una API comercial para construir un escriba, con documentación de aseguramiento y facturación pública. La selección corta permanece igual: la guía limita HealthScribe a `en-US` y `us-east-1`, y no se identifica conector Dedalus HCIS. [Guía](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html).

## Partners: quién ofrece qué

AWS publica estas cinco relaciones; aparecer como cliente o colaborador no acredita reventa, disponibilidad en España o certificación de un producto final. [Directorio de clientes](https://aws.amazon.com/healthscribe/customers/).

| Empresa | Evidencia comercial revisada | Interpretación |
| --- | --- | --- |
| **3M HIS / Solventum** | AWS recoge una colaboración; [Fluency Align](https://www.solventum.com/en-us/home/health-information-technology/solutions/fluency-align/) es un producto comercial. | No se identifica documentación que vincule específicamente **Align España** con HealthScribe. No trasladar sus límites regionales o certificaciones a Align. Solventum ya tiene ficha propia. |
| **Netsmart** | [AWS, 17/02/2025](https://aws.amazon.com/blogs/industries/netsmart-transforms-behavioral-healthcare-with-new-feature-of-aws-healthscribe/) describe Bells Virtual Scribe y su uso de HealthScribe para documentación de salud conductual; [producto comercial Bells](https://www.ntst.com/carefabric/careguidance-solutions/ai-documentation-assistant). | **Aplicación basada en HealthScribe identificada**, con plantilla GIRPP. La integración genérica con EHR anunciada no demuestra compatibilidad HCIS. |
| **ScribeEMR / ScribeRyte AI** | El directorio AWS anuncia integración de HealthScribe; [ScribeRyte](https://scriberyte.ai/) presenta una aplicación comercial y comunica el cambio de ScribeEMR a Nivaran. | Existe oferta terminada. La referencia de AWS no verifica por sí sola el backend de cada versión o contrato actual. No confundir con Scribeberry. |
| **TeleTracking** | AWS describe trabajo para incorporarlo a Healthcare Operations Cloud; [sitio corporativo](https://www.teletracking.com/) consultado. | Colaboración anunciada; sin escriba autónomo comercial basado en HealthScribe identificado en estas fuentes. |
| **Pariveda** | [Artículo de la consultora, 20/02/2025](https://parivedasolutions.com/perspectives/how-to-maximize-the-impact-of-ai-scribes-for-better-patient-care/), además del directorio AWS. | Vía de consultoría y desarrollo. No se identifica una licencia de escriba lista para implantación hospitalaria. |

Los cinco se documentan como ecosistema de AWS, sin contarlos como cinco nuevas fichas completamente auditadas. Una eventual compra a un partner exigiría su propio expediente de seguridad, datos, precio y conectores.

## Evidencia clínica y discrepancias documentales

La [AI Service Card](https://docs.aws.amazon.com/ai/responsible-ai/aws-healthscribe/overview.html) delimita su versión a noviembre de 2023. Su evaluación es del fabricante y guionizada; no se identifica tamaño muestral ni dataset descargable para reproducirla. Las métricas se transcriben en la ficha 43, evitando equipararlas a exactitud clínica. Puede aportar ideas para evaluar completitud, fidelidad y revisión de notas, pero no valida español.

Búsqueda pública dirigida: `"AWS HealthScribe" evaluation clinical study`, `"AWS HealthScribe" peer reviewed evaluation clinical notes study` y `"AWS HealthScribe" "HCIS"`. No se localizó un estudio clínico revisado por pares que evaluase específicamente este servicio ni una integración HCIS. Las menciones en revisiones y los casos comerciales no se trataron como validación independiente. No es una búsqueda sistemática exhaustiva.

Las [FAQ](https://aws.amazon.com/healthscribe/faqs/) y la Service Card conservan descripciones por lotes y especialidades limitadas; la [guía actual](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html) ya incluye streaming y más especialidades. Se prioriza la guía para disponibilidad y se conserva la fecha de versión de la evaluación. La guía enlaza Amazon Connect Health Ambient como oferta adicional; no se transfieren sus prestaciones a HealthScribe.

[Transcribe Medical](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-medical.html) es reconocimiento de voz médica por lotes o streaming, en inglés de EE. UU. No genera por sí solo las notas de HealthScribe. Tampoco debe confundirse con la cobertura multilingüe de Transcribe general.

## Certificados y datos: páginas examinadas

- [ISO 27001, PDF vigente de 7 páginas](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/certification/compliance/iso_27001_global_certification.pdf): inspección visual de todas las páginas. [Catálogo ISO](https://aws.amazon.com/compliance/iso-certified/) al que remite su alcance.
- [SOC 3, PDF 2025–2026](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/whitepapers/compliance/AWS_SOC3_Report.pdf): dictamen del auditor, límites y servicios incluidos; [acceso SOC 1/2](https://aws.amazon.com/compliance/soc-faqs/). El SOC 3 excluye evaluar rendimiento e integridad de los servicios IA.
- [ENS ALTA](https://aws.amazon.com/compliance/services-in-scope/ENS-High/), [SOC](https://aws.amazon.com/compliance/services-in-scope/SOC/), [C5](https://aws.amazon.com/compliance/services-in-scope/C5/) y [HITRUST](https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/): Transcribe incluido; regla de cobertura de funciones, con auditoría en la siguiente oportunidad. Esto sustenta una **inferencia de alcance**, no la inspección de certificados individuales de HealthScribe.
- [ISO 42001: anuncio](https://aws.amazon.com/blogs/machine-learning/aws-achieves-iso-iec-420012023-artificial-intelligence-management-system-accredited-certification/), [FAQ](https://aws.amazon.com/compliance/iso-42001-faqs/) y [elegibilidad HIPAA](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/): distintos niveles de evidencia, detallados en la ficha.
- [DPA, 10 páginas](https://d1.awsstatic.com/legal/aws-dpa/aws-dpa.pdf), [términos](https://aws.amazon.com/service-terms/) y [subencargados](https://aws.amazon.com/compliance/sub-processors/): DPA §6 prevé notificación de nuevos subencargados con 30 días de antelación. Los términos §50.3 excluyen HealthScribe del régimen de reutilización para mejora de otros servicios de IA; §§1.24–1.24.2 contemplan Bedrock e inferencia entre regiones. La lista general no demuestra una cadena específica cerrada de HealthScribe.

La evidencia no acredita tratamiento exclusivamente europeo ni certificación automática de una aplicación desarrollada sobre AWS. Quedan por precisar el flujo regional efectivo, accesos de soporte, retención de metadatos y responsabilidades del integrador. Las copias de entradas/salidas que mantiene el cliente necesitan su propia política de conservación.

## Precio y uso en la comparación

[Tarifa oficial](https://aws.amazon.com/healthscribe/pricing/): **0,001667 USD/segundo**, incrementos de un segundo y mínimo de 15 segundos por petición; incluye transcripción y resumen. Aproximadamente **1,50 USD por consulta de 15 minutos**, solo procesamiento. Publica **300 minutos mensuales durante los dos primeros meses** como prueba gratuita. El coste hospitalario requiere añadir aplicación, integración, almacenamiento y operación; no es una suscripción clínica completa. Transparencia **A para la API**, no presupuesto total.

Inventarios: [certificaciones](../certificaciones-escribas-digitales.md), [HCIS](../integraciones-hcis.md), [precios](../precios-escribas-digitales.md). Presentación pendiente de revisión independiente.
