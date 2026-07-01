---
title: 'Agent: Zero-Conf Installation'
sidebar:
  order: 4
---

This documentation describes the operation and architecture of the **Monsta Agent**, a tool to extend monitoring of your platform to remote and distributed networks, ensuring performance and security through the QUIC protocol.

## Installing the Agent on Windows

- Download the agent program:

| ![image-1660325708746.png](../../../../../assets/images/p139_image-1660325708746.png) | [**DOWNLOAD**](http://www.monsta.com.br/monsta/download/agent.msi)<br />[https://monsta.com.br/downloads/](https://www.monsta.com.br/monsta/download/agent.msi) |

- Logged in as a user with administrator permissions, run the "agent.msi" installer.
- When prompted, enter the Monsta license key to which you want the agent to connect.

## Command-line Installation

The **agent.msi** installer supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, removing the need for manual interaction with the graphical interface.

Command-line options:

| `LICENSEKEY=\[license key\]` | Provides the license key to which the Agent should connect. |
| `AGREE=\[Y\]` | Confirms acceptance of the terms of use. |

:::tip[Usage example]

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::

:::note
The License Key can be obtained in Monsta under the "Configuration" menu in the "Agents" option. It is shown in the upper-right corner.
:::

:::tip
**Firewall**:  

- It is not necessary to forward any port to the Monsta server;  
- To ensure direct connections, allow port **58580/UDP** (outbound) on your Monsta server firewall to the Internet;  
- Allow the Monsta server access to the hosts mind.monsta.com.br and agent.monsta.com.br.
:::

## Device Creation

Once installation is complete, the **Agent** will automatically appear on the **Configuration** screen under **Agents** with the host identification. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and addition of new monitors.

### How to Monitor Devices via the Agent Connection

To cover an entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Hierarchy Example:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##