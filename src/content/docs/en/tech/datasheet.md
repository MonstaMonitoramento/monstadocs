---
title: "Datasheet"
---

The **Monsta** is a complete and intuitive network monitoring solution, designed to provide detailed information about your devices and resources, enabling you to keep your network running smoothly and avoid outages. With a user-friendly interface and powerful features, the [Software Name] provides a comprehensive view of your network, allowing you to make informed decisions and optimize the performance of your infrastructure.

## Key Features

- **Comprehensive device monitoring**: Track the performance and health of all your network devices, including servers, routers, switches, firewalls, and more.
- **In-depth resource information**: Gain deep insights into CPU usage, memory, disk, bandwidth, and other important resources for each device.
- **Charts and dashboards generation**: Visualize real-time performance data through charts and customizable dashboards, enabling you to identify trends and bottlenecks.
- **Smart alerts**: Receive instant notifications about issues and critical events, allowing you to take preventive action and fix problems before they affect your users.
- **Problem forecasting**: Use advanced analytics to identify patterns and predict potential problems, allowing you to prepare and prevent outages.
- **Intuitive and easy-to-use interface**: Monsta is designed to be easy to use, even for users without advanced technical knowledge.
- **Customizable reports**: Generate detailed reports on your network's performance, enabling you to track progress and share information with your team.
- **Low hardware consumption**: Thanks to its optimized architecture, Monsta delivers exceptional performance with minimal resource usage. This translates into higher speed, smoother operation, and responsiveness, even in high-demand environments.
- **100% in-house development**: A 100% in-house solution developed by Monsta Technology, the result of our expertise and dedication to providing the best network monitoring software on the market.
- **Automatic backups**: Monsta automatically backs up all your configurations to the cloud.

![image-1740051151463.png](../../../../assets/images/p25_image-1740051151463.png)

## What is Monsta used for?

Monsta aims to ensure the continuous operation of essential services in your organization by continuously monitoring the hardware and software in your network and issuing alerts to the responsible parties.

## Minimum requirements

Suggested to monitor 500 devices and 5,000 monitors.


| Item | Minimum Requirement |
| :---: | :--- |
| ![image-1645452261754.png](../../../../assets/images/p25_image-1645452261754.png) | **Disk space**<br />40GB free for /var (configurations, database and logs)<sup>1</sup> <br />300MB free for /opt/monsta (programs and libraries) |
| ![image-1645452312898.png](../../../../assets/images/p25_image-1645452312898.png) | **RAM**<br />1GB RAM |
| ![image-1645452455434.png](../../../../assets/images/p25_image-1645452455434.png) | **Operating System**<br />Linux 64-bit<br />Recommended Linux Operating System: Fedora Server 40 |
| ![image-1645452542916.png](../../../../assets/images/p25_image-1645452542916.png) | **Processor**<br />Cores: 2<br />Clock speed: 1.8GHz |

:::note
<sup>1</sup> The partition size depends on the amount of information that will be stored. Monitoring data is compressed before being saved to disk.
:::

## Specifications

| Category / Item | Specification |
| :--- | :--- |
| **DEVELOPMENT** | |
| Development Language | Rust, Typescript and Go |
| HTML Language | HTML 5 |
| Scripting Languages | LUA, Python and MagoVM (Proprietary) |
| **SYSTEMS** | |
| HTTP Server | Monrouter (in-house development) |
| Operating System | Linux 64 bits |
| Cloud communication | HTTP and HTTPS with TLS encryption |
| Data collection mechanisms | SNMP, WMI, ICMP, TCP, API and external sources. (Allows the user to create their own mechanism) |
| **NATIVE ALERTS** | |
| SMS | Sent via Twilio and Zenvia |
| Emails | Sent via AWS |
| Telegram | Sent via the MonstaTecnologia bot on Telegram |
| **DATABASE (Monitors History)** | |
| MonstaDB | (Proprietary) `nosql` model for real-time queries |
| In-Memory | Yes |
| Protection against data corruption | Yes |
| Persistent | Yes |
| Data compression | Yes |
| Data discard | No (data is not summarized over days) |
| **DATABASE (Configurations)** | |
| Database | (Proprietary) SQL model |
| In-Memory | Yes |
| Protection against data corruption | Yes |
| Persistent | Yes |
| Data compression | Yes |
| Data discard | No |

## Software Architecture

![image-1645464317340.png](../../../../assets/images/p25_image-1645464317340.png)

## Try Monsta Before You Buy

Try Monsta in your organization to evaluate its operation and behavior. The trial version has no limit on monitors or devices, and if you liked the tool, all the work you did will not be discarded; simply activate the software license key and you turn the trial version into a permanent one.

## About the company

Monsta is a technology company focused on detecting and solving IT infrastructure problems. Our goal is to make network monitoring a simple and automated task, through a reliable and low-cost tool for the market.