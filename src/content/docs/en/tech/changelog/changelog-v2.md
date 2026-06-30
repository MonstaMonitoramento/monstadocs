---
title: "Changelog v2"
sidebar:
  order: 6
---

## Version 2.0.11

**🔧Fix**: Backup - During the restoration of a *backup*, Monsta could swap the names of the templates.

## Version 2.0.10

**✨New**: Tree view display - Changed the minimum value of the "Image Size" option to 5.

**🔧Fix**: Unable to add instances with descriptions that contain only numbers.

**🔧Fix**: After selecting a large time range to display on monitors with true/false metrics, Monsta shows everything as False.

**🔧Fix**: Under certain conditions Monsta shows a state change for a deleted device.

**🔧Fix**: When a parent device is in the "*Down*" state, Monsta may show its children in the "*Up*" state.

**🔧Fix**: When a new metric was added to an existing monitor, clicking OK would replace it with a copy of the previous metric.

## Version 2.0.6

**🔧Fix**: Under certain conditions Monsta may indicate the wrong state for a monitor.

## Version 2.0.5

**✨New**: New Visual Identity.

**✨New**: New Configuration screen with Templates, Images, *Backup* and Data Sources.

**✨New**: Option to add custom icons or images for templates, devices and monitors.

**✨New**: Access to monitor data sources.

**✨New**: New templates.

**✨New**: New graphical elements for dashboards.

**✨New**: Client for SQL queries on MySQL and SQLite databases.

**✨New**: Ability to add multiple monitors to a single chart.

**✨New**: Text monitors.

**✨New**: ICMP packet size editing.

**✨New**: New functions for scripts.

**✨New**: POP, IMAP and FTP checks with authentication.

**✨New**: String checking in text files.

**🔧Fix**: During activation Monsta did not accept the license key due to incorrect server time.

**🔧Fix**: Screen did not support more than 60 monitors per device.

**🔧Fix**: Monitors that did not contain a description `OID` in `SNMP` were not activated.

**🔧Fix**: Some monitors entered alert with the message "no value", even though they were active.