---
title: Changelog v6
description: Explore the Monsta v6 Changelog and stay up to date with new features, improvements, bug fixes, and changes introduced in each platform release.
sidebar:
  order: 2
---
## Version 6.0.13 Beta

**🔧Fix**: Optimized the data collection startup time on new installations.

**🔧Fix**: Fixed agent reconnection after restoring cloud backup on new installations.

**🔧Fix**: Fixed an intermittent issue that prevented alarms from firing on some monitors.

## Version 6.0.9

**🔧Fix**: Buttons are now available to remove disconnected and blocked agents on the management screen.

**🔧Fix**: Information about the key and license appeared blank in some cases.

**🔧Fix**: Monsta requests the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Remote network monitoring without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: [Map for hierarchical view](/en/manual/dispositivos/visualizacao-em-mapa#dynamic-map) with the ability to set positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area for any unit of measurement.

**🔧Fix**: Devices without uptime did not send alerts.

**🔧Fix**: Variables that report the previous state in alert templates were not enabled.

**🔧Fix**: Default value provided in a monitor's parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarmed with false status when thresholds are inverted.

**🔧Fix**: Namespace is not sent in WMI collections.
