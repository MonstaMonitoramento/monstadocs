---
title: "Changelog v3"
sidebar:
  order: 5
---

## Version 3.1.7

**🔧Fix**: When adding monitors with a large number of instances, Monsta displays a timeout message.

## Version 3.1.6

**🔧Fix**: In some cases memory leaks and failures occurred in the execution of some monitors.

## Version 3.1.5

**✨New**: Retry count was increased to 120.

**✨New**: "Search Device" filter also searches by IP address.

**✨New**: String Type accepts hexadecimal values.

**✨New**: String Type accepts text.

**✨New**: WMI search accepts other namespaces.

**✨New**: Function `return()` in a script can force the state of a metric in a monitor.

**✨New**: Sound alert for status changes.

**✨New**: Ability to publish a link to a monitor without requiring login.

**✨New**: Template Unbound - DNS Server.

**✨New**: Template Intelbras - Switches.

**✨New**: Template Microsoft - Windows (Inventory).

**✨New**: Monitors "Services Running", "Motherboard Status", "Physical Memory Status", "Processor Status" and "Power Supply Status" for the Microsoft - Windows template.

**✨New**: Monitors "Processes", "Load (Load Average)" and "MAC Address" for the Linux template.

**✨New**: Monitor "MAC Address" for the templates Generic, Linux, Ubiquiti - AirOS 5.6 and Ubiquiti - Airmax AC.

**🔧Fix**: State display filter could omit some devices from the list.

**🔧Fix**: ICMP packet size in the *uptime* check was ignored.

**🔧Fix**: Return type was not handled in Monsta templates.

**🔧Fix**: Selecting a date range in a string-type monitor did not work.

**🔧Fix**: The *uptime* history did not show more than 4 months of data.

**🔧Fix**: Monsta's init script might not start the application after a forced stop.

**🔧Fix**: Sometimes SMS and email credits were shown incorrectly.

**🔧Fix**: In some cases, the number of devices per state was shown incorrectly.

**🔧Fix**: Probable fix for sending monitor alerts even with the device **.

**🔧Fix**: Monitor database would lock up when changing the server's host name.

**🔧Fix**: Disabled magnitude unit handling when editing a monitor.

**🔧Fix**: "Connected Clients" monitor of the Airmax AC and Ubiquiti - AirOS 5.6 templates did not display information.

**🔧Fix**: "Interface Errors" monitor of the Ubiquiti - Airmax AC template did not display the network interfaces.

**🔧Fix**: "Input Frequency" monitor of the Nobreak - Generic template had the maximum limit calculation wrong.

## Version 3.0.13

**✨New**: New templates available.

## Version 3.0.11

**✨New**: Users and restrictions for devices.

**✨New**: Device groups.

**✨New**: View by device groups.

**✨New**: Provided program to reset the admin user's password to the default at `/opt/monsta/bin/resetadmin`.

**🔧Fix**: The *Uptime* monitor does not allow viewing history older than 6 days.

**🔧Fix**: The cloud connection icon sometimes incorrectly appears as critical state.

**🔧Fix**: Cloud connection history is not recorded in the Timeline.

**🔧Fix**: In an existing monitor, cloning metrics whose description is a number causes the "Ok" button to not work.

**🔧Fix**: Process supervision mechanism does not properly control the automatic update process.

**🔧Fix**: In an existing monitor, a cloned metric copies the original's maximum value.

**🔧Fix**: The *uptime* monitor does not display information about the *Up* and *Down* states.

**🔧Fix**: Probable fix for monitor database corruption when Monsta is terminated.

**🔧Fix**: When a metric is deleted from a monitor, it does not appear on the graph but continues to be monitored.