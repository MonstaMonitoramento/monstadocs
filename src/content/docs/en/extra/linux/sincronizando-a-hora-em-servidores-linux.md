---
title: Synchronizing Time on Linux Servers
sidebar:
  order: 11
---
The most recommended approach for servers is to use **NTP** to ensure the time is always accurate and synchronized with external sources. Below we cover the recommended method to perform this configuration.

## Using `chrony` (Recommended for More Accurate Synchronization)

`chrony` is often used on virtual machines or in environments with variable network time. It is common in RHEL/CentOS 7+ and some Ubuntu and Debian installations.

1. **Install `chrony` (if necessary)**:

   * **Debian/Ubuntu**: `sudo apt update && sudo apt install chrony`
   * **RHEL/CentOS/Fedora**: `sudo dnf install chrony` or `sudo yum install chrony`
2. **Start and Enable the Service**:

   ```shell
   sudo systemctl enable --now chronyd  
   # or chrony for Debian/Ubuntu
   ```
3. **Check the Synchronization**:

   ```shell
   chronyc tracking
   ```
   Look for a **`Reference ID`** and a **`Stratum`** different from zero. The **`System time`** will show the offset.
  

---

## Set Timezone

First, set the correct **timezone**, as this affects the system clock.

1. **List Timezones**:

   ```shell
   timedatectl list-timezones | grep 'America/Sao_Paulo'
   ```
   (Replace with the desired timezone)

2. **Set the Timezone**: 

   ```shell
   sudo timedatectl set-timezone 'America/Sao_Paulo'
   ```
3. **Verify that the time is correct**:
   ```shell
   date
   ```
   
## Synchronize the Hardware Clock (CMOS/BIOS)

The Linux server maintains two clocks: the **System Clock** (software) and the **Hardware/BIOS Clock** (CMOS, battery-backed). After fixing the system clock, synchronize it with the hardware clock so the time remains correct after a reboot.

```shell
sudo hwclock -w  # Writes System time (soft) to the Hardware (hard)
```