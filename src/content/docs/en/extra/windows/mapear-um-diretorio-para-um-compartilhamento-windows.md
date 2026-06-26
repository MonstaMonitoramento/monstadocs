---
title: "Map a Directory to a Windows Share"
---

Tutorial to mount a shared drive from a Windows system on a CentOS Linux server.

## Installing the Samba client

Logged in as root, at the Linux terminal prompt type:

```shell
yum install samba-client cifs-utils
```

## Creating the mapping

Logged in as root, at the Linux terminal prompt enter the following commands, replacing the items below with your settings:  

:::note
Windows uses the **SMB** (*Server Message Block*) protocol for network file sharing. Depending on the version in use, replace the `vers=2.0` parameter with the appropriate version, for example: `vers=1.0`
:::


:::danger[Warning]
The line is appended to the /etc/fstab file using `>>`. Do not delete or remove existing entries in your /etc/fstab file unless you understand the consequences; doing so may prevent the Linux server from booting.
:::



> **user** = Windows user  
> **password** = Windows password  
> **192.168.0.48** = Windows IP or host  
> **share** = Name of the share on Windows  
> **media** = Directory on the Linux system where the share will be mounted

```shell
echo username=usuário > /root/.credencial
echo password=senha >> /root/.credencial
echo //192.168.0.48/unidade /media cifs vers=2.0,credentials=/root/.credencial 0 0 >> /etc/fstab
```

The commands above will create the file `/root/.credencial` which will securely contain the user credentials for the Windows share and will add a configuration line to the `/etc/fstab` file, causing that share to be mounted automatically whenever the Linux server is restarted.

To mount the share, at the command line type:

```shell
mount /media 
```