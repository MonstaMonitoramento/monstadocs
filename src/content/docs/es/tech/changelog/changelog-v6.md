---
title: Registro de cambios v6
description: Sigue el registro de cambios de la versión 6 de Monsta y conoce las
  nuevas funcionalidades, mejoras, correcciones y cambios realizados en cada
  actualización de la plataforma.
sidebar:
  order: 2
---
## Versión 6.0.17

**✨Nuevo**: **Informes Mensuales con Inteligencia Artificial**. Ahora, su cuenta genera automáticamente informes mensuales enriquecidos con *insights* basados en IA.

![image.png](/src/assets/images/image-10.png)

**✨Nuevo**: **Ejecución remota vía PowerShell**. La Sonda permite la ejecución de comandos y *scripts* en PowerShell directamente desde la consola. Por motivos de seguridad, esta función se habilita únicamente cuando el usuario autoriza su uso durante la instalación de la Sonda. Además, todos los comandos se ejecutan usando un **usuario con privilegios restringidos (no administrador)**.

![image.png](/src/assets/images/image-5.png)

**✨Nuevo**: **Monitorización S.M.A.R.T.**. Hemos añadido soporte para la recopilación de datos S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitiendo seguir la integridad, la vida útil y los indicadores de salud del almacenamiento para identificar posibles fallos antes de que afecten al entorno.

![image.png](/src/assets/images/image-9.png)

🔧**Corrección**: Corregido un comportamiento inesperado en el que las actualizaciones del sistema afectaban indebidamente al logotipo personalizado definido por el usuario (White Label).

🔧**Corrección**: **Actualización en el estado de eventos.** Ahora, cuando un dispositivo o monitor cambia su estado entre aviso y crítico, solo el evento más reciente permanece marcado como no resuelto en la línea de tiempo, evitando la acumulación de pendientes para el mismo incidente.

**🔧Corrección**: **Reconexión de agentes tras copia de seguridad**. Se corrigió la reconexión de agentes después de la restauración del respaldo en la nube en nuevas instalaciones.

**🔧Corrección**: **Ajuste en el disparo de alarmas para monitores**. Se corrigió un problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Botones disponibles para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: Información sobre la clave y la licencia aparecía en blanco en algunos casos.

**🔧Corrección**: Monsta solicitaba la pantalla de inicio de sesión del área del cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs o reenvío de puertos [Agente: Instalación Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para visualización jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinámico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular el área en cualquier unidad de medida.

**🔧Corrección**: Dispositivos sin tiempo de actividad no enviaban alertas.

**🔧Corrección**: Las variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor predeterminado informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de fallo general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: Monitor booleano generaba alarma con estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se enviaba en las recopilaciones WMI.