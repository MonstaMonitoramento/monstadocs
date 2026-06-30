---
title: "Changelog v4"
sidebar:
  order: 4
---

## Version 4.1.19

**✨New**: Preparation for the upgrade to version **5**. Note: This update will restart the server.

## Version 4.1.16

**🔧Fix**: Folder `/var/monsta/agent/store` did not remove old files.

**🔧Fix**: Maximum value in a chart is shown as `0` when the value is negative.

**🔧Fix**: `SNMP` cache, in some situations, prevents the agent from performing queries against the device.

**🔧Fix**: Native `SNMP` uses the same request-id and causes high memory usage on some equipment.

**🔧Fix**: In the Panel, in some situations, the save button has no effect after modifying or inserting a component.

**🔧Fix**: Program `monagentd` stops responding to requests from the Monsta core in some situations.

**🔧Fix**: Instances with numeric names fail to be monitored.

**🔧Fix**: Automatic monitor rules create monitors with the alert group left blank.

## Version 4.1.15

**✨New**: Ability to remove automatic monitors in minutes/hours/days.

**🔧Fix**: Automatic monitors duplicate created items when dynamic instance search is not checked.

**🔧Fix**: New version available warning takes up to 15 minutes to appear on the screen.

**🔧Fix**: `monstadb` logs are not rotated correctly.

## Version 4.1.14

**✨New**: Automatic discovery of monitors (Monsta creates and removes monitors automatically as they are handled on the device).

**✨New**: Filter for displaying devices and monitors.

**✨New**: Ability to upgrade Monsta to Beta versions.

**✨New**: Backups with up to 1 month of information to restore.

**✨New**: Option to import and export templates.

**✨New**: `WebSockets` - New function `ws.send_recv()` to be used in monitors.

**✨New**: Low SMS and email credits trigger alerts on the screen.

**✨New**: Local cache for instances in `SNMP`.

**✨New**: Button to disable monitoring for a host.

**✨New**: Native `SNMP` (for lower resource consumption).

**✨New**: Option to save user data on the login screen.

**✨New**: Timeline shows monitor values.

**✨New**: Bar to increase device text on the main screen.

**✨New**: New TP-Link - Switch template.

**✨New**: New Cambium Networks template.

**✨New**: New WNI - Challenger template.

**✨New**: New Intracom Telecom - OmniBAS template.

**✨New**: New Intelbras - APC template.

**✨New**: New Juniper - MX5 template.

**✨New**: New Cianet - OLT GEPON template.

**✨New**: New Huawei - OLT MA5600 template.

**✨New**: New Socomec - Net Vision Masterys BC (UPS) template.

**✨New**: New 3Com - 4800 Switch template.

**✨New**: New Ericsson - Mini-Link template.

**✨New**: New Datacom (OLT) template.

**✨New**: New Volt - MPPT Charge Controller template.

**✨New**: New Volt - Full Power 620 Evolution template.

**✨New**: New Volt - AC Distribution Point template.

**✨New**: New Volt - Customer Distribution Point (PDC Evolution) template.

**✨New**: New Volt - Pop Protect template.

**✨New**: New Volt - Power Net 1000 Evolution template.

**✨New**: New Volt - Mini Central UPS `SNMP` template.

**✨New**: New monitors for Mikrotik - Routerboard.

**🔧Fix**: Groups displayed in alphabetical order.

**🔧Fix**: New devices appear for users without permission to access them.

**🔧Fix**: SMS messages longer than 160 characters were not sent (messages are now truncated).

**🔧Fix**: Real-time display option did not work properly on the timeline.

**🔧Fix**: Removed libraries from `/opt/monsta/lib` that conflicted with Linux server updates.

**🔧Fix**: Existing template monitors could not be modified.

**🔧Fix**: Data source for uptime check did not appear ordered. In some cases, some items were no longer displayed.

**🔧Fix**: Backups are overwritten when more than one license is in use on a single account.

**🔧Fix**: Cloning a device causes the primary device's chart to be published.

**🔧Fix**: A monitor's limits are not changed when the return type is changed (e.g., numeric, boolean, string, etc.).

**🔧Fix**: Function `params.InstaceId()` does not return the correct value, causing monitors that use it to fail.

**🔧Fix**: Devices are considered critical in the total sum even if only one monitor is in a critical state.

**🔧Fix**: Some Monsta logs were not being rotated.

**🔧Fix**: Monsta writes repeated information to the `moncored.log` file, causing these files to grow very large.

**🔧Fix**: When restoring a backup, icons are not copied.

**🔧Fix**: Device boxes do not shake when their state changes.

**🔧Fix**: When installing a license, Monsta occasionally reports that it is already in use.

**🔧Fix**: Charts with monitoring frequency in seconds are now displayed with a 1h range by default.

**🔧Fix**: In the panel, charts allow selection of monitors of type `string`.

## Version 4.0.20

**✨New**: Added option of tools for the device (`traceroute`, `ping` and open in a browser).

**✨New**: Option to hide chart legends in a panel.

**✨New**: Sending alerts via Telegram.

**✨New**: Real-time chart display.

**✨New**: New visualization tree (Sunburst).

**✨New**: New BGP - BGP4 template.

**✨New**: New Intelbras - Recorders (HDCVI) template.

**✨New**: New Sophos - XG Firewall template.

**✨New**: New Brother - Laser Printer template.

**✨New**: New Ubiquiti - Edgeswitch template.

**✨New**: New Parks - OLT 10008S template.

**✨New**: New Huawei - NE20S template.

**✨New**: New Huawei - S6720 template.

**✨New**: New Morningstar - XPS template.

**✨New**: New Volt - Net Probe template.

**✨New**: New BlockBit - UTM template.

**✨New**: New Seagate - NAS template.

**✨New**: New SMS - UPS template.

**✨New**: New Intelbras - WOM template.

**✨New**: New Apple - Mac OS X template.

**✨New**: New Lenovo - IX4 template.

**✨New**: New Dell - iDRAC template.

**✨New**: New Polycom - Videoconference template.

**✨New**: New Fiberhome - OLT template.

**🔧Fix**: While editing/inserting a device, when specifying a packet size in the uptime check, the Ok button did not save the settings.

**🔧Fix**: IP addresses are not displayed when selecting an instance.

**🔧Fix**: Color legends appear without information in published charts.

**🔧Fix**: In some system stress situations, monitors that use ICMP, such as uptime and ping, stop working.

**🔧Fix**: When cloning a device, the default group is added automatically.

**🔧Fix**: Monsta sends alerts for a device's monitors even when that device is in a critical state.

**🔧Fix**: Some scripts with dynamic instances cannot obtain metric values.

**🔧Fix**: When editing a metric, the maximum value did not allow negative values.

**🔧Fix**: Publishing a chart with multiple instances did not show their names in the legend.

**🔧Fix**: In some situations, the data verification service stops responding and it is necessary to restart the service.

## Version 4.0.12

**✨New**: Percentile and ability to select data grouping time in charts.

**✨New**: Multiple state selection on the devices screen.

**🔧Fix**: Date selection component in a chart sometimes becomes slow.

**🔧Fix**: Some metrics appear with zeroed values in the Panel.

**🔧Fix**: Chart fills do not keep the same color as the line.

**🔧Fix**: In monitors with multiple boolean metrics, clicking a metric always displayed the chart for the first one.

**🔧Fix**: Instances with long names cause a loading error when adding a monitor.

## Version 4.0.6

**🔧Fix**: It was not possible to save devices that use `snmp` with a port other than 161.

**🔧Fix**: It was not possible to save a data source with a return type other than numeric.

**🔧Fix**: Point view on charts did not show seconds.

**🔧Fix**: String-type monitors were always returned with the normal state.

## Version 4.0.4

**✨New**: Function ping.send() modified to return success after receiving the first packet.

**✨New**: The uptime monitor displays the time the equipment has been up (only for devices with `snmp`).

**✨New**: Button to export/print a chart in PNG, PDF, SVG, CSV and XLS formats.

**🔧Fix**: When adding a device, the uptime monitor started in a critical state.

**🔧Fix**: When removing a device group from a user, Monsta adds all devices from that group individually to the same user.

**🔧Fix**: Chart legend returned to the previous model.

**🔧Fix**: Devices marked to not send alerts were not listed on the device view screen.

**🔧Fix**: Metric name of a monitor returned in alerts when a monitor returns to normal state was incorrect.

**🔧Fix**: `SNMP` v3 generates error during authentication.

**🔧Fix**: On systems with `openssl` versions later than `1.0.1e`, RPM installation fails when generating the SSL certificate and the HTTP server does not start.

**🔧Fix**: Number of attempts was ignored in some situations.

## Version 4.0.2

**✨New**: System core completely remodeled for lower hardware consumption and increased performance.

**✨New**: Configuration database now works in memory.

**✨New**: New color selection format for monitor and Panel charts.

**✨New**: New models for tree display (Hierarchy and Map) with zoom and pan.

**✨New**: Device and monitor check interval can be in seconds.

**✨New**: Ability to search for dynamic instances on a device (e.g., users authenticated with PPPoE).

**✨New**: New variables to be used in alert templates.

**🔧Fix**: Uptime chart is not displayed correctly when selecting a period longer than 4 months.

**🔧Fix**: In some browsers, group boxes swap places when clicking on them.

**🔧Fix**: In some cases, the count of devices by status is not displayed correctly.

**🔧Fix**: In tree view, devices without an icon cannot be selected.

**🔧Fix**: Pagination enabled on the Timeline.

**🔧Fix**: During metric editing in a template, the up/down move arrows delete the selected metric.

**🔧Fix**: Special characters are not displayed correctly on the devices screen.

**🔧Fix**: Correction of the algorithm for the "CPU Usage" monitor in the Linux template.