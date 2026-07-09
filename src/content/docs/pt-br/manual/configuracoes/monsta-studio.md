---
title: "Monsta Studio"
sidebar:
  order: 5
---

O Monsta Studio gerencia os mecanismos de coletas, alertas e ações do Monsta. As fontes disponibilizadas neste local estarão disponíveis para os dispositivos, monitores e grupos de alerta.

## Tela Inicial

![image-1739987060103.png](../../../../../assets/images/p62_image-1739987060103.png)

---

![image-1739987089441.png](../../../../../assets/images/p62_image-1739987089441.png)
Listagem das fontes disponíveis e sua localização no Monsta. 

| Item | Descrição |
| :---: | :--- |
| Métricas | São as fontes utilizadas nas coletas de dados dos monitores. |
| Instâncias | São as fontes utilizadas na aba "Instâncias" durante a criação ou edição dos monitores. |
| Uptime | São as fontes utilizadas para checar o uptime durante a criação ou edição do dispositivo. |
| ![image-1739987364857.png](../../../../../assets/images/p62_image-1739987364857.png) | Categoria da fonte. Utilizada para uma melhor organização da lista. |
| ![image-1647622602480.png](../../../../../assets/images/p62_image-1647622602480.png) | Adiciona uma nova fonte de dados dentro da localização selecionada. | 

## Editor de Fontes

Nesta tela são criadas ou personalizadas as fontes de dados.

![image-1739987456748.png](../../../../../assets/images/p62_image-1739987456748.png)

#### Detalhes

![image-1647623122977.png](../../../../../assets/images/p62_image-1647623122977.png)
Exibe a tela para a edição de informações da fonte, como nomes e parâmetros.

| Opção / Ícone | Descrição |
| :---: | :--- |
| ![image-1739987483509.png](../../../../../assets/images/p62_image-1739987483509.png) | Seleciona um ícone para a fonte em evidência. |
| **Nome** | Informa um nome para a fonte. Esse nome é o que será mostrado nas listagens de fontes disponíveis. |
| **Descrição** | Breve comentário sobre o que faz a fonte. |
| **Categoria** | Informa em qual categoria a fonte se encontra. |
| **Tipo de Retorno** | Tipo de valor retornado ao final da execução da fonte. Pode ser um número, uma string, um texto, uma tabela, entre outros. |
| **Parâmetros** | São variáveis configuradas para serem utilizadas pelo código fonte da programação. É possível configurar um valor padrão para cada variável, assim como o usuário pode alterá-la durante a sua execução. |
| ![image-1739987532048.png](../../../../../assets/images/p62_image-1739987532048.png) | Nome da variável. |
| ![image-1739987551030.png](../../../../../assets/images/p62_image-1739987551030.png) | Tipo de valor da variável. |
| ![image-1739987627316.png](../../../../../assets/images/p62_image-1739987627316.png) | Define um valor padrão para a variável. |
| ![image-1739987708487.png](../../../../../assets/images/p62_image-1739987708487.png) | Um comentário sobre a variável. Essa informação aparecerá quando o mouse estiver sobre o campo de valor durante a execução. |
| ![image-1647624115398.png](../../../../../assets/images/p62_image-1647624115398.png) | Se marcado, a variável deverá ter um preenchimento obrigatório. |
| ![image-1647624151382.png](../../../../../assets/images/p62_image-1647624151382.png) | Se marcado a variável poderá ser duplicada pelo usuário. |
| ![image-1647624197215.png](../../../../../assets/images/p62_image-1647624197215.png) | Posição de exibição da variável na listagem. |
| ![image-1647624227451.png](../../../../../assets/images/p62_image-1647624227451.png) | Remove a variável selecionada. |

#### Código

![image-1647624338287.png](../../../../../assets/images/p62_image-1647624338287.png)
Nesta opção será apresentado o editor de código do Monsta. A linguagem de programação suportada será o LUA ([https://www.lua.org](https://www.lua.org/)). Para maiores informações sobre comandos e funções, consulte o [Scripting com LUA](/pt-br/tech/modulos-script/script-lua) ou [https://www.lua.org/manual/](https://www.lua.org/manual/). |

| Opção / Ícone | Descrição |
| :---: | :--- |
| ![image-1647625589954.png](../../../../../assets/images/p62_image-1647625589954.png) | Salva a edição de código atual. |
| ![image-1647625628655.png](../../../../../assets/images/p62_image-1647625628655.png) | Exporta a fonte em evidência para um arquivo. |
| ![image-1647625699048.png](../../../../../assets/images/p62_image-1647625699048.png) | Remove a fonte em evidência. Esse processo apenas é permitido se a mesma não estiver em uso. |
| ![image-1647625745603.png](../../../../../assets/images/p62_image-1647625745603.png) | Código de identificação da fonte para pesquisas. |
| ![image-1647625807586.png](../../../../../assets/images/p62_image-1647625807586.png) | Exibe as saídas e retorno do script quando executado. |
| ![image-1647625896651.png](../../../../../assets/images/p62_image-1647625896651.png) | Configura fonte e tamanho dos caracteres no editor de scripts. |
| ![image-1647625957430.png](../../../../../assets/images/p62_image-1647625957430.png) | Informa o tipo de linguagem utilizada pelo script. |
| ![image-1739988046784.png](../../../../../assets/images/p62_image-1739988046784.png) | Seleciona o dispositivo no qual será executado o teste do script. |
| ![image-1739988315966.png](../../../../../assets/images/p62_image-1739988315966.png) | Permite inserir valores nos parâmetros quando existentes. |
| ![image-1647625532238.png](../../../../../assets/images/p62_image-1647625532238.png) | Editor de código do Monsta. |
| ![image-1647626507459.png](../../../../../assets/images/p62_image-1647626507459.png) | Executa o script para fins de teste. |
