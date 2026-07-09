---
title: "Reset the root password: CentOS"
sidebar:
  order: 5
---

This tutorial aims to recover the root password on a CentOS Linux Server.

## Recover the root user password

During the server boot, the boot screen similar to the image below will appear:

![image-1740673001214.png](../../../../../assets/images/p81_image-1740673001214.png)

Press the "e" key to open the boot configuration edit mode as shown below:

![image-1740673021815.png](../../../../../assets/images/p81_image-1740673021815.png)

Find the line that starts with "linux" or "linux16" and append "rw init=/sysroot/bin/bash" to the end as in the example below:

![image-1740673058015.png](../../../../../assets/images/p81_image-1740673058015.png)

Press CTRL+X to boot Linux with the new settings. The following screen should appear:

![image-1740673113884.png](../../../../../assets/images/p81_image-1740673113884.png)

Enter the following commands to change the password:

```shell
chroot /sysroot
passwd root
touch /.autorelabel
exit
reboot
```