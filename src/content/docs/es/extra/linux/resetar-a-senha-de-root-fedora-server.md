---
title: "Restablecer la contraseña de root: Fedora Server"
sidebar:
  order: 7
---

Este tutorial tiene como objetivo recuperar la contraseña de root en un Linux Fedora Server.

## Recuperar la contraseña del usuario root

Al arrancar el servidor Linux aparecerá la pantalla de arranque similar a la imagen siguiente:

![image-1719319990630.png](../../../../../assets/images/p21_image-1719319990630.png)

Pulse la tecla “e”, con esto se abrirá el modo de edición de las configuraciones del arranque conforme la imagen abajo:

![image-1719320093869.png](../../../../../assets/images/p21_image-1719320093869.png)

Busque la línea que comienza con “linux” o "linux16" o "linuxefi" y al final añada "rw init=/bin/bash" conforme el ejemplo abajo:

![image-1719320698513.png](../../../../../assets/images/p21_image-1719320698513.png)

Pulse CTRL + X para iniciar Linux con las nuevas configuraciones. Debería aparecer la siguiente pantalla:

![image-1719320807739.png](../../../../../assets/images/p21_image-1719320807739.png)

Escriba los siguientes comandos para efectuar el cambio de la contraseña:

```shell
passwd
```

Restaure los permisos de SELinux con el siguiente comando:

```shell
/bin/sed -i s/"SELINUX=enforcing"/"SELINUX=permissive"/ /etc/selinux/config
touch /.autorelabel
```



:::danger[Atención]
Si los permisos de SELinux no se restauran con los procedimientos anteriores, el proceso de inicio de sesión podrá fallar y tendrá que repetir el proceso de restablecimiento de la contraseña.
:::



A continuación, reinicie el servidor con el siguiente comando:

```shell
/sbin/reboot -r
```



:::note
Utilice el siguiente comando solo si desea activar SELinux.
:::



Después de reiniciar el servidor, inicie sesión como root y vuelva a activar SELinux con los siguientes comandos:

```shell
sed -i s/"SELINUX=permissive"/"SELINUX=enforcing"/ /etc/selinux/config
setenforce enforcing
```