---
title: "Como funciona o sistema de notificações de alertas?"
---

O Monsta tem um sistema de grupos de alerta:

![image-1644795874070.png](../../../../../assets/images/p5_image-1644795874070.png)

Cada grupo de alerta contém configurações para notificações por E-mail, SMS e Telegram que podem ser aplicadas a dispositivos e monitores. Para cada um desses 3 mecanismos de enviar notificações, o grupo pode ser configurado para enviar alertas quando tem um evento em estado de aviso, estado de crítico ou ambos. Além disso, o grupo pode ser configurado para alertar apenas para dispositivos, apenas para monitores ou ambos:

![image-1644795936801.png](../../../../../assets/images/p5_image-1644795936801.png)

Finalmente, o grupo pode ser configurado para enviar alertas apenas durante um período especificado pelo usuário:

![image-1644796975555.png](../../../../../assets/images/p5_image-1644796975555.png)

Para aplicar essas configurações de alerta, cada dispositivo ou monitor pode ter zero ou mais grupos de alerta:

![image-1644795982010.png](../../../../../assets/images/p5_image-1644795982010.png)

Quando ocorre um evento para um dispositivo ou monitor, todos os grupos de alerta vinculados são verificados. Se as condições configuradas corresponderem, uma notificação será enviada.