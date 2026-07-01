---
title: 'Agent: Zero-Conf Installation'
sidebar:
  order: 4
---

This documentation describes the operation and architecture of the **Monsta Agent**, a tool to extend the monitoring of your platform to remote and distributed networks, ensuring performance and security through the QUIC protocol.

## Agent Installation for Windows

- Download the agent program:

<table>
  <tr style="border: none; background: none;">
    <td style="border: none; padding-right: 15px; vertical-align: middle;">
      <a href="https://www.monsta.com.br/monsta/download/agent.msi">
        <img src="/src/assets/images/p139_image-1660325708746.png" alt="Download do Agente" />
      </a>
    </td>
    <td style="border: none; vertical-align: middle;">
      <a href="https://www.monsta.com.br/monsta/download/agent.msi">
        https://www.monsta.com.br/monsta/download/agent.msi
      </a>
    </td>
  </tr>
</table>

- Logged in as a user with administrator privileges, run the installer "agent.msi".
- When prompted, enter the Monsta license key to which you want to connect the agent.

## Command-line Installation

The installer **agent.msi** supports command-line parameters for automation. Integrated with the **msiexec** utility, it allows installation via **GPO**, eliminating the need for manual intervention in the graphical interface.

Command-line options:

| Option | Description |
| --- | --- |
| `LICENSEKEY=[chave de licença]` | Informs the license key to which the Agent should connect. <aside class="starlight-aside starlight-aside--tip"><p class="starlight-aside__title">Tip</p>The License key can be obtained in Monsta within the "Configuration" menu under the "Agents" option. It is shown in the top-right corner.</aside> |
| `AGREE=[Y]` | Confirms acceptance of the terms of use. |

**Example usage:**

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

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

To cover the entire remote network with a single agent, register the new devices in Monsta and set the device to be under the **hierarchy** of the host where the Agent is installed.

Example of Hierarchy:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##