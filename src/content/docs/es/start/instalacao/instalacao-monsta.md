---
title: Instalación de Monsta
sidebar:
  order: 3
---

## Requisitos mínimos

Esta es la configuración mínima para la instalación de Monsta:

| Item                                                             | Requisito Mínimo                                                                                                                                 |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![HD](../../../../../assets/images/p25_image-1645452261754.png)  | **Espacio en disco**<br />40GB libres para /var (configuraciones, base de datos y registros)<br />300MB libres para /opt/monsta (programas y bibliotecas) |
| ![RAM](../../../../../assets/images/p25_image-1645452312898.png) | **Memoria RAM**<br />2GB de memoria RAM                                                                                                          |
| ![SO](../../../../../assets/images/p25_image-1645452455434.png)  | **Sistema operativo**<br />Linux 64bits<br />Sistema operativo Linux recomendado: Fedora Server                                                 |
| ![CPU](../../../../../assets/images/p25_image-1645452542916.png) | **Procesador**<br />Núcleos: 2<br />Velocidad: 1.8GHz                                                                                            |

## Descarga del archivo

Conectado en su servidor Linux como root, ejecute los siguientes comandos:

#### Fedora/Red Hat

```shell
yum install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.rpm
```

#### Ubuntu/Debian

```shell
apt-get install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.deb
```

## Instalación

Después de descargar el archivo de instalación de Monsta, ejecute el siguiente comando:

#### Fedora/Red Hat

```shell
dnf install -y monsta-latest.rpm
```

#### Ubuntu/Debian

```shell
export PATH=/usr/local/sbin:/usr/sbin:/sbin:$PATH
dpkg -i monsta-latest.deb
```

A partir de ahora Monsta está instalado en su servidor y se puede acceder a él a través de los puertos 80 (http) y 443 (https):

## Primer acceso a Monsta

Abra un navegador y acceda:

![image-1645528439997.png](../../../../../assets/images/p83_image-1645528439997.png)

Puede optar por autenticarse utilizando una credencial existente a través del botón **"Iniciar sesión con mi cuenta"** o iniciar el flujo de nuevo usuario haciendo clic en **"Crear cuenta nueva"**.

![](../../../../../assets/images/20260630-105252.png)

Rellene los campos para crear su cuenta en la nube y avance haciendo clic en "Siguiente":

![](../../../../../assets/images/Tela_Novo_Usuario.png)

A continuación recibirá un correo electrónico que contiene un código para validar su cuenta. Introduzca dicho código en la pantalla siguiente y haga clic en Confirmar:

![](../../../../../assets/images/20260630-111438.png)

Tras este procedimiento, se le dirigirá a la pantalla de licencias. Al ser una cuenta nueva, no se mostrará ninguna licencia y podrá seleccionar si desea suscribir una licencia o activar la versión Trial. Haga clic en el botón "Activar Trial" para habilitar los 30 días de prueba de Monsta en su empresa:

![](../../../../../assets/images/20260630-111706.png)

Será dirigido a la pantalla para establecer una contraseña para el usuario "admin" de Monsta. Escriba su contraseña y haga clic en el botón "Confirmar":

![image-1741981958907.png](../../../../../assets/images/p83_image-1741981958907.png)

Ahora será redirigido a la pantalla principal de Monsta:

![image-1741982076022.png](../../../../../assets/images/p83_image-1741982076022.png)

Desde esta pantalla podrá crear y administrar los dispositivos que serán monitorizados.

Para más información, consulte el [Manual del Usuario](/es/manual/manual-usuario) de Monsta.