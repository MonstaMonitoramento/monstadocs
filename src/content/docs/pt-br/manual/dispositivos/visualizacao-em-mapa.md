---
title: "Visualização em Mapa"
sidebar:
  order: 4
---

A visualização em mapa permite uma interpretação geográfica ou lógica da infraestrutura de TI, facilitando a identificação visual da topologia da rede. No Monsta, você conta com dois modos de operação: o **Mapa Dinâmico** e o **Mapa Estático**

## Mapa Estático

Este modo oferece uma visualização simplificada e otimizada da infraestrutura.

- **Interatividade**: A posição dos ícones é fixa e determinada pela hierarquia do sistema. O usuário possui o controle de habilitar ou desabilitar a visualização dos ícones dos dispositivos através dos filtros.
- **Customização**: Não permite a movimentação de itens ou a inserção de *widgets*, mantendo a interface limpa e focada no status dos ativos.
- **Aplicação**: Recomendado para visualização de grandes volumes de dispositivos e infraestruturas de larga escala que exigem alta performance de carregamento.

![image-1771270820757.png](../../../../../assets/images/p56_image-1771270820757.png)

## Mapa Dinâmico

Este modo permite a personalização completa do layout visual da rede.

- **Interatividade**: O usuário pode mover livremente os ícones dos dispositivos e posicioná-los manualmente no mapa.
- **Customização**: Permite a inserção de *widgets* informativos e elementos gráficos adicionais.
- **Aplicação**: Ideal para a criação de painéis de monitoramento personalizados e redes que demandam organização visual específica.

### **Organização e Posicionamento**

O mapa oferece total liberdade de layout para que a representação digital seja fiel à instalação física:

- **Movimentação Livre**: Clique e arraste qualquer dispositivo para posicioná-lo manualmente no quadrante desejado.
- **Persistência de Layout**: A disposição definida pelo usuário pode ser salva a qualquer momento, garantindo que a organização seja mantida em todos os acessos.

### **Gestão de Dependências (Hierarquia)**

A estrutura hierárquica define a relação de subordinação entre os dispositivos (dispositivos "pais" e "filhos").

- **Alteração de Hierarquia**: Para modificar o nó pai de um dispositivo, clique sobre o nó do dispositivo pai e arraste o mouse até o novo dispositivo filho.
- **Impacto Lógico**: Ao trocar o pai de um ativo, o sistema atualiza automaticamente a árvore de dependências e as regras de propagação de alertas associadas àquela ramificação.

### **Enriquecimento com Widgets**

O mapa permite inserir **Widgets** informativos diretamente na área de visualização:

- **Monitoramento em Tempo Real**: Adicione blocos de dados, gráficos de desempenho, indicadores e muito mais junto aos dispositivos.
- **Personalização de Painel**: Os widgets podem ser redimensionados e posicionados estrategicamente para destacar métricas críticas de ativos específicos sem a necessidade de navegar por outros menus.

![image-1768939041220.png](../../../../../assets/images/p56_image-1768939041220.png)

![image-1768939090089.png](../../../../../assets/images/p56_image-1768939090089.png) 
**Dispositivo principal**: O mapa possui um sistema de filtro inteligente que isola ramificações específicas. Ao selecionar um dispositivo através do filtro, a interface oculta os dispositivos irrelevantes e exibe exclusivamente a linhagem direta do item escolhido.


![image-1771271034725.png](../../../../../assets/images/p56_image-1771271034725.png) 
**Propriedades do Mapa**: Através do botão de **Propriedades**, é possível personalizar a exibição da topologia para facilitar a leitura e visualização:
- **Elementos**: Ajuste o tamanho e formato dos ícones dos dispositivos e dos textos.
- **Identificação**: Habilite ou oculte a exibição de imagens.
- **Conectividade**: Selecione diferentes tipos de setas e estilos de ligação para representar as conexões de rede.

![image-1739973711187.png](../../../../../assets/images/p56_image-1739973711187.png) 
**Edição**: Ao acionar o modo de **Edição**, o usuário ganha controle total sobre a interface visual da rede, permitindo:
- **Organização Espacial**: Reposicionar dispositivos livremente via *drag-and-drop* para refletir a topologia física ou lógica.
- **Métricas de Conexão**: Inserir indicadores de desempenho diretamente nas linhas de ligação entre dispositivos.
- **Enriquecimento com Widgets**: Adicionar componentes visuais extras (gráficos, medidores, etc) para criar um painel de monitoramento completo e personalizado.
- **Reorganize as posições**: Redefina automaticamente o posicionamento de todos os dispositivos de acordo com a hierarquia de definida no sistema.