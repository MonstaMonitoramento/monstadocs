---
title: "Why Does Monsta Show a Partition with 5% Less Used Space?"
---

This 5% difference in the disk space of a Linux partition, when monitored via [SNMP](/en/tech/protocolos-coleta/snmp), is a standard characteristic of the **Ext2, Ext3 and Ext4** filesystems. It is not a miscalculation, but an intentional space reservation.

This reservation exists to ensure the system continues to operate stably, even when the disk is nearly full. The 5% is reserved primarily for the **`root`** user, the system administrator.

The main reasons for this reservation are to:

- **Prevent file fragmentation**: The reservation helps ensure the filesystem has enough space to allocate new data contiguously, which improves performance.
- **Allow the system to operate**: If the disk fills to 100%, the operating system can hang or become unusable. This reservation ensures that `root` has space to, for example, write logs, move files, or run essential commands to free space.

In summary, the 5% difference is a feature of the **Ext** filesystem designed for protection. It ensures the administrator always has a buffer to perform critical operations and maintain the server's stability.