---
title: "Opções"
sidebar:
  order: 5
---

## Opções globais de dispositivos

![image-1646847756093.png](../../../../../assets/images/p52_image-1646847756093.png)
O Monsta permite a definição de **Valores Globais**, que funcionam como uma predefinição inteligente para todos os dispositivos cadastrados. Quando um valor é definido globalmente, ele é automaticamente herdado por todos os dispositivos, a menos que uma configuração específica seja definida individualmente para o dispositivo ou para seu grupo de dispositivos.

### Coleta

![image-1732557804866.png](../../../../../assets/images/p53_image-1732557804866.png)

**Parâmetros de Comunicação (SNMP, WMI e SSH)**: Centralize as credenciais de acesso e portas de comunicação. Ao configurar as comunidades SNMP ou usuários de SSH/WMI globalmente, novos dispositivos serão monitorados automaticamente sem a necessidade de inserir senhas manualmente para cada um.

### Sensibilidade  


![image-1732558676013.png](../../../../../assets/images/p53_image-1732558676013.png)

**Sensibilidade do Uptime**: Define o critério de tolerância para considerar um dispositivo como "offline". Ajustar a sensibilidade global permite determinar quantos testes de conectividade devem falhar antes que o sistema dispare um alerta de queda, evitando alarmes falsos em redes com oscilações momentâneas.



| **Nível** | Podem ser utilizados padrões pré-estabelecidos ou personalizar cada item. |
| --- | --- |
| **Pacote(s)** | Quantos pacotes serão disparados contra os equipamentos antes de considerá-los crítico em caso de falha no recebimento de resposta. |
| **Timeout** | Quanto tempo o Monsta irá aguardar por cada ping enviado antes de considerá-lo como não recebido. |
| **Delay** | Após recebido o pacote anterior ou em caso de timeout do mesmo, quanto tempo o Monsta deverá aguardar antes de enviar a próxima requisição. Pacotes para checar o uptime são encerrados ao receber um retorno. Já para monitorar o tempo de ping em um equipamento, todos os pacotes serão disparados e uma média do tempo será retornada. |



### Sons de Alerta

![image-1732559278364.png](../../../../../assets/images/p53_image-1732559278364.png)

**Sons de Alerta Personalizados**: Configure a experiência sonora do Centro de Operações (NOC). Você pode definir áudios distintos para os estados **Normal**, **Aviso** e **Crítico**. Essa herança garante que toda a interface mantenha um padrão sonoro coeso, facilitando a identificação imediata da gravidade de um evento pela equipe técnica.

## Opções de exibição

![image-1740681553351.png](../../../../../assets/images/p53_image-1740681553351.png)

O Monsta permite que você configure o nível de detalhamento visual dos seus ativos, priorizando a informação que for mais estratégica para o seu dia a dia:

- **Ajuste de Dimensões**: Controle o tamanho das caixas de dispositivos e monitores, permitindo maior densidade de informações em telas pequenas ou melhor visibilidade em painéis de monitoramento (NMS).
- **Configuração de Rótulo Dinâmico**: Você pode escolher o que cada monitor exibe em destaque na tela principal:    
    - **Nome do Monitor**: Ideal para identificação rápida do serviço ou parâmetro que está sendo observado (ex: "Temperatura CPU").
    - **Valor da Coleta Atual**: Exibe em tempo real o dado exato coletado (ex: "45°C"), permitindo acompanhar métricas críticas sem precisar abrir os detalhes do monitor.
- **Escalabilidade de Texto e Imagens**: Personalize o tamanho das fontes e imagens nos monitores para garantir que as informações sejam legíveis conforme o layout escolhido, adaptando-se tanto ao uso individual em desktops quanto em grandes telas de centros de operação.

| Item | Descrição |
| --- | --- |
| **Tamanho da barra de status** | Define o tamanho da barra que informa na parte superior relacionada ao status do dispositivo. |
| **Tamanho da caixa** | Define o tamanho da caixa de dispositivo. |
| **Tamanho da fonte** | Configura o tamanho da fonte do nome do dispositivo. |
| **Dispositivo deve seguir status dos monitores** | Quando ativada esta opção, o status do dispositivo assumirá o status dos monitores, sendo o estado crítico o de maior relevância e o normal, o menor. |
| **Paginação na página de dispositivos** | Exibe a tela de dispositivos com uma paginação ao invés de uma rolagem infinita; |
| **Mostrar endereço** | Exibe o host utilizado para monitorar o dispositivo. |
| **Mostrar ícone** | Exibe o ícone atribuído ao dispositivo. |
| **Mostrar monitores** | Exibe a contagem de monitores no topo da caixa do dispositivo. |
| **Mostrar animação** | Habilita a animação da caixa do dispositivo quando este trocar de status. |
| **Caixa do monitor** | Permite ao usuário alterar o tamanho da caixa dos monitores. |
| **Tamanho da fonte** | Permite ao usuário alterar o tamanho da fonte do texto dos monitores. |
| **Espaçamento entre as caixas** | Permite ao usuário alterar o espaço entre as caixas dos monitores. |
| **Tamanho do ícone** | Permite ao usuário alterar o tamanho do ícone apresentado nas caixas dos monitores. |
| **Modo de exibição do monitor** | Permite selecionar o tipo de informação que deve aparecer no monitor, nome ou valor da última leitura. |