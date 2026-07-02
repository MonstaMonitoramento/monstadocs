---
title: "Agent: Zero-Conf Installation"
sidebar:
  order: 4
---
This documentation describes the operation and architecture of the **Monsta Agent**, a tool to extend monitoring of your platform to remote and distributed networks, ensuring performance and security via the QUIC protocol.

## Installing the Agent on Windows

- Download the agent program:


|  | Download |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| ![Agent Download](../../../../../assets/images/p139_image-1660325708746.png) | [https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi) |


- While logged in as a user with administrator privileges, run the installer "agent.msi".
- When prompted, enter the Monsta license key to which you want to connect the agent.

## Command-line Installation

The **agent.msi** installer supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, eliminating the need for manual intervention in the graphical interface.

Command-line options:


| Option | Description |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LICENSEKEY=[chave de licença]` | Specifies the license key the Agent should connect to. Tip: The License Key can be obtained in Monsta under the "Configuration" menu in the "Agents" option. It is shown in the upper right corner. |
| `AGREE=[Y]` | Confirms acceptance of the terms of use. |


**Example usage:**

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

## Creating the Device

Once the installation is complete, the **Agent** will automatically appear on the **Configuration** screen under **Agents** with the host identification. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and the addition of new monitors.

### How to Monitor Devices via the Agent Connection

To cover the entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Example Hierarchy:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)