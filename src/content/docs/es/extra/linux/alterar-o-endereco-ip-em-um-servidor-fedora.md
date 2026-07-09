---
title: "Cambiar la dirección IP en un servidor Fedora"
sidebar:
  order: 2
---

Este tutorial paso a paso le guiará en el proceso de cambiar la dirección IP en un servidor Linux Fedora. Aprenda a configurar una dirección IP estática o dinámica para garantizar la conectividad de red óptima para su servidor.

## Configurar la IP del servidor

Inicie sesión con las credenciales de root en su servidor. Una vez conectado, instale el programa para gestionar interfaces de red:

```shell
dnf install -y NetworkManager-tui
```

Tras la instalación, ejecute el administrador:

```
nmtui
```

Siga la secuencia a continuación para editar las configuraciones de red:



![image-1645530757865.png](../../../../../assets/images/p85_image-1645530757865.png)
- Seleccione “Editar la conexión”;
- Pulse “Enter”.
![image-1718907509891.png](../../../../../assets/images/p85_image-1718907509891.png)
- Seleccione su conexión de red;
- Seleccione “Editar”.
![image-1718829976173.png](../../../../../assets/images/p85_image-1718829976173.png)
Utilice la tecla “TAB” para navegar entre los campos. Si su red dispone de un servidor DHCP habilitado, deje los campos de “CONFIGURACIÓN DE IPVx” en Automático. Si desea una IP fija para su servidor, haga lo siguiente:
- Seleccione el campo “CONFIGURACIÓN DE IPVx” y pulse “Enter”;- Seleccione el modo “Manual”;
- Seleccione “Mostrar” y pulse “Enter”;
- Rellene los campos conforme a las configuraciones de su red; Recuerde informar la máscara de red después de la dirección IP. En el ejemplo adjunto la máscara es /24.
- Al final, seleccione “OK”;
- Pulse “Enter”.
- Pulse la tecla “ESC” para volver a la pantalla inicial.
![image-1645531410027.png](../../../../../assets/images/p85_image-1645531410027.png)
- Seleccione “Activar una conexión” y pulse “Enter”.
![image-1645531449446.png](../../../../../assets/images/p85_image-1645531449446.png)
- Seleccione la interfaz de red a la que cambió la IP y pulse “Enter” para desactivarla;
- A continuación, pulse “Enter” de nuevo para activarla.
- Pulse “ESC” hasta salir del programa y volver al indicador de comandos.

## Acceder al Monsta

Tras configurar la dirección IP del servidor, abra un navegador de internet y acceda a:

![image-1645531726319.png](../../../../../assets/images/p85_image-1645531726319.png)

o

![image-1645531751491.png](../../../../../assets/images/p85_image-1645531751491.png)  
  
Se mostrará la pantalla de inicio de sesión de Monsta. Para iniciar sesión, utilice sus credenciales.

## Reglas de firewall (Opcional)

Si su red dispone de un cortafuegos que controla los accesos a Internet, permita los siguientes hosts y puertos:

>- Host ``a.ntp.br`` y 2.fedora.pool.ntp.org  
>- Host ``mind.monsta.com.br`` en el puerto 443/TCP  
>- Host ``mind.monsta.com.br`` en el puerto 80/TCP

Los puertos anteriores para ``mind.monsta.com.br`` y ``www.monsta.com.br`` permiten:

>- Copia de seguridad automática de las configuraciones.  
>- Restauración de la copia de seguridad en caso de alguna falla.  
>- Envío de notificaciones por E-mail, SMS y Telegram.  
>- Comprobación del estado de la comunicación entre el Monsta instalado en su servidor y la Nube de Monsta. Con esto es posible recibir alertas en caso de paradas inesperadas del servicio de monitorización, tal como el apagado impropio del servidor o fallo del enlace a Internet.  
>- Autenticación de las claves de licencia.  
>- Verificar y actualizar la versión del sistema.

:::tip
Utilice este tutorial para configurar las reglas de su cortafuegos en caso de que su instalación de Fedora haya instalado el sistema FirewallD: [Gestión de Firewall - FirewallD](/es/extra/linux/firewalld-gerenciamento-de-firewall)
:::