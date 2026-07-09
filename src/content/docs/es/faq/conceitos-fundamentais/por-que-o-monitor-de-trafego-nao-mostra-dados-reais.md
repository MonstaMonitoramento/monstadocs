---
title: "¿Por qué el monitor de tráfico no muestra datos reales?"
---

Al supervisar el tráfico de red a través de SNMP, nos encontramos con monitores de **32 bits** y **64 bits.** La principal diferencia entre ellos está en la capacidad máxima de conteo.

## Monitor de tráfico

Este monitor utiliza una variable de 32 bits que puede almacenar un valor máximo de 4 Gigabytes transferidos. En un enlace de red de alta velocidad, por ejemplo, un enlace de 1 Gbps, este conteo puede alcanzarse en 32 segundos.

- **Ocurrencia de rollover**: Cuando esta variable supera el valor máximo, el contador vuelve a cero. Esta característica se conoce en Monsta como `rollover`.
- **Problema ocasionado**: Este "desbordamiento" del contador puede dar lugar a gráficos de monitorización con caídas abruptas, informar velocidades incorrectas o menores que el total transferido en la interfaz de red monitorizada, dificultando el análisis y el cálculo correcto del tráfico. Así, el valor real del tráfico se pierde, ya que, dependiendo de la frecuencia con la que se realice la recopilación de datos del monitor, un rollover puede producirse sin ser detectado.

![image-1756919458783.png](../../../../../assets/images/p120_image-1756919458783.png)  
Ejemplo de un monitor de tráfico de 32 bits en un enlace de 1 Gbps con frecuencia de 5 minutos.

## Monitor de tráfico (64 bits)

Este monitor puede almacenar un valor máximo de 18 Exabytes. Este número es tan grande que un `rollover` en enlaces de alta velocidad es prácticamente imposible de producirse. Por ejemplo, un enlace de 100 Gbps tardaría aproximadamente 46 años en llenar toda la variable.

- **Mayor precisión y fiabilidad**: Con el contador de 64 bits, se garantiza que la contabilización del tráfico sea continua y precisa, sin interrupciones.
- **Análisis a largo plazo**: Permite un análisis del tráfico más preciso y fiable en periodos largos, ya que el valor acumulado no se pierde.

![image-1756919778342.png](../../../../../assets/images/p120_image-1756919778342.png)

El mismo tráfico en un monitor de 64 bits.

## Conclusión

Para gráficos reales, utilice siempre los monitores de 64 bits, que poseen una mejor precisión en la medición. No obstante, si el equipo que pretende monitorizar solo proporciona el tráfico en 32 bits, reduzca la frecuencia de recogida de datos a un valor que se ajuste a la velocidad de la interfaz de red monitorizada.