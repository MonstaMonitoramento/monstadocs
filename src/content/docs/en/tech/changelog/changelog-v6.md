---
title: Changelog v6
description: Follow the changelog for Monsta version 6 and discover the new
  features, improvements, fixes, and changes made in each platform update.
sidebar:
  order: 2
---
## Version 6.0.20 Beta

🔧**Fix**: **Probe collection failure**. Certain Windows probe monitors randomly freeze and stop collecting data.

## Version 6.0.19 Beta

**🔧Fix**: **Alerts not sent**. Some alerts were not triggered even when the value was above the threshold. This occurred when the monitored value rarely changed: after system restart it was not available in memory and the alert could not confirm the threshold, remaining inactive.

## Version 6.0.17

**✨New**: **Monthly Reports with Artificial Intelligence**. Now your account automatically generates monthly reports enriched with *insights* based on AI.

![image.png](/src/assets/images/image-10.png)

**✨New**: **Remote Execution via PowerShell**. The Probe allows the execution of PowerShell commands and *scripts* directly from the console. For security reasons, this feature is made available only when the user authorizes its use during Probe installation. Additionally, all commands are executed using a **user with restricted privileges (non-administrator)**.

:::note

This feature requires installing the latest version of the Monsta Probe, available on our website.

:::

![image.png](/src/assets/images/image-5.png)

**✨New**: **S.M.A.R.T. Monitoring**. We added support for collecting S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) data from physical drives, enabling monitoring of integrity, lifespan, and storage health indicators to identify potential failures before they impact the environment. 

:::note

This feature requires installing the latest version of the Monsta Probe, available on our website.

:::

![image.png](/src/assets/images/image-9.png)

🔧**Fix**: **Preservation of White Label on updates**. Fixed an unexpected behavior where system updates reverted to the default logo.

🔧**Fix**: **Event status update.** Now, when a device or monitor switches state between warning and critical, only the most recent event remains marked as unresolved on the timeline, preventing the accumulation of pending items for the same incident.

**🔧Fix**: **Agent Reconnection After Backup**. Fixed agent reconnection after restoring a cloud backup on new installations.

**🔧Fix**: **Adjustment to Alarm Triggering for Monitors**. Fixed an intermittent issue that prevented alarms from being triggered on some monitors.

## Version 6.0.9

**🔧Fix**: Added buttons to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Information about the key and license appeared blank in some cases.

**🔧Fix**: Monsta prompted the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#mapa-dinâmico) with the ability to set positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area in any unit of measurement.

**🔧Fix**: Devices without uptime did not send alerts.

**🔧Fix**: Variables that report the previous state in alert templates were not enabled.

**🔧Fix**: The default value provided in a monitor's parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarm showed false status when thresholds were inverted.

**🔧Fix**: Namespace was not sent in WMI collections.