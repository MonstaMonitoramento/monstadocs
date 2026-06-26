---
title: "Visualización en modo Grid"
sidebar:
  order: 2
---

En la pantalla de visualización en grid, los dispositivos se muestran como cuadros que indican el estado en el que se encuentra el equipo y un resumen de sus respectivos monitores.

:::note
**Dispositivo**: Equipo con al menos una dirección IP en la red.
:::



## Caja del Dispositivo

![image-1646920930381.png](../../../../../assets/images/p55_image-1646920930381.png)

| Informação | Descrição |
| :---: | :--- |
| ![image-1646920980786.png](../../../../../assets/images/p55_image-1646920980786.png) | **Nombre**: Indica el nombre del dispositivo. |
| ![image-1646921003457.png](../../../../../assets/images/p55_image-1646921003457.png) | **Dirección**: Indica la dirección del dispositivo. |
| ![image-1646921020039.png](../../../../../assets/images/p55_image-1646921020039.png) | **Vista detallada**: Abre el dispositivo seleccionado en una nueva pantalla con una vista más detallada de su monitorización. |
| ![image-1646921058196.png](../../../../../assets/images/p55_image-1646921058196.png) | **Acciones**: Son procesos que pueden ejecutarse sobre el dispositivo seleccionado. |
| ![image-1646921073359.png](../../../../../assets/images/p55_image-1646921073359.png) | **Editar**: Edita las propiedades del dispositivo. Para más información, consulte: [Nuevo Dispositivo](/es/manual/dispositivos/novo-dispositivo). |



- - - - - -

## Vista del Dispositivo

En esta pestaña es posible visualizar el estado y editar información del dispositivo y sus monitores, así como acceder a los gráficos de monitorización.

![image-1756130572475.png](../../../../../assets/images/p55_image-1756130572475.png)


| Ícono | Descrição |
| :---: | :--- |
| ![image-1646941577966.png](../../../../../assets/images/p55_image-1646941577966.png) | **Activar / Desactivar**: Permite activar o desactivar la monitorización del dispositivo seleccionado. |
| ![image-1646941614267.png](../../../../../assets/images/p55_image-1646941614267.png) | **Vista detallada**: Cambia al modo de visualización del dispositivo con un resumen de información. |
| ![image-1732625167859.png](../../../../../assets/images/p55_image-1732625167859.png) | **Línea de tiempo**: Abre la línea de tiempo del dispositivo seleccionado. Para más información, consulte: [Línea de Tiempo](/es/manual/linha-tempo/linha-do-tempo). |
| ![image-1646941719105.png](../../../../../assets/images/p55_image-1646941719105.png) | **Editar**: Edita las propiedades del dispositivo seleccionado. |
| ![image-1646941777433.png](../../../../../assets/images/p55_image-1646941777433.png) | **Eliminar**: Elimina el dispositivo seleccionado y sus monitores. |
| ![image-1646941797055.png](../../../../../assets/images/p55_image-1646941797055.png) | **Clonar**: Crea una copia del dispositivo seleccionado y de sus monitores. |
| ![image-1646941813782.png](../../../../../assets/images/p55_image-1646941813782.png) | **Monitores Automáticos**: Abre la edición de reglas para crear los monitores de forma automática para el dispositivo. Para más información consulte [Monitores Automáticos](/es/manual/dispositivos/monitores-automaticos). |
| ![image-1756130607601.png](../../../../../assets/images/p55_image-1756130607601.png) | **Vista en Mapa**: Abre el mapa con el filtro activado para el dispositivo seleccionado. Para más información consulte [Visualización en Mapa](/es/manual/dispositivos/visualizacao-em-mapa). |
| ![image-1646941865563.png](../../../../../assets/images/p55_image-1646941865563.png) | **Añadir Monitor**: Añade uno o más monitores al dispositivo seleccionado. |
| ![image-1732625538788.png](../../../../../assets/images/p55_image-1732625538788.png) | **Monitores**: Al hacer clic en sus iconos, sus datos correspondientes se muestran en la pantalla. |
| ![image-1646942048013.png](../../../../../assets/images/p55_image-1646942048013.png) | **Filtrar Monitores**: Muestra en pantalla solo los monitores que contienen las palabras del filtro. |
| ![image-1646942182734.png](../../../../../assets/images/p55_image-1646942182734.png) | **Filtrar por Estado**: Muestra en pantalla solo los monitores con los estados seleccionados. |
| ![image-1739971953866.png](../../../../../assets/images/p55_image-1739971953866.png) | **Métricas en ejecución**: Informa la cantidad de métricas en ejecución en el momento contra el dispositivo seleccionado y su límite máximo. |
| ![image-1732625517650.png](../../../../../assets/images/p55_image-1732625517650.png) | **Resumen**: Al hacer clic en este elemento, se abrirá una nueva ventana con una visualización resumida de todos los monitores del dispositivo.<br />![image-1732625598475.png](../../../../../assets/images/p55_image-1732625598475.png) |

- - - - - -

## Monitores

Para más información sobre los monitores, consulte [Visualización de Monitores](/es/manual/dispositivos/visualizacao-de-monitores).

### Añadir Monitores

![image-1732639335704.png](../../../../../assets/images/p55_image-1732639335704.png)
Al hacer clic en el botón + en el menú del dispositivo, será posible seleccionar una forma para añadir monitores.

![image-1732639306380.png](../../../../../assets/images/p55_image-1732639306380.png)

| Ícone | Descrição |
| :---: | :--- |
| ![image-1732639606113.png](../../../../../assets/images/p55_image-1732639606113.png) | Muestra una pantalla con los monitores relativos a la plantilla en evidencia. Al seleccionar un monitor, es posible seleccionar la instancia a recopilar o cambiar el nombre que se mostrará en el icono del monitor.<br /><br />![image-1732639931855.png](../../../../../assets/images/p55_image-1732639931855.png) **Descripción**: Muestra un resumen del icono, nombre y descripción del monitor seleccionado.<br /><br />![image-1732640005940.png](../../../../../assets/images/p55_image-1732640005940.png) **Nombre corto**: Es el nombre que se mostrará en el icono del monitor. Se muestra una vista previa a la derecha.<br /><br />![image-1739973171292.png](../../../../../assets/images/p55_image-1739973171292.png) **Parámetros**: Permite introducir datos, cuando se soliciten, al monitor, como por ejemplo el nombre de la interfaz de red que debe ser monitorizada.<br /><br />![image-1732640246016.png](../../../../../assets/images/p55_image-1732640246016.png) **Personalizar**: Edita propiedades del monitor. Para más información, consulte: [Editar/Personalizar un Monitor](/es/manual/dispositivos/visualizacao-de-monitores#editarpersonalizar-un-monitor). |
| ![image-1732640369424.png](../../../../../assets/images/p55_image-1732640369424.png) | Esta opción permite añadir múltiples monitores de una sola vez al dispositivo.<br /><br />![image-1732640714231.png](../../../../../assets/images/p55_image-1732640714231.png) **Plantilla**: Pestaña para selección de la plantilla. Una vez seleccionada una plantilla, sus monitores aparecerán en el lado derecho de la pantalla. <br /><br />![image-1732640799469.png](../../../../../assets/images/p55_image-1732640799469.png) **Monitor**: Cuando está marcado, indica a Monsta que ese monitor debe ser insertado en el dispositivo.<br /><br />![image-1732640902457.png](../../../../../assets/images/p55_image-1732640902457.png) **Parámetros**: Informa al monitor de un parámetro a utilizar en la creación del monitor, cuando sea necesario, como por ejemplo la interfaz de red a monitorizar en el dispositivo.<br /><br />![image-1732640990927.png](../../../../../assets/images/p55_image-1732640990927.png) **Añadir monitor**: Repite el monitor seleccionado abajo para permitir la adición de varios monitores del mismo tipo.<br /><br />![image-1732641077298.png](../../../../../assets/images/p55_image-1732641077298.png) **Editor**: Permite cambiar información del monitor antes de añadirlo. Para más información, consulte: [Editar/Personalizar un Monitor](/es/manual/dispositivos/visualizacao-de-monitores#editarpersonalizar-un-monitor). |
| ![image-1732641453798.png](../../../../../assets/images/p55_image-1732641453798.png) | **Monitores Personalizados**: Permite añadir un monitor personalizado. Esta función es útil para crear monitores que serán utilizados únicamente por un dispositivo. Para más información, consulte: [Editar/Personalizar un Monitor](/es/manual/dispositivos/visualizacao-de-monitores#editarpersonalizar-un-monitor). |

### Monitores automáticos

Monsta tiene la capacidad de identificar y añadir automáticamente nuevas instancias al monitoreo, como tarjetas de red, discos duros y otros dispositivos. Esta funcionalidad ahorra tiempo y evita la necesidad de configurarlos manualmente.

**Cómo funciona**: El sistema realiza escaneos periódicos en el dispositivo en busca de nuevas instancias. Al encontrar una que no haya sido añadida al monitoreo y sea compatible con los filtros, se añade automáticamente con la configuración predeterminada.

**Configuraciones**: Puede personalizar la frecuencia de los escaneos, los tipos de monitores a buscar y un filtro de palabras que será analizado.

**Ejemplo**: Al conectar una nueva tarjeta de red a un servidor, Monsta la detectará automáticamente y la añadirá al monitoreo, permitiéndole seguir su rendimiento en tiempo real.

![image-1732642591751.png](../../../../../assets/images/p55_image-1732642591751.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1732642765286.png](../../../../../assets/images/p55_image-1732642765286.png) | **Monitor**: Es el tipo de búsqueda que Monsta debe realizar para encontrar nuevas instancias. |
| ![image-1732642783014.png](../../../../../assets/images/p55_image-1732642783014.png) | **Filtro de instancia**: Busca solo instancias que contienen los caracteres especificados en el filtro y desestima las demás. |
| ![image-1732642861815.png](../../../../../assets/images/p55_image-1732642861815.png) | **Frecuencia**: Tiempo configurado para que Monsta busque y añada nuevas instancias en el dispositivo. |
| ![image-1732642933956.png](../../../../../assets/images/p55_image-1732642933956.png) | **Eliminar monitores**: Los monitores en estado de fallo, es decir, cuya instancia ya no existe, serán eliminados después del período seleccionado.<aside class="starlight-aside starlight-aside--caution">No confundir con monitores en estado crítico, cuya lectura se realiza pero cuyos valores están fuera de su límite normal.</aside> |
| ![image-1732643125055.png](../../../../../assets/images/p55_image-1732643125055.png) | **Propiedades**: Permite personalizar las propiedades siguientes para todos los monitores creados por la regla:<br />- Icono;<br />- Nombre de las métricas;<br />- Límites de alerta;<br />- Frecuencia de verificación;<br />- Número de intentos. |
| ![image-1732643318174.png](../../../../../assets/images/p55_image-1732643318174.png) | **Añadir regla**: Añade una nueva regla debajo de la actual. |
| ![image-1732643371764.png](../../../../../assets/images/p55_image-1732643371764.png) | **Eliminar regla**: Elimina la regla seleccionada. <aside class="starlight-aside starlight-aside--danger">Al eliminar una regla de monitor automático, todos los monitores creados por ella también serán eliminados, junto con sus respectivos historiales.</aside> |