---
title: "Monsta Probe: Installation"
sidebar:
  order: 5
---
A **Monsta Probe** is a local collection software designed to be installed directly on **Windows** servers and devices (coming soon for **Linux** and **Raspberry PI**). Its main function is to collect performance, health and availability metrics from the host system, acting as a native collection extension for the Monsta platform.

## Features and Technical Capabilities

### 1. Passive Architecture (On-Demand)

The probe strictly operates under a **passive request-and-response** model. It does not initiate network communications autonomously; data traffic only occurs when Monsta contacts it to perform *polling* (collection request).

### 2. Integration with the WMI API (Windows)

In Microsoft environments, the probe natively uses the WMI API (*Windows Management Instrumentation*), allowing extraction of detailed performance counters from servers and workstations without the need for complex remote management configurations on the network.

### 3. Execution of PowerShell Commands and Scripts

The probe acts as an automation arm directly on the host operating system.

- **Local Commands:** Can execute commands directly on the host operating system.
- **PowerShell Scripts:** Supports triggering custom scripts, allowing monitoring of specific applications or creating tailored validation routines.

### 4. Physical Disk Health Diagnostics

The software is capable of reading hardware indicators and the health status of hard drives and SSDs installed on the device. This enables early identification of physical failures (*bad blocks*) and storage degradation.

### 5. Encrypted Communication

All information exchanged between the central Monsta server and the Probe installed on the device is **100% encrypted**, ensuring the security of the metrics transmitted and preventing interception of sensitive infrastructure data.

## Probe Installation (Windows)

1. Download the probe program on the Windows operating system you want to monitor;


|  | Download |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [![Download da Sonda](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) | [https://www.monsta.com.br/monsta/download/MonstaProbe.exe](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) |

2. Logged in as an administrator user, run the installer "monstaprobe.exe" (see [Command-line installation](#instalação-pela-linha-de-comando) for batch installation);
3. Configure the port and password parameters that will be requested during installation.

**Instalação pela linha de comando**

O instalador MonstaProbe.exe aceita opções na linha de comando. Você pode utilizá-las para automatizar a instalação em uma rede através de uma GPO, sem necessidade de interação com a interface gráfica.


| Opção &nbsp; &nbsp; &nbsp; &nbsp; | Descrição |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `--agree` | Aceita o termo de uso da sonda coletora. |
| `--port` | Informa a porta a ser utilizada pela sonda coletora. Se não for informada, o padrão será 7743 (TCP). |
| `--passwd` | Atribui a senha a ser utilizada pela sonda coletora. A senha padrão será *monsta@dm* caso não seja informada. |


**Exemplo de uso**

```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```

:::note
**port**: É a porta que será utilizada pela sonda para o Monsta conectar. O padrão é **7743** (TCP).  
**password**: É a senha de autenticação para a sonda no computador instalado. O padrão é `monsta@dm`.
:::

**Configuration in Monsta**

Inside Monsta, when creating a device, simply configure it to use the Microsoft templates.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

And fill the "WMI User" field with any information (it will be discarded later) and the "WMI Password" field with the password provided during the probe installation.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

After creating the device you can now use the monitors available in the template.