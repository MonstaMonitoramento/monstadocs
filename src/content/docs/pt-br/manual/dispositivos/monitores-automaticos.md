---
title: "Monitores Automáticos"
sidebar:
  order: 8
---

Os **monitores automáticos** são um recurso fundamental do Monsta, projetado para simplificar e acelerar a configuração do seu ambiente de monitoramento. Em vez de adicionar manualmente cada monitor que você deseja acompanhar em seus dispositivos, o Monsta utiliza mecanismos inteligentes para **descobrir automaticamente** os elementos presentes em sua infraestrutura e adiciona os monitores para cada um deles.

#### Como Funciona:

Ao configurar a descoberta automática, o Monsta explora as instâncias do monitor que você especificar, utilizando protocolos de rede como **SNMP (Simple Network Management Protocol), WMI, SSH** ou **API**. Ao identificar uma instância nova, o Monsta cria um novo monitor com seu nome. Caso a instância seja excluída do dispositivo, o algoritmo de monitores automáticos detecta e remove a instância de seu monitoramento baseado no tempo decorrente da exclusão.

**Por exemplo**:

- Para um servidor Windows, o Monsta pode detectar automaticamente as interfaces de rede existentes e criar um monitor para cada uma delas;
- Em equipamentos que trabalham com VPN, o Monsta pode identificar as interfaces criadas para novos usuários e adicioná-las automaticamente, assim como remover a interface do monitoramento caso a mesma deixe de existir pela quantidade de dias configurado na regra do monitor.

Após a descoberta automática, você terá a oportunidade de **selecionar os monitores** criados e **personalizar as configurações** de cada um deles, como limites de alerta e frequência de coleta de dados. Os monitores automáticos são uma ferramenta poderosa para iniciar o seu monitoramento de forma rápida e inteligente, permitindo que você foque em analisar os dados e garantir a saúde da sua infraestrutura de TI.

#### Como Adicionar uma Regra de Monitor Automático:

1. Clique sobre o dispositivo que você deseja criar a regra de monitor automático;
2. Clique no botão![image-1746723454780.png](../../../../../assets/images/p99_image-1746723454780.png)<br />A seguinte tela será exibida:<br />![image-1746723532817.png](../../../../../assets/images/p99_image-1746723532817.png)
3. Clique em "Adicionar";
4. Personalize a regra conforme sua necessidade com os parâmetros abaixo:  
    
| Opção | Descrição |
| :--- | :--- |
| Monitor | Selecione o monitor que deseja automatizar |
| Filtro de instância | Você pode infomar um texto que será utilizado para filtrar os nomes de instâncias existentes e irá criar apenas monitores que "contenham" esse conteúdo. |
| Frequência | É o tempo em que o Monsta irá verificar se alguma nova instância foi criada. Caso sejam identificados novos itens, seus respectivos monitores serão criados. |
| Remover monitores | Em caso de falha na coleta de um monitor, isso significa que ele pode ter sido removido do equipamento. Após os dias configurados nessa opção o Monsta irá remover esses monitores. |

**Exemplo**:

![image-1746724019551.png](../../../../../assets/images/p99_image-1746724019551.png)

Na imagem acima, a regra criada irá adicionar monitores que contenham a palavra "vlan" em seu nome. A cada 30 minutos o Monsta fará uma varredura para verificar se existem novas instâncias e as adicionará ao monitoramento. Caso um monitor automático entre em estado de falha, se em 7 dias ele não retornar as coletas o mesmo será excluído do monitoramento.