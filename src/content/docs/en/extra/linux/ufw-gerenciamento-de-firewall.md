---
title: "Firewall Management - UFW"
sidebar:
  order: 4
---

**UFW** stands for **Uncomplicated Firewall**.

It is an interface to manage the Netfilter firewall on Linux, which is the system's packet filtering system. UFW was developed to simplify the process of configuring firewall rules through the `iptables` utility.

UFW is the most popular and recommended method to manage the firewall on Debian- and Ubuntu-based distributions.

### UFW Command Examples (Practical Guide)

Most UFW commands require superuser privileges (`sudo`).

#### 1. Status Check

Check if UFW is active and view the current rules:



| **Action** | **Command** | **Example Output** |
| --- | --- | --- |
| **Check Status** | `ufw status` | `Status: inactive` (or `active`) |
| **Check Details** | `ufw status verbose` | Lists all rules in detail. |



#### 2. Enabling and Disabling

It's crucial to set the rules before enabling to avoid locking yourself out of the server.



| **Action** | **Command** | **Note** |
| --- | --- | --- |
| **Enable UFW** | `ufw enable` | **Warning**: If you don't have an `allow ssh` rule, you'll lose remote access. |
| **Disable UFW** | `ufw disable` | Turns off the firewall (not recommended). |
| **Reset Rules** | `ufw reset` | Removes all user-defined rules. |



#### 3. Default Policies

Configure what happens to traffic that does not match any specific rule.



| **Action** | **Command** | **Result** |
| --- | --- | --- |
| **Deny Incoming (Recommended)** | `ufw default deny incoming` | No external connections are allowed unless explicitly specified. |
| **Allow Outgoing** | `ufw default allow outgoing` | Your server can initiate connections to the outside world. |



#### 4. Adding Rules (Allowing)



| **Goal** | **Command** | **Note** |
| --- | --- | --- |
| **Allow SSH (Port 22)** | `ufw allow ssh` | Uses the service name to open port 22/TCP. |
| **Allow HTTP (Port 80)** | `ufw allow http` | Opens port 80/TCP. |
| **Allow HTTPS (Port 443)** | `ufw allow 443/tcp` | Opens by port number and protocol. |
| **Specific Port** | `ufw allow 5432/udp` | Opens port 5432 only for the UDP protocol. |
| **Specific IP Traffic** | `ufw allow from 192.168.1.100 to any port 3306` | Allows only the IP `192.168.1.100` to access port 3306 (MySQL). |



#### 5. Removing Rules

Removal can be done by rule number or by rule text.



| **Action** | **Command** | **Note** |
| --- | --- | --- |
| **Remove by Text** | `ufw delete allow http` | Removes the rule allowing http (80/TCP). |
| **Remove by Number** | `ufw status numbered` `ufw status delete [número]` | The first command returns a list with existing rules and their positions, the second removes the rule at the selected position. |