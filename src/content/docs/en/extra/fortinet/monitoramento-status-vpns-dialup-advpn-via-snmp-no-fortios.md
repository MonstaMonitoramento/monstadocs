---
title: Monitoring Status of Dial-up (ADVPN) VPNs via SNMP on FortiOS
description: Understand why Fortinet's status monitor does not display Dial-up (ADVPN) VPNs in the default table (fgVpnTunTable) and view the fgVpn2DialupTable MIB structure for monitoring.
---

## Limitation of monitoring status for Dial-up (ADVPN) VPNs

**ADVPN is a Dialup/Dynamic architecture**: **ADVPN** uses parent tunnels of the *Dialup* type (on Hubs and Spokes) and creates dynamic shortcuts on demand between Spokes. For **FortiOS**, connections that negotiate Phase 1 and Phase 2 dynamically are not classified as "static tunnels", and therefore are omitted from the `fgVpnTunTable`.

ADVPN shortcuts are created and torn down dynamically based on traffic flow and the idle-timeout / *holddown timer*. Since the Phase 1 and Phase 2 SAs (*Security Associations*) of these shortcuts are temporary, Fortinet does not map them into the static MIB structure to avoid SNMP index pollution and scan inconsistencies.

For this reason, **it is not possible to monitor the traditional operational status (Up/Down)** of these VPNs via SNMP, because Fortinet does not provide a connection-state OID for dynamic tunnels. See below the *Dialup* table MIB with the information it provides.

## Dialup table MIB

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