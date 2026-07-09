---
title: "¿Cómo funciona el sistema de notificaciones de alertas?"
---

Monsta tiene un sistema de grupos de alerta:

![image-1644795874070.png](../../../../../assets/images/p5_image-1644795874070.png)

Cada grupo de alerta contiene configuraciones para notificaciones por E-mail, SMS y Telegram que pueden aplicarse a dispositivos y monitores. Para cada uno de estos 3 mecanismos de envío de notificaciones, el grupo puede configurarse para enviar alertas cuando hay un evento en estado de advertencia, en estado crítico o ambos. Además, el grupo puede configurarse para alertar solo para dispositivos, solo para monitores o ambos:

![image-1644795936801.png](../../../../../assets/images/p5_image-1644795936801.png)

Finalmente, el grupo puede configurarse para enviar alertas solo durante un período especificado por el usuario:

![image-1644796975555.png](../../../../../assets/images/p5_image-1644796975555.png)

Para aplicar estas configuraciones de alerta, cada dispositivo o monitor puede tener cero o más grupos de alerta:

![image-1644795982010.png](../../../../../assets/images/p5_image-1644795982010.png)

Cuando ocurre un evento para un dispositivo o monitor, se verifican todos los grupos de alerta vinculados. Si las condiciones configuradas coinciden, se enviará una notificación.