---
title: "Configuring SNMP on MikroTik Routerboard"
---

Tutorial aimed at enabling a basic configuration of SNMP services on a MikroTik Routerboard.

## Configuring the SNMP service

:::tip
This procedure can also be performed using MikroTik's Winbox software.
:::



Open a web browser and enter the MikroTik address in the URL. The following screen will appear:

![image-1645205030195.png](../../../../../assets/images/p16_image-1645205030195.png)Enter the username and password for your device (the default is admin and leave the password blank). Then, in the left menu, click IP and then click SNMP:

![image-1645205057404.png](../../../../../assets/images/p16_image-1645205057404.png)Fill the “Contact Info” field with the person responsible for contacting regarding this device and the “Location” field with its location.

## Configuring a Community

Then, click the “Communities” button; the following screen will be displayed:

![image-1645205091972.png](../../../../../assets/images/p16_image-1645205091972.png)  
If the community public already exists, modify the configuration information as shown below; otherwise, click the “Add New” button and fill the screen with the following information:

![image-1645205110836.png](../../../../../assets/images/p16_image-1645205110836.png)  
Click the Ok button and then click the Close button to close the community editing window.

## Apply the Configurations

On the SNMP screen, click the Apply button.

![image-1645205142984.png](../../../../../assets/images/p16_image-1645205142984.png)  
  
From now on SNMP is available on your MikroTik device and can be monitored by Monsta using versions 1 and 2c with the public community.