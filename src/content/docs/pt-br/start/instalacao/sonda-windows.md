---
title: "Sonda: Monitoramento Windows"
sidebar:
  order: 5
---

Maximize a eficiência e a estabilidade da sua rede com a nossa Sonda de Monitoramento WMI para Windows. Desenvolvida para oferecer uma visão detalhada do desempenho e da saúde de seus servidores e estações de trabalho Windows, esta ferramenta essencial coleta métricas cruciais através da API para WMI (Windows Management Instrumentation).

## Para que serve a Sonda?

Imagine ter um raio-x do seu ambiente Windows em tempo real. Nossa sonda age dessa forma, permitindo que você:

- Monitore o desempenho do sistema: Acompanhe o uso da CPU, memória RAM, disco rígido e rede para identificar gargalos e otimizar recursos.
- Detecte problemas proativamente: Receba alertas sobre eventos críticos, falhas de serviços e outros indicadores de potenciais instabilidades antes que afetem seus usuários.
- Analise o consumo de recursos: Entenda como os aplicativos e processos utilizam os recursos do sistema para um planejamento de capacidade mais inteligente.
- Visualize dados importantes: Integra as métricas coletadas com o Monsta para você criar dashboards personalizados e detalhados.
- Diagnostique problemas remotamente: Obtenha informações valiosas para solucionar incidentes de forma rápida e eficiente, mesmo sem acesso físico à máquina.

**Integração perfeita**: Projetada especificamente para o ambiente Windows, explorando ao máximo os recursos da API WMI.

**Leve e eficiente**: Baixo consumo de recursos, garantindo que o monitoramento não impacte o desempenho do sistema monitorado.

**Fácil instalação** e configuração: Um processo simples e intuitivo para colocar sua sonda em funcionamento rapidamente.

**Dados precisos** e confiáveis: Coleta de informações detalhadas e em tempo real para uma análise precisa da sua infraestrutura.

**Flexibilidade**: Adapte a coleta de métricas às suas necessidades específicas.

Com a nossa Sonda de Monitoramento WMI para Windows, você terá o controle total sobre a saúde e o desempenho dos seus sistemas Windows, garantindo uma infraestrutura de TI robusta, eficiente e sempre disponível. Comece agora mesmo a monitorar com inteligência!

## Instalação da Sonda

1. Baixe o programa da sonda no sistema operacional Windows que deseja monitorar;


| | |
| --- | --- |
| ![image-1660325708746.png](../../../../../assets/images/p139_image-1660325708746.png) | [**DOWNLOAD**](https://www.monsta.com.br/monsta/download/MonstaProbe.exe "Monsta - Sonda Coletora")<br />[https://www.monsta.com.br/monsta/download/MonstaProbe.exe (64bits)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe) |
2. Logado com um usuário administrador, execute o instalador "monstaprobe.exe" (consulte [Instalação pela linha de comando](#instalação-pela-linha-de-comando) para instalação em lote);
3. Configure os parâmetros de porta e senha que serão solicitados durante a instalação.  
      
    

:::note
**port**: É a porta que será utilizada pela sonda para o Monsta conectar. O padrão é **7744** (TCP).  
**password**: É a senha de autenticação para a sonda no computador instalado. O padrão é `monsta@dm`.
:::



## Configuração no Monsta

Dentro do Monsta, ao criar um dispositivo, apenas configure-o para utilizar os templates da Microsoft.

![image-1741105397485.png](../../../../../assets/images/p68_image-1741105397485.png)

E preencha o campo "Usuário WMI" com qualquer informação (ele será descartado futuramente) e o campo "Senha WMI" com a senha informada na instalação da sonda.

![image-1741105450183.png](../../../../../assets/images/p68_image-1741105450183.png)

Após criar o dispositivo você já pode utilizar os monitores disponíveis do template.

## Instalação pela linha de comando

O instalador MonstaProbe.exe aceita opções na linha de comando. Você pode utilizá-las para automatizar a instalação em uma rede através de uma GPO, sem necessidade de interação com a interface gráfica.

| Opção &nbsp; &nbsp; &nbsp; &nbsp; | Descrição |
| --- | --- |
| `--agree` | Aceita o termo de uso da sonda coletora. |
| `--port` | Informa a porta a ser utilizada pela sonda coletora. Se não for informada, o padrão será 7744 (TCP). |
| `--passwd` | Atribui a senha a ser utilizada pela sonda coletora. A senha padrão será *monsta@dm* caso não seja informada. |





:::tip[Exemplo de uso]
```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```
:::



- - - - - -
