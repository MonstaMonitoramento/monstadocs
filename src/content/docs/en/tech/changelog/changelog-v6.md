---
title: Changelog v6
description: Follow the Changelog for Monsta version 6 and learn about the new features,
  improvements, fixes, and changes made in each platform update.
sidebar:
  order: 2
---
## Version 6.0.16 Beta

**✨New**: **Monthly Reports with Artificial Intelligence**. Now your account automatically generates monthly reports enriched with *insights* based on AI.

![image.png](/src/assets/images/image-10.png)

**✨New**: **Remote Execution via PowerShell**. The Probe allows the execution of commands and *scripts* in PowerShell directly from the console. To ensure the security of your environment, all commands are processed using a **restricted-privilege user (non-administrator)**.

![image.png](/src/assets/images/image-5.png)

**✨New**: **S.M.A.R.T. Monitoring**. We added support for collecting S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) data from physical drives, allowing you to monitor storage health, lifespan, and indicators to identify potential failures before they affect the environment.

![image.png](/src/assets/images/image-9.png)

🔧**Fix**: Fixed an unexpected behavior where system updates improperly affected the custom logo set by the user.

## Version 6.0.13 Beta

**🔧Fix**: Optimized the startup time of data collection in new installations.

**🔧Fix**: Fixed agent reconnection after cloud backup restoration in new installations.

**🔧Fix**: Fixed an intermittent issue that prevented alarms from being triggered on some monitors.

## Version 6.0.9

**🔧Fix**: Added buttons to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Information about the key and license appeared blank in some cases.

**🔧Fix**: Monsta requested the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring of remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#dynamic-map) with the ability to set positions, add widgets, and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area in any unit of measurement.

**🔧Fix**: Devices without uptime did not send alerts.

**🔧Fix**: Variables that report the previous state in alert templates were not enabled.

**🔧Fix**: Default value provided in a monitor's parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarm showed false status when thresholds were inverted.

**🔧Fix**: Namespace was not sent in WMI collections.
