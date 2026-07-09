---
title: "Resetar a senha de root: CentOS"
sidebar:
  order: 5
---

Este tutorial tem como objetivo recuperar a senha de root em um Linux CentOS Server.

## Recuperar a senha do usuário root

Na inicialização do servidor Linux aparecerá a tela de boot semelhante a imagem abaixo:

![image-1740673001214.png](../../../../../assets/images/p81_image-1740673001214.png)

Pressione a tecla “e”, com isso será aberto o modo de edição das configurações do boot conforme a imagem abaixo:

![image-1740673021815.png](../../../../../assets/images/p81_image-1740673021815.png)

Procure pela linha que começa com “linux” ou "linux16" e ao final adicione "rw init=/sysroot/bin/bash" conforme exemplo abaixo:

![image-1740673058015.png](../../../../../assets/images/p81_image-1740673058015.png)

Pressione CTRL + X para iniciar o Linux com as novas configurações. A seguinte tela deverá aparecer:

![image-1740673113884.png](../../../../../assets/images/p81_image-1740673113884.png)

Digite os comandos abaixo para efetuar a troca da senha:

```shell
chroot /sysroot
passwd root
touch /.autorelabel
exit
reboot
```
