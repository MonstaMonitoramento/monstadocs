---
title: Changelog v6
description: Track the Changelog for Monsta version 6 and learn about new
  features, improvements, fixes and changes made in each platform update.
sidebar:
  order: 2
---
## Version 6.0.25 Beta

🔧**Fix**: **Improvements to WMI collection**. Intermittent read timeouts resolved.

🔧**Fix**: **SNMPv3 authentication failures**. Resolved failures in SNMPv3 authentications (authPriv and authNoPriv) caused by an issue in the initial handshake for time synchronization and encryption calculation when requested.

## Version 6.0.22 Beta

🔧**Fix**: **Metric in critical state**. Fixed an issue where metrics with a maximum limit defined via dynamic reading from the device were incorrectly entering a critical state under certain conditions.

🔧**Fix**: **WMI collection failures**. Fixed read errors and occasional inconsistencies in data collected by the Monsta probe.

## Version 6.0.21 Beta

🔧**Fix**: **Error when adding a panel**. Resolved a kernel error that prevented adding/removing a panel to an older user in the management interface.

🔧**Fix**: **Blank panel listing**. Fixed an issue that caused the panel list to appear blank immediately after adding a new record in user editing.

## Version 6.0.20 Beta

🔧**Fix**: **Probe collection failures**. Certain monitors of the Windows probe were freezing randomly and stopping data collection.

## Version 6.0.19 Beta

**🔧Fix**: **Alerts not sent**. Some alerts were not triggered even when the value was above the threshold. This occurred when the monitored value rarely changed: after a system restart, it was not available in memory and the alert could not confirm the threshold, remaining inactive.

## Version 6.0.17

**✨New**: **Monthly Reports with Artificial Intelligence**. Your account now automatically generates monthly reports enriched with AI-based *insights*.

![image.png](/src/assets/images/image-10.png)

**✨New**: **Remote Execution via PowerShell**. The Probe allows the execution of commands and *scripts* in PowerShell directly from the console. For security reasons, this feature is only made available when the user authorizes its use during Probe installation. In addition, all commands are executed using a **user with restricted privileges (non-administrator)**.

:::note

This feature requires the installation of the latest Monsta Probe, available on our website.

:::

![image.png](/src/assets/images/image-5.png)

**✨New**: **S.M.A.R.T. Monitoring**. We added support for collecting S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) data from physical drives, allowing you to monitor integrity, lifespan, and storage health indicators to identify potential failures before they affect the environment.

:::note

This feature requires the installation of the latest Monsta Probe, available on our website.

:::

![image.png](/src/assets/images/image-9.png)

🔧**Fix**: **Preservation of White Label during updates**. Fixed an unexpected behavior where system updates reverted to the default logo.

🔧**Fix**: **Update to event status.** Now, when a device or monitor switches state between warning and critical, only the most recent event remains marked as unresolved on the timeline, preventing the accumulation of pending items for the same incident.

**🔧Fix**: **Agents Reconnection After Backup**. Fixed agents reconnection after restoring a cloud backup on new installations.

**🔧Fix**: **Adjustment to Alarm Triggering for Monitors**. Fixed an intermittent issue that prevented alarms from firing on some monitors.

## Version 6.0.9

**🔧Fix**: Buttons were provided to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Information about the key and license appeared blank in some cases.

**🔧Fix**: Monsta prompts for the client area login to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#mapa-dinamico) with the ability to set positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area using any unit of measure.

**🔧Fix**: Devices without uptime did not send alerts.

**🔧Fix**: Variables that report the previous state in alert templates were not enabled.

**🔧Fix**: Default value specified in a monitor's parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarms with false status when thresholds are inverted.

**🔧Fix**: Namespace is not sent in WMI collections.