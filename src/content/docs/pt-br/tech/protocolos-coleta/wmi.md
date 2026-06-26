---
title: "WMI (Windows Management Instrumentation)"
sidebar:
  order: 1
---

# O que é WMI?

O *Windows Management Instrumentation* (**WMI**) é uma infraestrutura central para gerenciamento de dados e operações em sistemas operacionais Windows. Ela é a implementação do WBEM (Gerenciamento Corporativo Baseado na Web) da Microsoft e fornece uma interface padronizada para que administradores e aplicativos possam monitorar, controlar e configurar diversos aspectos do ambiente Windows, desde informações de hardware e software até o estado dos serviços e processos do sistema. Essa capacidade de “instrumentar” o sistema permite a automação de tarefas administrativas e facilita o diagnóstico e a solução de problemas de forma centralizada.

## Objetivos e Funcionalidades

O WMI foi projetado para fornecer:

- **Gerenciamento Centralizado**: Uma maneira uniforme de acessar informações de configuração e status dos sistemas Windows.
- **Automação**: Capacidade de criar scripts e aplicativos que monitoram eventos, realizam consultas e efetuam alterações de forma automatizada.
- **Monitoramento**: Obtenção em tempo real de dados sobre os processos, serviços, hardware, rede e outros componentes do sistema.
- **Interação com os Elementos do Sistema**: Operações de leitura e modificação de dados de sistema, incluindo a execução de métodos e scripts para manutenção e configuração.

Com essa abordagem, o WMI serve como uma poderosa ferramenta para administradores de sistemas, integradores de soluções e desenvolvedores que necessitam acompanhar e gerenciar ambientes de TI.

## Histórico e Evolução

O WMI foi introduzido pela Microsoft com a intenção de padronizar o acesso à informações de gerenciamento do sistema. Desde sua primeira versão no Windows NT e sua evolução a partir do Windows 2000, o WMI se tornou parte integrante das estratégias de gerenciamento da Microsoft. Seu desenvolvimento se baseia no Common Information Model (CIM), um padrão que unifica a forma de representar dispositivos e serviços em ambientes heterogêneos.

Historicamente, o WMI evoluiu para oferecer melhor desempenho, novas funcionalidades e maior integração com outras tecnologias de gerenciamento, permitindo uma maior amplitude de ações administrativas e de monitoramento.

**MI (Infraestrutura de Gerenciamento)**: A próxima geração do WMI, conhecida como MI (Infraestrutura de Gerenciamento), oferece recursos e benefícios adicionais para a criação e desenvolvimento de provedores e clientes WMI.

## Arquitetura do WMI

A arquitetura do WMI é robusta e construída sobre vários componentes que trabalham de forma integrada para fornecer suas funcionalidades.

### Componentes Principais

- **WMI Service (winmgmt)**: É o serviço central que actua como o “orquestrador” do WMI. Ele gerencia as requisições dos clientes, distribui consultas e coordena a comunicação com os provedores de dados.
- **Repositório CIM (Common Information Model)**: Este repositório contém uma representação padronizada dos dados do sistema. As classes CIM servem como modelos para as informações que o WMI expõe, garantindo consistência e interoperabilidade com outros sistemas de gerenciamento.
- **Clientes WMI**: São os aplicativos ou scripts que realizam consultas e comandos via WMI. Exemplos incluem o prompt de comando (usando `wmic`), scripts em PowerShell e aplicativos desenvolvidos em diversas linguagens que utilizem as APIs do WMI.

### WMI Providers

Os *Providers* são componentes que “traduzem” as solicitações feitas via WMI para comandos específicos do hardware ou software. Cada provider é responsável por uma área do sistema (por exemplo, gerenciamento de processos, informações de rede, dispositivos de armazenamento) e coleta os dados necessários para responder às consultas dos clientes.

### Repositório CIM e a Modelagem de Dados

O modelo CIM define uma estrutura hierárquica e padronizada para representar os dados do sistema. Através dele, o WMI organiza a informação em classes – por exemplo, `Win32_Process` para processos em execução, `Win32_OperatingSystem` para informações do sistema operacional, entre outras. Essa padronização facilita a criação de consultas coerentes e a integração com outras ferramentas de gerenciamento.

### WMI Query Language (WQL)

O WMI utiliza a WMI Query Language (WQL), que é similar à linguagem SQL, mas adaptada para o gerenciamento de informações do sistema. Com o WQL, é possível realizar consultas como:

```sql
SELECT * FROM Win32_Process WHERE Name = 'notepad.exe'
```

Essa consulta retorna informações sobre processos cujo nome é “notepad.exe”. Além disso, o WQL permite a criação de consultas para monitoramento de eventos. Por exemplo, você pode definir uma consulta que acione uma ação sempre que um novo processo for iniciado ou um serviço for interrompido.

## Utilização do WMI

Acesso via Ferramentas de Linha de Comando e Scripts

- **WMIC (Windows Management Instrumentation Command-line)**: Ferramenta em linha de comando que permite executar consultas, extrair informações e executar métodos via WMI. Exemplo:    
    ```powershell
    wmic process list brief
    
    ```
- **PowerShell**: Cmdlets como `Get-WmiObject` (em versões anteriores) e `Get-CimInstance` (nas versões mais recentes) permitem o acesso aos dados do WMI. Exemplo com PowerShell:
    
    ```powershell
    Get-WmiObject -Query "SELECT * FROM Win32_OperatingSystem"
    ```
- **VBScript, C#, Python (usando bibliotecas como pywin32)**: Diversas linguagens de programação podem interagir com o WMI, tornando-o acessível para scripts personalizados que automatizam tarefas administrativas.

## Como o Monsta coleta os recursos fornecidos pelo WMI

O Monsta possui uma sonda de desenvolvimento próprio que acessa diretamente as APIs do WMI para coletar as informações solicitadas pela plataforma de monitoramento. A sonda é instalada diretamente no servidor ou estação de trabalho que se deseja monitorar e seu funcionamento é passivo, ou seja, ela recebe solicitações por uma porta, processa as informações e as retorna pela mesma conexão.

Para baixar e instalar a sonda em seus servidores/estações, utilize nosso tutorial [Sonda: Monitoramento Windows](/pt-br/start/instalacao/sonda-windows) para monitorar seu ambiente Microsoft.
