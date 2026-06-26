---
title: "Fix the yum Command on CentOS 7"
sidebar:
  order: 10
---

CentOS 7 reached its end of life (*EOL - End Of Life*) on **June 30, 2024** and the `mirrors` used for updates and package installation no longer respond. However, the files were moved to an "archive" (the *vault*). This article shows how to fix the repository to point to `vault.centos.org` to access the archived packages and thus make it possible to use the `yum` command to install packages on CentOS 7.

## 1. Backup

Before making changes, make a copy of the CentOS base repository file.

```shell
cp -avr /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

## 2. Edit the CentOS-Base.repo file to point to the Vault

Open the file with a text editor (`vi`, `nano`...)

```shell
vi /etc/yum.repos.d/CentOS-Base.repo
```

Inside the file, look for lines that start with `mirrorlist=` and comment them out (add a `#` at the beginning of the line). Then uncomment (remove the `#`) the lines that start with `baseurl=` and change the URL to `http://vault.centos.org/7.9.2009/`.

You will need to do this for the `[base]`, `[updates]`, and `[extras]` sections (you can also do it for `[centosplus]` if you wish).

Here is an example of how it should look:

```vim
[base]
name=CentOS-$releasever - Base
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#released updates
[updates]
name=CentOS-$releasever - Updates
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
```

Save and close the file.

Clean the `yum` cache.

```shell
yum clean all
```

You can now install the desired packages using the `yum` command.