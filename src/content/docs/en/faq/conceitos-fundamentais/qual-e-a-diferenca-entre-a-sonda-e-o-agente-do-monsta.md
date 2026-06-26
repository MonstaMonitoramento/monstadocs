---
title: "What is the difference between the Monsta Probe and Agent?"
---

This article aims to briefly explain the difference between Monsta's [Probe](/en/start/instalacao/sonda-windows) and [Agent](/en/start/instalacao/agente-instalacao-zero-conf).

## Differences

The main difference between the Probe and the Agent is their purpose:

- The Monsta Probe was created to monitor Windows machines via WMI. Once installed on a computer, Monsta can obtain Windows WMI information through the Probe.
- The Monsta Agent was created to monitor devices on remote networks that are inaccessible to Monsta. With the Agent installed on a device in the remote network, Monsta can communicate with it to obtain information about the network's devices without the need for port forwarding or VPN.

## Comparison table: Agent vs. Probe

| Feature | **Agent** | **Probe** |
| --- | --- | --- |
| **Behavior** | **Active** — initiates the outgoing connection to the Monsta server | **Passive** — waits for requests from the Monsta server |
| **Supported systems** | Windows, Linux and Raspberry Pi | Windows only |
| **Use of VPN / Port Forwarding** | Not required | Required (Monsta needs to reach the probe) |
| **Communication protocol** | QUIC (encrypted, end-to-end) | WMI (Microsoft API) |
| **Environments with NAT / dynamic IP** | Natively supported | May be limited |
| **Offline data cache** | Yes — stores metrics locally if the connection is lost | No |
| **Ideal for** | Remote networks, branch offices, distributed environments without VPN | Local monitoring of Windows servers/workstations |
| **Cost** | Paid | Free |



## Summary

The Probe is a simpler tool focused on collecting metrics from Windows machines (CPU, RAM, disk, network) and responds when the Monsta server queries it. The Agent is a more robust, cross-platform solution, ideal for expanding monitoring to remote networks — it initiates communication with the server itself, removing the need for VPN, port forwarding, or a fixed IP.

![image-1773943312944.png](../../../../../assets/images/p174_image-1773943312944.png)

## More information

Other articles related to Agents and the Probe:

- 📄[Agents](/en/manual/configuracoes/agentes)
- 📄[Agent: Zero-Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf)
- 📄[Can I monitor a remote network by installing the Monsta Agent on just one server?](/en/faq/conceitos-fundamentais/posso-monitorar-uma-rede-remota-instalando-o-agente-monsta-em-apenas-um-servidor)
- 📄[The Agent's Communication Architecture](/en/tech/arquitetura-comunicacao/a-arquitetura-de-comunicacao-do-agente)
- 📄[Does Monsta need an agent installed on every machine?](/en/faq/conceitos-fundamentais/o-monsta-precisa-de-agente-instalado-em-cada-maquina)
- 📄[QUIC Protocol - The Future of Communications on the Internet](/en/tech/arquitetura-comunicacao/protocolo-quic)
- 📄[What is Monsta's Probe used for?](/en/faq/conceitos-fundamentais/para-que-serve-a-sonda-do-monsta)
- 📄[Probe: Windows Monitoring](/en/start/instalacao/sonda-windows)
- 📄[WMI (Windows Management Instrumentation)](/en/tech/protocolos-coleta/wmi)