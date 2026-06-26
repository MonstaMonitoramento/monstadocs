---
title: "Gerenciamento de Firewall - UFW"
sidebar:
  order: 4
---

**UFW** significa **Uncomplicated Firewall** (Firewall Descomplicado).

Ele é uma interface para gerenciar o firewall Netfilter no Linux, que é o sistema de filtragem de pacotes do sistema. O UFW foi desenvolvido com o objetivo de simplificar o processo de configuração de regras de firewall através do utilitário `iptables`.

O UFW é o método mais popular e recomendado para gerenciar o firewall em distribuições baseadas em Debian e Ubuntu.

### Exemplos de Comandos UFW (Guia Prático)

A maioria dos comandos UFW exige privilégios de superusuário (`sudo`).

#### 1. Verificação de Status

Verifique se o UFW está ativo e veja as regras atuais:



| **Ação** | **Comando** | **Saída de Exemplo** |
| --- | --- | --- |
| **Verificar Status** | `ufw status` | `Status: inactive` (ou `active`) |
| **Verificar Detalhes** | `ufw status verbose` | Lista todas as regras de forma detalhada. |



#### 2. Ativação e Desativação

É crucial definir as regras antes de ativar, para não se trancar para fora do servidor.



| **Ação** | **Comando** | **Observação** |
| --- | --- | --- |
| **Ativar UFW** | `ufw enable` | **Atenção**: Se não tiver uma regra `allow ssh`, você perderá o acesso remoto. |
| **Desativar UFW** | `ufw disable` | Remove o firewall (não recomendado). |
| **Resetar Regras** | `ufw reset` | Remove todas as regras definidas pelo usuário. |



#### 3. Políticas Padrão (Default)

Configure o que acontece com o tráfego que não corresponde a nenhuma regra específica.



| **Ação** | **Comando** | **Resultado** |
| --- | --- | --- |
| **Bloquear Entrada (Recomendado)** | `ufw default deny incoming` | Nenhuma conexão externa é permitida, a menos que especificada. |
| **Permitir Saída** | `ufw default allow outgoing` | Seu servidor pode iniciar conexões com o mundo exterior. |



#### 4. Adicionar Regras (Permissões)



| **Objetivo** | **Comando** | **Observação** |
| --- | --- | --- |
| **Permitir SSH (Porta 22)** | `ufw allow ssh` | Usa o nome do serviço para liberar a porta 22/TCP. |
| **Permitir HTTP (Porta 80)** | `ufw allow http` | Libera a porta 80/TCP. |
| **Permitir HTTPS (Porta 443)** | `ufw allow 443/tcp` | Libera pelo número da porta e protocolo. |
| **Porta Específica** | `ufw allow 5432/udp` | Libera a porta 5432 apenas para o protocolo UDP. |
| **Tráfego de IP Específico** | `ufw allow from 192.168.1.100 to any port 3306` | Permite que apenas o IP `192.168.1.100` acesse a porta 3306 (MySQL). |



#### 5. Remover Regras

A remoção pode ser feita pelo número da regra ou pelo texto da regra.



| **Ação** | **Comando** | **Observação** |
| --- | --- | --- |
| **Remover por Texto** | `ufw delete allow http` | Remove a regra de acesso a porta http (80/TCP). |
| **Remover por Número** | `ufw status numbered` `ufw status delete [número]` | O primeiro comando retorna uma lista com as regras existentes e sua posição, o segundo remove a regra na posição selecionada. |

