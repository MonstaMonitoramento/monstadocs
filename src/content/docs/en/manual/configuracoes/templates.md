---
title: "Templates"
sidebar:
  order: 2
---

A template is the set of resources that can be monitored on a device. Each vendor provides its own resources per equipment.

## Templates

![image-1647448202544.png](../../../../../assets/images/p61_image-1647448202544.png)

---

![image-1647448799678.png](../../../../../assets/images/p61_image-1647448799678.png)
**Import Templates**: Allows selecting a template file to import. 

---

![image-1647448005833.png](../../../../../assets/images/p61_image-1647448005833.png)
**Search Filter**: When used, displays only the templates that contain this text in their name.

---

![image-1647448121838.png](../../../../../assets/images/p61_image-1647448121838.png)
**New Template**: Creates a new template. See [Create/Edit a Template](#createedit-a-template) for more information.

---

![image-1647448227188.png](../../../../../assets/images/p61_image-1647448227188.png)
**Template List**: Displays a list of all templates available in the system.

---

![image-1739983220633.png](../../../../../assets/images/p61_image-1739983220633.png)
**Template Box**: Visual presentation of the template. Clicking it redirects the user to its monitors screen. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1647448422172.png](../../../../../assets/images/p61_image-1647448422172.png) | **Remove**: Removes the highlighted template. |
| ![image-1647448460969.png](../../../../../assets/images/p61_image-1647448460969.png) | **Edit**: Edits the template properties, such as name, description and icon. |

<a id="criareditar-um-template"></a>
### Create/Edit a Template

![image-1647450145680.png](../../../../../assets/images/p61_image-1647450145680.png)

| Option | Description |
| :---: | :--- |
| ![image-1647450183069.png](../../../../../assets/images/p61_image-1647450183069.png) | **Template Icon**: Allows selecting an icon for the template from an existing library or from a new image. |
| **Name** | Name given to the template. |
| **Description** | A brief description about the template. |

## Monitors

Monitors are system components that check a specific resource on a device and return its current status. They are the ones that generate information and alert about possible anomalies.

![image-1739984216883.png](../../../../../assets/images/p61_image-1739984216883.png)

---

---

![image-1739984247217.png](../../../../../assets/images/p61_image-1739984247217.png)
**Template Name**: Displays the name of the highlighted template.

---

![image-1739984391202.png](../../../../../assets/images/p61_image-1739984391202.png)
**Export**: Exports the selected monitors to a file.

---

![image-1739984511244.png](../../../../../assets/images/p61_image-1739984511244.png)
**Edit Template**: Edits the template properties, such as name, description and icon.

---

![image-1647449193273.png](../../../../../assets/images/p61_image-1647449193273.png)
**Search Filter**: When used, displays only the monitors that contain this text in their name.

---

![image-1647449307274.png](../../../../../assets/images/p61_image-1647449307274.png)
**New Monitor**: Creates a new monitor for the highlighted template. For more information, see xxxxxxx.

---

![image-1647449372287.png](../../../../../assets/images/p61_image-1647449372287.png)
**Monitor List**: Displays a list of all monitors available for the highlighted template. Clicking a monitor allows editing it. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1647449752980.png](../../../../../assets/images/p61_image-1647449752980.png) | **Clone**: Clones the monitor to a selected template. |
| ![image-1647449785056.png](../../../../../assets/images/p61_image-1647449785056.png) | **Remove**: Removes the selected monitor. | 


### Create/Edit a Monitor

#### Monitor

On this screen the basic information about the monitor is configured.

![image-1769000706570.png](../../../../../assets/images/p61_image-1769000706570.png)

| Option | Description |
| :---: | :--- |
| ![image-1739984579878.png](../../../../../assets/images/p61_image-1739984579878.png) | **Icon**: Allows selecting an icon for the template from an existing library or from a new image and also serves as a preview of how the monitor will be displayed on the screen. |
| **Short Name** | Information about the monitor that is shown on the devices screen icon. |
| **Name** | Information about the monitor that is shown on the templates screen. |
| **Description** | A brief information about the monitor. This text will be displayed when hovering the mouse over a device's monitors. |
| **Check Interval** | Selects the monitor's check interval. <aside class="starlight-aside starlight-aside--caution">If this value is greater than 59 seconds, when a metric leaves the normal state the check interval will automatically change to every 1 minute.</aside> |
| **Number of Attempts** | Number of checks that will be made after the monitor's value exceeds its normal limit before changing its state. |
| ![image-1769000749924.png](../../../../../assets/images/p61_image-1769000749924.png) | When editing a monitor and clicking this button, the system allows replicating the changes to other devices simultaneously. After clicking, select from the list the devices that should receive the new configuration. |



#### Instances

On this screen the listing method for resource instances is specified, such as the list of network interfaces of a device.

![image-1739984753223.png](../../../../../assets/images/p61_image-1739984753223.png)

| Option | Description |
| :---: | :--- |
| ![image-1647535774368.png](../../../../../assets/images/p61_image-1647535774368.png) | **Enable Instances**: Enables instance selection for the monitor. |
| ![image-1647535820722.png](../../../../../assets/images/p61_image-1647535820722.png) | Search method used to find the instances. |
| **Fix OID** | When disabled, Monsta checks if the instance name remains at the same OID. The following situations may occur:<br />- **Same OID**: Monsta collects the values in the same position;<br />- **Different OID**: Monsta discovers the new OID and will collect the values in the new position;<br />When enabled, Monsta will always collect the information at the same position, regardless of whether the instance changed OID. |
| **OIDDesc and Name** | This option allows the monitor to automatically identify multiple components of the same device (such as different network interfaces, disks, or partitions). The system uses **Monsta Studio** scripts to list these items. In the parameters, you define the desired properties (like OIDs or filters) to extract exactly the data that will be shown in the selection list. |



### Metrics

On this screen the method of collecting the device resources is configured.

![image-1769002820448.png](../../../../../assets/images/p61_image-1769002820448.png)

---

![image-1647537210606.png](../../../../../assets/images/p61_image-1647537210606.png)
**Metric**: Displays the name of the metric and its position on the chart. The top metric in the list has its chart overlaid by the lower metric. 

| Ícone | Descrição |
| :---: | :--- |
![image-1647537418530.png](../../../../../assets/images/p61_image-1647537418530.png) | **Ordering**: Toggles the metric's position to be drawn on the chart. | 
![image-1647537403522.png](../../../../../assets/images/p61_image-1647537403522.png) | **Remove**: Removes the selected metric. | 

---

![image-1647537518634.png](../../../../../assets/images/p61_image-1647537518634.png)
**Add**: Adds a new metric.

---

![image-1647537560886.png](../../../../../assets/images/p61_image-1647537560886.png)
**Data Source for Value**: Configures how the metric's data is collected. This is the value that will be plotted on the chart.

---

![image-1647538051533.png](../../../../../assets/images/p61_image-1647538051533.png)
**Data Source for Maximum Value**: Method to obtain the metric's maximum value. This value will be used to calculate the percentage applied to alert thresholds.

---

![image-1647538111673.png](../../../../../assets/images/p61_image-1647538111673.png)
**Color**: Color of the metric that will be shown when accessing its chart.

---

![image-1647538237011.png](../../../../../assets/images/p61_image-1647538237011.png)
**Name**: Name of the metric that will be shown when accessing its chart.

---

![image-1739986248546.png](../../../../../assets/images/p61_image-1739986248546.png)
**Unit**: Unit of measurement of the metric.

---

![image-1647538419774.png](../../../../../assets/images/p61_image-1647538419774.png)
**Fill**: Allows selecting whether the metric's chart should be filled. When this option is not selected the metric's chart will only present a line for the readings.

---

![image-1647538571119.png](../../../../../assets/images/p61_image-1647538571119.png)
**Value Type**: Indicates the type of value the metric returns. Choosing this property defines the type of chart that will be displayed.

---

![image-1739986284648.png](../../../../../assets/images/p61_image-1739986284648.png)
**Disable Thresholds**: Disables thresholds for the metric. When this option is enabled the metric's state will always be "Normal" and it will never be alarmed.

---

![image-1647539136617.png](../../../../../assets/images/p61_image-1647539136617.png)
**Alert Threshold Percentage**: In monitors that have a defined maximum value, the percentage bar is displayed. It allows quickly viewing and setting the thresholds defined for the metric states.

:::note
Available when a maximum value is configured.
:::

| Option | Description |
| :---: | :--- |
| ![image-1647539259537.png](../../../../../assets/images/p61_image-1647539259537.png) | **Invert**: Inverts the alert percentage. By default a lower value will be considered better. |
| ![image-1647539419645.png](../../../../../assets/images/p61_image-1647539419645.png) | **Percentage Bar**: Allows visually configuring the alert thresholds. Drag the selectors to determine the usage percentages that trigger the "Warning" and "Critical" states. |
| ![image-1647539324004.png](../../../../../assets/images/p61_image-1647539324004.png) | **Percentage Values**: Below the percentage bar, the system displays the exact numeric value corresponding to the marker positions. |

---

![image-1647539661996.png](../../../../../assets/images/p61_image-1647539661996.png)
**Alert Threshold Values**: In monitors without a predefined maximum value, the user is free to manually provide numeric values for the **Warning** and **Critical** states.

:::note
Available when no maximum value is configured.
:::

| Option | Description |
| :---: | :--- |
| ![image-1647539740732.png](../../../../../assets/images/p61_image-1647539740732.png) | **Warning Value**: Defines the condition for the metric to enter the warning state. |
| ![image-1647539844543.png](../../../../../assets/images/p61_image-1647539844543.png) | **Critical Value**: Defines the condition for the metric to enter the critical state. |

---


![image-1739986395801.png](../../../../../assets/images/p61_image-1739986395801.png)
**Data Source**: Allows selecting an existing collection source and, if necessary, filling in the values requested by it.

| Option | Description |
| :---: | :--- |
| ![image-1647540152635.png](../../../../../assets/images/p61_image-1647540152635.png) | **Test Button**: Tests the source against a selected device. |
| ![image-1647540263038.png](../../../../../assets/images/p61_image-1647540263038.png) | **Remove Button**: Removes the data source from the highlighted value. |
| **Collector** | **Collector Field**: Selects the method that will be used to collect the monitor's data. |
| **Parameters** | **Parameters Field**: Allows entering data for the selected parameters. Parameters with a "*" next to them indicate that filling them in when adding a monitor will be mandatory. |

---

![image-1647539918188.png](../../../../../assets/images/p61_image-1647539918188.png)
**Custom Scripts**: Allows selecting the data source for collection. On this screen it is possible to use scripts in the LUA language for metrics.

| Option | Description |
| :---: | :--- |
| ![image-1647540152635.png](../../../../../assets/images/p61_image-1647540152635.png) | **Test Button**: Tests the script against a selected device. |
| ![image-1647540263038.png](../../../../../assets/images/p61_image-1647540263038.png) | **Remove Button**: Removes the data source from the highlighted value. |
| **Open in Editor** | **Open in Editor Button**: Opens an advanced development editor for the script. |

---

### Parameters

On this screen it is possible to create parameters with predefined values to be used by metrics' data sources. This option is useful when a monitor has multiple metrics that use the same information, such as a username and password for authentication, for example.

![image-1739986497220.png](../../../../../assets/images/p61_image-1739986497220.png)

| Option | Description |
| :---: | :--- |
| ![image-1739986525205.png](../../../../../assets/images/p61_image-1739986525205.png) | **Name**: Defines a name for the parameter. |
| ![image-1739986588973.png](../../../../../assets/images/p61_image-1739986588973.png) | **Type**: The type of information the parameter should receive. The "Option" type will bring a list coming from the "Instances" tab. |
| ![image-1739986692649.png](../../../../../assets/images/p61_image-1739986692649.png) | **Default Value**: Sets a default value for the parameter when creating the monitor. This option is not available for the "Option" type. |
| ![image-1739986788958.png](../../../../../assets/images/p61_image-1739986788958.png) | **Field Description**: The text that will be shown to the user when adding monitors to devices. |
| ![image-1647546204637.png](../../../../../assets/images/p61_image-1647546204637.png) | **Required Field Option**: Requires the parameter to have some value. Empty fields are not allowed. |
| ![image-1647546282966.png](../../../../../assets/images/p61_image-1647546282966.png) | **Repeatable Field Option**: Allows the user to insert the same field multiple times with different values. |
| ![image-1647546340415.png](../../../../../assets/images/p61_image-1647546340415.png) | **Position**: Toggles the parameter's position in the listing. |
| ![image-1647546392820.png](../../../../../assets/images/p61_image-1647546392820.png) | **Remove Button**: Removes the selected parameter. |


:::caution[Important]
When creating or customizing a monitor, if the type is an option and the selected method is "Scripts", the return must be a table with the following format:

`local ret = { display = "Text", instanceId = "value" }`

- Make sure that `instanceId` is unique (no duplicates).
- Name the variable as `exec.instance`. This enables reuse in **automatic monitors** and **metric cloning**.
:::

:::danger[Attention]
The mandatory use of the variable name `exec.instance` is a prerequisite for automation. If another name is used, **automatic monitors will not work correctly** and **metric cloning will be unavailable**.
:::

Example:

```lua
local opts = {
    host = "192.168.1.1",
    username = "user",
    password = "password",
    command = "ls /backup/*.sql"
}
local ret = {}

local list = string.split(ssh.exec(opts),"\n")

for i, arq in pairs(list)
do
  local name = string.split(arq,"//")[2]
  table.insert(ret,{display=name,instanceId=i})
end

return ret
```