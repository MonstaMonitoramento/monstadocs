---
title: "Qual é a diferença entre a Sonda e o Agente do Monsta?"
---

Este artigo tem como objetivo explicar resumidamente a diferença entre a [Sonda](/pt-br/start/instalacao/sonda-windows) e o [Agente](/pt-br/start/instalacao/agente-instalacao-zero-conf) do Monsta.

## Diferenças

A principal diferença entre a Sonda e o Agente é o propósito de cada um:

- A Sonda do Monsta surgiu com a necessidade de monitorar equipamentos Windows através de WMI. Uma vez instalada no computador, o Monsta consegue obter informações do WMI do Windows através da Sonda.
- O Agente do Monsta surgiu com a necessidade de monitorar equipamentos em redes remotas, inacessíveis ao Monsta. Com o Agente instalado em um equipamento da rede remota, o Monsta consegue se comunicar com ele para obter informações dos equipamentos da rede sem a necessidade de redirecionamento de porta ou VPN.

## Quadro comparativo: Agente vs. Sonda

| Característica | **Agente** | **Sonda** |
| --- | --- | --- |
| **Comportamento** | **Ativo** — inicia a conexão de saída para o servidor Monsta | **Passivo** — aguarda requisições do servidor Monsta |
| **Sistemas suportados** | Windows, Linux e Raspberry PI | Somente Windows |
| **Uso de VPN / Port Forwarding** | Não precisa | Necessário (o Monsta precisa alcançar a sonda) |
| **Protocolo de comunicação** | QUIC (criptografado, ponta a ponta) | WMI (API da Microsoft) |
| **Ambientes com NAT / IP dinâmico** | Suportado nativamente | Pode ser limitado |
| **Cache de dados offline** | Sim — armazena métricas localmente se perder conexão | Não |
| **Ideal para** | Redes remotas, filiais, ambientes distribuídos sem VPN | Monitoramento local de servidores/estações Windows |
| **Custo** | Pago | Gratuito |



## Resumo

A Sonda é uma ferramenta mais simples, focada em coletar métricas de máquinas Windows (CPU, RAM, disco, rede) e responde quando o servidor Monsta a consulta. O Agente é uma solução mais robusta e multiplataforma, ideal para expandir o monitoramento para redes remotas — ele próprio inicia a comunicação com o servidor, dispensando VPN, redirecionamento de portas ou IP fixo.

![image-1773943312944.png](../../../../../assets/images/p174_image-1773943312944.png)

## Mais informações

Outros artigos relacionados aos Agentes e Sonda:

- 📄[Agentes](/pt-br/manual/configuracoes/agentes)
- 📄[Agente: Instalação Zero Conf](/pt-br/start/instalacao/agente-instalacao-zero-conf)
- 📄[Posso monitorar uma rede remota instalando o Agente Monsta em apenas um servidor?](/pt-br/faq/conceitos-fundamentais/posso-monitorar-uma-rede-remota-instalando-o-agente-monsta-em-apenas-um-servidor)
- 📄[A Arquitetura de Comunicação do Agente](/pt-br/tech/arquitetura-comunicacao/a-arquitetura-de-comunicacao-do-agente)
- 📄[O Monsta precisa de agente instalado em cada máquina?](/pt-br/faq/conceitos-fundamentais/o-monsta-precisa-de-agente-instalado-em-cada-maquina)
- 📄[Protoloco QUIC - O Futuro das Comunicações na Internet](/pt-br/tech/arquitetura-comunicacao/protocolo-quic)
- 📄[Para que serve a Sonda do Monsta?](/pt-br/faq/conceitos-fundamentais/para-que-serve-a-sonda-do-monsta)
- 📄[Sonda: Monitoramento Windows](/pt-br/start/instalacao/sonda-windows)
- 📄[WMI (Windows Management Instrumentation)](/pt-br/tech/protocolos-coleta/wmi)
