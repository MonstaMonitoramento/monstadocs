---
title: Registro de cambios v6
description: Sigue el registro de cambios de la versión 6 de Monsta y conoce las nuevas
  funcionalidades, mejoras, correcciones y modificaciones realizadas en cada
  actualización de la plataforma.
sidebar:
  order: 2
---
## Versión 6.0.22 Beta

🔧**Corrección**: **Métrica en estado crítico**. Corregido un fallo en el que métricas con límite máximo definido mediante lectura dinámica del equipo entraban indebidamente en estado crítico bajo determinadas condiciones.

🔧**Corrección**: **Fallas en la recolección WMI**. Corregidos fallos de lectura e inconsistencias puntuales en los datos recopilados por la sonda de Monsta.

## Versión 6.0.21 Beta

🔧**Corrección**: **Fallo al añadir un panel**. Resuelto el error de kernel que impedía la inclusión/eliminación de un panel a un usuario antiguo en la interfaz de gestión.

🔧**Corrección**: **Listado de paneles en blanco**. Corregido el problema que provocaba que la lista de paneles quedara en blanco justo después de la adición de un nuevo registro en la edición de usuarios.

## Versión 6.0.20 Beta

🔧**Corrección**: **Fallo en las recopilaciones con la sonda**. Determinados monitores de la sonda para Windows se congelaban de forma aleatoria y dejaban de recopilar datos.

## Versión 6.0.19 Beta

**🔧Corrección**: **Alertas no enviadas**. Algunos alertas no se activaban incluso con el valor por encima del límite. Esto ocurría cuando el valor monitorizado raramente cambiaba: tras el reinicio del sistema, no estaba disponible en memoria y la alerta no podía confirmar el límite, permaneciendo inactiva.

## Versión 6.0.17

**✨Nuevo**: **Informes Mensuales con Inteligencia Artificial**. Ahora, su cuenta genera automáticamente informes mensuales enriquecidos con *insights* basados en IA.

![image.png](/src/assets/images/image-10.png)

**✨Nuevo**: **Ejecución Remota vía PowerShell**. La Sonda permite la ejecución de comandos y *scripts* en PowerShell directamente desde la consola. Por motivos de seguridad, esta funcionalidad se habilita solo cuando el usuario autoriza su uso durante la instalación de la Sonda. Además, todos los comandos se ejecutan utilizando un **usuario con privilegios restringidos (no administrador)**.

:::note

Este recurso requiere la instalación de la versión más reciente de la Sonda Monsta, disponible en nuestro sitio web.

:::

![image.png](/src/assets/images/image-5.png)

**✨Nuevo**: **Monitorización S.M.A.R.T.**. Añadimos soporte para la recopilación de datos S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitiendo supervisar la integridad, la vida útil y los indicadores de salud del almacenamiento para identificar posibles fallos antes de que afecten al entorno.

:::note

Este recurso requiere la instalación de la versión más reciente de la Sonda de Monsta, disponible en nuestro sitio web.

:::

![image.png](/src/assets/images/image-9.png)

🔧**Corrección**: **Preservación del White Label en las actualizaciones**. Corregido un comportamiento inesperado en el que las actualizaciones del sistema restauraban el logotipo predeterminado.

🔧**Corrección**: **Actualización en el estado de eventos.** Ahora, cuando un dispositivo o monitor cambia de estado entre advertencia y crítico, solo el evento más reciente permanece marcado como no resuelto en la línea temporal, evitando la acumulación de pendientes para el mismo incidente.

**🔧Corrección**: **Reconexión de Agentes tras Backup**. Corregida la reconexión de agentes después de la restauración de una copia de seguridad en la nube en nuevas instalaciones.

**🔧Corrección**: **Ajuste en el Disparo de Alarmas para Monitores**. Corregido un problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Disponibles botones para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: Información sobre la clave y la licencia aparecía en blanco en algunos casos.

**🔧Corrección**: Monsta solicitaba la pantalla de inicio de sesión del área de cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs ni redireccionamiento de puertos [Agente: Instalación Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para vista jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinámico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular áreas en cualquier unidad de medida.

**🔧Corrección**: Los dispositivos sin tiempo de actividad no enviaban alertas.

**🔧Corrección**: Las variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor por defecto informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de fallo general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: El monitor booleano alarmaba con estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se enviaba en las recolecciones WMI.
