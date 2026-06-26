---
title: "Monitoring the Number of Users per PPPoE Server on Mikrotik"
---

For providers using the **Mikrotik** as a PPPoE concentrator, knowing the exact number of clients connected to each server is an essential metric. This quick guide shows how you can configure **Monsta** to monitor the total users per `pppoe-server`.

## 1. Data Collection

The method used to obtain the *per-server* count on Mikrotik is by executing a command via **SSH** (*Secure Shell*).

### 1.1. Access Configuration on Mikrotik

Before configuring Monsta, your Mikrotik must allow SSH access:

1. **Create a Specific User**: On Mikrotik, create a user (e.g.: `monsta`) with a strong password and minimal permissions (only what's necessary to run the command, such as `read`).
2. **Enable the SSH Service**: Ensure the SSH service (port 22, by default) is active and that the Mikrotik Firewall allows incoming connections from the IP where your Monsta is installed.

## 2. Configuring the Monitor in Monsta

Click the button to add a new device and enter the following information:

1. In the Details tab, fill in the following information: 
    1. **Device Name**: In this field enter any text that identifies your equipment;
    2. **IP Address**: Enter the Mikrotik's IP;
2. In the Templates tab, select "Mikrotik Routerboard;
3. In the collection tab, fill the "SSH" option with the username, password and port if it differs from 22. 

:::tip
You can use the "Test" button to check if the connection is OK.
:::


4. Click Save to create the new device.

![image-1759756111276.png](../../../../../assets/images/p122_image-1759756111276.png)
*SSH configuration screen*

## 3. Creating the User Monitor

After creating the device, click on it so that the monitors appear at the bottom of the screen. Click "+" to add a new monitor.

In the monitors window, search for "PPPoE: Users per PPPoE server" and select which server you want to monitor the number of users.

![image-1759756922247.png](../../../../../assets/images/p122_image-1759756922247.png)
*Screen for adding monitors*

Click the button to create the monitor.

Now your Monsta monitors the total users within that server. If you want to add monitoring for other servers, just click "+" again and select the available options.



:::tip
When opening the monitor to view its graph, click the "Edit" button located at the top right corner and set the thresholds at which you'd like to receive alerts in case of problems.
:::



![image-1759757535089.png](../../../../../assets/images/p122_image-1759757535089.png)
*Example of alert thresholds*