---
title: "Registro de cambios v3"
sidebar:
  order: 5
---

## Versión 3.1.7

**🔧Corrección**: Al añadir monitores con una gran cantidad de instancias, Monsta muestra un mensaje de timeout.

## Versión 3.1.6

**🔧Corrección**: En algunos casos ocurre fuga de memoria y fallo en la ejecución de algunos monitores.

## Versión 3.1.5

**✨Nuevo**: Número de intentos incrementado a 120.

**✨Nuevo**: Filtro "Buscar Dispositivo" busca también por dirección IP.

**✨Nuevo**: Tipo String acepta valores en hexadecimal.

**✨Nuevo**: Tipo String acepta textos.

**✨Nuevo**: Búsqueda por WMI acepta otros namespaces.

**✨Nuevo**: La función `return()` en un script puede forzar el estado de una métrica en un monitor.

**✨Nuevo**: Aviso sonoro para cambios de estado.

**✨Nuevo**: Posibilidad de publicar un enlace a un monitor sin necesidad de iniciar sesión.

**✨Nuevo**: Plantilla Unbound - DNS Server.

**✨Nuevo**: Plantilla Intelbras - Switches.

**✨Nuevo**: Plantilla Microsoft - Windows (Inventario).

**✨Nuevo**: Monitores "Servicios en Ejecución", "Estado de la Placa Base", "Estado de la Memoria Física", "Estado del Procesador" y "Estado de la Fuente de Alimentación" para la plantilla Microsoft - Windows.

**✨Nuevo**: Monitores "Procesos", "Carga (Load Average)" y "Dirección MAC" para la plantilla Linux.

**✨Nuevo**: Monitor "Dirección MAC" para las plantillas Genérico, Linux, Ubiquiti - AirOS 5.6 y Ubiquiti - Airmax AC.

**🔧Corrección**: El filtro de visualización por estado puede dejar algunos dispositivos fuera de la lista.

**🔧Corrección**: El tamaño del paquete ICMP en la comprobación del *uptime* era ignorado.

**🔧Corrección**: Tipo de retorno no era tratado en las plantillas de Monsta.

**🔧Corrección**: La selección de un intervalo de fecha en un monitor de tipo string no funcionaba.

**🔧Corrección**: El historial del *uptime* no mostraba más de 4 meses de datos.

**🔧Corrección**: El script de inicialización de Monsta podría no iniciar la aplicación tras una parada forzada.

**🔧Corrección**: Algunas veces los créditos de SMS y correo electrónico se mostraban incorrectamente.

**🔧Corrección**: En algunos casos, el número de dispositivos por estado se mostraba incorrectamente.

**🔧Corrección**: Probable corrección para el envío de alertas de monitores incluso con el dispositivo **.

**🔧Corrección**: La base de datos de monitores se bloqueaba al cambiar el nombre del host del servidor.

**🔧Corrección**: Deshabilitado el tratamiento de unidad de magnitud en la edición de un monitor.

**🔧Corrección**: El monitor "Clientes Conectados" de las plantillas Airmax AC y Ubiquiti - AirOS 5.6 no mostraba información.

**🔧Corrección**: El monitor "Errores en la Interfaz" de la plantilla Ubiquiti - Airmax AC no mostraba las interfaces de red.

**🔧Corrección**: El monitor "Frecuencia de Entrada" de la plantilla Nobreak - Genérico tenía el cálculo del límite máximo incorrecto.

## Versión 3.0.13

**✨Nuevo**: Nuevas plantillas disponibles.

## Versión 3.0.11

**✨Nuevo**: Usuarios y restricciones para dispositivos.

**✨Nuevo**: Grupos de dispositivos.

**✨Nuevo**: Visualización por grupos de dispositivos.

**✨Nuevo**: Disponible programa para restablecer al valor predeterminado la contraseña del usuario admin en `/opt/monsta/bin/resetadmin`.

**🔧Corrección**: El monitor *Uptime* no permite la visualización del historial con más de 6 días.

**🔧Corrección**: El icono de conexión con la nube a veces aparece, erróneamente, como estado crítico.

**🔧Corrección**: El historial de conexión con la nube no se registra en la Línea del Tiempo.

**🔧Corrección**: En un monitor existente, clonar métricas cuya descripción es un número hace que el botón "Aceptar" no funcione.

**🔧Corrección**: El mecanismo de supervisión de procesos no controla correctamente el proceso de actualización automática.

**🔧Corrección**: En un monitor existente, una métrica clonada copia el valor máximo de la original.

**🔧Corrección**: El monitor *uptime* no muestra información sobre los estados *Up* y *Down*.

**🔧Corrección**: Probable corrección para la corrupción de la base de datos de los monitores cuando se cierra Monsta.

**🔧Corrección**: Cuando se elimina una métrica de un monitor, no aparece en el gráfico, pero continúa siendo monitorizada.