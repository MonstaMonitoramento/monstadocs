---
title: "Changelog v2"
sidebar:
  order: 6
---

## Versão 2.0.11

**🔧Correção**: Backup - Durante a restauração de um *backup*, o Monsta poderia trocar o nome dos templates.

## Versão 2.0.10

**✨Novo**: Exibição em modo Árvore - Alterado o valor mínimo da opção "Tamanho da Imagem" para 5.

**🔧Correção**: Não é possível adicionar instâncias com descrições que contêm somente números.

**🔧Correção**: Após selecionar um período grande a ser exibido em monitores com métricas de verdadeiro/falso, o Monsta mostra tudo como Falso.

**🔧Correção**: Sob certas condições o Monsta mostra uma mudança de estado para um dispositivo excluído.

**🔧Correção**: Quando um dispositivo pai está no estado "*Down*", o Monsta pode mostrar os seus filhos no estado "*Up*".

**🔧Correção**: Quando adicionada uma nova métrica a um monitor existente, ao clicar em OK o sistema substituía a mesma por uma cópia da métrica anterior.

## Versão 2.0.6

**🔧Correção**: Sob certas condições o Monsta pode indicar o estado errado para um monitor.

## Versão 2.0.5

**✨Novo**: Nova Identidade Visual.

**✨Novo**: Nova tela de Configuração com Templates, Imagens, *Backup* e Fontes de Dados.

**✨Novo**: Opção para adicionar ícones ou imagens personalizadas para templates, dispositivos e monitores.

**✨Novo**: Acesso a fontes de dados dos monitores.

**✨Novo**: Novos templates.

**✨Novo**: Novos elementos gráficos para os painéis.

**✨Novo**: Cliente para consultas SQL em bancos MySQL e SQLite.

**✨Novo**: Possibilidade de adicionar vários monitores em um único gráfico.

**✨Novo**: Monitores do tipo texto.

**✨Novo**: Edição do tamanho do pacote ICMP.

**✨Novo**: Novas funções para os scripts.

**✨Novo**: Verificação de POP, IMAP e FTP com autenticação.

**✨Novo**: Verificação de strings em arquivos de texto.

**🔧Correção**: Durante a ativação o Monsta não aceitava a chave da licença devido ao horário incorreto do servidor.

**🔧Correção**: Tela não suportava mais do que 60 monitores por dispositivo.

**🔧Correção**: Monitores que não continham no `SNMP` uma `OID` de descrição não eram ativados.

**🔧Correção**: Alguns monitores entravam em alerta com a mensagem "sem valor", mesmo estando ativos.