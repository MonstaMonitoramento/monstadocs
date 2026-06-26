---
title: "Grupo de Dispositivos"
sidebar:
  order: 4
---

O Monsta permite criar grupos no qual podem ser cadastrados dispositivos de forma individual. Os dispositivos cadastrados em um grupo herdam suas configurações, tais como usuários, senhas, dados de snmp, e estas se sobrepõem as configurações globais.

Grupos de dispositivos são utilizados para otimizar tarefas de rotina, como configurações, disponibilizar para um usuário quais dispositivos ele tem acesso ou para uma visualização rápida do status geral dos seus dispositivos cadastrados.

![image-1739988728084.png](../../../../../assets/images/p65_image-1739988728084.png)

---

![image-1647884450145.png](../../../../../assets/images/p65_image-1647884450145.png)
**Novo grupo de dispositivos**: Cria um novo grupo.

---

![image-1739988753787.png](../../../../../assets/images/p65_image-1739988753787.png)
**Procurar grupos**: Filtra os grupos de acordo com o texto informado.

---

![image-1739988818350.png](../../../../../assets/images/p65_image-1739988818350.png)
**Caixa de Grupo**: Apresenta o nome do grupo e uma visualização rápida sobre a quantidade de dispositivos cadastrados e seus status. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1739988847442.png](../../../../../assets/images/p65_image-1739988847442.png) | Informa o total de dispositivos cadastrados no grupo por status. |
| ![image-1739988866136.png](../../../../../assets/images/p65_image-1739988866136.png) | Informa o nome do grupo. |
| ![image-1647884315767.png](../../../../../assets/images/p65_image-1647884315767.png) | Atribui ações que serão herdadas pelo grupo. Para mais informações, consulte [Opções Globais](/pt-br/manual/dispositivos/opcoes#opções-globais-de-dispositivos). |
| ![image-1647884360825.png](../../../../../assets/images/p65_image-1647884360825.png) | Adiciona um novo dispositivo ao grupo selecionado. |
| ![image-1647884405279.png](../../../../../assets/images/p65_image-1647884405279.png) | Abre a tela de edição do grupo. |



## Adicionar/Editar um grupo de dispositivos

![image-1739988994615.png](../../../../../assets/images/p65_image-1739988994615.png)

### Detalhes

Informações básicas sobre o grupo. 

| Opção | Descrição |
| :---: | :--- |
| ![image-1739989016556.png](../../../../../assets/images/p65_image-1739989016556.png) | Permite selecionar um ícone para o grupo. |
| **Nome do grupo de dispositivos** | Permite informar um nome para o grupo em edição. |
| **Descrição** | Um breve comentário sobre o grupo em edição. |

### Membros
São os dispositivos que fazer parte do grupo.


| Ícone | Descrição |
| :---: | :--- |
| ![image-1739989077427.png](../../../../../assets/images/p65_image-1739989077427.png) | Listagem de membros do grupo. |
| ![image-1739989114437.png](../../../../../assets/images/p65_image-1739989114437.png) | Adiciona ou remove membros selecionados. |
| ![image-1739989148209.png](../../../../../assets/images/p65_image-1739989148209.png) | Adiciona ou remove todos os membros. |

### Coleta
São as configurações dos principais métodos de busca que serão herdadas pelos dispositivos que fazem parte do grupo. Para mais informações, consulte [Coleta](/pt-br/manual/dispositivos/novo-dispositivo#coleta).

### Sons de Alerta
Configura os sons de alertas que serão herdados pelos dispositivos membros deste grupo. Para mais informações, consulte [Sons de Alerta](/pt-br/manual/dispositivos/novo-dispositivo#grupos-de-alerta).

### Sensibilidade
Define o comportamento do uptime pelos dispositivos membros deste grupo. Para mais informações, consulte [Sensibilidade](/pt-br/manual/dispositivos/opcoes#sensibilidade).
