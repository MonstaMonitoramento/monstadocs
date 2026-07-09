---
title: "How to Restore a Backup?"
---

This manual aims to instruct the user on how to restore a Monsta backup.

## Restore a Monsta cloud backup



:::note
Monsta requires access to the hosts `https://mind.monsta.com.br` and `https://store.monsta.com.br` to create and restore backups.
:::



Monsta performs an automatic backup of your settings to our cloud daily if there are changes and keeps a history of up to 10 backups.



:::caution[Attention]
Changes in the status of devices or monitors are not considered configuration changes.
:::



### Advantages and disadvantages of this method



| Vantagens | Desvantagens |
| --- | --- |
| • Restoration takes a few minutes;</br>• No Linux technical knowledge required. | • Existing monitor history is reset when restored on a new installation. |



### Restore the backup

To restore a backup from the cloud, follow these steps:

1. Access Monsta using a user with administrator permissions;
2. Click the "Configuration" menu;
3. Click the "Cloud Backup" option;
4. Select the date of the backup you want to restore;
5. Click the "Restore" button.  
    ![image-1741969806125.png](../../../../../assets/images/p26_image-1741969806125.png)

Within a few minutes, Monsta will be restored with the selected backup's settings and will prompt for login again. Use the users and passwords that were registered in that backup to log in.

## Restore a backup from a server

Use this method to keep the monitors' history in a new installation.

### Advantages and disadvantages



| Vantagens | Desvantagens |
| --- | --- |
| • Monitor history is preserved. | • Restoration time depends on the amount of data stored in the databases;</br>  
• Linux shell technical knowledge is required. |


### Back up the current server

For this procedure, we suggest using the tutorial available at [Migration to another server](/en/start/migracao/migracao-para-um-novo-servidor) on this wiki as it will automatically transfer Monsta to a new server.