---
title: "Changelog v5"
sidebar:
  order: 3
---

## Version 5.1.22

**🔧Fix**: Child device failure event does not send an alert after parent device recovered from failure.

**🔧Fix**: Device permissions for non-admin users.

**🔧Fix**: Indicator Bar widget loses the selected monitor when editing the dashboard.

**🔧Fix**: Port used by `Monagent` could cause memory overflow with malformed packets on servers without firewall enabled.

**🔧Fix**: In some cases a white screen appears when accessing the automatic monitors option.

## Version 5.1.21

**🔧Fix**: Cloud alert group does not save changes the first time.

**🔧Fix**: *Piechart* and *Doughnutchart* widgets add disabled devices.

**🔧Fix**: Some widgets were not displayed when publishing the dashboard.

## Version 5.1.20

**✨New**: Smart cache for `SNMP` queries.

**✨New**: Unresolved event indicator in the Timeline.

**✨New**: Responsive mobile layout.

**✨New**: New certificates accepted for HTTPS connections.

**✨New**: New widgets for dashboards.

**✨New**: Automatic update for new versions.

**✨New**: New templates.

**✨New**: Graph area calculation (ISPs can report traffic in MB to Anatel).

**🔧Fix**: Templates were imported without some metrics.

**🔧Fix**: IPv6 returned errors in `SNMP` collections.

**🔧Fix**: Monitors did not allow changing the unit of measure.

**🔧Fix**: Kernel error when removing some devices.

**🔧Fix**: Maps did not show duplicated or newly created devices on the map.

**🔧Fix**: `SNMP` did not collect information on IPv6 networks.

**🔧Fix**: Could not change the unit scale of existing monitors on devices.

**🔧Fix**: Instances with quotes in the name caused collection failures.

**🔧Fix**: Changes to duplicated dashboards affected the original.

## Version 5.0.4

**🔧Fix**: Incorrect alert sending behavior when the normal state is not selected.

## Version 5.0.3

**🔧Fix**: Restoring backups does not display files.

## Version 5.0

**✨New**: New system kernel controls monitor collection calls, increasing capacity for thousands of simultaneous queries.

**✨New**: New components for dashboards.

**✨New**: New templates.

**✨New**: Protection against excessive queries for slow devices.

**✨New**: Certificate automation for secure access with the *Let's Encrypt*.

**✨New**: Dark mode.

**✨New**: Alert templates can be created and configured individually.

**✨New**: Custom sound configuration per device or monitor.

**🔧Fix**: Algorithm for automatic monitors.

**🔧Fix**: Database log rotation.

**🔧Fix**: Automatic login when there is loss of connection with the *browser*.