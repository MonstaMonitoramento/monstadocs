---
title: "Como Resolver a Ausência de Dados nos Gráficos?"
---

Se você visualizar o símbolo **"---"** no lugar dos valor, isso indica que **o sistema não conseguiu utilizar o protocolo selecionado** para obter as informações necessárias do recurso monitorado.

Neste caso, a coleta de dados falhou, e nenhuma informação pode ser processada ou exibida nos gráficos.

## **O que fazer?**

Para investigar a causa específica da falha do protocolo, você pode checar o **Log de Erros** do evento:

1. **Edite o Monitor** em questão.
2. Na tela de edição que será aberta, procure e selecione a opção **"Log de Erros"** localizada no **canto inferior esquerdo** da tela.

O Log de Erros fornecerá detalhes técnicos sobre o motivo da falha de comunicação, auxiliando na solução do problema.

## Algumas falhas conhecidas:

### SNMP timeout (Múltiplas funções)

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *SNMP timeout stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'getex' [string "script"]:157: in function 'get' [string "script"]:1: in main chunk* |
| **Causa** | O equipamento monitorado não está respondendo ao SNMP. |
| **Solução** | Verifique se há comunicação entre o Monsta e o equipamento monitorado. Se estiver ok, verifique os itens abaixo:<br /><br />• O serviço de SNMP está sendo executado no equipamento monitorado?<br />• A porta configurada no Monsta é a mesma do equipamento?<br />• A comunidade está correta?<br />• Caso utilize SNMPv3, os dados configurados estão de acordo com a configuração do equipamento?<br />• Há algum firewall que bloqueia a comunicação na porta selecionada? |

---

### DNS resolution error (no record found)

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *DNS error: DNS resolution error: no record found for Query { name: Name("meuhost.com.br"), query_type: AAAA, query_class: IN } stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'getex' [string "script"]:157: in function 'get' [string "script"]:1: in main chunk* |
| **Causa** | O nome do host não é resolvido pelo servidor DNS. |
| **Solução** | Verifique se os servidores DNS configurados no sistema operacional estão corretos. |

---

### I/O: Timeout connecting

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *I/O: Timeout connecting to xx.xx.xx.xx:pppp stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'connect' [string "script"]:356: in function <[string "script"]:337> (tail call): in function <(tail call):-1>* |
| **Causa** | A consulta ao host xx.xx.xx.xx na porta pppp não retorna informações. |
| **Solução** | Cheque as seguintes informações:<br /><br />• Há comunicação entre o Monsta e o Host monitorado?<br />• O serviço que reporta informações na porta solicitada está em execução?<br />• Há algum firewall bloqueando a conexão? |