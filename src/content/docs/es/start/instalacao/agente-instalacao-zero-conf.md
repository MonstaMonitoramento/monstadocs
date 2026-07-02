---
title: "Agente: Instalación Zero Conf"
sidebar:
  order: 4
---
Esta documentación describe el funcionamiento y la arquitectura del **Agente Monsta**, una herramienta para extender el monitoreo de su plataforma a redes remotas y distribuidas, garantizando rendimiento y seguridad mediante el protocolo QUIC.

## Instalación del Agente en Windows

- Descargue el programa del agente:


|  | Descarga |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| ![Descarga del Agente](../../../../../assets/images/p139_image-1660325708746.png) | [https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi) |


- Inicie sesión con un usuario con permisos de administrador y ejecute el instalador "agent.msi".
- Cuando se le solicite, introduzca la clave de licencia de Monsta a la que desea conectar el agente.

## Instalación desde la línea de comandos

El instalador **agent.msi** admite parámetros de línea de comandos para automatización. Integrado con la utilidad **msiexec**, permite instalar mediante **GPO**, eliminando la necesidad de intervención manual en la interfaz gráfica.

Opciones de la línea de comandos:


| Opción | Descripción |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LICENSEKEY=[chave de licença]` | Indica la clave de licencia a la que el Agente debe conectarse. <aside class="starlight-aside starlight-aside--tip"><p class="starlight-aside__title">Consejo</p>La clave de licencia puede obtenerse en Monsta dentro del menú "Configuración" en la opción "Agentes". Se muestra en la esquina superior derecha.</aside>  |
| `AGREE=[Y]` | Confirma la aceptación de los términos de uso. |


**Ejemplo de uso:**

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

## Creación del Dispositivo

Una vez completada la instalación, el **Agente** aparecerá automáticamente en la pantalla de **Configuración** en el elemento **Agentes** con la identificación del host. El dispositivo monitorizado será **creado y listado instantáneamente** en la pantalla de **Dispositivos** con el mismo nombre del host y estará listo para la configuración y la adición de nuevos monitores.

### Cómo monitorizar dispositivos mediante la conexión del Agente

Para cubrir toda la red remota con un único agente, registre los nuevos dispositivos en Monsta y defina que el dispositivo está bajo la **jerarquía** del host donde está instalado el Agente.

Ejemplo de Jerarquía:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)



&nbsp;