---
title: "How to monitor the status of an HTTP URL?"
---

This article explains the proper procedure to monitor the status of a specific URL (such as `http://192.168.0.200:8080/sistema`) in Monsta, checking whether it responds with an HTTP/200 (OK) status.

## ❌ Common Mistake

It's a common mistake to try to add the full URL path (ex: `http://192.168.0.200:8080/sistema`) in the Device Address field on the device screen.

![image-1764180428270.png](../../../../../assets/images/p129_image-1764180428270.png)

The Device Address field accepts only the IP or *hostname* (ex: `192.168.10.16`, `www.foo.com`). It is used to identify the device and does not check URL paths or ports.

## ✅ Correct Procedure: Using the URL Monitor

To monitor whether a specific path on a URL is responding correctly, you should add a dedicated monitor to that device.

### 1. Add the HTTP Service Template

- Edit the device.
- Add the "Services - HTTP" template to the device.  
    ![image-1764180633849.png](../../../../../assets/images/p129_image-1764180633849.png)

### 2. Add and Configure the "Check URL" Monitor

The "Services - HTTP" template contains several monitors, including "Check URL", which will be used.

- Click the option to add a new monitor  
    ![image-1764180781279.png](../../../../../assets/images/p129_image-1764180781279.png)
- Select the "Check URL" monitor and click the pencil icon to edit  
    ![image-1764180854853.png](../../../../../assets/images/p129_image-1764180854853.png)
- Click Advanced and add the URL you want to monitor (ex: `http://192.168.0.200:8080/sistema`) ![image-1764180956419.png](../../../../../assets/images/p129_image-1764180956419.png)
- Save the changes and create the monitor



:::caution[Attention]
The "Check URL" monitor (from the "Services - HTTP" template) only works for URLs that use the HTTP protocol. If your URL is HTTPS (encrypted), contact support to check if there is a monitor that checks HTTPS URLs.
:::