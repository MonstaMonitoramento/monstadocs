---
title: "Migration to a New Server"
---

This tutorial shows how to migrate Monsta from version >5.0 to another server.

## Minimum requirements

Minimum requirements for Monsta migration:

:::caution
Make sure the "/var" partition on the new server has enough space to transfer Monsta data from the current server.
:::

| Item | Requisito Mínimo |
| :---: | :--- |
| ![Espaço em disco](../../../../../assets/images/p25_image-1645452261754.png) | **Disk space**<br />40GB free for /var (settings, database and logs)<br />300MB free for /opt/monsta (programs and libraries)<br />Ensure the new installation has enough space to perform the migration. |
| ![Memória RAM](../../../../../assets/images/p25_image-1645452312898.png) | **RAM**<br />2GB of RAM |
| ![Sistema Operacional](../../../../../assets/images/p25_image-1645452455434.png) | **Operating System**<br />Linux 64-bit<br />Recommended Linux OS: Fedora Server 40 (x86_64 systems) or Ubuntu Server 24. A minimal installation can be used for Monsta. |
| ![Processador](../../../../../assets/images/p25_image-1645452542916.png) | **Processor**<br />Cores: 2<br />Speed: 1.8GHz |

:::note
The above settings generally allow monitoring approximately 500 devices with 10 monitors each, or a total of 5,000 monitors.
:::


## Migration script

Logged in as root on your server, download the migration script as in the example below:

### Fedora/Red-Hat
```shell
yum install -y wget sshpass
wget https://www.monsta.com.br/monsta/download/migrate.sh
```

### Ubuntu/Debian
```shell
apt-get install -y wget sshpass
wget https://www.monsta.com.br/monsta/download/migrate.sh
```

## Starting the transfer
After downloading the script, run it with the following syntax:

`sh migrate.sh <user> <"password"> <current Monsta server IP> <ssh port>`

Example:

```shell
sh migrate.sh root "minha senha" 192.168.1.1 22
```

The script will stop Monsta processes running on the old server (192.168.1.1) and will start copying the structure and data to the new server. At the end of the process you will be able to access your Monsta on the new server and the old one can be deactivated.

:::note
The elapsed time for this transfer will depend on the size of the existing database, and can take from minutes to several hours.
:::

:::danger[Important]
To ensure the migrate script runs successfully and ensures the copying and creation of all files and directories with the correct permissions (including system files, logs, and sensitive configurations), it is **mandatory** that it is executed by a user with **Superuser (`root`)** privileges on **both servers** (Source and Destination). Running as a non-root user will cause problems during data transfer.  
  
If a **timeout** error occurs while running `migrate.sh`, check that the SSH port on the remote server is open in the firewall for access from the local server.  
  
In case of failure, even after following the `migrate.sh` usage instructions, **collect the logs displayed on the screen and contact our support team**.
:::
