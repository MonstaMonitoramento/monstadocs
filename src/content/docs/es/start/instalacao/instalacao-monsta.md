---
title: Instalación de Monsta
description: Aprenda cómo instalar Monsta y configure rápidamente la plataforma
  de monitorización de la infraestructura de TI siguiendo paso a paso la
  instalación.
sidebar:
  order: 3
---
## Requisitos mínimos

Esta es la configuración mínima para la instalación de Monsta:


| Item | Requisito Mínimo |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| ![HD](/src/assets/images/p25_image-1645452261754.png) | **Espacio en disco** 40GB libres para /var (configuraciones, base de datos y registros) 300MB libres para /opt/monsta (programas y bibliotecas) |
| ![RAM](/src/assets/images/p25_image-1645452312898.png) | **Memoria RAM** 2GB de memoria RAM |
| ![SO](/src/assets/images/p25_image-1645452455434.png) | **Sistema operativo** Linux 64 bits Sistema operativo Linux recomendado: Fedora Server |
| ![CPU](/src/assets/images/p25_image-1645452542916.png) | **Procesador** Núcleos: 2 Velocidad: 1.8GHz |


:::caution[Importante]

Las configuraciones anteriores permiten, en general, supervisar aproximadamente 500 dispositivos con 10 monitores cada uno o un total de 5.000 monitores.

:::

## Descarga del archivo

Inicie sesión en su servidor Linux como root y ejecute los siguientes comandos:

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

A partir de ahora Monsta está instalado en su servidor y puede accederse a través de los puertos 80 (http) y 443 (https).

:::caution[Atención]

Si su Linux tiene un *firewall* habilitado, verifique que los puertos 80/TCP y 443/TCP estén abiertos para entrada (si es FirewallD, [vea este artículo](/es/extra/linux/firewalld-gerenciamento-de-firewall)). De lo contrario, no será posible acceder a la interfaz web de su Monsta. 

:::

:::note

Si su red tiene un *firewall* que controla los accesos a Internet, permita el acceso a los siguientes hosts:

- [mind.monsta.com.br](http://mind.monsta.com.br)
- [store.monsta.com.br](http://store.monsta.com.br)

:::

:::tip 

La comunicación con los hosts anteriores permite:

- Copia de seguridad automática de las configuraciones.
- Restauración de la copia de seguridad en caso de alguna falla.
- Envío de notificaciones por E-mail, SMS y Telegram.
- Comprobación del estado de la comunicación entre el Monsta instalado en su servidor y la Nube de Monsta. Con ello es posible recibir alertas en caso de paradas inesperadas del servicio de monitorización, como el apagado impropio del servidor o fallo en el enlace a Internet.
- Autenticación de las claves de licenciamiento.
- Verificar y actualizar la versión del sistema.

:::

## Primer acceso a Monsta

Abra un navegador y acceda a:

![image-1645528439997.png](/src/assets/images/p83_image-1645528439997.png)

Puede optar por autenticarse utilizando una credencial existente a través del botón **"Entrar con mi cuenta"** o iniciar el flujo de nuevo usuario haciendo clic en **"Crear nueva cuenta"**.

![](/src/assets/images/20260630-105252.png)

Rellene los campos para crear su cuenta en la nube y continúe haciendo clic en "Siguiente":

![](/src/assets/images/Tela_Novo_Usuario.png)

A continuación recibirá un correo electrónico con un código para validar su cuenta. Introdúzcalo en la pantalla siguiente y haga clic en Confirmar:

![](/src/assets/images/20260630-111438.png)

Después de este procedimiento, será dirigido a la pantalla de licencias. Como esta es una cuenta nueva, no se mostrará ninguna licencia y podrá seleccionar si desea contratar una licencia o activar la versión Trial. Haga clic en el botón "Activar Trial" para habilitar los 30 días de prueba de Monsta en su empresa:

![](/src/assets/images/20260630-111706.png)

Se le dirigirá a la pantalla para informar una contraseña para el usuario "admin" de Monsta. Escriba su contraseña y haga clic en el botón "Confirmar":

![image-1741981958907.png](/src/assets/images/p83_image-1741981958907.png)

Ahora será redirigido a la pantalla principal de Monsta:

![image-1741982076022.png](/src/assets/images/p83_image-1741982076022.png)

Desde esta pantalla podrá crear y gestionar los dispositivos a monitorizar.

Para más información, consulte el [Manual del Usuario](/es/manual/manual-usuario) de Monsta.

:::tip 

Si ha instalado su servidor y necesita ayuda para configurar las direcciones IP en Fedora, utilice este tutorial: [Cambiar la dirección IP en un servidor Fedora](/es/extra/linux/alterar-o-endereco-ip-em-um-servidor-fedora)

:::