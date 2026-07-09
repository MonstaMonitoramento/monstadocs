---
title: "Agent: Zero Conf Installation"
description: Learn how to install the Monsta Agent using Zero-Conf mode and automate the setup to start monitoring devices quickly.
sidebar:
  order: 4
---
This documentation describes the installation process for the **Monsta Agent**, a tool to extend monitoring of your platform to remote and distributed networks, ensuring performance and security through the QUIC protocol.

## Agent Installation for Windows

- Download the agent program:

|  |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| ![Agent Download](/src/assets/images/p139_image-1660325708746.png) | [https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi) |

- Logged in as a user with administrator privileges, run the installer "agent.msi".
- When prompted, enter the Monsta license key to which you want to connect the agent.

## Installation via the command line

The installer **agent.msi** supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, eliminating the need for manual intervention in the graphical interface.

Command-line options:

| Option | Description |
| ------------------------------- | --------------------------------------------------------------- |
| `LICENSEKEY=[license key]` | Specifies the license key to which the Agent should connect. |
| `AGREE=[Y]` | Confirms acceptance of the terms of use. |

**Example usage:**

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::tip

The License key can be obtained in Monsta within the "Configuration" menu under "Agents". It is displayed in the top right corner.

:::

## Device Creation

Once installation is complete, the **Agent** will automatically appear on the **Configuration** screen under **Agents** with the host identification. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and addition of new monitors.

### How to Monitor Devices via the Agent Connection

To cover the entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Hierarchy Example:

![image-1765385133049.png](/src/assets/images/p139_image-1765385133049.png)
