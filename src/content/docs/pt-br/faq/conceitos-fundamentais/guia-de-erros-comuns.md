---
title: "Guia de Erros Comuns"
---

Este documento é um guia rápido para identificar e corrigir falhas em scripts personalizados no Monsta Tecnologia. Se você encontrou um erro de execução ou um retorno inesperado em um sensor, consulte as categorias abaixo.

**Estrutura de cada tópico**:

1. **Erro**: Descrição do sintoma ou mensagem de log.
2. **Causa Provável**: O que geralmente dispara esse comportamento.
3. **Solução**: Passo a passo para correção.

---

### Lua script runner timeout

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *Lua script runner timeout: deadline has elapsed* |
| **Causa** | Este erro ocorre quando o motor de execução do Monsta interrompe o script Lua porque ele excedeu o tempo limite (timeout) permitido para a execução de um sensor. Por padrão, o Monsta encerra scripts que demoram muito para responder para evitar que o sistema fique travado ou consuma recursos excessivos do servidor. |
| **Solução** | Acesse **Configuração > Parâmetros** e utilize o campo de pesquisa para localizar a chave `lua.timeout`. O valor padrão é de 130 segundos. Para alterá-lo, clique em **Desbloquear**, insira o novo valor e salve. |

---

### Pagefile: Timeout connecting

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *Pagefile: Timeout connecting to xx.xx.xx.xx:xxxx stack traceback: [C]: in function 'poll' [string "?"]:x: in function 'connect' [string "script"]:xxx: in function <[string "script"]:xxx> (tail call): in function <(tail call):-1>* |
| **Causa** | Este erro indica uma falha na tentativa de estabelecer uma conexão de rede. O script Lua conseguiu iniciar a chamada, mas ela expirou antes que o dispositivo de destino respondesse ao "aperto de mão" (handshake) da conexão.<br /><br />O *"stack traceback"* mostra que a falha ocorreu exatamente no momento da tentativa de conexão (`in function 'connect'`), antes mesmo de qualquer dado ser enviado ou recebido. |
| **Solução** | Edite o dispositivo, acesse o menu **Coleta > WMI** e aumente o campo WMI Timeout. Utilize o botão de "Testar" para validar a comunicação. Após, salve as modificações.<br /><br />Caso o problema persista, outros fatores relacionados a rede podem impedir essa comunicação. Nesse caso, verifique em sua rede:<br /><br />• **Firewall/Bloqueio**: Existe uma regra de firewall no destino ou no meio do caminho (ACL, IPS) bloqueando o IP do Monsta na porta especificada.<br />• **Serviço Offline**: O serviço que você está tentando monitorar (ex: API, servidor web, banco de dados) está parado ou não está escutando naquela porta específica.<br />• **Rede Inalcançável**: O servidor Monsta não possui uma rota válida para o IP de destino.<br />• **Porta Incorreta**: O script está tentando conectar em uma porta diferente da que o serviço utiliza.<br />• **Carga Excessiva no Destino**: O dispositivo alvo está com a CPU tão alta que não consegue processar novas requisições de conexão. |

---

### Tempo de Resposta: ping failed

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *Tempo de Resposta: ping failed: Request timeout for icmp_seq x* |
| **Causa** | Este erro ocorre quando o Monsta envia um pacote de eco ICMP (o famoso "Ping") para um dispositivo, mas não recebe a resposta (Echo Reply) dentro do tempo esperado. |
| **Solução** | O dispositivo monitorado não respondeu às solicitudes de ICMP (ping) do Monsta.<br /><br />💡 **Dica**: Se o equipamento estiver em uma rede com alta latência ou perda de pacotes, ajuste a sensibilidade de detecção. Para isso, edite o dispositivo e acesse **Detalhes > Sensibilidade**, alterando os parâmetros conforme a necessidade do ambiente. |

---

### SNMP timeout stack traceback

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *SNMP timeout stack traceback: [C]: in function 'poll' [string robbery/snmp_checker]:xx: in function 'getex' [string "script"]:xx: in function 'get' [string "script"]:xx: in main chunk* |
| **Causa** | Este erro ocorre quando o script tenta realizar uma leitura SNMP e a conexão expira sem receber os dados solicitados. |
| **Solução** | O dispositivo monitorado não respondeu às solicitações de SNMP do Monsta.<br /><br />Edite o dispositivo, acesse o menu **Coleta > SNMP** e aumente o Timeout SNMP. Utilize o botão de "Testar" para validar a comunicação. Após, salve as modificações.<br /><br />Caso o problema persista, verifique em sua rede:<br /><br />• **Comunidade SNMP Incorreta**: A "Community String" (ex: `public` ou `private`) configurada no Monsta não coincide com a configurada no dispositivo.<br />• **Versão do SNMP Divergente**: O dispositivo está usando SNMP v2c e o script/configuração está tentando v1 (ou vice-versa), ou há erro nas credenciais de v3.<br />• **ACL ou Firewall**: O dispositivo possui uma lista de controle de acesso (ACL) que permite apenas IPs específicos realizarem consultas SNMP, e o IP do Monsta não está nela.<br />• **Porta Bloqueada**: A porta UDP 161 (padrão do SNMP) está bloqueada no caminho.<br />• **Sobrecarga do Agente SNMP**: O processor do dispositivo monitorado está tão ocupado que o serviço (agente) SNMP não consegue responder à consulta a tempo. |

---

### Error converting to type: Float

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *Error converting to type: Float* |
| **Causa** | Esse erro ocorre quando o sistema espera um **número decimal (Float)**, mas recebeu algo que ele não consegue transformar em número, como um texto (String) inválido ou um valor nulo (`nil`). |
| **Solução** | Revise o script do monitor para garantir que o retorno não contenha **strings** (como vírgulas ou unidades de medida) no campo de valor. Caso o monitor apresente leituras normais, mas exiba falhas intermitentes com esse erro, é provável que o dispositivo esteja retornando um valor **nulo (nil)**. Isso ocorre quando não há resposta na consulta; nesses casos, verifique nos logs do equipamento a existência de alguma falha. |

---

### Erro: wamp.error.no_such_procedure

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *`wamp.error.no_such_procedure`* |
| **Causa** | Indica, na maioria dos casos, que o serviço **`monkerneld`** não está em execução no sistema operacional Linux onde o software está instalado. O serviço `monkerneld` é importante para o funcionamento correto do software, e sua inatividade impede que o Monsta execute procedimentos necessários. |
| **Solução** | A solução envolve garantir que o serviço `monkerneld` seja iniciado. O usuário pode escolher entre duas abordagens principais para contornar essa situação:<br /><br />**A. Reiniciar o Sistema**: A maneira mais abrangente de resolver a maioria dos problemas de inicialização de serviços é simplesmente **reiniciar o sistema Linux** onde o software está instalado. Ao reiniciar, o sistema operacional tentará carregar e iniciar todos os serviços configurados, incluindo o `monkerneld`, de forma automática.<br />**B. Iniciar o Serviço Manualmente (Recomendado)**: Caso a reinicialização não seja viável ou demorada, o usuário pode tentar iniciar o serviço diretamente usando o **`systemctl`**, que é a ferramenta padrão de gerenciamento de serviços em muitas distribuições Linux modernas (como Ubuntu, Debian, CentOS, RHEL, etc.).<br />**Passos**: <br />1. Abra um **Terminal** (ou utilize uma sessão SSH) no servidor Linux.<br />2. Execute o seguinte comando para tentar iniciar o serviço: `sudo systemctl start monsta-com.monkerneld`<br />**Nota**: É obrigatório que este comando exija permissões de **superusuário (sudo)**.<br /><br /> Após executar qualquer uma das ações acima (reiniciar o sistema ou iniciar o serviço manualmente), você pode **verificar o status do serviço** para garantir que ele esteja ativo e em execução: `systemctl status monsta-com.monkerneld`<br />O status ideal deve indicar **`active (running)`** |

---

### Ssh error occured: Key exchange init failed

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *Ssh error occured: Key exchange init failed stack traceback* |
| **Causa** | Este erro ocorre durante a tentativa de conexão SSH entre o Monsta e um dispositivo remoto (geralmente modelos mais antigos de switches, roteadores ou rádios). Ele indica que o Monsta e o dispositivo não conseguiram entrar em acordo sobre qual **algoritmo de troca de chaves (*Key Exchange*)** utilizar, pois o dispositivo utiliza padrões que hoje são considerados legados ou inseguros por bibliotecas modernas. |
| **Solução** | O Monsta utiliza bibliotecas de criptografia de última geração. A falha na troca de chaves (*Key Exchange*) é um alerta de que o seu dispositivo remoto está operando com padrões de segurança obsoletos. A correção definitiva é a atualização do dispositivo monitorado para que suporte algoritmos de criptografia seguros. |

---

### No route to host (os error 113)

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *No route to host (os error 113) stack traceback* |
| **Causa** | O erro `os error 113` é um código de erro de rede do sistema operacional que indica que o host de destino não pôde ser alcançado. O sistema operacional não sabe por qual interface de rede deve enviar o pacote para alcançar aquele IP específico. |
| **Solução** | Para resolver o erro, certifique-se de que a tabela de roteamento do sistema possui um caminho válido para o IP de destino e que o gateway padrão está configurado corretamente para encaminhar os pacotes fora da rede local. |