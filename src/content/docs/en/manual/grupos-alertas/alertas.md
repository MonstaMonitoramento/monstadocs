---
title: "Alert Groups"
---

![image-1756129907740.png](../../../../../assets/images/p37_image-1756129907740.png)

:::caution[Attention]
This feature requires the Monsta software to have communication with the host mind.monsta.com.br.
:::

:::tip
The alerts screen allows working with groups where the contacts that should receive the notifications when a device or monitor changes its “status” are specified.
:::

## Groups

This screen manages the user groups that will receive notifications and the service type, whether by email or SMS.

| Opção | Descrição |
| :---: | :--- |
| ![image-1645792155732.png](../../../../../assets/images/p37_image-1645792155732.png) | **New Group**: Creates a new group for sending alerts. |
| ![image-1645792160782.png](../../../../../assets/images/p37_image-1645792160782.png) | **Search Group**: Displays on the screen only the groups that match the entered search. |
| ![image-1756129930291.png](../../../../../assets/images/p37_image-1756129930291.png) | **Cloud Group**: This group sends alerts in case of loss of communication between Monsta and the cloud at [https://mind.monsta.com.br](https://mind.monsta.com.br). This feature is very useful in cases such as an internet link outage at the company or an unexpected server shutdown without the user's knowledge. This group cannot be removed from the system and is not available for devices or monitors.<br />The color of its border indicates the connection status with the cloud:<br />- **Green**: Communication established;<br />- **Red**: Communication failure. |
| ![image-1756129950105.png](../../../../../assets/images/p37_image-1756129950105.png) | **Default Group**: This group is mandatory in the system and cannot be deleted, only modified. The number shown in the upper right corner of the group box refers to the number of devices that use it in their alerts. When the group box is displayed in gray, it indicates that it has no alerts enabled. |
| ![image-1732710101229.png](../../../../../assets/images/p37_image-1732710101229.png) | **Active alerts**: The icons presented inside the group box indicate which alerts are currently active for it. |
| ![image-1732710190977.png](../../../../../assets/images/p37_image-1732710190977.png) | **Delete Group**: Deletes the selected group. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Attention</p>It will only be allowed to remove a group when it is not part of any device or monitor. You can obtain this information on the [Membros](#membros) tab when editing the group.</aside> |
| ![image-1645792184443.png](../../../../../assets/images/p37_image-1645792184443.png) | **Edit Group**: In this option the user can add and remove devices and monitors that are part of this group, as well as define the types of alerts that will be sent, their recipients and the allowed sending times for the messages. |



### Editing alert groups

#### Details

In this tab the icon, name and comment about the group are defined.

![image-1732711113493.png](../../../../../assets/images/p37_image-1732711113493.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1732710589288.png](../../../../../assets/images/p37_image-1732710589288.png) | It is possible to assign an image to the alert group that will be displayed on screen. |
| **Alert group name** | This is the name that will be shown on the groups screen, as well as what will be displayed when editing the alert groups option within devices or monitors. |
| **Description** | Allows adding a comment about the highlighted group. |

#### Membros  


In this tab it is possible to view the devices and monitors that will receive alerts from this group, as well as add new devices or remove existing ones.

![image-1739974572520.png](../../../../../assets/images/p37_image-1739974572520.png)

| Opção | Descrição |
| :---: | :--- |
| **All** | This component shows all the devices existing in Monsta. Click on a device to select it and use the buttons on the side to add it to the group. |
| **Selected** | This component shows the devices and monitors that are part of the highlighted group. Click on an item to select it and use the buttons on the side to remove it from the group. |



#### Monsta Alerts  


This tab shows Monsta's default alerts that use our cloud to be sent to recipients. The available sending options are Email, SMS and Telegram. Monsta Alerts do not require special configurations as they are automatically integrated with the cloud during software installation. 

![image-1732712034593.png](../../../../../assets/images/p37_image-1732712034593.png) 
To facilitate visualization, active alerts are marked with the icon above in their tab.


![image-1732711910237.png](../../../../../assets/images/p37_image-1732711910237.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1732712383308.png](../../../../../assets/images/p37_image-1732712383308.png) | Activates or deactivates the alert type in focus. |
| ![image-1732712469323.png](../../../../../assets/images/p37_image-1732712469323.png) | Sends a test to the existing recipients. This option is useful to verify if all destinations are configured correctly, such as email address, SMS or Telegram users. |
| ![image-1732712594374.png](../../../../../assets/images/p37_image-1732712594374.png) | These options allow selecting the type of event for which the alert should be sent. When unchecked, Monsta will not trigger for the selected status. |
| ![image-1732712693761.png](../../../../../assets/images/p37_image-1732712693761.png) | Here you can choose the object that will be used to trigger alerts. You can use this option to receive alerts only when the device becomes unreachable, but opt not to receive an alert if the CPU monitor alarms for high usage. |
| **Message template** | Templates are message models that will be sent to users. You can customize how messages will be sent to your recipients. For more information, see "Message templates". |
| ![image-1732713267486.png](../../../../../assets/images/p37_image-1732713267486.png) | This option is available only for Telegram. It lists the users who are part of the group and allows removing them manually. To add a user, you should use the code that appears at the beginning of this screen and send it to the bot "MonstaTecnologiaBot". The instructions on how to proceed are specified on this same screen. |
| ![image-1732713616303.png](../../../../../assets/images/p37_image-1732713616303.png) | Periods are the time intervals during which alerts can be sent. When creating a group the default is 24x7. The gray squares indicate that the selected times are inactive and Monsta will not send alerts for the group during those time intervals. |



## Alerts Center

This screen manages the user groups that will receive notifications and the service type, whether by email or SMS.

![image-1739974733737.png](../../../../../assets/images/p37_image-1739974733737.png)

![image-1739974790750.png](../../../../../assets/images/p37_image-1739974790750.png)  
**Display bar**: Allows the user to set the number of items per page and the period for which the information should be displayed on the screen.


| Information | Description |
| :---: | :--- |
| ![image-1739974961714.png](../../../../../assets/images/p37_image-1739974961714.png) | **Status**: Indicates the state of the message sent to a user. |
| ![image-1739975105124.png](../../../../../assets/images/p37_image-1739975105124.png) | **Type**: Indicates the medium to which the message was sent. |
| ![image-1739975173561.png](../../../../../assets/images/p37_image-1739975173561.png) | **Date and time**: Indicates the date and time of the trigger. |
| ![image-1739975251006.png](../../../../../assets/images/p37_image-1739975251006.png) | **Recipient**: Indicates the recipient of the message. This information is not available for Telegram alerts because messages are sent to a Bot. |
| ![image-1739975341938.png](../../../../../assets/images/p37_image-1739975341938.png) | **Source**: Indicates the device and monitor that originated the alert. |
| ![image-1739975429030.png](../../../../../assets/images/p37_image-1739975429030.png) | **Content**: Displays the content sent by the alert. |



## Message templates

With our templates, you can create customized messages for each type of alert, ensuring that the most important information is delivered to the responsible parties quickly and efficiently. Choose from a variety of variables to include details such as the device name, alert severity and the occurrence time, among many others.

![image-1732727391061.png](../../../../../assets/images/p37_image-1732727391061.png)



![image-1732727677203.png](../../../../../assets/images/p37_image-1732727677203.png)
Create a new template and customize the message as you wish.

---

![image-1732727745380.png](../../../../../assets/images/p37_image-1732727745380.png)
This is the box that represents the existing template. By clicking on it the user accesses the option to edit the existing information. 

| Icon | Description |
| :---: | :--- |
| ![image-1732727824893.png](../../../../../assets/images/p37_image-1732727824893.png) | Removes the existing template. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Attention</p>The template cannot be removed if it is in use by any alert group. The **Default** template is part of the system and also cannot be removed.</aside> |
| ![image-1732727887105.png](../../../../../assets/images/p37_image-1732727887105.png) | Opens the template editor for the user. |

### Editing a message template

On this screen the user can customize the message sent by alert groups. The available variables that can be used are listed and a simple programming language to work with conditions is provided.

![image-1732728340150.png](../../../../../assets/images/p37_image-1732728340150.png)


| Opção | Descrição |
| :--- | :--- |
| **Name** | This is the name that will be shown on the templates screen, as well as what will be displayed for selection when editing the alert groups option. |
| **Body** | This is the alert message text that will be sent to the user. When using variables or programming commands, these must be enclosed within "{{ }}". |
| **System variables** | These are the system variables with system information that are available to be used in alert templates. To speed up personalizing the body text with variables, simply double-click the desired variable and it will be inserted into the text. |



#### System variables

| Variable | Description
| --- | --- |
| `dataehora` | Returns the current date (d/m/y) and time (h:m). |
| `dispositivo.descricao` | Returns the device description. |
| `dispositivo.endereco` | Returns the device's IP address. |
| `dispositivo.estado` | Returns the current state of the device obtained by the Uptime monitor. |
| `dispositivo.estadoanterior` | Returns the previous state of the device obtained by the Uptime monitor. |
| `dispositivo.nome` | Returns the device name. |
| `estado` | Returns the device status. |
| `monitor.estado` | Returns the current state of the monitor. |
| `monitor.estadoanterior` | Returns the monitor's previous state. |
| `monitor.nome` | Returns the monitor name. |
| `monitor.nomecurto` | Returns the name shown on the monitor's icon. |
| `nome.metrica` | Returns the metric name. |
| `nome.instancia` | Returns the instance name. |
| `valor` | Returns the reading value. |

:::caution[Attention]
There is no support for *emojis* and images in alert templates. The message sent by the alert must be plain text only.
:::