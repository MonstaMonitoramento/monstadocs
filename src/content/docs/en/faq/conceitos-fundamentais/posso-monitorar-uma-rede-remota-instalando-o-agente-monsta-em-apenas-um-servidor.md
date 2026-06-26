---
title: "Can I monitor a remote network by installing the Monsta Agent on just one server?"
---

**Yes, it is possible.**

The **Monsta Agent** is designed to act as a *monitoring gateway*. You only need to install **one agent** on a device (server, VM) inside the remote network (branch office, office, etc.).

- **Centralized Collection**: The agent will collect data (via [SNMP](/en/tech/protocolos-coleta/snmp), ICMP, [WMI](/en/tech/protocolos-coleta/wmi), API, etc.) from all the other devices within that local network (routers, switches, servers, printers, etc).
- **Single Communication**: It then uses the **secure [QUIC](/en/tech/arquitetura-comunicacao/protocolo-quic) tunnel** to efficiently send all these aggregated metrics back to the Monsta Server.

This architecture eliminates the need to install multiple agents or to open firewall ports and rules for each device on the remote network. It is a **"one agent, many devices"** model.