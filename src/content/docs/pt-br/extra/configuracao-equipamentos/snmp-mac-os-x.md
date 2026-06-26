---
title: "Configurando o SNMP no Mac OS X"
---

Tutorial com objetivo de ativar uma configuração básica dos serviços SNMP em um Mac OS X.

## Configurando o serviço SNMP

Abra uma sessão de terminal e execute o comando abaixo:

```shell
sudo -i
```

Entre com a senha de root.

Execute os comandos abaixo para criar um arquivo de configuração básica do snmp:

```shell
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.original
echo “rocommunity public” > /etc/snmp/snmpd.conf
```

Execute o seguinte comando para iniciar o serviço de snmp:

```shell
launchctl load -w /System/Library/LaunchDaemons/org.net-snmp.snmpd.plist
```

A partir de agora o SNMP está disponível em seu equipamento com Mac OS X e já pode ser monitorado pelo Monsta através das versões 1 e 2c com a comunidade public. O template para esse dispositivo é o “Apple – Mac OS X”.
