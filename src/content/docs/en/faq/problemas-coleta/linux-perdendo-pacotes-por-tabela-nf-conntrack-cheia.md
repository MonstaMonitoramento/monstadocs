---
title: "How to Resolve Instability in Collections Due to Packet Loss?"
---

This article demonstrates how to resolve intermittent connection or packet loss that occurs when the Linux kernel's connection tracking table (*conntrack*) is full.

## 1. Problem and Causes

Linux uses `nf_conntrack` (*Network Filter Connection Tracking*) to track all active network connections (TCP, UDP, ICMP, etc.), required for correct operation of the firewall (*iptables/nftables*) and NAT (*Network Address Translation*).

When the number of active connections reaches the configured maximum, the kernel cannot track new connections and, by default, drops them. This manifests as:

- Connection and packet loss on Linux.
- Intermittent failure to establish new connections.
- Error messages in the system log (`/var/log/messages` or `dmesg`), such as:
    - `kernel: nf_conntrack: table full, dropping packet`
    - `nf_conntrack: table full`

![Captura de tela 2025-11-14 161942.png](../../../../../assets/images/p123_captura-de-tela-2025-11-14-161942.png)

This problem affects Monsta monitoring, causing random collection failures in monitors, because Monsta sends the request and does not receive a response.

Reasons that may cause table exhaustion:

1. **High Traffic of Short-Lived Connections**: Servers that handle many connections that are opened and closed quickly can fill the table rapidly. A large number of monitors in Monsta can contribute.
2. **Denial of Service Attacks (DDoS/DoS)**: A packet flood attack, especially *SYN floods* (which try to open many incomplete TCP connections), or large volumes of UDP traffic (which uses *conntrack* for basic tracking) can exhaust the table immediately.
3. **Timeouts That Are Too Long**: If the time the kernel takes to "forget" an inactive connection (*timeout*) is too long, entries remain stuck in the table even though the connection has ended. This is especially problematic for TCP connections in the `TIME_WAIT` state (the default 60-second timeout is often too long for high-traffic environments).

## How to confirm the problem

You can check the table status with the following commands:

```shell
# Maximum connections limit (nf_conntrack_max)
cat /proc/sys/net/netfilter/nf_conntrack_max

# Current number of active connections (nf_conntrack_count)
cat /proc/sys/net/netfilter/nf_conntrack_count
```

If `nf_conntrack_count` is very close to or equal to `nf_conntrack_max`, the table is full.

## 2. Solution: Increase and Optimize Limits

The solution is to increase the maximum connections limit (`nf_conntrack_max`) and optimize the table performance parameters. To change permanently (without losing the settings on reboot), follow these steps:

#### 2.1 Edit the system configuration file `/etc/sysctl.conf` with a text editor (`vi`, `nano`...)

```shell
vi /etc/sysctl.conf
```

#### 2.2 Add the following lines at the end of the file

```shell
######################################################
# Conntrack optimization for high traffic
######################################################
net.netfilter.nf_conntrack_max = 262144
net.netfilter.nf_conntrack_buckets = 65536
net.netfilter.nf_conntrack_tcp_timeout_time_wait = 30
```

#### 2.3 Save and close the file

#### 2.4 Apply the new settings without rebooting the system

```shell
sysctl -p
```

## 3. Verification

After applying the changes, verify the new limit.

```shell
cat /proc/sys/net/netfilter/nf_conntrack_max
# The result should be 262144
```