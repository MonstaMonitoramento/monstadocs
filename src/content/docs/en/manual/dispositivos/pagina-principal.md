---
title: "Main Page"
sidebar:
  order: 1
---

This screen displays all devices monitored on the network and their respective statuses. Here you can create new devices and add monitors for each of them, as well as view the graphs of the data collected by the selected monitors and customize them.

![image-1739970299845.png](../../../../../assets/images/p52_image-1739970299845.png)

## View Modes

| Ícone | Descrição |
| :---: | :--- |
| ![image-1646846764087.png](../../../../../assets/images/p52_image-1646846764087.png) | **Grid**: Displays devices in box format. It is the default landing screen.<br />For more information, see [Grid View](/en/manual/dispositivos/visualizacao-em-modo-grid). |
| ![image-1646846862499.png](../../../../../assets/images/p52_image-1646846862499.png) | **Detailed View**: Provides an overview of a selected device. |
| ![image-1646846951852.png](../../../../../assets/images/p52_image-1646846951852.png) | **Groups View**: Shows the existing device groups. Clicking on a group activates a filter and only the devices belonging to the selected group will be shown. |
| ![image-1646847134431.png](../../../../../assets/images/p52_image-1646847134431.png) | **Sunburst View**: Starting from the selected parent device this view presents a network structure with equipment organized hierarchically. A summary of statuses and changes on the timeline is also shown.<br />For more information, see [Sunburst View](/en/manual/dispositivos/visualizacao-sunburst). |
| ![image-1739970604314.png](../../../../../assets/images/p52_image-1739970604314.png) | **Map View**: Shows a graphical and hierarchical view of devices.<br />For more information, see [Map View](/en/manual/dispositivos/visualizacao-em-mapa). |

- - - - - -

## Global Device and Display Options

| Ícone | Descrição |
| :---: | :--- |
| ![image-1646847756093.png](../../../../../assets/images/p52_image-1646847756093.png) | **Global Options**: Centralize access credentials (SNMP/WMI/SSH), uptime sensitivity levels, and define sound alerts in a single place, applying the settings automatically to all devices and allowing manual exceptions only where necessary. Customize how devices and monitors are presented on the devices dashboard.<br />For more information, see [Options](/en/manual/dispositivos/opcoes). |

- - - - - -

## New Device


| Ícone | Descrição |
| :---: | :--- |
| ![image-1646853490547.png](../../../../../assets/images/p52_image-1646853490547.png) | To add new devices, click the "+ New" button. For more information see the topic [New Device](/en/manual/dispositivos/novo-dispositivo). |



- - - - - -

## Sort


| Ícone | Descrição |
| :---: | :--- |
| ![image-1647350134023.png](../../../../../assets/images/p52_image-1647350134023.png) | Sorts the display of devices by name, address, or status. |



- - - - - -

## Filter


| Ícone | Descrição |
| :---: | :--- |
| ![image-1647350333020.png](../../../../../assets/images/p52_image-1647350333020.png)<br />![image-1732552858800.png](../../../../../assets/images/p52_image-1732552858800.png)| Allows filtering the device display by its description/text, by groups, by their states or the state of their monitors, by disabled alerts, or by deactivated devices.<br />**Filter by Text**: Filters the device display by text or address.<br />**Filter by Device Group**: Filters the device display by the group in which they are registered.<br />**Show only disabled alerts**: Filters the device display to those that have alerts disabled.<br />**Filter by status**: Filters the device display by their respective statuses or those of their monitors.|
| ![image-1647350765256.png](../../../../../assets/images/p52_image-1647350765256.png) | **Quick Filter**: Filters the device display by text or address. |
| ![image-1732553089963.png](../../../../../assets/images/p52_image-1732553089963.png) | **Sound**: Enables/Disables sound alerts in Monsta. |


- - - - - -

## Status

| Ícone | Descrição |
| :---: | :--- |
| ![image-1732553534749.png](../../../../../assets/images/p52_image-1732553534749.png) | **Monitors**: Shows the number of monitors per status. Clicking on a status activates the monitor filter to display only the devices that have monitors in that state. |
| ![image-1732553586057.png](../../../../../assets/images/p52_image-1732553586057.png) | **Devices**: Shows the number of devices per status. Clicking on a status activates the device filter to display only the hosts that are in that state. |



## Device Box

![image-1732553898974.png](../../../../../assets/images/p52_image-1732553898974.png)

Displays device information and a summary of its status and monitors. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1732554918043.png](../../../../../assets/images/p52_image-1732554918043.png) | **Monitors**: Shows the number of monitors per status on the device. |
| ![image-1732554978099.png](../../../../../assets/images/p52_image-1732554978099.png) | **Name and Address**: | Shows the name assigned to the device and its respective address for monitoring. |
| ![image-1732555138160.png](../../../../../assets/images/p52_image-1732555138160.png) | **Icon**: Image assigned to the device. |
| ![image-1732555146691.png](../../../../../assets/images/p52_image-1732555146691.png) | **Detailed View**: Opens the screen with detailed information about the device. |
| ![image-1732555458211.png](../../../../../assets/images/p52_image-1732555458211.png) | **Tools**: Performs some actions on the highlighted device. |
| ![image-1732555468623.png](../../../../../assets/images/p52_image-1732555468623.png) | **Edit**: Opens the edit screen for the highlighted device. |

## Device Properties

![image-1746721902542.png](../../../../../assets/images/p52_image-1746721902542.png)

| Ícone | Descrição |
| :---: | :--- |
| ![image-1746721988339.png](../../../../../assets/images/p52_image-1746721988339.png) | **Enable Monitoring**: This switch, when inactive, pauses data collection for the device. |
| ![image-1746722104491.png](../../../../../assets/images/p52_image-1746722104491.png) | **Detailed View**: Opens a new window with various information about the device, such as uptime, monitor statuses, and its timeline. |
| ![image-1746722237020.png](../../../../../assets/images/p52_image-1746722237020.png) | **Timeline**: Opens the [Timeline](/en/manual/linha-tempo/linha-do-tempo) with the filter set for this device. |
| ![image-1746722341442.png](../../../../../assets/images/p52_image-1746722341442.png) | **Edit**: Opens the device edit. See [New Device](/en/manual/dispositivos/novo-dispositivo) for more information. |
| ![image-1746722438462.png](../../../../../assets/images/p52_image-1746722438462.png) | **Delete**: Deletes the selected device and all its monitors. |
| ![image-1746722493757.png](../../../../../assets/images/p52_image-1746722493757.png) | **Clone Device**: Creates a copy of the selected device along with all its monitors. |
| ![image-1746722576309.png](../../../../../assets/images/p52_image-1746722576309.png) | **Automatic Monitors**: This option creates rules for Monsta to automatically add monitors to the selected device. For more information, consult " |[Automatic Monitors](https://wiki.monsta.com.br/books/manual-do-usuario/page/monitores-automaticos)".
| ![image-1746722650939.png](../../../../../assets/images/p52_image-1746722650939.png) | **Add Monitors**: Add monitors from the selected template to the device or allow the creation of a custom monitor just for it. |
