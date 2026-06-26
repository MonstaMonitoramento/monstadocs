---
title: "Corregir el comando yum en CentOS 7"
sidebar:
  order: 10
---

CentOS 7 llegó al final de su vida útil (*EOL - End Of Life*) el **30 de junio de 2024** y los `mirrors` usados para actualizaciones e instalación de programas ya no responden. Sin embargo, los archivos fueron trasladados a un "archivo histórico" (el *vault*). Este artículo muestra cómo corregir el repositorio para apuntar a `vault.centos.org` para acceder a los paquetes archivados y así poder usar el comando `yum` para instalar programas en CentOS 7.

## 1. Copia de seguridad

Antes de realizar cambios, haga una copia del archivo base del repositorio de CentOS.

```shell
cp -avr /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

## 2. Edite el archivo CentOS-Base.repo para apuntar al Vault 

Abra el archivo con un editor de texto (`vi`, `nano`...)

```shell
vi /etc/yum.repos.d/CentOS-Base.repo
```

Dentro del archivo, busque las líneas que comienzan con `mirrorlist=` y coméntelas (añada un `#` al inicio de la línea). A continuación, descomente (elimine el `#`) las líneas que comienzan con `baseurl=` y cambie la URL a `http://vault.centos.org/7.9.2009/`.

Deberá hacer esto para las secciones `[base]`, `[updates]` y `[extras]` (puede hacerlo también para `[centosplus]`, si lo desea).

Aquí hay un ejemplo de cómo debe quedar:

```vim
[base]
name=CentOS-$releasever - Base
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#actualizaciones publicadas
[updates]
name=CentOS-$releasever - Updates
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#paquetes adicionales que pueden ser útiles
[extras]
name=CentOS-$releasever - Extras
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#paquetes adicionales que amplían la funcionalidad de paquetes existentes
[centosplus]
name=CentOS-$releasever - Plus
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus&infra=$infra
baseurl=http://vault.centos.org/7.9.2009/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
```

Guarde y cierre el archivo.

Limpie la caché de `yum`.

```shell
yum clean all
```

Ahora es posible instalar los programas deseados utilizando el comando `yum`.