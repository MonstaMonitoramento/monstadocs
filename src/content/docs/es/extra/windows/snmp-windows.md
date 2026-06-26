---
title: "Configurando el SNMP en Windows"
sidebar:
  order: 1
---

Tutorial con el objetivo de activar una configuración básica de los servicios SNMP en sistemas operativos Windows.

## Configurar el servicio SNMP

Conectado como administrador, en el símbolo del sistema escriba:

```powershell
control appwiz.cpl
```

A continuación se mostrará la siguiente pantalla:

![image-1645202947535.png](../../../../../assets/images/p12_image-1645202947535.png)

• Haga clic en “Activar o desactivar las características de Windows”;

![image-1645202976501.png](../../../../../assets/images/p12_image-1645202976501.png)  
• Marque la opción “Protocolo SNMP” y haga clic en Aceptar;

En el símbolo del sistema, escriba:

```powershell
services.msc
```

A continuación se mostrará la siguiente pantalla:

![image-1645203011196.png](../../../../../assets/images/p12_image-1645203011196.png)• Seleccione el elemento “Servicio SNMP”;  
• Haga clic en el menú “Acción” y seleccione “Propiedades”;

![image-1645203056884.png](../../../../../assets/images/p12_image-1645203056884.png)  
• En la pestaña “General”, marque el campo “Tipo de inicio” como “Automático”;

![image-1645203078004.png](../../../../../assets/images/p12_image-1645203078004.png)  
• En la pestaña “Seguridad” haga clic en el botón “Agregar”;  
• En “Derechos de la comunidad” seleccione la opción “SOLO LECTURA”;  
• En “Nombre de la Comunidad” escriba “public”;  
• Haga clic en el botón “Agregar”;  
• Marque la opción “Aceptar paquetes SNMP desde cualquier host”;  
• Haga clic en el botón “Aceptar”.

## Habilitar el acceso al servicio SNMP en el Firewall de Windows

Para habilitar el servicio SNMP en el Firewall de Windows, acceda al símbolo del sistema y escriba:

```powershell
netsh advfirewall firewall add rule name="Servidor SNMP" new dir=in action=allow enable=yes profile=public remoteip=any localport=161 protocol=udp
```



:::note
En general, el SNMP de Windows viene habilitado solo para la red local.
:::