---
title: "Sonda: Instalación"
description: Aprenda cómo instalar la Sonda de Monsta en Windows para realizar
  monitorizaciones remotas y ampliar el alcance de la plataforma en su
  infraestructura.
sidebar:
  order: 5
---
A **Sonda Monsta** es un software de recolección local diseñado para instalarse directamente en servidores y dispositivos **Windows** (próximamente para **Linux** y **Raspberry PI**). Su función principal es recopilar métricas de rendimiento, integridad y disponibilidad del sistema anfitrión, funcionando como una extensión nativa de recolección para la plataforma Monsta.

## Características y Capacidades Técnicas

### 1. Arquitectura Pasiva (Bajo Demanda)

La sonda opera estrictamente bajo un modelo **pasivo de petición y respuesta**. No inicia comunicaciones con la red de forma autónoma; el tráfico de datos se produce únicamente cuando Monsta contacta para realizar el *polling* (solicitud de recolección).

### 2. Integración con la API WMI (Windows)

En entornos Microsoft, la sonda utiliza de forma nativa la API WMI (*Windows Management Instrumentation*), permitiendo extraer contadores de rendimiento detallados de servidores y estaciones de trabajo sin la necesidad de configuraciones complejas de gestión remota en la red.

### 3. Ejecución de Comandos y Scripts PowerShell

La sonda actúa como un brazo de automatización directamente en el sistema operativo del host.

- **Comandos Locales:** Puede ejecutar comandos directamente en el sistema operativo anfitrión.
- **Scripts PowerShell:** Soporta el disparo de scripts personalizados, permitiendo monitorizar aplicaciones específicas o crear rutinas de validación a medida.

### 4. Diagnóstico de Salud de Discos Físicos

El software tiene la capacidad de leer indicadores de hardware y el estado de integridad de los discos duros y SSD instalados en el dispositivo. Esto posibilita la identificación temprana de fallos físicos (*bad blocks*) y degradación del almacenamiento.

### 5. Comunicación Cifrada

Todo el intercambio de información entre el servidor central de Monsta y la Sonda instalada en el dispositivo está **100% cifrado**, garantizando la seguridad de las métricas transmitidas e impidiendo la interceptación de datos sensibles de la infraestructura.

## Instalación de la Sonda (Windows)

1. Descargue el programa de la sonda en el sistema operativo Windows que desea monitorizar;


|  | Descarga |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ![Download da Sonda](/src/assets/images/p139_image-1660325708746.png) | [https://www.monsta.com.br/monsta/download/MonstaProbe.msi](https://www.monsta.com.br/monsta/download/MonstaProbe.msi) |


1. Con sesión iniciada con un usuario administrador, ejecute el instalador "monstaprobe.msi";
2. Configure los parámetros de puerto y contraseña que se solicitarán durante la instalación.

### Instalación desde la línea de comandos

El instalador MonstaProbe.exe acepta opciones en la línea de comandos. Puede utilizarlas para automatizar la instalación en una red mediante una GPO, sin necesidad de interacción con la interfaz gráfica.


| Opción &nbsp; &nbsp; &nbsp; &nbsp; | Descripción |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `AGREE=Y` | Acepta el término de uso de la sonda recolectora. |
| `PORT=<num>` | Indica el puerto que usará la sonda recolectora. Si no se especifica, el valor por defecto será 7743 (TCP). |
| `PASSWD=<password>` | Asigna la contraseña que usará la sonda recolectora. |
| `REMOTE_EXEC=1` | Habilita la ejecución de comandos y scripts en PowerShell. |


**Ejemplo de uso**:

```powershell
msiexec /i MonstaProbe.msi /qn AGREE=Y PORT=7743 PASSWD=MinhaSenha REMOTE_EXEC=1
```

### Comandos para cambiar la configuración

Los parámetros de la sonda pueden ajustarse vía línea de comandos.


| Opción | Descripción |
| ----------------- | ----------------------------------------------------- |
| `--cfg` | Indica que la configuración será modificada. |
| `--port` | Redefine el puerto que la sonda deberá escuchar. |
| `--passwd` | Redefine la contraseña. |
| `--remote-exec 1` | Habilita la ejecución de comandos y scripts PowerShell. |


**Ejemplo de uso**:

```powershell
"C:\Program Files (x86)\MonstaProbe\monsta_probe.exe" --cfg --port 7744 --passwd NovaSenha --remote-exec 1
```

### Ejecución Remota de Scripts: Seguridad y Permisos

La ejecución de comandos y scripts en PowerShell a través de la Sonda de Monsta se realiza en el contexto exclusivo del usuario local **monsta-probe**. Este usuario se crea automáticamente durante el proceso de instalación y opera estrictamente con permisos de usuario estándar, garantizando que todos los servicios, tareas y scripts disparados por la plataforma se ejecuten de forma aislada, sin privilegios de administrador ni acceso a archivos sensibles del sistema operativo.

### Configuración en Monsta

Dentro de Monsta, al crear un dispositivo, simplemente configúrelo para usar las plantillas de Microsoft.

![image-1741105397485.png](/src/assets/images/p68_image-1741105397485.png)

Y rellene el campo "Usuário WMI" con cualquier información (será descartada en el futuro) y el campo "Senha WMI" con la contraseña indicada durante la instalación de la sonda.

![image-1741105450183.png](/src/assets/images/p68_image-1741105450183.png)

Después de crear el dispositivo ya puede utilizar los monitores disponibles de la plantilla.