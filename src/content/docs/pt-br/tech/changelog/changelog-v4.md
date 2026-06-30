---
title: "Changelog v4"
sidebar:
  order: 4
---

## Versão 4.1.19

**✨Novo**: Preparação para o upgrade da versão **5**. OBS: Essa atualização reiniciará o servidor.

## Versão 4.1.16

**🔧Correção**: Pasta `/var/monsta/agent/store` não elimina arquivos antigos.

**🔧Correção**: Valor máximo em um gráfico é informado como `0` quando o valor é negativo.

**🔧Correção**: Cache `SNMP`, em algumas situações, impede o agente de efetuar pesquisas contra o dispositivo.

**🔧Correção**: `SNMP` nativo utiliza o mesmo request-id e gera um alto consumo de memória em alguns equipamentos.

**🔧Correção**: No Painel, em algumas situações, o botão de salvar não tem efeito após uma alteração ou inserção de um componente.

**🔧Correção**: Programa `monagentd` deixa de responder a requisições do core do Monsta em algumas situações.

**🔧Correção**: Instâncias com nomes numéricos apresentam falha no monitoramento.

**🔧Correção**: Regras de monitores automáticos criam monitores com o grupo de alerta em branco.

## Versão 4.1.15

**✨Novo**: Possibilidade de remover monitores automáticos em minutos/horas/dias.

**🔧Correção**: Os monitores automáticos duplicam os itens criados quando não está marcada a busca por instâncias dinâmicas.

**🔧Correção**: Aviso de nova versão disponível leva até 15 minutos para aparecer na tela.

**🔧Correção**: Logs do `monstadb` não são rotacionados corretamente.

## Versão 4.1.14

**✨Novo**: Descoberta automática de monitores (o Monsta cria e remove monitores automaticamente conforme eles são tratados no dispositivo).

**✨Novo**: Filtro para exibição de dispositivos e monitores.

**✨Novo**: Possibilidade de atualizar o Monsta para versões Beta.

**✨Novo**: Backups com até 1 mês de informações para restaurar.

**✨Novo**: Opção para importar e exportar templates.

**✨Novo**: `WebSockets` - Nova função `ws.send_recv()` para ser utilizada nos monitores.

**✨Novo**: Créditos de SMS e e-mail com pouca quantidade são alertados na tela.

**✨Novo**: Cache local para instâncias em `SNMP`.

**✨Novo**: Botão para inativar o monitoramento de um host.

**✨Novo**: `SNMP` nativo (para um menor consumo de recursos).

**✨Novo**: Opção para salvar dados do usuário na tela de login.

**✨Novo**: Linha do tempo exibe o valor dos monitores.

**✨Novo**: Barra para aumentar o texto dos dispositivos na tela principal.

**✨Novo**: Novo template TP-Link - Switch.

**✨Novo**: Novo template Cambium Networks.

**✨Novo**: Novo template WNI - Challenger.

**✨Novo**: Novo template Intracom Telecom - OmniBAS.

**✨Novo**: Novo template Intelbras - APC.

**✨Novo**: Novo template Juniper - MX5.

**✨Novo**: Novo template Cianet - OLT GEPON.

**✨Novo**: Novo template Huawei - OLT MA5600.

**✨Novo**: Novo template Socomec - Net Vision Masterys BC (Nobreak).

**✨Novo**: Novo template 3Com - 4800 Switch.

**✨Novo**: Novo template Ericsson - Mini-Link.

**✨Novo**: Novo template Datacom (OLT).

**✨Novo**: Novo template Volt - Controlador de Carga MPPT.

**✨Novo**: Novo template Volt - Full Power 620 Evolution.

**✨Novo**: Novo template Volt - Ponto de Distribuição AC Evolution.

**✨Novo**: Novo template Volt - Ponto de Distribuição Cliente (PDC Evolution).

**✨Novo**: Novo template Volt - Pop Protect.

**✨Novo**: Novo template Volt - Power Net 1000 Evolution.

**✨Novo**: Novo template Volt - Mini Central UPS `SNMP`.

**✨Novo**: Novos monitores para Mikrotik - Routerboard.

**🔧Correção**: Exibição dos grupos em ordem alfabética.

**🔧Correção**: Novos dispositivos aparecem para usuários sem autorização para acessá-los.

**🔧Correção**: SMS's com mais de 160 caracteres não são enviados (mensagens agora são truncadas).

**🔧Correção**: Opção de exibição em tempo real não funcionava adequadamente na linha do tempo.

**🔧Correção**: Removidas bibliotecas da pasta `/opt/monsta/lib` que conflitavam com atualizações do servidor Linux.

**🔧Correção**: Monitores de templates existentes não podem ser alterados.

**🔧Correção**: Fonte de dados para checagem do uptime não aparecia ordenada. Em alguns casos, alguns itens não são mais exibidos.

**🔧Correção**: Backups são sobrepostos quando existe mais de uma licença em uso em uma única conta.

**🔧Correção**: Clonar um dispositivo causa a publicação do gráfico do dispositivo primário.

**🔧Correção**: Limites de um monitor não são alterados quando alterado o tipo de retorno (Ex: numérico, boolean, string, etc.).

**🔧Correção**: Função `params.InstaceId()` não retorna o valor correto, causando falha nos monitores que a utilizam.

**🔧Correção**: Dispositivos são considerados críticos na soma total mesmo se apenas um monitor estiver em estado crítico.

**🔧Correção**: Alguns logs do Monsta não estavam sendo rotacionados.

**🔧Correção**: Monsta grava informações repetidas no arquivo `moncored.log`, ocasionando um crescimento muito grande desses arquivos.

**🔧Correção**: Ao restaurar um backup, os ícones não são copiados.

**🔧Correção**: Caixas de dispositivos não balançam quando o mesmo muda de estado.

**🔧Correção**: Ao instalar uma licença, ocasionalmente o Monsta informa que a mesma já está em uso.

**🔧Correção**: Gráficos com frequência de monitoramento em segundos agora são exibidos em intervalo de 1h por padrão.

**🔧Correção**: No painel, gráficos permitem a seleção de monitores do tipo `string`.

## Versão 4.0.20

**✨Novo**: Adicionada opção de ferramentas para o dispositivo (`traceroute`, `ping` e abrir em um *browser*).

**✨Novo**: Opção para ocultar as legendas dos gráficos em um painel.

**✨Novo**: Envio de alertas pelo Telegram.

**✨Novo**: Exibição de gráficos em tempo real.

**✨Novo**: Nova árvore de visualização (Sunburst).

**✨Novo**: Novo template BGP - BGP4.

**✨Novo**: Novo template Intelbras - Gravadores (HDCVI).

**✨Novo**: Novo template Sophos - XG Firewall.

**✨Novo**: Novo template Brother - Impressora Laser.

**✨Novo**: Novo template Ubiquiti - Edgeswitch.

**✨Novo**: Novo template Parks - OLT 10008S.

**✨Novo**: Novo template Huawei - NE20S.

**✨Novo**: Novo template Huawei - S6720.

**✨Novo**: Novo template Morningstar - XPS.

**✨Novo**: Novo template Volt - Net Probe.

**✨Novo**: Novo template BlockBit - UTM.

**✨Novo**: Novo template Seagate - NAS.

**✨Novo**: Novo template SMS - Nobreak.

**✨Novo**: Novo template Intelbras - WOM.

**✨Novo**: Novo template Apple - Mac OS X.

**✨Novo**: Novo template Lenovo - IX4.

**✨Novo**: Novo template Dell - iDRAC.

**✨Novo**: Novo template Polycom - Videoconferência.

**✨Novo**: Novo template Fiberhome - OLT.

**🔧Correção**: Durante a edição/inserção de um dispositivo, ao informar um tamanho de pacote na checagem do uptime, o botão de Ok não salva as configurações.

**🔧Correção**: Endereços IP's não são exibidos durante a seleção de uma instância.

**🔧Correção**: As legendas de cores aparecem sem informações nos gráficos publicados.

**🔧Correção**: Em algumas situações de stress do sistema, monitores que utilizam ICMP, como uptime e ping, param de funcionar.

**🔧Correção**: Ao clonar um dispositivo, o grupo padrão é adicionado automaticamente.

**🔧Correção**: O Monsta envia alertas dos monitores de um dispositivo mesmo quando este está em estado crítico.

**🔧Correção**: Alguns scripts com instâncias dinâmicas não conseguem obter o valor das métricas.

**🔧Correção**: Na edição de uma métrica, o valor máximo não permite valores negativos.

**🔧Correção**: A publicação de um gráfico com várias instâncias não mostra seus nomes na legenda.

**🔧Correção**: Em algumas situações, o serviço de verificação de dados para de responder e se faz necessário reiniciar o serviço.

## Versão 4.0.12

**✨Novo**: Percentil e possibilidade de selecionar o tempo de agrupamento de dados nos gráficos.

**✨Novo**: Seleção de múltiplos estados na tela de dispositivos.

**🔧Correção**: Componente para selecionar datas em um gráfico algumas vezes fica lento.

**🔧Correção**: Algumas métricas aparecem com valores zerados no Painel.

**🔧Correção**: Preenchimento dos gráficos não mantém a mesma cor da linha.

**🔧Correção**: Em monitores com múltiplas métricas do tipo boolean, ao clicar sobre uma métrica, o gráfico exibido era sempre relativo à primeira.

**🔧Correção**: Instâncias com nomes extensos causam erro de carregamento durante a adição de um monitor.

## Versão 4.0.6

**🔧Correção**: Não é possível salvar dispositivos que utilizam `snmp` com porta diferente da 161.

**🔧Correção**: Não é possível salvar uma fonte de dados com o retorno diferente do tipo numérico.

**🔧Correção**: Visualização de um ponto nos gráficos não mostra os segundos.

**🔧Correção**: Monitores do tipo string eram retornados sempre com o estado normal.

## Versão 4.0.4

**✨Novo**: Função ping.send() modificada para retornar sucesso após o recebimento do primeiro pacote.

**✨Novo**: No monitor uptime é exibida a informação do tempo que o equipamento está ligado (apenas para dispositivos com `snmp`).

**✨Novo**: Botão para exportar/imprimir um gráfico em formatos PNG, PDF, SVG, CSV e XLS.

**🔧Correção**: Ao adicionar um dispositivo, o monitor uptime inicia em estado crítico.

**🔧Correção**: Ao remover um grupo de dispositivos de um usuário, o Monsta adiciona todos os dispositivos deste grupo individualmente para o mesmo usuário.

**🔧Correção**: Retornada a legenda dos gráficos para o modelo anterior.

**🔧Correção**: Dispositivos marcados para não enviar alertas não eram listados na tela de visualização dos dispositivos.

**🔧Correção**: Nome da métrica de um monitor retornada nos alertas quando um monitor retorna ao estado normal está incorreta.

**🔧Correção**: `SNMP` v3 gera erro durante a autenticação.

**🔧Correção**: Em sistemas com versões do `openssl` posteriores à `1.0.1e`, a instalação do RPM apresenta uma falha ao gerar o certificado SSL e o servidor HTTP não inicia.

**🔧Correção**: Número de tentativas era ignorado em algumas situações.

## Versão 4.0.2

**✨Novo**: Core do sistema totalmente remodelado para menor consumo de hardware e aumento de performance.

**✨Novo**: Banco de dados das configurações agora trabalha em memória.

**✨Novo**: Novo formato para seleção de cores para os gráficos dos monitores e Painel.

**✨Novo**: Novos modelos para exibição em árvore (Hierarquia e Mapa) com zoom e pan.

**✨Novo**: Intervalo de verificação de dispositivos e monitores pode ser em segundos.

**✨Novo**: Possibilidade de buscar por instâncias dinâmicas em um dispositivo (Ex. usuários autenticados com PPPoE).

**✨Novo**: Novas variáveis para serem utilizadas nos templates de alerta.

**🔧Correção**: Gráfico do uptime não é exibido corretamente quando selecionado um período superior a 4 meses.

**🔧Correção**: Em alguns browsers, as caixas de grupos alternam de lugar ao clicar sobre elas.

**🔧Correção**: Em alguns casos, a quantidade de dispositivos por status não é exibida corretamente.

**🔧Correção**: Na exibição em árvore, dispositivos sem um ícone não podem ser selecionados.

**🔧Correção**: Habilitada a paginação na Linha do Tempo.

**🔧Correção**: Durante a edição de uma métrica em um template, as setas de mover para cima ou para baixo deletam a métrica selecionada.

**🔧Correção**: Caracteres especiais não são exibidos corretamente na tela de dispositivos.

**🔧Correção**: Correção do algoritmo do monitor "Uso de CPU" do template Linux.