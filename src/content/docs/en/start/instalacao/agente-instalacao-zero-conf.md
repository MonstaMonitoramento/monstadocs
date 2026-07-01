---
title: 'Agent: Zero Conf Installation'
sidebar:
  order: 4
---

This documentation describes the operation and architecture of the **Monsta Agent**, a tool to extend monitoring of your platform to remote and distributed networks, ensuring performance and security through the QUIC protocol.

## Agent Installation for Windows

- Download the agent program:

| &nbsp; | &nbsp; |
| --- | --- |
| ![image-1660325708746.png](../../../../../assets/images/p139_image-1660325708746.png) | [**DOWNLOAD**](http://www.monsta.com.br/monsta/download/agent.msi)<br />[https://monsta.com.br/downloads/](https://www.monsta.com.br/monsta/download/agent.msi) |

- Logged in with a user with administrator permissions, run the installer "agent.msi".
- When prompted, enter the Monsta license key for the Monsta instance to which you want to connect the agent.

## Installation via command line

The installer **agent.msi** supports command line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, eliminating the need for manual interaction with the graphical interface.

Command line options:

| &nbsp; | &nbsp; |
| --- | --- |
| `LICENSEKEY=\[license key\]` | Provides the license key the Agent should connect to. |
| `AGREE=\[Y\]` | Confirms acceptance of the terms of use. |

:::tip[Usage example]

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::

:::note
The License Key can be obtained in Monsta within the "Settings" menu under "Agents". It is shown in the top right corner.
:::

:::tip
**Firewall**:  

- It is not necessary to forward any ports to the Monsta server;  
- To ensure direct connections, open port **58580/UDP** (outbound) on your Monsta server's firewall to the Internet;  
- Allow the Monsta server to access the hosts mind.monsta.com.br and agent.monsta.com.br.
:::

## Device Creation

Once installation is complete, the **Agent** will appear automatically on the **Settings** screen under **Agents** with the host identification. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and adding new monitors.

### How to Monitor Devices via the Agent Connection

To cover the entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Hierarchy Example:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##