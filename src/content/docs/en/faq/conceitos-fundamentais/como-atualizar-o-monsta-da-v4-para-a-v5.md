---
title: "How to upgrade Monsta from v4 to v5?"
---

A **version 5 (v5)** of Monsta represents a complete overhaul of the system core, offering new features and greater efficiency compared to the previous version (v4).

## Why upgrade?

Support for v4 has been **discontinued** with the release of v5. Keeping Monsta outdated can cause critical compatibility and operational issues:

- **License Validation**: v4 is not compatible with the new subscription model. To apply or renew the license, Monsta must be on v5.
- **Template Import**: New templates requested from support are always provided in the **latest official version**. v5 templates **cannot be imported** into v4 due to file incompatibility.

It is essential to upgrade your Monsta to v5 to ensure continuity and validity of your monitoring.

If your Monsta does not show the new update under **Settings &gt; Update**, an error may have occurred preventing detection. Follow the steps below to try to resolve the issue.

## (Optional) Full backup

The upgrade process is **safe** and does not affect the monitoring history database (graphs). However, for maximum data preservation assurance, we recommend a **full backup**. The cloud backup only saves Monsta settings.

## Full Backup Options

1. **Virtual Machine (VM)**: If Monsta is installed on Linux inside a VM, the simplest method is to create a full clone of the virtual machine.
2. **Physical Server or Manual Backup**: If it is not possible to clone the VM or the installation is on a physical server, follow these steps:
    1. Check your Monsta version under **Settings &gt; About Monsta**
    2. Stop Monsta:   
        **\#v4.1.18 or lower**  
        `service monsta stop`  
        **\#4.1.19**  
        `systemctl stop monsta-com.*`
    3. With Monsta stopped, copy the folders: `/var/monsta` and `/opt/monsta`

## Checking the logs

A known issue that can block the update is a failure in Linux log rotation, resulting in an excessive accumulation of `monstadb` log files that overload the server.

1. Go to Monsta's log directory:  
    `cd /var/log/monsta`
2. Check the number of `monstadb` logs:  
    \- Run the command to count the monstadb log files. If there are **hundreds/thousands** of files, correction is needed. Note: You can also use the `ls -la` command to view the directory files.  
    `ls -la monstadb.log* | wc -l`
3. Stop the Monsta service (use the appropriate command according to the version, as described in item 2.2 of the Full Backup section.)
4. Delete the `monstadb.log` files:  
    `rm -f monstadb.log.*`  
    `rm -f monstadb.log-*`  
    Note: if the "argument list too long" error occurs on the `rm -f monstadb.log.*` command, use the following command:  
    `printf '%s\0' monstadb.log.* | xargs -0 rm -v`
5. Use `ls -la` to verify that the files have been removed
6. Start Monsta again  
    **\#v4.1.18 or lower**  
    `service monsta start`
    
    **\#V4.1.19**  
    `systemctl start monsta-com.nginx`  
    `systemctl start monsta-com.monstadb`  
    `systemctl start monsta-com.monstad`  
    `systemctl start monsta-com.moncored`  
    `systemctl start monsta-com.monagentd`  
    `systemctl start monsta-com.monstaupd`

## Upgrading

After starting the services, access the Monsta web interface and check if the update is available. Depending on your current version (e.g. 4.1.16 or 4.1.18), Monsta may first update to 4.1.19 (which will cause a restart) and then allow the final update to v5.

Follow the progress in real time via the log:

`tail -f /var/log/monstaupd.log`

(use `Ctrl + C` to stop the `tail` command)

:::tip
During the upgrade, the web interface screen may **not refresh automatically**. After a few minutes, try accessing your Monsta address again to view the login screen.
:::

## No log issues and the update still doesn't appear

If fixing the logs does not resolve the issue and the update to v5 does not appear, please contact **support**. Our specialists will analyze the root cause. **Access to your Monsta web interface and Linux will be requested** so the team can diagnose and resolve the issue directly.