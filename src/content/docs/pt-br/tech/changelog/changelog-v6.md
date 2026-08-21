---
title: Changelog v6
description: Acompanhe o Changelog da versão 6 do Monsta e conheça as novas
  funcionalidades, melhorias, correções e alterações realizadas em cada
  atualização da plataforma.
sidebar:
  order: 2
---
## Versão 6.0.19 Beta

**🔧Correção**: **Alertas não enviados**. Alguns alertas não eram acionados mesmo com o valor acima do limite. Isso acontecia quando o valor monitorado raramente mudava: após a reinicialização do sistema, ele não estava disponível na memória e o alerta não conseguia confirmar o limite, permanecendo inativo.

## Versão 6.0.17

**✨Novo**: **Relatórios Mensais com Inteligência Artificial**. Agora, sua conta gera automaticamente relatórios mensais enriquecidos com *insights* baseados em IA.

![image.png](/src/assets/images/image-10.png)

**✨Novo**: **Execução Remota via PowerShell**. A Sonda permite a execução de comandos e *scripts* em PowerShell diretamente pelo console. Por questões de segurança, esse recurso é disponibilizado somente quando o usuário autoriza sua utilização durante a instalação da Sonda. Além disso, todos os comandos são executados utilizando um **usuário com privilégios restritos (não administrador)**.

:::note

Este recurso requer a instalação da versão mais recente da Sonda Monsta, disponível em nosso site.

:::

![image.png](/src/assets/images/image-5.png)

**✨Novo**: **Monitoramento S.M.A.R.T.**. Adicionamos suporte à coleta de dados S.M.A.R.T. (*Self-Monitoring, Analysis, and Reporting Technology*) de discos físicos, permitindo acompanhar a integridade, a vida útil e os indicadores de saúde do armazenamento para identificar possíveis falhas antes que elas afetem o ambiente. 

:::note

Este recurso requer a instalação da versão mais recente da Sonda do Monsta, disponível em nosso site.

:::

![image.png](/src/assets/images/image-9.png)

🔧**Correção**: **Preservação do White Label em atualizações**. Corrigido um comportamento inesperado onde as atualizações do sistema retornavam o logotipo padrão.

🔧**Correção**: **Atualização no status de eventos.** Agora, quando um dispositivo ou monitor alterna de estado entre aviso e crítico, apenas o evento mais recente permanece marcado como não resolvido na linha do tempo, evitando o acúmulo de pendências para o mesmo incidente.

**🔧Correção**: **Reconexão de Agentes Após Backup**. Corrigida a reconexão de agentes após a restauração de backup da nuvem em novas instalações.

**🔧Correção**: **Ajuste no Disparo de Alarmes para Monitores**. Corrigido problema pontual que impedia o disparo de alarmes em alguns monitores.

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