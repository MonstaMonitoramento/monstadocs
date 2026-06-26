---
title: "Migração para um Novo Servidor"
---

Este tutorial mostra como migrar o Monsta a partir da versão >5.0 para outro servidor.

## Requisitos mínimos

Requisitos mínimos para a migração do Monsta:

:::caution
Verifique se a partição "/var" do novo servidor possui o espaço suficiente para transferência dos dados do Monsta do servidor atual.
:::

| Item | Requisito Mínimo |
| :---: | :--- |
| ![Espaço em disco](../../../../../assets/images/p25_image-1645452261754.png) | **Espaço em disco**<br />40GB livre para /var (configurações, banco de dados e logs)<br />300MB livre para /opt/monsta (programas e bibliotecas)<br />Certifique-se de que a nova instalação possui espaço o suficiente para efetuar a migração. |
| ![Memória RAM](../../../../../assets/images/p25_image-1645452312898.png) | **Memória RAM**<br />2GB de memória RAM |
| ![Sistema Operacional](../../../../../assets/images/p25_image-1645452455434.png) | **Sistema Operacional**<br />Linux 64bits<br />Sistema Operacional Linux recomendado: Fedora Server 40 (x86_64 systems) ou Ubuntu Server 24. Pode ser utilizada a instalação mínima para o Monsta. |
| ![Processador](../../../../../assets/images/p25_image-1645452542916.png) | **Processador**<br />Cores: 2<br />Velocidade: 1.8GHz |

:::note
As configurações acima permitem, em geral, verificar aproximadamente 500 dispositivos com 10 monitores cada ou um total de 5.000 monitores.
:::


## Script de migração

Logado como root no seu servidor, baixe o script de migração conforme exemplo abaixo:

### Fedora/Red-Hat
```shell
yum install -y wget sshpass
wget https://www.monsta.com.br/monsta/download/migrate.sh
```

### Ubuntu/Debian
```shell
apt-get install -y wget sshpass
wget https://www.monsta.com.br/monsta/download/migrate.sh
```

## Iniciando a transferência
Após baixar o script, execute-o com a seguinte sintaxe:

`sh migrate.sh <usuário> <"senha"> <IP do servidor Monsta atual> <porta ssh>`

Exemplo:

```shell
sh migrate.sh root "minha senha" 192.168.1.1 22
```

O script finalizará os processos do Monsta em execução no antigo servidor (192.168.1.1) e iniciará a cópia da estrutura com os dados para o novo servidor. Ao final do processo você poderá acessar o seu Monsta no novo servidor e o antigo poderá ser desativado.

:::note
O tempo decorrido desta transferência dependerá do tamanho da base de dados existente, podendo levar de minutos a algumas horas.
:::

:::danger[Importante]
Para que o script do migrate seja executado com sucesso e garanta a cópia e criação de todos os arquivos e diretórios com as permissões corretas (incluindo arquivos de sistema, logs, e configurações sensíveis), é **obrigatório** que a execução seja feita por um usuário com privilégios de **Superusuário (`root`)** em **ambos os servidores** (Origem e Destino). A execução com um usuário não root ocasionará problemas durante a transferência dos dados.  
  
Caso ocorra algum erro de **timeout** durante a execução do `migrate.sh`, verifique se a porta do SSH no servidor remoto está aberta no firewall para acesso do servidor local.  
  
Em caso de falha, mesmo seguindo as instruções de uso do `migrate.sh`, **colete os logs exibidos na tela e entre em contato com nossa equipe de suporte**.
:::
