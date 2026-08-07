---
title: Migration to a New Server
description: Learn how to migrate Monsta to a new server while preserving
  configurations, monitoring, history and platform data securely.
---
This tutorial shows how to migrate Monsta from version >5.0 to another server.

:::danger[Attention]

Do not install Monsta on the new server! This procedure must be performed on a Linux system without Monsta installed. The migration script performs the entire data copy and Monsta installation process.

:::

## Minimum requirements

Minimum requirements for migrating Monsta:

:::caution
Check that the "/var" partition on the new server has enough space to transfer Monsta data from the current server.
:::


| Item | Requisito Mínimo |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Espaço em disco](/src/assets/images/p25_image-1645452261754.png) | **Disk space** 40GB free for /var (configurations, database and logs) 300MB free for /opt/monsta (programs and libraries) Make sure the new installation has enough space to perform the migration. |
| ![Memória RAM](/src/assets/images/p25_image-1645452312898.png) | **RAM Memory** 2GB of RAM |
| ![Sistema Operacional](/src/assets/images/p25_image-1645452455434.png) | **Operating System** 64-bit Linux Recommended Operating System: Fedora Server 40 (x86_64 systems) or Ubuntu Server 24. A minimal installation can be used for Monsta. |
| ![Processador](/src/assets/images/p25_image-1645452542916.png) | **Processor** Cores: 2 Speed: 1.8GHz |


:::note
The settings above generally allow monitoring approximately 500 devices with 10 monitors each or a total of 5,000 monitors.
:::

## Migration script

Logged in as root on your server, download the migration script as in the example below:

### Fedora/Red-Hat/Ubuntu/Debian

```shell
yum install -y wget || apt-get install -y wget
wget https://www.monsta.com.br/monsta/download/migrate.sh
chmod +x migrate.sh
```

## Starting the transfer

After downloading the script, run it with the following syntax:

```shell
./migrate.sh
```

Before starting the migration and Monsta installation process, the script will request SSH access information to the source server: IP address/hostname, connection port and a user with root privileges.

These details are necessary to establish a secure remote connection between environments. From this access, the script will stop services on the old server, transfer the complete file structure, logs and databases preserving file permissions, and register and start Monsta services on the new server.

:::note
The elapsed time for this transfer will depend on the size of the existing database, and may take from minutes to several hours.
:::

:::danger[Important]
For the migrate script to run successfully and ensure the copy and creation of all files and directories with the correct permissions (including system files, logs, and sensitive configurations), it is **mandatory** that execution is performed by a user with **Superuser (`root`)** privileges on **both servers** (Source and Destination).

If a **timeout** error occurs during the execution of `migrate.sh`, check if the SSH port on the remote server is open in the firewall for access from the local server.

In case of failure, even after following the usage instructions of `migrate.sh`, **send the monsta_migration.log file to our support**.
:::