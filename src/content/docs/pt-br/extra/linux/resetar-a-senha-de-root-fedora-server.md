---
title: "Resetar a senha de root: Fedora Server"
sidebar:
  order: 7
---

Este tutorial tem como objetivo recuperar a senha de root em um Linux Fedora Server.

## Recuperar a senha do usuário root

Na inicialização do servidor Linux aparecerá a tela de boot semelhante a imagem abaixo:

![image-1719319990630.png](../../../../../assets/images/p21_image-1719319990630.png)

Pressione a tecla “e”, com isso será aberto o modo de edição das configurações do boot conforme a imagem abaixo:

![image-1719320093869.png](../../../../../assets/images/p21_image-1719320093869.png)

Procure pela linha que começa com “linux” ou "linux16" ou "linuxefi" e ao final adicione "rw init=/bin/bash" conforme exemplo abaixo:

![image-1719320698513.png](../../../../../assets/images/p21_image-1719320698513.png)

Pressione CTRL + X para iniciar o Linux com as novas configurações. A seguinte tela deverá aparecer:

![image-1719320807739.png](../../../../../assets/images/p21_image-1719320807739.png)

Digite os comandos abaixo para efetuar a troca da senha:

```shell
passwd
```

Restaure as permissões do SELinux com o seguinte comando:

```shell
/bin/sed -i s/"SELINUX=enforcing"/"SELINUX=permissive"/ /etc/selinux/config
touch /.autorelabel
```



:::danger[Atenção]
Se as permissões do SELinux não forem restauradas com os procedimentos acima, o processo de login poderá falhar e você terá que fazer o processo da senha novamente.
:::



Após, reinicie o servidor com o comando abaixo:

```shell
/sbin/reboot -r
```



:::note
Utilize o comando abaixo apenas se você deseja ativar o selinux.
:::



Após reiniciar o servidor, logue-se como root e ative novamente o selinux com os comandos abaixo:

```shell
sed -i s/"SELINUX=permissive"/"SELINUX=enforcing"/ /etc/selinux/config
setenforce enforcing
```