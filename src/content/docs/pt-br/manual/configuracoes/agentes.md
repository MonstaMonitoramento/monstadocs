---
title: "Agentes"
sidebar:
  order: 3
---

O Agente de Monitoramento da Monsta Tecnologia permite gerenciar infraestruturas de TI complexas e distribuídas, garantindo que o monitoramento seja eficiente, seguro e não sobrecarregue sua rede de longa distância (WAN). O Agente é multiplataforma, sua instalação é rápida e descomplicada em qualquer ambiente de TI, sendo compatível com os principais sistemas operacionais: Windows e Linux (incluindo as distribuições mais populares).

## Como o Agente Monsta Funciona?

O Agente Monsta atua como um Proxy de Monitoramento Distribuído para suas filiais e redes remotas. Monitore ativos de forma centralizada e segura, eliminando a complexidade de redirecionamento de portas, VPNs ou a exigência de IPs fixos/estáticos.

## Benefícios Arquiteturais



| **Recurso** | **Descrição** |
| --- | --- |
| **Coleta Local** | O Agente é instalado na rede remota e faz a coleta de dados de todos os dispositivos *localmente*. |
| **Comunicação Consolidada** | Ele **agrega e armazena** temporariamente as métricas antes de enviá-las ao Servidor Monsta central em um único fluxo. |
| **Segurança Otimizada** | Apenas o Agente precisa abrir comunicação com o servidor central, exigindo menos regras de firewall e reduzindo a superfície de ataque. |
| **Tolerância a Falhas** | Em caso de perda temporária da conexão WAN, o Agente continua coletando e armazenando dados (caching), garantindo que nenhuma informação seja perdida. |



## Gerenciamento de Agentes e Monitoramento Distribuído

![image-1768997185306.png](../../../../../assets/images/p63_image-1768997185306.png)

| Ícone | Descrição |
| :---: | :--- |
| ![image-1647867281671.png](../../../../../assets/images/p63_image-1647867281671.png) | **Pesquisar**: Utilize o campo de filtro para localizar agentes específicos. Ao digitar, a lista será atualizada automaticamente para exibir apenas os resultados que correspondam ao texto informado. |
| ![image-1768997246532.png](../../../../../assets/images/p63_image-1768997246532.png) | **Licenças de agentes disponíveis**: Este campo indica a quantidade de agentes disponíveis em sua assinatura. Caso precise monitorar mais dispositivos você pode acessar a área do cliente em nosso site e adicionar quantas licenças forem necessárias em seu plano. |
| ![image-1768998008744.png](../../../../../assets/images/p63_image-1768998008744.png) | **Total de agentes**: Quantidade de agentes configurados e ocupando uma vaga de licença. |
| ![image-1768999817872.png](../../../../../assets/images/p63_image-1768999817872.png) | **Ordenação**: As setas permitem reordenar a lista de agentes. Esta ordem define a prioridade de uso das licenças contratadas: agentes posicionados acima do limite de sua cota serão monitorados, enquanto os excedentes permanecerão em espera. |
| ![image-1768998685081.png](../../../../../assets/images/p63_image-1768998685081.png) | **Status**: Indica a condição atual de cada dispositivo na rede:<br /><br />• **Conectado**: O agente está ativo e comunicando-se normalmente com o servidor.<br />• **Desconectado**: O agente está offline ou houve perda de comunicação.<br />• **Limite Excedido**: O agente foi instalado, mas não está monitorando porque a cota de licenças do seu plano foi atingida.<br />• **Bloqueado**: O agente está com sua comunicação bloqueada. |
| ![image-1768998876264.png](../../../../../assets/images/p63_image-1768998876264.png) | **Dispositivo**: Exibe informações sobre o Sistema Operacional onde o agente está em execução. |
| ![image-1768999021483.png](../../../../../assets/images/p63_image-1768999021483.png) | **Conexão**: Exclusivo para agentes conectados, este campo indica a rota de comunicação.<br /><br />• **Direto**: O agente comunica-se diretamente com o servidor.<br />• **Híbrido**: O agente utiliza um servidor intermediário (Proxy) para contornar restrições de firewall ou isolamento de rede. |
| ![image-1768999216633.png](../../../../../assets/images/p63_image-1768999216633.png) | **Versão**: Indica a versão atual do agente instalada no host. Este campo é gerenciado automaticamente pelo sistema: sempre que uma nova atualização for lançada, o Monsta realizará o upgrade de forma automática, garantindo que você sempre tenha os recursos e correções mais recentes sem intervenção manual. |
| ![image-1768999398371.png](../../../../../assets/images/p63_image-1768999398371.png) | **Última atividade**: Registra o data e horário exato da última comunicação recebida do agente. É o principal indicador para verificar se o monitoramento está ocorrendo em tempo real. |
| ![image-1768999481044.png](../../../../../assets/images/p63_image-1768999481044.png) | **Bloquear agente**: Permite interromper ou retomar a comunicação de um agente específico manualmente. Quando bloqueado, o agente para de enviar dados ao servidor, mas permanece instalado e configurado, podendo ser reativado a qualquer momento com um clique. |
| ![image-1768999732028.png](../../../../../assets/images/p63_image-1768999732028.png) | **Excluir agente**: Remove permanentemente o agente da sua lista de monitoramento.<br />**Nota**: Por segurança, esta ação só é permitida para agentes que estejam com o status **Desconectado**. Caso o agente ainda esteja ativo, é necessário interromper o serviço no host antes da exclusão. |


:::caution[Atenção]
O suporte aos agentes está disponível a partir da versão **6** do Monsta.
:::