---
title: "Línea de Tiempo"
---

La Línea de Tiempo es una herramienta que transforma el registro continuo de datos en una representación visual y cronológica de todos los eventos y cambios ocurridos en la infraestructura monitorizada.

:::note
Todos los registros de eventos y métricas en la Línea de Tiempo son permanentes. Una vez creados, estos datos no pueden borrarse ni modificarse, garantizando la fiabilidad y la validez legal del historial a efectos de auditoría y cumplimiento.
:::

![image-1756131037153.png](../../../../../assets/images/p36_image-1756131037153.png)

## Filtros de Búsqueda


| Ícone | Descrição |
| :---: | :--- |
| ![image-1756131155728.png](../../../../../assets/images/p36_332image-1756131155728.png) | **Tiempo real**: Muestra los cambios que ocurren en los dispositivos y monitores en tiempo real. |
| ![image-1756131083740.png](../../../../../assets/images/p36_image-1756131083740.png) | **Evento no resuelto**: Cuando está activo, muestra solo los eventos que no se encuentran en estado normal. |
| ![image-1756131188512.png](../../../../../assets/images/p36_image-1756131188512.png) | **Pausa**: Congela la pantalla actual para su visualización. |

![image-1646833866456.png](../../../../../assets/images/p36_image-1646833866456.png)
**Filtro por dispositivo**: Filtra la visualización de las alertas para el dispositivo seleccionado.

---

![image-1646833926056.png](../../../../../assets/images/p36_image-1646833926056.png)
**Filtro por intervalo de tiempo**: Filtra la información de las alertas por el intervalo de tiempo seleccionado.


## Información Disponible

![image-1739974446872.png](../../../../../assets/images/p36_image-1739974446872.png)

---

![image-1732708907756.png](../../../../../assets/images/p36_image-1732708907756.png) **Estado**: Este icono indica el estado en el que el dispositivo/monitor entró en la hora indicada. Puede tener los siguientes significados: 

| Estado | Descripción |
| :---: | :--- |
| ![image-1756131369083.png](../../../../../assets/images/p36_image-1756131369083.png) | El dispositivo/monitor volvió al estado normal. | 
| ![image-1756131427462.png](../../../../../assets/images/p36_image-1756131427462.png) | El dispositivo/monitor tiene la recolección de datos operativa pero con valores en estado de aviso. 
| ![image-1756131484609.png](../../../../../assets/images/p36_uNyimage-1756131484609.png) | El dispositivo/monitor tiene la recolección de datos operativa pero con valores en estado crítico. | 
| ![image-1756131598663.png](../../../../../assets/images/p36_image-1756131598663.png) | El dispositivo/monitor no es capaz de reportar información referente a la recolección de datos. | 
| ![image-1756131693571.png](../../../../../assets/images/p36_image-1756131693571.png) | El dispositivo está inalcanzable debido a un problema con otro dispositivo superior en su jerarquía de red. |

| Info | Descripción |
| :---: | :--- |
| DNS Google | Dispositivo: Nombre del dispositivo en el que ocurrió el cambio de estado. |
| Ping | Monitor: Nombre del monitor en el que ocurrió el cambio de estado. Cuando el monitor tiene instancia, el nombre de esta se muestra a su lado entre "( )". |
| Tempo de Resposta | Métrica: Nombre de la métrica en la que ocurrió el evento. |
| ![image-1756131850905.png](../../../../../assets/images/p36_image-1756131850905.png) | Evento no resuelto: Cuando este icono se presenta, significa que este evento aún no ha vuelto al estado normal. |
| ![image-1739974466466.png](../../../../../assets/images/p36_image-1739974466466.png) | Horario del evento: Informa la fecha y la hora en que se detectó el evento. |
| ![image-1739974478397.png](../../../../../assets/images/p36_image-1739974478397.png) | Alerta: Informa si se disparó alguna alerta durante el evento. Los grupos a los que se envió la alerta se listarán en los detalles del evento. |
| ![image-1732709258147.png](../../../../../assets/images/p36_image-1732709258147.png) | Detalles: Expande u oculta los detalles del evento. |