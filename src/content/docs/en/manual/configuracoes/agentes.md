---
title: "Agents"
sidebar:
  order: 3
---

The Monsta Tecnologia Monitoring Agent enables managing complex, distributed IT infrastructures, ensuring that monitoring is efficient, secure, and does not overload your wide area network (WAN). The Agent is cross-platform; its installation is quick and straightforward in any IT environment, and it is compatible with the main operating systems: Windows and Linux (including the most popular distributions).

## How Does the Monsta Agent Work?

The Monsta Agent acts as a Distributed Monitoring Proxy for your branches and remote networks. Monitor assets centrally and securely, eliminating the complexity of port forwarding, VPNs, or the requirement for fixed/static IPs.

## Architectural Benefits



| **Feature** | **Description** |
| --- | --- |
| **Local Collection** | The Agent is installed on the remote network and collects data from all devices *locally*. |
| **Consolidated Communication** | It **aggregates and temporarily stores** metrics before sending them to the central Monsta Server in a single stream. |
| **Optimized Security** | Only the Agent needs to open communication with the central server, requiring fewer firewall rules and reducing the attack surface. |
| **Fault Tolerance** | In case of temporary WAN connection loss, the Agent continues collecting and storing data (caching), ensuring that no information is lost. |



## Agent Management and Distributed Monitoring

![image-1768997185306.png](../../../../../assets/images/p63_image-1768997185306.png)

| Icon | Description |
| :---: | :--- |
| ![image-1647867281671.png](../../../../../assets/images/p63_image-1647867281671.png) | **Search**: Use the filter field to locate specific agents. As you type, the list will update automatically to display only the results that match the entered text. |
| ![image-1768997246532.png](../../../../../assets/images/p63_image-1768997246532.png) | **Available agent licenses**: This field indicates the number of agents available in your subscription. If you need to monitor more devices, you can access the customer area on our website and add as many licenses as needed to your plan. |
| ![image-1768998008744.png](../../../../../assets/images/p63_image-1768998008744.png) | **Total agents**: Number of agents configured and occupying a license slot. |
| ![image-1768999817872.png](../../../../../assets/images/p63_image-1768999817872.png) | **Sorting**: The arrows allow reordering the agents list. This order defines the priority for using your purchased licenses: agents placed above your quota limit will be monitored, while excess agents will remain on standby. |
| ![image-1768998685081.png](../../../../../assets/images/p63_image-1768998685081.png) | **Status**: Indicates the current condition of each device on the network:<br /><br />• **Connected**: The agent is active and communicating normally with the server.<br />• **Disconnected**: The agent is offline or communication was lost.<br />• **Limit Exceeded**: The agent was installed but is not being monitored because your plan's license quota has been reached.<br />• **Blocked**: The agent's communication is blocked. |
| ![image-1768998876264.png](../../../../../assets/images/p63_image-1768998876264.png) | **Device**: Displays information about the Operating System where the agent is running. |
| ![image-1768999021483.png](../../../../../assets/images/p63_image-1768999021483.png) | **Connection**: For connected agents only, this field indicates the communication route.<br /><br />• **Direct**: The agent communicates directly with the server.<br />• **Hybrid**: The agent uses an intermediate server (Proxy) to bypass firewall restrictions or network isolation. |
| ![image-1768999216633.png](../../../../../assets/images/p63_image-1768999216633.png) | **Version**: Indicates the current version of the agent installed on the host. This field is automatically managed by the system: whenever a new update is released, Monsta will perform the upgrade automatically, ensuring you always have the latest features and fixes without manual intervention. |
| ![image-1768999398371.png](../../../../../assets/images/p63_image-1768999398371.png) | **Last activity**: Records the exact date and time of the last communication received from the agent. It is the main indicator to verify whether monitoring is occurring in real time. |
| ![image-1768999481044.png](../../../../../assets/images/p63_image-1768999481044.png) | **Block agent**: Allows you to manually stop or resume communication for a specific agent. When blocked, the agent stops sending data to the server but remains installed and configured, and can be reactivated at any time with a click. |
| ![image-1768999732028.png](../../../../../assets/images/p63_image-1768999732028.png) | **Delete agent**: Permanently removes the agent from your monitoring list.<br />**Note**: For security reasons, this action is only allowed for agents with the **Disconnected** status. If the agent is still active, you must stop the service on the host before deletion. |


:::caution[Attention]
Agent support is available starting with Monsta version **6**.
:::