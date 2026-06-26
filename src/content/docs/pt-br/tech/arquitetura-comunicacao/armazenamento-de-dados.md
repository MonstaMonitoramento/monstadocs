---
title: "Armazenamento de Dados"
sidebar:
  order: 2
---

Todos os dados de monitoramento coletados de seus dispositivos e monitores são armazenados em uma estrutura de banco de dados projetada para garantir velocidade, integridade e precisão histórica.

### O que isso significa para você



| **Característica Técnica** | **Benefício para o Usuário** |
| --- | --- |
| **NoSQL (Não-Relacional)** | Garante **alta velocidade** e **eficiência** no armazenamento e recuperação de grandes volumes de dados (Big Data), permitindo que o sistema acompanhe as métricas de inúmeros dispositivos em tempo real. |
| **Série Temporal** | Os dados são armazenados com um **carimbo de tempo exato**, organizados em ordem cronológica. Isso otimiza o acesso e a análise de **tendências e padrões ao longo do tempo**, sendo ideal para monitoramento. |
| **Não Podem ser Alterados/Apagados/Resetados** | Os dados coletados dos monitores não podem ser manipulados por segurança. Uma vez que um dado (evento, métrica) é registrado, ele se torna **permanente**. Essa característica é importante para **auditoria, conformidade e forense de TI**, pois garante que o histórico nunca foi manipulado. |



Em resumo, a combinação dessas tecnologias garante que você tenha acesso a um **histórico de performance rápido, confiável e à prova de adulteração**.