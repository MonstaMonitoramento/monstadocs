---
title: "Monitorizando la Calidad del Enlace a Internet: Inversión de los Límites de Alerta"
---

Al monitorizar la velocidad o el rendimiento de su enlace a Internet (como el *throughput*), desea ser alertado cuando la velocidad **caiga por debajo de un valor aceptable**.

Los monitores de tráfico en Monsta, por defecto, asumen que **cuanto mayor sea el valor, peor es el problema.** Pero puede invertir esa lógica para monitorizar su enlace para que funcione con: **cuanto menor sea el valor, peor es el problema**.

Utilice la funcionalidad **Invertir Límites** para aplicar esta lógica:

## Invirtiendo la Lógica

Para garantizar que reciba alertas cuando la velocidad caiga por debajo del mínimo aceptable, siga estos pasos:

- Haga clic en el monitor de tráfico;
- Haga clic en el botón "Editar";
- Haga clic en el botón "Invertir Límites"  
    ![image-1765802497808.png](../../../../../assets/images/p144_image-1765802497808.png)
- Ajuste las barras de porcentaje para elegir los límites en los que desea ser alertado.

En el ejemplo de la imagen anterior, el monitor está configurado para alertar sobre un enlace de 1G en las siguientes situaciones:



| Campo | Ejemplo de Valor | Objetivo |
| --- | --- | --- |
| **Límite Crítico** | 2% | Monsta enviará una alerta de estado crítico si el tráfico queda **por debajo o igual** a 20 Mbps. |
| **Límite de Aviso** | 8% | Monsta enviará una alerta de aviso si el tráfico queda **entre** 80 Mbps y **por encima** de 20 Mbps. |



Tras definir sus límites, haga clic en el botón **Guardar para grabar sus cambios**.