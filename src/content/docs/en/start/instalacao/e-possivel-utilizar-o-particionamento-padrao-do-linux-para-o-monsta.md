---
title: "Is it possible to use the Linux default partitioning for Monsta?"
sidebar:
  order: 2
---

:::caution[Attention]
Our recommendation is emphatically that the default/automatic Linux partitioning NOT be used for installing Monsta.
:::

Default partitioning, while convenient, is not optimized for Monsta's usage profile and growth needs. We always recommend **manual partitioning** to ensure correct space allocation and future flexibility.

Below, we explain the main reasons why default partitioning is not ideal.

---

## 1. 🏡 Inefficient Allocation for `/home`

Many Linux distribution installers are configured for personal (desktop) use and therefore tend to allocate a **considerable and generous amount of space to the `/home` partition**.

- **Problem**: Monsta is a software system that does not rely on the `/home` directory for its primary operation or high-volume data storage. The space allocated to `/home` will end up being **underutilized**, while other crucial areas may run low on space.
- **Recommendation**: Prioritize space for the directories where the system and Monsta data actually reside.

## 2. 🗃️ `/var` Partition Undersized or Missing

The `/var` partition is of **critical importance** to Monsta, as it is the default location where the system databases and *logs* are stored.

- **Problem**: Some automatic partitioners may **not create a separate partition for `/var`** or may allocate a very small volume to it. With Monsta's intensive use of databases, that partition can quickly run out of space, leading to operational failures and data storage issues.
- **Recommendation**: Create the `/var` partition separately and ensure it has the **largest volume of space** allocated, taking into account data growth over time.

## 3. 📉 Lack of Flexibility with LVM

Many default systems may not configure partitions using the **Logical Volume Manager (LVM)**.

- **Problem**: LVM is an abstraction layer that allows flexible management and manipulation of disk volumes. **Without LVM**, it will be impossible, or extremely difficult, to **increase the size** of a partition (such as `/var`) if it starts to run out of space in the future, requiring system downtime and potentially data migration.
- **Recommendation**: Use **LVM** when creating partitions, especially for `/var` and `/` to ensure the capacity for **future expansion** without complex *downtime*.

---

:::tip
To ensure the **performance**, **stability**, and **scalability** of your system, we recommend performing **manual partitioning** following the specific installation guidelines that prioritize space for the `/var`, `/` partitions and use LVM.
:::