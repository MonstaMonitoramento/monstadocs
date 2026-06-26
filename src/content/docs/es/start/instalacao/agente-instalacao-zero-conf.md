---
title: "Agente: Instalación Zero Conf"
sidebar:
  order: 4
---

Esta documentación describe el funcionamiento y la arquitectura del **Agente Monsta**, una herramienta para extender el monitorizado de su plataforma a redes remotas y distribuidas, asegurando rendimiento y seguridad mediante el protocolo QUIC.

## Instalación del Agente para Windows

- Descargue el programa del agente:

| | |
| --- | --- |
| ![image-1660325708746.png](../../../../../assets/images/p139_image-1660325708746.png) | [**DESCARGA**](http://www.monsta.com.br/monsta/download/agent.msi)<br />[https://monsta.com.br/downloads/](https://www.monsta.com.br/monsta/download/agent.msi) |

- Con sesión de un usuario con permisos de administrador, ejecute el instalador "agent.msi".
- Cuando se le solicite, ingrese la clave de licencia de Monsta a la que desea conectar el agente.

:::note
La Clave de Licencia se puede obtener en Monsta dentro del menú "Configuración" en la opción "Agentes". Se muestra en la esquina superior derecha.
:::

:::tip
**Firewall**:  
- No es necesario redirigir ningún puerto hacia el servidor de Monsta;  
- Para garantizar conexiones directas, permita la salida del puerto **58580/UDP** en su firewall del servidor de Monsta hacia Internet;  
- Permita el acceso del servidor de Monsta a los hosts mind.monsta.com.br y agent.monsta.com.br.
:::

## Creación del Dispositivo

Una vez completada la instalación, el **Agente** aparecerá automáticamente en la pantalla de **Configuración** en el apartado **Agentes** con la identificación del host. El dispositivo monitorizado será **creado y listado instantáneamente** en la pantalla de **Dispositivos** con el mismo nombre del host y estará listo para la configuración y la adición de nuevos monitores.

### Cómo monitorizar dispositivos mediante la conexión del Agente

Para cubrir toda la red remota con un único agente, registre los nuevos dispositivos en Monsta y defina que el dispositivo esté bajo la **jerarquía** del host donde el Agente está instalado.

Ejemplo de Jerarquía:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

## Instalación desde la línea de comandos

El instalador **agent.msi** admite parámetros de línea de comandos para automatización. Integrado con la utilidad **msiexec**, permite instalar vía **GPO**, eliminando la necesidad de intervención manual en la interfaz gráfica.

Opciones de la línea de comandos:


|  |  |
| --- | --- |
| `LICENSEKEY=\[clave de licencia\]` | Indica la clave de licencia a la que el Agente deberá conectarse. |
| `AGREE=\[Y\]` | Confirma la aceptación de los términos de uso. |

:::tip[Ejemplo de uso]
```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```
:::