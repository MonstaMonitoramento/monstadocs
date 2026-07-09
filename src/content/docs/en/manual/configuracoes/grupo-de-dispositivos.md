---
title: "Device Group"
sidebar:
  order: 4
---

Monsta allows creating groups in which devices can be registered individually. Devices registered in a group inherit its configurations, such as users, passwords, SNMP data, and these override the global configurations.

Device groups are used to optimize routine tasks, such as applying configurations, granting a user visibility of which devices they have access to, or for a quick overview of the overall status of your registered devices.

![image-1739988728084.png](../../../../../assets/images/p65_image-1739988728084.png)

---

![image-1647884450145.png](../../../../../assets/images/p65_image-1647884450145.png)
**New device group**: Creates a new group.

---

![image-1739988753787.png](../../../../../assets/images/p65_image-1739988753787.png)
**Search groups**: Filters groups according to the entered text.

---

![image-1739988818350.png](../../../../../assets/images/p65_image-1739988818350.png)
**Group Box**: Shows the group name and a quick view of the number of registered devices and their statuses. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1739988847442.png](../../../../../assets/images/p65_image-1739988847442.png) | Shows the total number of devices registered in the group by status. |
| ![image-1739988866136.png](../../../../../assets/images/p65_image-1739988866136.png) | Displays the group's name. |
| ![image-1647884315767.png](../../../../../assets/images/p65_image-1647884315767.png) | Assigns actions that will be inherited by the group. For more information, see [Global Options](/en/manual/dispositivos/opcoes#opções-globais-de-dispositivos). |
| ![image-1647884360825.png](../../../../../assets/images/p65_image-1647884360825.png) | Adds a new device to the selected group. |
| ![image-1647884405279.png](../../../../../assets/images/p65_image-1647884405279.png) | Opens the group edit screen. |



## Add/Edit a device group

![image-1739988994615.png](../../../../../assets/images/p65_image-1739988994615.png)

### Details

Basic information about the group. 

| Option | Description |
| :---: | :--- |
| ![image-1739989016556.png](../../../../../assets/images/p65_image-1739989016556.png) | Allows selecting an icon for the group. |
| **Device group name** | Allows entering a name for the group being edited. |
| **Description** | A brief comment about the group being edited. |

### Members
These are the devices that are part of the group.


| Ícone | Descrição |
| :---: | :--- |
| ![image-1739989077427.png](../../../../../assets/images/p65_image-1739989077427.png) | List of group members. |
| ![image-1739989114437.png](../../../../../assets/images/p65_image-1739989114437.png) | Adds or removes selected members. |
| ![image-1739989148209.png](../../../../../assets/images/p65_image-1739989148209.png) | Adds or removes all members. |

### Collection
These are the settings for the main discovery methods that will be inherited by the devices that are part of the group. For more information, see [Collection](/en/manual/dispositivos/novo-dispositivo#coleta).

### Alert Sounds
Configures the alert sounds that will be inherited by the devices that are members of this group. For more information, see [Alert Sounds](/en/manual/dispositivos/novo-dispositivo#grupos-de-alerta).

### Sensitivity
Defines the uptime behavior for the devices that are members of this group. For more information, see [Sensitivity](/en/manual/dispositivos/opcoes#sensibilidade).