---
title: "Configurando el SNMP en Mac OS X"
---

Tutorial con el objetivo de activar una configuración básica de los servicios SNMP en un Mac OS X.

## Configurando el servicio SNMP

Abra una sesión de terminal y ejecute el siguiente comando:

```shell
sudo -i
```

Introduzca la contraseña de root.

Ejecute los siguientes comandos para crear un archivo de configuración básica del snmp:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.original
echo “rocommunity public” > /etc/snmp/snmpd.conf
```

Ejecute el siguiente comando para iniciar el servicio de snmp:

```shell
launchctl load -w /System/Library/LaunchDaemons/org.net-snmp.snmpd.plist
```

A partir de ahora el SNMP está disponible en su equipo con Mac OS X y ya puede ser monitorizado por Monsta a través de las versiones 1 y 2c con la comunidad public. El template para este dispositivo es “Apple – Mac OS X”.