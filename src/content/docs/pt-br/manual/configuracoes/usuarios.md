---
title: "Usuários"
sidebar:
  order: 9
---

O Monsta é multi-usuário, ou seja, ele permite que vários usuários sejam utilizados simultaneamente no sistema com permissões personalizadas. O sistema de gerenciamento de usuários do Monsta permite informar quais dispositivos, grupos, painéis ou grupos de alerta podem ser visualizados e gerenciados por cada integrante.

![image-1647888175595.png](../../../../../assets/images/p66_image-1647888175595.png)

| Ícone / Opção | Descrição |
| :---: | :--- |
| ![image-1647888202156.png](../../../../../assets/images/p66_image-1647888202156.png) | Adiciona um novo usuário para acessar a plataforma. |
| **Admin** | Quando marcado, indica que o usuário na lista tem permissões de administrador e acesso a todos os dispositivos, monitores e recursos disponíveis. |
| **Login** | É o nome para login no Monsta. |
| **Nome** | Nome do usuário. |
| ![image-1647888352963.png](../../../../../assets/images/p66_image-1647888352963.png) | Edita as propriedades do usuário selecionado. |
| ![image-1647888388977.png](../../../../../assets/images/p66_image-1647888388977.png) | Clona as propriedades do usuário atual para um novo. |
| ![image-1647888449977.png](../../../../../assets/images/p66_image-1647888449977.png) | Remove o usuário selecionado. |



## Criar/Editar um Usuário

### Detalhes
São informações básicas do usuário. 

| Opção | Descrição |
| :--- | :--- |
| **Login** | Nome do usuário. Não pode ser alterado para usuários já existentes. |
| **Nome Completo** | Informação do nome completo do usuário. |
| **Alterar Senha** | Permite trocar a senha do usuário em edição. |
| ![image-1647888733932.png](../../../../../assets/images/p66_image-1647888733932.png) | **Administrador**: Atribui propriedades de administrador quando ativada. O usuário terá acesso a todos os dispositivos, monitores e recursos disponíveis no Monsta. <aside class="starlight-aside starlight-aside--note">Quando um usuário não é administrador, a visão hierárquica não será liberada para ele.</aside> |


### Dispositivos
Permite ao administrador definir exatamente quais dispositivos um usuário específico poderá visualizar e gerenciar no sistema.

| Ícone / Opção | Descrição |
| :--- | :--- |
| ![image-1647889770987.png](../../../../../assets/images/p66_image-1647889770987.png) | **Gravação**: O usuário recebe permissões de escrita (alteração). Ele poderá:<br />• Alterar e Remover Dispositivos;<br />• Adicionar, Alterar e Remover Monitores (serviços/métricas) nos dispositivos existentes.<br /><br />Quando desmarcado, o usuário só pode visualizar dados. Nenhuma alteração é permitida na lista de dispositivos, monitores ou em suas configurações. |
| ![image-1739989429159.png](../../../../../assets/images/p66_image-1739989429159.png) | **Filtro de Dispositivos**: Filtra os dispositivos pelo texto informado. |
| ![image-1739989466314.png](../../../../../assets/images/p66_image-1739989466314.png) | **Lista de Dispositivos**: Na coluna à esquerda estão listados todos os dispositivos que estão sendo monitorados no Monsta. Já na coluna a direita, são listados os dispositivos que o usuário poderá visualizar e interagir. Estes são os ativos que o usuário vai acessar. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Botões de Seleção Individual**: Move os dispositivos selecionados entre as colunas da lista de dispositivos. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Botões de Seleção Geral**: Move todos os dispositivos de uma coluna para a outra na lista de dispositivos. |



### Grupos
Configura os grupos no qual o usuário terá acesso aos dispositivos membros.



| Ícone / Opção | Descrição |
| :--- | :--- |
| ![image-1739989584199.png](../../../../../assets/images/p66_image-1739989584199.png) | **Lista de Grupos de Dispositivos**: Na coluna à esquerda estão listados todos os grupos cadastrados no Monsta. Já na coluna a direita, são listados os grupos que o usuário terá acesso. Os dispositivos pertencentes a esse grupo serão listados na aba "Dispositivos", na coluna a direita, marcados apenas como leitura. |
| ![image-1739989429159.png](../../../../../assets/images/p66_image-1739989429159.png) | **Filtro de Grupos de Dispositivos**: Filtra os grupos pelo texto informado. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Botões de Seleção Individual**: Move os grupos selecionados entre as colunas da lista de grupos de dispositivos. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Botões de Seleção Geral**: Move todos os grupos de uma coluna para a outra na lista de grupos de dispositivos. |



### Grupos de Alerta
Configura os grupos de alerta no qual o usuário terá acesso.

| Ícone / Opção | Descrição |
| :--- | :--- |
| ![image-1647889770987.png](../../../../../assets/images/p66_image-1647889770987.png) | **Gravação**: O usuário recebe permissões de escrita (alteração). Ele poderá:  Alerta.<br /><br />Quando desmarcado, o usuário só pode visualizar dados. Nenhuma alteração é permitida nos grupos de alerta. |
| ![image-1739989663950.png](../../../../../assets/images/p66_image-1739989663950.png) | **Filtro de Grupos de Alerta**: Filtra os grupos pelo texto informado. |
| ![image-1739989506457.png](../../../../../assets/images/p66_image-1739989506457.png) | **Botões de Seleção Individual**: Move os grupos selecionados entre as colunas da lista de grupos de alerta. |
| ![image-1739989535974.png](../../../../../assets/images/p66_image-1739989535974.png) | **Botões de Seleção Geral**: Move todos os grupos de uma coluna para a outra na lista de grupos de alerta. |
