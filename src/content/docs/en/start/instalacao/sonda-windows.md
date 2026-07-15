---
title: "Monsta Probe: Installation"
description: Learn how to install the Monsta Probe on Windows to perform remote monitoring and extend the platform's reach across your infrastructure.
sidebar:
  order: 5
---
A **Monsta Probe** is an on-host collection software designed to be installed directly on **Windows** servers and devices (coming soon for **Linux** and **Raspberry PI**). Its main function is to collect performance, health, and availability metrics from the host system, acting as a native collection extension for the Monsta platform.

## Features and Technical Capabilities

### 1. Passive Architecture (On Demand)

The probe operates strictly under a **passive request-and-response** model. It does not initiate network communications autonomously; data traffic occurs only when Monsta contacts it to perform polling (collection request).

### 2. Integration with the WMI API (Windows)

In Microsoft environments, the probe natively utilizes the WMI (*Windows Management Instrumentation*) API, allowing extraction of detailed performance counters from servers and workstations without the need for complex remote management configurations on the network.

### 3. Execution of PowerShell Commands and Scripts

The probe acts as an automation agent directly on the host operating system.

- **Local Commands:** It can execute commands directly on the host operating system.
- **PowerShell Scripts:** It supports triggering custom scripts, allowing monitoring of specific applications or creating tailored validation routines.

### 4. Physical Disk Health Diagnostics

The software can read hardware indicators and the health status of HDDs and SSDs installed on the device. This enables early detection of physical failures (*bad blocks*) and storage degradation.

### 5. Encrypted Communication

All information exchanged between the Monsta central server and the Probe installed on the device is **100% encrypted**, ensuring the security of transmitted metrics and preventing interception of sensitive infrastructure data.

## Probe Installation (Windows)

1. Download the probe program on the Windows system you want to monitor;


|  | Download |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ![Probe Download](/src/assets/images/p139_image-1660325708746.png) | [https://www.monsta.com.br/monsta/download/MonstaProbe.msi](https://www.monsta.com.br/monsta/download/MonstaProbe.msi) |


1. Logged in with an administrator user, run the installer "monstaprobe.msi";
2. Configure the port and password parameters that will be requested during installation.

### Command-line Installation

The MonstaProbe.exe installer accepts options on the command line. You can use them to automate installation across a network via GPO, without the need for interaction with the graphical interface.


| Opção &nbsp; &nbsp; &nbsp; &nbsp; | Descrição |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `AGREE=Y` | Accepts the probe collector's terms of use. |
| `PORT=<num>` | Specifies the port to be used by the probe collector. If not provided, the default will be 7743 (TCP). |
| `PASSWD=<password>` | Sets the password to be used by the probe collector. |
| `REMOTE_EXEC=1` | Enables execution of commands and PowerShell scripts. |


**Exemplo de uso**:

```powershell
msiexec /i MonstaProbe.msi /qn AGREE=Y PORT=7743 PASSWD=MinhaSenha REMOTE_EXEC=1
```

### Commands to Change Configuration

Probe parameters can be adjusted via the command line.


| Opção | Descrição |
| ----------------- | ----------------------------------------------------- |
| `--cfg` | Indicates that the configuration will be changed. |
| `--port` | Redefines the port the probe should listen on. |
| `--passwd` | Redefines the password. |
| `--remote-exec 1` | Enables execution of PowerShell commands and scripts. |


**Exemplo de uso**:

```powershell
"C:\Program Files (x86)\MonstaProbe\monsta_probe.exe" --cfg --port 7744 --passwd NovaSenha --remote-exec 1
```

### Remote Script Execution: Security and Permissions

Execution of commands and PowerShell scripts through the Monsta Probe is performed under the exclusive context of the local user **monsta-probe**. This user is automatically created during installation and operates strictly with standard user permissions, ensuring that all services, tasks, and scripts triggered by the platform run in isolation, without administrator privileges or access to sensitive operating system files.

### Configuration in Monsta

Within Monsta, when creating a device, simply configure it to use the Microsoft templates.

![image-1741105397485.png](/src/assets/images/p68_image-1741105397485.png)

And fill the "WMI User" field with any information (it will be discarded later) and the "WMI Password" field with the password provided during probe installation.

![image-1741105450183.png](/src/assets/images/p68_image-1741105450183.png)

After creating the device you can use the monitors available in the template.