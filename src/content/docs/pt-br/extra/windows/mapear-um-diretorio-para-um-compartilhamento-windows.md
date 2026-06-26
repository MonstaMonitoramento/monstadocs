---
title: "Mapear um Diretório Para um Compartilhamento Windows"
---

Tutorial para montar uma unidade compartilhada em um sistema Windows em um servidor Linux CentOS.

## Instalando o cliente Samba

Logado como root, na tela de terminal do Linux digite:

```shell
yum install samba-client cifs-utils
```

## Criando o mapeamento

Logado como root, na tela de terminal do Linux digite os seguintes comandos substituindo os itens abaixo por suas configurações:  

:::note
O Windows utiliza o protocolo **SMB** (*Server Message Block*) para compartilhamento de arquivos em rede. Dependendo da versão utilizada, substitua o parâmetro `vers=2.0` pela versão adequada, exemplo: `vers=1.0`
:::


:::danger[Cuidado]
A inserção da linha no arquivo /etc/fstab é feita com `>>`. Não delete ou remova configurações existentes no seu arquivo /etc/fstab sem conhecimento sob o risco do servidor Linux não iniciar mais.
:::



> **usuário** = Usuário do Windows  
> **senha** = Senha do Windows  
> **192.168.0.48** = IP ou host do Windows  
> **unidade** = Nome do compartilhamento no Windows  
> **media** = Diretório no Linux onde será montado o compartilhamento

```shell
echo username=usuário > /root/.credencial
echo password=senha >> /root/.credencial
echo //192.168.0.48/unidade /media cifs vers=2.0,credentials=/root/.credencial 0 0 >> /etc/fstab
```

Os comandos acima irão criar o arquivo `/root/.credencial` que possuirá, de forma segura, os dados do usuário para o compartilhamento no Windows e adicionarão uma linha de configuração no arquivo `/etc/fstab`, fazendo com que esse compartilhamento criado seja sempre mapeado quando o servidor Linux for reiniciado.

Para montar o compartilhamento, na linha de comando digite:

```shell
mount /media 
```
