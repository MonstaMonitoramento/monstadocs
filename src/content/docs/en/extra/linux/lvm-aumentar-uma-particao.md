---
title: "Increasing an LVM Partition"
sidebar:
  order: 9
---

![image-1740053130226.png](../../../../../assets/images/p19_image-1740053130226.png)

This tutorial teaches how to increase a partition configured on LVM using a new disk. Before continuing, add a new virtual disk to your VM or a new physical disk to a non-virtualized server.



:::caution[Caution]
There are many Linux distributions, each with its own particularities. The information below was tested on Fedora Server 40 and may not work on other distributions.
:::



## Identify and create a new partition

Logged in as root, on the screen of the Linux server that will have its partition increased, type the command below:

```shell
lsblk
```

This command will list the partitions on the physical disks available to Linux. The command output will look something like:

![image-1719319256777.png](../../../../../assets/images/p19_image-1719319256777.png)

In this example, the physical disk /dev/sdb with 127GiB is the additional disk and it will be used to increase the LVM volume.

To use the entire partition to create an LVM volume, use the command below:

```shell
(echo n; echo p; echo 1; echo; echo; echo t; echo 8e; echo w) | fdisk /dev/sdb
```

![image-1719319583211.png](../../../../../assets/images/p19_image-1719319583211.png)

To check if the new disk was initialized correctly, type the command again:

```shell
fdisk -l /dev/sdb
```

The disk dev/sdb should be shown as a partition of type LVM:

![image-1719319740087.png](../../../../../assets/images/p19_image-1719319740087.png)

## Increase space in the logical volume

Now that there is a partition with free space we need to inform Linux to add it to the existing logical volume. To do this, run the commands below:

```shell
pvcreate /dev/sdb1
```

This command will create a new physical volume that can be assigned to a logical volume. To find out which volumes exist, type the command below:

```shell
vgdisplay
```

The output should be similar to the example below:

![image-1719317745124.png](../../../../../assets/images/p19_image-1719317745124.png)

In our example the `logical` volume will be extended. To do this, run the command:

```shell
vgextend logical /dev/sdb1
```

Run the command below again to verify that the size of the volume group has increased by comparing the `VG Size` parameter:

```shell
vgdisplay
```

![image-1719317853910.png](../../../../../assets/images/p19_image-1719317853910.png)

Now it is necessary to extend the logical volume. To list the existing volumes, run the command below:

```shell
lvdisplay
```

Identify the volume for the `/var` partition, as shown in the image below:

![image-1719317916295.png](../../../../../assets/images/p19_image-1719317916295.png)

To increase the size of the volume /dev/logical/var, run the commands below:

```shell
lvextend /dev/lvar/var /dev/sdb1
xfs_growfs /dev/logical/var
```



:::tip
The `xfs_growfs` command is used for the xfs file system. If your partition uses the `extfs` formatting, use the `resizefs /dev/logical/var` command, for example.
:::



The command `vextend` increases the logical volume and the `xfs_growfs` command tells the file system to use all the newly available space. To verify that the partition was increased correctly, use the command below:

```shell
df -h
```

In our example, the `/var` partition should be 591GB in size.

![image-1719318344313.png](../../../../../assets/images/p19_image-1719318344313.png)