---
title: Monsta Installation
sidebar:
  order: 3
---

## Minimum requirements

This is the minimum configuration for installing Monsta:

| Item                                                             | Requisito Mínimo                                                                                                                                 |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![HD](../../../../../assets/images/p25_image-1645452261754.png)  | **Espaço em disco**<br />40GB livre para /var (configurações, banco de dados e logs)<br />300MB livre para /opt/monsta (programas e bibliotecas) |
| ![RAM](../../../../../assets/images/p25_image-1645452312898.png) | **Memória RAM**<br />2GB de memória RAM                                                                                                          |
| ![SO](../../../../../assets/images/p25_image-1645452455434.png)  | **Sistema Operacional**<br />Linux 64bits<br />Sistema Operacional Linux recomendado: Fedora Server                                              |
| ![CPU](../../../../../assets/images/p25_image-1645452542916.png) | **Processador**<br />Cores: 2<br />Velocidade: 1.8GHz                                                                                            |

## Downloading the file

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

Monsta is now installed on your server and can be accessed through ports 80 (http) and 443 (https):

## First access to Monsta

Open a browser and go to:

![image-1645528439997.png](../../../../../assets/images/p83_image-1645528439997.png)

You can choose to authenticate using an existing credential via the **"Entrar com minha conta"** button or start the new user flow by clicking **"Criar nova conta"**.

![](../../../../../assets/images/20260630-105252.png)

Fill in the fields to create your cloud account and proceed by clicking "Next":

![](../../../../../assets/images/Tela_Novo_Usuario.png)

You will then receive an email containing a code to validate your account. Enter it on the screen below and click Confirm:

![](../../../../../assets/images/20260630-111438.png)

After this, you will be directed to the licenses screen. Since this is a new account, no licenses will be shown and you can choose to purchase a license or activate the Trial. Click the "Activate Trial" button to enable Monsta's 30-day trial for your company:

![](../../../../../assets/images/20260630-111706.png)

You will be taken to the screen to set a password for Monsta's "admin" user. Enter your password and click the "Confirm" button:

![image-1741981958907.png](../../../../../assets/images/p83_image-1741981958907.png)

Now you will be redirected to Monsta's main screen:

![image-1741982076022.png](../../../../../assets/images/p83_image-1741982076022.png)

From this screen you can create and manage the devices to be monitored.

For more information, consult the [User Manual](/en/manual/manual-usuario) of Monsta.