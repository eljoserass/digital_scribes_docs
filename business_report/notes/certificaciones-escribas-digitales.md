# Escribas digitales: certificaciones y evidencia pública

Revisión pública inicial: **9 de septiembre de 2026**. **43 proveedores**: 20 del conjunto inicial, 22 adicionales del registro NHS y AWS HealthScribe, incorporado el **17/09/2026**. Esta ampliación no supone una nueva revisión de las otras 42 fichas. La comparación aplica un formato y unos criterios de evidencia uniformes; el número de credenciales no constituye una medida de calidad clínica. [Integraciones con HCIS](integraciones-hcis.md) · [Precios](precios-escribas-digitales.md) · [Evaluación comparativa](analisis-escribas-digitales.md).

**Criterios de clasificación de la evidencia:** «declara» significa que el proveedor anuncia la credencial; la categoría «documentación primaria examinada» identifica certificados, informes o registros cuyo contenido ha sido consultado directamente. La verificación íntegra del emisor, la vigencia y el alcance requiere el certificado o informe completo. «No localizado» indica ausencia de evidencia identificada en las fuentes públicas consultadas; no permite concluir que la credencial no exista. Las condiciones de datos son declaraciones/documentos del proveedor, salvo indicación contraria.

## Definición y alcance de las credenciales

| Credencial | Objeto y límites de acreditación |
| --- | --- |
| **ENS, categoría ALTA: España** | Esquema Nacional de Seguridad: requisitos organizativos y técnicos para sistemas del sector público y proveedores incluidos en su ámbito. **ALTA es la categoría más exigente**, sujeta a auditoría; importa el sistema incluido en el certificado. No acredita por sí sola exactitud clínica ni residencia UE. [BOE, RD 311/2022](https://www.boe.es/eli/es/rd/2022/05/03/311). |
| **ISO/IEC 27001** | Certifica el sistema de gestión de seguridad de la información: riesgos, accesos, incidentes, continuidad y protección de confidencialidad, integridad y disponibilidad. El alcance puede cubrir solo parte de la empresa. [ISO](https://www.iso.org/standard/27001). |
| **ISO/IEC 27701** | Sistema de gestión de privacidad: responsabilidades y controles sobre el tratamiento de datos personales. No sustituye el análisis de cumplimiento del RGPD. [ISO](https://www.iso.org/standard/27701). |
| **ISO/IEC 27017 / 27018** | **27017:** controles de seguridad específicos de servicios cloud. **27018:** protección de datos personales cuando la nube pública actúa como encargada del tratamiento. [27017](https://www.iso.org/standard/43757.html), [27018](https://www.iso.org/standard/76559.html). |
| **ISO/IEC 20000-1** | Sistema de gestión de servicios de TI: planificación, prestación y mejora del servicio. No evalúa exactitud clínica. [ISO](https://www.iso.org/standard/70636.html). |
| **ISO/IEC 42001** | Certifica la **gestión de IA**: gobernanza, riesgos, responsabilidades y mejora continua. No acredita la ausencia de contenido no sustentado ni certifica la precisión clínica del escriba. [ISO](https://www.iso.org/standard/42001). |
| **Ethik-IA: Francia** | Sello privado de supervisión humana y uso ético de IA sanitaria. Examina, entre otros aspectos, equidad, trazabilidad, datos y robustez; no es el marcado CE ni una aprobación del AI Act. [Guía oficial francesa, §5.6](https://esante.gouv.fr/sites/default/files/media_entity/documents/guide-ia_vf.pdf). |
| **ISO 9001 / 13485 / 14001** | **9001:** gestión general de calidad. **13485:** gestión de calidad para productos sanitarios y requisitos regulatorios. **14001:** gestión ambiental. Ninguna sustituye la evaluación clínica del producto. [9001](https://www.iso.org/standard/62085.html), [13485](https://www.iso.org/standard/59752.html), [14001](https://www.iso.org/standard/14001). |
| **SOC 1 / SOC 2 / SOC 3; tipos I y II** | Informes de auditoría: **SOC 1**, controles relevantes para información financiera; **SOC 2**, controles de seguridad y, según alcance, disponibilidad, confidencialidad, privacidad e integridad del procesamiento. **I:** diseño en una fecha; **II:** también funcionamiento durante un periodo. **SOC 3:** informe de uso general sobre controles, con menos detalle que SOC 2. [AICPA](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services). |
| **C5 tipo II** | Auditoría de controles de seguridad cloud según el catálogo del BSI alemán; tipo II incluye eficacia durante un periodo. El auditor emite el informe, no un certificado del BSI. [BSI](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/CloudComputing/ComplianceControlsCatalogue-Cloud_Computing-C5.pdf?__blob=publicationFile&v=3). |
| **ISAE 3000** | Norma para encargos de aseguramiento no financiero. Puede respaldar una auditoría de privacidad, pero su interpretación requiere examinar criterios, alcance y periodo: el nombre solo no acredita cumplimiento íntegro del RGPD. [IAASB](https://www.iaasb.org/publications/international-standard-assurance-engagements-isae-3000-revised-assurance-engagements-other-audits-or). |
| **NEN 7510 / 7512 / 7513: Países Bajos** | **7510:** seguridad de información sanitaria; **7512:** intercambio seguro; **7513:** registro de accesos y operaciones. Aplicar las normas no equivale automáticamente a poseer certificados externos de las tres. [NEN](https://www.nen.nl/en/zorg-welzijn/ict-in-de-zorg/informatiebeveiliging-in-de-zorg). |
| **Cyber Essentials / Plus: UK** | Protección frente a ciberataques comunes. La modalidad básica usa autoevaluación verificada; **Plus añade comprobación técnica independiente**. No evalúa calidad clínica. [NCSC](https://www.ncsc.gov.uk/cyberessentials/overview). |
| **HDS: Francia** | Certificación del alojamiento de datos de salud por un organismo acreditado. Su interpretación requiere comprobar el titular y las actividades cubiertas: usar un proveedor HDS no convierte automáticamente al escriba en certificado HDS. [Agencia de Salud Digital](https://esante.gouv.fr/produits-services/hds). |
| **HITRUST** | Certificaciones de controles de ciberseguridad con distintas modalidades y profundidad. Deben identificarse certificado, sistema y vigencia; mencionar el marco no demuestra estar certificado. [HITRUST](https://hitrustalliance.net/assessments-and-certifications). |
| **TX-RAMP: Texas** | Programa público de evaluación de seguridad cloud. **Nivel 2:** datos confidenciales en sistemas de impacto moderado/alto; existe también nivel 1 y estatus provisional. No es una aprobación clínica. [Texas DIR](https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp/tx-ramp-frequently). |
| **CE bajo MDR / UKCA médico; clases I y IIa** | Marcados de conformidad para productos sanitarios de la UE/Gran Bretaña. En software de **clase I** suele bastar la declaración del fabricante; **IIa requiere evaluación de un organismo externo**. Alcance e indicación de uso son esenciales. [MDR UE](https://eur-lex.europa.eu/eli/reg/2017/745/oj), [MHRA](https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk). |
| **Registro MHRA** | Inscripción para comercializar en Gran Bretaña; no equivale por sí misma a una evaluación clínica independiente o certificación de clase IIa. [MHRA](https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk). |
| **Certificado de libre venta** | Acredita la comercialización de los productos identificados y facilita su exportación. Es distinto del certificado de conformidad MDR y de un estudio clínico. [Agencia sueca del medicamento](https://www.lakemedelsverket.se/en/medical-devices/sale). |
| **LVV/Valvira A1: Finlandia** | Clasificación de sistemas de información sociosanitaria, con evaluación de seguridad recogida en Astori. **A1 no es una clase de producto sanitario MDR**; son marcos diferentes. [Registro LVV](https://astori.lvv.fi/). |
| **ISO 14971 / IEC 62366-1** | **14971:** gestión de riesgos de productos sanitarios. **62366-1:** usabilidad y prevención de errores de uso que afectan a seguridad. En las fichas son normas aplicadas, salvo certificado externo identificado. [ISO](https://www.iso.org/standard/72704.html), [IEC](https://webstore.iec.ch/en/publication/21863). |
| **DTAC / DCB0129 / DCB0160 / DSPT: NHS** | **DTAC:** criterios para evaluar tecnología digital al adquirirla. **DCB0129:** gestión de riesgos clínicos por el fabricante; **DCB0160**, por la organización que lo implanta. **DSPT:** autoevaluación de seguridad/protección de datos. «NHS compliant» no constituye un certificado externo único. [DTAC](https://digital.nhs.uk/services/digital-technology-assessment-criteria-dtac), [DCB0129](https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dcb0129-clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems/), [DSPT](https://www.dsptoolkit.nhs.uk/). |
| **TGV / EFVP: Québec** | **TGV** (*Trousse globale de vérification*): certificación del producto exigida por el sistema sanitario provincial. **EFVP:** evaluación del impacto en privacidad de su implantación, responsabilidad de la organización compradora; son requisitos distintos. [Gobierno de Québec](https://www.quebec.ca/sante/professionnels/programme-transcription-intelligence-artificielle). |
| **FCC / ISED / conformidad radio UE-UK; ensayo SGS** | En Heidi Remote, credenciales de radio del **hardware** y un ensayo antibacteriano concreto de SGS. No certifican el escriba ni convierten el micrófono en producto sanitario. [Manual y referencias regulatorias](https://www.heidihealth.com/en-ca/docs/remote-user-manual). |
| **WEEE / RoHS / EMC: hardware** | **WEEE:** gestión de residuos electrónicos; aquí, adhesión a un sistema de recogida/reciclaje. **RoHS:** restricción de sustancias peligrosas. **EMC:** compatibilidad electromagnética. Las dos últimas figuran en la declaración del fabricante del micrófono Tandem. [WEEE/RoHS](https://environment.ec.europa.eu/topics/waste-and-recycling/rohs-directive_en), [declaración](https://trust.tandemhealth.ai/doc/trust?rid=6a78f0c64c2eeb0a116d6fb1&r=e0qkrepqo674el4jxq28px&view=true). |
| **AAPC / ACR-VPAT** | **AAPC:** aquí se refiere a una evaluación de codificación anunciada por Ambience. **ACR/VPAT:** informe sobre accesibilidad de software, publicado por Oracle. No son certificaciones generales de seguridad clínica. [Ambience](https://www.ambiencehealthcare.com/), [Oracle](https://docs.oracle.com/en/corporate/accessibility/templates/t2-16521.html). |
| **ISO 22301** | Gestión de continuidad de negocio: preparación, respuesta y recuperación ante interrupciones. No acredita exactitud clínica. [ISO](https://www.iso.org/standard/75106.html). |
| **Dubai AI Seal** | DCAI evalúa y clasifica empresas proveedoras de IA; el sello tiene número y categoría. No es aprobación de un producto sanitario. [DCAI](https://dub.ai/en/ai-seal/). |
| **CSA STAR niveles 1–2 / GovRAMP / IRAP** | **STAR 1:** autoevaluación de seguridad cloud. **STAR 2:** certificación o atestación con evaluación independiente; es necesario identificar modalidad y alcance. **GovRAMP:** programa de seguridad cloud con distintos niveles de verificación; es necesario verificar el estado específico. **IRAP:** evaluación frente a requisitos australianos, no certificación o acreditación del sistema. [CSA](https://cloudsecurityalliance.org/star/), [GovRAMP](https://govramp.org/security-program), [IRAP](https://www.cyber.gov.au/business-government/protecting-devices-systems/assessment-evaluation-programs/irap). |
| **IM1: NHS** | Proceso de aseguramiento de interfaces con sistemas de atención primaria, actualmente EMIS Web y SystmOne. No evalúa los modelos de IA ni acredita integración con HCIS. [NHS](https://digital.nhs.uk/services/digital-services-for-integrated-care/im1-pairing-integration). |
| **CREST: pentests** | Acredita empresas de pruebas de ciberseguridad y certifica profesionales. Un pentest realizado por ellos evalúa un alcance y una fecha; no convierte al escriba en «certificado CREST». [CREST](https://www.crest-approved.org/about-us/what-we-do/), [certificaciones profesionales](https://www.crest-approved.org/skills-certifications-careers/crest-certifications/). |

**Evidencia contractual, técnica y clínica complementaria:** declarar cumplimiento de RGPD, HIPAA o PIPEDA no demuestra una certificación externa; HHS no reconoce los sellos privados de «certificación HIPAA». DPA/BAA son contratos, PIA/EFVP son evaluaciones de privacidad; pentests, model cards y publicaciones son evidencias complementarias, con el alcance descrito en cada ficha. [HHS](https://www.hhs.gov/hipaa/for-professionals/faq/2003/are-we-required-to-certify-our-organizations-compliance-with-the-standards/index.html). Los estudios se separan y se señala la participación del proveedor. Una insignia «Verified» del portal no sustituye al certificado. El alcance de la revisión se limita a fuentes públicas, sin acceso a expedientes privados ni confirmación directa de los proveedores.

## 1. Noa Notes: Doctoralia / Docplanner

Documentación de referencia: [Seguridad](https://noa.ai/es-es/seguridad-y-privacidad) y DPA. No se localizó un Trust Center específico de Notes con certificados descargables.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | Docplanner; [Seguridad](https://noa.ai/es-es/seguridad-y-privacidad) | **Declarada** a nivel corporativo. Certificado, emisor, vigencia y alcance Notes pendientes de verificación. |

- **Tratamiento de datos en España:** DPA público: AWS para alojamiento/transcripción y Azure para resúmenes, almacenamiento UE; también enumera servicios auxiliares en EE. UU./Australia. **Permite mejorar modelos con datos desidentificados si el paciente consiente**; esta condición excluye una prohibición absoluta de reutilización para entrenamiento. [Contrato, §§3 y 6; anexo A y apéndice I](https://notes.es.noa.ai/terms-and-conditions/noa-notes-es.pdf).
- **Regulación sanitaria y calidad clínica:** el contrato declara que Notes **no es dispositivo médico** y exige revisión clínica. No se localizó evaluación del escriba revisada por pares; que Noa Evidence consulte literatura científica no valida Notes. [Contrato](https://notes.es.noa.ai/terms-and-conditions/noa-notes-es.pdf), [distinción de productos](https://noa.ai/es-es/).

## 2. Invox Medical: Invox Genesis / Vócali

Documentación de referencia: [Anuncio](https://www.invoxmedical.com/blog/invox-medical-refuerza-su-compromiso-con-la-seguridad-de-la-informacion-con-la-obtencion-de-la-certificacion-iso-27001-y-el-ens-nivel-alto) y documentación del producto; no se localizó catálogo público de certificados completos.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | Emisor no identificado; [Anuncio](https://www.invoxmedical.com/blog/invox-medical-refuerza-su-compromiso-con-la-seguridad-de-la-informacion-con-la-obtencion-de-la-certificacion-iso-27001-y-el-ens-nivel-alto) | **Declarada** por Invox/Vócali; certificado íntegro y vigencia no localizados. |
| ENS categoría ALTA | Emisor no identificado; [Anuncio](https://www.invoxmedical.com/blog/invox-medical-refuerza-su-compromiso-con-la-seguridad-de-la-informacion-con-la-obtencion-de-la-certificacion-iso-27001-y-el-ens-nivel-alto) | **Declarada**; alcance Genesis pendiente. Legitec aparece como asesor, no certificador. |

- **Tratamiento de datos:** anuncia migración de infraestructura a **AWS** y ausencia de almacenamiento de audios/información generada. País de procesamiento, DPA y lista completa de subencargados de Genesis pendientes de verificación. [Infraestructura](https://www.invoxmedical.com/blog/migramos-a-aws-para-reforzar-la-seguridad-y-escalabilidad-de-nuestra-infraestructura-tecnologica), [producto](https://www.invoxmedical.com/).
- **Evidencia externa:** la **Comunidad de Madrid confirma Genesis en Psiquiatría del Hospital Fundación Alcorcón**, junio de 2025. Acredita adopción en un hospital público, sin demostrar despliegue general del SERMAS ni validación clínica revisada por pares. [Comunidad de Madrid](https://www.comunidad.madrid/noticias/2025/06/10/hospital-publico-fundacion-alcorcon-incorpora-aplicacion-ia-optimizar-generacion-documentacion-clinica-partir-entrevistas).

## 3. Heidi: Scribe y Remote

Documentación de referencia: [Trust Center](https://trust.heidihealth.com/) y catálogo de recursos; combina PDFs públicos con documentos bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | **A-LIGN**, ISMS-HE-042726; [ISO](https://trust.heidihealth.com/doc/trust?rid=6a4673e10d5928c7f9995cea&r=qq3qqjsmu9pfv6v9q9xa7m&view=true) | **Certificado examinado**: ISMS de Scribe, Comms y Evidence; expira **10/05/2029**. |
| Cyber Essentials Plus | **AMTIVO**; [CE+](https://trust.heidihealth.com/doc/trust?rid=6a469d372506b7e736cfbd7d&r=qq3qqjsmu9pfv6v9q9xa7m&view=true) | **Certificado examinado**: Heidi Health Ltd; recertificación **02/07/2027**. |
| TX-RAMP nivel 2 | **Texas DIR**, TX1569070; [TX-RAMP](https://trust.heidihealth.com/doc/trust?rid=66f7864e59f37adebcf7d679&r=qq3qqjsmu9pfv6v9q9xa7m&view=true) | **Certificado examinado**; expira **26/09/2027**. |
| SOC 2 tipo II | **Prescient Assurance**; [carta SOC](https://trust.heidihealth.com/doc/trust?rid=6a1fad949f2b8d0d8c8937ca&r=qq3qqjsmu9pfv6v9q9xa7m&view=true) | **Carta examinada**, sin salvedades; periodo **05/06/2024–04/06/2025**. Verificación del informe completo pendiente. |
| ISO 9001 / ISO 42001 | [Credenciales](https://www.heidihealth.com/it/safety); [Trust Center](https://trust.heidihealth.com/) | **Declaradas**; emisor/alcance/vigencia pendientes de verificación. Certificado 42001 bajo solicitud. |
| C5 / UKCA | [Trust Center](https://trust.heidihealth.com/) | Insignias publicadas; tipo C5, clase UKCA y alcance del software pendientes de verificación. |
| TGV: Québec | [Québec](https://www.quebec.ca/sante/professionnels/programme-transcription-intelligence-artificielle) | **Registro oficial consultado**: TGV sí; EFVP de Santé Québec no. |

- **Tratamiento de datos:** declara permanencia UE/EEE para la oferta europea, sin entrenamiento con consultas/notas; subencargados en Trust Centre. **Remote conserva audio cifrado localmente hasta sincronizar**, por lo que no procede generalizar «no almacena audio». [UE](https://www.heidihealth.com/compliance/gdpr), [entrenamiento](https://support.heidihealth.com/en/articles/14648423-how-heidi-protects-your-data), [subencargados](https://trust.heidihealth.com/subprocessors), [Remote](https://support.heidihealth.com/en/articles/14130260-getting-started-with-heidi-remote).
- **Credenciales del dispositivo Remote:** manual declara FCC **2BULL-HV0**, ISED **35134-HV0**, conformidad radio UE/UK y ensayo antibacteriano SGS **GZF26-0000530-01**. Son credenciales del periférico; el fabricante indica que **no es dispositivo médico**. [Manual](https://www.heidihealth.com/en-ca/docs/remote-user-manual).
- **Evidencia de evaluación:** ensayo aleatorizado con Heidi, **279 pacientes**, *Journal of Arthroplasty* (2026): mejora eficiencia, pero registra **19 errores médicos frente a 9** con documentación convencional. Un único cirujano; no demuestra rendimiento general ni evalúa Remote. [Artículo](https://doi.org/10.1016/j.arth.2026.03.069).
- **Evaluación en español:** preprint de agosto de 2026 con **385 consultas simuladas emparejadas en cinco países**, incluido un centro de Barcelona en español. Compara notas de Heidi y de clínicos con evaluación ciega; resultados agregados favorables. **Financiado íntegramente por Heidi, sin revisión por pares**; las 385 consultas no son todas españolas y no prueban resultados en pacientes reales. [Estudio](https://www.medrxiv.org/content/10.64898/2026.08.18.26360701v1).

## 4. Solventum: Fluency Align

Documentación de referencia: [Ficha UK](https://assets.solventum.com/is/content/mmmspinco/fluency-align-key-benefits-and-security-data-sheet-his-cps-en-gbpdf) y [FAQ España](https://www.solventum.com/es-es/home/health-information-technology/solutions/fluency-align/); no se localizó expediente público de Align.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 / Cyber Essentials | [Ficha UK](https://assets.solventum.com/is/content/mmmspinco/fluency-align-key-benefits-and-security-data-sheet-his-cps-en-gbpdf) | **Declaradas**; certificados, emisor, vigencia y alcance Align con verificación documental pendiente. |
| ENS categoría ALTA | [FAQ España](https://www.solventum.com/es-es/home/health-information-technology/solutions/fluency-align/) | Declara cumplimiento ENS ALTO; **certificado pendiente de verificación**. |
| ISO 42001 | [Ficha UK](https://assets.solventum.com/is/content/mmmspinco/fluency-align-key-benefits-and-security-data-sheet-his-cps-en-gbpdf) | **Alineación**, no certificación demostrada. |

- **Tratamiento de datos:** declara almacenamiento **y procesamiento en AWS Frankfurt, UE**; no cede datos para entrenar modelos externos. Esto no descarta entrenamiento interno. Retención, DPA y cadena completa de subencargados pendientes de verificar. [FAQ España](https://www.solventum.com/es-es/home/health-information-technology/solutions/fluency-align/).
- **Regulación sanitaria y calidad clínica:** la ficha UK promete cumplimiento **DTAC/DCB0129 antes de firmar contrato**. No se localizó estudio revisado por pares específico de Align; el caso del Hospital del Sureste corresponde a **Fluency Direct**. [Ficha UK](https://assets.solventum.com/is/content/mmmspinco/fluency-align-key-benefits-and-security-data-sheet-his-cps-en-gbpdf), [recursos y casos](https://www.solventum.com/es-es/home/health-information-technology/solutions/fluency-align/).

## 5. Tandem Health

**Documentación externa examinada**, disponible en su [Trust Center](https://trust.tandemhealth.ai/) y [catálogo Assuric](https://trust.assuric.com/tandem/public/compliance):

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| **[ENS categoría ALTA](https://file.assuric.com/orgs%2Ftandem%2FcontrolEvidence%2FrTj5GDSXKa16FVqjjsV4%2F25252991-%20ENS%20-%20ALTA-TANDEM%20HEALTH%20AB%20%28SITE%20VIRTUAL%29-ESPANI%CC%80_OL.pdf?alt=media&token=77dff88d-f576-4c0a-a95e-77ed28223e1f)** | **Bureau Veritas**, ES154689-1 | Sistema de desarrollo/soporte del SaaS Tandem para atención clínica y administración; Azure Gävle. **10/09/2025–10/09/2027**. Copia pública: página 1/2. |
| **[ISO 27001:2022](https://file.assuric.com/orgs%2Ftandem%2FcontrolEvidence%2F4YOEj8c6wuyZ7rpTKD4u%2F05%20ISMS%20Certificate%20v2.0%20-%20Tandem%20Health%20AB.pdf?alt=media&token=8e3ca92c-f0db-475a-bc3b-06044a35716f)** | **Insight Assurance**, IA-2024-12-17-02 | Gestión de seguridad de Tandem Health AB; versión 05/02/2026, expira **17/12/2027**. |
| **[ISO 13485:2016](https://file.assuric.com/orgs%2Ftandem%2FcontrolEvidence%2Fs4KoRqo4iYEUdz0Jmu7p%2FSCAR-9.1.1.0%20-%20Tandem%20-%20ISO%2013485%20Certificate.pdf?alt=media&token=b87e7394-d280-44fd-a73f-cb75d27b1126)** | **Scarlet**, SCAR-9.1.1.0 | Diseño/fabricación de software sanitario de documentación; **15/10/2025–14/10/2028**. |
| **[ISO 42001:2023](https://file.assuric.com/orgs%2Ftandem%2FcontrolEvidence%2FpoCpC7GQYwIJRb65B40G%2FSCAR-9.9.1.0.pdf?alt=media&token=3196aaed-1602-4fc2-b196-2e6939bb6cc4)** | **Scarlet**, SCAR-9.9.1.0 | Software sanitario con IA y usos internos de IA; expira **06/05/2029**. |
| **[ISO 14001:2015](https://file.assuric.com/orgs%2Ftandem%2FcontrolEvidence%2FqkNFoPUk2Ck4cMsMGwgr%2F0245002_ENG_14001_Tandem%20Health%20AB.pdf?alt=media&token=9c97057e-cff8-404a-86bc-43c491c3dd3c)** | **Intertek**, 0245002 | Gestión ambiental del desarrollo/operación de software sanitario; expira **06/05/2029**. |
| **[NEN 7510-1:2024](https://file.assuric.com/orgs%2Ftandem%2FcontrolEvidence%2FjGRsY5eN0u0cu7ynzA9o%2FNL%202864.1.2%20-%20Tandem%20Health%20AB%20-%20NEN%207510.pdf?alt=media&token=51a06ba9-5b80-4eb5-96ef-17818c7d3ee2)** | **Brand Compliance**, NL 2864.1.2 | Seguridad de la plataforma de documentación clínica; alojamiento externalizado. Expira **15/04/2029**. |
| **[C5 tipo II: dictamen](https://trust.tandemhealth.ai/doc/trust?rid=6a79840c39de23960acdd51f&r=e0qkrepqo674el4jxq28px&view=true)** | **HKKG**, 16/06/2026 | SaaS Tandem; periodo **17/02–18/05/2026**. **Con salvedades**: verificaciones de personal, formación, manejo de metadatos y estrategias de salida de proveedores. |
| **[CE MDR clase IIa](https://file.assuric.com/orgs%2Ftandem%2FcontrolEvidence%2F7f7koYGmQJa8TWFMTNqm%2FSCAR-9.2.1.5%20-%20Tandem%20-%20Quality%20EU%20MDR%20Certificate.pdf?alt=media&token=aa8686b7-6a03-4f04-9d4a-f40e217d6bd1)** | **Scarlet NB B.V., 3022**, SCAR-9.2.1.5 | Incluye explícitamente **AI Medical Scribe**, Coder y Guide; revisión 18/06/2026, expira **15/02/2031**. Requiere revisión profesional de las salidas. |

- **Otras credenciales:** **Cyber Essentials Plus** declarado, con enlace a registro; **Ethik-IA** anunciado, sin certificado localizado. **Astori/LVV confirma Scribe v1.0.0, clase A1**, certificado de seguridad **FI251028-214**, 28/10/2025–28/10/2028. **DSPT 2025–26: “Standards exceeded”**; DTAC/DCB0129 con documentación bajo solicitud. [Trust Center](https://trust.tandemhealth.ai/), [Astori: buscar Tandem](https://astori.lvv.fi/), [DSPT oficial](https://www.dsptoolkit.nhs.uk/OrganisationSearch/TAHEAB001).
- **Documentación complementaria examinada:** **libre venta**, Agencia Sueca del Medicamento, 10/08/2026, incluye Scribe/Coder/Guide; **WEEE 2026**, adhesión a El-Kretsen para residuos electrónicos; micrófono **BM10**, declaración propia RoHS/EMC. La representación suiza es un mandato, no certificación del producto; también enlaza inscripción estonia. [Libre venta](https://trust.tandemhealth.ai/doc/trust?rid=6a86ba9438622132aac7533c&r=e0qkrepqo674el4jxq28px&view=true), [WEEE](https://trust.tandemhealth.ai/doc/trust?rid=6a78f060820290d89042a93e&r=e0qkrepqo674el4jxq28px&view=true), [micrófono](https://trust.tandemhealth.ai/doc/trust?rid=6a78f0c64c2eeb0a116d6fb1&r=e0qkrepqo674el4jxq28px&view=true), [mandato suizo](https://www.chrep.me/certificates-ch-rep/ch-rep-eu6romde4), [catálogo](https://trust.tandemhealth.ai/resources).
- **Tratamiento de datos:** declara procesamiento/almacenamiento UE, audio eliminado tras transcribir y sin entrenamiento con datos de pacientes. Lista actual: **Azure, ElevenLabs, Snowflake, Intercom** y entidades del grupo, con ubicaciones UE declaradas. [Seguridad](https://tandemhealth.ai/product/data-security), [subencargados](https://trust.tandemhealth.ai/subprocessors).
- **Evidencia de evaluación:** *JMIR Medical Informatics* (2026), **236.153 notas y encuesta a 177 usuarios en Suecia**, observacional, con autores de Tandem: tiempo autodeclarado por nota −29%; no es ensayo de seguridad clínica ni validación en español. El documento de orientación para la contratación es una guía comercial de contratación. [Estudio y resumen](https://tandemhealth.ai/resources/research/evaluation-of-an-ai-medical-scribe-after-236153-notes-generated-across-care-levels-in-a-european-health-system), [DOI](https://doi.org/10.2196/90052), [whitepaper](https://mcusercontent.com/92915049aef2f51e4bcdd8434/files/a252c926-b88a-0af8-4071-a19fed8b9bf5/Procurement_of_Ambient_Voice_Technology_EN.pdf).

## 6. Microsoft: Dragon Copilot

Documentación de referencia: [FAQ](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/about/faqs) y catálogo de cumplimiento de Microsoft; informes completos con verificación documental pendiente.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 42001 | [Alcance 42001](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001) | Microsoft incluye Dragon Copilot en el alcance publicado; verificación del certificado íntegro pendiente. |
| SOC 1 II / SOC 2 II / C5 II | [FAQ](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/about/faqs) | **Declarados** para Dragon Copilot; auditor, periodos e informes pendientes de verificación. |
| NEN 7510 / 7512 / 7513 | [FAQ](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/about/faqs) | Cumplimiento declarado; certificados individuales con verificación documental pendiente. |
| ISO 27001 / ISO 27701 | [FAQ](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/about/faqs) | **Pendientes** en la FAQ de 27/07/2026; no se cuentan como obtenidas. |
| UKCA clase I | [Instrucciones](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/about/eifu) | **Autodeclaración** del fabricante; no evaluación independiente de clase IIa. |

- **Tratamiento de datos:** EU Data Boundary, con excepciones contractuales; documentación europea identifica Francia/Alemania, sin concretar España. Retención hasta **90 días**; **reutiliza datos anonimizados para mejorar modelos**, con posible intervención humana. Publica enlaces a DPA/subencargados. [Privacidad](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/whitepapers/privacy), [condiciones](https://www.microsoft.com/licensing/terms/en-US/product/PrivacyandSecurityTerms/all).
- **Regulación sanitaria y evaluación clínica:** UKCA clase I **autocertificada**. El ensayo *NEJM AI* con 238 médicos evaluó **DAX Copilot**, su predecesor: relevante, pero no valida toda la versión actual; DAX no redujo significativamente el tiempo de documentación (*time-in-note*) frente al control. [Instrucciones](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/about/eifu), [ensayo](https://doi.org/10.1056/AIoa2501000).

## 7. Nabla

Documentación de referencia: [Trust Center](https://trust.nabla.com/?format=html); certificados, SOC y pentest requieren acceso.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | [Trust Center](https://trust.nabla.com/?format=html) | **Declarada**; documento de septiembre de 2025 bajo solicitud. |
| SOC 2 tipo II | [Trust Center](https://trust.nabla.com/?format=html) | **Declarado**; periodo noviembre 2024–octubre 2025. Informe/auditor con verificación documental pendiente. |
| TX-RAMP nivel 2 | [Trust Center](https://trust.nabla.com/?format=html) | **Declarado**; documento enero de 2026 bajo solicitud. |
| HDS | [oferta europea](https://www.nabla.com/compliance-security) | Atribuido a **infraestructura**; certificado propio de Nabla no demostrado. |

- **Tratamiento de datos:** GCP Bélgica para clientes fuera de EE. UU.; oferta europea declara tratamiento UE. Audio no conservado por defecto; notas **14 días**, configurable. DPA identifica Google/Microsoft Ireland y permite reutilización anonimizada con autorización expresa; la matriz regional de subencargados requiere confirmación contractual. [Trust Center](https://trust.nabla.com/?format=html), [DPA](https://www.nabla.com/fr/security-documents/data-protection-agreement).
- **Evidencia de evaluación:** ensayo aleatorizado *NEJM AI* (2025), **238 médicos/14 especialidades**, Nabla/DAX/control: reducción modesta del tiempo de documentación con Nabla; un centro y consultas en inglés. Model card y adhesión CHAI no se cuentan como certificación clínica. [Ensayo](https://doi.org/10.1056/AIoa2501000), [documentos de gobernanza](https://trust.nabla.com/?format=html).

## 8. Abridge

Documentación de referencia: [Trust Center](https://trust.abridge.com/); SOC, pentest y documentación de IA requieren acceso.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 tipos I y II | [Trust Center](https://trust.abridge.com/) | **Declarados** para sus productos, seguridad/confidencialidad; informes bajo solicitud. |
| TX-RAMP | [Trust Center](https://trust.abridge.com/) | Mención en portal; **nivel, vigencia y documento pendientes de verificación**. |

- **Tratamiento de datos:** soporte declara almacenamiento/procesamiento en **EE. UU.** La política general excluye los datos clínicos de clientes, regidos por contrato/BAA: retención, entrenamiento y subencargados del escriba necesitan esos documentos. [Soporte](https://support.abridge.com/hc/en-us/articles/30235294201619-Data-Security-and-HIPAA-Compliance), [privacidad](https://www.abridge.com/privacy).
- **Evidencia de evaluación:** *JAMA Network Open* (2025), antes/después, **263 profesionales de seis sistemas**, mejora autodeclarada de carga/burnout; sin aleatorización y con coautor del proveedor. También hay trabajo específico de aseguramiento de calidad en *NEJM AI*. [JAMA](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2839542), [NEJM AI](https://doi.org/10.1056/AIcs2400977), [catálogo](https://www.abridge.com/ai/publications).

## 9. Ambience Healthcare

Documentación de referencia: [Trust Center y recursos](https://trust.ambiencehealthcare.com/); documentos bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 tipos I y II | [Trust Center](https://trust.ambiencehealthcare.com/) | **Declarados**; catálogo lista SOC 2 II 2026, pentest 2026 y subencargados, todos bajo solicitud. |
| Evaluación de codificación AAPC | [AAPC según proveedor](https://www.ambiencehealthcare.com/) | Anuncia **95%**; informe externo completo y metodología no localizados. |
| ISO 27001 / Cyber Essentials del revendedor | [ficha Hitachi](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/285898651648070) | Titular **Hitachi**; no se atribuyen automáticamente al escriba Ambience. |

- **Tratamiento de datos:** esa oferta G-Cloud declara almacenamiento/procesamiento **UK**; no demuestra residencia UE. La política remite al contrato/BAA para datos clínicos y permite compartir información desidentificada según contrato; retención y lista completa de subencargados pendientes de verificación. [Ficha](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/285898651648070), [privacidad](https://www.ambiencehealthcare.com/privacy).
- **Evidencia de evaluación:** *npj Health Systems* (2026), implantación en Cleveland Clinic a **más de 4.000 profesionales** en cuatro meses, con coautores del proveedor. Es evidencia de implementación, no ensayo de exactitud clínica. [Artículo](https://www.nature.com/articles/s44401-026-00144-6).

## 10. Suki

Documentación de referencia: [Trust Center](https://trust.suki.ai/) y subencargados; informes bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 tipo II | [Trust Center](https://trust.suki.ai/) | **Declarado**; informe **26/05/2025–25/05/2026** bajo solicitud; auditor pendiente de verificación. |
| TX-RAMP | [Trust Center](https://trust.suki.ai/) | **Declarado**; nivel y vigencia pendientes de verificación. No se encontró respaldo primario para ISO/HITRUST. |

- **Tratamiento de datos:** Compose declara entrenamiento con **datos anonimizados** y grabaciones en nube cifrada; BAA público y subencargados publicados en el Trust Center. Residencia UE y plazo del audio pendientes de verificación. Las condiciones deben verificarse para la solución contratada. [Compose](https://www.suki.ai/suki-compose/), [BAA](https://app.suki.ai/business-associate-agreement), [subencargados](https://trust.suki.ai/subprocessors).
- **Evidencia de evaluación:** *Frontiers in Artificial Intelligence* (2025), comparación ciega de notas de **97 consultas/cinco especialidades**: alucinaciones en 31% de notas Suki frente a 20% de referencia médica. Datos de 2024, en inglés, autores vinculados comercialmente a Suki; no es tasa universal del producto actual. [Artículo](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1691499/full).

## 11. DeepScribe

Documentación de referencia: [Trust Center y actualizaciones](https://trust.deepscribe.ai/); documentos bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 tipo II | [Trust Center y actualizaciones](https://trust.deepscribe.ai/) | **Declarado**; informe **01/01–31/12/2024**, carta de continuidad 03/10/2025, bajo solicitud. |
| Auditoría HIPAA | [Trust Center y actualizaciones](https://trust.deepscribe.ai/) | Documento bajo solicitud; **no certificación HIPAA oficial**. Vanta aloja el portal, no es el auditor identificado. |

- **Tratamiento de datos:** identifica **AWS SageMaker/Bedrock**; publica cifrado, desidentificación y controles de acceso. Retención según necesidad/contrato/BAA; residencia UE, cadena completa de subencargados y prohibición contractual de entrenamiento pendientes de verificación. [Arquitectura y controles](https://www.deepscribe.ai/resources/deepscribe-launches-new-and-innovative-trust-and-safety-suite-for-its-ambient-ai-technology), [privacidad](https://www.deepscribe.ai/privacy).
- **Evidencia de evaluación:** **DeepScore**, arXiv (2024), describe evaluación de errores/entidades/aceptación; **preprint del proveedor**, sin publicación revisada por pares identificada en las fuentes consultadas. Su *Trust and Safety Suite* es funcionalidad propia, no acreditación externa; no se localizó validación oncológica independiente específica. [DeepScore](https://arxiv.org/abs/2409.16307), [suite](https://www.deepscribe.ai/resources/deepscribe-launches-new-and-innovative-trust-and-safety-suite-for-its-ambient-ai-technology).

## 12. Commure: Ambient AI

Documentación de referencia: [Trust Center](https://www.commure.com/trust-center); no ofrece un informe que resuelva la ambigüedad de alcance SOC.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 | [KLAS, p. 4](https://discover.commure.com/hubfs/Commure%20Ambient%20AI%202025%20First%20Look%20-%20Final-1.pdf); [Trust Center](https://www.commure.com/trust-center) | Declaración en KLAS; portal ambiguo y referencia tipo II de **centros de datos**. Informe del Ambient pendiente de verificación. |
| HITRUST | [KLAS, p. 4](https://discover.commure.com/hubfs/Commure%20Ambient%20AI%202025%20First%20Look%20-%20Final-1.pdf) | Ficha 2025: **no**. Certificación posterior del producto no localizada. |
| CE MDR clase I / registro MHRA | [Anuncio](https://www.commure.com/press-releases/commure-ambient-ai-achieves-class-i-certification-and-mhra-registration) | Anuncio 03/09/2026: **autodeclarados**; no certificado de organismo notificado. |
| ISO 14971 / IEC 62366-1 | [Anuncio](https://www.commure.com/press-releases/commure-ambient-ai-achieves-class-i-certification-and-mhra-registration) | Normas aplicadas; certificados externos con verificación documental pendiente. |

- **Tratamiento de datos y evaluación:** anuncia residencia **UK**, mientras el Trust Center describe infraestructura estadounidense; retención contractual y subencargados bajo solicitud. La modalidad regional requiere confirmación contractual. KLAS recoge experiencia de siete organizaciones, **sin revisión por pares ni validación clínica**; no se localizó una publicación científica del producto Ambient actual. [Anuncio UK](https://www.commure.com/press-releases/commure-ambient-ai-achieves-class-i-certification-and-mhra-registration), [datos](https://www.commure.com/trust-center), [KLAS](https://discover.commure.com/hubfs/Commure%20Ambient%20AI%202025%20First%20Look%20-%20Final-1.pdf).

## 13. Corti: plataforma/API y Assistant MD

Documentación de referencia: [Seguridad](https://corti.ai/safety) y base de conocimiento; [portal Drata](https://app.drata.com/trust/9cc6d701-0c38-11ee-865f-029d78a187d9) con acceso técnico al portal, pero sin contenido susceptible de examen documental.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 / 27017 / 27018 | **A-LIGN**, según [ISO](https://corti.ai/stories/corti-completes-iso-audits-with-zero-nonconformities) | Auditoría anunciada **16/06/2026**; certificados y vigencias con verificación documental pendiente. |
| ISO 42001 / Cyber Essentials Plus | [42001/CE+](https://corti.ai/stories/corti-achieves-iso-iec-42001-certification) | **Declaradas**; documentación íntegra pendiente de verificación. |
| SOC 2 II / C5 II / ISAE 3000 II | [auditorías](https://corti.ai/stories/how-corti-supports-medical-device-manufacturers-regulatory-ready-ai) | **Declaradas**; última, privacidad. Auditor, periodos y dictámenes con verificación documental pendiente. |
| Clase I UK/UE: Assistant MD | [Alcance regulatorio](https://corti.ai/stories/corti-achieves-eu-medical-device-registration-strengthening-the-foundation-for-regulated-healthcare-ai) | Registro declarado para **Assistant MD**; no se traslada a la API ni a productos desarrollados sobre la plataforma. |
| ISO 13485 / ISO 14971 | [Alcance regulatorio](https://corti.ai/stories/corti-achieves-eu-medical-device-registration-strengthening-the-foundation-for-regulated-healthcare-ai) | Conformidad declarada; **certificación no demostrada**. |

- **Tratamiento de datos:** ofrece región UE, DPA público y aviso de nuevos subencargados; contrato prohíbe entrenar modelos para otros clientes salvo **opt-in expreso**. No significa ausencia de todo ajuste específico del cliente. [Seguridad](https://corti.ai/safety), [contrato](https://corti.ai/legal/master-terms-of-service), [DPA](https://corti.ai/legal/data-processing-agreement).
- **Evidencia de evaluación:** **FactsR** evalúa documentación, pero es preprint del proveedor; el trabajo de ictus no valida el escriba. [FactsR](https://arxiv.org/abs/2505.10360), [investigación](https://corti.ai/research).

## 14. Oracle: Health Clinical AI Agent / Clinical Note

Documentación de referencia: [Certificaciones y auditorías OHAI](https://www.oracle.com/uk/corporate/acquisitions/cerner/security/); no se localizó certificado específico de Clinical Note.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | [Certificaciones y auditorías OHAI](https://www.oracle.com/uk/corporate/acquisitions/cerner/security/) | Programa corporativo OHAI; **alcance Clinical Note pendiente de verificación**. |
| SOC 1 / SOC 2 tipo II | [Certificaciones y auditorías OHAI](https://www.oracle.com/uk/corporate/acquisitions/cerner/security/) | Determinados entornos de alojamiento; no atribuidos automáticamente al escriba. |
| ACR/VPAT | [ACR](https://docs.oracle.com/en/corporate/accessibility/templates/t2-16521.html) | Declaración de **accesibilidad** de Oracle; no certificación clínica. |

- **Tratamiento de datos:** OHAI describe alojamiento en el país del cliente salvo acuerdo distinto, con acceso operativo internacional posible. No acredita procesamiento íntegro UE de Clinical Note; región, retención, entrenamiento y subencargados específicos pendientes. La consola contempla archivar/descargar grabaciones. [OHAI](https://www.oracle.com/uk/corporate/acquisitions/cerner/security/), [consola](https://docs.oracle.com/en/corporate/accessibility/templates/t2-16689.html).
- **Evidencia de calidad clínica:** los resultados localizados son pilotos/casos NHS; no se localizó evaluación del escriba revisada por pares ni documentación primaria de certificación sanitaria accesible. [Pilotos](https://www.oracle.com/uk/news/announcement/oracle-health-clinicalai-agent-helps-uk-doctors-spend-more-time-on-patient-care-2026-02-12/).

## 15. Tortus

Documentación de referencia: [Trust Center](https://trust.tortus.ai/) y recursos públicos; otros documentos requieren acceso.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | **LRQA**, 10712929; [27001](https://trust.tortus.ai/doc/trust?rid=68cc0d7dc8e88b2e67d98932&r=p97jk29hxd122x8d1cq4&view=true) | **Certificado examinado**: alcance escriba TORTUS; expira **24/08/2028**. |
| ISO 13485 | **Scarlet NB UK**, SCAR-16.4.1.0; [13485](https://trust.tortus.ai/doc/trust?rid=699582984a4bafd95d114b9a&r=p97jk29hxd122x8d1cq4&view=true) | **Certificado examinado**: software de documentación; expira **16/02/2029**. |
| Cyber Essentials Plus | **CyberSmart**; [CE+](https://trust.tortus.ai/doc/trust?rid=68cc0e3a1650a1721bb52f61&r=p97jk29hxd122x8d1cq4&view=true) | **Certificado examinado**; recertificación **24/07/2027**. |
| UKCA clase IIa | **Scarlet, 8536**, según [UKCA](https://tortus.ai/years-in-the-making) | Anunciado **24/06/2026**; verificación documental de UKCA pendiente. El catálogo conserva un registro clase I anterior. |

- **Tratamiento de datos:** lista **Google Cloud, OpenAI, Auth0 y Datadog**; infraestructura Londres, endpoint OpenAI UE con retención cero y sin entrenamiento, Datadog UE. No demuestra residencia íntegra UE; transcripciones para depuración pueden conservarse hasta resolver incidencias. [Política del producto](https://tortus.ai/privacy).
- **Evidencia de evaluación:** *npj Digital Medicine* (2025), **25 consultas simuladas, 18 experimentos, 50 evaluadores**, con autores de Tortus. El **75% menos de alucinaciones mayores** corresponde a cambios de prompt (4→1), no a una certificación independiente del sistema Shell actual. [Artículo](https://www.nature.com/articles/s41746-025-01670-7).

## 16. Lyrebird

Documentación de referencia: [Trust Center](https://trust.lyrebirdhealth.com/) y recursos; certificado ISO examinado, otros documentos con acceso o extracción limitada.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | **Certifi International**, A307RA001ISMS; [Certificado ISO](https://trust.lyrebirdhealth.com/doc/trust?rid=6a4b29f494ea8ceec985e54e&r=5fwb6zo2bnid995vtydj6&view=true) | **Certificado examinado**: Subsidio Pty Ltd / Lyrebird, plataforma clínica; **26/06/2026–26/06/2029**. |
| Cyber Essentials / Plus | [Trust Center](https://trust.lyrebirdhealth.com/) | **Declaradas**; PDF Plus localizado, contenido pendiente de verificación. |
| MHRA / UKCA clase I | [compliance UK](https://www.lyrebirdhealth.com/uk/uk-compliance) | Registro/conformidad declarados; **no evaluación externa de clase IIa**. |

- **Tratamiento de datos:** documentación UK: almacenamiento **UK**, inferencia transitoria **UE**, sin entrenamiento; audio eliminado tras transcribir (sin conexión, permanece en el dispositivo hasta reconectar); notas/transcripciones **siete días por defecto**, configurable. Subencargados en Trust Centre. La página de producto `/uk/` menciona Australia: **documentación regional inconsistente**. [Compliance](https://www.lyrebirdhealth.com/uk/uk-compliance), [retención](https://help.lyrebirdhealth.com/en/articles/9229907-what-processes-does-lyrebird-use-to-protect-data), [producto](https://www.lyrebirdhealth.com/uk/product/clinical-notes).
- **Evidencia de evaluación:** *BMC Health Services Research* (2026), estudio mixto de **16 semanas/7.499 consultas**; reporta errores/alucinaciones. Queensland Health identifica Lyrebird como herramienta evaluada. [Artículo](https://pubmed.ncbi.nlm.nih.gov/41507920/), [identificación del producto](https://www.clinicalexcellence.qld.gov.au/improvement-exchange/enhancing-clinical-care-with-ambient-listening).

## 17. Tali

Documentación de referencia: [Seguridad](https://tali.ai/security-privacy); SOC, PIA y pentest bajo solicitud, sin repositorio público específico localizado.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 tipo II | [Seguridad](https://tali.ai/security-privacy) | **Declarado**; informe, auditor y periodo con verificación documental pendiente. |
| TGV: Québec | [registro](https://www.quebec.ca/sante/professionnels/programme-transcription-intelligence-artificielle) | **Registro oficial consultado**, 09/07/2026: TGV sí; EFVP de Santé Québec no. |

- **Tratamiento de datos:** Canadá si se selecciona esa región; otros países, EE. UU.; cuenta puede procesarse en EE. UU. Política: audio hasta **48 h**, notas/transcripciones **al menos 30 días**, desidentificación para mejoras. **Contradice el mensaje comercial de no conservar información clínica**. Proveedores de IA no identificados nominalmente. [Política](https://tali.ai/privacy-policy), [seguridad](https://tali.ai/security-privacy).
- **Evidencia de evaluación:** *Urology* (2025), comparación de cinco escribas con consultas simuladas. Tali y Nabla reciben mejores valoraciones, pero todos generan errores menores y críticos. [Artículo](https://doi.org/10.1016/j.urology.2024.11.061).

## 18. Scribeberry

Documentación de referencia: [Trust Center](https://trust.scribeberry.com/) y documentos de seguridad; SOC bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 tipo II | [SOC](https://scribeberry.com/product/security); [Trust Center](https://trust.scribeberry.com/) | **Declarado**; informe bajo solicitud. |
| Evaluación de riesgos HIPAA/PIPEDA | **Ingrid Ruys**, 14/01/2024; [evaluación firmada](https://scribeberry.com/docs/security-risk-assessment.pdf) | **Documento externo examinado**; no sustituye al SOC ni certifica HIPAA oficialmente. |
| TGV / EFVP: Québec | [Québec](https://www.quebec.ca/sante/professionnels/programme-transcription-intelligence-artificielle) | **Registro oficial consultado**, 24/04/2026: ambos **no**. |

- **Tratamiento de datos:** declara residencia **Canadá/EE. UU.** según región; Azure/Google Cloud y acuerdos con Microsoft, Google, OpenAI y Anthropic. Sin retención de audio ni entrenamiento con datos clínicos; notas con retención configurable. No acreditada residencia UE. [Seguridad y documentos](https://scribeberry.com/product/security).
- **Evidencia de evaluación:** *Healthcare* (2025), piloto prospectivo de Scribeberry V2 en paliativos, **dos residentes/19 casos**, resultados heterogéneos. La muestra reducida limita la generalización a otras versiones y contextos. [Artículo](https://www.mdpi.com/2227-9032/13/17/2118).

## 19. Quirónsalud: proyecto Scribe

Documentación de referencia: [Anuncio](https://www.quironsalud.com/es/comunicacion/actualidad/quironsalud-redisena-modelo-asistencial-reafirmandose-human); no se localizó Trust Center específico del proyecto Scribe.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Certificación del sistema Scribe | [Anuncio](https://www.quironsalud.com/es/comunicacion/actualidad/quironsalud-redisena-modelo-asistencial-reafirmandose-human) | **No localizada**. Noticia asistencial sin fabricante técnico, certificado ni oferta para terceros. |

- **Tratamiento de datos:** anuncia confidencialidad, almacenamiento seguro y validación médica; no especifica país, subencargados, retención o entrenamiento. [Misma fuente](https://www.quironsalud.com/es/comunicacion/actualidad/quironsalud-redisena-modelo-asistencial-reafirmandose-human).
- **Evidencia de evaluación:** *International Journal of Medical Informatics* (2026): estudio retrospectivo de **48 hospitales españoles, 1.032.558 consultas con Scribe**, febrero de 2025–enero de 2026. Reporta menor duración y mejoras documentales. Revisado por pares, con autores del grupo; sin aleatorización. El resumen no desglosa rendimiento por idioma ni demuestra exactitud clínica de todas las notas. Publicación electrónica julio de 2026, número de noviembre. [PubMed](https://pubmed.ncbi.nlm.nih.gov/42456601/), [artículo](https://doi.org/10.1016/j.ijmedinf.2026.106584).
- **Evidencia ambulatoria (actualización de 11/09/2026):** un segundo estudio analiza más de **2,33 millones de usos**. Duración media: **15,01 min con Scribe frente a 14,65 sin él**. El **87,4–89,2% es similitud semántica entre borrador y texto corregido**, no exactitud clínica independiente. Encuestas transversales de baja respuesta; autores empleados por Quirón. Es evidencia española de implantación, sin validar todos los acentos ni demostrar HCIS o venta a terceros. Los usos de ambos estudios no deben sumarse como si correspondieran a pacientes independientes. [Artículo y métodos](https://doi.org/10.3389/fdgth.2026.1874919), [ficha de lectura](executive_report/notes/references/U5GHQW86.md).

## 20. Freed

Documentación de referencia: [Seguridad](https://www.getfreed.ai/security); [Trust Center](https://app.drata.com/trust/1d1964c2-b90c-41ac-8d7c-2ea7f5af001c) con contenido inaccesible durante la consulta; verificación del expediente pendiente.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| SOC 2 tipos I y II | [Seguridad](https://www.getfreed.ai/security) | **Declarados**; informe, auditor y periodo con verificación documental pendiente. ISO/HITRUST o acreditación médica no localizados. |

- **Tratamiento de datos:** **Azure EE. UU.**; audio temporal hasta completar resumen/comprobaciones y posterior borrado. Notas borrables manualmente o automáticamente a 30 días. **Sí entrena con notas desidentificadas**. Residencia UE y lista pública completa de subencargados pendientes de verificación. [Seguridad](https://www.getfreed.ai/security), [privacidad](https://help.getfreed.ai/en/articles/9879953-privacy-policy-scribe-ai-chat).
- **Evidencia de evaluación:** artículo en *Plastic and Reconstructive Surgery – Global Open* (2025), con experiencia y ejemplos de errores de Freed. Se trata de una **publicación narrativa y de recomendaciones**, sin diseño de validación clínica. [Artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC11737491/).

## Proveedores adicionales del registro NHS

El [registro oficial](https://digital.nhs.uk/services/ambient-scribing/ambient-voice-technology-self-certified-supplier-registry), actualizado el **02/09/2026**, contiene **28 proveedores**. Corti, Heidi, Lyrebird, Microsoft Dragon, Tandem y Tortus forman parte del conjunto inicial; los **22 restantes** se añaden a continuación. Es **autocertificación con evidencia presentada**, no aprobación clínica general del NHS. Los expedientes aportados al Procurement Hub no son públicos; su pertenencia al registro no se usa para inferir certificados concretos.

## 21. 33n: CLEARnotes

Documentación de referencia: [producto](https://clearnotes.co.uk/product/) y [seguridad en la web](https://clearnotes.co.uk/); no se localizó Trust Center con certificados completos.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Cyber Essentials Plus | [Declaración de 33n](https://clearnotes.co.uk/) | Declara certificación; emisor, número y vigencia pendientes de verificación. |
| DCB0129 / DCB0160 / DSPT | [Seguridad](https://clearnotes.co.uk/) | Cumplimiento declarado; no certificados clínicos externos. |

**Tratamiento de datos y evaluación:** publica resultados de pilotos, pero esa página no aporta un estudio revisado por pares ni mapa completo de regiones/subencargados. [Despliegue y evaluación](https://clearnotes.co.uk/clinically-led-deployment-and-compliance-the-key-to-sustainable-ai-integration-in-the-nhs/).

## 22. Accuro: Assistant

Documentación de referencia: [Assistant](https://accuro.co.uk/accuro-assistant-the-ambient-scribe-built-for-nhs-clinicians/) y [oferta sanitaria](https://accuro.co.uk/sectors/healthcare/); no se localizó catálogo público de certificados. Es Accuro UK, distinto del EHR canadiense Accuro.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | [Assistant](https://accuro.co.uk/accuro-assistant-the-ambient-scribe-built-for-nhs-clinicians/) | Declarada para el servicio; certificado, emisor y vigencia con verificación documental pendiente. |
| Cyber Essentials Plus | [Seguridad](https://accuro.co.uk/sectors/healthcare/) | Declarada; documento no localizado. HIPAA se trata como cumplimiento legal. |

**Tratamiento de datos:** ofrece revisión por secretarios médicos en UK; no equivale a servicio sin acceso humano. Ubicaciones del procesamiento automático y subencargados completos pendientes. [Flujo del servicio](https://accuro.co.uk/sectors/healthcare/).

## 23. Accurx: Scribe

Documentación de referencia: [Trust Centre: certificados y recursos](https://trust.assuric.com/accurx/public/compliance). Publica certificados; riesgos clínicos y otros expedientes tienen acceso restringido.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001:2022 | **Amtivo / British Assessment Bureau**, 246818; [PDF](https://file.assuric.com/orgs%2Faccurx%2FcontrolEvidence%2F1Jug9FI4p8olD3SUfIcN%2FISO_27001_Certificate.pdf?alt=media&token=cd8659cf-72a1-44ce-8d27-0604bdc6f4d8) | **Documento examinado**: incluye explícitamente tecnología de voz ambiental; emitido 26/06/2026, expira **15/08/2027**. |
| Cyber Essentials / Plus | [Catálogo y PDF Plus 2025–26](https://trust.assuric.com/accurx/public/compliance) | PDFs localizados; contenido y vigencia de Plus pendientes de verificación por limitaciones de legibilidad. |
| Clase I / IIa del escriba | [Declaración de Accurx](https://support.accurx.com/en/articles/768578-privacy-information-governance-and-security-an-overview) | Anuncia ambas clases; certificado/región exactos pendientes de verificación para la oferta Accurx. |
| DTAC / DCB0129 / DSPT | [Trust Centre](https://trust.assuric.com/accurx/public/compliance) | Documentación de cumplimiento; DTAC de plataforma v8, 18/08/2026. No aprobación clínica general. |

**Tratamiento de datos y proveedores tecnológicos:** identifica **Tandem Health como subencargado del Scribe** y Azure; el audio se elimina tras transcribir. Las credenciales de Tandem deben comprobarse para la cadena contratada, no sumarse como certificados propios de Accurx. [Subencargados y descripción](https://trust.assuric.com/accurx/public).

## 24. Anathem

Documentación de referencia: [página de aseguramiento y producto sanitario](https://anathem.ai/medical-device); sin repositorio público de certificados localizado.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 / Cyber Essentials Plus | [Aseguramiento](https://anathem.ai/medical-device) | Declaradas; emisor, certificado y vigencia con verificación documental pendiente. |
| MHRA clase I | [Página con enlace al registro](https://anathem.ai/medical-device) | Declara registro de ANATHEM LTD, sistema de dictado GMDN 36216; **IIa en desarrollo**. |
| DTAC / DSPT; pentest CREST | [Aseguramiento](https://anathem.ai/medical-device) | Cumplimiento/pruebas declarados; sin verificación del informe externo. |

**Tratamiento de datos y gobernanza de IA:** declara Azure UK, eliminación a diez días configurable, sin entrenamiento con datos sensibles. Describe pruebas con transcripciones sintéticas y trazabilidad; la documentación citada no aporta una evaluación independiente del mecanismo antialucinación. [Misma documentación](https://anathem.ai/medical-device).

## 25. Anima: Annie / Ambient Scribe

Documentación de referencia: [Security & Compliance](https://www.animahealth.com/security-compliance) y [Scribe](https://www.animahealth.com/products/scribe). El dominio animaapp.com corresponde a otro producto.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Cyber Essentials / Plus | [Seguridad](https://www.animahealth.com/security-compliance) | Declara Plus, pero una FAQ de la misma página lo mantiene «en curso»; vigencia **no resuelta**. |
| MHRA clase I | [Annie](https://www.animahealth.com/products/scribe) | Declarada para el escriba; registro/certificado con verificación documental pendiente. |
| DTAC / DCB0129 / DSPT; IM1 | [Seguridad](https://www.animahealth.com/security-compliance) | Expedientes bajo solicitud; IM1 es aseguramiento de interoperabilidad NHS, HCIS sin documentación específica identificada. |

**Tratamiento de datos:** AWS Londres; DPA y DPIA específica del Scribe bajo solicitud. No se deduce la cadena de IA completa a partir del alojamiento de la plataforma. [Seguridad](https://www.animahealth.com/security-compliance).

## 26. Aprobrium: Lexacom

Documentación de referencia: [gobernanza](https://www.lexacom.co.uk/compliance-with-nhs-ai-guidance-and-assurance-standards/) y [certificaciones corporativas](https://www.lexacom.co.uk/about-lexacom/).

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 / ISO 9001 | [Página con imágenes de certificados](https://www.lexacom.co.uk/about-lexacom/) | Declara actualización agosto de 2024; contenido de las imágenes y vigencia con verificación documental pendiente. |
| Cyber Essentials Plus | [Certificaciones](https://www.lexacom.co.uk/about-lexacom/) | Declara actualización diciembre de 2024; renovación vigente pendiente de verificación. |
| MHRA clase I | [Gobernanza](https://www.lexacom.co.uk/compliance-with-nhs-ai-guidance-and-assurance-standards/) | Clase I bajo UK MDR; no certificado de evaluación externa IIa. |
| DTAC / DSPT / DCB0129; pentests CREST | [Gobernanza](https://www.lexacom.co.uk/compliance-with-nhs-ai-guidance-and-assurance-standards/) | Cumplimiento y pruebas declarados; informes con verificación documental pendiente. |

**Tratamiento de datos y gobernanza de IA:** Patient Shield elimina identificadores antes del procesamiento de IA, según proveedor; no implica por sí solo anonimización irreversible. [Gobernanza](https://www.lexacom.co.uk/compliance-with-nhs-ai-guidance-and-assurance-standards/).

## 27. Beam Up: Beam Notes / Magic Notes

Documentación de referencia: [Trust Portal](https://trust.beam.org/); políticas, informes y documentos de IA bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 / Cyber Essentials Plus | [Trust Portal](https://trust.beam.org/) | Declaradas; titularidad corporativa, certificados y vigencias con verificación documental pendiente. |
| SOC 2 | [Trust Portal](https://trust.beam.org/) | Mención e informe en catálogo; tipo, auditor y periodo pendientes de verificación. |
| CSA STAR nivel 1 / GovRAMP / IRAP | [Trust Portal](https://trust.beam.org/) | Insignias: STAR 1 es autoevaluación; estatus y evaluaciones GovRAMP/IRAP pendientes de verificación. |
| DSPT | [Registro NHS](https://www.dsptoolkit.nhs.uk/OrganisationSearch/U2A6H) | **Registro consultado**: 2025–26, estándares superados, 17/02/2026. |

**Tratamiento de datos y evaluación:** oferta UK declara tratamiento UK/EEE; Nesta publicó una evaluación de aceptación social, **no validación de exactitud clínica**. [Ficha de servicio](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717297/985901463553519-service-definition-document-2025-12-08-1626.pdf), [evaluación Nesta](https://www.nesta.org.uk/report/ai-sral-magicnotes/).

## 28. Cerebric

Documentación de referencia: [Trust Centre](https://trust.cerebric.io/public) y [catálogo de cumplimiento](https://trust.cerebric.io/public/compliance).

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Cyber Essentials / Plus | [Catálogo con PDFs](https://trust.cerebric.io/public/compliance) | Declaradas; PDF Plus localizado, contenido no extraíble. Emisor/vigencia pendientes de verificación. |
| UKCA / MHRA clase I | [Producto](https://cerebric.io/product) | Registro declarado para la plataforma; no evaluación externa IIa. |
| DTAC / DCB0129 / DSPT | [Trust Centre](https://trust.cerebric.io/public/compliance) | Catálogo de expedientes; declara DSPT con estándares superados. |

**Tratamiento de datos y gobernanza de IA:** identifica AWS y Neon; genera informes con referencias a fuentes. Regiones, retención y condiciones de entrenamiento completas pendientes de verificación. [Subencargados](https://trust.cerebric.io/public), [producto](https://cerebric.io/product).

## 29. CLAI Ltd: ClinicLetter.ai / Mayden

Documentación de referencia: [página de producto y seguridad](https://clinicletter.ai/); no se localizó Trust Center con informes descargables del escriba.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Cyber Essentials Plus | [Seguridad](https://clinicletter.ai/) | Declarada; certificado, emisor y vigencia pendientes de verificación. |
| MHRA clase I | [Producto](https://clinicletter.ai/) | Registro declarado; no evaluación externa IIa. |
| DTAC / DSPT | [Seguridad](https://clinicletter.ai/) | Cumplimiento declarado; no acreditación clínica externa. |

**Tratamiento de datos:** anuncia residencia UK y borrado de sesiones completadas; cadena de subencargados/retención residual pendiente de verificación. [Producto](https://clinicletter.ai/).

## 30. Dentistry Dashboard: AI Notes

Documentación de referencia: [Trust Pack UK](https://dentistrydashboard.com/trust-pack); certificados e informes completos bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Cyber Essentials | **IASME**, según [Trust Pack](https://dentistrydashboard.com/trust-pack) | Declara 11/09/2025, toda la organización; certificado con verificación documental pendiente. **No declara Plus propio**. |
| Pentest independiente | **Mondas Consulting**, según [Trust Pack](https://dentistrydashboard.com/trust-pack) | Retest 10/04/2026 sin hallazgos pendientes en alcance; informe con verificación documental pendiente. |
| MHRA / UK MDR clase I | [Trust Pack](https://dentistrydashboard.com/trust-pack) | Outlook Aesthetics Ltd, AI Notes, 20/09/2025; registro declarado. |
| ISO 27001 de infraestructura; DSPT/DTAC/DCB0129 | [Trust Pack](https://dentistrydashboard.com/trust-pack) | **No acredita ISO propia**: corresponde a subencargados. Documentación NHS bajo solicitud. |

**Tratamiento de datos:** AWS Londres/Azure UK South; audio transitorio, retención de notas configurable. Lista completa de subencargados bajo solicitud. [Trust Pack](https://dentistrydashboard.com/trust-pack).

## 31. Dictate IT: AVT en Swift / DIT3

Documentación de referencia: [biblioteca de seguridad](https://dictateit.com/security-and-data-protection/) con certificados públicos.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001:2022 | **Amtivo / British Assessment Bureau**, 186273; [PDF](https://dictateit.com/wp-content/uploads/2025/04/Dictate.IT-ISO-27001-Certificate.pdf) | **Documento examinado**: dictado, transcripción y reconocimiento de voz sanitario; expira **16/04/2027**. |
| ISO 9001:2015 | **Amtivo / British Assessment Bureau**, 185884; [PDF](https://dictateit.com/wp-content/uploads/2025/04/Dictate-IT-ISO-9001-Certificate.pdf) | **Documento examinado**: mismo ámbito; expira **14/04/2027**. |
| Cyber Essentials Plus | [PDF publicado](https://dictateit.com/wp-content/uploads/2024/09/Dictate-IT-Cyber-Essentials-Plus-Certificate.pdf) | **Documento examinado, vencido 12/07/2025**; excluye sistemas heredados en red separada. Renovación actual pendiente de verificación. |
| MHRA clase I; DTAC/DCB0129/DSPT | [Declaración AVT](https://dictateit.com/wp-content/uploads/2025/09/Dictate-IT-NHS-AVT-standards-compliance-summary.pdf) | Declarados para AVT en Swift/DIT3; no certificado clínico externo. |

**Tratamiento de datos:** declara almacenamiento/procesamiento UK, sin proveedores externos de IA; pentest anual NCC Group. Es declaración de julio de 2025, no auditoría actual de toda la arquitectura. [Documento AVT](https://dictateit.com/wp-content/uploads/2025/09/Dictate-IT-NHS-AVT-standards-compliance-summary.pdf).

## 32. Docwise

Documentación de referencia: [Compliance](https://www.docwise.co.uk/compliance): enlaces a registros; DTAC/DCB0129 bajo solicitud. El análisis corresponde al escriba de docwise.co.uk; excluye empresas homónimas de gestión documental.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Cyber Essentials | [Compliance, enlace a registro](https://www.docwise.co.uk/compliance) | Declarada; certificado, emisor y vigencia con verificación documental pendiente. |
| UKCA / MHRA clase I | [Compliance](https://www.docwise.co.uk/compliance) | Marcado/registro declarados; no evaluación externa IIa. |
| DTAC / DCB0129 / DSPT | [Compliance](https://www.docwise.co.uk/compliance) | Declara DSPT «standards met»; documentos clínicos bajo solicitud. |

**Tratamiento de datos y evaluación:** declara servidores UK; lista completa de subencargados pendiente de verificación. La web presenta resultados de piloto sin referencia bibliográfica que permita verificar la revisión por pares. [Seguridad](https://www.docwise.co.uk/compliance), [piloto](https://www.docwise.co.uk/).

## 33. eConsult: Hi Scribe

Documentación de referencia: [seguridad corporativa](https://econsult.net/primary-care/security) y [política específica Hi Scribe](https://econsult.net/hi-scribe-privacy-policy).

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | **Alcumus ISOQAR**, según [declaración 2024](https://info.econsult.health/hubfs/eConsult%20Health%20-%20GDPR%20and%20Data%20Protection%20and%20Information%20Security%20Compliance%20Statement%20-%202024.pdf) | Certificado corporativo 20623 citado; vigencia actual y alcance explícito Hi Scribe pendientes de verificación. |
| DSPT | [Política Hi Scribe](https://econsult.net/hi-scribe-privacy-policy) | Declara estándares superados; no certificación clínica. |

**Tratamiento de datos:** política marzo de 2026: Google Speech-to-Text y AWS Comprehend en UK; Vertex AI en UE; CloudWatch/Datadog para metadatos. Audio no almacenado, texto en sesión; feedback voluntario hasta dos semanas. [Mapa y retención](https://econsult.net/hi-scribe-privacy-policy).

## 34. Epro: Bluewire Technologies

Documentación de referencia: [anuncio ISO](https://epro.com/blog/epro-has-been-awarded-with-the-iso27001-accreditation-the-internationally-recognised-standard-for-information-security-management-system/), [producto](https://epro.com/) y política; no se localizó Trust Center de certificados completos.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | [Anuncio, 24/10/2025](https://epro.com/blog/epro-has-been-awarded-with-the-iso27001-accreditation-the-internationally-recognised-standard-for-information-security-management-system/) | Declarada; emisor, número, alcance y vigencia pendientes de verificación. |
| ISO 9001 | [Declaración corporativa](https://www.linkedin.com/company/epro_health/) | Declarada por Epro; certificado con verificación documental pendiente. |
| MHRA clase I / DCB0129 | [Producto](https://epro.com/) | Conformidad declarada; no evaluación externa IIa. |

**Tratamiento de datos:** alojamiento cloud anunciado; la política web no basta para establecer países, retención y subencargados del AVT. [Política](https://epro.com/product/ai-speech/policy).

## 35. G2 Speech: SpeechAmbient

Documentación de referencia: [Security & Compliance](https://www.g2speech.com/security); no se localizó repositorio público de certificados completos.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 / ISO 27701 | [Seguridad](https://www.g2speech.com/security) | Declaradas; certificado, emisor y vigencia con verificación documental pendiente. |
| NEN 7510 / Cyber Essentials Plus | [Seguridad](https://www.g2speech.com/security) | Declaradas; alcance concreto de SpeechAmbient pendiente. |
| MHRA clase I | [Seguridad](https://www.g2speech.com/security) | Registro declarado; no evaluación externa IIa. |
| DCB0129 / DSPT / DTAC | [Seguridad](https://www.g2speech.com/security) | Cumplimiento; no certificaciones clínicas independientes. |

**Tratamiento de datos:** declara alojamiento UK o UE, sin conservar audio y acceso de soporte solicitado por el cliente. Región concreta y lista completa de subencargados pendientes. [Seguridad](https://www.g2speech.com/security).

## 36. HealthOrbit AI

Documentación de referencia: [Trust Center](https://healthorbit.ai/trust-center/): expediente completo, DPA, DPIA y riesgos clínicos bajo solicitud.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 / SOC 2 tipo II | [Trust Center](https://healthorbit.ai/trust-center/) | Declaradas; emisor, alcance y vigencia/periodo con verificación documental pendiente. |
| Cyber Essentials / Plus | [Trust Center](https://healthorbit.ai/trust-center/) | Insignias publicadas; certificados con verificación documental pendiente. |
| Dubai AI Seal | **DCAI**, según [anuncio](https://healthorbit.ai/news/healthorbit-ai-officially-recognised-with-dubai-ai-seal/) | Anunciado 07/11/2025; número/categoría oficial pendientes de verificación. No certificación médica. |
| UKCA / MOHAP | [Trust Center](https://healthorbit.ai/trust-center/) | Logotipos sin documento, clase o autorización identificados; no se cuentan como aprobaciones verificadas. MOHAP es el Ministerio de Salud y Prevención de EAU, no el nombre de una certificación. |
| DTAC / DCB0129 / DSPT | [Trust Center](https://healthorbit.ai/trust-center/) | Cumplimiento declarado; FAQ aún describe DTAC completo en preparación. |

**Tratamiento de datos:** identifica AWS y Google Workspace, pero la lista completa requiere solicitud. No verificada residencia íntegra UE. [Subencargados](https://healthorbit.ai/trust-center/).

## 37. Medhasyn Ltd: Clinical Companion

Documentación de referencia: [sitio oficial](https://www.medhasyn.com/) y [registro NHS](https://digital.nhs.uk/services/ambient-scribing/ambient-voice-technology-self-certified-supplier-registry).

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Certificación externa del escriba | [Web](https://www.medhasyn.com/) | **No localizada**: información pública limitada, sin certificados, informes ni Trust Center identificable. |
| Registro AVT NHS | [NHS](https://digital.nhs.uk/services/ambient-scribing/ambient-voice-technology-self-certified-supplier-registry) | Pertenencia verificada; expediente no público, no permite inferir ISO/CE/otros. |

**Tratamiento de datos:** alude a flujos locales cuando se necesitan; no demuestra una configuración contratada, regiones, subencargados o retención. [Web](https://www.medhasyn.com/).

## 38. Optum: EMIS Scribe

Documentación de referencia: [producto](https://www.emishealth.com/news-insights/march-2026-newsletter) y [condiciones/subencargados](https://www.emishealth.com/terms-conditions); no se localizó expediente público de certificación específico del Scribe.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| Certificaciones propias del Scribe | [Condiciones](https://www.emishealth.com/terms-conditions) | **No verificadas**. No se trasladan las credenciales de otros productos de Optum ni las del proveedor T-Pro. |
| Registro AVT NHS | [NHS](https://digital.nhs.uk/services/ambient-scribing/ambient-voice-technology-self-certified-supplier-registry) | Pertenencia verificada; no certificación independiente del producto. |

**Tratamiento de datos y proveedores tecnológicos:** **T-Pro aporta la IA de EMIS Scribe**; la tabla contractual indica que ese servicio no procesa fuera de UK. No localizados plazos de retención ni mapa técnico completo del escriba. [Subencargados](https://www.emishealth.com/terms-conditions).

## 39. Pungo: Joy / JoyNotes

Documentación de referencia: [Trust Centre](https://trust.assuric.com/the-joy-app/public/compliance): ISO público, expedientes DCB/DTAC/DPA con acceso restringido.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001:2022 | **Citation ISO Certification**, 363532021; [PDF](https://file.assuric.com/orgs%2Fthe-joy-app%2FcontrolEvidence%2F22pghJ4mEH7v7DPByRHz%2FISO%2027001%20_%202022%20Certificate.pdf?alt=media&token=bbae1827-a31f-48e6-ac52-fd720c6b4fc3) | **Documento examinado**: software de prescripción social; expira **05/01/2027**. JoyNotes no nombrado expresamente. |
| Cyber Essentials / Plus | [Catálogo](https://trust.assuric.com/the-joy-app/public/compliance) | CE público localizado; contenido no legible. Plus figuraba en una versión indexada anterior; vigencia actual pendiente de verificación. |
| MHRA clase I: JoyNotes | [Catálogo con enlace MHRA](https://trust.assuric.com/the-joy-app/public/compliance) | Registro declarado; declaración de conformidad con verificación documental pendiente. |
| DTAC / DCB0129 / DSPT | [Trust Centre](https://trust.assuric.com/the-joy-app/public/compliance) | Recursos específicos JoyNotes; no certificación clínica externa. |

**Tratamiento de datos:** DPA y DPIA identificados en catálogo, con verificación íntegra pendiente; regiones, subencargados y entrenamiento del escriba pendientes. [Recursos](https://trust.assuric.com/the-joy-app/public/compliance).

## 40. Scribetech: Augnito Omni

Documentación de referencia: [aseguramiento Omni](https://scribetech.co.uk/press-releases/nhs-ready-ai-medical-scribe-augnito-omni-ai-among-first-to-fully-meet-new-nhs-england-ambient-voice-tech-guidelines) y documentación corporativa; sin Trust Center de certificados completos localizado.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | **BSI**, según [documentación Scribetech](https://scribetech.co.uk/wp-content/uploads/2022/11/ProductComparison.pdf) | Declarada; certificado/vigencia actuales y alcance exacto Omni con verificación documental pendiente. |
| ISO 9001 / ISO 14001 / Cyber Essentials Plus | [Anuncio Omni, 26/07/2025](https://scribetech.co.uk/press-releases/nhs-ready-ai-medical-scribe-augnito-omni-ai-among-first-to-fully-meet-new-nhs-england-ambient-voice-tech-guidelines) | Declaradas para la plataforma; certificados y vigencias con verificación documental pendiente. |
| SOC 2 | [Artículo corporativo 2023](https://scribetech.co.uk/blog/2023/06/26/the-realities-of-successfully-integrating-natural-speech-recognition-into-mental-health-services) | Menciona conformidad; tipo, auditor y cobertura Omni no demostrados. |
| UKCA / MHRA clase I; DCB0129/DCB0160/DSPT | [Anuncio Omni](https://scribetech.co.uk/press-releases/nhs-ready-ai-medical-scribe-augnito-omni-ai-among-first-to-fully-meet-new-nhs-england-ambient-voice-tech-guidelines) | Registro/cumplimiento declarados; **IIa era objetivo**, no credencial obtenida en esa fuente. |

**Tratamiento de datos:** declara procesamiento UK y retención opcional dentro del país; entrenamiento previo con datos clínicos UK no aclara reutilización contractual de nuevas consultas. [Omni](https://scribetech.co.uk/press-releases/nhs-ready-ai-medical-scribe-augnito-omni-ai-among-first-to-fully-meet-new-nhs-england-ambient-voice-tech-guidelines).

## 41. T-Pro: Scribe / Copilot

El [Trust Center](https://trust.tpro.io/) presentó limitaciones de acceso al contenido. Fuentes alternativas: [ficha G-Cloud](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/310198615907338) y [declaración AVT](https://info.tpro.io/hubfs/T-Pro%20Scribe%20with%20Compliance%20with%20NHS%20England%20AVT%20Requirements.pdf?hsLang=en).

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 27001 | **SGS UK**, según [ficha presentada por T-Pro](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/310198615907338) | Fecha citada 07/11/2022; dictado/transcripción/correspondencia. Verificación del certificado vigente pendiente. |
| Cyber Essentials Plus | [Declaración AVT, 18/06/2025](https://info.tpro.io/hubfs/T-Pro%20Scribe%20with%20Compliance%20with%20NHS%20England%20AVT%20Requirements.pdf?hsLang=en) | Renovación anual declarada; documento/auditor pendientes de verificación. |
| ISO 13485 / ISO 14971 | [Comunicación de T-Pro](https://www.linkedin.com/posts/tpro_healthcareai-ambientvoicetechnology-clinicaldocumentation-activity-7467515379280457728-9-we) | Referencias a estándares; **certificación externa no demostrada** en las fuentes consultadas. |
| MHRA clase I; DTAC/DCB0129/DSPT | [Declaración AVT](https://info.tpro.io/hubfs/T-Pro%20Scribe%20with%20Compliance%20with%20NHS%20England%20AVT%20Requirements.pdf?hsLang=en) | En junio de 2025 el registro médico estaba **en curso**; estado posterior pendiente de verificación. Cumplimiento NHS declarado. |

**Tratamiento de datos:** DPIA y flujos por cliente; el documento no permite establecer residencia UE y cadena completa para España. La ISO 9001 de material de **InventAsia** no se atribuye automáticamente a T-Pro Scribe. [AVT](https://info.tpro.io/hubfs/T-Pro%20Scribe%20with%20Compliance%20with%20NHS%20England%20AVT%20Requirements.pdf?hsLang=en), [alcance InventAsia](https://info.tpro.io/hubfs/PDFs/T-Pro%20Compliance%20-%20Invent%20Asia.pdf?hsLang=en).

## 42. X-on Health: Surgery Intellect, powered by TORTUS

Documentación de referencia: [Trust Centre](https://www.x-on.co.uk/trust-centre/) y [Academy: documentos](https://surgeryconnect.academy/trust-centre/). Certificados públicos; parte del expediente clínico requiere autenticación.

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| ISO 9001:2015 | **Citation**, 136442021; [PDF](https://surgeryconnect.academy/wp-content/uploads/2026/05/ISO-9001_2015-Certificate.pdf) | **Documento examinado**: navegación asistencial y soluciones digitales sanitarias; expira **02/08/2027**. |
| ISO 22301:2019 | **Citation**, 427522023; [PDF](https://surgeryconnect.academy/wp-content/uploads/2026/05/ISO-22301_2019-Certificate.pdf) | **Documento examinado**, mismo ámbito; expira **13/09/2027**. |
| ISO 14001:2015 | **Citation**, 429932023; [PDF](https://surgeryconnect.academy/wp-content/uploads/2026/05/ISO-14001_2015-Certificate.pdf) | **Documento examinado**, mismo ámbito; expira **17/10/2027**. |
| ISO 27001 / ISO 42001 | [27001](https://surgeryconnect.academy/wp-content/uploads/2026/07/ISO27001-Certificate.pdf), [42001](https://surgeryconnect.academy/wp-content/uploads/2026/08/ISO42001-Certificate.pdf) | Certificados públicos localizados; sin extracción legible. Emisor, alcance y vigencia pendientes de verificación. |
| Cyber Essentials / Plus | [Academy](https://surgeryconnect.academy/trust-centre/) | Declara Plus; enlaza documento titulado CE octubre 2025–octubre 2026, con verificación íntegra pendiente. |
| UKCA clase IIa: tecnología TORTUS | [Surgery Intellect](https://www.x-on.co.uk/surgery-intellect/) | Declaración explícita de la tecnología incorporada; sin verificación de un certificado independiente de X-on. |
| DTAC / DCB0129 / DSPT | [Trust Centre](https://www.x-on.co.uk/trust-centre/) | Expedientes por producto; cumplimiento, no certificación clínica externa. |

**Tratamiento de datos:** política corporativa declara UK con excepciones contractuales; para el escriba es necesario el expediente **X-on + TORTUS**, no solo el de telefonía. [Privacidad](https://www.x-on.co.uk/privacy-notice/), [DPIA y cadena del producto](https://surgeryconnect.academy/trust-centre/).

## 43. AWS: HealthScribe

**Revisión específica: 17/09/2026.** API gestionada para construir aplicaciones clínicas: transcripción y borradores de notas, por lotes o streaming. **Solo inglés de EE. UU. y región US East (N. Virginia)** según la guía; sin conector HCIS identificado. [Producto](https://aws.amazon.com/es/healthscribe/), [documentación técnica](https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html).

**Interpretación del alcance:** AWS presenta HealthScribe dentro de Amazon Transcribe. Sus catálogos incluyen Transcribe y extienden la cobertura a funciones de disponibilidad general, salvo exclusión, con evaluación en la siguiente oportunidad de auditoría. La aplicación a HealthScribe se infiere de esa regla cuando no se nombra expresamente; **no demuestra certificación de la aplicación de un partner** ni revisión de cada versión posterior. [Regla y alcance ENS](https://aws.amazon.com/compliance/services-in-scope/ENS-High/).

| Credencial | Emisor / documento | Alcance, vigencia y evidencia |
| --- | --- | --- |
| **ISO 27001:2022** | **EY CertifyPoint**, 2013-009; [certificado público, 7 páginas](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/certification/compliance/iso_27001_global_certification.pdf) | **Documento examinado**: emitido 25/11/2025, reexpedido 24/08/2026; expira 30/11/2028. Su p. 2 remite al catálogo de servicios, que incluye Transcribe; p. 4 incluye Virginia. |
| **ENS ALTA** | [Catálogo AWS de servicios en alcance](https://aws.amazon.com/compliance/services-in-scope/ENS-High/) | Transcribe figura incluido. Cobertura de HealthScribe inferida según la regla anterior; **certificado completo, emisor, vigencia y anexos pendientes de examen** mediante AWS Artifact. No se clasifica como ENS ausente ni como expediente íntegramente verificado. |
| **SOC 1 / 2 / 3** | **Ernst & Young LLP** para el [SOC 3 público](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/whitepapers/compliance/AWS_SOC3_Report.pdf); [catálogo SOC](https://aws.amazon.com/compliance/services-in-scope/SOC/) | **SOC 3 examinado**, periodo 01/04/2025–31/03/2026, firmado 29/05/2026; Transcribe en p. 7. El auditor excluye expresamente evaluar el rendimiento/integridad de la IA. SOC 1/2: informes restringidos, no examinados. |
| ISO 27017 / 27018 / 27701; 9001 / 22301 / 20000-1; CSA STAR | [Catálogo ISO de AWS](https://aws.amazon.com/compliance/iso-certified/) | Certificaciones declaradas y Transcribe incluido; documentos individuales y alcance detallado pendientes. No se atribuye a todos el emisor o vigencia del certificado 27001. |
| **ISO 42001:2023** | **Schellman Compliance LLC**, según [anuncio AWS](https://aws.amazon.com/blogs/machine-learning/aws-achieves-iso-iec-420012023-artificial-intelligence-management-system-accredited-certification/); [acceso al certificado](https://aws.amazon.com/compliance/iso-42001-faqs/) | Anuncio de 2024 incluye Transcribe. Certificado vigente y anexos no examinados; gestión de IA, no validación clínica de HealthScribe. |
| C5 / HITRUST CSF | [Alcance C5](https://aws.amazon.com/compliance/services-in-scope/C5/), [alcance HITRUST](https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/) | Transcribe incluido en ambos catálogos. Informes/certificados completos, periodos y modalidad HITRUST pendientes; sin atribuir tipo C5 específico. |
| HIPAA: elegibilidad | [Listado AWS](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/) | Mención explícita a Transcribe **incluido HealthScribe**. Requiere BAA y configuración adecuada; **no es certificación externa HIPAA**. |

**Datos y privacidad:** AWS declara no entrenar con entradas/salidas ni retenerlas tras entregar resultados; las copias en S3 quedan bajo gestión del cliente. DPA y lista de subencargados públicos, sin mapa específico completo de HealthScribe identificado. La disponibilidad en Virginia **no acredita residencia UE**; almacenar la salida en otro lugar tampoco cambia dónde se procesa. Los términos contemplan inferencia entre regiones para servicios basados en Bedrock, incluido HealthScribe: requiere aclaración contractual del flujo efectivo. [FAQ](https://aws.amazon.com/healthscribe/faqs/), [DPA](https://d1.awsstatic.com/legal/aws-dpa/aws-dpa.pdf), [subencargados](https://aws.amazon.com/compliance/sub-processors/), [términos §§1.24 y 50.3](https://aws.amazon.com/service-terms/).

**Calidad y seguridad clínica:** la AI Service Card, aplicable a la versión de **28/11/2023**, publica evaluación propia: F1 de reconocimiento de palabras ≥84% en 28 grupos y F1 de resumen 72% en conversaciones guionizadas. No son porcentajes de notas clínicamente correctas ni resultados en español. Incluye vínculos de las notas a la transcripción y sus limitaciones. No se localizó validación clínica específica revisada por pares en la búsqueda dirigida. [Service Card](https://docs.aws.amazon.com/ai/responsible-ai/aws-healthscribe/overview.html).

**Partners:** AWS identifica **3M HIS/Solventum, Netsmart, ScribeEMR, TeleTracking y Pariveda**. Netsmart documenta **Bells Virtual Scribe con HealthScribe**; las otras referencias combinan productos, colaboraciones y desarrollo a medida. La relación con 3M no demuestra que Fluency Align España utilice esta API. [Clientes AWS](https://aws.amazon.com/healthscribe/customers/), [implementación Netsmart](https://aws.amazon.com/blogs/industries/netsmart-transforms-behavioral-healthcare-with-new-feature-of-aws-healthscribe/). El detalle comercial y las páginas revisadas constan en la [nota de revisión AWS](additional/aws-healthscribe.md).

**Distinción necesaria:** [Amazon Transcribe Medical](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-medical.html) ofrece transcripción médica, también limitada a inglés de EE. UU.; no sustituye la generación de notas de HealthScribe. Las garantías de una aplicación terminada requieren evaluar además al integrador. **Sin inclusión en la selección corta actual:** español, procesamiento UE e integración HCIS no acreditados.
