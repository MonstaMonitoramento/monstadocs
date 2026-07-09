---
title: "Linha do Tempo"
---

A Linha do Tempo é uma ferramenta que transforma o registro contínuo de dados em uma representação visual e cronológica de todos os eventos e alterações ocorridas na infraestrutura monitorada.

:::note
Todos os registros de eventos e métricas na Linha do Tempo são permanentes. Uma vez criados, esses dados não podem ser apagados ou alterados, garantindo a confiabilidade e a validade legal do histórico para fins de auditoria e conformidade.
:::

![image-1756131037153.png](../../../../../assets/images/p36_image-1756131037153.png)

## Filtros de Pesquisa


| Ícone | Descrição |
| :---: | :--- |
| ![image-1756131155728.png](../../../../../assets/images/p36_332image-1756131155728.png) | **Tempo real**: Mostra as alterações que ocorrem nos dispositivos e monitores em tempo real. |
| ![image-1756131083740.png](../../../../../assets/images/p36_image-1756131083740.png) | **Evento não resolvido**: Quanto ativo, lista apenas os eventos que não se encontram no estado normal. |
| ![image-1756131188512.png](../../../../../assets/images/p36_image-1756131188512.png) | **Pausa**: Congela a tela atual para visualização. |

![image-1646833866456.png](../../../../../assets/images/p36_image-1646833866456.png)
**Filtro por dispositivo**: Filtra a visualização dos alertas para o dispositivo selecionado.

---

![image-1646833926056.png](../../../../../assets/images/p36_image-1646833926056.png)
**Filtro por intervalo de tempo**: Filtra as informações dos alertar pelo intervalo de tempo selecionado.


## Informações Disponíveis

![image-1739974446872.png](../../../../../assets/images/p36_image-1739974446872.png)

---

![image-1732708907756.png](../../../../../assets/images/p36_image-1732708907756.png) **Status**: Esse ícone indica o status que o dispositivo/monitor entrou no horário indicado. Ele pode ter os seguinte sgnificados: 

| Status | Descrição |
| :---: | :--- |
| ![image-1756131369083.png](../../../../../assets/images/p36_image-1756131369083.png) | O dispositivo/monitor retornou ao estado normal. | 
| ![image-1756131427462.png](../../../../../assets/images/p36_image-1756131427462.png) | O dispositivo/monitor possui coleta de dados operante porém com valores em estado de aviso. 
| ![image-1756131484609.png](../../../../../assets/images/p36_uNyimage-1756131484609.png) | O dispositivo/monitor possui coleta de dados operante porém com valores em estado crítico. | 
| ![image-1756131598663.png](../../../../../assets/images/p36_image-1756131598663.png) | O dispositivo/monitor não é capaz de reportar informação referente a coleta de dados. | 
| ![image-1756131693571.png](../../../../../assets/images/p36_image-1756131693571.png) | O dispositivo está inalcançavel devido a um problema com outro dipositivo acima na sua hierarquia da rede. |

| Info | Descrição |
| :---: | :--- |
| DNS Google | Dispositivo: Nome do dispositivo em que ocorreu a mudança de status. |
| Ping | Monitor: Nome do monitor em que ocorreu a mudança de status. Quando o monitor possui instância, o nome desta é mostrado ao lado entre "( )". |
| Tempo de Resposta | Métrica: Nome da métrica em que o evento ocorreu. |
| ![image-1756131850905.png](../../../../../assets/images/p36_image-1756131850905.png) | Evento não resolvido: Quando este ícone é apresentado, significa que este evento ainda não retornou ao estado normal. |
| ![image-1739974466466.png](../../../../../assets/images/p36_image-1739974466466.png) | Horário do evento: Informa a data e a hora que o evento foi detectado. |
| ![image-1739974478397.png](../../../../../assets/images/p36_image-1739974478397.png) | Alerta: Informa se algum alerta foi disparado durante o evento. Os grupos para os quais o alerta foi enviado serão listados nos detalhes do evento. |
| ![image-1732709258147.png](../../../../../assets/images/p36_image-1732709258147.png) | Detalhes: Expande ou esconde os detalhes do evento. |