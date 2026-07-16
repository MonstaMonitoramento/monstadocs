---
title: Registro de cambios v6
description: Sigue el Registro de cambios de la versión 6 de Monsta y conoce las nuevas
  funcionalidades, mejoras, correcciones y cambios realizados en cada
  actualización de la plataforma.
sidebar:
  order: 2
---
## Versión 6.0.16 Beta

**✨Nuevo**: **Informes Mensuales con Inteligencia Artificial**. Ahora, tu cuenta genera automáticamente informes mensuales enriquecidos con *insights* basados en IA.

![image.png](/src/assets/images/image-10.png)

**✨Nuevo**: **Ejecución Remota vía PowerShell**. La Sonda permite la ejecución de comandos y *scripts* en PowerShell directamente desde la consola. Para garantizar la seguridad de tu entorno, todos los comandos se procesan utilizando un **usuario con privilegios restringidos (no administrador)**.

![image.png](/src/assets/images/image-5.png)

**✨Nuevo**: **Monitorización S.M.A.R.T.**. Hemos añadido soporte para la recolección de datos S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitiendo supervisar la integridad, la vida útil y los indicadores de salud del almacenamiento para identificar posibles fallos antes de que afecten al entorno.

![image.png](/src/assets/images/image-9.png)

🔧**Corrección**: Corregido un comportamiento inesperado donde las actualizaciones del sistema afectaban indebidamente el logotipo personalizado definido por el usuario.

## Versión 6.0.13 Beta

**🔧Corrección**: Optimizado el tiempo de inicialización de la recolección de datos en nuevas instalaciones.

**🔧Corrección**: Corregida la reconexión de agentes tras la restauración de backup en la nube en nuevas instalaciones.

**🔧Corrección**: Corregido problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Disponibilizados botones para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: Información sobre la clave y licencia aparecía en blanco en algunos casos.

**🔧Corrección**: Monsta solicita la pantalla de login del área del cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs o reenvío de puertos [Agente: Instalación Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para visión jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinámico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular área en cualquier unidad de medida.

**🔧Corrección**: Dispositivos sin uptime no enviaban alertas.

**🔧Corrección**: Variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor por defecto informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de fallo general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: El monitor booleano generaba alarma con estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se envía en recolecciones WMI.
