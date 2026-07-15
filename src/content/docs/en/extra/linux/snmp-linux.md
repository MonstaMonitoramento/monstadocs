---
title: Configuring SNMP on Linux
description: What is the best way to monitor a Linux system? It's through SNMP. This
  tutorial guides how to configure SNMP on Linux distributions that use package
  managers with the yum and apt-get commands, such as Fedora, CentOS, RedHat,
  Debian, Ubuntu, Mint, among others.
sidebar:
  order: 1
---
The best way to monitor a Linux server or workstation (Red Hat, Fedora, Debian, Ubuntu, Mint, CentOS, Rocky Linux, Suse, OpenSuse... practically any Linux distribution) is through `SNMP`. This tutorial aims to install the `snmpd` service and perform a basic configuration of the service to make the information available to Monsta.

:::note
There are many Linux distributions, each with its own particularities. The information below may not work on your distribution.
:::

## Installation

### Systems using yum

Logged in as root, on the Linux terminal type:

```shell
yum install net-snmp
```

### Systems using apt-get

Logged in as root, on the Linux terminal type:

```shell
apt-get install snmpd
```

## Configuring the snmpd.conf file

In general, the snmpd.conf file is located in `/etc/snmp/`. Make a *backup* of the original file:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.old
```

Edit the new file (example with `vim`: `vim /etc/snmp/snmpd.conf`) according to the lines below:

```bash
rocommunity public  
sysLocation “Localização deste servidor”  
sysContact seu@email.com.br
```

## Restart and enable the SNMP service

### Systems with Systemd

On the terminal, type:

```shell
systemctl restart snmpd
systemctl enable snmpd
```

### Systems with Systemv

On the terminal, type:

```shell
service snmpd restart
```

## Allow the SNMP service in the Linux firewall

If the Linux server or workstation you want to monitor has a *firewall* enabled, to access the SNMP service add the example below to this device's *firewall* rules. If your distribution manages the *firewall* differently, open the incoming UDP/161 port.

```shell
firewall-cmd --permanent --zone=public --add-port=161/udp
systemctl restart firewalld
```

:::danger[Attention]
This firewall rule will allow SNMP queries from any IP address. Consult your network administrator to restrict access only to the necessary hosts.
:::