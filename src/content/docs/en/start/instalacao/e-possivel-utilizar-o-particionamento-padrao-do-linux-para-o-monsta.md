---
title: "Is it possible to use the Linux default partitioning for Monsta?"
sidebar:
  order: 2
---

Default partitioning, while convenient, is not optimized for the usage profile and growth needs of the Monsta software. We always recommend **manual partitioning** to ensure correct space allocation and future flexibility.

Below, we explain the main reasons why default partitioning is not ideal.

***

## 1. 🏡 Inefficient Allocation for `/home`



Many Linux distribution installers are configured for personal (desktop) use, and therefore tend to allocate a **considerable and generous amount of space to the `/home` partition**.

- **Problem**: Monsta is a software system that does not rely on the `/home` directory for its main operation or high-volume data storage. The space allocated to `/home` will end up being **underutilized**, while other crucial areas may run low on space.
- **Recommendation**: Prioritize space for directories where the system and Monsta data actually reside.

## 2. 🗃️ `/var` Partition Undersized or Missing



The `/var` partition is of **critical importance** for Monsta, as it is the default location where the system databases and *logs* are stored.

- **Problem**: Some automatic partitioners may **not create a separate partition for `/var`** or allocate a very small volume for it. With Monsta's intensive use of databases, this partition can quickly exhaust its space, leading to operational failures and data storage issues.
- **Recommendation**: Create the `/var` partition separately and ensure it has the **largest volume of space** allocated, taking into account data growth over time.

## 3. 📉 Lack of Flexibility with LVM



Many default systems may not configure partitions using the **Logical Volume Manager (LVM)**.

- **Problem**: LVM is an abstraction layer that allows flexible management and manipulation of disk volumes. **Without LVM**, it will be impossible, or extremely difficult, to **increase the size** of a partition (such as `/var`) if it starts to run out of space in the future, requiring system downtime and potentially data migration.
- **Recommendation**: Use **LVM** when creating partitions, especially for `/var` and `/` to ensure the ability to **expand in the future** without complex *downtime*.

***