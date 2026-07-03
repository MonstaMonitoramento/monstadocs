---
title: Agentes
sidebar:
  order: 3
---
El Agente de Monitorización de Monsta Tecnologia permite gestionar infraestructuras de TI complejas y distribuidas, garantizando que la monitorización sea eficiente, segura y no sobrecargue su red de área amplia (WAN). Actualmente, el Agente está disponible para Windows y su instalación es rápida y sencilla en cualquier entorno de TI. Próximamente dispondremos de un instalador para Linux (incluyendo las distribuciones más populares).

## ¿Cómo funciona el Agente Monsta?

El Agente es la inteligencia distribuida de nuestro sistema. En lugar de centralizar todo el trabajo en el servidor, el Agente realiza las comprobaciones directamente en la red donde residen los activos, garantizando una recopilación precisa y de alto rendimiento.

Diseñado para entornos de red modernos, el Agente ofrece:

- **Descentralización do Processamento:** Al ejecutar las tareas de monitorización directamente en la red remota, el Agente elimina la sobrecarga de procesamiento en el servidor principal, permitiendo que la plataforma gestione una mayor escala de dispositivos sin comprometer el rendimiento del núcleo del sistema.
- **Resiliencia Total:** El sistema es inmune a fallos intermitentes de conexión a Internet. En caso de que la comunicación con el servidor se interrumpa, el Agente continúa ejecutando las tareas localmente, garantizando la integridad de la monitorización, y sincroniza los datos automáticamente tan pronto se restablezca la conexión.
- **Conectividad Simplificada:** El Agente funciona perfectamente sin la necesidad de configurar VPN complejas o reenvío de puertos (*port forwarding*), garantizando una instalación rápida y manteniendo la seguridad de su infraestructura intacta.

## Gerenciamiento de Agentes y Monitorización Distribuida

![image-1768997185306.png](../../../../../assets/images/p63_image-1768997185306.png)


| Ícone                                                                                | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-1647867281671.png](../../../../../assets/images/p63_image-1647867281671.png) | **Pesquisar**: Utilice el campo de filtro para localizar agentes específicos. Al escribir, la lista se actualizará automáticamente para mostrar únicamente los resultados que coincidan con el texto ingresado. |
| ![image-1768997246532.png](../../../../../assets/images/p63_image-1768997246532.png) | **Licenças de agentes disponíveis**: Este campo indica la cantidad de agentes disponibles en su suscripción. Si necesita monitorizar más dispositivos puede acceder al área de cliente en nuestro sitio y añadir tantas licencias como sean necesarias a su plan. |
| ![image-1768998008744.png](../../../../../assets/images/p63_image-1768998008744.png) | **Total de agentes**: Cantidad de agentes configurados y que ocupan una licencia. |
| ![image-1768999817872.png](../../../../../assets/images/p63_image-1768999817872.png) | **Ordenação**: Las flechas permiten reordenar la lista de agentes. Este orden define la prioridad de uso de las licencias contratadas: los agentes posicionados por encima del límite de su cuota serán monitorizados, mientras que los excedentes permanecerán en espera. |
| ![image-1768998685081.png](../../../../../assets/images/p63_image-1768998685081.png) | **Status**: Indica la condición actual de cada dispositivo en la red:<br />• **Conectado**: El agente está activo y se comunica normalmente con el servidor.<br />• **Desconectado**: El agente está offline o se ha perdido la comunicación.<br />• **Límite Excedido**: El agente fue instalado, pero no está monitorizando porque se alcanzó la cuota de licencias de su plan.<br />• **Bloqueado**: La comunicación del agente está bloqueada. |
| ![image-1768998876264.png](../../../../../assets/images/p63_image-1768998876264.png) | **Dispositivo**: Muestra información sobre el sistema operativo donde el agente está en ejecución. |
| ![image-1768999021483.png](../../../../../assets/images/p63_image-1768999021483.png) | **Conexão**: Exclusivo para agentes conectados, este campo indica la ruta de comunicación.<br />• **Direto**: El agente se comunica directamente con el servidor.<br />• **Híbrido**: El agente utiliza un servidor intermedio (Proxy) para sortear restricciones de firewall o aislamiento de red. |
| ![image-1768999216633.png](../../../../../assets/images/p63_image-1768999216633.png) | **Versão**: Indica la versión actual del agente instalada en el host. Este campo se gestiona automáticamente por el sistema: siempre que se publique una nueva actualización, Monsta realizará la actualización de forma automática, garantizando que siempre disponga de las funcionalidades y correcciones más recientes sin intervención manual. |
| ![image-1768999398371.png](../../../../../assets/images/p63_image-1768999398371.png) | **Última atividade**: Registra la fecha y hora exactas de la última comunicación recibida del agente. Es el principal indicador para verificar si la monitorización se está realizando en tiempo real. |
| ![image-1768999481044.png](../../../../../assets/images/p63_image-1768999481044.png) | **Bloquear agente**: Permite interrumpir o reanudar la comunicación de un agente específico manualmente. Cuando está bloqueado, el agente deja de enviar datos al servidor, pero permanece instalado y configurado, pudiendo reactivarse en cualquier momento con un clic. |
| ![image-1768999732028.png](../../../../../assets/images/p63_image-1768999732028.png) | **Excluir agente**: Elimina permanentemente el agente de su lista de monitorización.<br />**Nota**: Por seguridad, esta acción solo está permitida para agentes con estado **Desconectado**. Si el agente aún está activo, es necesario detener el servicio en el host antes de la eliminación. |


:::caution[Atención]
El soporte para los agentes está disponible a partir de la versión **6** de Monsta.
:::