---
title: Migration to a New Server
description: Learn how to migrate Monsta to a new server while securely preserving
  configurations, monitoring, history and platform data.
---
This tutorial shows how to migrate Monsta from version >5.0 to another server.

:::danger[Warning]

Do not install Monsta on the new server! This procedure must be performed on a Linux machine without Monsta installed. The migration script performs the entire process of copying the data and installing Monsta.

:::

## Minimum Requirements

Minimum requirements for migrating Monsta:

:::caution
Check that the "/var" partition on the new server has enough space to transfer Monsta data from the current server.
:::


| Item | Minimum Requirement |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Disk space](/src/assets/images/p25_image-1645452261754.png) | **Disk space** 40GB free for /var (configurations, database and logs) 300MB free for /opt/monsta (programs and libraries) Ensure the new installation has enough space to perform the migration. |
| ![RAM](/src/assets/images/p25_image-1645452312898.png) | **RAM** 2GB of RAM |
| ![Operating System](/src/assets/images/p25_image-1645452455434.png) | **Operating System** 64-bit Linux Recommended Linux OS: Fedora Server 40 (x86_64 systems) or Ubuntu Server 24. A minimal installation can be used for Monsta. |
| ![Processor](/src/assets/images/p25_image-1645452542916.png) | **Processor** Cores: 2 Speed: 1.8GHz |


:::note
The above settings generally allow monitoring approximately 500 devices with 10 monitors each, or a total of 5,000 monitors.
:::

## Migration script

Logged in as root on your server, download the migration script as shown below:

### Fedora/Red-Hat/Ubuntu/Debian

```shell
yum install -y wget || apt-get install -y wget
wget https://www.monsta.com.br/monsta/download/migrate.sh
chmod +x migrate.sh
```

## Starting the transfer

After downloading the script, run it with the following syntax:

`./migrate.sh`

Before starting the migration and installation process, the script will request SSH access information for the source server: IP address/hostname, connection port, and a user with root privileges.

This information is required to establish a secure remote connection between the environments. Using that access, the script will stop services on the old server, transfer the complete structure of files, logs and databases while preserving file permissions, and register and start Monsta services on the new server.

:::note
The elapsed time for this transfer will depend on the size of the existing database, and may range from minutes to several hours.
:::

:::danger[Important]
For the migrate script to execute successfully and ensure the copying and creation of all files and directories with correct permissions (including system files, logs, and sensitive configurations), it is **mandatory** that it be run by a user with **Superuser (`root`)** privileges on **both servers** (Source and Destination). 

If a **timeout** error occurs during the execution of `migrate.sh`, check whether the SSH port on the remote server is open in the firewall for access from the local server.  

If a failure occurs even after following the `migrate.sh` usage instructions, **send the monsta_migration.log file to our support**.  
:::