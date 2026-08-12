---
title: Migration to a New Server
description: Learn how to migrate Monsta to a new server while safely preserving
  configurations, monitors, history and platform data.
---
This tutorial shows how to migrate Monsta from version >5.0 to another server.

:::danger[Attention]

Do not install Monsta on the new server! This procedure must be carried out on a Linux system without Monsta installed. The migration script performs the entire process of copying the data and installing Monsta.

:::

## Minimum requirements

Minimum requirements for migrating Monsta:

:::caution
Check that the "/var" partition on the new server has enough space for transferring Monsta data from the current server.
:::


| Item | Minimum Requirement |
| --- | --- |
| ![Disk space](/src/assets/images/p25_image-1645452261754.png) | **Disk space**<br>• 40GB free for `/var` (configurations, database and logs)<br>• 300MB free for `/opt/monsta` (programs and libraries)<br><br>Make sure the new installation has enough space to perform the migration. |
| ![RAM](/src/assets/images/p25_image-1645452312898.png) | **RAM**<br>• 2GB of RAM |
| ![Operating System](/src/assets/images/p25_image-1645452455434.png) | **Operating System**<br>• 64-bit Linux<br>• Recommended Linux OS: Fedora Server 40 (x86_64 systems) or Ubuntu Server 24<br><br>A minimal installation can be used for Monsta. |
| ![Processor](/src/assets/images/p25_image-1645452542916.png) | **Processor**<br>• Cores: 2<br>• Speed: 1.8GHz |


:::note
The above settings generally allow checking approximately 500 devices with 10 monitors each, for a total of 5,000 monitors.
:::

## Migration script

Log in to your new server as root and download the migration script as in the example below:

### Fedora/Red-Hat/Ubuntu/Debian

```shell
yum install -y wget || apt-get install -y wget
wget https://www.monsta.com.br/monsta/download/migrate.sh
chmod +x migrate.sh
```

## Starting the transfer

After downloading the script, execute it with the following syntax:

```shell
./migrate.sh
```

Before starting the migration and installation process, the script will ask for SSH access information to the source server: IP address/hostname, connection port and a user with root privileges.

These details are necessary to establish a secure remote connection between environments. From that access, the script will stop services on the old server, transfer the complete structure of files, logs and databases preserving file permissions, and register and start Monsta services on the new server.

:::note
The elapsed time for this transfer will depend on the size of the existing database, and may take from minutes to several hours.
:::

:::danger[Important]
For the migrate script to run successfully and ensure the copying and creation of all files and directories with the correct permissions (including system files, logs, and sensitive configurations), it is **mandatory** that execution is done by a user with **Superuser (`root`)** privileges on **both servers** (Source and Destination). 

If a **timeout** error occurs during the execution of `migrate.sh`, check whether the SSH port on the remote server is open in the firewall for access from the local server.  

In case of failure, even after following the `migrate.sh` usage instructions, **send the monsta_migration.log file to our support**.  
:::