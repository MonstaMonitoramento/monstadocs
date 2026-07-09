---
title: "How does the alert notification system work?"
---

Monsta has a system of alert groups:

![image-1644795874070.png](../../../../../assets/images/p5_image-1644795874070.png)

Each alert group contains settings for notifications via E-mail, SMS, and Telegram that can be applied to devices and monitors. For each of these three notification delivery mechanisms, the group can be configured to send alerts when there is an event in a warning state, a critical state, or both. Additionally, the group can be configured to alert only for devices, only for monitors, or both:

![image-1644795936801.png](../../../../../assets/images/p5_image-1644795936801.png)

Finally, the group can be configured to send alerts only during a user-specified time period:

![image-1644796975555.png](../../../../../assets/images/p5_image-1644796975555.png)

To apply these alert settings, each device or monitor can have zero or more alert groups:

![image-1644795982010.png](../../../../../assets/images/p5_image-1644795982010.png)

When an event occurs for a device or monitor, all linked alert groups are checked. If the configured conditions match, a notification will be sent.