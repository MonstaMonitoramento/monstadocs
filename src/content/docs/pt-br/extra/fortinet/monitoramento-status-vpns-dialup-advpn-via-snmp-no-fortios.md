---
title: Monitoramento de Status das VPNs Dialup (ADVPN) via SNMP no FortiOS
description: Entenda por que o monitor de status do Fortinet não exibe as VPNs do tipo Dialup (ADVPN) na tabela padrão (fgVpnTunTable) e consulte a estrutura da MIB fgVpn2DialupTable para monitoramento.
---

## Limitação do monitoramento de Status das VPNs Dialup (ADVPN)

**ADVPN é uma arquitetura Dialup/Dynamic**: O **ADVPN** utiliza túneis pai do tipo *Dialup* (nos Hubs e Spokes) e cria atalhos dinâmicos (*shortcuts*) sob demanda entre os Spokes. Para o **FortiOS**, conexões que negociam Fase 1 e Fase 2 dinamicamente não são classificadas como "túneis estáticos", e por isso são omitidas da `fgVpnTunTable`.

Os atalhos ADVPN nascem e fecham dinamicamente com base no fluxo de tráfego e nos cronômetros de ociosidade (*idle-timeout* / *holddown timer*). Como as SAs (*Security Associations*) de Fase 1 e Fase 2 desses atalhos são temporárias, a Fortinet não as mapeia na estrutura de MIB estática para evitar poluição de índices SNMP e inconsistências de varredura.

Por essa razão, **não é possível monitorar o status operacional tradicional (Up/Down)** dessas VPNs via SNMP, pois a Fortinet não disponibiliza uma OID de estado de conexão para túneis dinâmicos. Veja a seguir a MIB da tabela *Dialup* com as informações que ela fornece.

**MIB da tabela Dialup**

| | | |
| ------------------------ | --------------------------------- | ---------------------------------------------------------------------------------------- |
| `fgVpn2Tables` | `1.3.6.1.4.1.12356.101.12.4` | |
| `fgVpn2DialupTable` | `1.3.6.1.4.1.12356.101.12.4.1` | Dial-up VPN peers information |
| `fgVpn2DialupEntry` | `1.3.6.1.4.1.12356.101.12.4.1.1` | Dial-up VPN peer info |
| `fgVpn2DialupIndex` | `1.3.6.1.4.1.12356.101.12.4.1.1.1` | An index value that uniquely identifies an VPN dial-up peer within the `fgVpn2DialupTable` |
| `fgVpn2DialupGatewayType` | `1.3.6.1.4.1.12356.101.12.4.1.1.2` | Remote gateway address type of the tunnel |
| `fgVpn2DialupGateway` | `1.3.6.1.4.1.12356.101.12.4.1.1.3` | Remote gateway address of the tunnel |
| `fgVpn2DialupLifetime` | `1.3.6.1.4.1.12356.101.12.4.1.1.4` | Tunnel life time (seconds) of the tunnel |
| `fgVpn2DialupTimeout` | `1.3.6.1.4.1.12356.101.12.4.1.1.5` | Time before the next key exchange (seconds) of the tunnel |
| `fgVpn2DialupSrcBeginType` | `1.3.6.1.4.1.12356.101.12.4.1.1.6` | Beginning's IP type of remote address range of the tunnel |
| `fgVpn2DialupSrcBegin` | `1.3.6.1.4.1.12356.101.12.4.1.1.7` | Beginning of remote address range of the tunnel |
| `fgVpn2DialupSrcEndType` | `1.3.6.1.4.1.12356.101.12.4.1.1.8` | End's IP type of remote address range of the tunnel |
| `fgVpn2DialupSrcEnd` | `1.3.6.1.4.1.12356.101.12.4.1.1.9` | End of remote address range of the tunnel |
| `fgVpn2DialupDstBeginType` | `1.3.6.1.4.1.12356.101.12.4.1.1.10` | Beginning's IP type of local address range of the tunnel |
| `fgVpn2DialupDstBegin` | `1.3.6.1.4.1.12356.101.12.4.1.1.11` | Beginning of local address range of the tunnel |
| `fgVpn2DialupDstEndType` | `1.3.6.1.4.1.12356.101.12.4.1.1.12` | End's IP type of local address range of the tunnel |
| `fgVpn2DialupDstEnd` | `1.3.6.1.4.1.12356.101.12.4.1.1.13` | End of local address range of the tunnel |
| `fgVpn2DialupInOctets` | `1.3.6.1.4.1.12356.101.12.4.1.1.14` | Number of bytes received on tunnel since instantiation. |
| `fgVpn2DialupOutOctets` | `1.3.6.1.4.1.12356.101.12.4.1.1.15` | Number of bytes sent on tunnel since instantiation. |
| `fgVpn2DialupPhase1Name` | `1.3.6.1.4.1.12356.101.12.4.1.1.16` | Descriptive name of phase1 configuration for the tunnel |
| `fgVpn2DialupVdom` | `1.3.6.1.4.1.12356.101.12.4.1.1.17` | Virtual domain tunnel is part of. This index corresponds to the index used by fgVdTable. |
