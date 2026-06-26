---
title: "Configurando o SNMP no Windows Server 2012"
sidebar:
  order: 2
---

Tutorial com objetivo de ativar uma configuração básica dos serviços SNMP em Sistemas Operacionais Windows.

## Configurar o serviço SNMP

Logado como administrador, no prompt de comando digite:

```powershell
control appwiz.cpl
```

A seguinte tela será mostrada:

![image-1645203240026.png](../../../../../assets/images/p13_image-1645203240026.png)• Clique em “Ativar ou desativar recursos do Windows”;

![image-1645203263156.png](../../../../../assets/images/p13_image-1645203263156.png)  
• Clique no botão “Próximo”;

![image-1645203290724.png](../../../../../assets/images/p13_image-1645203290724.png)  
• Selecione “Instalação baseada em função ou recurso” e clique no botão “Próximo”;

![image-1645203356817.png](../../../../../assets/images/p13_image-1645203356817.png)  
• Selecione o servidor no qual você deseja instalar o SNMP e clique no botão “Próximo”;

![image-1645203375023.png](../../../../../assets/images/p13_image-1645203375023.png)  
• Clique no botão “Próximo”;

![image-1645203393692.png](../../../../../assets/images/p13_image-1645203393692.png)  
• Marque o item “SNMP Service”;  
• Na janela que abrir clique no botão “Adicionar Recursos”;  
• Clique no botão “Próximo”;

![image-1645203409651.png](../../../../../assets/images/p13_image-1645203409651.png)  
• Marque a opção “Reiniciar cada servidor de destino automaticamente, se necessário”;  
• Clique no botão “Instalar”;  
• Terminada a instalação clique no botão “Fechar”;

No prompt de comando, digite:

```powershell
services.msc
```

A seguinte tela irá aparecer:

![image-1645203449317.png](../../../../../assets/images/p13_image-1645203449317.png)• Selecione o item “Serviço SNMP”;  
• Clique no menu “Ação” e selecione “Propriedades”;

![image-1645203494580.png](../../../../../assets/images/p13_image-1645203494580.png)  
• Na aba “Geral”, marque o campo “Tipo de inicialização” como “Automático”;

![image-1645203512798.png](../../../../../assets/images/p13_image-1645203512798.png)  
• Na aba “Segurança” clique no botão “Adicionar”;  
• Em “Direitos da comunidade” selecione a opção “SOMENTE LEITURA”;  
• Em “Nome da Comunidade” digite “public”;  
• Clique no botão “Adicionar”;  
• Marque a opção “Aceitar pacotes SNMP de qualquer host”;  
• Clique no botão “Ok”.

## Liberar o acesso ao serviço SNMP no Firewall do Windows Server 2012

Para liberar o serviço SNMP no Firewall do Windows, acesse o prompt de comando e digite:

```
netsh advfirewall firewall add rule name="Servidor SNMP" new dir=in action=allowenable=yes profile=public remoteip=any localport=161 protocol=udp
```



:::note
Em geral o SNMP do Windows vem habilitado apenas para a rede local.
:::



- - - - - -
