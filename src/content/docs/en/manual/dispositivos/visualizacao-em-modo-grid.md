---
title: "Grid View"
sidebar:
  order: 2
---

On the grid view screen devices are displayed as boxes that show the state the equipment is in and a summary of their respective monitors.

:::note
**Device**: Equipment with at least one IP address on the network.
:::



## Device Box

![image-1646920930381.png](../../../../../assets/images/p55_image-1646920930381.png)

| Information | Description |
| :---: | :--- |
| ![image-1646920980786.png](../../../../../assets/images/p55_image-1646920980786.png) | **Name**: Displays the device name. |
| ![image-1646921003457.png](../../../../../assets/images/p55_image-1646921003457.png) | **Address**: Displays the device address. |
| ![image-1646921020039.png](../../../../../assets/images/p55_image-1646921020039.png) | **Detailed view**: Opens the selected device in a new screen with a more detailed view of its monitoring. |
| ![image-1646921058196.png](../../../../../assets/images/p55_image-1646921058196.png) | **Actions**: Processes that can be triggered against the highlighted device. |
| ![image-1646921073359.png](../../../../../assets/images/p55_image-1646921073359.png) | **Edit**: Edits the device properties. For more information, see: [New Device](/en/manual/dispositivos/novo-dispositivo). |



- - - - - -

## Device View

In this tab you can view the device status and edit information about the device and its monitors, as well as access monitoring graphs.

![image-1756130572475.png](../../../../../assets/images/p55_image-1756130572475.png)


| Icon | Description |
| :---: | :--- |
| ![image-1646941577966.png](../../../../../assets/images/p55_image-1646941577966.png) | **Enable / Disable**: Allows enabling or disabling monitoring of the selected device. |
| ![image-1646941614267.png](../../../../../assets/images/p55_image-1646941614267.png) | **Detailed view**: Switches to the device view mode with a summary of information. |
| ![image-1732625167859.png](../../../../../assets/images/p55_image-1732625167859.png) | **Timeline**: Opens the timeline of the selected device. For more information, see: [Timeline](/en/manual/linha-tempo/linha-do-tempo). |
| ![image-1646941719105.png](../../../../../assets/images/p55_image-1646941719105.png) | **Edit**: Edits the properties of the selected device. |
| ![image-1646941777433.png](../../../../../assets/images/p55_image-1646941777433.png) | **Delete**: Deletes the selected device and its monitors. |
| ![image-1646941797055.png](../../../../../assets/images/p55_image-1646941797055.png) | **Clone**: Creates a copy of the selected device and its monitors. |
| ![image-1646941813782.png](../../../../../assets/images/p55_image-1646941813782.png) | **Automatic Monitors**: Opens the rule editor to create monitors automatically for the device. For more information see [Automatic Monitors](/en/manual/dispositivos/monitores-automaticos). |
| ![image-1756130607601.png](../../../../../assets/images/p55_image-1756130607601.png) | **Map View**: Opens the map with the filter activated for the highlighted device. For more information see [Map View](/en/manual/dispositivos/visualizacao-em-mapa). |
| ![image-1646941865563.png](../../../../../assets/images/p55_image-1646941865563.png) | **Add Monitor**: Adds one or more monitors to the selected device. |
| ![image-1732625538788.png](../../../../../assets/images/p55_image-1732625538788.png) | **Monitors**: By clicking on their icons, their corresponding data are shown on the screen. |
| ![image-1646942048013.png](../../../../../assets/images/p55_image-1646942048013.png) | **Filter Monitors**: Shows only the monitors that contain the filter words on the screen. |
| ![image-1646942182734.png](../../../../../assets/images/p55_image-1646942182734.png) | **Filter by State**: Shows only the monitors with the selected states on the screen. |
| ![image-1739971953866.png](../../../../../assets/images/p55_image-1739971953866.png) | **Running Metrics**: Shows the number of metrics currently running against the selected device and its maximum limit. |
| ![image-1732625517650.png](../../../../../assets/images/p55_image-1732625517650.png) | **Summary**: Clicking this item will open a new window with a summarized view of all device monitors.<br />![image-1732625598475.png](../../../../../assets/images/p55_image-1732625598475.png) |

- - - - - -

## Monitors

For more information about monitors, see [Monitor View](/en/manual/dispositivos/visualizacao-de-monitores).

### Add Monitors

![image-1732639335704.png](../../../../../assets/images/p55_image-1732639335704.png)
By clicking the + button in the device menu, it will be possible to select a way to add monitors.

![image-1732639306380.png](../../../../../assets/images/p55_image-1732639306380.png)

| Icon | Description |
| :---: | :--- |
| ![image-1732639606113.png](../../../../../assets/images/p55_image-1732639606113.png) | Displays a screen with monitors related to the highlighted template. When selecting a monitor, it is possible to select the instance to be collected or change the name to be displayed on the monitor icon.<br /><br />![image-1732639931855.png](../../../../../assets/images/p55_image-1732639931855.png) **Description**: Displays a summary of the icon, name and description of the selected monitor.<br /><br />![image-1732640005940.png](../../../../../assets/images/p55_image-1732640005940.png) **Short name**: This is the name that will be displayed on the monitor icon. A preview is shown to the side.<br /><br />![image-1739973171292.png](../../../../../assets/images/p55_image-1739973171292.png) **Parameters**: Allows providing data, when requested, to the monitor, such as the name of the network interface to be monitored.<br /><br />![image-1732640246016.png](../../../../../assets/images/p55_image-1732640246016.png) **Customize**: Edits monitor properties. For more information, see: [Edit/Customize a Monitor](/en/manual/dispositivos/visualizacao-de-monitores#editarcustomizar-um-monitor). |
| ![image-1732640369424.png](../../../../../assets/images/p55_image-1732640369424.png) | This option allows adding multiple monitors at once to the device.<br /><br />![image-1732640714231.png](../../../../../assets/images/p55_image-1732640714231.png) **Template**: Tab for selecting the template. Once a template is selected, its monitors will appear on the right side of the screen. <br /><br />![image-1732640799469.png](../../../../../assets/images/p55_image-1732640799469.png) **Monitor**: When checked, tells Monsta that this monitor should be added to the device.<br /><br />![image-1732640902457.png](../../../../../assets/images/p55_image-1732640902457.png) Parameters: Provides a parameter to the monitor to be used when creating the monitor, when necessary, for example, the network interface to be monitored on the device.<br /><br />![image-1732640990927.png](../../../../../assets/images/p55_image-1732640990927.png) **Add monitor**: Repeats the selected monitor below to allow adding multiple monitors of the same type.<br /><br />![image-1732641077298.png](../../../../../assets/images/p55_image-1732641077298.png) **Editor**: Allows changing monitor information before adding it. For more information, see: [Edit/Customize a Monitor](/en/manual/dispositivos/visualizacao-de-monitores#editarcustomizar-um-monitor). |
| ![image-1732641453798.png](../../../../../assets/images/p55_image-1732641453798.png) | **Custom Monitors**: Allows adding a custom monitor. This feature is useful to create monitors that will be used only by one device. For more information, see: [Edit/Customize a Monitor](/en/manual/dispositivos/visualizacao-de-monitores#editarcustomizar-um-monitor). |

### Automatic Monitors

Monsta has the ability to automatically identify and add new instances to monitoring, such as network cards, hard drives and other devices. This functionality saves time and avoids the need to configure them manually.

How it works: The system performs periodic scans on the device searching for new instances. When it finds one that has not been added to monitoring and is compatible with the filters, it is automatically added with the default settings.

Settings: You can customize the scan frequency, the types of monitors to look for and a word filter to be analyzed.

Example: When a new network card is connected to a server, Monsta will automatically detect it and add it to monitoring, allowing you to track its performance in real time.

![image-1732642591751.png](../../../../../assets/images/p55_image-1732642591751.png)


| Icon | Description |
| :---: | :--- |
| ![image-1732642765286.png](../../../../../assets/images/p55_image-1732642765286.png) | **Monitor**: The type of search Monsta should perform for new instances. |
| ![image-1732642783014.png](../../../../../assets/images/p55_image-1732642783014.png) | **Instance filter**: Searches only for instances that contain the characters entered in the filter and ignores the others. |
| ![image-1732642861815.png](../../../../../assets/images/p55_image-1732642861815.png) | **Frequency**: Time configured for Monsta to search for and add new instances on the device. |
| ![image-1732642933956.png](../../../../../assets/images/p55_image-1732642933956.png) | **Remove monitors**: Monitors in a failed state, that is, whose instance no longer exists, will be removed after the selected period.<aside class="starlight-aside starlight-aside--caution">Do not confuse with monitors in a critical state, whose reading occurs but the values are outside their normal limits.</aside> |
| ![image-1732643125055.png](../../../../../assets/images/p55_image-1732643125055.png) | **Properties**: Allows customizing the properties below for all monitors created by the rule:<br />- Icon;<br />- Metric names;<br />- Alert thresholds;<br />- Check frequency;<br />- Number of attempts. |
| ![image-1732643318174.png](../../../../../assets/images/p55_image-1732643318174.png) | **Add rule**: Adds a new rule below the current one. |
| ![image-1732643371764.png](../../../../../assets/images/p55_image-1732643371764.png) | **Remove rule**: Removes the selected rule. <aside class="starlight-aside starlight-aside--danger">When removing an automatic monitor rule, all monitors created by it will also be removed, along with their respective histories.</aside> |