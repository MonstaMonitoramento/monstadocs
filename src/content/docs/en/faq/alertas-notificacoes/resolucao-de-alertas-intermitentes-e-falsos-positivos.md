---
title: "How Do I Resolve Intermittent Alerts and False Positives?"
---

## Problem Description

Occurrence of intermittent alerts on specific monitors, generating down or critical notifications that do not match the actual state of the service (False Positives).

## Common Causes

There are three main scenarios that trigger this behavior:

1. **Poorly Sized Thresholds**: The **Warning** and **Critical** triggers are too close to the device's normal operation.
2. **Data Collection Failure**: Monsta does not receive a response to the request, either due to network instability (packet loss) or overload on the monitored device's hardware.
3. **Uptime Failure**: Monsta uses ICMP (ping) packets by default to test if the device is up on the network. Frequent uptime drops indicate that Monsta is not receiving the expected ping reply.

## How to Resolve

### Scenario 1: Adjusting Thresholds

If the monitor oscillates between alert states due to normal usage spikes, perform the following procedure:

- Access the problematic monitor and edit its settings.
- Adjust the **Warning** and **Critical** fields to values that match the equipment's realistic load.

### Scenario 2: Read Failure on a Monitor

Usually, this condition is caused by a *timeout* in the data collection process. To identify the cause, click on the problematic monitor, click the "Edit" button and select the "Error Log" option in the lower-left corner of the window. If the log indicates a timeout failure, do the following:

1. **Solution for Standard Protocols (SNMP, WMI, SSH)**:    
    - Edit the **Device** settings.
    - Increase the collection **Timeout** to give more response margin to an overloaded device or slow network.
2. **Solution for Script Timeouts**:    
    - Go to the top menu: **Configuration** > **Parameters**.
    - Locate the variable `lua.timeout` and increase its value as needed.

### Scenario 3: Uptime Failures

Monsta's Uptime monitor uses **ICMP (Ping)** packets to validate the presence of the device on the network. A failure in this monitor technically means that the Monsta server sent the packet and did not receive the "Echo Reply" within the expected time.

When the device is powered on but Monsta reports "Down", the causes are usually:

1. **Route Instability**: Packet loss in the network.
2. **CPU Overload on the Target**: The device prioritizes production traffic and drops ICMP packets to save processing.
3. **High Sensitivity**: Monsta is configured to consider the device "down" after few consecutive failures.

In the 1st Case (Route Instability), correctly configuring the hierarchy between devices (Parent and Child) allows Monsta to try to isolate the issue, firing alerts only for the 'parent device' and indicating where the problem begins.

For 2 and 3, if the environment presents acceptable oscillations (e.g., high latency on satellite links), configure Monsta to be more permissive. This is done by reducing the detection sensitivity in the device settings to avoid unnecessary alerts. To do this, perform the following:

- Edit the specific device.
- On the Details tab, click the Sensitivity button.
- In this window you customize the number of packets sent, the waiting time for a reply, and the time between sending each packet.

:::tip
You can customize sensitivity globally by clicking the "Options" / "Global Device Options" / "Sensitivity" button. This feature is also available when editing a device group on the "Sensitivity" tab.
:::