---
title: "Internet Link Monitoring"
---

Monsta is a powerful tool to ensure the availability and performance of your company's network connectivity. Monitoring internet links is important to detect connectivity failures and identify bandwidth consumption bottlenecks.

## How It Works

Monsta monitors the internet link on the **network interface of your local equipment** where the link arrives.

1. **Data Collection**: Monsta connects to your network equipment (such as a router, firewall, or switch) and collects information from the interface configured for the internet link (WAN port). More than one port can be monitored simultaneously.
2. **Metrics Monitored**:
    
    
    - **Interface Speed and Status**: Indicates whether the interface is active (*UP*) or inactive (*DOWN*) and its connection speed, reporting if it becomes inactive or if the physical connection speed is below expected.
    - **Traffic Volume**: Measures the amount of inbound (*Inbound*) and outbound (*Outbound*) data in bits per second, metrics used for monitoring consumption.
    - **Calculation of Transferred Volume**: Monsta can calculate the total volume of data transferred over the time interval you select.
3. **Processing**: Collected data is stored and presented in charts and can be configured on dashboards for trend and historical analysis.

## Creating Proactive Alarms

The main advantage of monitoring the link is the ability to configure **proactive and reactive alarms** based on the collected metrics.



| Alarm Type | Threshold Condition | Impact and Action |
| --- | --- | --- |
| **Link Down** | The interface changes from **Status UP to DOWN**. | **Critical Alert.** Indicates total connectivity failure with the provider. |
| **Physical Connection Speed Reduction** | The network interface reduces its physical connection speed due to a cabling issue or a problem with the network interface. | **Warning/Issue Alert.** Warns if the physical interface is operating below its full capacity. |
| **Excessive Consumption (Bandwidth)** | The traffic rate (Inbound or Outbound) exceeds a pre-configured **utilization threshold** (e.g., 90% of the link's total capacity) for a period of time. | **Warning/Issue Alert.** Indicates that the link is saturated. The alarm suggests the need for **bandwidth management** or an *upgrade* to the link. |


:::tip[Practical example]
If your link is 100 Mbps, you can configure an alarm to trigger when usage consistently reaches 90 Mbps.
:::

## Practical Configuration

To configure monitoring of an internet link in Monsta, follow these basic steps:

1. **Add the Device**: Create a device in Monsta to monitor your Router/Firewall.
2. **Add the Monitors**: Select the device and click the "+" button to add the network traffic monitor and Interface Speed monitor.
3. **Configure the Alarms**: Select the created monitors and click "Edit" to configure the alert thresholds you want to receive.



:::note
To receive notifications, remember to add an Alert Group to your device. For more information, see [Alerts](/en/manual/grupos-alertas/alertas)
:::