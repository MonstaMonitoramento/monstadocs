---
title: Changelog v6
description: Follow the Changelog for Monsta version 6 and discover the new
  features, improvements, fixes and changes made in each platform update.
sidebar:
  order: 2
---
## Version 6.0.17

**✨New**: **Monthly Reports with Artificial Intelligence**. Now, your account automatically generates monthly reports enriched with *insights* based on AI.

![image.png](/src/assets/images/image-10.png)

**✨New**: **Remote Execution via PowerShell**. The Probe allows the execution of commands and *scripts* in PowerShell directly from the console. For security reasons, this feature is only made available when the user authorizes its use during Probe installation. In addition, all commands are executed using a **user with restricted privileges (non-administrator)**.

![image.png](/src/assets/images/image-5.png)

**✨New**: **S.M.A.R.T. Monitoring**. We added support for collecting S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) data from physical disks, allowing you to monitor storage integrity, lifespan, and health indicators to identify possible failures before they affect the environment.

![image.png](/src/assets/images/image-9.png)

🔧**Fix**: Fixed an unexpected behavior where system updates were inadvertently affecting the custom logo set by the user (White Label).

🔧**Fix**: **Event status update.** Now, when a device or monitor switches state between warning and critical, only the most recent event remains marked as unresolved in the timeline, preventing the accumulation of pending items for the same incident.

**🔧Fix**: **Agent Reconnection After Backup**. Fixed agent reconnection after restoring cloud backup on new installations.

**🔧Fix**: **Adjustment to Alarm Triggering for Monitors**. Fixed an intermittent issue that prevented alarms from triggering on some monitors.

## Version 6.0.9

**🔧Fix**: Buttons are available to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Key and license information appeared blank in some cases.

**🔧Fix**: Monsta requested the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#mapa-dinamico) with the ability to define positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area in any unit of measurement.

**🔧Fix**: Devices without uptime did not send alerts.

**🔧Fix**: Variables that inform the previous state in alert templates were not enabled.

**🔧Fix**: Default value provided in a monitor's parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarm showed false status when limits were inverted.

**🔧Fix**: Namespace was not sent in WMI collections.