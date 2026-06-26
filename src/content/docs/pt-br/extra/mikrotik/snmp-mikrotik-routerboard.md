---
title: "Configurando o SNMP na Routerboard MikroTik"
---

Tutorial com objetivo ativar uma configuração básica dos serviços SNMP em um Routerboard da MikroTik.

## Configurando o serviço SNMP

:::tip
Esse procedimento também pode ser feito utilizando o software Winbox da própria MikroTik.
:::



Abra um navegador de internet e digite na URL o endereço do MikroTik. A seguinte tela aparecerá:

![image-1645205030195.png](../../../../../assets/images/p16_image-1645205030195.png)Entre com o usuário e senha do seu dispositivo (o padrão é admin e a senha deixe em branco). A seguir, no menu da esquerda, clique em IP e abaixo clique em SNMP:

![image-1645205057404.png](../../../../../assets/images/p16_image-1645205057404.png)Preencha os campos “Contact Info” com o responsável pelo contato desse dispositivo e o campo “Location” com a sua localização.

## Configurando uma Comunidade

Após, clique no botão “Communities”, a seguinte tela será exibida:

![image-1645205091972.png](../../../../../assets/images/p16_image-1645205091972.png)  
Se já existir a comunidade public, modifique as informações de configuração conforme a tela abaixo, caso contrário, clique no botão “Add New” e preencha a tela com as seguintes informações:

![image-1645205110836.png](../../../../../assets/images/p16_image-1645205110836.png)  
Clique no botão Ok e em seguida, clique no botão Close para fechar a tela de edição de comunidades.

## Aplicar as Configurações

Na tela do SNMP, clique no botão Apply.

![image-1645205142984.png](../../../../../assets/images/p16_image-1645205142984.png)  
  
A partir de agora o SNMP está disponível em seu dispositivo MikroTik e já pode ser monitorado pelo Monsta através das versões 1 e 2c com a comunidade public.