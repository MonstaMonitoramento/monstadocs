---
title: Registro de cambios v6
description: Sigue el Registro de cambios de la versión 6 de Monsta y conoce las nuevas
  funcionalidades, mejoras, correcciones y cambios realizados en cada
  actualización de la plataforma.
sidebar:
  order: 2
---
## Versión 6.0.17

**✨Nuevo**: **Informes mensuales con Inteligencia Artificial**. Ahora, su cuenta genera automáticamente informes mensuales enriquecidos con *insights* basados en IA.

![image.png](/src/assets/images/image-10.png)

**✨Nuevo**: **Ejecución remota vía PowerShell**. La Sonda permite la ejecución de comandos y *scripts* en PowerShell directamente desde la consola. Por motivos de seguridad, esta función solo está disponible cuando el usuario autoriza su uso durante la instalación de la Sonda. Además, todos los comandos se ejecutan usando un **usuario con privilegios restringidos (no administrador)**.

![image.png](/src/assets/images/image-5.png)

**✨Nuevo**: **Monitorización S.M.A.R.T.**. Añadimos soporte para la recopilación de datos S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitiendo supervisar la integridad, la vida útil y los indicadores de salud del almacenamiento para identificar posibles fallos antes de que afecten al entorno.

![image.png](/src/assets/images/image-9.png)

🔧**Corrección**: **Preservación del White Label en las actualizaciones**. Corregido un comportamiento inesperado en el que las actualizaciones del sistema restablecían el logotipo predeterminado.

🔧**Corrección**: **Actualización en el estado de eventos.** Ahora, cuando un dispositivo o monitor cambia de estado entre aviso y crítico, solo el evento más reciente permanece marcado como no resuelto en la cronología, evitando la acumulación de pendientes para el mismo incidente.

**🔧Corrección**: **Reconexión de Agentes tras Backup**. Corregida la reconexión de agentes después de la restauración de una copia de seguridad en la nube en nuevas instalaciones.

**🔧Corrección**: **Ajuste en el Disparo de Alarmas para Monitores**. Corregido un problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Se han habilitado botones para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: La información sobre la clave y la licencia aparecía en blanco en algunos casos.

**🔧Corrección**: Monsta solicitaba la pantalla de inicio de sesión del área de cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs ni redirección de puertos [Agente: Instalación Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para visión jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinâmico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular el área de cualquier unidad de medida.

**🔧Corrección**: Los dispositivos sin uptime no enviaban alertas.

**🔧Corrección**: Las variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor predeterminado informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de fallo general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: Monitor booleano activaba la alarma con estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se enviaba en las recopilaciones WMI.