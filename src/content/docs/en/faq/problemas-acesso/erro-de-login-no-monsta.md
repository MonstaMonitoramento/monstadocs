---
title: "How to Fix the Login Error in Monsta?"
---

This article aims to explain how to fix the Monsta login error, since the problem can be caused by different reasons.

![image-1774290685990.png](../../../../../assets/images/p175_image-1774290685990.png)

## Probable causes

The main cause of an error when logging into Monsta is an incorrect password. If you have already reviewed the password, before resetting the admin user's password, there is one more check you can perform.

When the available space on the partition where Monsta's database resides runs out, the system may stop functioning correctly. You can check the available space on your Linux. If it is out of space, you have found the problem.

To resolve it, first check whether the Monsta directory (`/var/monsta`) is the one consuming all the space (see the commands in the following section - [How to check the available space?](#how-to-check-the-available-space)). If that is the case, you will need to increase the available space (if the partition uses **LVM**, you can follow the article [Increasing an LVM Partition](/en/extra/linux/lvm-aumentar-uma-particao)) or [migrate to a new server](/en/start/migracao/migracao-para-um-novo-servidor) with greater storage capacity.

If the `/var/monsta` directory is not occupying all the space, check which files are consuming storage (logs, temporary files, etc.) and delete them if possible. If it is not possible to remove them, you will need to increase the available space on the server.

If you checked the available space and did not identify storage-related issues, try [resetting the admin user's password](/en/tech/tutoriais-monsta/reset-da-senha-do-usuario-admin).



:::tip
In many cases, the Linux server where Monsta is installed is not part of monitoring. For this reason, the partition can fill up without you noticing. We strongly recommend that you monitor the disk space of this server to track its usage. To configure SNMP on the Monsta Linux, see the article [Configuring SNMP on Linux](/en/extra/linux/snmp-linux).
:::



## How to check the available space?



:::caution[Attention]
You need access to the Linux where Monsta is installed to perform the following procedure.
:::



Below are some commands that allow you to check the current disk space and identify which directories are consuming the most storage.

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

:::note[Note]
The following examples were performed on a Fedora Server. Depending on your Linux distribution, the structure may be different.
:::



In the example, we observe that the `/var` directory is using 48% of the partition space. `/var` is the directory where Monsta's database is located, so it must not run out of available space.

There are cases where there is no dedicated partition for `/var`. In that situation, you need to check the available space on the root partition `/`.

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

In the example, the root partition `/` is full, which can cause system malfunctions.

It is also possible to identify which directories are occupying the most space. For that, use the command:

`# du -sh /*`

This command will display the size of each directory inside `/`. After identifying the directory that consumes the most space, repeat the command inside it to further detail the usage.

Normally, on servers where only Monsta is installed, the directory with the highest consumption will be `/var`, and within it, `/var/monsta`.

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

If the `/var/monsta` directory is using a lot of space, the best solution is to increase the available capacity (if the partition uses LVM, you can follow the article [Increasing an LVM Partition](/en/extra/linux/lvm-aumentar-uma-particao)) or [migrate to a new server](/en/start/migracao/migracao-para-um-novo-servidor) with greater storage capacity.