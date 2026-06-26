---
title: "Datasheet"
---

O **Monsta** é uma solução completa e intuitiva para monitoramento de redes, projetada para fornecer informações detalhadas sobre seus dispositivos e recursos, permitindo que você mantenha sua rede funcionando sem problemas e evite interrupções. Com uma interface amigável e recursos poderosos, o \[Nome do Software\] oferece uma visão abrangente da sua rede, permitindo que você tome decisões informadas e otimize o desempenho da sua infraestrutura.

## Principais características

- **Monitoramento abrangente de dispositivos**: Acompanhe o desempenho e a saúde de todos os seus dispositivos de rede, incluindo servidores, roteadores, switches, firewalls e muito mais.
- **Informações detalhadas sobre recursos**: Obtenha insights profundos sobre o uso de CPU, memória, disco, largura de banda e outros recursos importantes de cada dispositivo.
- **Geração de gráficos e painéis**: Visualize dados de desempenho em tempo real por meio de gráficos e painéis personalizáveis, permitindo que você identifique tendências e gargalos.
- **Alertas inteligentes**: Receba notificações instantâneas sobre problemas e eventos críticos, permitindo que você tome medidas preventivas e corrija problemas antes que eles afetem seus usuários.
- **Previsão de problemas**: Utilize recursos avançados de análise para identificar padrões e prever possíveis problemas, permitindo que você se prepare e evite interrupções.
- **Interface intuitiva e fácil de usar**: O Monsta foi projetado para ser fácil de usar, mesmo para usuários sem conhecimento técnico avançado.
- **Relatórios personalizáveis**: Gere relatórios detalhados sobre o desempenho da sua rede, permitindo que você acompanhe o progresso e compartilhe informações com sua equipe.
- **Baixo consumo de Hardware**: Graças à sua arquitetura otimizada, o Monsta garante um desempenho excepcional com o mínimo de consumo de recursos. Isso se traduz em maior velocidade, fluidez e capacidade de resposta, mesmo em ambientes com alta demanda.
- **Desenvolvimento 100 próprio**: Solução 100% desenvolvida pela Monsta Tecnologia, fruto de nossa expertise e dedicação em oferecer o melhor software de monitoramento de redes do mercado.
- **Backup automáticos**. O Monsta faz um backup na nuvem, automaticamente, de todas suas configurações.

![image-1740051151463.png](../../../../assets/images/p25_image-1740051151463.png)

## Para que server o Monsta?

O Monsta objetiva garantir o contínuo funcionamento dos serviços essenciais em sua organização, monitorando continuamente o hardware e software existentes em sua rede e emitindo alertas para os responsáveis.

## Requisitos mínimos

Sugerido para monitorar 500 dispositivos e 5.000 monitores.


| Item | Requisito mínimo |
| :---: | :--- |
| ![image-1645452261754.png](../../../../assets/images/p25_image-1645452261754.png) | **Espaço em disco**<br />40GB livre para /var (configurações, banco de dados e logs)<sup>1</sup> <br />300MB livre para /opt/monsta (programas e bibliotecas) |
| ![image-1645452312898.png](../../../../assets/images/p25_image-1645452312898.png) | **Memória RAM**<br />1GB de memória RAM |
| ![image-1645452455434.png](../../../../assets/images/p25_image-1645452455434.png) | **Sistema Operacional**<br />Linux 64bits<br />Sistema Operacional Linux recomendado: Fedora Server 40 |
| ![image-1645452542916.png](../../../../assets/images/p25_image-1645452542916.png) | **Processador**<br />Cores: 2<br />Velocidade: 1.8GHz |

:::note
<sup>1</sup> O tamanho da partição depende da quantidade de informações que serão armazenadas. Os dados de monitoramento são compactados antes de serem salvos em disco.
:::

## Especificações

| Categoria / Item | Especificação |
| :--- | :--- |
| **DESENVOLVIMENTO** | |
| Linguagem de Desenvolvimento | Rust, Typescript e Go |
| Linguagem HTML | HTML 5 |
| Linguagem dos Scripts | LUA, Python e MagoVM (Proprietário) |
| **SISTEMAS** | |
| Servidor HTTP | Monrouter (desenvolvimento próprio) |
| Sistema Operacional | Linux 64 bits |
| Comunicação com a nuvem | HTTP e HTTPS com criptografia TLS |
| Mecanismos de Coletas | SNMP, WMI, ICMP, TCP, API e *fontes externas. (Permite ao usuário criar seu próprio mecanismo) |
| **ALERTAS NATIVOS** | |
| SMS | Envio através de Twilio e Zenvia |
| E-mails | Envio através da AWS |
| Telegram | Envio através do bot MonstaTecnologia no Telegram |
| **BANCO DE DADOS (Histórico dos Monitores)** | |
| MonstaDB | (Proprietário) Modelo `nosql` para consultas em tempo real |
| In-Memory | Sim |
| Proteção contra corrupção de dados | Sim |
| Persistente | Sim |
| Compactação dos dados | Sim |
| Descarte de informações | Não (dados não são resumidos com o passar dos dias) |
| **BANCO DE DADOS (Configurações)** | |
| Banco de Dados | (Proprietário) Modelo SQL |
| In-Memory | Sim |
| Proteção contra corrupção de dados | Sim |
| Persistente | Sim |
| Compactação dos dados | Sim |
| Descarte de informações | Não |

## Arquitetura de software

![image-1645464317340.png](../../../../assets/images/p25_image-1645464317340.png)

## Experimente antes de comprar

Experimente o Monsta em sua organização para avaliar seu funcionamento e comportamento. A versão de avaliação não possui limite de monitores ou dispositivos e se você gostou da ferramenta, todo o trabalho que você fez não é descartado, bastando apenas ativar a chave de licença do software e assim você torna a versão de avaliação em definitiva.

## Sobre a empresa

Monsta é uma empresa de tecnologia focada na detecção e solução dos problemas de infraestrutura de TI. Nosso objetivo é tornar o monitoramento da rede uma tarefa simples e automatizada, através de uma ferramenta confiável e de baixo custo para o mercado.
