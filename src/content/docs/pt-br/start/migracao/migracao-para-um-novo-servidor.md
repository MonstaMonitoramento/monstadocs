---
title: Migração para um Novo Servidor
description: Aprenda como migrar o Monsta para um novo servidor preservando
  configurações, monitoramentos, histórico e dados da plataforma com segurança.
---
Este tutorial mostra como migrar o Monsta a partir da versão >5.0 para outro servidor.

:::danger[Atenção]

Não instale o Monsta no novo servidor! Este procedimento deve ser realizado em um Linux sem um Monsta instalado. O script de migração realiza todo o processo de cópia dos dados e instalação do Monsta.

:::

## Requisitos mínimos

Requisitos mínimos para a migração do Monsta:

:::caution
Verifique se a partição "/var" do novo servidor possui o espaço suficiente para transferência dos dados do Monsta do servidor atual.
:::


| Item | Requisito Mínimo |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Espaço em disco](/src/assets/images/p25_image-1645452261754.png) | **Espaço em disco** 40GB livre para /var (configurações, banco de dados e logs) 300MB livre para /opt/monsta (programas e bibliotecas) Certifique-se de que a nova instalação possui espaço o suficiente para efetuar a migração. |
| ![Memória RAM](/src/assets/images/p25_image-1645452312898.png) | **Memória RAM** 2GB de memória RAM |
| ![Sistema Operacional](/src/assets/images/p25_image-1645452455434.png) | **Sistema Operacional** Linux 64bits Sistema Operacional Linux recomendado: Fedora Server 40 (x86_64 systems) ou Ubuntu Server 24. Pode ser utilizada a instalação mínima para o Monsta. |
| ![Processador](/src/assets/images/p25_image-1645452542916.png) | **Processador** Cores: 2 Velocidade: 1.8GHz |


:::note
As configurações acima permitem, em geral, verificar aproximadamente 500 dispositivos com 10 monitores cada ou um total de 5.000 monitores.
:::

## Script de migração

Logado como root no seu servidor, baixe o script de migração conforme exemplo abaixo:

### Fedora/Red-Hat/Ubuntu/Debian

```shell
yum install -y wget
wget https://www.monsta.com.br/monsta/download/migrate.sh
```

## Iniciando a transferência

Após baixar o script, execute-o com a seguinte sintaxe:

`./migrate.sh`

Antes de iniciar o processo de migração e instalação do Monsta, o script solicitará as informações de acesso SSH ao servidor de origem: endereço IP/hostname, porta de conexão e usuário com privilégios de root.

Esses dados são necessários para estabelecer uma conexão remota segura entre os ambientes. A partir desse acesso, o script irá interromper os serviços no servidor antigo, transferir a estrutura completa de arquivos, logs e bancos de dados preservando as permissões de arquivo, e registrar e inicializar os serviços do Monsta no novo servidor.

:::note
O tempo decorrido desta transferência dependerá do tamanho da base de dados existente, podendo levar de minutos a algumas horas.
:::

:::danger[Importante]
Para que o script do migrate seja executado com sucesso e garanta a cópia e criação de todos os arquivos e diretórios com as permissões corretas (incluindo arquivos de sistema, logs, e configurações sensíveis), é **obrigatório** que a execução seja feita por um usuário com privilégios de **Superusuário (`root`)** em **ambos os servidores** (Origem e Destino). 

Caso ocorra algum erro de **timeout** durante a execução do `migrate.sh`, verifique se a porta do SSH no servidor remoto está aberta no firewall para acesso do servidor local.  

Em caso de falha, mesmo seguindo as instruções de uso do `migrate.sh`, **colete os logs exibidos na tela e entre em contato com nossa equipe de suporte**.
:::