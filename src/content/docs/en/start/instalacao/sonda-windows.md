---
title: 'Probe: Windows Monitoring'
sidebar:
  order: 5
---

A **Monsta Probe** is local collection software designed to be installed directly on **Windows, Linux and Raspberry Pi** servers and devices. Its main function is to collect performance, integrity and availability metrics of the host system, acting as a native collection extension for the Monsta platform.

## Features and Technical Capabilities

### 1. Passive Architecture (On Demand)

The probe strictly operates under a **passive request-and-response** model. It does not initiate communications on the network autonomously; data traffic occurs only when Monsta contacts it to perform polling (_polling_).

### 2. Integration with the WMI API (Windows)

In Microsoft environments, the probe natively uses the WMI (_Windows Management Instrumentation_) API, allowing extraction of detailed performance counters from servers and workstations without the need for complex remote management configurations on the network.

### 3. Execution of PowerShell Commands and Scripts

The probe acts as an automation arm directly on the host operating system.

- **Local Commands:** It can execute commands directly on the host operating system.
- **PowerShell Scripts:** It supports triggering custom scripts, allowing monitoring of specific applications or creating tailored validation routines.

### 4. Physical Disk Health Diagnostics

The software can read hardware indicators and the health status of hard drives and SSDs installed on the device. This enables early identification of physical failures (bad blocks) and storage degradation.

### 5. Encrypted Communication

All information exchanged between the Monsta central server and the Probe installed on the device is **100% encrypted**, ensuring the security of transmitted metrics and preventing interception of sensitive infrastructure data.

## Probe Installation

1. Download the probe program on the Windows operating system you want to monitor;

[![](/src/assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe)

[https://www.monsta.com.br/monsta/download/MonstaProbe.exe](https://www.monsta.com.br/monsta/download/MonstaProbe.exe)

2. Logged in as an administrator user, run the installer "monstaprobe.exe" (see [Instalação pela linha de comando](#instalação-pela-linha-de-comando) for bulk installation);
3. Configure the port and password parameters that will be requested during installation.  

## Instalação pela linha de comando

The MonstaProbe.exe installer accepts command line options. You can use them to automate installation across a network via GPO, without needing interaction with the graphical interface.

| Opção | Descrição |
| --- | --- |
| `--agree` | Accepts the probe collector's terms of use. |
| `--port` | Specifies the port to be used by the probe collector. If not provided, the default will be 7744 (TCP). |
| `--passwd` | Sets the password to be used by the probe collector. The default password will be *monsta@dm* if not provided. |

:::tip[Example usage]

```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```

:::

:::note
**port**: Is the port that will be used by the probe for Monsta to connect. The default is **7744** (TCP).  
**password**: Is the authentication password for the probe on the installed computer. The default is `monsta@dm`.
:::

## Configuration in Monsta

Inside Monsta, when creating a device, simply configure it to use the Microsoft templates.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

And fill the "WMI User" field with any information (it will be discarded later) and the "WMI Password" field with the password provided during probe installation.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

After creating the device you can use the template's available monitors.

##