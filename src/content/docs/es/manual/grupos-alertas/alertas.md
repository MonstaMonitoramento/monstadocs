---
title: "Grupos de Alerta"
---

![image-1756129907740.png](../../../../../assets/images/p37_image-1756129907740.png)

:::caution[Atención]
El funcionamiento de este recurso requiere, obligatoriamente, que el software de Monsta tenga comunicación con el host mind.monsta.com.br.
:::

:::tip
La pantalla de alertas permite trabajar con grupos donde se indican los contactos que deberán recibir los avisos correspondientes cuando un dispositivo o monitor cambie su “estado”.
:::

## Grupos

En esta pantalla se gestionan los grupos de usuarios que recibirán las notificaciones y el tipo de servicio, ya sea por correo electrónico o SMS.

| Opción | Descripción |
| :---: | :--- |
| ![image-1645792155732.png](../../../../../assets/images/p37_image-1645792155732.png) | **Nuevo Grupo**: Crea un nuevo grupo para el envío de alertas. |
| ![image-1645792160782.png](../../../../../assets/images/p37_image-1645792160782.png) | **Buscar Grupo**: Muestra en pantalla solo los grupos que coinciden con la búsqueda introducida. |
| ![image-1756129930291.png](../../../../../assets/images/p37_image-1756129930291.png) | **Grupo Nube**: Este grupo envía alertas en caso de pérdida de comunicación entre Monsta y la nube en [https://mind.monsta.com.br](https://mind.monsta.com.br). Este recurso es muy útil en casos como la caída del enlace a Internet en la empresa o el apagado inesperado del servidor sin el conocimiento del usuario. Este grupo no puede ser removido del sistema y no está disponible para dispositivos o monitores.<br />El color de su borde indica el estado de la conexión con la nube:<br />- **Verde**: Comunicación establecida;<br />- **Rojo**: Fallo en la comunicación. |
| ![image-1756129950105.png](../../../../../assets/images/p37_image-1756129950105.png) | **Grupo Predeterminado**: Este grupo es obligatorio en el sistema y no puede ser eliminado, solo modificado. El número mostrado en la esquina superior derecha del recuadro del grupo se refiere al número de dispositivos que lo utilizan en sus alertas. Cuando el recuadro del grupo se presenta en color gris, esto indica que no tiene alertas activadas. |
| ![image-1732710101229.png](../../../../../assets/images/p37_image-1732710101229.png) | **Alertas activas**: Los iconos presentados dentro del recuadro del grupo indican qué alertas están activas en ese momento para el mismo. |
| ![image-1732710190977.png](../../../../../assets/images/p37_image-1732710190977.png) | **Eliminar Grupo**: Elimina el grupo seleccionado. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Atención</p>Sólo se permitirá eliminar un grupo cuando el mismo no forme parte de ningún dispositivo o monitor. Esta información podrá obtenerse en la pestaña [Miembros](#membros) al editar el grupo.</aside> |
| ![image-1645792184443.png](../../../../../assets/images/p37_image-1645792184443.png) | **Editar Grupo**: En esta opción el usuario podrá agregar y eliminar dispositivos y monitores que forman parte de este grupo, así como definir los tipos de alerta que se enviarán, sus destinatarios y los horarios permitidos para el envío de los mensajes. |



### Editando grupos de alertas

#### Detalles

En esta pestaña se definen el icono, nombre y comentario sobre el grupo.

![image-1732711113493.png](../../../../../assets/images/p37_image-1732711113493.png)

| Opción | Descripción |
| :---: | :--- |
| ![image-1732710589288.png](../../../../../assets/images/p37_image-1732710589288.png) | Es posible asignar una imagen al grupo de alertas que se mostrará en pantalla. |
| **Nombre del grupo de alertas** | Es el nombre que se presentará en la pantalla de grupos, así como el que se mostrará al editar la opción de grupos de alertas dentro de los dispositivos o monitores. |
| **Descripción** | Permite añadir un comentario sobre el grupo en cuestión. |

#### Miembros  


En esta pestaña es posible visualizar los dispositivos y monitores que recibirán alertas de este grupo, así como añadir nuevos dispositivos o eliminar los existentes.

![image-1739974572520.png](../../../../../assets/images/p37_image-1739974572520.png)

| Opción | Descripción |
| :---: | :--- |
| **Todos** | Este componente muestra todos los dispositivos existentes en Monsta. Haga clic sobre un dispositivo para seleccionarlo y utilice los botones al lado para añadirlo al grupo. |
| **Seleccionados** | Este componente muestra los dispositivos y monitores que forman parte del grupo en cuestión. Haga clic sobre un elemento para seleccionarlo y utilice los botones al lado para eliminarlo del grupo. |



#### Alertas Monsta  


Esta pestaña muestra las alertas estándar de Monsta que utilizan nuestra nube para ser enviadas a los destinatarios. Las opciones de envío disponibles son Correo electrónico, SMS y Telegram. Las Alertas Monsta no requieren configuraciones especiales ya que se integran automáticamente con la nube durante la instalación del software. 

![image-1732712034593.png](../../../../../assets/images/p37_image-1732712034593.png) 
Para facilitar la visualización, las alertas activas se marcan con el icono anterior en su pestaña.


![image-1732711910237.png](../../../../../assets/images/p37_image-1732711910237.png)

| Opción | Descripción |
| :---: | :--- |
| ![image-1732712383308.png](../../../../../assets/images/p37_image-1732712383308.png) | Activa o desactiva el tipo de alerta en cuestión. |
| ![image-1732712469323.png](../../../../../assets/images/p37_image-1732712469323.png) | Envía una prueba a los destinatarios existentes. Esta opción es útil para verificar si todos los destinos están configurados correctamente, como direcciones de correo electrónico, números de SMS o usuarios de Telegram. |
| ![image-1732712594374.png](../../../../../assets/images/p37_image-1732712594374.png) | Estas opciones permiten seleccionar el tipo de evento en el que debe enviarse la alerta. Cuando está desmarcada, Monsta no realizará envíos para el estado seleccionado. |
| ![image-1732712693761.png](../../../../../assets/images/p37_image-1732712693761.png) | Aquí es posible elegir el objeto que se utilizará para el disparo de alertas. Puede usar esta opción para recibir alertas solo cuando el dispositivo se vuelve incomunicable, pero optar por no recibir una alerta si el monitor de CPU alarma por un uso elevado. |
| **Plantilla del mensaje** | Las plantillas son modelos de mensajes que se enviarán a los usuarios. Puede personalizar cómo se enviarán los mensajes a sus destinatarios. Para más información, consulte "Plantillas de mensajes". |
| ![image-1732713267486.png](../../../../../assets/images/p37_image-1732713267486.png) | Esta opción está disponible solo para Telegram. Muestra los usuarios que forman parte del grupo y permite eliminarlos manualmente. Para que un usuario se una, debe usar el código que aparece al inicio de esta pantalla y enviarlo al bot "MonstaTecnologiaBot". Las instrucciones de cómo proceder están especificadas en esta misma pantalla. |
| ![image-1732713616303.png](../../../../../assets/images/p37_image-1732713616303.png) | Los periodos son los intervalos de tiempo en los que las alertas pueden ser enviadas. Al crear un grupo, el valor predeterminado es 24x7. Los cuadrados en gris indican que los horarios seleccionados están inactivos y Monsta no enviará alertas al grupo en esos intervalos de tiempo. |



## Centro de alertas

En esta pantalla se gestionan los grupos de usuarios que recibirán las notificaciones y el tipo de servicio, ya sea por correo electrónico o SMS.

![image-1739974733737.png](../../../../../assets/images/p37_image-1739974733737.png)

![image-1739974790750.png](../../../../../assets/images/p37_image-1739974790750.png)  
**Barra de visualización**: Permite al usuario establecer la cantidad de elementos por página y el periodo que la información debe mostrarse en pantalla.


| Información | Descripción |
| :---: | :--- |
| ![image-1739974961714.png](../../../../../assets/images/p37_image-1739974961714.png) | **Estado**: Informa sobre el estado del mensaje enviado a un usuario. |
| ![image-1739975105124.png](../../../../../assets/images/p37_image-1739975105124.png) | **Tipo**: Indica por qué medio se envió el mensaje. |
| ![image-1739975173561.png](../../../../../assets/images/p37_image-1739975173561.png) | **Fecha y hora**: Indica la fecha y hora del envío. |
| ![image-1739975251006.png](../../../../../assets/images/p37_image-1739975251006.png) | **Destinatario**: Indica el destinatario del mensaje. Esta información no está disponible para alertas por Telegram debido a que los mensajes se envían a un Bot. |
| ![image-1739975341938.png](../../../../../assets/images/p37_image-1739975341938.png) | **Origen**: Indica el dispositivo y monitor que originaron la alerta. |
| ![image-1739975429030.png](../../../../../assets/images/p37_image-1739975429030.png) | **Contenido**: Muestra el contenido enviado por la alerta. |



## Plantillas de mensajes

Con nuestras plantillas, puede crear mensajes personalizados para cada tipo de alerta, garantizando que la información más importante se entregue a los responsables de forma rápida y eficiente. Elija entre una variedad de variables para incluir detalles como el nombre del dispositivo, la gravedad de la alerta y la hora de ocurrencia, entre otros.

![image-1732727391061.png](../../../../../assets/images/p37_image-1732727391061.png)



![image-1732727677203.png](../../../../../assets/images/p37_image-1732727677203.png)
Cree una nueva plantilla y personalice el mensaje como desee.

---

![image-1732727745380.png](../../../../../assets/images/p37_image-1732727745380.png)
Esta es la casilla que representa la plantilla existente. Al hacer clic sobre ella, el usuario accede a la opción de editar la información existente. 

| Ícono | Descripción |
| :---: | :--- |
| ![image-1732727824893.png](../../../../../assets/images/p37_image-1732727824893.png) | Elimina la plantilla existente. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Atención</p>La plantilla no podrá eliminarse si está en uso por algún grupo de alertas. La plantilla **Predeterminada** forma parte del sistema y tampoco podrá eliminarse.</aside> |
| ![image-1732727887105.png](../../../../../assets/images/p37_image-1732727887105.png) | Abre la edición de la plantilla para el usuario. |

### Editando una plantilla de mensaje

En esta pantalla el usuario puede personalizar el mensaje enviado por los grupos de alerta. Se listan las variables existentes que pueden utilizarse y un sencillo lenguaje de programación para trabajar con condiciones.

![image-1732728340150.png](../../../../../assets/images/p37_image-1732728340150.png)


| Opción | Descripción |
| :--- | :--- |
| **Nombre** | Es el nombre que se mostrará en la pantalla de plantillas, así como el que se mostrará para la selección al editar la opción de grupos de alerta. |
| **Cuerpo** | Este es el texto del mensaje de alerta que se enviará al usuario. Cuando se usan variables o comandos de programación, estos deberán ir, obligatoriamente, entre "{{ }}". |
| **Variables del sistema** | Son las variables con información del sistema que están disponibles para ser usadas en las plantillas de alerta. Para agilizar la personalización del texto del cuerpo con las variables, basta con hacer un "doble clic" sobre la variable deseada para insertarla en el texto. |



#### Variables del sistema

| Variable | Descripción
| --- | --- |
| `dataehora` | Devuelve la fecha (d/m/a) y la hora actual (h:m). |
| `dispositivo.descricao` | Devuelve la descripción del dispositivo. |
| `dispositivo.endereco` | Devuelve la dirección IP del dispositivo. |
| `dispositivo.estado` | Devuelve el estado actual del dispositivo obtenido por el monitor Uptime. |
| `dispositivo.estadoanterior` | Devuelve el estado anterior del dispositivo obtenido por el monitor Uptime. |
| `dispositivo.nome` | Devuelve el nombre del dispositivo. |
| `estado` | Devuelve el estado del dispositivo. |
| `monitor.estado` | Devuelve el estado actual del monitor. |
| `monitor.estadoanterior` | Devuelve el estado anterior del monitor. |
| `monitor.nome` | Devuelve el nombre del monitor. |
| `monitor.nomecurto` | Devuelve el nombre mostrado en el icono del monitor. |
| `nome.metrica` | Devuelve el nombre de la métrica. |
| `nome.instancia` | Devuelve el nombre de la instancia. |
| `valor` | Devuelve el valor de la lectura. |

:::caution[Atención]
No hay soporte para *emojis* ni imágenes en las plantillas de alerta. El mensaje enviado por la alerta debe ser solo texto.
:::