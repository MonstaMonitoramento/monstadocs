---
title: "¿Cómo Resolver la Inestabilidad en las Recopilaciones por Pérdida de Paquetes?"
---

Este artículo muestra cómo resolver el problema de pérdida intermitente de conexión o de paquetes que ocurre cuando la tabla de seguimiento de conexiones (*conntrack*) del kernel Linux está llena.

## 1. Problema y Causas

Linux usa `nf_conntrack` (*Network Filter Connection Tracking*) para rastrear todas las conexiones de red activas (TCP, UDP, ICMP, etc.), necesario para el correcto funcionamiento del *firewall* (*iptables/nftables*) y del NAT (*Network Address Translation*).

Cuando el número de conexiones activas alcanza el límite máximo configurado, el kernel no puede rastrear nuevas conexiones y, por defecto, las descarta. Esto se manifiesta como:

- Pérdida de conexión y paquetes en Linux.
- Fallo intermitente para establecer nuevas conexiones.
- Mensajes de error en el registro del sistema (`/var/log/messages` o `dmesg`), como:
    - `kernel: nf_conntrack: table full, dropping packet`
    - `nf_conntrack: table full`

![Captura de pantalla 2025-11-14 161942.png](../../../../../assets/images/p123_captura-de-tela-2025-11-14-161942.png)

Este problema influye en el monitoreo de Monsta, causando fallos de recopilación en monitores de forma aleatoria, ya que Monsta envía la solicitud y no recibe una respuesta.

Motivos que pueden causar el agotamiento de la tabla:

1. **Alto Tráfico de Conexiones de Corta Duración**: Servidores que manejan muchas conexiones que se abren y cierran rápidamente pueden llenar la tabla con rapidez. Una gran cantidad de monitores en Monsta puede contribuir.
2. **Ataques de Denegación de Servicio (DDoS/DoS)**: Un ataque de inundación de paquetes, especialmente *SYN floods* (que intentan abrir muchas conexiones TCP incompletas), o grandes volúmenes de tráfico UDP (que usa *conntrack* para rastreo básico) pueden agotar la tabla inmediatamente.
3. **Timeouts Demasiado Largos**: Si el tiempo que el kernel tarda en "olvidar" una conexión inactiva (*timeout*) es muy largo, las entradas quedan atascadas en la tabla, incluso si la conexión se ha cerrado. Esto es especialmente problemático para conexiones TCP en el estado `TIME_WAIT` (el *timeout* predeterminado de 60 segundos suele ser demasiado largo para entornos de alto tráfico).

## Cómo confirmar el problema

Puede verificar el estado de la tabla con los siguientes comandos:

```shell
# Límite máximo de conexiones (nf_conntrack_max)
cat /proc/sys/net/netfilter/nf_conntrack_max

# Número actual de conexiones activas (nf_conntrack_count)
cat /proc/sys/net/netfilter/nf_conntrack_count
```

Si el `nf_conntrack_count` está muy cerca o es igual a `nf_conntrack_max`, la tabla está llena.

## 2. Solución: Aumentar y Optimizar los Límites

La solución es aumentar el límite máximo de conexiones (`nf_conntrack_max`) y optimizar los parámetros de rendimiento de la tabla. Para cambiarlo de forma permanente (sin perder las configuraciones al reiniciar Linux), siga los pasos:

#### 2.1 Edite el archivo de configuración del sistema `/etc/sysctl.conf` con un editor de texto (`vi`, `nano`...)

```shell
vi /etc/sysctl.conf
```

#### 2.2 Añada las siguientes líneas al final del archivo

```shell
######################################################
# Optimización de Conntrack para alto tráfico
######################################################
net.netfilter.nf_conntrack_max = 262144
net.netfilter.nf_conntrack_buckets = 65536
net.netfilter.nf_conntrack_tcp_timeout_time_wait = 30
```

#### 2.3 Guarde y cierre el archivo

#### 2.4 Aplique las nuevas configuraciones sin necesidad de reiniciar el sistema

```shell
sysctl -p
```

## 3. Verificación

Después de aplicar los cambios, verifique el nuevo límite.

```shell
cat /proc/sys/net/netfilter/nf_conntrack_max
# El resultado debe ser 262144
```