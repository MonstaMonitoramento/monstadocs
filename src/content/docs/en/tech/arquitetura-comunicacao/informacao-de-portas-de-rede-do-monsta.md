---
title: "Monsta Network Ports"
sidebar:
  order: 1
---

The **Monsta** was designed to operate with a minimal and specific set of network ports. For the purposes of configuring security on your firewall, it is important to know which ports are used and which can be blocked.

- - - - - -

## Network Ports Used

By default, Monsta requires access only to the following ports for its normal operation and communication:

| Porta | Protocolo | Descrição |
| --- | --- | --- |
| **80** | **TCP** (HTTP) | Used for **unencrypted** communication (HTTP). If Monsta is accessed without SSL/TLS, this port will be used. |
| **443** | **TCP** (HTTPS) | Used for **secure, encrypted** communication (HTTPS). This is the **preferred** port for secure access. |

Additionally, Monsta may perform **internal accesses** that originate from and are destined to the `localhost` (the server where Monsta is installed). Such internal communications are generally **not affected** by firewall rules that govern external network inbound/outbound traffic.

## Security Recommendation (Firewall)

To maximize the security of the system where Monsta is hosted, we recommend the following firewall configuration:

- **Allow** inbound traffic on ports **80 (HTTP)** and **443 (HTTPS)**.
- **Allow** all access to and from `localhost` - 127.0.0.1 (IPv4) and ::1 (IPv6).
- **Block (Deny/Drop)** all **other unused ports**.

Blocking unused ports reduces the **likelihood of attacks** against the server, preventing exploitation attempts on services that are not necessary for Monsta's operation.