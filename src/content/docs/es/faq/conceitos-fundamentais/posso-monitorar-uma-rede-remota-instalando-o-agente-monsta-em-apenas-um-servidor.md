---
title: "¿Puedo monitorizar una red remota instalando el Agente Monsta en un solo servidor?"
---

**Sí, es posible.**

El **Agente Monsta** fue diseñado para actuar como un *gateway de monitorización*. Necesitas instalar solo **un agente** en un equipo (servidor, VM) dentro de la red remota (sucursal, oficina, etc).

- **Recopilación centralizada**: El agente realizará la recopilación de datos (a través de [SNMP](/es/tech/protocolos-coleta/snmp), ICMP, [WMI](/es/tech/protocolos-coleta/wmi), API, etc.) de todos los demás dispositivos dentro de esa red local (enrutadores, switches, servidores, impresoras, etc).
- **Comunicación única**: A continuación, utiliza el **túnel [QUIC](/es/tech/arquitetura-comunicacao/protocolo-quic) seguro** para enviar de forma agregada y eficiente todas esas métricas de vuelta al Servidor Monsta.

Esta arquitectura elimina la necesidad de instalar varios agentes o de abrir puertos y reglas de firewall para cada dispositivo en la red remota. Es un modelo **"un agente, muchos dispositivos"**.