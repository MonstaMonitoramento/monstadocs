---
title: "Reset the root password: Debian"
sidebar:
  order: 6
---

The root password can be reset using the **GRUB** (Grand Unified Bootloader) menu to boot the system into *single-user mode* or with a *recovery shell*.

## Prerequisites

- Physical access to the server/machine console.
- The Debian operating system must be using **GRUB** as the bootloader.

## Step-by-Step to Reset the Password

### 1. Access the GRUB Menu

1. **Reboot** your Debian system.
2. Wait for the GRUB menu to appear on the screen;
3. Use the arrow keys (↑ and ↓) to select the Debian kernel entry (usually the first option).

### 2. Edit the Boot Parameters

1. Press the `e` key to edit the boot commands of the selected entry.
2. Use the down arrows to locate the line that begins with `linux` (or `linuxefi`). This line contains the kernel path and its boot parameters.
3. On that line, locate and replace the `ro` (read-only) parameter with `rw` (read-write).
4. At the **end of that same line**, add the following parameter to load the bash shell as the main init process:  
      
    `init=/bin/bash`  
    Example of how the modified line will look:
    
    > `linux /boot/vmlinuz-5.10.0-23-amd64 root=UUID=... rw quiet init=/bin/bash`

![image-1764956789240.png](../../../../../assets/images/p135_image-1764956789240.png)

### 3. Boot the System and Change the Password

1. Press `Ctrl+X` to boot the system with the new parameters.
2. The system will skip the normal init process and directly load a *shell* as the *root* user (indicated by `#`).
3. Run the `passwd` command to reset the *root* user's password:
    
    ```shell
    passwd    
    ```
4. Type the **new password** and confirm it when prompted. Characters will not be displayed (standard security behavior).
5. A message like `password updated successfully` will confirm the change.

### 4. Reboot the System

1. Reboot the system after changing the password. Use the `exec` command to return to the normal init process:
    
    ```shell
    exec /sbin/init 6
    ```
2. Debian will reboot. At the login prompt, you can use the username `root` and the **new password** you just set.