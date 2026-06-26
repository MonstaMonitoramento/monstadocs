---
title: "SNMP (Simple Network Management Protocol)"
sidebar:
  order: 1
---

# O que é SNMP?

O *Simple Network Management Protocol* (**SNMP**), é um protocolo padrão da Internet usado para coletar e organizar informações sobre dispositivos gerenciados em redes IP (Protocolo de Internet) e para modificar essas informações para alterar o comportamento do dispositivo. Em termos mais simples, o SNMP permite que administradores de rede monitorem e gerenciem seus equipamentos de rede, como roteadores, switches, servidores, impressoras e muito mais, a partir de um ponto central.

Imagine ter um painel de controle para toda a sua infraestrutura de rede. O SNMP funciona fornecendo dados a esse painel, permitindo que você:

- **Monitore o status e o desempenho dos seus dispositivos**: Verifique se um roteador está funcionando corretamente, qual a utilização da CPU de um servidor, quanta tinta resta em uma impressora, etc.
- **Receba alertas sobre problemas**: Seja notificado automaticamente se um dispositivo falhar, se a largura de banda estiver alta ou se houver qualquer outro evento que exija atenção.
- **Configure remotamente alguns dispositivos**: Em alguns casos, o SNMP permite que você altere configurações em seus dispositivos de rede sem precisar acessá-los diretamente.
- **Colete dados para análise**: O SNMP fornece dados históricos de desempenho que podem ser usados para identificar tendências, planejar a capacidade da rede e solucionar problemas futuros.

O SNMP funciona através da troca de mensagens entre um **agente SNMP**, que reside no dispositivo gerenciado, e um **gerenciador SNMP**, que é o sistema central de monitoramento, como o **Monsta**, por exemplo. Os agentes SNMP coletam informações sobre o dispositivo e as armazenam em uma estrutura chamada **MIB (Management Information Base)**. O gerenciador SNMP pode então consultar os agentes para obter essas informações ou enviar comandos para alterar configurações (em alguns casos).

Em resumo, o SNMP é uma ferramenta fundamental para o gerenciamento eficiente e proativo de redes de computadores, ajudando a garantir a disponibilidade e o bom funcionamento dos seus serviços de TI.

Desde sua criação, o SNMP passou por evoluções significativas para se adaptar às crescentes demandas de segurança e funcionalidade. As versões mais conhecidas e utilizadas são a v1, v2c e v3. Embora todas tenham o mesmo propósito central, elas se distinguem por recursos, principalmente em termos de segurança.

## SNMP v1: O Pioneiro Simples e Inseguro

Lançada em 1988, a versão SNMPv1 foi a primeira a ser amplamente adotada. Ela se destacou por sua simplicidade, utilizando um modelo de gerenciamento baseado em comunidades. Uma comunidade é, essencialmente, uma senha de texto simples (chamada de string de comunidade) que permite o acesso de leitura ou leitura/escrita a um dispositivo.

- **String de Comunidade**: É o único mecanismo de "autenticação". Se a string de comunidade do gerenciador de rede corresponder à do dispositivo, o acesso é concedido.
- **Mensagens**: Utiliza três tipos básicos de mensagens: GET (para obter valores), SET (para alterar valores) e TRAP (para notificar eventos).
- **Vulnerabilidade**: A principal fraqueza do SNMPv1 é a falta de segurança. As strings de comunidade são transmitidas em texto puro, tornando-as suscetíveis a interceptação e uso malicioso. Isso significa que qualquer pessoa com acesso à rede pode capturar o tráfego e descobrir a comunidade, obtendo acesso ao SNMP dos dispositivos.

:::caution[Importante]
Recomenda-se o uso do SNMP v1 apenas se o equipamento não possui suporte às versões seguintes, devido às suas limitações.
:::

## SNMP v2c: Melhorias e Maior Flexibilidade

O SNMPv2 foi uma tentativa de modernizar o protocolo, introduzindo melhorias substanciais. A versão SNMPv2c (onde o "c" significa Community-Based, ou seja, "baseado em comunidades") manteve o modelo de segurança do SNMPv1, mas trouxe avanços importantes em outras áreas.

- **Melhorias na Mensagem**: Introduziu novos tipos de mensagens, como GETBULK, que permite a recuperação de grandes volumes de dados de forma mais eficiente, reduzindo a carga na rede. Também aprimorou o mecanismo de TRAP com a introdução do INFORM, que confirma o recebimento da notificação.
- **Tipos de Dados**: Aprimorou a definição de tipos de dados, oferecendo mais flexibilidade e precisão na representação das informações gerenciadas.
- **Suporte a Variáveis de 64 bits**: Uma melhoria técnica significativa é a capacidade de gerenciar valores maiores, como contadores de tráfego de rede. O SNMPv1 é limitado a contadores de 32 bits, que podem atingir o valor máximo e "virar" (reiniciar do zero) rapidamente em redes de alta velocidade. O SNMPv2c e o v3 suportam contadores de 64 bits, que podem rastrear volumes de dados muito maiores antes de "virar", oferecendo estatísticas mais precisas e confiáveis para o monitoramento de tráfego.
- **Modelo de Comunidade**: Apesar das melhorias, o SNMPv2c ainda utiliza a mesma abordagem de segurança do SNMPv1, com strings de comunidade transmitidas em texto simples. Por isso, ele herda as mesmas vulnerabilidades de segurança, tornando-o inadequado para ambientes onde a confidencialidade é crítica.

## SNMP v3: A Resposta para a Segurança

O SNMPv3 representa um salto gigantesco em termos de segurança e é a versão recomendada para o gerenciamento de redes modernas. Ele abandona o modelo de comunidades e implementa um framework robusto de segurança e autenticação.

- **Autenticação (Authentication)**: O SNMPv3 exige a configuração de um nome de usuário e uma senha para cada dispositivo. As mensagens são assinadas digitalmente para garantir que vêm de uma fonte confiável. Isso impede que terceiros mal-intencionados injetem mensagens falsas na rede. Os algoritmos de autenticação mais comuns são MD5 e SHA.
- **Privacidade (Privacy)**: Além da autenticação, o SNMPv3 oferece criptografia. Os dados transmitidos entre o gerenciador e o dispositivo podem ser criptografados, impedindo que sejam lidos caso sejam interceptados. Os algoritmos de criptografia mais utilizados são DES e AES.
- **Modelo de Usuário**: A segurança é baseada em usuários, onde cada um pode ter diferentes níveis de acesso e permissões. Isso permite um controle de acesso granular e mais rigoroso.



| **Característica** | **SNMP v1** | **SNMP v2c** | **SNMP v3** |
| --- | --- | --- | --- |
| **Segurança** | Nenhuma (texto simples) | Nenhuma (texto simples) | Autenticação e Criptografia |
| **Autenticação** | String de Comunidade | String de Comunidade | Usuário e Senha (MD5/SHA) |
| **Criptografia** | Não | Não | Sim (DES/AES) |
| **Tipos de Mensagem** | GET, SET, TRAP | GETBULK, INFORM (e as da v1) | GETBULK, INFORM (e as da v1) |



## Portas de Comunicação

O protocolo utiliza duas portas de comunicação por padrão:

- **161/UDP**: para comunicação do gerente (sistema de monitoramento) para o agente (equipamento que é monitorado);
- **162/UDP**: para comunicação do agente para o gerente (comunicações que parte do equipamento monitorado, como no caso do **TRAP**).

Alguns equipamentos permitem alterar as configurações do SNMP, como comunidade, porta e, para o caso de SNMPv3, credenciais de autenticação e tipo de criptografia. É sempre importante verificar nas configurações do equipamento essas informações para utilizar no sistema de monitoramento.

## Monsta

O Monsta tem suporte às três versões do SNMP e permite informar os parâmetros necessários para monitorar os equipamentos de acordo com cada versão (comunidade, porta, usuário, senha, tipo de criptografia).

No momento, o Monsta atua apenas com a comunicação **gerente > agente**, utilizando os tipos de mensagem **GET** e **GETBULK**.
