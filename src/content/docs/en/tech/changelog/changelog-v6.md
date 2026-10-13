---
title: Changelog v6
description: Follow the Changelog for Monsta version 6 and learn about the new
  features, improvements, fixes and changes made in each platform update.
sidebar:
  order: 2
---
## Version 6.0.23 Beta

🔧**Fix**: **Improvements to WMI collection**. Intermittent read timeouts resolved.

## Version 6.0.22 Beta

🔧**Fix**: **Metric in critical state**. Fixed an issue where metrics with a maximum limit defined via dynamic device reading incorrectly entered a critical state under certain conditions.

🔧**Fix**: **WMI collection failures**. Fixed read failures and occasional inconsistencies in data collected by the Monsta Probe.

## Version 6.0.21 Beta

🔧**Fix**: **Failure when adding a dashboard**. Resolved a kernel error that prevented adding/removing a dashboard to an old user in the management interface.

🔧**Fix**: **Blank dashboard listing**. Fixed an issue that caused the dashboard list to appear blank immediately after adding a new record in user editing.

## Version 6.0.20 Beta

🔧**Fix**: **Probe collection failures**. Certain monitors of the Windows probe randomly freeze and stop collecting data.

## Version 6.0.19 Beta

**🔧Fix**: **Alerts not sent**. Some alerts were not triggered even when the value was above the limit. This happened when the monitored value rarely changed: after system restart it was not available in memory and the alert could not confirm the limit, remaining inactive.

## Version 6.0.17

**✨New**: **Monthly Reports with Artificial Intelligence**. Now your account automatically generates monthly reports enriched with *insights* powered by AI.

![image.png](/src/assets/images/image-10.png)

**✨New**: **Remote Execution via PowerShell**. The Probe allows execution of commands and *scripts* in PowerShell directly from the console. For security reasons, this feature is only available when the user authorizes its use during the Probe installation. In addition, all commands are executed using a **user with restricted privileges (non-administrator)**.

:::note

This feature requires installation of the latest Monsta Probe, available on our website.

:::

![image.png](/src/assets/images/image-5.png)

**✨New**: **S.M.A.R.T. Monitoring**. We added support for collecting S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) data from physical disks, allowing you to monitor integrity, lifespan, and storage health indicators to identify potential failures before they affect the environment. 

:::note

This feature requires installation of the latest Monsta Probe, available on our website.

:::

![image.png](/src/assets/images/image-9.png)

🔧**Fix**: **Preservation of White Label on updates**. Fixed an unexpected behavior where system updates reverted to the default logo.

🔧**Fix**: **Update to event status.** Now, when a device or monitor toggles state between warning and critical, only the most recent event remains marked as unresolved in the timeline, preventing accumulation of pending entries for the same incident.

**🔧Fix**: **Agent Reconnection After Backup**. Fixed agent reconnection after restoring a cloud backup on new installations.

**🔧Fix**: **Adjustment to Alarm Triggering for Monitors**. Fixed an occasional issue that prevented alarms from firing on some monitors.

## Version 6.0.9

**🔧Fix**: Buttons added to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Information about the key and license appeared blank in some cases.

**🔧Fix**: Monsta prompts the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring of remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#mapa-dinamico) with the ability to set positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area in any unit of measurement.

**🔧Fix**: Devices without uptime did not send alerts.

**🔧Fix**: Variables that report the previous state in alert templates were not enabled.

**🔧Fix**: Default value provided in monitor parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarm with false status when limits are inverted.

**🔧Fix**: Namespace is not sent in WMI collections.