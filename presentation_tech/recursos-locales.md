# Recursos locales: de dónde salen las cifras de la slide 26

Revisión del 12/10/2026. La slide muestra **un presupuesto de memoria y dos referencias externas de velocidad**, no un benchmark propio de la pipeline. Se retiraron las fuentes del pie para darle espacio a las tres tarjetas; quedan aquí y en el guion.

## RAM: presupuesto aproximado de 4–8 GB

Supuestos: MOSS 0.9B Q8_0 en un motor C++/GGUF, Qwen3-0.6B Q8_0, consulta de 15–30 minutos, contexto del generador de 4–8k tokens, un usuario. Un PC con **16 GB totales** sería un punto de partida para probar y dejar margen al sistema/HCIS; no es un requisito mínimo validado.

| Parte | Cálculo de planificación |
|---|---|
| Pesos de MOSS Q8_0 | El port de `transcribe.cpp` publica un archivo de ≈987 MB. |
| Estado adicional de MOSS | El mismo port propone ≈85 MB por minuto de audio: ≈1,28–2,55 GB para 15–30 min, además de los pesos. Es una aproximación específica de esa implementación. |
| Pesos de Qwen Q8_0 | Archivo oficial ≈639 MB. |
| KV cache de Qwen | Con cache FP16: 28 capas × 2 (K,V) × 8 cabezas KV × 128 dimensiones × 2 bytes = 114.688 bytes/token. A 4.096–8.192 tokens: ≈0,47–0,94 GB. |
| Subtotal calculable | ≈3,37–5,12 GB, antes de buffers, activaciones, runtime, temporales y diferencias de implementación. |
| Presupuesto mostrado | **4–8 GB para procesos**, redondeando con margen de trabajo. Es una estimación, no una medida de RAM máxima. |

Fuentes: [MOSS/transcribe.cpp: modelo, memoria y benchmarks](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/moss-transcribe-diarize.md), [archivo oficial Qwen GGUF](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/tree/main), [configuración oficial Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json).

Los valores del cálculo están en GB decimales; el KV de 4k/8k equivale a 448/896 MiB. Un contexto mayor necesita más cache. Una consulta larga puede superar 8k tokens al añadir la historia: la cifra no presupone que toda consulta de 30 min quepa en ese límite. Hay que medir con la entrada real o evaluar la estrategia de selección/chunking.

Tampoco trasladar el rango a PyTorch FP32: sus pesos, buffers y entorno pueden consumir más. El port usado para estas cifras valida sobre todo inglés/chino; no hemos comprobado equivalencia ni calidad clínica española de esa implementación respecto al modelo actual.

## Audio: 35,3 segundos en 21,08 segundos

El mantenedor de `transcribe.cpp` publica para MOSS Q8_0, en **CPU de un AMD Ryzen 7 PRO 4750U**, 21,08 s de cómputo para el clip `dots` de 35,3 s. Incluye mel, encoder y decode; media de tres iteraciones tras un warmup, commit `218aeae3`, 14/09/2026. El clip `jfk` de 11 s tarda 7,54 s. [Medición y reproducción del autor](https://github.com/handy-computer/transcribe.cpp/blob/main/docs/models/moss-transcribe-diarize.md#amd-ryzen-7-pro-4750u).

Esto sitúa un motor CPU especializado por debajo de tiempo real en **esos clips**. No permite multiplicar linealmente por 30 minutos: el contexto y coste de decode crecen con la grabación. Tampoco mide una consulta médica española completa ni proporciona p50/p95 de un despliegue.

Como segunda referencia técnica, [moss-transcribe.cpp de LocalAI](https://github.com/localai-org/moss-transcribe.cpp/blob/master/benchmarks/BENCHMARK.md) publica en una CPU x86 de 20 núcleos, limitada a 8 hilos, F32: 11 s de audio →6,5 s; 44 s →24,2 s; 132 s →102,8 s. Son pruebas calientes, excluyendo carga. La CPU exacta no se identifica; por eso esa tabla no se presenta como un benchmark i5.

## Generador: unos 7 tokens/s en un i5

Un experimento del autor del motor **Ember** publica para **Qwen3-0.6B Q8_0 en i5-1135G7**, 6,97 tokens/s con un hilo y 5,89 con cuatro. Medianas de 2–3 ejecuciones tras warmup. Es una medición histórica y orientativa de ese motor experimental, no de llama.cpp. [Experimento y código](https://voidwest.dev/research-notes/crossover-point-cpu-llm-decode.html).

Cálculo mostrado: **500 / 6,97 ≈72 s** para generar 500 tokens a ese ritmo. Es extrapolación aritmética, no una nota médica de 500 tokens medida. No incluye prefill (leer el prompt), carga, ASR ni comprobación. El coste real cambia con longitud de contexto, tokens de razonamiento, configuración y hardware. llama.cpp sigue siendo un motor candidato a medir en el proyecto.

## Qué mediríamos nosotros

Una consulta corta y una de 15–30 minutos, con configuración/versiones fijadas, modelo frío y cargado. Registrar RAM máxima del proceso y del flujo, tiempo ASR, prefill, decode y tiempo total. Repetir suficientes casos para p50/p95, además de calidad, omisiones, atribución y ediciones clínicas.

La [guía de intuición](guia-intuicion.md) explica tokens/s, p50/p95 y el resto de las tareas. Los benchmarks citados son de los autores de sus motores, sin reproducción local todavía.
