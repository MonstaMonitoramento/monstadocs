---
title: Monitorizar el servidor DNS Unbound
---

Tutorial para monitorizar el servidor DNS Unbound mediante el servicio SNMP.

![image-1740053252228.png](../../../../../assets/images/p11_image-1740053252228.png)

:::note
Los comandos de Linux de este tutorial son compatibles con distribuciones Linux como CentOS y Fedora Server. Si usa otra distribución (como Debian o Ubuntu), comandos como `yum`, por ejemplo, deberán ser reemplazados. 
:::

## Instalación de Unbound

Para instalar el servidor DNS Unbound y configurarlo para que se inicie automáticamente, escriba los siguientes comandos:

```shell
yum install unbound
systemctl enable unbound
systemctl start unbound
```

## Configuración

Edite el archivo `/etc/unbound/unbound.conf` y habilite la opción para generar estadísticas como se muestra a continuación:

`extended-statistics: yes`

El siguiente ejemplo muestra una configuración básica del servidor DNS Unbound con la opción para mostrar estadísticas extendidas habilitada.

```bash
server:
  verbosity: 1
  satistics-interval: 0
  statistics-cumulative: no
  extended-statistics: yes
  num-threads: 2
  interface: 0.0.0.0
  interface-automatic: yes
  outgoing-range: 5000
  so-rcvbuf: 4m
  so-sndbuf: 4m
  msg-cache-size: 25m
  msg-cache-slabs: 2
  num-queries-per-thread: 2500
  rrset-cache-size: 50m
  rrset-cache-slabs: 2
  infra-cache-slabs: 2
  access-control: 0.0.0.0/0 allow
  chroot: ""
  username: "unbound"
  directory: "/etc/unbound"
  log-time-ascii: yes
  pidfile: "/var/run/unbound/unbound.pid"
  harden-glue: yes
  harden-dnssec-stripped: yes
  harden-below-nxdomain: yes
  harden-referral-path: yes
  use-caps-for-id: no
  unwanted-reply-threshold: 10000000
  prefetch: yes
  prefetch-key: yes
  rrset-roundrobin: yes
  minimal-responses: yes
  trusted-keys-file: /etc/unbound/keys.d/*.key
  auto-trust-anchor-file: "/var/lib/unbound/root.key"
  val-clean-additional: yes
  val-permissive-mode: no
  val-log-level: 1
  key-cache-slabs: 2
  include: /etc/unbound/local.d/*.conf

remote-control:
  control-enable: yes
  server-key-file: "/etc/unbound/unbound_server.key"
  server-cert-file: "/etc/unbound/unbound_server.pem"
  control-key-file: "/etc/unbound/unbound_control.key"
  control-cert-file: "/etc/unbound/unbound_control.pem"
  include: /etc/unbound/conf.d/*.conf
```

## Reiniciando el servicio unbound

Después, reinicie el servicio con el comando:

```shell
systemctl restart unbound
```

## Configurando el SNMP para enviar las estadísticas de Unbound

:::note
Si su sistema no tiene el servidor SNMP configurado, vea [Configurando el SNMP en Linux](/es/extra/linux/snmp-linux)
:::

Haga una copia de seguridad del archivo /etc/snmpd.conf:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.backup
```

Edite el archivo /etc/snmp/snmpd.conf y configúrelo según el siguiente ejemplo. Si lo desea, cambie el nombre de la comunidad.

```text
rocommunity public
extend .1.3.6.1.3.1983.1.1 Unbound /usr/bin/cat /tmp/unbound_stats.txt
```

## Reiniciando y habilitando el servicio SNMP

En la terminal, escriba:

```shell
systemctl restart snmpd
```

## Añadiendo las estadísticas al cron

En la terminal, escriba el siguiente comando:

```shell
(crontab -l ; echo '*/1 * * * * /usr/sbin/unbound-control stats_noreset > /tmp/unbound_stats.txt' ) | crontab -
```

Tras estos procedimientos, ya es posible utilizar la plantilla “Unbound – DNS Server” para monitorizar las estadísticas de su servidor DNS.

## Extra

En algunos sistemas, el comando cat se encuentra en un directorio distinto al configurado en el archivo snmpd.conf. Para evitar problemas, puede crear un enlace simbólico con el siguiente comando:

```shell
ln -s /usr/sbin/cat /bin
```

## Prueba de las configuraciones

Para comprobar si las configuraciones realizadas son correctas, ejecute los pasos siguientes:

```shell
yum install net-snmp-utils
snmpwalk -c public -v2c localhost .1.3.6.1.3.1983.1.1
```

El comando snmpwalk debería devolver información similar al siguiente ejemplo:

> SNMPv2-SMI::experimental.1983.1.1.1.0 = INTEGER: 1\
> SNMPv2-SMI::experimental.1983.1.1.2.1.2.7.85.110.98.111.117.110.100 = STRING: "/usr/bin/cat"\
> SNMPv2-SMI::experimental.1983.1.1.2.1.3.7.85.110.98.111.117.110.100 = STRING: "/tmp/unbound_stats.txt"\
> SNMPv2-SMI::experimental.1983.1.1.2.1.4.7.85.110.98.111.117.110.100 = ""\
> SNMPv2-SMI::experimental.1983.1.1.2.1.5.7.85.110.98.111.117.110.100 = INTEGER: 5\
> SNMPv2-SMI::experimental.1983.1.1.2.1.6.7.85.110.98.111.117.110.100 = INTEGER: 1\
> SNMPv2-SMI::experimental.1983.1.1.2.1.7.7.85.110.98.111.117.110.100 = INTEGER: 1\
> SNMPv2-SMI::experimental.1983.1.1.2.1.20.7.85.110.98.111.117.110.100 = INTEGER: 4\
> SNMPv2-SMI::experimental.1983.1.1.2.1.21.7.85.110.98.111.117.110.100 = INTEGER: 1