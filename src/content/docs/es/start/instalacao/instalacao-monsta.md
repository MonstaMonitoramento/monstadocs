---
title: Instalación de Monsta
sidebar:
  order: 3
---
## Requisitos mínimos

Esta es la configuración mínima para la instalación de Monsta:

| Item | Requisito Mínimo |
| :---: | :--- |
| ![HD](../../../../../assets/images/p25_image-1645452261754.png) | **Espacio en disco**<br />40GB libres para /var (configuraciones, base de datos y registros)<br />300MB libres para /opt/monsta (programas y bibliotecas) |
| ![RAM](../../../../../assets/images/p25_image-1645452312898.png) | **Memoria RAM**<br />2GB de memoria RAM |
| ![SO](../../../../../assets/images/p25_image-1645452455434.png) | **Sistema operativo**<br />Linux 64 bits<br />Sistema operativo Linux recomendado: Fedora Server |
| ![CPU](../../../../../assets/images/p25_image-1645452542916.png) | **Procesador**<br />Núcleos: 2<br />Velocidad: 1.8GHz |

:::caution[Importante]
Las configuraciones anteriores permiten, en general, supervisar aproximadamente 500 dispositivos con 10 monitores cada uno o un total de 5.000 monitores.
:::

## Descarga del archivo

Inicie sesión en su servidor Linux como root y ejecute los comandos a continuación:

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

A partir de ahora, Monsta está instalado en su servidor y puede accederse a través de los puertos 80 (http) y 443 (https):

:::note
Si su red tiene un cortafuegos que controla los accesos a Internet, permita el acceso a los siguientes hosts:  

* mind.monsta.com.br  
* store.monsta.com.br
:::

:::tip
La comunicación con los hosts anteriores permite:  

* Copia de seguridad automática de las configuraciones.  
* Restauración de la copia de seguridad en caso de alguna falla.  
* Envío de notificaciones por correo electrónico, SMS y Telegram.  
* Verificación del estado de la comunicación entre el Monsta instalado en su servidor y la Nube de Monsta. De este modo es posible recibir alertas en caso de paradas inesperadas del servicio de monitorización, como el apagado incorrecto del servidor o una falla en el enlace de Internet.  
* Autenticación de las claves de licencia.  
* Comprobar y actualizar la versión del sistema.
:::

## Primer acceso a Monsta

Abra un navegador y acceda:

![image-1645528439997.png](../../../../../assets/images/p83_image-1645528439997.png)

La siguiente pantalla solicita un inicio de sesión en la nube. Si aún no tiene una cuenta, haga clic en "Crear cuenta":

![image-1741981403822.png](../../../../../assets/images/p83_image-1741981403822.png)

Rellene los campos para crear su cuenta en la nube y haga clic en "Regístrese":

![image-1741981571242.png](../../../../../assets/images/p83_image-1741981571242.png)

A continuación recibirá un correo electrónico con un código para validar su cuenta. Introdúzcalo en la pantalla siguiente y haga clic en Confirmar:

![image-1741981652915.png](../../../../../assets/images/p83_image-1741981652915.png)

Después de este procedimiento, será dirigido a la pantalla de licencias. Como se trata de una cuenta nueva, no se mostrará ninguna licencia y podrá elegir si desea suscribirse a una licencia o activar la versión de prueba. Haga clic en el botón "Activar prueba" para habilitar los 30 días de prueba de Monsta en su empresa:

![image-1741981798571.png](../../../../../assets/images/p83_image-1741981798571.png)

Se le dirigirá a la pantalla para establecer una contraseña para el usuario "admin" de Monsta. Introduzca su contraseña y haga clic en el botón "Confirmar":

![image-1741981958907.png](../../../../../assets/images/p83_image-1741981958907.png)

Ahora será redirigido a la pantalla principal de Monsta:

![image-1741982076022.png](../../../../../assets/images/p83_image-1741982076022.png)

Desde esta pantalla podrá crear y gestionar los dispositivos que se van a supervisar.

Para más información, consulte el [Manual del Usuario](/es/manual/manual-usuario) de Monsta.

:::tip
Si ha instalado su servidor y necesita ayuda para configurar las direcciones IP en Fedora, utilice este tutorial: [Cambiar la dirección IP en un servidor Fedora](/es/extra/linux/alterar-o-endereco-ip-em-um-servidor-fedora)
:::