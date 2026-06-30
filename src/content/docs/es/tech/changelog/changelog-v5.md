---
title: "Registro de cambios v5"
sidebar:
  order: 3
---

## Versión 5.1.22

**🔧Corrección**: Evento de fallo del dispositivo hijo no envía alerta tras la recuperación del fallo del dispositivo padre.

**🔧Corrección**: Permisos de dispositivos para usuarios que no son administradores.

**🔧Corrección**: El widget Barra de Indicador pierde el monitor seleccionado al editar el panel.

**🔧Corrección**: El puerto utilizado por `Monagent` puede provocar un desbordamiento de memoria con paquetes malformados en servidores sin firewall habilitado.

**🔧Corrección**: En algunos casos aparece una pantalla en blanco al acceder a la opción de monitores automáticos.

## Versión 5.1.21

**🔧Corrección**: El grupo de alertas en la nube no guarda cambios la primera vez.

**🔧Corrección**: *Widgets Piechart* y *Doughnutchart* añaden dispositivos desactivados.

**🔧Corrección**: Algunos widgets no se mostraban en la publicación del panel.

## Versión 5.1.20

**✨Nuevo**: Caché inteligente para consultas `SNMP`.

**✨Nuevo**: Indicador de evento no resuelto en la Línea del Tiempo.

**✨Nuevo**: Pantalla responsiva para móviles.

**✨Nuevo**: Nuevos certificados aceptados para conexiones por HTTPS.

**✨Nuevo**: Nuevos widgets para los paneles.

**✨Nuevo**: Actualización automática de nuevas versiones.

**✨Nuevo**: Nuevas plantillas.

**✨Nuevo**: Cálculo del área del gráfico (los ISP pueden reportar el tráfico en MB a la Anatel).

**🔧Corrección**: Las plantillas se importaban sin algunas métricas.

**🔧Corrección**: IPv6 devolvía error en las recopilaciones por `SNMP`.

**🔧Corrección**: Los monitores no permitían cambiar la unidad de medida.

**🔧Corrección**: Error de kernel al eliminar algunos dispositivos.

**🔧Corrección**: Los mapas no mostraban dispositivos duplicados/creados en su pantalla.

**🔧Corrección**: `SNMP` no recopilaba información en redes IPv6.

**🔧Corrección**: No era posible cambiar la unidad de magnitud de monitores existentes en los dispositivos.

**🔧Corrección**: Instancias con comillas en el nombre provocaban fallos en las recopilaciones.

**🔧Corrección**: Los cambios en paneles duplicados afectaban al original.

## Versión 5.0.4

**🔧Corrección**: Comportamiento incorrecto del envío de alertas cuando el estado normal no está marcado.

## Versión 5.0.3

**🔧Corrección**: Restaurar copias de seguridad no muestra archivos.

## Versión 5.0

**✨Nuevo**: Nuevo kernel del sistema controla las llamadas para las recolecciones de monitores, con capacidad aumentada para miles de consultas simultáneas.

**✨Nuevo**: Nuevos componentes para paneles.

**✨Nuevo**: Nuevas plantillas.

**✨Nuevo**: Control contra exceso de consultas para dispositivos lentos.

**✨Nuevo**: Automatización del certificado para acceso seguro con el *Let's Encrypt*.

**✨Nuevo**: Modo nocturno.

**✨Nuevo**: Las plantillas de alerta pueden crearse y configurarse de forma individual.

**✨Nuevo**: Configuración de sonidos personalizada por dispositivo o monitor.

**🔧Corrección**: Algoritmo para monitores automáticos.

**🔧Corrección**: Rotación de logs de la base de datos.

**🔧Corrección**: Inicio de sesión automático cuando hay pérdida de conexión con el *browser*.