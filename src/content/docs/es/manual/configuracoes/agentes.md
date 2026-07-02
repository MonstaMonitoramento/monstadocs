---
title: Agentes
sidebar:
  order: 3
---
El Agente de Monitorización de Monsta Tecnología permite gestionar infraestructuras de TI complejas y distribuidas, garantizando que la monitorización sea eficiente, segura y no sobrecargue su red de área extensa (WAN). Actualmente, el Agente está disponible para Windows y su instalación es rápida y sencilla en cualquier entorno de TI. Próximamente tendremos un instalador para Linux (incluyendo las distribuciones más populares).

## ¿Cómo funciona el Agente Monsta?

El Agente Monsta actúa como un Proxy de Monitorización Distribuida para sus sucursales y redes remotas. Monitorice activos de forma centralizada y segura, eliminando la complejidad de redireccionamiento de puertos, VPNs o la exigencia de IPs fijos/estáticos.

## Beneficios arquitectónicos


| **Recurso** | **Descripción** |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Coleta Local** | El Agente se instala en la red remota y realiza la recopilación de datos de todos los dispositivos *localmente*. |
| **Comunicação Consolidada** | Agrega y almacena temporalmente las métricas antes de enviarlas al Servidor Monsta central en un único flujo. |
| **Segurança Otimizada** | Solo el Agente necesita abrir comunicación con el servidor central, requiriendo menos reglas de firewall y reduciendo la superficie de ataque. |
| **Tolerância a Falhas** | En caso de pérdida temporal de la conexión WAN, el Agente continúa recopilando y almacenando datos (caché), garantizando que ninguna información se pierda. |


## Gerenciamento de Agentes e Monitoramento Distribuído

![image-1768997185306.png](../../../../../assets/images/p63_image-1768997185306.png)


| Icono | Descripción |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-1647867281671.png](../../../../../assets/images/p63_image-1647867281671.png) | **Buscar**: Utilice el campo de filtro para localizar agentes específicos. Al escribir, la lista se actualizará automáticamente para mostrar únicamente los resultados que coincidan con el texto introducido. |
| ![image-1768997246532.png](../../../../../assets/images/p63_image-1768997246532.png) | **Licencias de agentes disponibles**: Este campo indica la cantidad de agentes disponibles en su suscripción. Si necesita monitorizar más dispositivos, puede acceder al área de cliente en nuestro sitio web y añadir tantas licencias como sean necesarias a su plan. |
| ![image-1768998008744.png](../../../../../assets/images/p63_image-1768998008744.png) | **Total de agentes**: Número de agentes configurados y que ocupan una plaza de licencia. |
| ![image-1768999817872.png](../../../../../assets/images/p63_image-1768999817872.png) | **Ordenación**: Las flechas permiten reordenar la lista de agentes. Este orden define la prioridad de uso de las licencias contratadas: los agentes situados por encima del límite de su cuota serán monitorizados, mientras que los excedentes permanecerán en espera. |
| ![image-1768998685081.png](../../../../../assets/images/p63_image-1768998685081.png) | **Estado**: Indica la condición actual de cada dispositivo en la red: • **Conectado**: El agente está activo y comunicándose normalmente con el servidor. • **Desconectado**: El agente está sin conexión o hubo pérdida de comunicación. • **Límite Excedido**: El agente fue instalado, pero no está monitorizando porque la cuota de licencias de su plan ha sido alcanzada. • **Bloqueado**: La comunicación del agente está bloqueada. |
| ![image-1768998876264.png](../../../../../assets/images/p63_image-1768998876264.png) | **Dispositivo**: Muestra información sobre el sistema operativo donde el agente se está ejecutando. |
| ![image-1768999021483.png](../../../../../assets/images/p63_image-1768999021483.png) | **Conexión**: Exclusivo para agentes conectados, este campo indica la ruta de comunicación. • **Directa**: El agente se comunica directamente con el servidor. • **Híbrida**: El agente utiliza un servidor intermedio (Proxy) para sortear restricciones de firewall o aislamiento de red. |
| ![image-1768999216633.png](../../../../../assets/images/p63_image-1768999216633.png) | **Versión**: Indica la versión actual del agente instalada en el host. Este campo es gestionado automáticamente por el sistema: siempre que se publique una nueva actualización, Monsta realizará la actualización de forma automática, garantizando que usted siempre tenga las funciones y correcciones más recientes sin intervención manual. |
| ![image-1768999398371.png](../../../../../assets/images/p63_image-1768999398371.png) | **Última actividad**: Registra la fecha y hora exactas de la última comunicación recibida del agente. Es el principal indicador para comprobar si la monitorización se está produciendo en tiempo real. |
| ![image-1768999481044.png](../../../../../assets/images/p63_image-1768999481044.png) | **Bloquear agente**: Permite interrumpir o reanudar la comunicación de un agente específico manualmente. Cuando está bloqueado, el agente deja de enviar datos al servidor, pero permanece instalado y configurado, pudiendo reactivarse en cualquier momento con un clic. |
| ![image-1768999732028.png](../../../../../assets/images/p63_image-1768999732028.png) | **Eliminar agente**: Elimina permanentemente el agente de su lista de monitorización. **Nota**: Por seguridad, esta acción solo está permitida para agentes que tengan el estado **Desconectado**. Si el agente aún está activo, es necesario detener el servicio en el host antes de la eliminación. |


:::caution[Atención]
El soporte a los agentes está disponible a partir de la versión **6** de Monsta.
:::