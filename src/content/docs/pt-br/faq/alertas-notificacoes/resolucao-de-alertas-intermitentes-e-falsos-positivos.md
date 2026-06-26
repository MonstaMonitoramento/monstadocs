---
title: "Como Resolvo Alertas Intermitentes e Falsos Positivos?"
---

## Descrição do Problema

Ocorrência de alertas intermitentes em monitores específicos, gerando notificações de queda ou criticidade que não condizem com o estado real do serviço (Falsos Positivos).

## Causas Comuns

Existem três cenários principais que disparam esse comportamento:

1. **Limites Mal Dimensionados**: Os gatilhos de **Aviso** e **Crítico** estão muito próximos da operação normal do dispositivo.
2. **Falha na Coleta de Dados**: O Monsta não recebe a resposta da requisição, seja por instabilidade na rede (perda de pacotes) ou sobrecarga no hardware do dispositivo monitorado.
3. **Falha no Uptime**: O Monsta utiliza, por padrão, pacotes icmp (ping) para testar se o dispositivo está ativo na rede. Quedas frequentes no uptime indicam que o Monsta não recebe o devido retorno do ping.

## Como Resolver

### Cenário 1: Ajuste de Thresholds (Limites)

Se o monitor alterna entre estados de alerta devido a picos normais de uso, execute o procedimento abaixo:

- Acesse o monitor com problema e edite suas configurações.
- Ajuste os campos de **Aviso** e **Crítico** para valores que se adequem à realidade de carga do equipamento.

### Cenário 2: Falha de Leitura em um Monitor

Geralmente, essa condição é causada por um *timeout* no processo de coleta de dados. Para identificar a causa, clique sobre o monitor com problema, clique no botão "Editar" e selecione a opção "Log de erros" no canto inferior esquerdo da janela. Se o log indicar falha por timeout, faça o seguinte:

1. **Solução para Protocolos Padrão (SNMP, WMI, SSH)**:    
    - Edite as configurações do **Dispositivo**.
    - Aumente o tempo de **Timeout** da coleta para dar mais margem de resposta ao equipamento sobrecarregado ou à rede lenta.
2. **Solução para timeout de Scripts**:    
    - Acesse o menu superior: **Configuração** > **Parâmetros**.
    - Localize a variável `lua.timeout` e aumente o seu valor conforme necessário.

### Cenário 3: Falhas no Uptime

O monitor de Uptime do Monsta utiliza pacotes **ICMP (Ping)** para validar a presença do dispositivo na rede. Uma falha neste monitor significa, tecnicamente, que o servidor do Monsta disparou o pacote e não recebeu o "Echo Reply" dentro do tempo esperado.

Quando o dispositivo está ligado, mas o Monsta reporta "Down", as causas geralmente são:

1. **Instabilidade de Rota**: Perda de pacotes na rede.
2. **Sobrecarga de CPU no Alvo**: O dispositivo prioriza o tráfego de produção e descarta pacotes ICMP para poupar processamento.
3. **Sensibilidade Alta**: O Monsta está configurado para considerar o dispositivo "fora do ar" com poucas falhas consecutivas.

No **1º Caso (Instabilidade de Rota)**, a correta configuração da hierarquia entre dispositivos (Pai e Filho) permite que o Monsta tente isolar a falha, disparando alertas apenas para o 'dispositivo pai' e indicando onde o problema inicia.

Para **2** e **3**, caso o ambiente apresente oscilações aceitáveis (ex: latência elevada em enlaces via satélite), configure o Monsta para ser mais permissivo. Isso é feito reduzindo a sensibilidade de detecção nas configurações do dispositivo para evitar alertas desnecessários. Para fazer isso, faça o seguinte:

- Edite o dispositivo específico.
- Na aba Detalhes, clique no botão Sensibilidade.
- Nessa janela você personaliza a quantidade de pacotes enviados, o tempo de espera para um retorno e o tempo entre o envio de cada pacote.

:::tip
Você pode personalizar a sensibilidade de forma geral clicando no botão "Opções" / "Opções Globais de Dispositivos" / "Sensibilidade". Esse recurso também está disponível ao editar um grupo de dispositivos na aba "Sensibilidade".
:::