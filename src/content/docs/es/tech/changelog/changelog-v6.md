---
title: Registro de cambios v6
description: Sigue el registro de cambios de la versión 6 de Monsta y conoce las nuevas funcionalidades, mejoras, correcciones y cambios realizados en cada actualización de la plataforma.
sidebar:
  order: 2
---
## Versión 6.0.19 Beta

**🔧Corrección**: **Alertas no enviadas**. Algunas alertas no se activaban incluso con el valor por encima del límite. Esto ocurría cuando el valor monitorizado raramente cambiaba: tras el reinicio del sistema, no estaba disponible en memoria y la alerta no podía confirmar el límite, permaneciendo inactiva.

## Versión 6.0.17

**✨Nuevo**: **Informes mensuales con Inteligencia Artificial**. Ahora, tu cuenta genera automáticamente informes mensuales enriquecidos con *insights* basados en IA.

![image.png](/src/assets/images/image-10.png)

**✨Nuevo**: **Ejecución remota vía PowerShell**. La Sonda permite la ejecución de comandos y *scripts* en PowerShell directamente desde la consola. Por motivos de seguridad, esta funcionalidad solo está disponible cuando el usuario autoriza su uso durante la instalación de la Sonda. Además, todos los comandos se ejecutan utilizando un **usuario con privilegios restringidos (no administrador)**.

:::note

Esta funcionalidad requiere la instalación de la versión más reciente de la Sonda Monsta, disponible en nuestro sitio.

:::

![image.png](/src/assets/images/image-5.png)

**✨Nuevo**: **Monitorización S.M.A.R.T.**. Añadimos soporte para la recolección de datos S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitiendo supervisar la integridad, la vida útil y los indicadores de salud del almacenamiento para identificar posibles fallos antes de que afecten al entorno. 

:::note

Esta funcionalidad requiere la instalación de la versión más reciente de la Sonda del Monsta, disponible en nuestro sitio.

:::

![image.png](/src/assets/images/image-9.png)

🔧**Corrección**: **Preservación del White Label en actualizaciones**. Corregido un comportamiento inesperado donde las actualizaciones del sistema restauraban el logotipo por defecto.

🔧**Corrección**: **Actualización en el estado de eventos.** Ahora, cuando un dispositivo o monitor alterna de estado entre aviso y crítico, solo el evento más reciente permanece marcado como no resuelto en la línea de tiempo, evitando la acumulación de pendientes para el mismo incidente.

**🔧Corrección**: **Reconexión de agentes tras restauración de backup**. Corregida la reconexión de agentes tras la restauración de copia de seguridad en instalaciones nuevas.

**🔧Corrección**: **Ajuste en el disparo de alarmas para monitores**. Corregido un problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Disponibilizados botones para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: Información sobre la clave y la licencia aparecía en blanco en algunos casos.

**🔧Corrección**: Monsta solicita la pantalla de login del área del cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs o redireccionamiento de puertos [Agente: Instalación Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para visión jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinâmico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular el área de cualquier unidad de medida.

**🔧Corrección**: Dispositivos sin uptime no enviaban alertas.

**🔧Corrección**: Las variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor por defecto informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de falla general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: Monitor booleano disparaba alarma con estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se envía en las recolecciones WMI.