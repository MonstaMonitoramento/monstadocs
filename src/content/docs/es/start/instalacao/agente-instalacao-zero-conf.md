---
title: 'Agente: Instalación Zero Conf'
sidebar:
  order: 4
---

Esta documentación describe el funcionamiento y la arquitectura del **Agente Monsta**, una herramienta para ampliar el monitoreo de su plataforma a redes remotas y distribuidas, garantizando rendimiento y seguridad mediante el protocolo QUIC.

## Instalação do Agente para Windows

- Baixe o programa do agente:

|  | Link para download |
| --- | --- |
| [![Descarga del Agente](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/agent.msi) | [https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi) |

- Con sesión iniciada con un usuario con permisos de administrador, ejecute el instalador "agent.msi".
- Cuando se le solicite, introduzca la clave de licencia de Monsta a la que desea conectar el agente.

## Instalação pela linha de comando

El instalador **agent.msi** admite parámetros de línea de comandos para automatización. Integrado con la utilidad **msiexec**, permite instalar vía **GPO**, eliminando la necesidad de intervención manual en la interfaz gráfica.

Opções da linha de comando:

| Opção | Descrição |
| --- | --- |
| `LICENSEKEY=[chave de licença]` | Indica la clave de licencia a la que deberá conectarse el Agente. <aside class="starlight-aside starlight-aside--tip"><p class="starlight-aside__title">Consejo</p>La clave de licencia puede obtenerse en Monsta dentro del menú "Configuração" en la opción "Agentes". Se muestra en la esquina superior derecha.</aside> |
| `AGREE=[Y]` | Confirma la aceptación de los términos de uso. |

**Exemplo de uso:**

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::tip
**Firewall**:  

- No es necesario redirigir ningún puerto al servidor de Monsta;  
- Para garantizar conexiones directas, abra el puerto **58580/UDP** (salida) en el firewall de su servidor Monsta hacia Internet;  
- Permita el acceso del servidor de Monsta a los hosts mind.monsta.com.br y agent.monsta.com.br.
:::

## Criação do Dispositivo

Una vez completada la instalación, el **Agente** aparecerá automáticamente en la pantalla de **Configuración** en el ítem **Agentes** con la identificación del host. El dispositivo monitorizado será **creado y listado al instante** en la pantalla de **Dispositivos** con el mismo nombre del host y estará listo para la configuración y la adición de nuevos monitores.

### Como Monitorar Dispositivos pela Conexão do Agente

Para cubrir toda la red remota con un único agente, registre los nuevos dispositivos en Monsta y defina que el dispositivo está bajo la **jerarquía** del host donde el Agente está instalado.

Exemplo de Hierarquia:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##