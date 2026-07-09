---
title: "Novo Dispositivo"
sidebar:
  order: 6
---

Ao clicar sobre o botão "Novo" é possível adicionar um dispositivo ao monitoramento do Monsta.

## Detalhes

Define as informações básicas sobre o equipamento.

![image-1739970776422.png](../../../../../assets/images/p51_image-1739970776422.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1646855537251.png](../../../../../assets/images/p51_image-1646855537251.png) | **Ícone**: Permite selecionar um ícone para o dispositivo. |
| ![image-1646855610278.png](../../../../../assets/images/p51_image-1646855610278.png) | **Nome do dispositivo**: Será o nome exibido nos modos de visualização. |
| ![image-1646855698393.png](../../../../../assets/images/p51_image-1646855698393.png) | **Endereço do dispositivo**: É o endereço IPv4, IPv6 ou host do dispositivo. É possível pingar o endereço para testá-lo. |
| ![image-1646855946392.png](../../../../../assets/images/p51_image-1646855946392.png) | **Descrição do dispositivo**: Permite inserir um breve texto sobre o equipamento. |
| ![image-1646856003694.png](../../../../../assets/images/p51_image-1646856003694.png) | **Agente**: Local onde serão disparadas as coletas do dispositivo. Essa informação é de apenas leitura. |
| ![image-1646856167964.png](../../../../../assets/images/p51_image-1646856167964.png) | **Monitor de uptime**: Método utilizado para identificar se o dispositivo está ativo. O padrão é o envio de pacotes icmp echo-request (ping). Os métodos de verificação podem permitir que sejam informados alguns parâmetros para consultas, como por exemplo o tamanho do pacote icmp a ser enviado ou a porta TCP a ser verificada no dispositivo. |
| ![image-1732555718867.png](../../../../../assets/images/p51_image-1732555718867.png) | **Sensibilidade**: Configura o nível de sensibilidade do dispositivo para pacotes do tipo ping (icmp). Para maiores informações, consulte a página [Sensibilidade](/pt-br/manual/dispositivos/opcoes#sensibilidade). |



## Templates

São os monitores disponíveis para cada tido de equipamento. Cada template possui monitores específicos para serem utilizados. e mais de um template pode ser utilizado em um dispositivo.

![image-1646856297549.png](../../../../../assets/images/p51_image-1646856297549.png)

| Opção | Descrição |
| :--- | :--- |
| **Selecionados** | São os templates utilizados nesse dispositivo. |
| **Usado frequentemente** | É uma lista dos templates mais utilizados no seu Monsta o que permite uma seleção mais ágil. |
| **Todos** | É a listagem de todos os templates disponíveis no Monsta. |



## Pai

Define a dependência hierárquica do ativo. Utilizado para organizar o mapa da rede e otimizar o sistema de notificações, relacionando dispositivos as suas dependências.

:::caution[Importante]
Essas informações serão utilizadas pelo sistema de envio de alertas para que o Monsta dispare uma comunicação apenas do dispositivo que está com problema.
:::



![image-1769000388348.png](../../../../../assets/images/p51_image-1769000388348.png)

## Coleta

Nesta tela aparecem os principais métodos para busca de informações dos dispositivos utilizados pelo Monsta. Sua principal funcionalidade é permitir que o usuário utilize uma configuração padrão para os monitores utilizados além de testar se a comunicação está funcional.

![image-1739970973988.png](../../../../../assets/images/p51_image-1739970973988.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1739971005493.png](../../../../../assets/images/p51_image-1739971005493.png) | **Métodos de coleta**: São os tipos de coleta padrão executados pelo Monsta. Ao clicar sobre esse métodos é possível configurar parâmetros gerais que serão utilizados pelos monitores dos dispositivos. Para coletar dados de Servidores e Estações Windows, utilize a Sonda. Para maiores informações, consulte nosso tutorial [Sonda: Monitoramento de Servidores e Estações Windows](/pt-br/start/instalacao/sonda-windows). |
| ![image-1646915286768.png](../../../../../assets/images/p51_image-1646915286768.png) | **Herdar do Grupo ou Global**: Esta propriedade, quando marcada, obtém os valores configurados globalmente ou do grupo no qual o dispositivo pertence. Para maiores informações consulte [Opções globais de dispositivos](/pt-br/manual/dispositivos/opcoes#opções-globais-de-dispositivos). |
| ![image-1646913740044.png](../../../../../assets/images/p51_image-1646913740044.png) | **Propriedade**: Permite alterar o valor dessa propriedade da coleta. Caso a opção "Herdar valor do grupo ou global" esteja marcada essa propriedade herdará o valor configurado. |
| ![image-1732556926759.png](../../../../../assets/images/p51_image-1732556926759.png) | **Exponencial**: Quando disponível, utiliza um algoritmo de timeout para a coleta. Esse algoritmo dobra o tempo de timeout a cada coleta falha, iniciando em 1 segundo. |
| ![image-1739971041554.png](../../../../../assets/images/p51_image-1739971041554.png) | **Testar**: Quando disponível, permite testar se o dispositivo responde aos parâmetros configurados. |



## Grupos

Os dispositivos no Monsta podem fazer parte de grupos e herdar suas configurações. Nesta tela é possível consultar os grupos ao qual o dispositivo pertence além de adicionar outros. Para adicionar grupos, consulte Grupos de Dispositivos.

![image-1732557160475.png](../../../../../assets/images/p51_image-1732557160475.png)

| Ícone | Descrição |
| :---: | :--- |
| ![image-1732557200808.png](../../../../../assets/images/p51_image-1732557200808.png) | **Nome do grupo**: Informa o grupo ao qual o dispositivo pertence. |
| ![image-1646919486747.png](../../../../../assets/images/p51_image-1646919486747.png) | **Adicionar grupo**: Permite adicionar um novo grupo ao qual o dispositivo pertencerá. |
| ![image-1646919524906.png](../../../../../assets/images/p51_image-1646919524906.png) | **Remover grupo**: Remove o dispositivo do grupo selecionado. |



## Alertas

O Monsta tem a capacidade de emitir sons quando um dispositivo ou monitor troca de estado. Nesta tela você poderá personalizar os sons individualmente para o dispositivo em evidência.

![image-1732557243546.png](../../../../../assets/images/p51_image-1732557243546.png)

### Grupos de Alerta

Os grupos de alerta são utilizados para o envio de mensagens quando um dispositivo ou monitor troca de estado. Esses grupos podem ser personalizados para cada dispositivo ou monitor ou atribuídos sons específicos para o dispositivo em evidência. Para maiores informações sobre os grupos de alerta consulte [Alertas](/pt-br/manual/grupos-alertas/alertas).

![image-1739971123424.png](../../../../../assets/images/p51_image-1739971123424.png)


| Ícone | Descrição |
| :---: | :--- |
| ![image-1732557441016.png](../../../../../assets/images/p51_image-1732557441016.png) | **Notificar grupos de alerta**: Habilita/Desabilita o envio de alertas para o dispositivo selecionado. |
| ![image-1732557452354.png](../../../../../assets/images/p51_image-1732557452354.png) | **Selecionar**: Informa o grupo de alerta ao qual o dispositivo pertence. |
| ![image-1646919486747.png](../../../../../assets/images/p51_image-1646919486747.png) | **Adicionar grupo de alerta**: Permite adicionar um novo grupo de alerta ao qual o dispositivo pertencerá. |
| ![image-1646919524906.png](../../../../../assets/images/p51_image-1646919524906.png) | **Remover grupo de alerta**: Remove o dispositivo do grupo de alerta selecionado. |
| ![image-1732557653598.png](../../../../../assets/images/p51_image-1732557653598.png) | **Sons de Alerta**: Permite selecionar um som específico para cada estado do dispositivo. |
