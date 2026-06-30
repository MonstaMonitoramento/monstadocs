---
title: "Changelog v6"
sidebar:
  order: 2
---

## Version 6.0.9

**🔧Fix**: Buttons to remove disconnected and blocked agents made available on the management screen.

**🔧Fix**: Key and license information appeared blank in some cases.

**🔧Fix**: Monsta prompts the client area login screen to validate the key in some situations.

## Version 6.0.6

**✨New**: **Agents** - Monitoring of remote networks without the need for VPNs or port forwarding [Agent: Zero Conf Installation](/en/start/instalacao/agente-instalacao-zero-conf).

**✨New**: Map for hierarchical view with the ability to set positions, add widgets and metrics.

**✨New**: Dashboards can be made available to non-administrator users.

**✨New**: Consumption report can calculate area in any unit of measurement.

**🔧Fix**: Devices without uptime did not send alerts.

**🔧Fix**: Variables that report the previous state in alert templates were not enabled.

**🔧Fix**: Default value provided in a monitor's parameters returned null.

**🔧Fix**: General failure message when adding automatic monitors with some templates.

**🔧Fix**: Boolean monitor alarmed with false status when thresholds are inverted.

**🔧Fix**: Namespace was not sent in WMI collections.