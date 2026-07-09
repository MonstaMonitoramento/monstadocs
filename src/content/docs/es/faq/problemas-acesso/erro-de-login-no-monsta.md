---
title: "¿Cómo Resolver el Error de Inicio de Sesión en Monsta?"
---

Este artículo tiene como objetivo explicar cómo resolver el error de inicio de sesión de Monsta, ya que el problema puede deberse a distintas causas.

![image-1774290685990.png](../../../../../assets/images/p175_image-1774290685990.png)

## Causas prováveis

La causa principal de error al iniciar sesión en Monsta es la contraseña incorrecta. Si ya ha revisado la contraseña, antes de restablecer la contraseña del usuario admin, hay una verificación más que se puede realizar.

Cuando el espacio disponible en la partición donde está la base de datos de Monsta se agota, el sistema puede dejar de funcionar correctamente. Puede verificar el espacio disponible en su Linux. Si no hay espacio, ha encontrado el problema.

Para solucionarlo, primero verifique si el directorio de Monsta (`/var/monsta`) es el responsable de consumir todo el espacio (vea los comandos en el siguiente ítem - [¿Cómo verificar el espacio disponible?](#como-verificar-o-espaço-disponível)). Si ese es el caso, será necesario aumentar el espacio disponible (si la partición utiliza **LVM**, puede seguir el artículo [Aumentando uma Partição LVM](/es/extra/linux/lvm-aumentar-uma-particao)) o [migrar para um novo servidor](/es/start/migracao/migracao-para-um-novo-servidor) con mayor capacidad de almacenamiento.

Si el directorio `/var/monsta` no está ocupando todo el espacio, verifique qué archivos están consumiendo el almacenamiento (logs, archivos temporales, etc.) y elimínelos, si es posible. Si no es posible retirarlos, será necesario aumentar el espacio disponible en el servidor.

Si ha verificado el espacio disponible y no ha identificado problemas relacionados con el almacenamiento, intente [resetear la contraseña del usuario admin](/es/tech/tutoriais-monsta/reset-da-senha-do-usuario-admin).



:::tip
En muchos casos, el Linux donde está instalado Monsta no forma parte del monitoreo. Por este motivo, la partición puede llenarse sin que lo note. Recomendamos encarecidamente que monitorice el espacio en disco de ese servidor para seguir su utilización. Para configurar SNMP en el Linux de Monsta, consulte el artículo de [Configurando el SNMP en Linux](/es/extra/linux/snmp-linux).
:::



## Como verificar o espaço disponível?



:::caution[Atención]
Es necesario tener acceso al Linux donde está instalado Monsta para realizar el procedimiento que sigue.
:::



A continuación hay algunos comandos que permiten verificar el espacio en disco actual e identificar qué directorios están consumiendo más almacenamiento.

```shell
# df -h
Sist. Arq.               Tam. Usado Disp. Uso% Montado em
/dev/mapper/fedora-root   30G  2,6G   28G   9% /
devtmpfs                 4,0M     0  4,0M   0% /dev
tmpfs                    2,0G     0  2,0G   0% /dev/shm
tmpfs                    782M  776K  781M   1% /run
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-journald.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-network-generator.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-udev-load-credentials.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-tmpfiles-setup-dev-early.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-sysctl.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-tmpfiles-setup-dev.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-vconsole-setup.service
tmpfs                    2,0G  828K  2,0G   1% /tmp
/dev/vda2                2,0G  270M  1,7G  14% /boot
/dev/mapper/fedora-var   366G  175G  192G  48% /var
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-tmpfiles-setup.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-resolved.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/getty@tty1.service
tmpfs                    391M   12K  391M   1% /run/user/0
```



:::note[Observación]
Los ejemplos siguientes se realizaron en un Fedora Server. Dependiendo de su distribución Linux, la estructura puede ser diferente.
:::



En el ejemplo, observamos que el directorio `/var` está utilizando el 48% del espacio de la partición. `/var` es el directorio donde se encuentra la base de datos de Monsta, por lo tanto no debe quedarse sin espacio disponible.

Existen casos en los que no hay una partición dedicada a `/var`. En esa situación, es necesario verificar el espacio disponible en la partición raíz `/`.

```shell
# df -h
Sist. Arq.               Tam. Usado Disp. Uso% Montado em
/dev/mapper/fedora-root   40G  40G   0G   100% /
devtmpfs                 4,0M     0  4,0M   0% /dev
tmpfs                    2,0G     0  2,0G   0% /dev/shm
tmpfs                    782M  776K  781M   1% /run
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-journald.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-network-generator.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-udev-load-credentials.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-tmpfiles-setup-dev-early.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-sysctl.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-tmpfiles-setup-dev.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-vconsole-setup.service
tmpfs                    2,0G  828K  2,0G   1% /tmp
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-tmpfiles-setup.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/systemd-resolved.service
tmpfs                    1,0M     0  1,0M   0% /run/credentials/getty@tty1.service
tmpfs                    391M   12K  391M   1% /run/user/0
```

En el ejemplo, la partición raíz `/` está llena, lo que puede provocar fallos en el funcionamiento del sistema.

También es posible identificar qué directorios están ocupando más espacio. Para ello, utilice el comando:

`# du -sh /*`

Ese comando mostrará el tamaño de cada directorio dentro de `/`. Tras identificar el directorio que más consume espacio, repita el comando dentro de él para detallar aún más el uso.

Normalmente, en servidores donde solo está instalado Monsta, el directorio con mayor consumo será `/var`, y dentro de él, `/var/monsta`.

```shell
# du -sh /var/*
0       /var/adm
105M    /var/cache
0       /var/db
0       /var/empty
176M    /var/flow
0       /var/ftp
0       /var/games
0       /var/kerberos
43M     /var/lib
0       /var/local
0       /var/lock
3,0G    /var/log
0       /var/mail
164G    /var/monsta
0       /var/nis
0       /var/opt
0       /var/preserve
0       /var/run
0       /var/spool
4,0K    /var/tmp
520M    /var/www
0       /var/yp
```

Si el directorio `/var/monsta` está usando mucho espacio, la mejor solución es aumentar la capacidad disponible (si la partición utiliza LVM, puede seguir el artículo [Aumentando uma Partição LVM](/es/extra/linux/lvm-aumentar-uma-particao)) o [migrar para um novo servidor](/es/start/migracao/migracao-para-um-novo-servidor) con mayor capacidad de almacenamiento.