---
title: "Para que serve a Sonda do Monsta?"
---

A "Sonda do Monsta" refere-se a uma ferramenta de monitoramento desenvolvida pela Monsta Tecnologia para sistemas operacionais Windows. Ela é passiva, ou seja, aguarda por solicitações vindas do Monsta em uma porta específica e retorna as informações pela mesma conexão.

Em resumo, a Sonda do Monsta serve para:

- **Monitorar o desempenho do sistema Windows em tempo real**: Acompanha o uso de CPU, memória RAM, disco rígido e rede, permitindo identificar gargalos e otimizar recursos.
- **Visualizar dados importantes**: Integra as métricas coletadas com a plataforma Monsta para criar dashboards personalizados e detalhados.
- **Diagnosticar problemas remotamente**: Fornece informações valiosas para solucionar incidentes de forma rápida e eficiente, mesmo sem acesso físico à máquina.

Em termos técnicos, a sonda coleta métricas cruciais através das bibliotecas de API fornecida pela Microsoft para WMI (Windows Management Instrumentation).

A instalação da sonda pode ser feita através de um instalador gráfico (`MonstaProbe.exe`) ou via linha de comando para automatizar a instalação em rede.

Para instalar nossa Sonda, utilize o nosso tutorial [Sonda: Monitoramento Windows](/pt-br/start/instalacao/sonda-windows).
