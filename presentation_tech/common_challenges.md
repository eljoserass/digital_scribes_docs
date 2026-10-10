# Common challenges — escribas médicos

Dificultades habituales de la pipeline. Los ejemplos son ilustrativos; las fuentes explican el problema o cómo evaluarlo.

| Reto | Qué complica la tarea | Fuente |
| --- | --- | --- |
| Captura real | Ruido, distancia al micrófono y canales distintos alteran lo que llega al ASR. | [PriMock57](https://arxiv.org/abs/2204.00333) |
| Quién habla | Solapamientos y habla no detectada; separar voces tampoco identifica automáticamente al médico, paciente o acompañante. | [Benchmarking Diarization Models](https://arxiv.org/abs/2509.26177) |
| Lenguaje coloquial y vocabulario médico | Convertir expresiones del paciente a redacción clínica conservando significado; reconocer términos poco frecuentes. | [Singh et al.](https://aclanthology.org/2023.clinicalnlp-1.18/) |
| Conversaciones largas | Un dato y su aclaración pueden estar muy separados; el diálogo vuelve sobre temas y corrige afirmaciones previas. | [Singh et al.](https://aclanthology.org/2023.clinicalnlp-1.18/) |
| Información que no se oye | Gestos, exploración y referencias como «me duele aquí» requieren observaciones o contexto adicional. | [Singh et al.](https://aclanthology.org/2023.clinicalnlp-1.18/) |
| Seleccionar lo relevante | La nota reorganiza información dispersa; hay que comprimir repeticiones conservando los hechos necesarios. | [CLUSTER2SENT](https://aclanthology.org/2021.acl-long.384/) |
| Negación y detalles clínicos | «No toma», «tomaba» y «tomará» cambian el hecho; fármaco, dosis y frecuencia necesitan conservarse juntos. | [Dr. Summarize](https://aclanthology.org/2020.findings-emnlp.335/), [Anatomy](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/) |
| Omisiones y contenido sin respaldo | Una nota fluida puede olvidar datos o añadir afirmaciones; comparar con diálogo y referencia ayuda a distinguir ambos fallos. | [Robustness of SOAP generation](https://proceedings.mlr.press/v333/latif26a.html) |
| Incorporar la historia | Comprobar fecha y respaldo del contexto; una ausencia en el EHR no demuestra que lo dicho sea falso. | [VeriFact](https://arxiv.org/abs/2501.16672) |
| Formato y estilo | Especialidad y profesional cambian la organización de la nota; una plantilla única puede ser insuficiente. | [Anatomy](https://pmc.ncbi.nlm.nih.gov/articles/PMC8075472/), [Singh et al.](https://aclanthology.org/2023.clinicalnlp-1.18/) |
| Datos representativos | Inglés, habla leída y audio TTS cubren escenarios diferentes del español espontáneo de nuestra consulta. | [TEME: corpus y experimento](https://doi.org/10.65109/RHNT7438), [PriMock57](https://arxiv.org/abs/2204.00333) |
| Medir utilidad | Similitud textual, errores clínicos y tiempo de edición responden a preguntas diferentes. | [Moramarco et al.](https://aclanthology.org/2022.acl-long.394/) |
| Revisión e integración | Entregar el borrador dentro del EHR, facilitar correcciones y dejar claras las responsabilidades del equipo. | [Safe use of the EHR](https://doi.org/10.1093/jamia/ocaa199) |
| Ejecución y datos | Latencia, hardware, continuidad de captura y qué audio/texto se transmite o conserva forman parte del diseño. | [ASR survey](https://arxiv.org/abs/2303.03329), [guía NHS](https://www.england.nhs.uk/long-read/ai-enabled-ambient-scribing-products-in-health-and-care-settings/) |

Para empezar: **Singh** para diálogo→nota, **Moramarco** para evaluación y **Safe use of the EHR** para el trabajo del equipo. Este último estudia escribas humanos; sus hallazgos organizativos sirven como contexto, sin validar modelos de IA.

Ver también [qué es una nota clínica](clinical_note_context.md) y el [catálogo técnico](README.md).
