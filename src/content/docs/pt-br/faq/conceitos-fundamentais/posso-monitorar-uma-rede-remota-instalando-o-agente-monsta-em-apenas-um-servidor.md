---
title: "Posso monitorar uma rede remota instalando o Agente Monsta em apenas um servidor?"
---

**Sim, é possível.**

O **Agente Monsta** foi projetado para atuar como um *gateway de monitoramento*. Você precisa instalar apenas **um agente** em um equipamento (servidor, VM) dentro da rede remota (filial, escritório, etc).

- **Coleta Centralizada**: O agente fará a coleta de dados (via [SNMP](/pt-br/tech/protocolos-coleta/snmp), ICMP, [WMI](/pt-br/tech/protocolos-coleta/wmi), API, etc.) de todos os outros dispositivos dentro daquela rede local (roteadores, switches, servidores, impressoras, etc).
- **Comunicação Única**: Em seguida, ele utiliza o **túnel [QUIC](/pt-br/tech/arquitetura-comunicacao/protocolo-quic) seguro** para enviar de forma agregada e eficiente todas essas métricas de volta para o Servidor Monsta.

Essa arquitetura elimina a necessidade de instalar vários agentes ou de abrir portas e regras de firewall para cada dispositivo na rede remota. É um modelo **"um agente, muitos dispositivos"**.