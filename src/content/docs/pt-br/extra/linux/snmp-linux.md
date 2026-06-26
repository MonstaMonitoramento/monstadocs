---
title: "Configurando o SNMP no Linux"
sidebar:
  order: 1
---

Tutorial com objetivo de ativar uma configuração básica dos serviços SNMP em Sistemas Operacionais Linux.



:::note
Existem diversas distribuições Linux, cada qual com suas particularidades. As informações a seguir podem não funcionar em sua distribuição.
:::

## Instalação

### Sistemas que utilizam yum

Logado como root, na tela de terminal do Linux digite:

```shell
yum install net-snmp
```

### Sistemas que utilizam apt-get

Logado como root, na tela de terminal do Linux digite:

```shell
apt-get install snmpd
```

## Configuração do arquivo snmpd.conf

Em geral, o arquivo snmpd.conf encontra-se em `/etc/snmp/`. Faça um *backup* do arquivo original:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.old
```

Edite o novo arquivo (exemplo com `vim`: `vim /etc/snmp/snmpd.conf`) conforme as linhas abaixo:

```bash
rocommunity public  
sysLocation “Localização deste servidor”  
sysContact seu@email.com.br
```

## Reiniciar e habilitar o serviço SNMP
### Sistemas com Systemd

Na tela de terminal, digite:

```shell
systemctl restart snmpd
systemctl enable snmpd
```

### Sistemas com Systemv

Na tela de terminal, digite:

```shell
service snmpd restart
```

## Liberar o serviço SNMP no firewall do Linux

Caso o servidor ou estação Linux que deseja monitorar possua um *firewall* habilitado, para acessar o serviço SNMP adicione o exemplo abaixo nas regras de *firewall* deste dispositivo. Caso sua distribuição gerencie o *firewall* de forma diferente, libere a porta de entrada UDP/161.

```shell
firewall-cmd --permanent --zone=public --add-port=161/udp
systemctl restart firewalld
```

:::danger[Atenção]
Essa liberação de *firewall* irá liberar a consulta snmp para qualquer endereço IP. Consulte seu administrador de rede para restringir os acessos apenas aos hosts necessários.
:::