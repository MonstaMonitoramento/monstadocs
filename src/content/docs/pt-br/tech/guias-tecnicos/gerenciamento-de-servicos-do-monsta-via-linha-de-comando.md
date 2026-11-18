---
title: "Gerenciamento de Serviços do Monsta via Linha de Comando (Linux)"
description: Descubra para parar, iniciar e verificar o status dos serviços do Monsta através de comandos no Linux.
---

Este artigo descreve os procedimentos padrão para iniciar, parar e verificar o status dos serviços do **Monsta** em sistemas operacionais Linux utilizando o utilitário `systemd` (`systemctl`).

---

## 1. Inicialização dos Serviços (Start)

A inicialização dos serviços do Monsta deve seguir uma **ordem específica** de dependências para garantir que a infraestrutura subjacente esteja pronta antes que os módulos de roteamento e atualização sejam ativados.

Execute os comandos abaixo sequencialmente no terminal com privilégios de superusuário (`sudo`):

```bash
# 1. Iniciar o banco de dados
sudo systemctl start monsta-com.monstadb.service

# 2. Iniciar o monagent, responsável pelas coletas
sudo systemctl start monsta-com.monagent.service

# 3. Iniciar o core do sistema, responsável pelos logs e a interface entre os demais serviços e o banco de dados
sudo systemctl start monsta-com.monkernel.service

# 4. Iniciar o servidor http responsável por fornecer a interface http para o usuário
sudo systemctl start monsta-com.monrouter.service

# 5. Iniciar o subsistema que verifica periodicamente por novas atualizações
sudo systemctl start monsta-com.monstaupd.service
```

---

## 2. Encerramento dos Serviços (Stop)

Para interromper o funcionamento dos serviços, você pode optar por encerrá-los individualmente ou todos de uma única vez.

### Parada Individual

Substitua `<nome-do-servico>` pelo identificador correspondente (por exemplo, `monstaupd`, `monrouter`, etc.):

```bash
sudo systemctl stop monsta-com.<nome-do-servico>.service
```

### Parada Completa (Todos os Serviços)

Para parar **todos** os serviços do ecossistema Monsta simultaneamente de forma rápida, utilize o curinga (`*`):

```bash
sudo systemctl stop monsta-com.*
```

---

## 3. Verificação de Status

Para verificar se um serviço específico está em execução, ativo e se há mensagens recentes de log relacionadas ao seu estado, utilize o comando `status`:

```bash
sudo systemctl status monsta-com.<nome-do-servico>.service
```

*Exemplo para verificar o status do banco de dados:*

```bash
sudo systemctl status monsta-com.monstadb.service
```
