---
title: 'Agent: Zero-Conf Installation'
sidebar:
  order: 4
---

Esta documentação descreve o funcionamento e a arquitetura do **Monsta Agent**, uma ferramenta para estender o monitoramento da sua plataforma para redes remotas e distribuídas, garantindo performance e segurança por meio do protocolo QUIC.

## Agent Installation for Windows

- Download the agent program:

[![](../../../../../assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/agent.msi)
- [https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi)

- While logged in with a user with administrator permissions, run the "agent.msi" installer.
- When prompted, enter the Monsta license key to which you want to connect the agent.

## Command-line Installation

The **agent.msi** installer supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, eliminating the need for manual intervention in the graphical interface.

Command-line options:
|Opção|Descrição|
|---|---|
| `LICENSEKEY=\[license key\]` | Specifies the license key to which the Agent should connect. |
| `AGREE=\[Y\]` | Confirms acceptance of the terms of use. |

:::tip[Example usage]

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::

:::note
The License Key can be obtained in Monsta within the "Configuration" menu under the "Agents" option. It is shown in the top-right corner.
:::

:::tip
**Firewall**:  

- It is not necessary to forward any ports to the Monsta server;  
- To ensure direct connections, allow port **58580/UDP** (outbound) on your Monsta server firewall to the Internet;  
- Allow access from the Monsta server to the hosts mind.monsta.com.br and agent.monsta.com.br.
:::

## Device Creation

Once the installation is complete, the **Agent** will automatically appear on the **Configuration** screen under **Agents** with the host identification. The monitored device will be **created and listed instantly** on the **Devices** screen with the same host name and ready for configuration and addition of new monitors.

### How to Monitor Devices via the Agent Connection

To cover the entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Hierarchy Example:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)
