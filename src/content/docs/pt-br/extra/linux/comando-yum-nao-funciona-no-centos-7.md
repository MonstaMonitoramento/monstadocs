---
title: "Corrigir o Comando yum no CentOS 7"
sidebar:
  order: 10
---

O CentOS 7 chegou ao seu fim de vida (*EOL - End Of Life*) em **30 Junho de 2024** e os `mirrors` utilizados para atualizações e instalação de programas não respondem mais. Porém, os arquivos foram movidos para um "arquivo histórico" (o *vault*). Este artigo demonstra como corrigir o repositório para consultar no `vault.centos.org` para acessar os pacotes arquivados e assim tornar possível utilizar o comando `yum` para instalar programas no CentOS 7.

## 1. Backup

Antes de realizar alterações, faça uma cópia do arquivo base do repositório do CentOS.

```shell
cp -avr /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

## 2. Edite o arquivo CentOS-Base.repo para apontar para o Vault 

Abra o arquivo com um editor de texto (`vi`, `nano`...)

```shell
vi /etc/yum.repos.d/CentOS-Base.repo
```

Dentro do arquivo, procure por linhas que começam com `mirrorlist=` e comente-as (adicione um `#` no início da linha). Em seguida, descomente (remova o `#`) as linhas que começam com `baseurl=` e altere o URL para `http://vault.centos.org/7.9.2009/`.

Você precisará fazer isso para as seções `[base]`, `[updates]`, e `[extras]` (podes fazer também para o `[centosplus]`, se desejar).

Aqui está um exemplo de como deve ficar:

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

Salve e feche o arquivo.

Limpe o cache do `yum`.

```shell
yum clean all
```

Agora é possível instalar os programas desejados utilizando o comando `yum`.
