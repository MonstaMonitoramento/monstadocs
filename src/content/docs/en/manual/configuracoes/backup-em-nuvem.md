---
title: "Cloud Backup"
sidebar:
  order: 13
---

Monsta provides a cloud service<sup>1</sup> that automatically backs up your configurations<sup>2</sup> daily at 00:00 each day, provided there have been changes to the configurations. Up to 10 files can be stored in the cloud.

:::caution[Important]
<sup>1</sup> The operation of this feature requires that the Monsta software have communication with the host `mind.monsta.com.br` on port **443/TCP**.  
  
<sup>2</sup> The monitor history is not included in this backup.
:::

![image-1739988536042.png](../../../../../assets/images/p64_image-1739988536042.png)

| Opção / Botão | Descrição |
| :---: | :--- |
| ![image-1739988569479.png](../../../../../assets/images/p64_image-1739988569479.png) | List of available backups to restore. |
| ![image-1739988610183.png](../../../../../assets/images/p64_image-1739988610183.png) | Restores the selected backup. This procedure will overwrite all current configurations with the selected backup. |
| ![image-1739988634554.png](../../../../../assets/images/p64_image-1739988634554.png) | Creates a backup with the current date/time. |