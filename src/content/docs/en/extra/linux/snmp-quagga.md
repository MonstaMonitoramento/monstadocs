---
title: "Configuring SNMP on Quagga"
---

Tutorial aimed at enabling a basic configuration of SNMP services on the Quagga system.

## Install and configure SNMP on Linux

See our tutorial [Configuring SNMP on Linux](/en/extra/linux/snmp-linux).

## Quagga

### Configure SNMP

:::caution[Important]
For Quagga to provide information via SNMP, the software must have been compiled with the option `–with-mib-modules=agentx`. For more information, see the Quagga documentation at [http://www.nongnu.org/quagga/](http://www.nongnu.org/quagga/).
:::

Logged in as root, edit the file `/etc/quagga/bgpd.conf` and add the following command at the end of the file:

`agentx`

## Restart the zebra and bgpd services

### systemd systems

To restart the services on a systemd system, use the commands below:

```shell
systemctl restart zebra
systemctl enable bgpd
```

### systemv systems

To restart the services on a systemd system, use the commands below:

```shell
service zebra restart
service bgpd restart
```

## Monitor Quagga with Monsta

In Monsta, use the “BGP – BGP4” and “Linux” templates to monitor BGP and the Quagga server resources.