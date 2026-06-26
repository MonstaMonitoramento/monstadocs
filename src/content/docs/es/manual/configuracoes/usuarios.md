---
title: "Usuarios"
sidebar:
  order: 9
---

O Monsta é multi-usuário, ou seja, ele permite que vários usuários sejam utilizados simultaneamente no sistema com permissões personalizadas. O sistema de gerenciamento de usuários do Monsta permite informar quais dispositivos, grupos, painéis ou grupos de alerta podem ser visualizados e gerenciados por cada integrante.

![image-1647888175595.png](../../../../../assets/images/p66_image-1647888175595.png)

| Ícone / Opção | Descrição |
| :---: | :--- |
| ![image-1647888202156.png](../../../../../assets/images/p66_image-1647888202156.png) | Añade un nuevo usuario para acceder a la plataforma. |
| **Admin** | Cuando está marcado, indica que el usuario en la lista tiene permisos de administrador y acceso a todos los dispositivos, monitores y recursos disponibles. |
| **Login** | Es el nombre para iniciar sesión en Monsta. |
| **Nome** | Nombre del usuario. |
| ![image-1647888352963.png](../../../../../assets/images/p66_image-1647888352963.png) | Edita las propiedades del usuario seleccionado. |
| ![image-1647888388977.png](../../../../../assets/images/p66_image-1647888388977.png) | Clona las propiedades del usuario actual a uno nuevo. |
| ![image-1647888449977.png](../../../../../assets/images/p66_image-1647888449977.png) | Elimina el usuario seleccionado. |



## Crear/Editar un Usuario

### Detalles
Son la información básica del usuario. 

| Opção | Descrição |
| :--- | :--- |
| **Login** | Nombre de usuario. No puede ser modificado para usuarios ya existentes. |
| **Nome Completo** | Información del nombre completo del usuario. |
| **Alterar Senha** | Permite cambiar la contraseña del usuario en edición. |
| ![image-1647888733932.png](../../../../../assets/images/p66_image-1647888733932.png) | **Administrador**: Asigna propiedades de administrador cuando está activado. El usuario tendrá acceso a todos los dispositivos, monitores y recursos disponibles en Monsta. <aside class="starlight-aside starlight-aside--note">Cuando un usuario no es administrador, la vista jerárquica no estará disponible para él.</aside> |


### Dispositivos
Permite al administrador definir exactamente qué dispositivos podrá visualizar y gestionar un usuario específico en el sistema.

| Ícone / Opção | Descrição |
| :--- | :--- |
| ![image-1647889770987.png](../../../../../assets/images/p66_image-1647889770987.png) | **Escritura**: El usuario recibe permisos de escritura (modificación). Podrá:<br />• Modificar y eliminar dispositivos;<br />• Añadir, modificar y eliminar monitores (servicios/métricas) en los dispositivos existentes.<br /><br />Cuando está desmarcado, el usuario solo puede visualizar datos. No se permiten cambios en la lista de dispositivos, monitores ni en sus configuraciones. |
| ![image-1739989429159.png](../../../../../assets/images/p66_image-1739989429159.png) | **Filtro de Dispositivos**: Filtra los dispositivos por el texto indicado. |
| ![image-1739989466314.png](../../../../../assets/images/p66_image-1739989466314.png) | **Lista de Dispositivos**: En la columna a la izquierda están listados todos los dispositivos que están siendo monitorizados en Monsta. En la columna a la derecha, están listados los dispositivos que el usuario podrá visualizar e interactuar. Estos son los activos a los que el usuario accederá. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Botones de Selección Individual**: Mueve los dispositivos seleccionados entre las columnas de la lista de dispositivos. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Botones de Selección General**: Mueve todos los dispositivos de una columna a otra en la lista de dispositivos. |



### Grupos
Configura los grupos en los que el usuario tendrá acceso a los dispositivos miembros.



| Ícone / Opção | Descrição |
| :--- | :--- |
| ![image-1739989584199.png](../../../../../assets/images/p66_image-1739989584199.png) | **Lista de Grupos de Dispositivos**: En la columna a la izquierda están listados todos los grupos registrados en Monsta. En la columna a la derecha, están listados los grupos a los que el usuario tendrá acceso. Los dispositivos pertenecientes a ese grupo se mostrarán en la pestaña "Dispositivos", en la columna a la derecha, marcados solo como lectura. |
| ![image-1739989429159.png](../../../../../assets/images/p66_image-1739989429159.png) | **Filtro de Grupos de Dispositivos**: Filtra los grupos por el texto indicado. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Botones de Selección Individual**: Mueve los grupos seleccionados entre las columnas de la lista de grupos de dispositivos. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Botones de Selección General**: Mueve todos los grupos de una columna a otra en la lista de grupos de dispositivos. |



### Grupos de Alerta
Configura los grupos de alerta a los que el usuario tendrá acceso.

| Ícone / Opção | Descrição |
| :--- | :--- |
| ![image-1647889770987.png](../../../../../assets/images/p66_image-1647889770987.png) | **Escritura**: El usuario recibe permisos de escritura (modificación). Podrá gestionar alertas.<br /><br />Cuando está desmarcado, el usuario solo puede visualizar datos. No se permiten cambios en los grupos de alerta. |
| ![image-1739989663950.png](../../../../../assets/images/p66_image-1739989663950.png) | **Filtro de Grupos de Alerta**: Filtra los grupos por el texto indicado. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Botones de Selección Individual**: Mueve los grupos seleccionados entre las columnas de la lista de grupos de alerta. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Botones de Selección General**: Mueve todos los grupos de una columna a otra en la lista de grupos de alerta. |