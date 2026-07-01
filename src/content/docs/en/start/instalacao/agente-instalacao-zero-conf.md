---
title: 'Agent: Zero-Conf Installation'
sidebar:
  order: 4
---

This documentation describes the operation and architecture of the **Monsta Agent**, a tool to extend monitoring of your platform to remote and distributed networks, ensuring performance and security through the QUIC protocol.

## Installing the Agent on Windows

- Download the agent program:
| - | Link to download |
| :---: | :--- |
| [![Agent Download](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/agent.msi) | <br>[https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi) |

- While logged in as a user with administrator permissions, run the installer "agent.msi".
- When prompted, enter the Monsta license key for the Monsta instance you want the agent to connect to.

## Command-line Installation

The **agent.msi** installer supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, removing the need for manual interaction with the graphical interface.

Command-line options:

| Option | Description |
| --- | --- |
| `LICENSEKEY=[license key]` | Specifies the license key that the Agent should connect to. <aside class="starlight-aside starlight-aside--tip"><p class="starlight-aside__title">Tip</p>The License key can be obtained in Monsta within the "Configuration" menu under the "Agents" option. It is shown in the top right corner.</aside> |
| `AGREE=[Y]` | Confirms acceptance of the terms of use. |

**Example usage:**

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::

:::tip
**Firewall**:  

- It is not necessary to forward any port to the Monsta server;  
- To ensure direct connections, open port **58580/UDP** (outbound) on your Monsta server firewall to the Internet;  
- Allow the Monsta server to access the hosts mind.monsta.com.br and agent.monsta.com.br.
:::

## Device Creation

Once installation is complete, the **Agent** will automatically appear in the **Configuration** screen under **Agents** with the host identification. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and addition of new monitors.

### How to Monitor Devices via the Agent Connection

To cover an entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Example Hierarchy:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##