---
title: "Probe: Windows Monitoring"
sidebar:
  order: 5
---

Maximize efficiency and stability of your network with our WMI Monitoring Probe for Windows. Designed to provide a detailed view of the performance and health of your Windows servers and workstations, this essential tool collects crucial metrics via the WMI (Windows Management Instrumentation) API.

## What is the Probe for?

Imagine having an X-ray of your Windows environment in real time. Our probe works that way, allowing you to:

- Monitor system performance: Track CPU, RAM, disk and network usage to identify bottlenecks and optimize resources.
- Detect problems proactively: Receive alerts about critical events, service failures and other indicators of potential instabilities before they impact your users.
- Analyze resource consumption: Understand how applications and processes use system resources for smarter capacity planning.
- Visualize key data: Integrate the collected metrics with Monsta so you can create customized, detailed dashboards.
- Diagnose issues remotely: Get valuable information to resolve incidents quickly and efficiently, even without physical access to the machine.

**Seamless integration**: Specifically designed for the Windows environment, making full use of the WMI API capabilities.

**Lightweight and efficient**: Low resource consumption, ensuring monitoring does not impact the monitored system's performance.

**Easy installation** and configuration: A simple and intuitive process to get your probe running quickly.

**Accurate** and reliable data: Collects detailed, real-time information for precise analysis of your infrastructure.

**Flexibility**: Tailor metric collection to your specific needs.

With our WMI Monitoring Probe for Windows, you'll have full control over the health and performance of your Windows systems, ensuring a robust, efficient and always-available IT infrastructure. Start monitoring intelligently now!

## Probe Installation

1. Download the probe program on the Windows operating system you want to monitor;


| | |
| --- | --- |
| ![image-1660325708746.png](../../../../../assets/images/p139_image-1660325708746.png) | [**DOWNLOAD**](https://www.monsta.com.br/monsta/download/MonstaProbe.exe "Monsta - Collector Probe")<br />[https://www.monsta.com.br/monsta/download/MonstaProbe.exe (64bits)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) |
2. Logged in as an administrator user, run the installer "monstaprobe.exe" (see [Installation via the command line](#installation-via-the-command-line) for batch installation);
3. Configure the port and password parameters that will be requested during installation.  
      
    

:::note
**port**: This is the port that the probe will use for Monsta to connect. The default is **7744** (TCP).  
**password**: This is the authentication password for the probe on the installed computer. The default is `monsta@dm`.
:::



## Configuration in Monsta

Inside Monsta, when creating a device, simply configure it to use the Microsoft templates.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

And fill the "WMI User" field with any information (it will be discarded later) and the "WMI Password" field with the password provided during the probe installation.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

After creating the device you can start using the template's available monitors.

## Installation via the command line

The MonstaProbe.exe installer accepts command-line options. You can use them to automate installation across a network via a GPO, without the need for interaction with the graphical interface.

| Option &nbsp; &nbsp; &nbsp; &nbsp; | Description |
| --- | --- |
| `--agree` | Accepts the probe collector's terms of use. |
| `--port` | Specifies the port to be used by the probe collector. If not specified, the default will be 7744 (TCP). |
| `--passwd` | Sets the password to be used by the probe collector. The default password will be *monsta@dm* if not provided. |





:::tip[Usage example]
```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```
:::



- - - - - -