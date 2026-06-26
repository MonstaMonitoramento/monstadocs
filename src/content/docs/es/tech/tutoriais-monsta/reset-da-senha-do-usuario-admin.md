---
title: "Restablecimiento de la contraseña del usuario admin"
---

Para restablecer la contraseña del usuario admin en Monsta es necesario iniciar sesión en Linux con un usuario que tenga permisos de root y escribir el comando siguiente:

```shell
/opt/monsta/bin/monagent -c /opt/monsta/etc/monkerneld.ini reset-admin
```

:::note
Tras este procedimiento, será posible iniciar sesión en Monsta con el **usuario** `admin` y la **contraseña** `admin`.
:::