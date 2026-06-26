---
title: "Firewall Management - FirewallD"
sidebar:
  order: 3
---

The **FirewallD** is the standard firewall management tool for Linux operating systems in distributions such as Fedora, Red Hat and CentoOS. It acts as a *front-end* for the Linux kernel packet filtering *framework*, known as **netfilter**.

## FirewallD - Concept

This firewall has some default rules and works with the concept of zones where the allowance of services is done within them.

The table below shows how the network firewall is configured after the operating system installation:



| Regra | Comportamento |
| --- | --- |
| INPUT | Liberado o acesso conexões do tipo RELATED,ESTABLISHED. |
| FORWARD | Aceita apenas conexões do tipo RELATED,ESTABLISHED. |
| OUTPUT | Não possui restrições. |



## Zones

firewalld manages a set of rules known as zones. Zones define the type of traffic that will be allowed based on the trust level of the network to which your server is connected. Each zone is attached to an existing network interface on the server.

The command below lists the existing zones:

```shell
firewall-cmd --get-zones
```

Below are the zones available in firewalld shown in order of trust level:



| Zona | Descrição |
| --- | --- |
| `drop` | Todos os pacotes são descartados. |
| `block` | Todos os pacotes são rejeitados. |
| `public` | Rede que você não conhece, pública. |
| `external` | Rede externa onde o servidor com o firewalld funciona como um |
| `gateway` | para a rede interna. É configurada com mascaramento para manter a privacidade da rede interna. |
| `internal` | É a parte interna da rede. Equipamentos nessa rede possuem um nível maior de confiança e serviços adicionais estão disponíveis. |
| `dmz` | São equipamentos isolados, ou seja, que não devem possuir acesso a sua rede. Apenas algumas conexões de entrada para esses equipamentos são permitidas. |
| `work` | Equipamentos de trabalho com liberação de serviços adicionais. |
| `home` | Equipamentos de casa. São dispositivos mais conhecidos e  
confiáveis e que possuem liberação para um pouco mais de serviços que a zona work. |
| `trusted` | Equipamentos de confiança. Praticamente todos os serviços estão disponíveis para os equipamentos nesta zona. |



## List existing rules

The command below lists all existing rules in the firewalld service:

```shell
firewall-cmd --list-all
```

If you want to list only the rules of a specific zone use the –zone option:

```shell
firewall-cmd –zone=public --list-all
```

## Open incoming ports

To modify the firewall incoming rules on Fedora, we use the firewall-cmd command.

The example below shows how to open ports 80(TCP) and 443(TCP) for access from the public network, permanently, for an HTTP server via the command line:

```shell
firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --permanent --zone=public --add-port=443/tcp
firewall-cmd --set-default-zone=public
firewall-cmd --reload
```

where:

| Parâmetro | Descrição |
| --- | --- |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If this option is omitted the rules are valid until firewalld is restarted. |
| `--zone=public` | It is the untrusted public zone. These are addresses you do not know but may be authorized case by case. |
| `--add-port=80/tcp` | Information of the port and protocol that will be added to the public zone. |
| `--reload` | Reloads the rules keeping the connection states. |
| `--set-default-zone=public` | Sets the public zone as the default to be used. |



The example below shows how to open the SSH port for the Linux server:

```shell
firewall-cmd --permanent --zone=public --add-port=22/tcp
firewall-cmd --set-default-zone=public
firewall-cmd --reload
```

## Allowing a host or a network

Below is shown how to allow full access to the server for the network whose source is 192.168.1.0/24:

```shell
firewall-cmd --permanent --zone=public --add-source=127.0.0.1/8
firewall-cmd --reload
```


| Parâmetro | Descrição |
| --- | --- |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If this option is omitted the rules are valid until firewalld is restarted. |
| `--zone=public` | It is the untrusted public zone. These are addresses you do not know but may be authorized case by case. |
| `--add-source=192.168.1.0/24` | Information of the network or host that will be added to the public zone. |
| `--reload` | Reloads the rules keeping the connection states. |



## Configuring firewalld to act as NAT

For this function it is necessary to have at least 2 network interfaces on the server, one that connects to the public network and another to the internal network.

In the example below, interface eth0 is connected to the public network and eth1 to the internal network:

```shell
firewall-cmd --permanent –zone=internal –add-interface=eth1
firewall-cmd –permanent –zone=public -add-masquerade
firewall-cmd --reload
```

| Parâmetro | Descrição |
| --- | --- |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If this option is  
omitted this option the rules are valid until firewalld is restarted. |
| `--zone=public`<br />`--zone=internal` | We select the public zone to perform masquerading and the internal to indicate the internal network. |
| `--add-masquerade` | Adds masquerading to the selected zone. |
| `--reload` | Reloads the rules keeping the connection states. |



## Configuring firewalld for Port Forward

To forward ports from the external network to an address on the internal network, use the commands below:

```shell
firewall-cmd --permanent --zone=public –add-forward-port=port=443:proto=tcp:toport=443:toaddr=192.168.1.11
firewall-cmd --reload
```


| Parâmetro | Descrição |
| --- | --- |
| `--permanent` | Adds the rule permanently, that is, after restarting the filter the rules will remain. If this option is omitted the rules are valid until firewalld is restarted. |
| `--zone=public` | It is the untrusted public zone. These are addresses you do not know but may be authorized case by case. |
| `--add-forward-port=` | Enables the rule for port forward. |
| `port=443` | Source port. |
| `proto=tcp` | Source protocol. |
| `toport=443` | Destination port. |
| `toaddr=192.168.1.11` | Destination IP on the internal network. |
| `--reload` | Reloads the rules keeping the connection states. |