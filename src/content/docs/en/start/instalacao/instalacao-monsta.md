---
title: Monsta Installation
description: Learn how to install Monsta and quickly set up the IT infrastructure
  monitoring platform by following the installation step-by-step.
sidebar:
  order: 3
---
## Minimum requirements

This is the minimum configuration for installing Monsta:


| Item | Minimum Requirement |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| ![HD](/src/assets/images/p25_image-1645452261754.png) | **Disk space** 40GB free for /var (configurations, database and logs) 300MB free for /opt/monsta (programs and libraries) |
| ![RAM](/src/assets/images/p25_image-1645452312898.png) | **RAM** 2GB of RAM |
| ![SO](/src/assets/images/p25_image-1645452455434.png) | **Operating System** 64-bit Linux Recommended Linux distribution: Fedora Server |
| ![CPU](/src/assets/images/p25_image-1645452542916.png) | **Processor** Cores: 2 Speed: 1.8GHz |


:::caution[Important]

The above settings generally allow monitoring approximately 500 devices with 10 monitors each, or a total of 5,000 monitors.

:::

## Download the file

Logged in to your Linux server as root, run the commands below:

#### Fedora/Red Hat

```shell
yum install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.rpm
```

#### Ubuntu/Debian

```shell
apt-get install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.deb
```

## Installation

After downloading the Monsta installation file, run the following command:

#### Fedora/Red Hat

```shell
dnf install -y monsta-latest.rpm
```

#### Ubuntu/Debian

```shell
export PATH=/usr/local/sbin:/usr/sbin:/sbin:$PATH
dpkg -i monsta-latest.deb
```

Monsta is now installed on your server and can be accessed via ports 80 (http) and 443 (https):

:::note

If your network has a firewall controlling internet access, allow access to the following hosts:

- [mind.monsta.com.br](http://mind.monsta.com.br)
- [store.monsta.com.br](http://store.monsta.com.br)

:::

:::tip 

Communication with the hosts above allows:

- Automatic backup of configurations.
- Restoration of backup in case of a failure.
- Sending notifications by Email, SMS and Telegram.
- Checking the communication status between the Monsta installed on your server and the Monsta Cloud. This makes it possible to receive alerts in case of unexpected monitoring service stoppages, such as improper server shutdown or internet link failure.
- License key authentication.
- Check and update the system version. 

:::

## First access to Monsta

Open a browser and access:

![image-1645528439997.png](/src/assets/images/p83_image-1645528439997.png)

You can choose to authenticate using an existing credential via the **"Sign in with my account"** button or start the new user flow by clicking **"Create new account"**.

![](/src/assets/images/20260630-105252.png)

Fill in the fields to create your cloud account and proceed by clicking "Next":

![](/src/assets/images/Tela_Novo_Usuario.png)

You will then receive an email containing a code to validate your account. Enter it on the screen below and click Confirm:

![](/src/assets/images/20260630-111438.png)

After this procedure, you will be directed to the licenses screen. Since this is a new account, no license will be shown and you can choose whether to purchase a license or activate the Trial version. Click the "Activate Trial" button to enable 30 days of Monsta trial in your company:

![](/src/assets/images/20260630-111706.png)

You will be taken to the screen to provide a password for the Monsta "admin" user. Enter your password and click the "Confirm" button:

![image-1741981958907.png](/src/assets/images/p83_image-1741981958907.png)

Now you will be redirected to the Monsta main screen:

![image-1741982076022.png](/src/assets/images/p83_image-1741982076022.png)

From this screen you can create and manage the devices to be monitored.

For more information, consult the [User Manual](/en/manual/manual-usuario) of Monsta.

:::tip 

If you installed your server and need help configuring IP addresses on Fedora, use this tutorial: [Change the IP address on a Fedora server](/en/extra/linux/alterar-o-endereco-ip-em-um-servidor-fedora)

:::