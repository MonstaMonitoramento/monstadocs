---
title: 'Probe: Windows Monitoring'
sidebar:
  order: 5
---

A **Monsta Probe** is a local data-collection software designed to be installed directly on **Windows, Linux and Raspberry PI** servers and devices. Its primary function is to collect performance, health and availability metrics from the host system, acting as a native collection extension for the Monsta platform.

## Features and Technical Capabilities

### 1. Passive Architecture (On-Demand)

The probe operates strictly under a **passive request-response model**. It does not initiate network communications autonomously; data traffic occurs only when Monsta contacts it to perform polling (collection request).

### 2. Integration with the WMI API (Windows)

In Microsoft environments, the probe natively uses the WMI (Windows Management Instrumentation) API, allowing it to extract detailed performance counters from servers and workstations without the need for complex remote management configurations on the network.

### 3. Execution of Commands and PowerShell Scripts

The probe acts as an automation agent directly on the host operating system.

- **Local Commands:** Can execute commands directly on the host operating system.
- **PowerShell Scripts:** Supports triggering custom scripts, enabling monitoring of specific applications or creating tailored validation routines.

### 4. Physical Disk Health Diagnostics

The software can read hardware indicators and the health status of HDDs and SSDs installed on the device. This enables early detection of physical failures (bad blocks) and storage degradation.

### 5. Encrypted Communication

All information exchanged between the Monsta central server and the Probe installed on the device is **100% encrypted**, ensuring the security of transmitted metrics and preventing interception of sensitive infrastructure data.

## Probe Installation

1. Download the probe program on the Windows operating system you want to monitor;

| [![Download](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) | [https://www.monsta.com.br/monsta/download/MonstaProbe.exe (64bits)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) |
| :---: | :--- |

2. Logged in as an administrator user, run the installer "monstaprobe.exe" (see [Command-line installation](#command-line-installation) for bulk installation);
3. Configure the port and password parameters that will be requested during installation.  

:::note
**port**: This is the port that will be used by the probe for Monsta to connect. The default is **7744** (TCP).  
**password**: This is the authentication password for the probe on the installed computer. The default is `monsta@dm`.
:::

## Configuration in Monsta

Within Monsta, when creating a device, just configure it to use the Microsoft templates.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

And fill the "Usuário WMI" field with any information (it will be discarded later) and the "Senha WMI" field with the password provided during the probe installation.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

After creating the device you can already use the available monitors from the template.

## Command-line installation

The MonstaProbe.exe installer accepts command-line options. You can use them to automate installation across a network via GPO, without the need to interact with the graphical interface.

| Opção &nbsp; &nbsp; &nbsp; &nbsp; | Descrição |
| --- | --- |
| `--agree` | Accepts the probe collector's terms of use. |
| `--port` | Specifies the port to be used by the probe collector. If not provided, the default will be 7744 (TCP). |
| `--passwd` | Assigns the password to be used by the probe collector. The default password will be *monsta@dm* if not provided. |

:::tip[Example usage]

```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```

:::