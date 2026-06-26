---
title: "Configurando el SNMP en Quagga"
---

Tutorial con el objetivo de activar una configuración básica de los servicios SNMP en el sistema Quagga.

## Instalar y configurar SNMP en Linux

Consulte nuestro tutorial [Configurando el SNMP no Linux](/es/extra/linux/snmp-linux).

## Quagga

### Configurar el SNMP

:::caution[Importante]
Para que Quagga proporcione información por snmp, el software debe haber sido compilado con la opción `–with-mib-modules=agentx`. Para más información, consulte la documentación de Quagga en [http://www.nongnu.org/quagga/](http://www.nongnu.org/quagga/).
:::


Conectado como root, edite el archivo `/etc/quagga/bgpd.conf` y añada el siguiente comando al final del archivo:

`agentx`

## Reiniciar los servicios zebra y bgpd

### Sistemas systemd

Para reiniciar los servicios en sistemas systemd, utilice los siguientes comandos:

```shell
systemctl restart zebra
systemctl enable bgpd
```

### Sistemas systemv

Para reiniciar los serviços em sistema systemd, utilize os comandos abaixo:

```shell
service zebra restart
service bgpd restart
```

## Monitorizar Quagga con Monsta

En Monsta, utilice las plantillas “BGP – BGP4” y “Linux” para monitorizar el BGP y los recursos del servidor Quagga.