---
title: Grupos de Alertas
---
![image-1756129907740.png](/src/assets/images/p37_image-1756129907740.png)

:::caution[Atención]
El funcionamiento de esta función requiere, obligatoriamente, que el software de Monsta tenga comunicación con el host mind.monsta.com.br.
:::

:::tip
La pantalla de alertas permite trabajar con grupos donde se indican los contactos que deberán recibir los avisos correspondientes cuando un dispositivo o monitor cambie su “estado”.
:::

## Grupos

En esta pantalla se gestionan los grupos de usuarios que recibirán las notificaciones y el tipo de servicio, ya sea por correo electrónico o SMS.

| Opção | Descripción |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-1645792155732.png](/src/assets/images/p37_image-1645792155732.png) | **Nuevo Grupo**: Crea un nuevo grupo para el envío de alertas. |
| ![image-1645792160782.png](/src/assets/images/p37_image-1645792160782.png) | **Buscar Grupo**: Muestra en la pantalla solo los grupos que coinciden con la búsqueda ingresada. |
| ![image-1756129930291.png](/src/assets/images/p37_image-1756129930291.png) | **Grupo Nube**: Este grupo envía alertas en caso de pérdida de comunicación entre Monsta y la nube en [https://mind.monsta.com.br](https://mind.monsta.com.br). Este recurso es muy útil en casos como caída del enlace a Internet en la empresa o apagado inesperado del servidor sin el debido conocimiento del usuario. Este grupo no puede eliminarse del sistema y no está disponible para dispositivos o monitores. El color de su borde indica el estado de la conexión con la nube:<br> - **Verde**: Comunicación establecida;<br> - **Rojo**: Fallo en la comunicación.<br>El tiempo para el envío de una alerta es de 20 minutos. |
| ![image-1756129950105.png](/src/assets/images/p37_image-1756129950105.png) | **Grupo Predeterminado**: Este grupo es obligatorio en el sistema y no puede eliminarse, solo modificarse. El número indicado en la esquina superior derecha de la caja del grupo se refiere al número de dispositivos que lo utilizan en sus alertas. Cuando la caja del grupo se presenta en color gris, esto indica que no posee alertas activadas. |
| ![image-1732710101229.png](/src/assets/images/p37_image-1732710101229.png) | **Alertas activas**: Los iconos presentados dentro de la caja del grupo indican qué alertas están activas en ese momento para el mismo. |
| ![image-1732710190977.png](/src/assets/images/p37_image-1732710190977.png) | **Eliminar Grupo**: Elimina el grupo seleccionado. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Atención</p>Solo se permitirá eliminar un grupo cuando este no forme parte de ningún dispositivo o monitor. Esta información puede obtenerla en la pestaña [Membros](#membros) al editar el grupo.</aside> |
| ![image-1645792184443.png](/src/assets/images/p37_image-1645792184443.png) | **Editar Grupo**: En esta opción el usuario podrá añadir y quitar dispositivos y monitores que formen parte de este grupo, así como definir los tipos de alerta que se enviarán, sus destinatarios y los horarios permitidos para el envío de los mensajes. |

### Editando grupos de alertas

#### Detalhes

En esta pestaña se definen el icono, nombre y comentario sobre el grupo.

![image-1732711113493.png](/src/assets/images/p37_image-1732711113493.png)

| Opção | Descripción |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-1732710589288.png](/src/assets/images/p37_image-1732710589288.png) | Es posible asignar una imagen al grupo de alerta que se mostrará en pantalla. |
| **Nome do grupo de alerta** | Es el nombre que se presentará en la pantalla de grupos, así como el que se mostrará al editar la opción de grupos de alerta dentro de los dispositivos o monitores. |
| **Descrição** | Permite añadir un comentario sobre el grupo en cuestión. |

#### Membros

En esta pestaña es posible visualizar los dispositivos y monitores que recibirán alertas de este grupo, así como añadir nuevos dispositivos o eliminar los existentes.

![image-1739974572520.png](/src/assets/images/p37_image-1739974572520.png)

| Opção | Descripción |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Todos** | Este componente muestra todos los dispositivos existentes en Monsta. Haga clic sobre un dispositivo para seleccionarlo y utilice los botones a un lado para añadirlo al grupo. |
| **Selecionados** | Este componente muestra los dispositivos y monitores que forman parte del grupo en cuestión. Haga clic sobre un elemento para seleccionarlo y utilice los botones a un lado para eliminarlo del grupo. |

#### Alertas Monsta

Esta pestaña muestra las alertas predeterminadas de Monsta que utilizan nuestra nube para ser enviadas a los destinatarios. Las opciones de envío existentes son Correo electrónico, SMS y Telegram. Las Alertas Monsta no requieren configuraciones especiales pues se integran automáticamente con la nube durante la instalación del software.

![image-1732712034593.png](/src/assets/images/p37_image-1732712034593.png)
Para facilitar la visualización, las alertas activas están marcadas con el icono anterior en su pestaña.

![image-1732711910237.png](/src/assets/images/p37_image-1732711910237.png)

| Opção | Descripción |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-1732712383308.png](/src/assets/images/p37_image-1732712383308.png) | Activa o desactiva el tipo de alerta en cuestión. |
| ![image-1732712469323.png](/src/assets/images/p37_image-1732712469323.png) | Envía una prueba a los destinatarios existentes. Esta opción es útil para verificar si todos los destinos están configurados correctamente, como dirección de correo electrónico, SMS o usuarios de Telegram. |
| ![image-1732712594374.png](/src/assets/images/p37_image-1732712594374.png) | Estas opciones permiten seleccionar el tipo de evento en el que se deberá enviar la alerta. Cuando está desmarcada, Monsta no enviará notificaciones para el estado seleccionado. |
| ![image-1732712693761.png](/src/assets/images/p37_image-1732712693761.png) | Aquí es posible elegir el objeto que se utilizará para el envío de alertas. Puede usar esta opción para recibir alertas solo cuando el dispositivo quede incomunicable, pero optar por no recibir una alerta si el monitor de CPU dispara una alarma por alta utilización. |
| **Template da mensagem** | Las plantillas son modelos de mensajes que se enviarán a los usuarios. Puede personalizar cómo se enviarán los mensajes a sus destinatarios. Para más información, consulte "Templates de mensagens". |
| ![image-1732713267486.png](/src/assets/images/p37_image-1732713267486.png) | Esta opción está disponible solo para Telegram. Muestra los usuarios que forman parte del grupo y permite eliminarlos manualmente. Para incorporar un usuario, deberá usar el código que aparece al inicio de esta pantalla y enviarlo al bot "MonstaTecnologiaBot". Las instrucciones sobre cómo proceder están especificadas en esta misma pantalla. |
| ![image-1732713616303.png](/src/assets/images/p37_image-1732713616303.png) | Los períodos son los intervalos de tiempo en los que las alertas podrán enviarse. Al crear un grupo, el valor predeterminado es 24x7. Los cuadrados en gris indican que los horarios seleccionados están inactivos y Monsta no enviará alertas al grupo en esos intervalos de tiempo. |

## Centro de alertas

En esta pantalla se gestionan los grupos de usuarios que recibirán las notificaciones y el tipo de servicio, ya sea por correo electrónico o SMS.

![image-1739974733737.png](/src/assets/images/p37_image-1739974733737.png)

![image-1739974790750.png](/src/assets/images/p37_image-1739974790750.png)  
**Barra de visualización**: Permite al usuario establecer la cantidad de elementos por página y el período que la información debe mostrarse en la pantalla.

| Información | Descripción |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-1739974961714.png](/src/assets/images/p37_image-1739974961714.png) | **Estado**: Informa sobre el estado del mensaje enviado a un usuario. |
| ![image-1739975105124.png](/src/assets/images/p37_image-1739975105124.png) | **Tipo**: Indica a través de qué medio se envió el mensaje. |
| ![image-1739975173561.png](/src/assets/images/p37_image-1739975173561.png) | **Fecha y hora**: Indica la fecha y hora del envío. |
| ![image-1739975251006.png](/src/assets/images/p37_image-1739975251006.png) | **Destinatario**: Indica el destinatario del mensaje. Esta información no está disponible para alertas por Telegram debido a que los mensajes se envían a un Bot. |
| ![image-1739975341938.png](/src/assets/images/p37_image-1739975341938.png) | **Origen**: Indica el dispositivo y monitor que originaron la alerta. |
| ![image-1739975429030.png](/src/assets/images/p37_image-1739975429030.png) | **Contenido**: Muestra el contenido enviado por la alerta. |

## Templates de mensagem

Con nuestras plantillas, puede crear mensajes personalizados para cada tipo de alerta, asegurando que la información más importante se entregue a los responsables de forma rápida y eficiente. Elija entre una variedad de variables para incluir detalles como el nombre del dispositivo, la gravedad de la alerta y la hora de ocurrencia, entre otros.

![image-1732727391061.png](/src/assets/images/p37_image-1732727391061.png)

![image-1732727677203.png](/src/assets/images/p37_image-1732727677203.png)
Cree una nueva plantilla y personalice el mensaje como desee.

---

![image-1732727745380.png](/src/assets/images/p37_image-1732727745380.png)
Esta es la caja que representa la plantilla existente. Al hacer clic sobre ella, el usuario accede a la opción de editar la información existente.

| Ícone | Descripción |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![image-1732727824893.png](/src/assets/images/p37_image-1732727824893.png) | Elimina la plantilla existente. Atención: La plantilla no podrá eliminarse si está en uso por algún grupo de alertas. La plantilla **Predeterminada** forma parte del sistema y tampoco podrá eliminarse. |
| ![image-1732727887105.png](/src/assets/images/p37_image-1732727887105.png) | Abre la edición de la plantilla para el usuario. |

### Editando um template de mensagem

En esta pantalla el usuario puede personalizar el mensaje enviado por los grupos de alerta. Se listan las variables disponibles que pueden utilizarse y un sencillo lenguaje de programación para trabajar con condiciones.

![image-1732728340150.png](/src/assets/images/p37_image-1732728340150.png)

| Opção | Descripción |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nome** | Es el nombre que se mostrará en la pantalla de plantillas, así como el que se presentará para selección al editar la opción de grupos de alerta. |
| **Corpo** | Este es el texto del mensaje de alerta que se enviará al usuario. Cuando se usan variables o comandos de programación, estos deben estar, obligatoriamente, entre "{{ }}". |
| **Variáveis do sistema** | Son las variables con información del sistema que están disponibles para usarse en las plantillas de alerta. Para agilizar la personalización del texto del cuerpo del mensaje con las variables, basta con hacer doble clic sobre la variable deseada para que se inserte en el texto. |

#### Variáveis do sistema

| Variável | Descripción |
| ---------------------------- | -------------------------------------------------------------------- |
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
| `monitor.nomecurto` | Devuelve el nombre informado en el icono del monitor. |
| `nome.metrica` | Devuelve el nombre de la métrica. |
| `nome.instancia` | Devuelve el nombre de la instancia. |
| `valor` | Devuelve el valor de la lectura. |

:::caution[Atención]
No hay soporte para *emojis* e imágenes en las plantillas de alerta. El mensaje enviado por la alerta debe ser únicamente texto.
:::
