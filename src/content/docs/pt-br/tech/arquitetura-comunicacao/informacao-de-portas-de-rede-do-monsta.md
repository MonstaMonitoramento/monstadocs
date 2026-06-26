---
title: "Portas de Rede do Monsta"
sidebar:
  order: 1
---

O **Monsta** foi projetado para operar com um conjunto mínimo e específico de portas de rede. Para fins de configuração de segurança no seu firewall, é importante saber quais portas são utilizadas e quais podem ser bloqueadas.

- - - - - -

## Portas de Rede Utilizadas

Por padrão, o Monsta requer acesso apenas às seguintes portas para o seu funcionamento normal e comunicação:

| Porta | Protocolo | Descrição |
| --- | --- | --- |
| **80** | **TCP** (HTTP) | Usada para comunicação **não criptografada** (HTTP). Se o Monsta for acessado sem SSL/TLS, esta porta será utilizada. |
| **443** | **TCP** (HTTPS) | Usada para comunicação **segura e criptografada** (HTTPS). Esta é a porta **preferencial** para acesso seguro. |

Além disso, o Monsta pode realizar **acessos internos** que se originam de e se destinam ao `localhost` (o próprio servidor onde o Monsta está instalado). Tais comunicações internas geralmente **não são afetadas** pelas regras de firewall que governam o tráfego de entrada/saída da rede externa.

## Recomendação de Segurança (Firewall)

Para maximizar a segurança do sistema onde o Monsta está hospedado, recomendamos a seguinte configuração de firewall:

- **Permitir** o tráfego de entrada (Inbound) nas portas **80 (HTTP)** e **443 (HTTPS)**.
- **Permitir** todos os acessos de e para o `localhost` - 127.0.0.1 (IPv4) e ::1 (IPv6).
- **Bloquear (Deny/Drop)** todas as **demais portas** não utilizadas.

Bloquear portas não utilizadas reduz a **probabilidade de ataques** ao servidor, prevenindo tentativas de exploração em serviços que não são necessários para a operação do Monsta.