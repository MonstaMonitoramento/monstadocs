---
title: "Reset the root password: Ubuntu"
sidebar:
  order: 8
---

A step-by-step guide to reset the password of any user (including **root**) on **Ubuntu** using the **GRUB** menu to access a recovery *shell*.

## 1. Access the GRUB Menu

1. **Restart** your Ubuntu system.
2. Hold the `Shift` key (or, on **UEFI** systems, press the `Esc` key repeatedly) during early boot to force the **GRUB** menu to appear (if it doesn't show automatically).
3. Use the arrow keys to select your current kernel option, usually the first line.
4. Press the `e` key to edit the boot parameters.

---

## 2. Edit the Boot Line

1. In the edit screen, use the down arrows to find the line that starts with `linux`.
2. On that line, look for the `ro` (read-only) parameter and replace it with `rw` (read-write).
3. Go to the end of that same line and add the following:
    
    ```shell  
    init=/bin/bash
    ```

    The end of the modified line should look like: `... ro quiet splash rw init=/bin/bash`
4. Press `Ctrl+X` to boot the system with these new parameters. The system will boot directly to a root shell (`#`).
    
    ![image-1764957644158.png](../../../../../assets/images/p136_image-1764957644158.png)

---

## 3. Change the User Password

In the root *shell* that appears, you can reset any user's password using the `passwd` command.

### 3.1. Reset a Regular User's Password

If you want to reset a regular user's password (e.g. `joao`):

1. Run the `passwd` command followed by the username:    
    ```shell
    passwd joao    
    ```
2. Enter the **new password** and confirm it.

### 3.2. Reset the Root (Superuser) Password

Ubuntu normally disables the root account by default, but you can enable it (and set its password) if necessary:

1. Run the `passwd` command without arguments:
    ```shell
    passwd root
    ```
2. Enter the **new password** and confirm it.

---

## 4. Finish and Reboot

1. After changing the password, you need to **reboot the system** for the changes to take effect and for the system to boot normally. Use the `exec` command to restore the init process:
    ```shell
    exec /sbin/init 6 
    ```
2. The system will reboot and you will be able to log in with the new password set for the chosen user.