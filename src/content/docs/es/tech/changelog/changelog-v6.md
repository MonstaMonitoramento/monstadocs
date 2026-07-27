---
title: Registro de cambios v6
description: Sigue el registro de cambios de la versión 6 de Monsta y conoce las
  nuevas funcionalidades, mejoras, correcciones y cambios realizados en cada
  actualización de la plataforma.
sidebar:
  order: 2
---
## Versión 6.0.17 Beta

🔧**Corrección**: **Actualización en el estado de eventos**. Ahora, cuando un dispositivo o monitor cambia de estado entre aviso y crítico, solo el evento más reciente permanece marcado como no resuelto en la línea de tiempo, evitando la acumulación de pendientes para el mismo incidente.

🔧**Corrección**: **Corrección en alertas con valores decimales**. Ajustada la lectura de límites para que las alertas consideren correctamente los decimales, evitando activaciones incorrectas en métricas fraccionadas.

**🔧Corrección**: **Ajuste en alertas porcentuales**. Corregido el límite de configuración para permitir que la barra porcentual se posicione en **0%**.

## Versión 6.0.16 Beta

**✨Nuevo**: **Informes mensuales con Inteligencia Artificial**. Ahora, su cuenta genera automáticamente informes mensuales enriquecidos con *insights* basados en IA.

![image.png](/src/assets/images/image-10.png)

**✨Nuevo**: **Ejecución remota vía PowerShell**. La Sonda permite la ejecución de comandos y *scripts* en PowerShell directamente desde la consola. Para garantizar la seguridad de su entorno, todos los comandos se procesan utilizando un **usuario con privilegios restringidos (no administrador)**.

![image.png](/src/assets/images/image-5.png)

**✨Nuevo**: **Monitorización S.M.A.R.T.**. Añadimos soporte para la recopilación de datos S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitiendo seguir la integridad, la vida útil y los indicadores de salud del almacenamiento para identificar posibles fallos antes de que afecten al entorno.

![image.png](/src/assets/images/image-9.png)

🔧**Corrección**: Corregido un comportamiento inesperado en el que las actualizaciones del sistema afectaban indebidamente al logotipo personalizado definido por el usuario.

## Versión 6.0.13 Beta

**🔧Corrección**: Optimizado el tiempo de inicialización de la recopilación de datos en nuevas instalaciones.

**🔧Corrección**: Corregida la reconexión de agentes tras la restauración de la copia de seguridad en la nube en nuevas instalaciones.

**🔧Corrección**: Corregido problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Se han añadido botones para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: Información sobre la clave y la licencia aparece en blanco en algunos casos.

**🔧Corrección**: Monsta solicita la pantalla de inicio de sesión del área de cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs o reenvío de puertos [Agente: Instalação Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para visión jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinámico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular el área de cualquier unidad de medida.

**🔧Corrección**: Los dispositivos sin tiempo de actividad no enviaban alertas.

**🔧Corrección**: Las variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor predeterminado informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de fallo general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: Monitor booleano alarmaba con estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se envía en recopilaciones WMI.