# SCRIBE: el marco de evaluación de Wang et al.

[An evaluation framework for ambient digital scribing tools in clinical applications](https://doi.org/10.1038/s41746-025-01622-1), **Wang et al., npj Digital Medicine, 2025**. Esta es la referencia de la figura 1 que usamos en la presentación; no es Robust SOAP de Latif et al.

- **Figura 1(a):** conecta transcripción, atribución de hablantes y generación con la evaluación de cada etapa y de la nota. Añade simulaciones para observar propagación de errores, robustez y sesgos.
- **Figura 1(b):** compara evaluación humana, métricas automáticas y jueces LLM. El Venn es una síntesis conceptual; sus etiquetas no demuestran capacidad ni fiabilidad universal del juez.
- **Datos:** 40 grabaciones reales de consultas prenatales, de 6–35 minutos, media de 16,7 minutos. Los datos originales no son públicos por privacidad; los autores enlazan [simulaciones y estadísticas](https://github.com/AutoEvaluation/ADS_evaluation).
- **Hablantes:** transcriben con Whisper y atribuyen hablantes sobre el texto usando LLM. Lo denominan diarización, pero no es un diarizador acústico que agrupa embeddings de voz. También simulan distorsiones de atribución. No decir que ignoran la diarización.
- **Evaluación:** combinan revisión clínica, métricas y jueces; estudian calibrar métricas con puntuaciones humanas. Un evaluador calibrado necesita validación separada si queremos medir generalización.
- **Límites:** muestra pequeña y específica; los autores reconocen posible sesgo porque algunas referencias parten de salidas GPT corregidas. No trasladar sus resultados a nuestro hospital ni asumir que reproducimos el stack completo.

## Qué tomaríamos para nuestro proyecto

La lógica de evaluar componentes y nota completa, contrastar jueces con médicos y simular errores. Usaríamos nuestras referencias españolas y mediríamos ejecución local, tiempo, memoria y esfuerzo de revisión. Incorporar historia longitudinal añade otra entrada y otros errores; debe evaluarse explícitamente.

**Leer primero:** figura 1 y Methods: desarrollo del ADS, marco SCRIBE y métodos de evaluación. Después simulaciones y limitaciones. En el guion, recorrer el panel (a) sin leer todas sus celdas; dedicar unos 35 segundos al mensaje de (b).
