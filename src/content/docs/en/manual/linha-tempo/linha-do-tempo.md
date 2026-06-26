---
title: "Timeline"
---

The Timeline is a tool that transforms the continuous recording of data into a visual, chronological representation of all events and changes that occurred in the monitored infrastructure.

:::note
All event and metric records in the Timeline are permanent. Once created, this data cannot be deleted or altered, ensuring the reliability and legal validity of the history for audit and compliance purposes.
:::

![image-1756131037153.png](../../../../../assets/images/p36_image-1756131037153.png)

## Search Filters


| Ícone | Descrição |
| :---: | :--- |
| ![image-1756131155728.png](../../../../../assets/images/p36_332image-1756131155728.png) | **Real time**: Shows changes that occur on devices and monitors in real time. |
| ![image-1756131083740.png](../../../../../assets/images/p36_image-1756131083740.png) | **Unresolved event**: When active, lists only events that are not in the normal state. |
| ![image-1756131188512.png](../../../../../assets/images/p36_image-1756131188512.png) | **Pause**: Freezes the current screen for viewing. |

![image-1646833866456.png](../../../../../assets/images/p36_image-1646833866456.png)
**Filter by device**: Filters the alerts view to the selected device.

---

![image-1646833926056.png](../../../../../assets/images/p36_image-1646833926056.png)
**Filter by time range**: Filters alert information by the selected time range.


## Available Information

![image-1739974446872.png](../../../../../assets/images/p36_image-1739974446872.png)

---

![image-1732708907756.png](../../../../../assets/images/p36_image-1732708907756.png) **Status**: This icon indicates the status the device/monitor entered at the indicated time. It can have the following meanings: 

| Status | Descrição |
| :---: | :--- |
| ![image-1756131369083.png](../../../../../assets/images/p36_image-1756131369083.png) | The device/monitor returned to the normal state. | 
| ![image-1756131427462.png](../../../../../assets/images/p36_image-1756131427462.png) | The device/monitor is collecting data and is operating but with values in a warning state. |
| ![image-1756131484609.png](../../../../../assets/images/p36_uNyimage-1756131484609.png) | The device/monitor is collecting data and is operating but with values in a critical state. | 
| ![image-1756131598663.png](../../../../../assets/images/p36_image-1756131598663.png) | The device/monitor is unable to report information related to data collection. | 
| ![image-1756131693571.png](../../../../../assets/images/p36_image-1756131693571.png) | The device is unreachable due to a problem with another device above it in the network hierarchy. |

| Info | Description |
| :---: | :--- |
| DNS Google | Device: Name of the device where the status change occurred. |
| Ping | Monitor: Name of the monitor where the status change occurred. When the monitor has an instance, its name is shown next to it in parentheses. |
| Tempo de Resposta | Metric: Name of the metric where the event occurred. |
| ![image-1756131850905.png](../../../../../assets/images/p36_image-1756131850905.png) | Unresolved event: When this icon appears, it means this event has not yet returned to the normal state. |
| ![image-1739974466466.png](../../../../../assets/images/p36_image-1739974466466.png) | Event time: Shows the date and time the event was detected. |
| ![image-1739974478397.png](../../../../../assets/images/p36_image-1739974478397.png) | Alert: Indicates whether any alert was triggered during the event. The groups to which the alert was sent will be listed in the event details. |
| ![image-1732709258147.png](../../../../../assets/images/p36_image-1732709258147.png) | Details: Expands or hides the event details. |