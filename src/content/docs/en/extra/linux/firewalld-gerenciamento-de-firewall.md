---
title: Firewall Management - FirewallD
sidebar:
  order: 3
---
The **FirewallD** is a default firewall management tool for Linux operating systems in distributions such as Fedora, Red Hat and CentOS. It acts as a front-end for the Linux kernel packet filtering framework, known as **netfilter**.

## FirewallD - Concept

This firewall has some default rules and works with the concept of zones where the allowance of services is done within them.

The table below shows how the network firewall is configured after operating system installation:




| Regra | Comportamento |
| ------- | ------------------------------------------------------- |
| INPUT | Liberado o acesso conexões do tipo RELATED,ESTABLISHED. |
| FORWARD | Aceita apenas conexões do tipo RELATED,ESTABLISHED. |
| OUTPUT | Não possui restrições. |


## Zones

firewalld manages a set of rules known as zones. Zones define the type of traffic that will be allowed based on the trust level of the network to which your server is connected. Each zone is tied to an existing network interface on the server.

The command below lists the existing zones:

```bash
firewall-cmd --get-zones
```

Below are the zones available in firewalld in order of trust level:




| Zona | Descrição |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `drop` | All packets are discarded. |
| `block` | All packets are rejected. |
| `public` | A network you do not know, public. |
| `external` | External network where the server running firewalld acts as a |
| `gateway` | for the internal network. It is configured with masquerading to preserve the internal network's privacy. |
| `internal` | It is the internal part of the network. Devices on this network have a higher level of trust and additional services are available. |
| `dmz` | Devices that are isolated, that is, that should not have access to your network. Only some incoming connections to these devices are allowed. |
| `work` | Work devices with additional services allowed. |
| `home` | Home devices. These are more known devices and |
| trusted and that have permission to a few more services than the work zone. |  |
| `trusted` | Trusted devices. Practically all services are available to devices in this zone. |


## List existing rules

The command below lists all existing rules in the firewalld service:

```bash
firewall-cmd --list-all
```

If you want to list only the rules of a specific zone use the --zone option:

```bash
firewall-cmd --zone=public --list-all
```

## Open incoming ports

To modify the firewall input rules on Fedora, we use the firewall-cmd command.

The example below demonstrates how to open ports 80(TCP) and 443(TCP) for access from the public network, permanently, for an HTTP server via the command line:

```bash
firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --permanent --zone=public --add-port=443/tcp
firewall-cmd --set-default-zone=public
firewall-cmd --reload
```

where:


| Parâmetro | Descrição |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If this option is omitted the rules are valid until firewalld is restarted. |
| `--zone=public` | It is the untrusted public zone. These are addresses you do not know but may be authorized on a case-by-case basis. |
| `--add-port=80/tcp` | Information about the port and protocol that will be added to the public zone. |
| `--reload` | Reloads the rules preserving the state of connections. |
| `--set-default-zone=public` | Sets the public zone as the default to be used. |


The example below demonstrates how to open the SSH port for the Linux server:

```bash
firewall-cmd --permanent --zone=public --add-port=22/tcp
firewall-cmd --set-default-zone=public
firewall-cmd --reload
```

## Allowing a host or a network

Below is shown how to allow full access to the server for the network whose origin is 192.168.1.0/24:

```bash
firewall-cmd --permanent --zone=public --add-source=127.0.0.1/8
firewall-cmd --reload
```


| Parâmetro | Descrição |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If this option is omitted the rules are valid until firewalld is restarted. |
| `--zone=public` | It is the untrusted public zone. These are addresses you do not know but may be authorized on a case-by-case basis. |
| `--add-source=192.168.1.0/24` | Information about the network or host that will be added to the public zone. |
| `--reload` | Reloads the rules preserving the state of connections. |


## Configuring firewalld to act as NAT

For this function it is necessary to have at least 2 network interfaces on the server, one that connects to the public network and another to the internal network.

In the example below, the eth0 interface is connected to the public network and eth1 to the internal network:

```bash
firewall-cmd --permanent --zone=internal --add-interface=eth1
firewall-cmd --permanent --zone=public --add-masquerade
firewall-cmd --reload
```


| Parâmetro | Descrição |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If |
| the option is omitted the rules are valid until firewalld is restarted. |  |
| `--zone=public` `--zone=internal` | We select the public zone to apply masquerading and the internal to indicate the internal network. |
| `--add-masquerade` | Adds masquerading in the selected zone. |
| `--reload` | Reloads the rules preserving the state of connections. |


## Configuring firewalld for Port Forward

To forward ports from the external network to an address on the internal network, use the commands below:

```bash
firewall-cmd --permanent --zone=public --add-forward-port=port=443:proto=tcp:toport=443:toaddr=192.168.1.11
firewall-cmd --reload
```


| Parâmetro | Descrição |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If this option is omitted the rules are valid until firewalld is restarted. |
| `--zone=public` | It is the untrusted public zone. These are addresses you do not know but may be authorized on a case-by-case basis. |
| `--add-forward-port=` | Enables the rule for port forwarding. |
| `port=443` | Source port. |
| `proto=tcp` | Source protocol. |
| `toport=443` | Destination port. |
| `toaddr=192.168.1.11` | Destination IP on the internal network. |
| `--reload` | Reloads the rules preserving the state of connections. |