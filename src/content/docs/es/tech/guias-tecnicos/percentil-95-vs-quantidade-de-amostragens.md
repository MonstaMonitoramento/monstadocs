---
title: "Percentil 95 vs Cantidad de Muestreos"
---

O **Percentil 95** es una métrica estadística ampliamente utilizada en diversas áreas, pero con destaque en **redes de computadores y telecomunicaciones**, para medir y tarificar el uso del ancho de banda y para monitorizar el rendimiento de sistemas.



## O que é um Percentil?

Un percentil es una medida que indica el valor por debajo del cual cae un determinado porcentaje de observaciones en un conjunto de datos ordenado. Por ejemplo, el 50.º percentil es la mediana, el valor por debajo del cual se encuentra el 50% de los datos.



## Percentil 95 em Redes de Computadores e Telecomunicações

En el contexto de redes, especialmente para proveedores de Internet (ISPs) y empresas que contratan enlaces dedicados, el Percentil 95 es una metodología de **medición y facturación del tráfico de datos**. La idea es ofrecer un modelo de facturación más flexible y justo, que acomode picos de uso ocasionales sin penalizar al cliente con costes excesivos.

### Como funciona?

1. **Coleta de Dados**: El uso del ancho de banda se monitoriza y muestrea en intervalos regulares, generalmente cada 5 minutos, a lo largo de un período de tiempo (típicamente un mes). Cada muestra representa la media del ancho de banda utilizado en ese intervalo.
2. **Ordenação**: Al final del período de medición, todas esas muestras se recogen y se ordenan en orden creciente, del menor uso de banda al mayor.
3. **Descarte dos Picos**: Los **5% valores más altos de uso del ancho de banda se descartan**. Esto significa que los picos de tráfico más elevados y esporádicos, que podrían inflar el coste, no se consideran en la facturación.
4. **Cálculo do Percentil 95**: El siguiente valor más alto tras descartar el 5% superior es el **Percentil 95**. Este es el valor que se utilizará para la facturación. En otras palabras, el 95% del tiempo, el uso del ancho de banda estuvo por debajo o igual a ese valor.

## Impacto da Granularidade da Amostragem no Percentil 95

En el monitoreo del tráfico de datos, la **granularidad del muestreo** —es decir, la frecuencia con la que se recopilan los datos— tiene un impacto directo en el valor del percentil 95. En el experimento abajo, observamos que el percentil 95 fue **mayor en monitorizaciones con muestreo cada 1 minuto** en comparación con monitorizaciones con muestreo cada 5 minutos.

Esto se debe a la capacidad inherente del muestreo más frecuente para capturar variaciones más rápidas y picos de uso. Vamos a detallar técnicamente:

### Amostragem a Cada 1 Minuto: Captura mais Precisa de Picos

![image-1748523913039.png](../../../../../assets/images/p108_image-1748523913039.png)

Cuando los datos se muestrean cada 1 minuto, el sistema de monitorización registra el tráfico de datos en intervalos muy cortos. Esto le permite **capturar con mayor precisión los picos de uso transitorios y de corta duración**. Imagine un escenario donde hay un aumento abrupto en el tráfico de datos durante 30 segundos y luego vuelve a los niveles normales. Un muestreo cada 1 minuto tiene una alta probabilidad de registrar ese pico, ya que el intervalo de recogida posee un intervalo menor entre las muestras.

### Amostragem a Cada 5 Minutos: Suavização dos Picos

![image-1748523993137.png](../../../../../assets/images/p108_image-1748523993137.png)

Por otro lado, cuando el muestreo se realiza cada 5 minutos, el sistema calcula una media del tráfico de datos a lo largo de un período de 300 segundos. Esa media de tiempo mayor inerentemente **suaviza los picos de uso**. Si ocurre un pico de tráfico de corta duración (por ejemplo, 30 segundos) dentro de un intervalo de 5 minutos, su impacto se diluye por la media de los 4 minutos y 30 segundos restantes de tráfico potencialmente más bajo.

En términos técnicos, cada muestra de 5 minutos es una representación agregada del tráfico en ese intervalo. La menor frecuencia de muestreo resulta en un conjunto de datos más "suavizado", donde las variaciones rápidas son menos perceptibles. Los valores extremos (los picos) se "aplanan" debido al cálculo de la media sobre un período más largo, lo que resulta en un percentil 95 menor. Esto no significa que los picos no existan, sino que el muestreo con menor granularidad no los registra con la misma fidelidad.

Como ejemplo, el gráfico abajo posee un intervalo de muestreo de 30 minutos. La diferencia del percentil 95 con respecto a los demás muestreos se atenúa considerablemente:

![image-1748525353442.png](../../../../../assets/images/p108_image-1748525353442.png)

## Conclusão

La elección de la granularidad del muestreo en la monitorización del tráfico de datos es crucial y depende de los objetivos del análisis. Para una **detección precisa y oportuna de picos de uso** y para entender la capacidad de explosión de la red, un **muestreo más granular (como cada 1 minuto)** es preferible, aunque resulte en un percentil 95 más alto. Esto proporciona una visión más detallada y fiel del comportamiento de la red en momentos de alta demanda. Si el objetivo es tener una visión más consolidada y estable del tráfico medio y descartar fluctuaciones muy rápidas, un muestreo menos granular (como cada 5 minutos) puede ser suficiente. Es importante ser consciente de que muestras con intervalos grandes pueden subestimar la magnitud real de los picos de uso.