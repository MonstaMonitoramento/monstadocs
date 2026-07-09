---
title: "New Device"
sidebar:
  order: 6
---

By clicking the "New" button you can add a device to Monsta monitoring.

## Details

Sets the basic information about the device.

![image-1739970776422.png](../../../../../assets/images/p51_image-1739970776422.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1646855537251.png](../../../../../assets/images/p51_image-1646855537251.png) | **Icon**: Allows selecting an icon for the device. |
| ![image-1646855610278.png](../../../../../assets/images/p51_image-1646855610278.png) | **Device name**: This will be the name displayed in the view modes. |
| ![image-1646855698393.png](../../../../../assets/images/p51_image-1646855698393.png) | **Device address**: The IPv4 address, IPv6 or host of the device. It is possible to ping the address to test it. |
| ![image-1646855946392.png](../../../../../assets/images/p51_image-1646855946392.png) | **Device description**: Allows entering a short text about the equipment. |
| ![image-1646856003694.png](../../../../../assets/images/p51_image-1646856003694.png) | **Agent**: Location where the device's collections will be triggered. This information is read-only. |
| ![image-1646856167964.png](../../../../../assets/images/p51_image-1646856167964.png) | **Uptime monitor**: Method used to identify whether the device is active. The default is sending ICMP echo-request (ping) packets. Verification methods may allow some parameters to be specified for queries, such as the size of the ICMP packet to be sent or the TCP port to be checked on the device. |
| ![image-1732555718867.png](../../../../../assets/images/p51_image-1732555718867.png) | **Sensitivity**: Sets the device's sensitivity level for ping (ICMP) packets. For more information, see the [Sensitivity](/en/manual/dispositivos/opcoes#sensitivity) page. |



## Templates

These are the monitors available for each equipment type. Each template has specific monitors to be used, and more than one template can be used on a device.

![image-1646856297549.png](../../../../../assets/images/p51_image-1646856297549.png)

| Opção | Descrição |
| :--- | :--- |
| **Selecionados** | Templates used on this device. |
| **Usado frequentemente** | A list of the most used templates in your Monsta, which allows quicker selection. |
| **Todos** | A list of all templates available in Monsta. |



## Parent

Defines the asset's hierarchical dependency. Used to organize the network map and optimize the notification system by relating devices to their dependencies.

:::caution[Important]
This information will be used by the alert sending system so that Monsta sends a notification only for the device that has a problem.
:::



![image-1769000388348.png](../../../../../assets/images/p51_image-1769000388348.png)

## Collection

This screen shows the main methods for retrieving information from devices used by Monsta. Its main functionality is to allow the user to use a standard configuration for the monitors used and to test whether the communication is functional.

![image-1739970973988.png](../../../../../assets/images/p51_image-1739970973988.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1739971005493.png](../../../../../assets/images/p51_image-1739971005493.png) | **Collection methods**: These are the default collection types performed by Monsta. By clicking on these methods it is possible to configure general parameters that will be used by the device monitors. To collect data from Windows Servers and Workstations, use the Sonda. For more information, see our tutorial [Probe: Windows Monitoring](/en/start/instalacao/sonda-windows). |
| ![image-1646915286768.png](../../../../../assets/images/p51_image-1646915286768.png) | **Inherit from Group or Global**: This property, when checked, obtains the values configured globally or from the group to which the device belongs. For more information see [Global device options](/en/manual/dispositivos/opcoes#global-device-options). |
| ![image-1646913740044.png](../../../../../assets/images/p51_image-1646913740044.png) | **Property**: Allows changing the value of this collection property. If the "Inherit value from group or global" option is checked, this property will inherit the configured value. |
| ![image-1732556926759.png](../../../../../assets/images/p51_image-1732556926759.png) | **Exponential**: When available, uses a timeout algorithm for collection. This algorithm doubles the timeout time after each failed collection, starting at 1 second. |
| ![image-1739971041554.png](../../../../../assets/images/p51_image-1739971041554.png) | **Test**: When available, allows testing whether the device responds to the configured parameters. |



## Groups

Devices in Monsta can be part of groups and inherit their configurations. On this screen it is possible to view the groups to which the device belongs and to add others. To add groups, see Device Groups.

![image-1732557160475.png](../../../../../assets/images/p51_image-1732557160475.png)

| Ícone | Descrição |
| :---: | :--- |
| ![image-1732557200808.png](../../../../../assets/images/p51_image-1732557200808.png) | **Group name**: Indicates the group to which the device belongs. |
| ![image-1646919486747.png](../../../../../assets/images/p51_image-1646919486747.png) | **Add group**: Allows adding a new group to which the device will belong. |
| ![image-1646919524906.png](../../../../../assets/images/p51_image-1646919524906.png) | **Remove group**: Removes the device from the selected group. |



## Alerts

Monsta has the ability to play sounds when a device or monitor changes state. On this screen you can customize the sounds individually for the device in focus.

![image-1732557243546.png](../../../../../assets/images/p51_image-1732557243546.png)

### Alert Groups

Alert groups are used to send messages when a device or monitor changes state. These groups can be customized for each device or monitor or specific sounds can be assigned for the device in focus. For more information about alert groups, see [Alerts](/en/manual/grupos-alertas/alertas).

![image-1739971123424.png](../../../../../assets/images/p51_image-1739971123424.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1732557441016.png](../../../../../assets/images/p51_image-1732557441016.png) | **Notify alert groups**: Enables/disables the sending of alerts for the selected device. |
| ![image-1732557452354.png](../../../../../assets/images/p51_image-1732557452354.png) | **Select**: Indicates the alert group to which the device belongs. |
| ![image-1646919486747.png](../../../../../assets/images/p51_image-1646919486747.png) | **Add alert group**: Allows adding a new alert group to which the device will belong. |
| ![image-1646919524906.png](../../../../../assets/images/p51_image-1646919524906.png) | **Remove alert group**: Removes the device from the selected alert group. |
| ![image-1732557653598.png](../../../../../assets/images/p51_image-1732557653598.png) | **Alert sounds**: Allows selecting a specific sound for each state of the device. |