---
title: Changelog v6
description: Follow the Changelog of Monsta version 6 and learn about the new
  features, improvements, fixes and changes made in each platform update.
sidebar:
  order: 2
---
## Version 6.0.17

**✨New**: **Monthly Reports with Artificial Intelligence**. Now your account automatically generates monthly reports enriched with AI-based *insights*.

![image.png](/src/assets/images/image-10.png)

**✨New**: **Remote Execution via PowerShell**. The Probe allows the execution of PowerShell commands and *scripts* directly from the console. For security reasons, this feature is available only when the user authorizes its use during Probe installation. In addition, all commands are executed using a **user with restricted privileges (non-administrator)**.

![image.png](/src/assets/images/image-5.png)

**✨New**: **S.M.A.R.T. Monitoring**. We added support for collecting S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) data from physical drives, allowing monitoring of integrity, lifespan and storage health indicators to identify potential failures before they affect the environment.

![image.png](/src/assets/images/image-9.png)

🔧**Fix**: **Preservation of White Label on updates**. Fixed an unexpected behavior where system updates reverted the logo to the default.

🔧**Fix**: **Event status update.** Now, when a device or monitor switches state between warning and critical, only the most recent event remains marked as unresolved in the timeline, avoiding accumulation of pending items for the same incident.

**🔧Fix**: **Agents Reconnection After Backup**. Fixed agents reconnection after restoring cloud backup in new installations.

**🔧Fix**: **Adjustment in Alarm Triggering for Monitors**. Fixed a sporadic issue that prevented alarms from firing on some monitors.

## Version 6.0.9

**🔧Fix**: Added buttons to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Information about the key and license appeared blank in some cases.

**🔧Fix**: Monsta prompts the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#mapa-dinâmico) with the ability to set positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area from any unit of measurement.

**🔧Fix**: Devices with no uptime did not send alerts.

**🔧Fix**: Variables that report the previous state in alert templates were not enabled.

**🔧Fix**: Default value provided in a monitor's parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarmed with a false status when thresholds were inverted.

**🔧Fix**: Namespace was not sent in WMI collections.