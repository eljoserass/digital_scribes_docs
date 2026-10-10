# Qué es una nota clínica

La nota documenta el encuentro para comunicar hallazgos, razonamiento, decisiones y seguimiento. Su contenido puede venir de conversación, exploración e historia previa. **El origen y la fecha de cada dato importan.** [Colicchio et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/).

## SOAP como ejemplo de organización

| Parte | Qué recoge | De dónde puede venir |
| --- | --- | --- |
| **S — Subjective** | Motivo de consulta, síntomas, evolución e historia referida. | Paciente o acompañante; antecedentes relevantes, indicando su origen. |
| **O — Objective** | Hallazgos de exploración, constantes y resultados. | Observaciones del profesional y registros clínicos; distinguir actuales y previos. |
| **A — Assessment** | Valoración, problemas e interpretación clínica. | Juicio del profesional; conservar incertidumbre y alternativas. |
| **P — Plan** | Tratamiento, pruebas, recomendaciones y seguimiento. | Decisiones comunicadas o documentadas por el profesional. |

Base: [SOAP Notes — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK482263/), consultado mediante tu copia de Zotero. Los orígenes son una aplicación al diseño del escriba. Para nuestro borrador, valoración y plan deben reflejar lo expresado o documentado por el clínico.

## Contenido que conviene conservar

- **Quién, qué y cuándo:** paciente o familiar, problema actual o antecedente, hecho confirmado o sospecha.
- **Relaciones:** medicamento con dosis/frecuencia; intervención con motivo; prueba solicitada frente a realizada.
- **Razonamiento:** por qué se considera un diagnóstico o se decide una actuación.
- **Selección:** suficiente información para entender el encuentro, evitando arrastrar texto antiguo o redundante.

[Anatomy](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/) analiza HPI e impresión/plan de **80 notas**: identifica contenido clínico, temporal, razones y participantes, con formatos narrativos y listas. Esa muestra ayuda a caracterizar la salida; no define una plantilla universal.

## La nota dentro del EHR

- El documento puede mezclar texto libre, plantillas y campos estructurados; escribirlo requiere conocer el flujo del servicio.
- El profesional revisa y corrige el borrador. La coordinación, formación y feedback también afectan a su calidad.
- Para nuestro sistema: diferenciar dato recuperado, texto generado y corrección del clínico; registrar quién aprobó la nota.

Los dos primeros puntos se apoyan en [Safe use of the EHR — Ash et al.](https://doi.org/10.1093/jamia/ocaa199), un estudio cualitativo de **escribas humanos** en 12 centros de cinco organizaciones. El tercero es una decisión de diseño, apoyada en [FHIR Provenance](https://hl7.org/fhir/R4/provenance.html).

## Lecturas para ampliar

- [Singh et al., 2023](https://aclanthology.org/2023.clinicalnlp-1.18/) — Puente hacia generación: contexto disperso, lenguaje informal y estilo según especialidad/profesional.
- [Communication in Medical Care](https://doi.org/10.1017/CBO9780511607172) / [RIAS](https://doi.org/10.1016/S0738-3991(02)00012-5) — Ayudan a entender las funciones del diálogo del que seleccionaremos información.
- [Taking note](https://pmc.ncbi.nlm.nih.gov/articles/PMC6694617/) — Cómo se incorpora la escritura de notas al trabajo de un equipo de primaria.
- [Moramarco et al.](https://aclanthology.org/2022.acl-long.394/) — Evaluar contenido y edición cuando varias redacciones pueden ser aceptables.
