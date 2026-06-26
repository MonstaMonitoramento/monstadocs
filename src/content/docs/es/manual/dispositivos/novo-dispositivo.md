---
title: "Nuevo Dispositivo"
sidebar:
  order: 6
---

Al hacer clic en el botón "Nuevo" es posible añadir un dispositivo al monitoreo de Monsta.

## Detalles

Define la información básica sobre el equipo.

![image-1739970776422.png](../../../../../assets/images/p51_image-1739970776422.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1646855537251.png](../../../../../assets/images/p51_image-1646855537251.png) | **Ícono**: Permite seleccionar un ícono para el dispositivo. |
| ![image-1646855610278.png](../../../../../assets/images/p51_image-1646855610278.png) | **Nombre del dispositivo**: Será el nombre mostrado en los modos de visualización. |
| ![image-1646855698393.png](../../../../../assets/images/p51_image-1646855698393.png) | **Dirección del dispositivo**: Es la dirección IPv4, IPv6 o el host del dispositivo. Es posible hacer ping a la dirección para probarla. |
| ![image-1646855946392.png](../../../../../assets/images/p51_image-1646855946392.png) | **Descripción del dispositivo**: Permite insertar un breve texto sobre el equipo. |
| ![image-1646856003694.png](../../../../../assets/images/p51_image-1646856003694.png) | **Agente**: Lugar desde donde se lanzarán las recopilaciones del dispositivo. Esta información es de solo lectura. |
| ![image-1646856167964.png](../../../../../assets/images/p51_image-1646856167964.png) | **Monitor de uptime**: Método utilizado para identificar si el dispositivo está activo. Por defecto se envían paquetes icmp echo-request (ping). Los métodos de verificación pueden permitir informar algunos parámetros para las consultas, como por ejemplo el tamaño del paquete icmp a enviar o el puerto TCP a verificar en el dispositivo. |
| ![image-1732555718867.png](../../../../../assets/images/p51_image-1732555718867.png) | **Sensibilidad**: Configura el nivel de sensibilidad del dispositivo para paquetes de tipo ping (icmp). Para más información, consulte la página [Sensibilidad](/es/manual/dispositivos/opcoes#sensibilidad). |



## Templates

Son los monitores disponibles para cada tipo de equipo. Cada plantilla posee monitores específicos para ser utilizados, y se puede utilizar más de una plantilla en un dispositivo.

![image-1646856297549.png](../../../../../assets/images/p51_image-1646856297549.png)

| Opção | Descrição |
| :--- | :--- |
| **Seleccionados** | Son las plantillas utilizadas en este dispositivo. |
| **Usado frequentemente** | Es una lista de las plantillas más utilizadas en su Monsta, lo que permite una selección más ágil. |
| **Todos** | Es el listado de todas las plantillas disponibles en Monsta. |



## Pai

Define la dependencia jerárquica del activo. Utilizado para organizar el mapa de la red y optimizar el sistema de notificaciones, relacionando los dispositivos con sus dependencias.

:::caution[Importante]
Esta información será utilizada por el sistema de envío de alertas para que Monsta dispare una comunicación únicamente del dispositivo que esté con problema.
:::



![image-1769000388348.png](../../../../../assets/images/p51_image-1769000388348.png)

## Coleta

En esta pantalla aparecen los principales métodos para la búsqueda de información de los dispositivos utilizados por Monsta. Su funcionalidad principal es permitir que el usuario utilice una configuración por defecto para los monitores utilizados, además de probar si la comunicación está funcional.

![image-1739970973988.png](../../../../../assets/images/p51_image-1739970973988.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1739971005493.png](../../../../../assets/images/p51_image-1739971005493.png) | **Métodos de recopilación**: Son los tipos de recopilación por defecto ejecutados por Monsta. Al hacer clic en estos métodos es posible configurar parámetros generales que serán usados por los monitores de los dispositivos. Para recopilar datos de Servidores y Estaciones Windows, utilice la Sonda. Para más información, consulte nuestro tutorial [Sonda: Monitorización de Windows](/es/start/instalacao/sonda-windows). |
| ![image-1646915286768.png](../../../../../assets/images/p51_image-1646915286768.png) | **Heredar del Grupo o Global**: Esta propiedad, cuando está marcada, obtiene los valores configurados globalmente o del grupo al que pertenece el dispositivo. Para más información consulte [Opciones globales de dispositivos](/es/manual/dispositivos/opcoes#opciones-globales-de-dispositivos). |
| ![image-1646913740044.png](../../../../../assets/images/p51_image-1646913740044.png) | **Propiedad**: Permite cambiar el valor de esta propiedad de recopilación. Si la opción "Heredar valor del grupo o global" está marcada, esta propiedad heredará el valor configurado. |
| ![image-1732556926759.png](../../../../../assets/images/p51_image-1732556926759.png) | **Exponencial**: Cuando está disponible, utiliza un algoritmo de timeout para la recopilación. Este algoritmo duplica el tiempo de timeout en cada recopilación fallida, iniciando en 1 segundo. |
| ![image-1739971041554.png](../../../../../assets/images/p51_image-1739971041554.png) | **Probar**: Cuando está disponible, permite probar si el dispositivo responde a los parámetros configurados. |



## Grupos

Los dispositivos en Monsta pueden formar parte de grupos y heredar sus configuraciones. En esta pantalla es posible consultar los grupos a los que pertenece el dispositivo además de añadir otros. Para añadir grupos, consulte Grupos de Dispositivos.

![image-1732557160475.png](../../../../../assets/images/p51_image-1732557160475.png)

| Ícone | Descrição |
| :---: | :--- |
| ![image-1732557200808.png](../../../../../assets/images/p51_image-1732557200808.png) | **Nombre del grupo**: Indica el grupo al que pertenece el dispositivo. |
| ![image-1646919486747.png](../../../../../assets/images/p51_image-1646919486747.png) | **Añadir grupo**: Permite añadir un nuevo grupo al que pertenecerá el dispositivo. |
| ![image-1646919524906.png](../../../../../assets/images/p51_image-1646919524906.png) | **Eliminar grupo**: Elimina el dispositivo del grupo seleccionado. |



## Alertas

Monsta tiene la capacidad de emitir sonidos cuando un dispositivo o monitor cambia de estado. En esta pantalla podrá personalizar los sonidos individualmente para el dispositivo en cuestión.

![image-1732557243546.png](../../../../../assets/images/p51_image-1732557243546.png)

### Grupos de Alerta

Los grupos de alerta se utilizan para el envío de mensajes cuando un dispositivo o monitor cambia de estado. Estos grupos pueden personalizarse para cada dispositivo o monitor o asignarse sonidos específicos al dispositivo en cuestión. Para más información sobre los grupos de alerta consulte [Alertas](/es/manual/grupos-alertas/alertas).

![image-1739971123424.png](../../../../../assets/images/p51_image-1739971123424.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1732557441016.png](../../../../../assets/images/p51_image-1732557441016.png) | **Notificar grupos de alerta**: Habilita/Deshabilita el envío de alertas para el dispositivo seleccionado. |
| ![image-1732557452354.png](../../../../../assets/images/p51_image-1732557452354.png) | **Seleccionar**: Indica el grupo de alerta al que pertenece el dispositivo. |
| ![image-1646919486747.png](../../../../../assets/images/p51_image-1646919486747.png) | **Añadir grupo de alerta**: Permite añadir un nuevo grupo de alerta al que pertenecerá el dispositivo. |
| ![image-1646919524906.png](../../../../../assets/images/p51_image-1646919524906.png) | **Eliminar grupo de alerta**: Elimina el dispositivo del grupo de alerta seleccionado. |
| ![image-1732557653598.png](../../../../../assets/images/p51_image-1732557653598.png) | **Sonidos de Alerta**: Permite seleccionar un sonido específico para cada estado del dispositivo. |