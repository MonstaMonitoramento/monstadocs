---
title: Configurando el SNMP en Linux
description: ¿Cuál es la mejor forma de monitorizar un Linux? Es a través del SNMP. Este
  tutorial orienta cómo configurar el SNMP en distribuciones Linux que utilizan
  gestores de paquetes con los comandos yum y apt-get, como Fedora, CentOS,
  RedHat, Debian, Ubuntu, Mint, entre otros.
sidebar:
  order: 1
---
La mejor forma de supervisar un servidor o estación Linux (Red Hat, Fedora, Debian, Ubuntu, Mint, CentOS, Rocky Linux, Suse, OpenSuse... prácticamente cualquier distribución Linux) es a través del `SNMP`. Este tutorial tiene como objetivo instalar el servicio `snmpd` y realizar una configuración básica del servicio para poner a disposición la información a Monsta.

:::note
Existen diversas distribuciones Linux, cada una con sus particularidades. La información a continuación puede no funcionar en su distribución.
:::

## Instalación

### Sistemas que utilizan yum

Conectado como root, en la terminal de Linux escriba:

```shell
yum install net-snmp
```

### Sistemas que utilizan apt-get

Conectado como root, en la terminal de Linux escriba:

```shell
apt-get install snmpd
```

## Configuración del archivo snmpd.conf

En general, el archivo snmpd.conf se encuentra en `/etc/snmp/`. Haga una *copia de seguridad* del archivo original:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.old
```

Edite el nuevo archivo (ejemplo con `vim`: `vim /etc/snmp/snmpd.conf`) según las líneas siguientes:

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

Si el servidor o estación Linux que desea monitorizar tiene un *firewall* habilitado, para acceder al servicio SNMP añada el ejemplo a continuación en las reglas de *firewall* de ese dispositivo. Si su distribución gestiona el *firewall* de forma diferente, abra el puerto de entrada UDP/161.

```shell
firewall-cmd --permanent --zone=public --add-port=161/udp
systemctl restart firewalld
```

:::danger[Atención]
Esta apertura del *firewall* permitirá las consultas SNMP desde cualquier dirección IP. Consulte con su administrador de red para restringir los accesos solo a los hosts necesarios.
:::