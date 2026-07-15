---
title: Changelog v6
description: Acompanhe o Changelog da versão 6 do Monsta e conheça as novas
  funcionalidades, melhorias, correções e alterações realizadas em cada
  atualização da plataforma.
sidebar:
  order: 2
---
## Versão 6.0.16 Beta

**✨Novo**: **Relatórios Mensais com Inteligência Artificial**. Agora, sua conta gera automaticamente relatórios mensais enriquecidos com *insights* baseados em IA.

![image.png](/src/assets/images/image-10.png)

**✨Novo**: **Execução Remota via PowerShell**. A Sonda permite a execução de comandos e *scripts* em PowerShell diretamente pelo console. Para garantir a segurança do seu ambiente, todos os comandos são processados utilizando um **usuário com privilégios restritos (não administrador)**.

![image.png](/src/assets/images/image-5.png)

**✨Novo**: **Monitoramento S.M.A.R.T.**. Adicionamos suporte à coleta de dados S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitindo acompanhar a integridade, a vida útil e os indicadores de saúde do armazenamento para identificar possíveis falhas antes que elas afetem o ambiente.

![image.png](/src/assets/images/image-9.png)

🔧**Correção**: Corrigido um comportamento inesperado onde as atualizações do sistema afetavam indevidamente o logotipo personalizado definido pelo usuário.

## Versão 6.0.13 Beta

**🔧Correção**: Otimizado o tempo de inicializacao da coleta de dados em novas instalacoes.

**🔧Correção**: Corrigida a reconexao de agentes apos a restauracao de backup da nuvem em novas instalacoes.

**🔧Correção**: Corrigido problema pontual que impedia o disparo de alarmes em alguns monitores.

## Versão 6.0.9

**🔧Correção**: Disponibilizados botões para remover agentes desconectados e bloqueados na tela de gerenciamento.

**🔧Correção**: Informações sobre a chave e licença aparecem em branco em alguns casos.

**🔧Correção**: Monsta solicita tela de login da área do cliente para validar a chave em algumas situações.

## Versão 6.0.6

**✨Novo**: **Agentes** - Monitoramento de redes remotas sem necessidade de VPNs ou redirecionamento de portas [Agente: Instalação Zero Conf](/pt-br/start/instalacao/agente-instalacao-zero-conf).

**✨Novo**: [Mapa para visão hierárquica](/pt-br/manual/dispositivos/visualizacao-em-mapa#mapa-dinâmico) com possibilidade de definir posições, adicionar widgets e métricas.

**✨Novo**: Painéis podem ser disponibilizados para usuários não administradores.

**✨Novo**: Relatório de consumo pode calcular área de qualquer unidade de medida.

**🔧Correção**: Dispositivos sem uptime não enviavam alertas.

**🔧Correção**: Variáveis que informam o estado anterior nos templates de alerta não estavam habilitadas.

**🔧Correção**: Valor padrão informado nos parâmetros de um monitor retornava nulo.

**🔧Correção**: Mensagem de falha geral ao adicionar monitores automáticos com alguns templates.

**🔧Correção**: Monitor boolean alarma com status falso quando os limites são invertidos.

**🔧Correção**: Namespace não é enviado em coletas WMI.
