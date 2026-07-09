---
title: "Opciones"
sidebar:
  order: 5
---

## Opciones globales de dispositivos

![image-1646847756093.png](../../../../../assets/images/p52_image-1646847756093.png)
Monsta permite la definición de **Valores Globales**, que funcionan como una predefinición inteligente para todos los dispositivos registrados. Cuando un valor se define de forma global, se hereda automáticamente en todos los dispositivos, a menos que se establezca una configuración específica de forma individual para el dispositivo o para su grupo de dispositivos.

### Recopilación

![image-1732557804866.png](../../../../../assets/images/p53_image-1732557804866.png)

**Parámetros de Comunicación (SNMP, WMI y SSH)**: Centralice las credenciales de acceso y los puertos de comunicación. Al configurar las comunidades SNMP o los usuarios de SSH/WMI de forma global, los nuevos dispositivos se monitorizarán automáticamente sin necesidad de introducir contraseñas manualmente para cada uno.

### Sensibilidad  


![image-1732558676013.png](../../../../../assets/images/p53_image-1732558676013.png)

**Sensibilidad del Uptime**: Define el criterio de tolerancia para considerar un dispositivo como "offline". Ajustar la sensibilidad global permite determinar cuántas pruebas de conectividad deben fallar antes de que el sistema dispare una alerta de caída, evitando falsas alarmas en redes con fluctuaciones momentáneas.



| **Nivel** | Pueden utilizarse patrones preestablecidos o personalizar cada elemento. |
| --- | --- |
| **Paquete(s)** | Cuántos paquetes se enviarán contra los equipos antes de considerarlos críticos en caso de no recibir respuesta. |
| **Timeout** | Cuánto tiempo esperará Monsta por cada ping enviado antes de considerarlo como no recibido. |
| **Delay** | Tras recibirse el paquete anterior o en caso de timeout del mismo, cuánto tiempo deberá esperar Monsta antes de enviar la siguiente solicitud. Los paquetes para comprobar el uptime se finalizan al recibir una respuesta. Para monitorizar el tiempo de ping en un equipo, se enviarán todos los paquetes y se devolverá un promedio del tiempo. |



### Sonidos de Alerta

![image-1732559278364.png](../../../../../assets/images/p53_image-1732559278364.png)

**Sonidos de Alerta Personalizados**: Configure la experiencia sonora del Centro de Operaciones (NOC). Puede definir audios distintos para los estados **Normal**, **Aviso** y **Crítico**. Esta herencia garantiza que toda la interfaz mantenga un patrón sonoro coherente, facilitando la identificación inmediata de la gravedad de un evento por el equipo técnico.

## Opciones de visualización

![image-1740681553351.png](../../../../../assets/images/p53_image-1740681553351.png)

Monsta le permite configurar el nivel de detalle visual de sus activos, priorizando la información que sea más estratégica para su día a día:

- **Ajuste de dimensiones**: Controle el tamaño de las cajas de dispositivos y monitores, permitiendo mayor densidad de información en pantallas pequeñas o mejor visibilidad en paneles de monitorización (NMS).
- **Configuración de etiqueta dinámica**: Puede elegir qué muestra cada monitor en destaque en la pantalla principal:    
    - **Nombre del Monitor**: Ideal para identificación rápida del servicio o parámetro que se está observando (ej.: "Temperatura de la CPU").
    - **Valor de la recopilación actual**: Muestra en tiempo real el dato exacto recogido (ej.: "45°C"), permitiendo seguir métricas críticas sin necesidad de abrir los detalles del monitor.
- **Escalabilidad de texto e imágenes**: Personalice el tamaño de las fuentes e imágenes en los monitores para garantizar que la información sea legible según el diseño elegido, adaptándose tanto al uso individual en escritorios como a grandes pantallas de centros de operación.

| Item | Descripción |
| --- | --- |
| **Tamaño de la barra de estado** | Define el tamaño de la barra que informa en la parte superior relacionada con el estado del dispositivo. |
| **Tamaño de la caja** | Define el tamaño de la caja del dispositivo. |
| **Tamaño de la fuente** | Configura el tamaño de la fuente del nombre del dispositivo. |
| **El dispositivo debe seguir el estado de los monitores** | Cuando esta opción está activada, el estado del dispositivo asumirá el estado de los monitores, siendo el estado crítico el de mayor relevancia y el normal, el menor. |
| **Paginación en la página de dispositivos** | Muestra la pantalla de dispositivos con paginación en lugar de desplazamiento infinito; |
| **Mostrar dirección** | Muestra el host utilizado para monitorizar el dispositivo. |
| **Mostrar ícono** | Muestra el icono asignado al dispositivo. |
| **Mostrar monitores** | Muestra el recuento de monitores en la parte superior de la caja del dispositivo. |
| **Mostrar animación** | Habilita la animación de la caja del dispositivo cuando este cambie de estado. |
| **Caja del monitor** | Permite al usuario cambiar el tamaño de la caja de los monitores. |
| **Tamaño de la fuente** | Permite al usuario cambiar el tamaño de la fuente del texto de los monitores. |
| **Espaciado entre las cajas** | Permite al usuario cambiar el espacio entre las cajas de los monitores. |
| **Tamaño del icono** | Permite al usuario cambiar el tamaño del icono mostrado en las cajas de los monitores. |
| **Modo de visualización del monitor** | Permite seleccionar el tipo de información que debe aparecer en el monitor, nombre o valor de la última lectura. |