---
title: "Configurando el SNMP en la Routerboard MikroTik"
---

Tutorial con el objetivo de activar una configuración básica de los servicios SNMP en una Routerboard de MikroTik.

## Configurando el servicio SNMP

:::tip
Este procedimiento también puede realizarse utilizando el software Winbox de la propia MikroTik.
:::



Abra un navegador de internet y escriba en la URL la dirección del MikroTik. Aparecerá la siguiente pantalla:

![image-1645205030195.png](../../../../../assets/images/p16_image-1645205030195.png)Introduzca el usuario y la contraseña de su dispositivo (el predeterminado es admin y deje la contraseña en blanco). A continuación, en el menú de la izquierda, haga clic en IP y debajo haga clic en SNMP:

![image-1645205057404.png](../../../../../assets/images/p16_image-1645205057404.png)Rellene los campos “Contact Info” con la persona responsable de contacto de este dispositivo y el campo “Location” con su ubicación.

## Configurando una Comunidad

A continuación, haga clic en el botón “Communities”, se mostrará la siguiente pantalla:

![image-1645205091972.png](../../../../../assets/images/p16_image-1645205091972.png)  
Si ya existe la comunidad public, modifique la información de configuración según la pantalla de abajo; de lo contrario, haga clic en el botón “Add New” y rellene la pantalla con la siguiente información:

![image-1645205110836.png](../../../../../assets/images/p16_image-1645205110836.png)  
Haga clic en el botón Ok y, a continuación, en el botón Close para cerrar la pantalla de edición de comunidades.

## Aplicar las Configuraciones

En la pantalla de SNMP, haga clic en el botón Apply.

![image-1645205142984.png](../../../../../assets/images/p16_image-1645205142984.png)  
  
A partir de ahora el SNMP está disponible en su dispositivo MikroTik y ya puede ser monitorizado por Monsta a través de las versiones 1 y 2c con la comunidad public.