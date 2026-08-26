---
title: Supervisión del estado de las VPN Dialup (ADVPN) mediante SNMP en FortiOS
description: Entienda por qué el monitor de estado de Fortinet no muestra las VPN del tipo Dialup (ADVPN) en la tabla predeterminada (fgVpnTunTable) y consulte la estructura de la MIB fgVpn2DialupTable para la supervisión.
---

## Limitación de la supervisión del estado de las VPN Dialup (ADVPN)

**ADVPN es una arquitectura Dialup/Dynamic**: El **ADVPN** utiliza túneles padre del tipo *Dialup* (en Hubs y Spokes) y crea atajos dinámicos (*shortcuts*) bajo demanda entre los Spokes. Para **FortiOS**, las conexiones que negocian Fase 1 y Fase 2 de forma dinámica no se clasifican como "túneles estáticos", y por eso se omiten de la `fgVpnTunTable`.

Los atajos ADVPN se crean y cierran dinámicamente en función del flujo de tráfico y de los temporizadores de inactividad (*idle-timeout* / *holddown timer*). Como las SAs (*Asociaciones de Seguridad*) de Fase 1 y Fase 2 de esos atajos son temporales, Fortinet no las mapea en la estructura de MIB estática para evitar la contaminación de índices SNMP y las inconsistencias en el sondeo.

Por esa razón, **no es posible monitorizar el estado operativo tradicional (Up/Down)** de estas VPN mediante SNMP, ya que Fortinet no proporciona una OID de estado de conexión para túneles dinámicos. A continuación se muestra la MIB de la tabla *Dialup* con la información que proporciona.

## MIB da tabela Dialup

| | | |
| ------------------------ | --------------------------------- | ---------------------------------------------------------------------------------------- |
| `fgVpn2Tables` | `1.3.6.1.4.1.12356.101.12.4` | |
| `fgVpn2DialupTable` | `1.3.6.1.4.1.12356.101.12.4.1` | Información de pares de VPN Dial-up |
| `fgVpn2DialupEntry` | `1.3.6.1.4.1.12356.101.12.4.1.1` | Información del par (peer) de VPN Dial-up |
| `fgVpn2DialupIndex` | `1.3.6.1.4.1.12356.101.12.4.1.1.1` | Un valor de índice que identifica de manera única a un par VPN dial-up dentro de la `fgVpn2DialupTable` |
| `fgVpn2DialupGatewayType` | `1.3.6.1.4.1.12356.101.12.4.1.1.2` | Tipo de dirección del gateway remoto del túnel |
| `fgVpn2DialupGateway` | `1.3.6.1.4.1.12356.101.12.4.1.1.3` | Dirección del gateway remoto del túnel |
| `fgVpn2DialupLifetime` | `1.3.6.1.4.1.12356.101.12.4.1.1.4` | Tiempo de vida (segundos) del túnel |
| `fgVpn2DialupTimeout` | `1.3.6.1.4.1.12356.101.12.4.1.1.5` | Tiempo antes del siguiente intercambio de claves (segundos) del túnel |
| `fgVpn2DialupSrcBeginType` | `1.3.6.1.4.1.12356.101.12.4.1.1.6` | Tipo de IP inicial del rango de direcciones remotas del túnel |
| `fgVpn2DialupSrcBegin` | `1.3.6.1.4.1.12356.101.12.4.1.1.7` | Inicio del rango de direcciones remotas del túnel |
| `fgVpn2DialupSrcEndType` | `1.3.6.1.4.1.12356.101.12.4.1.1.8` | Tipo de IP final del rango de direcciones remotas del túnel |
| `fgVpn2DialupSrcEnd` | `1.3.6.1.4.1.12356.101.12.4.1.1.9` | Final del rango de direcciones remotas del túnel |
| `fgVpn2DialupDstBeginType` | `1.3.6.1.4.1.12356.101.12.4.1.1.10` | Tipo de IP inicial del rango de direcciones locales del túnel |
| `fgVpn2DialupDstBegin` | `1.3.6.1.4.1.12356.101.12.4.1.1.11` | Inicio del rango de direcciones locales del túnel |
| `fgVpn2DialupDstEndType` | `1.3.6.1.4.1.12356.101.12.4.1.1.12` | Tipo de IP final del rango de direcciones locales del túnel |
| `fgVpn2DialupDstEnd` | `1.3.6.1.4.1.12356.101.12.4.1.1.13` | Final del rango de direcciones locales del túnel |
| `fgVpn2DialupInOctets` | `1.3.6.1.4.1.12356.101.12.4.1.1.14` | Número de bytes recibidos en el túnel desde su instanciación. |
| `fgVpn2DialupOutOctets` | `1.3.6.1.4.1.12356.101.12.4.1.1.15` | Número de bytes enviados en el túnel desde su instanciación. |
| `fgVpn2DialupPhase1Name` | `1.3.6.1.4.1.12356.101.12.4.1.1.16` | Nombre descriptivo de la configuración de la fase 1 del túnel |
| `fgVpn2DialupVdom` | `1.3.6.1.4.1.12356.101.12.4.1.1.17` | Dominio virtual al que pertenece el túnel. Este índice corresponde al utilizado por fgVdTable. |