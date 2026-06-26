---
title: "Configurando el SNMP en Linux"
sidebar:
  order: 1
---

Tutorial con el objetivo de activar una configuración básica de los servicios SNMP en sistemas operativos Linux.



:::note
Existen diversas distribuciones de Linux, cada una con sus particularidades. La información que sigue puede no funcionar en su distribución.
:::

## Instalación

### Sistemas que usan yum

Conectado como root, en la terminal de Linux escriba:

```shell
yum install net-snmp
```

### Sistemas que usan apt-get

Conectado como root, en la terminal de Linux escriba:

```shell
apt-get install snmpd
```

## Configuración del archivo snmpd.conf

En general, el archivo snmpd.conf se encuentra en `/etc/snmp/`. Haga una *copia de seguridad* del archivo original:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.old
```

Edite el nuevo archivo (ejemplo con `vim`: `vim /etc/snmp/snmpd.conf`) conforme las líneas siguientes:

```bash
rocommunity public  
sysLocation “Localização deste servidor”  
sysContact seu@email.com.br
```

## Reiniciar y habilitar el servicio SNMP
### Sistemas con Systemd

En la terminal, escriba:

```shell
systemctl restart snmpd
systemctl enable snmpd
```

### Sistemas con Systemv

En la terminal, escriba:

```shell
service snmpd restart
```

## Permitir el servicio SNMP en el firewall de Linux

Si el servidor o estación Linux que desea monitorizar tiene un *firewall* habilitado, para acceder al servicio SNMP añada el ejemplo siguiente en las reglas de *firewall* de este dispositivo. Si su distribución gestiona el *firewall* de forma diferente, abra el puerto de entrada UDP/161.

```shell
firewall-cmd --permanent --zone=public --add-port=161/udp
systemctl restart firewalld
```

:::danger[Atención]
Esta apertura del *firewall* permitirá consultas SNMP desde cualquier dirección IP. Consulte con su administrador de red para restringir los accesos solo a los hosts necesarios.
:::