---
title: "Monsta Probe: Installation"
description: Learn how to install the Monsta Probe on Windows to perform remote
  monitoring and extend the platform's reach within your infrastructure.
sidebar:
  order: 5
---
A **Monsta Probe** is a local collection software designed to be installed directly on **Windows** servers and devices (coming soon for **Linux** and **Raspberry PI**). Its main function is to collect performance, health and availability metrics of the host system, acting as a native collection extension for the Monsta platform.

## Technical Features and Capabilities

### 1. Passive Architecture (On Demand)

The probe operates strictly under a **passive request-and-response** model. It does not initiate network communications autonomously; data traffic occurs only when Monsta contacts it to perform polling.

### 2. Integration with the WMI (Windows) API

In Microsoft environments, the probe natively uses the WMI (*Windows Management Instrumentation*) API, allowing extraction of detailed performance counters from servers and workstations without the need for complex remote management network configurations.

### 3. Execution of Commands and PowerShell Scripts

The probe acts as an automation arm directly on the host operating system.

- **Local Commands**: It can execute commands directly on the host operating system.
- **PowerShell Scripts**: Supports triggering custom scripts, allowing monitoring of specific applications or creating tailored validation routines.

### 4. Physical Disk Health Diagnostics

The software can read hardware indicators and the health status of HDDs and SSDs installed on the device. This enables early identification of physical failures (*bad blocks*) and storage degradation.

### 5. Encrypted Communication

All information exchanged between the Monsta central server and the Probe installed on the device is **100% encrypted**, ensuring the security of transmitted metrics and preventing interception of sensitive infrastructure data.

## Probe Installation (Windows)

1. Download the probe program on the Windows operating system you want to monitor;


|  | Download |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ![Download da Sonda](/src/assets/images/p139_image-1660325708746.png) | [https://www.monsta.com.br/monsta/download/MonstaProbe.msi](https://www.monsta.com.br/monsta/download/MonstaProbe.msi) |


1. Logged in with an administrator user, run the installer "monstaprobe.msi";
2. Configure the port and password parameters that will be requested during installation.

### Command-line Installation

The MonstaProbe installer accepts options on the command line. You can use them to automate installation across a network via GPO, without the need for interaction with the graphical interface.


| Option &nbsp; &nbsp; &nbsp; &nbsp; | Description |
| ---------------------------------- | -------------------------------------------------------------------------------------------- |
| `AGREE=Y` | Accepts the probe's terms of use. |
| `PORT=<num>` | Specifies the port to be used by the probe. If not provided, the default will be 7743 (TCP). |
| `PASSWD=<password>` | Assigns the password to be used by the probe. |
| `REMOTE_EXEC=1` | Enables execution of commands and PowerShell scripts. Use 1 to enable or 0 to disable. |


**Example**:

```powershell
msiexec /i MonstaProbe.msi /qn AGREE=Y PORT=7743 PASSWD=MinhaSenha REMOTE_EXEC=1
```

### Commands to change configuration

The probe parameters can be adjusted via the command line.


| Option &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Description |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `--cfg` | Indicates that the configuration will be changed. |
| `--port` | Redefines the port the probe should listen on. |
| `--passwd` | Redefines the password. |
| `--remote-exec 1` | Sets whether execution of PowerShell commands and scripts is enabled. Use **1** to enable and **0** to disable. |


**Example**:

```powershell
"C:\Program Files (x86)\MonstaProbe\monsta_probe.exe" --cfg --port 7744 --passwd NovaSenha --remote-exec 1
```

### Remote Script Execution: Security and Permissions

Execution of PowerShell commands and scripts through the Monsta Probe is performed under the exclusive context of the local user **monsta-probe**. This user is automatically created during the installation process and operates strictly with standard user permissions, ensuring that all services, tasks and scripts triggered by the platform run in isolation, without administrator privileges or access to sensitive operating system files.

### Configuration in Monsta

Within Monsta, when creating a device, simply configure it to use the Microsoft templates.

![image-1741105397485.png](/src/assets/images/p68_image-1741105397485.png)

And fill the "WMI User" field with any information (it will be discarded later) and the "WMI Password" field with the password provided during the probe installation.

![image-1741105450183.png](/src/assets/images/p68_image-1741105450183.png)

After creating the device you can already use the monitors available in the template.