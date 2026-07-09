---
title: "Aumentando uma Partição LVM"
sidebar:
  order: 9
---

![image-1740053130226.png](../../../../../assets/images/p19_image-1740053130226.png)

Esse tutorial ensina como aumentar uma partição configurada sobre LVM utilizando um novo disco. Antes de continuar, adicione um novo disco virtual à sua VM ou um novo disco físico a um servidor não virtualizado.



:::caution[Atenção]
Existem diversas distribuições Linux, cada qual com suas particularidades. As informações a seguir foram testadas no sistema operacional Fedora Server 40 e podem não funcionar em outras distribuições.
:::



## Identificar e criar uma nova partição

Logado como root, na tela do servidor Linux que será incrementada a partição, digite o comando abaixo:

```shell
lsblk
```

Esse comando irá listar as partições nos discos físicos disponíveis para o Linux. O resultado do comando será algo como:

![image-1719319256777.png](../../../../../assets/images/p19_image-1719319256777.png)

Nesse exemplo, o disco físico /dev/sdb com 127GiB é o disco adicional e o mesmo será usado para aumentar o volume do LVM.

Para utilizar toda a partição para criar um volume com LVM, utilize o comando abaixo:

```shell
(echo n; echo p; echo 1; echo; echo; echo t; echo 8e; echo w) | fdisk /dev/sdb
```

![image-1719319583211.png](../../../../../assets/images/p19_image-1719319583211.png)

Para verificar se o novo disco foi inicializado corretamente, digite novamente o comando:

```shell
fdisk -l /dev/sdb
```

O disco dev/sdb deve ser mostrado como uma partição do tipo LVM:

![image-1719319740087.png](../../../../../assets/images/p19_image-1719319740087.png)

## Incrementar o espaço no volume lógico

Agora que há uma partição com espaço livre precisamos informar ao Linux para adicioná-la ao volume lógico existente. Para fazer isso, execute os comandos abaixo:

```shell
pvcreate /dev/sdb1
```

Esse comando irá criar um novo volume físico que poderá ser atribuído a um volume lógico. Para saber quais os volumes existentes, digite o comando abaixo:

```shell
vgdisplay
```

A saída deverá ser conforme o exemplo abaixo:

![image-1719317745124.png](../../../../../assets/images/p19_image-1719317745124.png)

Em nosso exemplo será incrementado o volume `logical`. Para fazer isso, execute o comando:

```shell
vgextend logical /dev/sdb1
```

Execute novamente o comando abaixo para verificar se o tamanho do volume lógico foi incrementado comparando o parâmetro `VG Size`:

```shell
vgdisplay
```

![image-1719317853910.png](../../../../../assets/images/p19_image-1719317853910.png)

Agora é necesário incrementar o volume lógico. Para listar os volumes existentes, execute o comando abaixo:

```shell
lvdisplay
```

Identifique o volume da partição `/var`, conforme a imagem abaixo:

![image-1719317916295.png](../../../../../assets/images/p19_image-1719317916295.png)

Para incrementar o tamanho do volume /dev/logical/var, execute os comandos abaixo:

```shell
lvextend /dev/lvar/var /dev/sdb1
xfs_growfs /dev/logical/var
```



:::tip
O comando `xfs_growfs` é utilizado para o sistema de arquivos xfs. Caso sua partição utilize a formatação `extfs`, utilize o comando `resizefs /dev/logical/var`, por exemplo.
:::



O comando `vextend` aumenta o volume lógico e o comando `xfs_growfs` informa ao sistema de arquivos para utilizar todo o novo espaço disponível. Para verificar se a partição foi incrementada corretamente, utilize o comando abaixo:

```shell
df -h
```

Em nosso exemplo, a partição `/var` deverá ter 591GB de tamanho.

![image-1719318344313.png](../../../../../assets/images/p19_image-1719318344313.png)
