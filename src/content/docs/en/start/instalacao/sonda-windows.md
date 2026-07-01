---
title: 'Probe: Windows Monitoring'
sidebar:
  order: 5
---

A **Monsta Probe** is a local collection software designed to be installed directly on **Windows, Linux and Raspberry PI** servers and devices. Its main function is to collect performance, health and availability metrics from the host system, acting as a native collection extension for the Monsta platform.

## Features and Technical Capabilities

### 1. Passive Architecture (On Demand)

The probe operates strictly under a **passive request-response** model. It does not initiate network communications autonomously; data traffic occurs only when Monsta contacts it to perform polling (collection request).

### 2. Integration with the WMI API (Windows)

In Microsoft environments, the probe natively uses the WMI (Windows Management Instrumentation) API, allowing extraction of detailed performance counters from servers and workstations without the need for complex remote management configurations on the network.

### 3. Execution of PowerShell Commands and Scripts

The probe acts as an automation arm directly on the host operating system.

- **Local Commands:** It can execute commands directly on the host operating system.
- **PowerShell Scripts:** It supports triggering custom scripts, allowing monitoring of specific applications or creating tailored validation routines.

### 4. Physical Disk Health Diagnostics

The software is capable of reading hardware indicators and the integrity status of HDDs and SSDs installed on the device. This enables early identification of physical failures (bad blocks) and storage degradation.

### 5. Encrypted Communication

All information exchanged between the Monsta central server and the Probe installed on the device is **100% encrypted**, ensuring the security of transmitted metrics and preventing interception of sensitive infrastructure data.

## Probe Installation

1. Download the probe program on the Windows operating system you want to monitor;

|                                                                                                                                                         | Download                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| <a href="https://www.monsta.com.br/monsta/download/MonstaProbe.exe">![Download da Sonda](../../../../../assets/images/p139_image-1660325708746.png)</a> | [https://www.monsta.com.br/monsta/download/MonstaProbe.exe](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) |

1. Logged in as an administrator, run the installer "monstaprobe.exe" (see [Installation via command line](#instalação-pela-linha-de-comando) for batch installation);
2. Configure the port and password parameters that will be requested during installation.

## Instalação pela linha de comando

The MonstaProbe.exe installer accepts command line options. You can use them to automate installation across a network via GPO, without the need to interact with the graphical interface.

| Option              | Description                                                                                                        |
| :------------------ | :----------------------------------------------------------------------------------------------------------------- |
| `--agree`           | Accepts the probe collector's terms of use.                                                                        |
| `--port`            | Specifies the port to be used by the probe collector. If not provided, the default will be 7744 (TCP).             |
| `--passwd`          | Assigns the password to be used by the probe collector. The default password will be *monsta\@dm* if not provided. |

**Example**

```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```

## Configuration in Monsta

Inside Monsta, when creating a device, just configure it to use the Microsoft templates.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

And fill the "WMI User" field with any information (it will be discarded later) and the "WMI Password" field with the password provided during the probe installation.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

After creating the device you can already use the monitors available in the template.

##
