---
title: Instalação do Monsta
sidebar:
  order: 3
---

## Requisitos mínimos

Esta é a configuração mínima para a instalação do Monsta:

| Item                                                             | Requisito Mínimo                                                                                                                                 |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![HD](../../../../../assets/images/p25_image-1645452261754.png)  | **Espaço em disco**<br />40GB livre para /var (configurações, banco de dados e logs)<br />300MB livre para /opt/monsta (programas e bibliotecas) |
| ![RAM](../../../../../assets/images/p25_image-1645452312898.png) | **Memória RAM**<br />2GB de memória RAM                                                                                                          |
| ![SO](../../../../../assets/images/p25_image-1645452455434.png)  | **Sistema Operacional**<br />Linux 64bits<br />Sistema Operacional Linux recomendado: Fedora Server                                              |
| ![CPU](../../../../../assets/images/p25_image-1645452542916.png) | **Processador**<br />Cores: 2<br />Velocidade: 1.8GHz                                                                                            |

## Download do Arquivo

Logado em seu servidor Linux como root, execute os comandos abaixo:

#### Fedora/Red Hat

```shell
yum install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.rpm
```

#### Ubuntu/Debian

```shell
apt-get install -y wget && wget https://www.monsta.com.br/monsta/download/monsta-latest.deb
```

## Instalação

Após baixar o arquivo de instalação do Monsta, execute o seguinte comando:

#### Fedora/Red Hat

```shell
dnf install -y monsta-latest.rpm
```

#### Ubuntu/Debian

```shell
export PATH=/usr/local/sbin:/usr/sbin:/sbin:$PATH
dpkg -i monsta-latest.deb
```

A partir de agora o Monsta está instalado em seu servidor e pode ser acessado através das portas 80 (http) e 443 (https):

## Primeiro acesso ao Monsta

Abra um browser e acesse:

![image-1645528439997.png](../../../../../assets/images/p83_image-1645528439997.png)

Você pode optar por autenticar-se utilizando uma credencial existente através do botão **"Entrar com minha conta"** ou iniciar o fluxo de novo usuário clicando em **"Criar nova conta"**.

![](../../../../../assets/images/20260630-105252.png)

Preencha os campos para criar sua conta na nuvem e avance clicando em "Próximo":

![](../../../../../assets/images/Tela_Novo_Usuario.png)

Você receberá em seguida um e-mail contendo um código para validar sua conta. Informe-o na tela abaixo e clique em Confirmar:

![](../../../../../assets/images/20260630-111438.png)

Após esse procedimento, você será direcionado para a tela de licenças. Como esta é uma nova conta, nenhuma licença será apresentada e você poderá selecionar se deseja assinar uma licença ou ativar a versão Trial. Clique no botão "Ativar Trial" para habilitar os 30 dias de teste do Monsta em sua empresa:

![](../../../../../assets/images/20260630-111706.png)

Você será encaminhado a tela para informar uma senha para o usuário "admin" do Monsta. Digite sua senha e clique no botão "Confirmar":

![image-1741981958907.png](../../../../../assets/images/p83_image-1741981958907.png)

Agora você será redirecionado a tela principal do Monsta:

![image-1741982076022.png](../../../../../assets/images/p83_image-1741982076022.png)

A partir desta tela você poderá criar e gerenciar os dispositivos a serem monitorados.

Para maiores informações, consulte o [Manual do Usuário](/pt-br/manual/manual-usuario) do Monsta.
