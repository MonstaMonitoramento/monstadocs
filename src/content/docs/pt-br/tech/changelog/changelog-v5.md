---
title: "Changelog v5"
sidebar:
  order: 3
---

## Versão 5.1.22

**🔧Correção**: Evento de falha do dispositivo filho não envia alerta após retorno de falha do dispositivo pai.

**🔧Correção**: Permissões de dispositivos para usuários não admin.

**🔧Correção**: Widget Barra de Indicador perde o monitor selecionado ao editar o painel.

**🔧Correção**: Porta utilizada pelo `Monagent` pode acarretar em estouro de memória com pacotes malformados em servidores sem firewall habilitado.

**🔧Correção**: Em alguns casos ocorre uma tela branca ao acessar a opção de monitores automáticos.

## Versão 5.1.21

**🔧Correção**: Grupo de alertas na nuvem não grava alterações na primeira vez.

**🔧Correção**: *Widgets Piechart* e *Doughnutchart* adicionam dispositivos desativados.

**🔧Correção**: Alguns widgets não eram apresentados na publicação do painel.

## Versão 5.1.20

**✨Novo**: Cache inteligente para consultas `SNMP`.

**✨Novo**: Indicador de evento não resolvido na Linha do Tempo.

**✨Novo**: Tela responsiva para celulares.

**✨Novo**: Novos certificados aceitos para conexões por HTTPS.

**✨Novo**: Novos widgets para os painéis.

**✨Novo**: Atualização automática de novas versões.

**✨Novo**: Novos templates.

**✨Novo**: Cálculo de área do gráfico (ISP's podem reportar o tráfego em MB para a Anatel).

**🔧Correção**: Templates eram importados sem algumas métricas.

**🔧Correção**: IPv6 retornava erro nas coletas por `SNMP`.

**🔧Correção**: Monitores não permitiam trocar a unidade de medida.

**🔧Correção**: Erro de kernel ao remover alguns dispositivos.

**🔧Correção**: Mapas não mostravam dispositivos duplicados/criados em sua tela.

**🔧Correção**: `SNMP` não coletava informações em redes IPv6.

**🔧Correção**: Não era possível trocar a unidade de grandeza de monitores existentes nos dispositivos.

**🔧Correção**: Instâncias com aspas no nome geravam falha nas coletas.

**🔧Correção**: Alterações em painéis duplicados afetavam o original.

## Versão 5.0.4

**🔧Correção**: Comportamento incorreto do envio de alertas quando o estado normal não está marcado.

## Versão 5.0.3

**🔧Correção**: Restaurar backups não exibe arquivos.

## Versão 5.0

**✨Novo**: Novo kernel do sistema controla as chamadas para as coletas de monitores, com capacidade aumentada para milhares de consultas simultâneas.

**✨Novo**: Novos componentes para painéis.

**✨Novo**: Novos templates.

**✨Novo**: Controle contra excesso de consultas para dispositivos lentos.

**✨Novo**: Automação do certificado para acesso seguro com o *Let's Encrypt*.

**✨Novo**: Modo noturno.

**✨Novo**: Templates de alerta podem ser criados e configurados de forma individual.

**✨Novo**: Configuração de sons personalizada por dispositivo ou monitor.

**🔧Correção**: Algoritmo para monitores automáticos.

**🔧Correção**: Rotação de logs do banco de dados.

**🔧Correção**: Login automático quando há perda de conexão com o *browser*.