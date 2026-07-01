---
title: 'Sonda: Monitorización de Windows'
sidebar:
  order: 5
---

A **Sonda Monsta** es un software de recopilación local diseñado para instalarse directamente en servidores y dispositivos **Windows, Linux y Raspberry PI**. Su función principal es recopilar métricas de rendimiento, integridad y disponibilidad del sistema anfitrión, funcionando como una extensión nativa de recopilación para la plataforma Monsta.

## Características e Capacidades Técnicas

### 1. Arquitectura Pasiva (Bajo Demanda)

La sonda opera estrictamente bajo un modelo **pasivo de petición y respuesta**. No inicia comunicaciones con la red de forma autónoma; el tráfico de datos ocurre solo cuando Monsta se pone en contacto para realizar el _polling_ (solicitud de recopilación).

### 2. Integración con la API WMI (Windows)

En entornos Microsoft, la sonda utiliza de forma nativa la API WMI (_Windows Management Instrumentation_), permitiendo extraer contadores de rendimiento detallados de servidores y estaciones de trabajo sin la necesidad de configuraciones complejas de gestión remota en la red.

### 3. Ejecución de Comandos y Scripts PowerShell

La sonda actúa como un brazo de automatización directamente en el sistema operativo del host.

- **Comandos Locales:** Puede ejecutar comandos directamente en el sistema operativo anfitrión.  
- **Scripts PowerShell:** Admite la ejecución de scripts personalizados, permitiendo monitorizar aplicaciones específicas o crear rutinas de validación a medida.

### 4. Diagnóstico de Salud de Discos Físicos

El software posee la capacidad de leer indicadores de hardware y el estado de integridad de los discos duros y SSD instalados en el dispositivo. Esto posibilita la identificación temprana de fallos físicos (_bad blocks_) y degradación del almacenamiento.

### 5. Comunicación Cifrada

Todo el intercambio de información entre el servidor central de Monsta y la Sonda instalada en el dispositivo está **100% cifrado**, garantizando la seguridad de las métricas transmitidas e impidiendo la interceptación de datos sensibles de la infraestructura.

## Instalação da Sonda

1. Descargue el programa de la sonda en el sistema operativo Windows que desee supervisar;

|  | Link para download |
| --- | --- |
| [![Download da Sonda](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) | [https://www.monsta.com.br/monsta/download/MonstaProbe.exe](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) |

2. Conectado con un usuario administrador, ejecute el instalador "monstaprobe.exe" (consulte [Instalação pela linha de comando](#instalação-pela-linha-de-comando) para instalación en lote);
3. Configure los parámetros de puerto y contraseña que se solicitarán durante la instalación.  

## Instalação pela linha de comando

El instalador MonstaProbe.exe acepta opciones en la línea de comandos. Puede utilizarlas para automatizar la instalación en una red mediante una GPO, sin necesidad de interacción con la interfaz gráfica.

| Opção | Descrição |
| --- | --- |
| `--agree` | Acepta el acuerdo de uso de la sonda recolectora. |
| `--port` | Indica el puerto que será utilizado por la sonda recolectora. Si no se especifica, el valor por defecto será 7744 (TCP). |
| `--passwd` | Asigna la contraseña que será utilizada por la sonda recolectora. La contraseña por defecto será *monsta@dm* si no se especifica. |

**Exemplo de uso**

```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```

:::note
**port**: Es el puerto que será utilizado por la sonda para que Monsta se conecte. El valor por defecto es **7744** (TCP).  
**password**: Es la contraseña de autenticación para la sonda en el equipo instalado. El valor por defecto es `monsta@dm`.
:::

## Configuração no Monsta

Dentro de Monsta, al crear un dispositivo, simplemente configúrelo para utilizar las plantillas de Microsoft.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

Y rellene el campo "Usuário WMI" con cualquier información (será descartado posteriormente) y el campo "Senha WMI" con la contraseña indicada durante la instalación de la sonda.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

Tras crear el dispositivo ya puede utilizar los monitores disponibles de la plantilla.

##