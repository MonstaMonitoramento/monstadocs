---
title: "Monitorando a Quantidade de Usuários por Servidor PPPoE Server no Mikrotik"
---

Para provedores que utilizam o **Mikrotik** como concentrador PPPoE, saber o número exato de clientes conectados em cada servidor é uma métrica essencial. Este guia rápido mostra como você pode configurar o **Monsta** para monitorar o total de usuários por `pppoe-server`.

## 1. Coleta de Dados

O método utilizado para obter a contagem *por servidor* no Mikrotik é através da execução de um comando via **SSH** (*Secure Shell*).

### 1.1. Configuração de Acesso no Mikrotik

Antes de configurar no Monsta, seu Mikrotik deve permitir o acesso SSH:

1. **Crie um Usuário Específico**: No Mikrotik, crie um usuário (ex: `monsta`) com uma senha forte e permissões mínimas (apenas o necessário para executar o comando, como `read`).
2. **Habilite o Serviço SSH**: Garanta que o serviço SSH (porta 22, por padrão) esteja ativo e que o Firewall do Mikrotik permita conexões de entrada do IP onde o seu Monsta está instalado.

## 2. Configurando o Monitor no Monsta

Clique no botão para adicionar um novo dispositivo e insira as seguintes informações:

1. Na aba Detalhes, preencha as seguintes informações: 
    1. **Nome do Dispositivo**: Nesse campo digite qualquer texto que identifique seu equipamento;
    2. **Endereço IP**: Informe o IP do Mikrotik;
2. Na aba Templates, selecione "Mikrotik Routerboard;
3. Na aba coleta, preencha a opção "SSH" com o usuário, senha e porta caso seja diferente da 22. 

:::tip
Você pode utilizar o botão "Testar" para checar se a conexão está ok.
:::


4. Clique em Salvar para criar o novo dispositivo.

![image-1759756111276.png](../../../../../assets/images/p122_image-1759756111276.png)
*Tela de configuração do SSH*

## 3. Criando o Monitor de Usuários

Após criar o dispositivo, clique sobre ele para que os monitores apareçam na parte inferior da tela. Clique em "+" para adicionar um novo monitor.

Na janela de monitores, procure por "PPPoE: Usuários por servidor PPPoE" e selecione qual servidor você deseja monitorar a quantidade de usuários.

![image-1759756922247.png](../../../../../assets/images/p122_image-1759756922247.png)
*Tela para adicionar monitores*

Clique no botão para criar o monitor.

Agora seu Monsta monitora o total de usuários dentro desse servidor. Se deseja adicionar o monitoramento de outros servidores, basta clicar novamente em "+" e selecionar as opções disponíveis.



:::tip
Ao abrir o monitor para visualizar seu gráfico, clique no botão "Editar" localizado no canto superior direito e informe os limites no qual gostaria de receber alertas em caso de problemas.
:::



![image-1759757535089.png](../../../../../assets/images/p122_image-1759757535089.png)
*Exemplo de limites de alerta*
