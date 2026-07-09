---
title: "¿Cómo restaurar una copia de seguridad?"
---

Este manual tiene como objetivo instruir al usuario sobre cómo restaurar una copia de seguridad de Monsta.

## Restaurar una copia de seguridad en la nube de Monsta



:::note
Monsta necesita acceso a los hosts `https://mind.monsta.com.br` y `https://store.monsta.com.br` para realizar y restaurar copias de seguridad.
:::



Monsta realiza una copia de seguridad automática de sus configuraciones en nuestra nube diariamente si existen modificaciones y mantiene un historial de hasta 10 copias de seguridad.



:::caution[Atención]
Los cambios de estado de dispositivos o monitores no se consideran cambios de configuración.
:::



### Ventajas y desventajas de este método



| Ventajas | Desventajas |
| --- | --- |
| • La restauración tarda pocos minutos;</br>• No se necesita conocimiento técnico en Linux. | • El historial existente de los monitores se reinicia cuando se restaura en una nueva instalación. |



### Restaurar la copia de seguridad

Para restaurar una copia de seguridad desde la nube, siga los siguientes pasos:

1. Acceda a Monsta utilizando un usuario con permisos de administrador;
2. Haga clic en el menú “Configuración”;
3. Haga clic en la opción “Copia de seguridad en la nube”;
4. Seleccione la fecha de la copia de seguridad que desea restaurar;
5. Haga clic en el botón “Restaurar”.  
    ![image-1741969806125.png](../../../../../assets/images/p26_image-1741969806125.png)

En unos minutos, Monsta se restaurará con las configuraciones de la copia de seguridad seleccionada y solicitará el inicio de sesión nuevamente. Utilice los usuarios y contraseñas que estaban registrados en esa copia de seguridad para iniciar sesión.

## Restaurar una copia de seguridad desde un servidor

Utilice este método para mantener el historial de los monitores en una nueva instalación.

### Ventajas y desventajas



| Ventajas | Desventajas |
| --- | --- |
| • El historial de los monitores se mantiene. | • El tiempo de restauración depende de la cantidad de datos almacenados en las bases de datos;</br>  
• Se requiere conocimiento técnico de shell en Linux. |


### Realizar la copia de seguridad del servidor actual

Para este procedimiento, sugerimos que utilice el tutorial disponible en [Migración a otro servidor](/es/start/migracao/migracao-para-um-novo-servidor) de esta wiki, ya que éste transferirá automáticamente Monsta a un nuevo servidor.