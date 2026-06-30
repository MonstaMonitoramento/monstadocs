---
title: Instalación de Monsta
sidebar:
  order: 3
---

## Requisitos mínimos

Esta es la configuración mínima para la instalación de Monsta:

| Item | Requisito Mínimo |
| --- | --- |
| ![HD](../../../../../assets/images/p25_image-1645452261754.png) | **Espacio en disco**<br />40GB libres para /var (configuraciones, base de datos y logs)<br />300MB libres para /opt/monsta (programas y bibliotecas) |
| ![RAM](../../../../../assets/images/p25_image-1645452312898.png) | **Memoria RAM**<br />2GB de memoria RAM |
| ![SO](../../../../../assets/images/p25_image-1645452455434.png) | **Sistema Operativo**<br />Linux 64 bits<br />Sistema operativo Linux recomendado: Fedora Server |
| ![CPU](../../../../../assets/images/p25_image-1645452542916.png) | **Procesador**<br />Núcleos: 2<br />Velocidad: 1.8GHz |

:::caution[Importante]
Las configuraciones anteriores permiten, en general, supervisar aproximadamente 500 dispositivos con 10 monitores cada uno o un total de 5.000 monitores.
:::

## Descarga del archivo

Conectado a su servidor Linux como root, ejecute los comandos a continuación:

#### Fedora/Red Hat

```shell
yum install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.rpm
```

#### Ubuntu/Debian

```shell
apt-get install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.deb
```

## Instalación

Tras descargar el archivo de instalación de Monsta, ejecute el siguiente comando:

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
Si su red tiene un firewall que controla el acceso a Internet, permita el acceso a los siguientes hosts:  

* mind.monsta.com.br  
* agent.monsta.com.br
:::

:::tip
La comunicación con los hosts anteriores permite:  

* Copia de seguridad automática de las configuraciones.  
* Restauración de la copia de seguridad en caso de alguna falla.  
* Envío de notificaciones por correo electrónico, SMS y Telegram.  
* Verificación del estado de la comunicación entre Monsta instalado en su servidor y la Nube de Monsta. Con ello es posible recibir alertas en caso de paradas inesperadas del servicio de monitorización, como el apagado impropio del servidor o una falla en el enlace a Internet.  
* Autenticación de las claves de licencia.  
* Verificar y actualizar la versión del sistema.  
* Conexión con los agentes para el monitoreo de redes remotas.
:::

## Primer acceso a Monsta

Abra un navegador y acceda:

![image-1645528439997.png](../../../../../assets/images/p83_image-1645528439997.png)

Puede optar por autenticarse utilizando una credencial existente mediante el botón **"Entrar con mi cuenta"** o iniciar el flujo de nuevo usuario haciendo clic en **"Crear nueva cuenta"**.

![](../../../../../assets/images/20260630-105252.png)

Rellene los campos para crear su cuenta en la nube y avance haciendo clic en "Siguiente":

![](../../../../../assets/images/Tela_Novo_Usuario.png)

A continuación recibirá un correo electrónico con un código para validar su cuenta. Indíquelo en la pantalla siguiente y haga clic en Confirmar:

![](../../../../../assets/images/20260630-111438.png)

Tras este procedimiento, será dirigido a la pantalla de licencias. Como esta es una cuenta nueva, no se mostrará ninguna licencia y podrá elegir si desea contratar una licencia o activar la versión Trial. Haga clic en el botón "Activar Trial" para habilitar los 30 días de prueba de Monsta en su empresa:

![](../../../../../assets/images/20260630-111706.png)

Será dirigido a la pantalla para indicar una contraseña para el usuario "admin" de Monsta. Escriba su contraseña y haga clic en el botón "Confirmar":

![image-1741981958907.png](../../../../../assets/images/p83_image-1741981958907.png)

Ahora será redirigido a la pantalla principal de Monsta:

![image-1741982076022.png](../../../../../assets/images/p83_image-1741982076022.png)

Desde esta pantalla podrá crear y gestionar los dispositivos que serán monitorizados.

Para más información, consulte el [Manual del Usuario](/es/manual/manual-usuario) de Monsta.

:::tip
Si instaló su servidor y necesita ayuda para configurar las direcciones IP en Fedora, utilice este tutorial: [Cambiar la dirección IP en un servidor Fedora](/es/extra/linux/alterar-o-endereco-ip-em-um-servidor-fedora)
:::