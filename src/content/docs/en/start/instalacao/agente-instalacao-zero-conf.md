---
title: 'Agent: Zero-Conf Installation'
sidebar:
  order: 4
---

This documentation describes the operation and architecture of the **Monsta Agent**, a tool to extend the monitoring of your platform to remote and distributed networks, ensuring performance and security through the QUIC protocol.

## Installing the Agent on Windows

- Download the agent program:

[![](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/agent.msi)[https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi)

- While logged in as a user with administrator privileges, run the "agent.msi" installer.
- When prompted, enter the Monsta license key for the Monsta instance you want the agent to connect to.

## Installation via command line

The **agent.msi** installer supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, eliminating the need for manual intervention in the graphical interface.

Command line options:

| Opção | Descrição |
| --- | --- |
| `LICENSEKEY=\[license key\]` | Specifies the license key that the Agent should connect to. \n\n:::note\nThe License Key can be obtained in Monsta within the "Configuration" menu under "Agents". It is shown in the upper right corner.\n::: |
| `AGREE=\[Y\]` | Confirms acceptance of the terms of use. |

:::tip[Usage example]

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::

:::tip
**Firewall**:  

- It is not necessary to forward any ports to the Monsta server;  
- To ensure direct connections, allow port **58580/UDP** (outbound) on your Monsta server firewall to the Internet;  
- Allow the Monsta server access to the hosts mind.monsta.com.br and agent.monsta.com.br.
:::

## Creating the Device

Once installation is complete, the **Agent** will automatically appear on the **Configuration** screen under **Agents** with the host identifier. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and the addition of new monitors.

### How to Monitor Devices via the Agent Connection

To cover the entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Hierarchy example:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##