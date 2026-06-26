---
title: "SNMP (Simple Network Management Protocol)"
sidebar:
  order: 1
---

# What is SNMP?

The *Simple Network Management Protocol* (**SNMP**) is a standard Internet protocol used to collect and organize information about managed devices on IP (Internet Protocol) networks and to modify that information to change the device's behavior. In simpler terms, SNMP allows network administrators to monitor and manage their network equipment—such as routers, switches, servers, printers, and more—from a central point.

Imagine having a control panel for your entire network infrastructure. SNMP works by providing data to that panel, allowing you to:

- **Monitor the status and performance of your devices**: Check if a router is functioning correctly, what a server's CPU usage is, how much ink remains in a printer, etc.
- **Receive alerts about issues**: Be notified automatically if a device fails, if bandwidth is high, or if any other event requires attention.
- **Remotely configure some devices**: In some cases, SNMP allows you to change configurations on your network devices without accessing them directly.
- **Collect data for analysis**: SNMP provides historical performance data that can be used to identify trends, plan network capacity, and troubleshoot future problems.

SNMP works through the exchange of messages between an **SNMP agent**, which resides on the managed device, and an **SNMP manager**, which is the central monitoring system, such as **Monsta**, for example. SNMP agents collect information about the device and store it in a structure called the **MIB (Management Information Base)**. The SNMP manager can then query the agents to obtain this information or send commands to change configurations (in some cases).

In summary, SNMP is a fundamental tool for efficient and proactive computer network management, helping ensure the availability and proper functioning of your IT services.

Since its creation, SNMP has undergone significant evolutions to adapt to increasing demands for security and functionality. The most well-known and used versions are v1, v2c, and v3. Although they all share the same central purpose, they differ in features, mainly in terms of security.

## SNMP v1: The Simple and Insecure Pioneer

Released in 1988, SNMPv1 was the first widely adopted version. It stood out for its simplicity, using a community-based management model. A community is essentially a plain-text password (called a community string) that grants read or read/write access to a device.

- **Community String**: It is the only "authentication" mechanism. If the network manager's community string matches the device's, access is granted.
- **Messages**: Uses three basic message types: GET (to retrieve values), SET (to change values), and TRAP (to notify events).
- **Vulnerability**: The main weakness of SNMPv1 is the lack of security. Community strings are transmitted in plain text, making them susceptible to interception and malicious use. This means anyone with network access can capture the traffic and discover the community, gaining SNMP access to the devices.

:::caution[Important]
The use of SNMP v1 is recommended only if the equipment does not support later versions, due to its limitations.
:::

## SNMP v2c: Improvements and Greater Flexibility

SNMPv2 was an attempt to modernize the protocol, introducing substantial improvements. SNMPv2c (where the "c" means Community-Based) retained the SNMPv1 security model but brought important advances in other areas.

- **Message Improvements**: Introduced new message types, such as GETBULK, which allows retrieval of large amounts of data more efficiently, reducing network load. It also improved the TRAP mechanism with the introduction of INFORM, which confirms receipt of the notification.
- **Data Types**: Improved the definition of data types, offering more flexibility and precision in representing managed information.
- **Support for 64-bit Variables**: A significant technical improvement is the ability to manage larger values, such as network traffic counters. SNMPv1 is limited to 32-bit counters, which can reach their maximum and "wrap" (reset to zero) quickly on high-speed networks. SNMPv2c and v3 support 64-bit counters, which can track much larger data volumes before wrapping, providing more accurate and reliable statistics for traffic monitoring.
- **Community Model**: Despite the improvements, SNMPv2c still uses the same security approach as SNMPv1, with community strings transmitted in plain text. Therefore, it inherits the same security vulnerabilities, making it unsuitable for environments where confidentiality is critical.

## SNMP v3: The Answer for Security

SNMPv3 represents a huge leap in terms of security and is the recommended version for managing modern networks. It abandons the community model and implements a robust framework for security and authentication.

- **Authentication**: SNMPv3 requires configuring a username and password for each device. Messages are digitally signed to ensure they come from a trusted source. This prevents malicious third parties from injecting fake messages into the network. The most common authentication algorithms are MD5 and SHA.
- **Privacy**: In addition to authentication, SNMPv3 offers encryption. Data transmitted between the manager and the device can be encrypted, preventing it from being read if intercepted. The most used encryption algorithms are DES and AES.
- **User-Based Model**: Security is based on users, where each can have different access levels and permissions. This allows for granular and stricter access control.

| **Feature** | **SNMP v1** | **SNMP v2c** | **SNMP v3** |
| --- | --- | --- | --- |
| **Security** | None (plain text) | None (plain text) | Authentication and Encryption |
| **Authentication** | Community String | Community String | User and Password (MD5/SHA) |
| **Encryption** | No | No | Yes (DES/AES) |
| **Message Types** | GET, SET, TRAP | GETBULK, INFORM (and v1 types) | GETBULK, INFORM (and v1 types) |

## Communication Ports

The protocol uses two default communication ports:

- **161/UDP**: for communication from the manager (monitoring system) to the agent (the monitored device);
- **162/UDP**: for communication from the agent to the manager (communications that originate from the monitored device, such as **TRAP**).

Some devices allow changing SNMP settings, such as community, port and, for SNMPv3, authentication credentials and encryption type. It is always important to check these settings on the device to use them in the monitoring system.

## Monsta

Monsta supports all three versions of SNMP and allows you to provide the necessary parameters to monitor devices according to each version (community, port, user, password, encryption type).

At the moment, Monsta operates only with the **manager > agent** communication, using the **GET** and **GETBULK** message types.