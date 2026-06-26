---
title: "Serviços"
sidebar:
  order: 12
---

![image-1756129281788.png](../../../../../assets/images/p115_image-1756129281788.png)

A tela **Gerenciar Serviços** oferece uma visão geral do estado dos serviços essenciais para o funcionamento do Monsta. Ela permite que você monitore e gerencie cada serviço individualmente, garantindo que o sistema opere sem interrupções.

## Como Usar

Nesta tela, você verá uma lista de serviços, cada um com as seguintes informações:

- **Nome do Serviço**: O nome do serviço em execução.
- **Status**: O estado atual do serviço, indicado por um ícone de status. Os status mais comuns são:    
    - **Verde**: O serviço está **ativo** e funcionando corretamente.
    - **Vermelho**: O serviço está **inativo** ou com algum problema.
- **Horário de Início**: Informa a data e hora em que o serviço foi iniciado.
- **Ações**: Nesta coluna, você encontra o botão para **reiniciar** o serviço.    
    - **Reiniciar**: Clique neste botão para reiniciar um serviço específico. Isso pode ser útil para resolver problemas pontuais sem precisar reiniciar todo o sistema.

## Serviços

| Serviço | Descrição |
| --- | --- |
| `monkernel` | É o core do sistema, responsável pelos logs e a interface entre os demais serviços e o banco de dados. |
| `monagent` | Responsável pela coleta de informações dos equipamentos. |
| `monstaupd` | É o subsistemas que verifica periodicamente por novas atualizações do Monsta. |
| `monrouter` | É o servidor http responsável por fornecer a interface http para o usuário. |
| `monstadb` | Banco de dados das coletas de informações. |
