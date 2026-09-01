---
title: Registro de cambios v6
description: Sigue el Registro de cambios de la versión 6 de Monsta y conoce las nuevas
  funcionalidades, mejoras, correcciones y cambios realizados en cada
  actualización de la plataforma.
sidebar:
  order: 2
---
## Versión 6.0.20 Beta

🔧**Corrección**: **Fallo en las recogidas con la sonda**. Determinados monitores de la sonda para Windows se congelan de forma aleatoria y dejan de recopilar datos.

## Versión 6.0.19 Beta

**🔧Corrección**: **Alertas no enviadas**. Algunas alertas no se activaban aunque el valor superara el límite. Esto ocurría cuando el valor monitorizado cambiaba muy raramente: tras el reinicio del sistema, no estaba disponible en memoria y la alerta no podía confirmar el límite, permaneciendo inactiva.

## Versión 6.0.17

**✨Nuevo**: **Informes mensuales con Inteligencia Artificial**. Ahora, tu cuenta genera automáticamente informes mensuales enriquecidos con *insights* basados en IA.

![image.png](/src/assets/images/image-10.png)

**✨Nuevo**: **Ejecución remota a través de PowerShell**. La Sonda permite la ejecución de comandos y *scripts* de PowerShell directamente desde la consola. Por motivos de seguridad, esta funcionalidad solo se habilita cuando el usuario autoriza su uso durante la instalación de la Sonda. Además, todos los comandos se ejecutan utilizando un **usuario con privilegios restringidos (sin privilegios de administrador)**.

:::note

Este recurso requiere la instalación de la versión más reciente de la Sonda Monsta, disponible en nuestro sitio.

:::

![image.png](/src/assets/images/image-5.png)

**✨Nuevo**: **Monitorización S.M.A.R.T.**. Añadimos soporte para la recopilación de datos S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitiendo supervisar la integridad, la vida útil y los indicadores de salud del almacenamiento para identificar posibles fallos antes de que afecten al entorno.

:::note

Este recurso requiere la instalación de la versión más reciente de la Sonda del Monsta, disponible en nuestro sitio.

:::

![image.png](/src/assets/images/image-9.png)

🔧**Corrección**: **Preservación del White Label en actualizaciones**. Corregido un comportamiento inesperado en el que las actualizaciones del sistema restauraban el logotipo predeterminado.

🔧**Corrección**: **Actualización en el estado de eventos.** Ahora, cuando un dispositivo o monitor cambia de estado entre aviso y crítico, solo el evento más reciente permanece marcado como no resuelto en la línea de tiempo, evitando la acumulación de pendientes para el mismo incidente.

**🔧Corrección**: **Reconexión de agentes tras la copia de seguridad**. Corregida la reconexión de agentes tras la restauración de la copia de seguridad en la nube en nuevas instalaciones.

**🔧Corrección**: **Ajuste en el disparo de alarmas para monitores**. Corregido un problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Habilitados botones para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: La información sobre la clave y la licencia aparecía en blanco en algunos casos.

**🔧Corrección**: Monsta solicita la pantalla de inicio de sesión del área de cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs ni redireccionamiento de puertos [Agente: Instalación Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para vista jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinámico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular el área de cualquier unidad de medida.

**🔧Corrección**: Dispositivos sin uptime no enviaban alertas.

**🔧Corrección**: Las variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor predeterminado informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de fallo general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: El monitor booleano activaba alarma con estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se envía en las recogidas WMI.
