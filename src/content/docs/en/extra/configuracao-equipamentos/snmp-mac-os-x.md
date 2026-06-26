---
title: "Configuring SNMP on Mac OS X"
---

Tutorial aimed at enabling a basic SNMP service configuration on a Mac OS X.

## Configuring the SNMP service

Open a terminal session and run the command below:

```shell
sudo -i
```

Enter the root password.

Run the commands below to create a basic snmp configuration file:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.original
echo “rocommunity public” > /etc/snmp/snmpd.conf
```

Run the following command to start the snmp service:

```shell
launchctl load -w /System/Library/LaunchDaemons/org.net-snmp.snmpd.plist
```

From now on SNMP is available on your Mac OS X machine and can be monitored by Monsta using versions 1 and 2c with the community public. The template for this device is the “Apple – Mac OS X”.