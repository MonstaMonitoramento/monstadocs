---
title: "Restablecer la contraseña de root: Ubuntu"
sidebar:
  order: 8
---

Una guía paso a paso para restablecer la contraseña de cualquier usuario (incluido el **root**) en **Ubuntu** utilizando el menú de **GRUB** para acceder a un *shell* de recuperación.

## 1. Acceder al menú de GRUB

1. **Reinicie** su sistema Ubuntu.
2. Mantenga presionada la tecla `Shift` (o, en sistemas **UEFI**, pulse la tecla `Esc` repetidamente) durante el arranque para forzar la visualización del menú de **GRUB** (si no aparece automáticamente).
3. Use las flechas para seleccionar la opción de su kernel actual, generalmente la primera línea.
4. Pulse la tecla `e` para editar los parámetros de arranque.

---

## 2. Editar la línea de arranque

1. En la pantalla de edición, use las flechas hacia abajo para encontrar la línea que comienza con `linux`.
2. En esa línea, busque el parámetro `ro` (solo lectura) y sustitúyalo por `rw` (lectura-escritura).
3. Vaya al final de esa misma línea y añada lo siguiente:
    
    ```shell  
    init=/bin/bash
    ```

    El final de la línea modificada debería parecerse a: `... ro quiet splash rw init=/bin/bash`
4. Pulse `Ctrl+X` para iniciar el sistema con estos nuevos parámetros. El sistema arrancará directamente en un *shell* de root (`#`).
    
    ![image-1764957644158.png](../../../../../assets/images/p136_image-1764957644158.png)

---

## 3. Cambiar la contraseña del usuario

En el *shell* de *root* que apareció, puede restablecer la contraseña de cualquier usuario usando el comando `passwd`.

### 3.1. Restablecer la contraseña de un usuario estándar

Si desea restablecer la contraseña de un usuario común (ej.: `joao`):

1. Ejecute el comando `passwd` seguido del nombre de usuario:    
    ```shell
    passwd joao    
    ```
2. Escriba la **nueva contraseña** y confírmela.

### 3.2. Restablecer la contraseña de root (superusuario)

Ubuntu normalmente desactiva la cuenta de *root* por defecto, pero puede activarla (y definir su contraseña) si es necesario:

1. Ejecute el comando `passwd` sin argumentos:
    ```shell
    passwd root
    ```
2. Escriba la **nueva contraseña** y confírmela.

---

## 4. Finalizar y reiniciar

1. Tras cambiar la contraseña, necesita **reiniciar el sistema** para que los cambios tengan efecto y el sistema vuelva a arrancar con normalidad. Use el comando `exec` para restaurar el proceso de inicio:
    ```shell
    exec /sbin/init 6 
    ```
2. El sistema se reiniciará y podrá hacer *login* con la nueva contraseña establecida para el usuario elegido.