---
title: 'Agent: Zero-Conf Installation'
sidebar:
  order: 4
---

This documentation describes the operation and architecture of the **Monsta Agent**, a tool to extend monitoring of your platform to remote and distributed networks, ensuring performance and security through the QUIC protocol.

## Installing the Agent on Windows

- Download the agent program:

|  | Link to download |
| --- | --- |
| [![Agent Download](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/agent.msi) | [https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi) |

- Logged in as a user with administrator privileges, run the installer "agent.msi".
- When prompted, enter the Monsta license key to which you want the agent to connect.

## Command-Line Installation

The **agent.msi** installer supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, eliminating the need for manual GUI intervention.

Command-line options:

| Option | Description |
| --- | --- |
| `LICENSEKEY=[chave de licença]` | Specifies the license key the Agent should connect to. <aside class="starlight-aside starlight-aside--tip"><p class="starlight-aside__title">Tip</p>The License Key can be obtained in Monsta under the "Configuration" menu in the "Agents" option. It is shown in the upper-right corner.</aside> |
| `AGREE=[Y]` | Confirms acceptance of the terms of use. |

**Example usage:**

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::tip
**Firewall**:  

- It is not necessary to forward any ports to the Monsta server;  
- To ensure direct connections, open port **58580/UDP** (outbound) on your Monsta server firewall to the Internet;  
- Allow the Monsta server access to the hosts mind.monsta.com.br and agent.monsta.com.br.
:::

## Device Creation

Once the installation is complete, the **Agent** will automatically appear in the **Configuration** screen under **Agents** with the host identification. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and addition of new monitors.

### How to Monitor Devices via the Agent Connection

To cover an entire remote network with a single agent, register new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Example of Hierarchy:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##