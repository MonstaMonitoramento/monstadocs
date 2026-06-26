---
title: "Ejemplos de Plantillas de Mensajes de Alerta"
---

Las alertas enviadas por Monsta pueden personalizarse a través de las Plantillas de Mensaje, disponibles en Grupo de Alertas > Template de Mensagem. Este artículo muestra algunos ejemplos de personalización para mejorar los mensajes de alerta, con el fin de adaptarlos a sus necesidades. Para entender el funcionamiento de las Plantillas de Mensaje y cómo funcionan las variables disponibles, vea el artículo sobre los [Alertas](/es/manual/grupos-alertas/alertas#plantillas-de-mensaje) de Monsta.

## Utilizando variables de acuerdo con el alerta

Algunas variables están relacionadas con el dispositivo y otras con el monitor. Por ejemplo, la variable `{{nomemetrica}}` está relacionada con un monitor. Por lo tanto, al utilizar esa variable en una alerta de dispositivo, se enviará vacía en la alerta. Sin embargo, es posible diferenciar en la misma plantilla cuál será el mensaje para una alerta de dispositivo o de monitor. El código siguiente es un ejemplo que utiliza este recurso.

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Estado: {{monitor.estado}}
Dispositivo: {{dispositivo.nome}}
Monitor: {{monitor.nomecurto}}
{{nomemetrica}} ({{nomeinstancia}}): {{valor}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{/if}}
```

Lo que está entre `{{#if alertadispositivo}}` y el `{{else}}` se refiere al mensaje para una alerta generada por un dispositivo (cuando queda sin conexión, por ejemplo). Lo que está entre `{{else}}` y `{{/if}}` se refiere al mensaje para una alerta generada por un monitor (cuando un monitor alcanza una métrica de alerta, por ejemplo). Cabe señalar que el campo "`> Subject:`" se refiere al "asunto" cuando la alerta se envía por correo electrónico. Las alertas por Telegram y SMS no contendrán esa información.

El código de ejemplo generará las siguientes alertas (ejemplos recibidos en Telegram).
- Alerta generada por un Dispositivo que volvió del estado crítico:

:::tip[Alerta]
Estado: Normal  
Dispositivo: Impressora  
IP: 192.168.10.10  
Horario: 01/01/2026 - 14:50:18
:::

- Alerta generada por un Monitor sin instancia que entró en estado crítico:

:::tip[Alerta]
Estado: Crítico  
Dispositivo: Servidor Firewall  
Monitor: Carga (Load Average)  
Carga (): 3  
IP: 192.168.10.1  
Horario: 01/01/2026 - 11:55:06
:::



- Alerta generada por un Monitor con instancia que entró en estado crítico:



:::tip[Alerta]
Estado: Crítico  
Dispositivo: Servidor de E-mails  
Monitor: Partición /home  
Partición (/home): 500 GB  
IP: 192.168.10.2  
Horario: 01/01/2026 - 12:33:46
:::



Si no se hubiera utilizado la personalización para dispositivo y monitor (usando las configuraciones del mensaje de los alertas de monitor para ambos), el mensaje de alerta de un dispositivo quedaría así:

- Alerta generada por un Dispositivo con las variables de monitores.



:::tip[Alerta]
Estado: Normal  
Dispositivo: Impressora  
Monitor:   
 (): False  
IP: 192.168.10.10  
Horario: 01/01/2026 - 14:50:18
:::



La personalización permite que el mensaje esté mejor estructurado.

## Personalizando con informaciones fijas

Además de utilizar las variables, también puede añadir información que no cambia según la alerta, como el nombre de la empresa, departamento, responsable, número de soporte... Estos datos pueden ser útiles si recibe alertas de más de un Monsta (para identificar de dónde provino la alerta) o incluso para alertas que se envían a gerentes, proveedores o terceros. Como es posible crear varias plantillas de mensaje, puede crear un [Grupo de Alertas](/es/manual/grupos-alertas/alertas#grupos) para un proveedor de suministros de impresora que recibirá un correo cuando el tóner de su impresora esté en estado crítico. Basta con configurar la plantilla en el grupo de alertas y añadir el grupo de alertas en el monitor específico.

Por ejemplo:

- Template para proveedor de suministros para la impresora, que puede utilizarse exclusivamente en monitores de impresora

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Alerta da empresa Monsta
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Alerta da empresa Monsta
Nossa impressora ({{dispositivo.nome}}) está alertando que {{nomemetrica}} ({{nomeinstancia}}) está em estado {{monitor.estado}} ({{valor}}).
Por favor, envie um orçamento para suporteti@empresa.com.br
Horário: {{dataehora}}
{{/if}}
```

- Alerta generado por un Monitor de la impresora en estado crítico:



:::tip[Alerta]
Alerta da empresa Monsta  
Nossa impressora (Impressora XYZ) está alertando que Toner (Toner) está en estado Crítico (10 %).  
Por favor, envie um orçamento para <suporteti@empresa.com.br> para substituição.  
Horario: 01/01/2026 - 12:33:46
:::



Ejemplo de la configuración del grupo de alertas, para que el destinatario reciba solo la alerta crítica de monitores:

![image-1773337531514.png](../../../../../assets/images/p173_image-1773337531514.png)

Configuración del monitor Toner, utilizado en el ejemplo:

![image-1773337636144.png](../../../../../assets/images/p173_image-1773337636144.png)

Vea otro ejemplo, en el caso de tener más de un servidor Monsta y querer identificar de cuál de ellos provino la alerta.

- Template Monsta 1

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Monsta Matriz - Alerta Dispositivo
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Monsta Matriz - Alerta Monitor
Estado: {{monitor.estado}}
Dispositivo: {{dispositivo.nome}}
Monitor: {{monitor.nomecurto}}
{{nomemetrica}} ({{nomeinstancia}}): {{valor}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{/if}}
```

- Alerta generada por un Dispositivo que volvió del estado crítico:



:::tip[Alerta]
Monsta Matriz - Alerta Dispositivo  
Estado: Normal  
Dispositivo: Impressora  
IP: 192.168.10.10  
Horario: 01/01/2026 - 14:50:18
:::



- Alerta generada por un Monitor con instancia que entró en estado crítico:



:::tip[Alerta]
Monsta Matriz - Alerta Monitor  
Estado: Crítico  
Dispositivo: Servidor de E-mails  
Monitor: Partición /home  
Partición (/home): 500 GB  
IP: 192.168.10.2  
Horario: 01/01/2026 - 12:33:46
:::



- Template Monsta 2

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Monsta Filial - Alerta Dispositivo
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Monsta Filial - Alerta Monitor
Estado: {{monitor.estado}}
Dispositivo: {{dispositivo.nome}}
Monitor: {{monitor.nomecurto}}
{{nomemetrica}} ({{nomeinstancia}}): {{valor}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{/if}}
```

- Alerta generada por un Dispositivo que volvió del estado crítico:



:::tip[Alerta]
Monsta Filial - Alerta Dispositivo  
Estado: Normal  
Dispositivo: Impressora  
IP: 192.168.11.10  
Horario: 01/01/2026 - 14:50:18
:::



- Alerta generada por un Monitor con instancia que entró en estado crítico:



:::tip[Alerta]
Monsta Filial - Alerta Monitor  
Estado: Crítico  
Dispositivo: Servidor Firewall  
Monitor: Partición /home  
Partición (/home): 500 GB  
IP: 192.168.11.2  
Horario: 01/01/2026 - 12:33:46
:::



## Conclusión

Hay innumerables formas de personalizar los mensajes de alerta de Monsta. Utilice estos ejemplos para explorar ideas que se adapten a su escenario. Si tiene alguna duda adicional, póngase en contacto con nuestro soporte.