---
title: Gestión de Firewall - FirewallD
sidebar:
  order: 3
---
El **FirewallD** es una herramienta de gestión de firewall estándar para sistemas operativos Linux en distribuciones como Fedora, Red Hat y CentoOS. Actúa como un *front-end* para el *framework* de filtrado de paquetes del kernel Linux, conocido como **netfilter**.

## FirewallD - Concepto

Este firewall posee algunas reglas por defecto y trabaja con el concepto de zonas donde la liberación de servicios se realiza dentro de ellas.

La tabla a continuación demuestra cómo está configurado el firewall de la red después de la instalación del sistema operativo:




| Regra | Comportamento |
| ------- | ------------------------------------------------------- |
| INPUT | Liberado el acceso a conexiones del tipo RELATED,ESTABLISHED. |
| FORWARD | Acepta solo conexiones del tipo RELATED,ESTABLISHED. |
| OUTPUT | No posee restricciones. |


## Zonas

El firewalld gestiona un grupo de reglas conocido como zonas. Las zonas definen el tipo de tráfico que será permitido basado en el nivel de confianza de la red a la que está conectado su servidor. Cada zona está vinculada a una interfaz de red existente en el servidor.

El comando abajo lista las zonas existentes:

```bash
firewall-cmd --get-zones
```

A continuación se muestran las zonas existentes en firewalld en orden de nivel de confianza:




| Zona | Descripción |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `drop` | Todos los paquetes son descartados. |
| `block` | Todos los paquetes son rechazados. |
| `public` | Red que no conoces, pública. |
| `external` | Red externa donde el servidor con el firewalld funciona como un |
| `gateway` | para la red interna. Está configurada con enmascaramiento para mantener la privacidad de la red interna. |
| `internal` | Es la parte interna de la red. Equipos en esta red poseen un nivel mayor de confianza y servicios adicionales están disponibles. |
| `dmz` | Son equipos aislados, es decir, que no deben poseer acceso a su red. Solo algunas conexiones entrantes para estos equipos son permitidas. |
| `work` | Equipos de trabajo con liberación de servicios adicionales. |
| `home` | Equipos domésticos. Son dispositivos más conocidos y |
| confiables y que poseen liberación para un poco más de servicios que la zona work. |  |
| `trusted` | Equipos de confianza. Prácticamente todos los servicios están disponibles para los equipos en esta zona. |


## Listar las reglas existentes

El comando abajo lista todas las reglas existentes en el servicio firewalld:

```bash
firewall-cmd --list-all
```

Si desea listar solo las reglas de una determinada zona utilice la opción –zone:

```bash
firewall-cmd --zone=public --list-all
```

## Abrir puertos de entrada

Para modificar las reglas de entrada del firewall de Fedora, utilizamos el comando firewall-cmd.

En el ejemplo abajo se demuestra cómo abrir los puertos 80(TCP) y 443(TCP) para acceso desde la red pública, de forma permanente, para un servidor HTTP a través de la línea de comandos:

```bash
firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --permanent --zone=public --add-port=443/tcp
firewall-cmd --set-default-zone=public
firewall-cmd --reload
```

donde:


| Parâmetro | Descrição |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--permanent` | Añade la regla de forma permanente, es decir, después de reiniciar el filtro las reglas permanecerán. Si se omite esta opción las reglas son válidas hasta que el firewalld sea reiniciado. |
| `--zone=public` | Es la zona pública no confiable. Son direcciones que no conoces pero que pueden ser autorizadas caso por caso. |
| `--add-port=80/tcp` | Información del puerto y protocolo que serán añadidos en la zona public. |
| `--reload` | Recarga las reglas manteniendo el estado de las conexiones. |
| `--set-default-zone=public` | Define la zona public como la predeterminada a utilizar. |


El ejemplo abajo demuestra cómo liberar el puerto SSH para el servidor Linux:

```bash
firewall-cmd --permanent --zone=public --add-port=22/tcp
firewall-cmd --set-default-zone=public
firewall-cmd --reload
```

## Permitir un host o una red

A continuación se demuestra cómo permitir el acceso total al servidor para la red cuya origen es 192.168.1.0/24:

```bash
firewall-cmd --permanent --zone=public --add-source=127.0.0.1/8
firewall-cmd --reload
```


| Parâmetro | Descrição |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--permanent` | Añade la regla de forma permanente, es decir, después de reiniciar el filtro las reglas permanecerán. Si se omite esta opción las reglas son válidas hasta que el firewalld sea reiniciado. |
| `--zone=public` | Es la zona pública no confiable. Son direcciones que no conoces pero que pueden ser autorizadas caso por caso. |
| `--add-source=192.168.1.0/24` | Información de la red o host que serán añadidos en la zona public. |
| `--reload` | Recarga las reglas manteniendo el estado de las conexiones. |


## Configurando el firewalld para actuar como NAT

Para esta función es necesario tener al menos 2 interfaces de red en el servidor, una que haga la conexión con la red pública y otra la red interna.

En el ejemplo abajo, la interfaz eth0 está conectada en la red pública y la eth1 en la red interna:

```bash
firewall-cmd --permanent --zone=internal --add-interface=eth1
firewall-cmd --permanent --zone=public --add-masquerade
firewall-cmd --reload
```


| Parâmetro | Descrição |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| `--permanent` | Añade la regla de forma permanente, es decir, después de reiniciar el filtro las reglas permanecerán. Si se |
| omitida esta opção as regras são válidas até o firewalld ser reiniciado. |  |
| `--zone=public` `--zone=internal` | Seleccionamos la zona public para hacer el enmascaramiento y la internal para informar la red interna. |
| `--add-masquerade` | Añade el enmascaramiento en la zona seleccionada. |
| `--reload` | Recarga las reglas manteniendo el estado de las conexiones. |


## Configurando el firewalld para Redirección de puertos

Para redirigir puertos de la red externa a una dirección de la red interna, utilice los comandos abajo:

```bash
firewall-cmd --permanent --zone=public --add-forward-port=port=443:proto=tcp:toport=443:toaddr=192.168.1.11
firewall-cmd --reload
```


| Parâmetro | Descrição |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--permanent` | Añade la regla de forma permanente, es decir, después de reiniciar el filtro las reglas permanecerán. Si se omite esta opción las reglas son válidas hasta que el firewalld sea reiniciado. |
| `--zone=public` | Es la zona pública no confiable. Son direcciones que no conoces pero que pueden ser autorizadas caso por caso. |
| `--add-forward-port=` | Activa la regla para el port forward. |
| `port=443` | Puerto de origen. |
| `proto=tcp` | Protocolo de origen. |
| `toport=443` | Puerto de destino. |
| `toaddr=192.168.1.11` | IP de destino en la red interna. |
| `--reload` | Recarga las reglas manteniendo el estado de las conexiones. |