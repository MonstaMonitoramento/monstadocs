---
title: "Sonda: Monitorización de Windows"
sidebar:
  order: 5
---

Maximice la eficiencia y la estabilidad de su red con nuestra Sonda de Monitorización WMI para Windows. Desarrollada para ofrecer una visión detallada del rendimiento y la salud de sus servidores y estaciones de trabajo Windows, esta herramienta esencial recopila métricas cruciales a través de la API para WMI (Windows Management Instrumentation).

## ¿Para qué sirve la Sonda?

Imagine tener una radiografía de su entorno Windows en tiempo real. Nuestra sonda actúa de ese modo, permitiéndole:

- Supervise el rendimiento del sistema: Controle el uso de CPU, memoria RAM, disco duro y red para identificar cuellos de botella y optimizar recursos.
- Detecte problemas proactivamente: Reciba alertas sobre eventos críticos, fallos de servicios y otros indicadores de posibles inestabilidades antes de que afecten a sus usuarios.
- Analice el consumo de recursos: Entienda cómo las aplicaciones y procesos utilizan los recursos del sistema para una planificación de capacidad más inteligente.
- Visualice datos importantes: Integra las métricas recopiladas con Monsta para que pueda crear dashboards personalizados y detallados.
- Diagnostique problemas de forma remota: Obtenga información valiosa para resolver incidentes rápida y eficazmente, incluso sin acceso físico a la máquina.

**Integración perfecta**: Diseñada específicamente para el entorno Windows, aprovechando al máximo los recursos de la API WMI.

**Ligera y eficiente**: Bajo consumo de recursos, garantizando que el monitoreo no impacte el rendimiento del sistema monitorizado.

**Instalación fácil** y configuración: Un proceso simple e intuitivo para poner su sonda en funcionamiento rápidamente.

**Datos precisos** y fiables: Recopilación de información detallada y en tiempo real para un análisis preciso de su infraestructura.

**Flexibilidad**: Adapte la recopilación de métricas a sus necesidades específicas.

Con nuestra Sonda de Monitorización WMI para Windows, tendrá el control total sobre la salud y el rendimiento de sus sistemas Windows, garantizando una infraestructura de TI robusta, eficiente y siempre disponible. ¡Empiece ahora mismo a monitorizar con inteligencia!

## Instalación de la Sonda

1. Descargue el programa de la sonda en el sistema operativo Windows que desea monitorizar;


| | |
| --- | --- |
| ![image-1660325708746.png](../../../../../assets/images/p139_image-1660325708746.png) | [**DOWNLOAD**](https://www.monsta.com.br/monsta/download/MonstaProbe.exe "Monsta - Sonda Coletora")<br />[https://www.monsta.com.br/monsta/download/MonstaProbe.exe (64bits)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) |
2. Con sesión iniciada con un usuario administrador, ejecute el instalador "monstaprobe.exe" (consulte [Instalación por línea de comandos](#instalación-por-línea-de-comandos) para instalación en lote);
3. Configure los parámetros de puerto y contraseña que se le solicitarán durante la instalación.  
      
    

:::note
**port**: Es el puerto que será utilizado por la sonda para que Monsta se conecte. El valor por defecto es **7744** (TCP).  
**password**: Es la contraseña de autenticación para la sonda en el equipo donde se instala. El valor por defecto es `monsta@dm`.
:::



## Configuración en Monsta

Dentro de Monsta, al crear un dispositivo, simplemente configúrelo para utilizar las plantillas de Microsoft.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

Y rellene el campo "Usuário WMI" con cualquier información (será descartado posteriormente) y el campo "Senha WMI" con la contraseña indicada durante la instalación de la sonda.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

Tras crear el dispositivo ya puede utilizar los monitores disponibles de la plantilla.

## Instalación por línea de comandos

El instalador MonstaProbe.exe acepta opciones en la línea de comandos. Puede utilizarlas para automatizar la instalación en una red mediante una GPO, sin necesidad de interacción con la interfaz gráfica.

| Opção &nbsp; &nbsp; &nbsp; &nbsp; | Descripción |
| --- | --- |
| `--agree` | Acepta el término de uso de la sonda colectora. |
| `--port` | Indica el puerto que será utilizado por la sonda colectora. Si no se indica, el valor por defecto será 7744 (TCP). |
| `--passwd` | Asigna la contraseña que utilizará la sonda colectora. La contraseña por defecto será *monsta@dm* si no se proporciona. |





:::tip[Ejemplo de uso]
```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```
:::



- - - - - -