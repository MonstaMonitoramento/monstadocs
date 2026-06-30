---
title: "Registro de cambios v2"
sidebar:
  order: 6
---

## Versión 2.0.11

**🔧Corrección**: Copia de seguridad - Durante la restauración de una *copia de seguridad*, Monsta podía cambiar el nombre de las plantillas.

## Versión 2.0.10

**✨Nuevo**: Vista en modo Árbol - Cambiado el valor mínimo de la opción "Tamaño de la Imagen" a 5.

**🔧Corrección**: No es posible añadir instancias con descripciones que contienen solo números.

**🔧Corrección**: Después de seleccionar un período grande para mostrar en monitores con métricas de verdadero/falso, Monsta muestra todo como Falso.

**🔧Corrección**: Bajo ciertas condiciones Monsta muestra un cambio de estado para un dispositivo eliminado.

**🔧Corrección**: Cuando un dispositivo padre está en estado "*Caído*", Monsta puede mostrar a sus hijos en estado "*Arriba*".

**🔧Corrección**: Cuando se añadía una nueva métrica a un monitor existente, al hacer clic en OK el sistema la reemplazaba por una copia de la métrica anterior.

## Versión 2.0.6

**🔧Corrección**: Bajo ciertas condiciones Monsta puede indicar el estado incorrecto para un monitor.

## Versión 2.0.5

**✨Nuevo**: Nueva identidad visual.

**✨Nuevo**: Nueva pantalla de Configuración con plantillas, imágenes, *copia de seguridad* y fuentes de datos.

**✨Nuevo**: Opción para añadir iconos o imágenes personalizadas para plantillas, dispositivos y monitores.

**✨Nuevo**: Acceso a fuentes de datos de los monitores.

**✨Nuevo**: Nuevas plantillas.

**✨Nuevo**: Nuevos elementos gráficos para los paneles.

**✨Nuevo**: Cliente para consultas SQL en bases MySQL y SQLite.

**✨Nuevo**: Posibilidad de añadir varios monitores en un único gráfico.

**✨Nuevo**: Monitores de tipo texto.

**✨Nuevo**: Edición del tamaño del paquete ICMP.

**✨Nuevo**: Nuevas funciones para los scripts.

**✨Nuevo**: Verificación de POP, IMAP y FTP con autenticación.

**✨Nuevo**: Verificación de cadenas en archivos de texto.

**🔧Corrección**: Durante la activación Monsta no aceptaba la clave de la licencia debido a la hora incorrecta del servidor.

**🔧Corrección**: La pantalla no soportaba más de 60 monitores por dispositivo.

**🔧Corrección**: Los monitores que no contenían en `SNMP` una `OID` de descripción no eran activados.

**🔧Corrección**: Algunos monitores entraban en alerta con el mensaje "sin valor", incluso estando activos.