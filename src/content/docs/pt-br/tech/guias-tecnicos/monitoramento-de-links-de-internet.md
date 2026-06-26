---
title: "Monitoramento de Links de Internet"
---

O Monsta é uma ferramenta poderosa para garantir a disponibilidade e o desempenho da conectividade de rede da sua empresa. O monitoramento de links de internet é importante para detectar falhas de conectividade e identificar gargalos de consumo de banda.

## Princípio de Funcionamento

O Monsta monitora o link de internet na **interface de rede do seu equipamento local** onde o link chega.

1. **Coleta de Dados**: O Monsta se conecta ao seu equipamento de rede (como roteador, firewall ou switch) e coleta informações da interface configurada para o link de internet (porta WAN). Mais de uma porta pode ser monitorada simultaneamente.
2. **Métricas Monitoradas**:
    
    
    - **Velocidade e Status da Interface**: Indica se a interface está ativa (*UP*) ou inativa (*DOWN*) e a sua velocidade de conexão, reportando caso a mesma fique inativa ou com velocidade de conexão física abaixo do esperado.
    - **Volume de Tráfego**: Mede a quantidade de dados de entrada (*Inbound*) e saída (*Outbound*) em bits por segundo, métricas utilizadas para o monitoramento de consumo.
    - **Cálculo do Volume Trafegado**: O Monsta pode calcular o volume de dados total trafegado no intervalo de tempo que você selecionar.
3. **Processamento**: Os dados coletados são armazenados e apresentados em gráficos e podem ser configurados nos painéis para análise de tendências e histórico.

## Criação de Alarmes Proativos

A principal vantagem de monitorar o link é a capacidade de configurar **alarmes proativos e reativos** com base nas métricas coletadas.



| Tipo de Alarme | Condição de Limite | Impacto e Ação |
| --- | --- | --- |
| **Queda do Link** | A interface muda de **Status UP para DOWN**. | **Alerta Crítico.** Indica falha total de conectividade com o provedor. |
| **Redução da Velocidade de Conexão Física** | A interface de rede reduz a velocidade de conexão física para se adequar a algum problema de cabeamento ou da interface de rede. | **Alerta de Advertência/Problema.** Avisa se a interface física está operando abaixo da sua capacidade total. |
| **Excesso de Consumo (Banda)** | A taxa de tráfego (Inbound ou Outbound) excede um **limite de utilização** pré-configurado (ex: 90% da capacidade total do link) por um período de tempo. | **Alerta de Advertência/Problema.** Indica que o link está saturado. O alarme sugere a necessidade de **gerenciamento de banda** ou um *upgrade* no link. |


:::tip[Exemplo prático]
Se o seu link tem 100 Mbps, você pode configurar um alarme para disparar quando o consumo atingir consistentemente 90 Mbps.
:::

## Configuração na Prática

Para configurar o monitoramento de um link de internet no Monsta, siga estas etapas básicas:

1. **Adicione o Dispositivo**: Crie um dispositivo no Monsta para monitorar seu Roteador/Firewall.
2. **Adicione os Monitores**: Selecione o dispositivo e clique no botão "+" para adicionar o monitor de tráfego de rede e Velocidade da Interface.
3. **Configure os Alarmes**: Selecione os monitores criados e clique em "Editar" para configurar os limites de alerta que deseja receber informações.



:::note
Para receber avisos, lembre-se de adicionar um Grupo de Alertas ao seu dispositivo. Para maiores informações, consulte [Alertas](/pt-br/manual/grupos-alertas/alertas)
:::
