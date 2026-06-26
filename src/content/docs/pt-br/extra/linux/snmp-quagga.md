---
title: "Configurando o SNMP no Quagga"
---

Tutorial com objetivo de ativar uma configuração básica dos serviços SNMP no sistema Quagga.

## Instalar e configurar o SNMP no Linux

Consulte nosso tutorial [Configurando o SNMP no Linux](/pt-br/extra/linux/snmp-linux).

## Quagga

### Configurar o SNMP

:::caution[Importante]
Para o Quagga fornecer informações por snmp, o software deve ter sido compilado com a opção `–with-mib-modules=agentx`. Para maiores informações, consulte a documentação do Quagga em [http://www.nongnu.org/quagga/](http://www.nongnu.org/quagga/).
:::


Logado como root, edite o arquivo `/etc/quagga/bgpd.conf` e adicione o seguinte comando ao final do arquivo:

`agentx`

## Reiniciar os serviços zebra e bgpd

### Sistemas systemd

Para reiniciar os serviços em sistema systemd, utilize os comandos abaixo:

```shell
systemctl restart zebra
systemctl enable bgpd
```

### Sistemas systemv

Para reiniciar os serviços em sistema systemd, utilize os comandos abaixo:

```shell
service zebra restart
service bgpd restart
```

## Monitorar o Quagga pelo Monsta

No Monsta, utilize os templates “BGP – BGP4” e “Linux” para monitorar o BGP e os recursos do servidor do Quagga.
