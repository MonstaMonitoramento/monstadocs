---
title: "Configuring SNMP on Windows Server 2012"
sidebar:
  order: 2
---

Tutorial aimed at enabling a basic SNMP services configuration on Windows Operating Systems.

## Configure the SNMP service

Logged in as administrator, at the command prompt type:

```powershell
control appwiz.cpl
```

The following screen will be shown:

![image-1645203240026.png](../../../../../assets/images/p13_image-1645203240026.png)• Click "Turn Windows features on or off";

![image-1645203263156.png](../../../../../assets/images/p13_image-1645203263156.png)  
• Click the "Next" button;

![image-1645203290724.png](../../../../../assets/images/p13_image-1645203290724.png)  
• Select "Role-based or feature-based installation" and click the "Next" button;

![image-1645203356817.png](../../../../../assets/images/p13_image-1645203356817.png)  
• Select the server where you want to install SNMP and click the "Next" button;

![image-1645203375023.png](../../../../../assets/images/p13_image-1645203375023.png)  
• Click the "Next" button;

![image-1645203393692.png](../../../../../assets/images/p13_image-1645203393692.png)  
• Check "SNMP Service";  
• In the window that opens click the "Add Features" button;  
• Click the "Next" button;

![image-1645203409651.png](../../../../../assets/images/p13_image-1645203409651.png)  
• Check the option "Restart the destination server automatically if required";  
• Click the "Install" button;  
• When the installation finishes click the "Close" button;

At the command prompt, type:

```powershell
services.msc
```

The following screen will appear:

![image-1645203449317.png](../../../../../assets/images/p13_image-1645203449317.png)• Select "SNMP Service";  
• Click the "Action" menu and select "Properties";

![image-1645203494580.png](../../../../../assets/images/p13_image-1645203494580.png)  
• On the "General" tab, set the "Startup type" field to "Automatic";

![image-1645203512798.png](../../../../../assets/images/p13_image-1645203512798.png)  
• On the "Security" tab click the "Add" button;  
• Under "Community rights" select the "READ ONLY" option;  
• In "Community Name" type "public";  
• Click the "Add" button;  
• Check the option "Accept SNMP packets from any host";  
• Click the "OK" button.

## Allow SNMP service through the Windows Server 2012 Firewall

To allow the SNMP service through the Windows Firewall, open the command prompt and type:

```
netsh advfirewall firewall add rule name="Servidor SNMP" new dir=in action=allowenable=yes profile=public remoteip=any localport=161 protocol=udp
```



:::note
By default, Windows' SNMP is enabled only for the local network.
:::



- - - - - -