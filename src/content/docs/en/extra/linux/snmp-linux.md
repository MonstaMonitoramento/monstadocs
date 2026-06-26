---
title: "Configuring SNMP on Linux"
sidebar:
  order: 1
---

Tutorial aimed at enabling a basic configuration of SNMP services on Linux operating systems.



:::note
There are many Linux distributions, each with its own particularities. The following information may not work on your distribution.
:::

## Installation

### Systems using yum

While logged in as root, in the Linux terminal type:

```shell
yum install net-snmp
```

### Systems using apt-get

While logged in as root, in the Linux terminal type:

```shell
apt-get install snmpd
```

## Configuring the snmpd.conf file

Generally, the snmpd.conf file is located at `/etc/snmp/`. Back up the original file:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.old
```

Edit the new file (example with `vim`: `vim /etc/snmp/snmpd.conf`) as the lines below:

```bash
rocommunity public  
sysLocation “Localização deste servidor”  
sysContact seu@email.com.br
```

## Restart and enable the SNMP service
### Systems with Systemd

In the terminal, type:

```shell
systemctl restart snmpd
systemctl enable snmpd
```

### Systems with System V

In the terminal, type:

```shell
service snmpd restart
```

## Allow the SNMP service through the Linux firewall

If the Linux server or workstation you want to monitor has a *firewall* enabled, to access the SNMP service add the example below to the *firewall* rules of that device. If your distribution manages the *firewall* differently, open the incoming UDP/161 port.

```shell
firewall-cmd --permanent --zone=public --add-port=161/udp
systemctl restart firewalld
```

:::danger[Attention]
This firewall allowance will permit SNMP queries from any IP address. Consult your network administrator to restrict access only to the necessary hosts.
:::