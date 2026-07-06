---
title: Registro de cambios v6
sidebar:
  order: 2
---
## Versión 6.0.13 Beta

**🔧Corrección**: Optimizado el tiempo de inicialización de la recopilación de datos en nuevas instalaciones.

**🔧Corrección**: Corregida la reconexión de agentes tras la restauración de la copia de seguridad en la nube en nuevas instalaciones.

**🔧Corrección**: Corregido un problema puntual que impedía el disparo de alarmas en algunos monitores.

## Versión 6.0.9

**🔧Corrección**: Disponibles botones para eliminar agentes desconectados y bloqueados en la pantalla de gestión.

**🔧Corrección**: La información sobre la clave y la licencia aparecía en blanco en algunos casos.

**🔧Corrección**: Monsta solicitaba la pantalla de inicio de sesión del área de cliente para validar la clave en algunas situaciones.

## Versión 6.0.6

**✨Nuevo**: **Agentes** - Monitorización de redes remotas sin necesidad de VPNs o redirecciones de puertos [Agente: Instalación Zero Conf](/es/start/instalacao/agente-instalacao-zero-conf).

**✨Nuevo**: [Mapa para visualización jerárquica](/es/manual/dispositivos/visualizacao-em-mapa#mapa-dinâmico) con posibilidad de definir posiciones, añadir widgets y métricas.

**✨Nuevo**: Los paneles pueden estar disponibles para usuarios no administradores.

**✨Nuevo**: El informe de consumo puede calcular el área de cualquier unidad de medida.

**🔧Corrección**: Los dispositivos sin tiempo de actividad no enviaban alertas.

**🔧Corrección**: Las variables que informan el estado anterior en las plantillas de alerta no estaban habilitadas.

**🔧Corrección**: El valor predeterminado informado en los parámetros de un monitor devolvía nulo.

**🔧Corrección**: Mensaje de fallo general al añadir monitores automáticos con algunas plantillas.

**🔧Corrección**: Monitor booleano con alarma en estado falso cuando los límites estaban invertidos.

**🔧Corrección**: El namespace no se enviaba en las recopilaciones WMI.