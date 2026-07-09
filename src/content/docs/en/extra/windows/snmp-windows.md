---
title: "Configuring SNMP on Windows"
sidebar:
  order: 1
---

Tutorial aimed at enabling a basic SNMP service configuration on Windows operating systems.

## Configure the SNMP service

Logged in as administrator, at the command prompt type:

```powershell
control appwiz.cpl
```

The following screen will be shown:

![image-1645202947535.png](../../../../../assets/images/p12_image-1645202947535.png)

• Click on “Turn Windows features on or off”;

![image-1645202976501.png](../../../../../assets/images/p12_image-1645202976501.png)  
• Check the item “SNMP Protocol” and click OK;

At the command prompt, type:

```powershell
services.msc
```

The following screen will be shown:

![image-1645203011196.png](../../../../../assets/images/p12_image-1645203011196.png)• Select the item “SNMP Service”;  
• Click the “Action” menu and select “Properties”;

![image-1645203056884.png](../../../../../assets/images/p12_image-1645203056884.png)  
• On the “General” tab, set the “Startup type” field to “Automatic”;

![image-1645203078004.png](../../../../../assets/images/p12_image-1645203078004.png)  
• On the “Security” tab click the “Add” button;  
• In “Community rights” select the option “READ ONLY”;  
• In “Community Name” type “public”;  
• Click the “Add” button;  
• Check the option “Accept SNMP packets from any host”;  
• Click the “OK” button.

## Allowing access to the SNMP service in Windows Firewall

To allow the SNMP service in Windows Firewall, open the command prompt and type:

```powershell
netsh advfirewall firewall add rule name="Servidor SNMP" new dir=in action=allow enable=yes profile=public remoteip=any localport=161 protocol=udp
```



:::note
Generally, Windows SNMP is enabled only for the local network.
:::