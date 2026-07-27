---
title: Changelog v6
description: Track the Changelog of Monsta version 6 and discover the new
  features, improvements, fixes and changes made in each platform update.
sidebar:
  order: 2
---
## Version 6.0.17 Beta

🔧**Fix**: **Event status update**. Now, when a device or monitor switches state between warning and critical, only the most recent event remains marked as unresolved in the timeline, avoiding the accumulation of pending items for the same incident.

🔧**Fix**: **Fix in alerts with decimal values**. Adjusted the reading of thresholds so that alerts correctly consider decimal places, preventing incorrect triggers on fractional metrics.

**🔧Fix**: **Adjustment in percentage alerts**. Fixed the configuration limit to allow the percentage bar to be positioned at **0%**.

## Version 6.0.16 Beta

**✨New**: **Monthly Reports with Artificial Intelligence**. Now, your account automatically generates monthly reports enriched with *insights* based on AI.

![image.png](/src/assets/images/image-10.png)

**✨New**: **Remote Execution via PowerShell**. The Probe allows the execution of commands and *scripts* in PowerShell directly from the console. To ensure your environment's security, all commands are processed using a **user with restricted privileges (non-administrator)**.

![image.png](/src/assets/images/image-5.png)

**✨New**: **S.M.A.R.T. Monitoring**. We added support for collecting S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) data from physical disks, allowing you to monitor integrity, lifespan, and storage health indicators to identify potential failures before they affect the environment.

![image.png](/src/assets/images/image-9.png)

🔧**Fix**: Fixed an unexpected behavior where system updates improperly affected the user-defined custom logo.

## Version 6.0.13 Beta

**🔧Fix**: Optimized the startup time for data collection in new installations.

**🔧Fix**: Fixed agent reconnection after cloud backup restoration in new installations.

**🔧Fix**: Fixed an intermittent issue that prevented alarms from triggering on some monitors.

## Version 6.0.9

**🔧Fix**: Added buttons to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Fixed an issue where information about the key and license appeared blank in some cases.

**🔧Fix**: Fixed an issue where Monsta requested the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring of remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#dynamic-map) with the ability to set positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area in any unit of measurement.

**🔧Fix**: Fixed an issue where devices without uptime did not send alerts.

**🔧Fix**: Fixed an issue where variables reporting the previous state in alert templates were not enabled.

**🔧Fix**: Fixed an issue where the default value provided in a monitor's parameters returned null.

**🔧Fix**: Fixed a general failure message when adding automatic monitors with certain templates.

**🔧Fix**: Fixed an issue where boolean monitors alarmed with a false status when limits were inverted.

**🔧Fix**: Fixed an issue where namespace was not sent in WMI collections.