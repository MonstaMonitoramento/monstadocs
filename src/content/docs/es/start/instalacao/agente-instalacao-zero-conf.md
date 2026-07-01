---
title: 'Agente: Instalación Zero Conf'
sidebar:
  order: 4
---

Esta documentación describe el funcionamiento y la arquitectura del **Agente Monsta**, una herramienta para extender el monitoreo de su plataforma a redes remotas y distribuidas, garantizando rendimiento y seguridad mediante el protocolo QUIC.

## Instalación del Agente para Windows

- Descargue el programa del agente:

| ![image-1660325708746.png](../../../../../assets/images/p139_image-1660325708746.png) | [**DESCARGA**](http://www.monsta.com.br/monsta/download/agent.msi)<br />[https://monsta.com.br/downloads/](https://www.monsta.com.br/monsta/download/agent.msi) |

- Conectado con un usuario con permisos de administrador, ejecute el instalador "agent.msi".
- Cuando se solicite, introduzca la clave de licencia del Monsta al que desea conectar el agente.

## Instalación desde la línea de comandos

El instalador **agent.msi** admite parámetros de línea de comandos para automatización. Integrado con la utilidad **msiexec**, permite instalar mediante **GPO**, eliminando la necesidad de intervención manual en la interfaz gráfica.

Opciones de la línea de comandos:

| `LICENSEKEY=\[chave de licença\]` | Indica la clave de licencia a la que el Agente debe conectarse. |
| `AGREE=\[Y\]` | Confirma la aceptación de los términos de uso. |

:::tip[Ejemplo de uso]

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::

:::note
La clave de licencia puede obtenerse en Monsta dentro del menú "Configuración" en la opción "Agentes". Se muestra en la esquina superior derecha.
:::

:::tip
**Firewall**:  

- No es necesario redirigir ningún puerto al servidor de Monsta;  
- Para garantizar conexiones directas, permita el tráfico saliente por el puerto **58580/UDP** en el firewall del servidor de Monsta hacia Internet;  
- Permita el acceso del servidor de Monsta a los hosts mind.monsta.com.br y agent.monsta.com.br.
:::

## Creación del Dispositivo

Una vez completada la instalación, el **Agente** aparecerá automáticamente en la pantalla de **Configuración** en el elemento **Agentes** con la identificación del host. El dispositivo monitorizado será **creado y listado al instante** en la pantalla de **Dispositivos** con el mismo nombre del host y estará listo para la configuración y la adición de nuevos monitores.

### Cómo monitorizar dispositivos mediante la conexión del Agente

Para cubrir toda la red remota con un solo agente, registre los nuevos dispositivos en Monsta y defina que el dispositivo está bajo la **jerarquía** del host donde está instalado el Agente.

Ejemplo de Jerarquía:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##