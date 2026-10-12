# Recursos locales: cálculo de RAM y almacenamiento

12/10/2026 · Apoyo para la slide 26. **Estimación de planificación**, sin benchmark de velocidad ni ejecución de un modelo nuevo en esta revisión.

## Lo que cabe en disco: aproximadamente 1–2 GB de modelos

Configuración del ejemplo: MOSS 0.9B para transcripción/hablantes y Qwen3-0.6B para nota. Suman aproximadamente **1,5 mil millones de parámetros**.

```text
Tamaño nominal de pesos ≈ parámetros × bits por peso / 8

1,5B × 4 bits / 8 ≈0,75 GB
1,5B × 8 bits / 8 ≈1,50 GB
```

Los archivos reales añaden metadatos, escalas de cuantización y tensores que conservan más precisión. Por eso mostramos **≈1–2 GB de archivos de modelos**, como orden de magnitud para cuantización de 4–8 bits.

Un punto de referencia concreto: el port de MOSS publica un GGUF Q8_0 de ≈987 MB; el GGUF oficial Qwen Q8_0 ocupa ≈639 MB. Juntos: **≈1,63 GB**, antes de bibliotecas, entorno, audio y datos. [MOSS/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/moss-transcribe-diarize.md#download) · [Qwen GGUF oficial](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/tree/main).

**Cuantizar** representa pesos con menos bits. Reduce archivos y memoria de pesos; no reduce automáticamente el KV cache ni elimina la memoria de trabajo. La calidad tras cuantizar también se evalúa. `llama.cpp` es un motor que usa GGUF; GGUF es un formato, no una técnica única de cuantización. [llama.cpp](https://github.com/ggml-org/llama.cpp).

## Lo que ocupa al ejecutar: aproximadamente 4–8 GB

Supuestos: motores C++/GGUF, MOSS y Qwen Q8_0, audio de **15–30 min**, contexto del generador de **4–8k tokens**, cache de Qwen FP16 y un usuario.

| Parte | Orden de magnitud |
|---|---:|
| Pesos de ambos modelos | ≈1,63 GB |
| Estado adicional de MOSS | ≈1,28–2,55 GB |
| KV cache de Qwen | ≈0,47–0,94 GB |
| Subtotal calculable | ≈3,37–5,12 GB |
| Con buffers, activaciones y margen del motor | **≈4–8 GB para procesos**, estimado |

Para MOSS, el port propone ≈85 MB adicionales por minuto de audio; es una aproximación de esa implementación. Para Qwen, su configuración da 28 capas, 8 cabezas KV y dimensión 128. La cache FP16 usa `28 × 2(K,V) × 8 × 128 × 2 bytes =114.688 bytes/token`: ≈0,47/0,94 GB para 4.096/8.192 tokens. [Memoria de MOSS](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/moss-transcribe-diarize.md#memory-and-length) · [Configuración oficial Qwen](https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json).

**Cómo salió el rango de la slide:** ≈1,63 GB de pesos + ≈1,28–2,55 GB de estado acústico + ≈0,47–0,94 GB de caché = ≈3,37–5,12 GB. Redondeamos a 4–8 GB al reservar memoria de trabajo. Ese margen es una decisión conservadora de planificación, no una cifra publicada ni medida. Supone ambos modelos residentes; liberarlos entre etapas puede reducir el pico. La alternativa LiteRT-LM se investigó por separado y no es el origen de este rango.

Los GB son decimales. **4 y 8 GB no son mínimos/máximos universales**: el rango redondea un cálculo bajo estas hipótesis. Contexto más largo, FP32, otra implementación o concurrencia pueden necesitar más. Una consulta de 30 min con historia puede superar 8k tokens. El presupuesto tampoco incluye toda la RAM del sistema, HCIS y otras aplicaciones. Falta medir el máximo real.

**¿Qué eran los buffers?** Espacios de memoria que el motor reserva para cálculos intermedios: ventanas de audio, activaciones entre capas o resultados temporales de operaciones. Son la mesa de trabajo del modelo; los pesos son sus parámetros. La KV cache conserva claves/valores de atención para reutilizarlos al generar. El motor puede reutilizar espacios temporales, y su tamaño depende de la entrada y la implementación. En la slide usamos **«memoria de trabajo»**.

## Qué ocupa una alternativa con un motor especializado

Google publica estos tamaños para **LiteRT-LM**. Consulta del 12/10/2026; documentación actualizada el 06/10/2026:

| Modelo distribuido para LiteRT-LM | Archivo de modelo | Memoria publicada |
|---|---:|---|
| Qwen3-0.6B | **586 MB** | La tabla de ese modelo no da RAM máxima. |
| Gemma3-1B | **1.005 MB** | La tabla de ese modelo no da RAM máxima. |
| Gemma4-E2B | **2.583 MB** | **1.733 MB de «Peak CPU Memory»** en Samsung S26 Ultra, backend CPU; **3.505 MB** en Windows/Intel Lunar Lake, backend CPU. |

[Tabla y condiciones oficiales de Google](https://developers.google.com/edge/litert-lm/overview). Esa métrica de memoria CPU tiene un alcance específico: no la tratamos como toda la RAM del dispositivo o del escriba. La página no detalla suficientemente la contabilidad para deducir por qué algunos valores son menores que el archivo. Tampoco fija todos los supuestos de longitud del contexto que necesitaríamos para trasladarlos a una consulta.

El Qwen de **586 MB** muestra una distribución compacta del mismo tamaño de modelo del ejemplo. El GGUF Q8_0 citado arriba ocupa ≈639 MB: son formatos/configuraciones diferentes, **no una comparación controlada entre motores**. LiteRT-LM puede ser un candidato para probar, pero esos datos no permiten reemplazar nuestro presupuesto de 4–8 GB por una cifra medida en otro modelo/dispositivo. Hay que sumar MOSS, contexto y memoria de trabajo, y medir calidad de las notas españolas. Retiramos la mención genérica de móvil de la slide.

## Tiempo: lo mediremos después

Retiramos las cifras externas de segundos y tokens/s de la presentación, guion y guía. Una prueba en nuestro PC sería un benchmark de desarrollo, identificado por modelo, precisión, motor, hardware, duración y contexto. Para decidir uso clínico, después se medirá en los equipos objetivo.

Todavía no estimamos tiempo por consulta. La [guía de intuición](guia-intuicion.md) mantiene p50/p95 y RTF como conceptos para diseñar esa futura medición.
