---
title: "Changelog v3"
sidebar:
  order: 5
---

## Versão 3.1.7

**🔧Correção**: Ao adicionar monitores com uma quantidade grande de instâncias, o Monsta exibe uma mensagem de timeout.

## Versão 3.1.6

**🔧Correção**: Em alguns casos ocorre vazamento de memória e falha na execução de alguns monitores.

## Versão 3.1.5

**✨Novo**: Número de tentativas foi incrementado para 120.

**✨Novo**: Filtro "Procurar Dispositivo" busca também por endereço IP.

**✨Novo**: Tipo String aceita valores em hexadecimal.

**✨Novo**: Tipo String aceita textos.

**✨Novo**: Busca por WMI aceita outros namespaces.

**✨Novo**: Função `return()` em um script pode forçar o estado de uma métrica em um monitor.

**✨Novo**: Aviso sonoro para mudanças de status.

**✨Novo**: Possibilidade de publicar um link para um monitor sem a necessidade de login.

**✨Novo**: Template Unbound - DNS Server.

**✨Novo**: Template Intelbras - Switches.

**✨Novo**: Template Microsoft - Windows (Inventário).

**✨Novo**: Monitores "Serviços em Execução", "Estado da Placa-Mãe", "Estado da Memória Física", "Estado do Processador" e "Estado da Fonte de Alimentação" para o template Microsoft - Windows.

**✨Novo**: Monitores "Processos", "Carga (Load Average)" e "Endereço MAC" para o template Linux.

**✨Novo**: Monitor "Endereço MAC" para os templates Genérico, Linux, Ubiquiti - AirOS 5.6 e Ubiquiti - Airmax AC.

**🔧Correção**: Filtro de exibição por estado pode deixar alguns dispositivos de fora da lista.

**🔧Correção**: Tamanho do pacote ICMP na checagem do *uptime* era ignorado.

**🔧Correção**: Tipo de retorno não era tratado nos templates do Monsta.

**🔧Correção**: Seleção de um intervalo de data em um monitor do tipo string não funcionava.

**🔧Correção**: Histórico do *uptime* não mostrava mais do que 4 meses de dados.

**🔧Correção**: Script de inicialização do Monsta poderia não iniciar a aplicação após uma parada forçada.

**🔧Correção**: Algumas vezes os créditos de SMS e e-mail eram mostrados incorretamente.

**🔧Correção**: Em alguns casos, o número de dispositivos por estado era mostrado incorretamente.

**🔧Correção**: Provável correção para o envio de alertas de monitores mesmo com o dispositivo **.

**🔧Correção**: Banco de dados de monitores travava ao trocar o nome do host do servidor.

**🔧Correção**: Desabilitado o tratamento de unidade de grandeza na edição de um monitor.

**🔧Correção**: Monitor "Clientes Conectados" dos templates Airmax AC e Ubiquiti - AirOS 5.6 não exibiam informações.

**🔧Correção**: Monitor "Erros na Interface" do template Ubiquiti - Airmax AC não exibia as interfaces de rede.

**🔧Correção**: Monitor "Frequência de Entrada" do template Nobreak - Genérico estava com o cálculo do limite máximo errado.

## Versão 3.0.13

**✨Novo**: Novos templates disponíveis.

## Versão 3.0.11

**✨Novo**: Usuários e restrições para dispositivos.

**✨Novo**: Grupos de dispositivos.

**✨Novo**: Visualização por grupos de dispositivos.

**✨Novo**: Disponibilizado programa para resetar ao valor padrão a senha do usuário admin em `/opt/monsta/bin/resetadmin`.

**🔧Correção**: O monitor *Uptime* não permite a visualização do histórico com mais de 6 dias.

**🔧Correção**: O ícone de conexão com a nuvem algumas vezes aparece, erroneamente, como estado crítico.

**🔧Correção**: Histórico de conexão com a nuvem não é registrado na Linha do Tempo.

**🔧Correção**: Em um monitor existente, clonar métricas cuja descrição é um número faz com que o botão "Ok" não funcione.

**🔧Correção**: Mecanismo de supervisão de processos não controla corretamente o processo de atualização automática.

**🔧Correção**: Em um monitor existente, uma métrica clonada copia o valor máximo da original.

**🔧Correção**: Monitor *uptime* não exibe informações sobre os estados *Up* e *Down*.

**🔧Correção**: Provável correção para corrompimento do banco de dados dos monitores quando encerrado o Monsta.

**🔧Correção**: Quando deletada uma métrica de um monitor, ela não aparece no gráfico, mas continua sendo monitorada.