---
title: "Registro de cambios v4"
sidebar:
  order: 4
---

## Versión 4.1.19

**✨Nuevo**: Preparación para la actualización a la versión **5**. Nota: Esta actualización reiniciará el servidor.

## Versión 4.1.16

**🔧Corrección**: La carpeta `/var/monsta/agent/store` no elimina archivos antiguos.

**🔧Corrección**: El valor máximo en un gráfico se muestra como `0` cuando el valor es negativo.

**🔧Corrección**: La caché `SNMP`, en algunas situaciones, impide que el agente realice consultas contra el dispositivo.

**🔧Corrección**: `SNMP` nativo utiliza el mismo request-id y genera un alto consumo de memoria en algunos equipos.

**🔧Corrección**: En el Panel, en algunas situaciones, el botón de guardar no tiene efecto después de una modificación o inserción de un componente.

**🔧Corrección**: El programa `monagentd` deja de responder a peticiones del core de Monsta en algunas situaciones.

**🔧Corrección**: Instancias con nombres numéricos presentan fallos en el monitoreo.

**🔧Corrección**: Las reglas de monitores automáticos crean monitores con el grupo de alerta en blanco.

## Versión 4.1.15

**✨Nuevo**: Posibilidad de eliminar monitores automáticos en minutos/horas/días.

**🔧Corrección**: Los monitores automáticos duplican los ítems creados cuando no está marcada la búsqueda por instancias dinámicas.

**🔧Corrección**: El aviso de nueva versión disponible tarda hasta 15 minutos en aparecer en pantalla.

**🔧Corrección**: Los logs del `monstadb` no se rotan correctamente.

## Versión 4.1.14

**✨Nuevo**: Descubrimiento automático de monitores (Monsta crea y elimina monitores automáticamente según se detecten en el dispositivo).

**✨Nuevo**: Filtro para la visualización de dispositivos y monitores.

**✨Nuevo**: Posibilidad de actualizar Monsta a versiones Beta.

**✨Nuevo**: Copias de seguridad con hasta 1 mes de información para restaurar.

**✨Nuevo**: Opción para importar y exportar plantillas.

**✨Nuevo**: `WebSockets` - Nueva función `ws.send_recv()` para ser utilizada en los monitores.

**✨Nuevo**: Créditos de SMS y correo con cantidad baja son alertados en pantalla.

**✨Nuevo**: Caché local para instancias en `SNMP`.

**✨Nuevo**: Botón para inactivar el monitoreo de un host.

**✨Nuevo**: `SNMP` nativo (para un menor consumo de recursos).

**✨Nuevo**: Opción para guardar datos del usuario en la pantalla de inicio de sesión.

**✨Nuevo**: La línea de tiempo muestra el valor de los monitores.

**✨Nuevo**: Barra para aumentar el tamaño del texto de los dispositivos en la pantalla principal.

**✨Nuevo**: Nueva plantilla TP-Link - Switch.

**✨Nuevo**: Nueva plantilla Cambium Networks.

**✨Nuevo**: Nueva plantilla WNI - Challenger.

**✨Nuevo**: Nueva plantilla Intracom Telecom - OmniBAS.

**✨Nuevo**: Nueva plantilla Intelbras - APC.

**✨Nuevo**: Nueva plantilla Juniper - MX5.

**✨Nuevo**: Nueva plantilla Cianet - OLT GEPON.

**✨Nuevo**: Nueva plantilla Huawei - OLT MA5600.

**✨Nuevo**: Nueva plantilla Socomec - Net Vision Masterys BC (SAI).

**✨Nuevo**: Nueva plantilla 3Com - 4800 Switch.

**✨Nuevo**: Nueva plantilla Ericsson - Mini-Link.

**✨Nuevo**: Nueva plantilla Datacom (OLT).

**✨Nuevo**: Nueva plantilla Volt - Controlador de Carga MPPT.

**✨Nuevo**: Nueva plantilla Volt - Full Power 620 Evolution.

**✨Nuevo**: Nueva plantilla Volt - Punto de Distribución AC Evolution.

**✨Nuevo**: Nueva plantilla Volt - Punto de Distribución Cliente (PDC Evolution).

**✨Nuevo**: Nueva plantilla Volt - Pop Protect.

**✨Nuevo**: Nueva plantilla Volt - Power Net 1000 Evolution.

**✨Nuevo**: Nueva plantilla Volt - Mini Central UPS `SNMP`.

**✨Nuevo**: Nuevos monitores para Mikrotik - Routerboard.

**🔧Corrección**: Visualización de los grupos en orden alfabético.

**🔧Corrección**: Nuevos dispositivos aparecen para usuarios sin autorización para acceder a ellos.

**🔧Corrección**: SMS con más de 160 caracteres no se envían (las mensajes ahora se truncan).

**🔧Corrección**: La opción de visualización en tiempo real no funcionaba adecuadamente en la línea de tiempo.

**🔧Corrección**: Se eliminaron bibliotecas de la carpeta `/opt/monsta/lib` que conflictaban con actualizaciones del servidor Linux.

**🔧Corrección**: Monitores de plantillas existentes no pueden ser modificados.

**🔧Corrección**: La fuente de datos para la comprobación del uptime no aparecía ordenada. En algunos casos, algunos ítems dejan de mostrarse.

**🔧Corrección**: Las copias de seguridad se sobreescriben cuando existe más de una licencia en uso en una única cuenta.

**🔧Corrección**: Clonar un dispositivo provoca la publicación del gráfico del dispositivo primario.

**🔧Corrección**: Los límites de un monitor no se modifican cuando se cambia el tipo de retorno (Ej.: numérico, booleano, string, etc.).

**🔧Corrección**: La función `params.InstaceId()` no devuelve el valor correcto, provocando fallos en los monitores que la utilizan.

**🔧Corrección**: Los dispositivos se consideran críticos en la suma total incluso si solo un monitor está en estado crítico.

**🔧Corrección**: Algunos logs de Monsta no estaban siendo rotados.

**🔧Corrección**: Monsta registra información repetida en el archivo `moncored.log`, ocasionando un crecimiento muy grande de esos archivos.

**🔧Corrección**: Al restaurar una copia de seguridad, los iconos no se copian.

**🔧Corrección**: Las cajas de dispositivos no tiemblan cuando el mismo cambia de estado.

**🔧Corrección**: Al instalar una licencia, ocasionalmente Monsta informa que la misma ya está en uso.

**🔧Corrección**: Los gráficos con frecuencia de monitorización en segundos ahora se muestran en un intervalo de 1h por defecto.

**🔧Corrección**: En el panel, los gráficos permiten la selección de monitores del tipo `string`.

## Versión 4.0.20

**✨Nuevo**: Añadida opción de herramientas para el dispositivo (`traceroute`, `ping` y abrir en un *browser*).

**✨Nuevo**: Opción para ocultar las leyendas de los gráficos en un panel.

**✨Nuevo**: Envío de alertas por Telegram.

**✨Nuevo**: Visualización de gráficos en tiempo real.

**✨Nuevo**: Nueva vista en árbol (Sunburst).

**✨Nuevo**: Nueva plantilla BGP - BGP4.

**✨Nuevo**: Nueva plantilla Intelbras - Grabadores (HDCVI).

**✨Nuevo**: Nueva plantilla Sophos - XG Firewall.

**✨Nuevo**: Nueva plantilla Brother - Impresora Láser.

**✨Nuevo**: Nueva plantilla Ubiquiti - Edgeswitch.

**✨Nuevo**: Nueva plantilla Parks - OLT 10008S.

**✨Nuevo**: Nueva plantilla Huawei - NE20S.

**✨Nuevo**: Nueva plantilla Huawei - S6720.

**✨Nuevo**: Nueva plantilla Morningstar - XPS.

**✨Nuevo**: Nueva plantilla Volt - Net Probe.

**✨Nuevo**: Nueva plantilla BlockBit - UTM.

**✨Nuevo**: Nueva plantilla Seagate - NAS.

**✨Nuevo**: Nueva plantilla SMS - SAI.

**✨Nuevo**: Nueva plantilla Intelbras - WOM.

**✨Nuevo**: Nueva plantilla Apple - Mac OS X.

**✨Nuevo**: Nueva plantilla Lenovo - IX4.

**✨Nuevo**: Nueva plantilla Dell - iDRAC.

**✨Nuevo**: Nueva plantilla Polycom - Videoconferencia.

**✨Nuevo**: Nueva plantilla Fiberhome - OLT.

**🔧Corrección**: Durante la edición/inserción de un dispositivo, al indicar un tamaño de paquete en la comprobación del uptime, el botón Ok no guarda las configuraciones.

**🔧Corrección**: Las direcciones IP no se muestran durante la selección de una instancia.

**🔧Corrección**: Las leyendas de colores aparecen sin información en los gráficos publicados.

**🔧Corrección**: En algunas situaciones de estrés del sistema, los monitores que utilizan ICMP, como uptime y ping, dejan de funcionar.

**🔧Corrección**: Al clonar un dispositivo, el grupo por defecto se añade automáticamente.

**🔧Corrección**: Monsta envía alertas de los monitores de un dispositivo incluso cuando éste está en estado crítico.

**🔧Corrección**: Algunos scripts con instancias dinámicas no consiguen obtener el valor de las métricas.

**🔧Corrección**: En la edición de una métrica, el valor máximo no permitía valores negativos.

**🔧Corrección**: La publicación de un gráfico con varias instancias no muestra sus nombres en la leyenda.

**🔧Corrección**: En algunas situaciones, el servicio de verificación de datos deja de responder y es necesario reiniciar el servicio.

## Versión 4.0.12

**✨Nuevo**: Percentil y posibilidad de seleccionar el tiempo de agrupamiento de datos en los gráficos.

**✨Nuevo**: Selección de múltiples estados en la pantalla de dispositivos.

**🔧Corrección**: El componente para seleccionar fechas en un gráfico a veces se vuelve lento.

**🔧Corrección**: Algunas métricas aparecen con valores a cero en el Panel.

**🔧Corrección**: El relleno de los gráficos no mantiene el mismo color de la línea.

**🔧Corrección**: En monitores con múltiples métricas de tipo booleano, al hacer clic sobre una métrica, el gráfico mostrado era siempre relativo a la primera.

**🔧Corrección**: Instancias con nombres extensos causan error de carga durante la adición de un monitor.

## Versión 4.0.6

**🔧Corrección**: No es posible guardar dispositivos que usan `snmp` con puerto distinto del 161.

**🔧Corrección**: No es posible guardar una fuente de datos con el retorno distinto del tipo numérico.

**🔧Corrección**: La visualización de un punto en los gráficos no muestra los segundos.

**🔧Corrección**: Los monitores del tipo string eran devueltos siempre con el estado normal.

## Versión 4.0.4

**✨Nuevo**: La función ping.send() modificada para devolver éxito tras la recepción del primer paquete.

**✨Nuevo**: En el monitor de tiempo de actividad se muestra la información del tiempo que el equipo ha estado encendido (solo para dispositivos con `snmp`).

**✨Nuevo**: Botón para exportar/imprimir un gráfico en formatos PNG, PDF, SVG, CSV y XLS.

**🔧Corrección**: Al añadir un dispositivo, el monitor de tiempo de actividad inicia en estado crítico.

**🔧Corrección**: Al eliminar un grupo de dispositivos de un usuario, Monsta añade todos los dispositivos de ese grupo individualmente para el mismo usuario.

**🔧Corrección**: Restaurada la leyenda de los gráficos al modelo anterior.

**🔧Corrección**: Dispositivos marcados para no enviar alertas no eran listados en la pantalla de visualización de dispositivos.

**🔧Corrección**: El nombre de la métrica de un monitor devuelto en las alertas cuando un monitor vuelve al estado normal está incorrecto.

**🔧Corrección**: `SNMP` v3 genera error durante la autenticación.

**🔧Corrección**: En sistemas con versiones de `openssl` posteriores a la `1.0.1e`, la instalación del RPM falla al generar el certificado SSL y el servidor HTTP no inicia.

**🔧Corrección**: El número de intentos era ignorado en algunas situaciones.

## Versión 4.0.2

**✨Nuevo**: Core del sistema totalmente remodelado para menor consumo de hardware y aumento de rendimiento.

**✨Nuevo**: La base de datos de configuraciones ahora trabaja en memoria.

**✨Nuevo**: Nuevo formato para la selección de colores para los gráficos de los monitores y Panel.

**✨Nuevo**: Nuevos modelos para visualización en árbol (Jerarquía y Mapa) con zoom y pan.

**✨Nuevo**: El intervalo de verificación de dispositivos y monitores puede ser en segundos.

**✨Nuevo**: Posibilidad de buscar por instancias dinámicas en un dispositivo (Ej.: usuarios autenticados con PPPoE).

**✨Nuevo**: Nuevas variables para ser utilizadas en las plantillas de alerta.

**🔧Corrección**: El gráfico del uptime no se muestra correctamente cuando se selecciona un periodo superior a 4 meses.

**🔧Corrección**: En algunos navegadores, las cajas de los grupos se intercambian de lugar al hacer clic sobre ellas.

**🔧Corrección**: En algunos casos, la cantidad de dispositivos por estado no se muestra correctamente.

**🔧Corrección**: En la vista en árbol, los dispositivos sin un icono no pueden ser seleccionados.

**🔧Corrección**: Habilitada la paginación en la Línea de Tiempo.

**🔧Corrección**: Durante la edición de una métrica en una plantilla, las flechas de mover hacia arriba o hacia abajo eliminaban la métrica seleccionada.

**🔧Corrección**: Los caracteres especiales no se muestran correctamente en la pantalla de dispositivos.

**🔧Corrección**: Corrección del algoritmo del monitor "Uso de CPU" de la plantilla Linux.