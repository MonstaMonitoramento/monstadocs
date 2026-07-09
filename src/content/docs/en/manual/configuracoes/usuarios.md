---
title: "Users"
sidebar:
  order: 9
---

Monsta is multi-user, meaning it allows multiple users to be used simultaneously in the system with custom permissions. Monsta's user management system allows specifying which devices, groups, dashboards or alert groups can be viewed and managed by each member.

![image-1647888175595.png](../../../../../assets/images/p66_image-1647888175595.png)

| Icon / Option | Description |
| :---: | :--- |
| ![image-1647888202156.png](../../../../../assets/images/p66_image-1647888202156.png) | Adds a new user to access the platform. |
| **Admin** | When checked, indicates that the user in the list has administrator permissions and access to all devices, monitors and available resources. |
| **Login** | This is the login name for Monsta. |
| **Name** | User's name. |
| ![image-1647888352963.png](../../../../../assets/images/p66_image-1647888352963.png) | Edits the selected user's properties. |
| ![image-1647888388977.png](../../../../../assets/images/p66_image-1647888388977.png) | Clones the current user's properties to a new one. |
| ![image-1647888449977.png](../../../../../assets/images/p66_image-1647888449977.png) | Removes the selected user. |



## Create/Edit a User

### Details
These are the user's basic information. 

| Option | Description |
| :--- | :--- |
| **Login** | The user's login name. Cannot be changed for existing users. |
| **Full Name** | The user's full name information. |
| **Change Password** | Allows changing the password of the user being edited. |
| ![image-1647888733932.png](../../../../../assets/images/p66_image-1647888733932.png) | **Administrator**: Assigns administrator properties when enabled. The user will have access to all devices, monitors and resources available in Monsta. <aside class="starlight-aside starlight-aside--note">When a user is not an administrator, the hierarchical view will not be available to them.</aside> |


### Devices
Allows the administrator to specify exactly which devices a specific user can view and manage in the system.

| Icon / Option | Description |
| :--- | :--- |
| ![image-1647889770987.png](../../../../../assets/images/p66_image-1647889770987.png) | **Write**: The user receives write (modification) permissions. They will be able to:<br />• Modify and Remove Devices;<br />• Add, Edit and Remove Monitors (services/metrics) on existing devices.<br /><br />When unchecked, the user can only view data. No changes are allowed to the device list, monitors, or their settings. |
| ![image-1739989429159.png](../../../../../assets/images/p66_image-1739989429159.png) | **Device Filter**: Filters devices by the entered text. |
| ![image-1739989466314.png](../../../../../assets/images/p66_image-1739989466314.png) | **Device List**: The left column lists all devices being monitored by Monsta. The right column lists the devices the user will be able to view and interact with. These are the assets the user will access. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Individual Selection Buttons**: Moves the selected devices between the columns of the device list. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Bulk Selection Buttons**: Moves all devices from one column to the other in the device list. |



### Groups
Configures the groups whose member devices the user will have access to.



| Icon / Option | Description |
| :--- | :--- |
| ![image-1739989584199.png](../../../../../assets/images/p66_image-1739989584199.png) | **Device Group List**: The left column lists all groups registered in Monsta. The right column lists the groups the user will have access to. Devices belonging to that group will be listed in the "Devices" tab, in the right column, marked as read-only. |
| ![image-1739989429159.png](../../../../../assets/images/p66_image-1739989429159.png) | **Device Group Filter**: Filters groups by the entered text. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Individual Selection Buttons**: Moves the selected groups between the columns of the device groups list. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Bulk Selection Buttons**: Moves all groups from one column to the other in the device groups list. |



### Alert Groups
Configures the alert groups that the user will have access to.

| Icon / Option | Description |
| :--- | :--- |
| ![image-1647889770987.png](../../../../../assets/images/p66_image-1647889770987.png) | **Write**: The user receives write (modification) permissions. They will be able to: Alert.<br /><br />When unchecked, the user can only view data. No changes are allowed in the alert groups. |
| ![image-1739989663950.png](../../../../../assets/images/p66_image-1739989663950.png) | **Alert Group Filter**: Filters groups by the entered text. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Individual Selection Buttons**: Moves the selected groups between the columns of the alert groups list. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Bulk Selection Buttons**: Moves all groups from one column to the other in the alert groups list. |