---
title: "Grupos de Alerta"
---

![image-1756129907740.png](../../../../../assets/images/p37_image-1756129907740.png)

:::caution[Atenção]
O funcionamento deste recurso necessita, obrigatoriamente, que o software do Monsta possua comunicação com o host mind.monsta.com.br.
:::

:::tip
A tela de alertas permite trabalhar com grupos onde são informados os contatos que deverão receber os devidos avisos quando um dispositivo ou monitor mudar seu “status”.
:::

## Grupos

Nesta tela são gerenciados os grupos de usuários que receberão as notificações e o tipo de serviço, seja por e-mail ou SMS.

| Opção | Descrição |
| :---: | :--- |
| ![image-1645792155732.png](../../../../../assets/images/p37_image-1645792155732.png) | **Novo Grupo**: Cria um novo grupo para envio de alertas. |
| ![image-1645792160782.png](../../../../../assets/images/p37_image-1645792160782.png) | **Procurar Grupo**: Exibe na tela apenas os grupos que combinam com a pesquisa digitada. |
| ![image-1756129930291.png](../../../../../assets/images/p37_image-1756129930291.png) | **Grupo Nuvem**: Este grupo envia alertas em caso de perda de comunicação entre o Monsta e a nuvem em [https://mind.monsta.com.br](https://mind.monsta.com.br). Esse recurso é muito útil em casos como queda do link de internet na empresa ou desligamento inesperado do servidor sem o devido conhecimento do usuário. Este grupo não pode ser removido do sistema e não está disponível para dispositivos ou monitores.<br />A cor de sua borda indica o status da conexão com a nuvem:<br />- **Verde**: Comunicação estabelecida;<br />- **Vermelho**: Falha na comunicação. |
| ![image-1756129950105.png](../../../../../assets/images/p37_image-1756129950105.png) | **Grupo Padrão**: Este grupo é obrigatório no sistema e não pode ser deletado, apenas alterado. O número informado no canto superior direito da caixa de grupo refere-se ao número de dispositivos que o utilizam em seus alertas. Quando a caixa do grupo é apresentada na cor cinza, isso indica que ele não possui alertas ativados. |
| ![image-1732710101229.png](../../../../../assets/images/p37_image-1732710101229.png) | **Alertas ativos**: Os ícones apresentados dentro da caixa do grupo indicam quais alertas estão ativos no momento para ele. |
| ![image-1732710190977.png](../../../../../assets/images/p37_image-1732710190977.png) | **Excluir Grupo**: Exclui o grupo selecionado. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Atenção</p>Só será permitido remover um grupo quando o mesmo não faz parte de nenhum dispositivo ou monitor. Essa informação você poderá obter na aba [Membros](#membros) ao editar o grupo.</aside> |
| ![image-1645792184443.png](../../../../../assets/images/p37_image-1645792184443.png) | **Editar Grupo**: Nessa opção o usuário poderá adicionar e remover dispositivos e monitores que fazem parte deste grupo, assim como definir os tipos de alerta que serão enviados, seus destinatários e os horários de disparo permitidos para as mensagens. |



### Editando grupos de alertas

#### Detalhes

Nessa aba são definidos o ícone, nome e comentário sobre o grupo.

![image-1732711113493.png](../../../../../assets/images/p37_image-1732711113493.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1732710589288.png](../../../../../assets/images/p37_image-1732710589288.png) | É possível atribuir uma imagem ao grupo de alerta que será exibida em tela. |
| **Nome do grupo de alerta** | É o nome que será apresentado na tela de grupos, assim como o que será exibido ao editar a opção de grupos de alerta dentro dos dispositivos ou monitores. |
| **Descrição** | Permite adicionar um comentário sobre o grupo em evidência. |

#### Membros  


Nessa aba é possível visualizar os dispositivos e monitores nos quais receberão alertas deste grupo, assim como adicionar novos dispositivos ou remover os existentes.

![image-1739974572520.png](../../../../../assets/images/p37_image-1739974572520.png)

| Opção | Descrição |
| :---: | :--- |
| **Todos** | Esse componente mostra todos os dispositivos existentes no Monsta. Clique sobre um dispositivo para selecioná-lo e utilize os botões ao lado para adicioná-lo ao grupo. |
| **Selecionados** | Esse componente mostra os dispositivos e monitores que fazer parte do grupo em evidência. Clique sobre um item para selecioná-lo e utilize os botões ao lado para removê-lo do grupo. |



#### Alertas Monsta  


Essa aba mostra os alertas padrão do Monsta que utilizam nossa nuvem para serem disparados aos destinatários. As opções de envio existentes são E-mail, SMS e Telegram. Os Alertas Monsta não necessitam de configurações especiais pois são automaticamente intregrados a nuvem durante a instalação do software. 

![image-1732712034593.png](../../../../../assets/images/p37_image-1732712034593.png) 
Para facilitar a visualização, os alertas ativos são marcados com o ícone acima em sua aba.


![image-1732711910237.png](../../../../../assets/images/p37_image-1732711910237.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1732712383308.png](../../../../../assets/images/p37_image-1732712383308.png) | Ativa ou desativa o tipo de alerta em evidência. |
| ![image-1732712469323.png](../../../../../assets/images/p37_image-1732712469323.png) | Dispara um teste para os destinatários existentes. Essa opção é útil para verificar se todos os destinos estão configurados corretamente, como endereço de e-mail ou SMS ou usuários de Telegram. |
| ![image-1732712594374.png](../../../../../assets/images/p37_image-1732712594374.png) | Essas opções permitem selecionar o tipo de evento em que deverá ser enviado o alerta. Quando desmarcada, o Monsta não fará disparo para o status selecionado. |
| ![image-1732712693761.png](../../../../../assets/images/p37_image-1732712693761.png) | Aqui é possível escolher o objeto que será utilizado para o disparo de alertas. Você pode utilizar essa opção para receber alertas apenas de quando o dispositivo se torna incomunicável, mas opta por não receber um alerta se o monitor de CPU alarmar por estar com alta utilização. |
| **Template da mensagem** | Os templates são modelos de mensagens que serão enviadas aos usuários. Você pode personalizar como as mensagens serão enviadas para seus destinatários. Para maiores informações, consulte "Templates de mensagens". |
| ![image-1732713267486.png](../../../../../assets/images/p37_image-1732713267486.png) | Essa opção está disponível apenas para o Telegram. Ela informa os usuários que fazem parte do grupo e permite removê-los manualmente. Para ingressar um usuário, você deverá utilizar o código que aparece ao início desta tela e enviá-lo ao bot "MonstaTecnologiaBot". As instruções de como proceder estão especificadas nesta mesma tela. |
| ![image-1732713616303.png](../../../../../assets/images/p37_image-1732713616303.png) | Os períodos são o intervalo de tempo que os alertas poderão ser enviados. Ao criar um grupo o padrão é 24x7. Os quadrados em cinza indicam que os horários selecionados estão inativos e o Monsta não irá disparar alertas para o grupo nesses intervalos de tempo. |



## Centro de alertas

Nesta tela são gerenciados os grupos de usuários que receberão as notificações e o tipo de serviço, seja por e-mail ou SMS.

![image-1739974733737.png](../../../../../assets/images/p37_image-1739974733737.png)

![image-1739974790750.png](../../../../../assets/images/p37_image-1739974790750.png)  
**Barra de exibição**: Permite ao usuário estipular a quantidade de itens por página e o período que as informações devem ser exibidas na tela.


| Informação | Descrição |
| :---: | :--- |
| ![image-1739974961714.png](../../../../../assets/images/p37_image-1739974961714.png) | **Status**: Informa o estado da mensagem enviada para um usuário. |
| ![image-1739975105124.png](../../../../../assets/images/p37_image-1739975105124.png) | **Tipo**: Informa para qual meio a mensagem foi disparada. |
| ![image-1739975173561.png](../../../../../assets/images/p37_image-1739975173561.png) | **Data e hora**: Informa a data e hora do disparo. |
| ![image-1739975251006.png](../../../../../assets/images/p37_image-1739975251006.png) | **Destinatário**: Informa o destinatário da mensagem. Essa informação não está disponível para alertas pelo Telegram pelo fato das mensagens serem disparadas para o um Bot. |
| ![image-1739975341938.png](../../../../../assets/images/p37_image-1739975341938.png) | **Origem**: Informa o dispositivo e monitor que originou o alerta. |
| ![image-1739975429030.png](../../../../../assets/images/p37_image-1739975429030.png) | **Conteúdo**: Exibe o conteúdo disparado pelo alerta. |



## Templates de mensagem

Com nossos templates, você pode criar mensagens personalizadas para cada tipo de alerta, garantindo que as informações mais importantes sejam entregues aos responsáveis de forma rápida e eficiente. Escolha entre uma variedade de variáveis para incluir detalhes como o nome do dispositivo, a gravidade do alerta e o horário de ocorrência, entre várias outras.

![image-1732727391061.png](../../../../../assets/images/p37_image-1732727391061.png)



![image-1732727677203.png](../../../../../assets/images/p37_image-1732727677203.png)
Crie um novo template e personalize a mensagem como desejar.

---

![image-1732727745380.png](../../../../../assets/images/p37_image-1732727745380.png)
Esta é a caixa que representa o template existente. Ao clicar sobre ela o usuário acessa a opção de editar as informações existentes. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1732727824893.png](../../../../../assets/images/p37_image-1732727824893.png) | Remove o template existente. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Atenção</p>O template não poderá ser removido se estiver em uso por algum grupo de alerta. O template **Padrão** faz parte do sistema e também não poderá ser removido.</aside> |
| ![image-1732727887105.png](../../../../../assets/images/p37_image-1732727887105.png) | Abre a edição do template para o usuário. |

### Editando um template de mensagem

Nesta tela o usuário pode personalizar a mensagem enviada pelos grupos de alerta. Estão listadas as variáveis existentes que podem ser utilizadas e uma simples linguagem de programação para trabalhar com condições.

![image-1732728340150.png](../../../../../assets/images/p37_image-1732728340150.png)


| Opção | Descrição |
| :--- | :--- |
| **Nome** | É o nome que será apresentado na tela dos templates, assim como o que será exibido para seleção ao editar a opção de grupos de alerta. |
| **Corpo** | Esse é o texto da mensagem de alerta que será enviado para o usuário. Quando utilizadas variáveis ou comandos de programação, estes deverão estar, obrigatoriamente, entre "{{ }}". |
| **Variáveis do sistema** | São as variáveis com informações do sistema que estão disponíveis para serem utilizadas nos templates de alerta. Para agilizar na personalização do texto do corpo da mensagem com as variáveis, basta executar um "duplo clique" sobre a variável desejada que ela será inserida no texto. |



#### Variáveis do sistema

| Variável | Descrição
| --- | --- |
| `dataehora` | Retorna a data (d/m/a) e a hora atual (h:m). |
| `dispositivo.descricao` | Retorna a descrição do dispositivo. |
| `dispositivo.endereco` | Retorna o endereço IP do dispositivo. |
| `dispositivo.estado` | Retorna o estado atual do dispositivo obtido pelo monitor Uptime. |
| `dispositivo.estadoanterior` | Retorna o estado anterior do dispositivo obtido pelo monitor Uptime. |
| `dispositivo.nome` | Retorna o nome do dispositivo. |
| `estado` | Retorna o status do dispositivo. |
| `monitor.estado` | Retorna o estado atual do monitor. |
| `monitor.estadoanterior` | Retorna o estado anterior do monitor. |
| `monitor.nome` | Retorna o nome do monitor. |
| `monitor.nomecurto` | Retorna o nome informado no ícone do monitor. |
| `nome.metrica` | Retorna o nome da métrica. |
| `nome.instancia` | Retorna o nome da instância. |
| `valor` | Retorna o valor da leitura. |

:::caution[Atenção]
Não há suporte a *emojis* e imagens nos templates de alerta. A mensagem enviada pelo alerta deve ser apenas texto.
:::