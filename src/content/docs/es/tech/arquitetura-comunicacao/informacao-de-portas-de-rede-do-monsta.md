---
title: "Puertos de Red de Monsta"
sidebar:
  order: 1
---

El **Monsta** fue diseñado para operar con un conjunto mínimo y específico de puertos de red. Para la configuración de seguridad en su firewall, es importante saber qué puertos se utilizan y cuáles pueden bloquearse.

- - - - - -

## Puertos de Red Utilizados

Por defecto, el Monsta requiere acceso solo a los siguientes puertos para su funcionamiento normal y comunicación:

| Puerto | Protocolo | Descripción |
| --- | --- | --- |
| **80** | **TCP** (HTTP) | Usado para comunicación **no cifrada** (HTTP). Si el Monsta se accede sin SSL/TLS, este puerto será utilizado. |
| **443** | **TCP** (HTTPS) | Usado para comunicación **segura y cifrada** (HTTPS). Este es el puerto **preferente** para el acceso seguro. |

Además, el Monsta puede realizar **accesos internos** que se originan en y se destinan al `localhost` (el propio servidor donde el Monsta está instalado). Tales comunicaciones internas generalmente **no se ven afectadas** por las reglas del firewall que gobiernan el tráfico de entrada/salida de la red externa.

## Recomendación de Seguridad (Firewall)

Para maximizar la seguridad del sistema donde el Monsta está hospedado, recomendamos la siguiente configuración de firewall:

- **Permitir** el tráfico entrante (Inbound) en los puertos **80 (HTTP)** y **443 (HTTPS)**.
- **Permitir** todos los accesos desde y hacia el `localhost` - 127.0.0.1 (IPv4) y ::1 (IPv6).
- **Bloquear (Deny/Drop)** todos los **demás puertos** no utilizados.

Bloquear puertos no utilizados reduce la **probabilidad de ataques** al servidor, previniendo intentos de explotación en servicios que no son necesarios para la operación del Monsta.