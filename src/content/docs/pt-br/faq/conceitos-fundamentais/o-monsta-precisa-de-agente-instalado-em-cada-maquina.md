---
title: "O Monsta Precisa de Agente Instalado em Cada Equipamento?"
---

Para dispositivos de rede como roteadores, *switches*, *firewalls*, impressoras e outros equipamentos que suportam o protocolo [SNMP](/pt-br/tech/protocolos-coleta/snmp), o Monsta pode coletar informações valiosas diretamente através deste padrão da indústria. Isso permite monitorar tráfego de rede, utilização de recursos, níveis de tinta (em impressoras) e outras métricas específicas do dispositivo sem a necessidade de instalação de software adicional no equipamento.

Já para o Sistema Operacional Windows, para obter informações detalhadas sobre o desempenho e o status de servidores e estações de trabalho, é **necessário instalar uma [Sonda](/pt-br/start/instalacao/sonda-windows)** fornecida pelo Monsta. A Sonda é um pequeno software que reside no sistema Windows e funciona como um extrator, coletando dados internos, como utilização de CPU e memória, espaço livre em disco, status de serviços e outros contadores de performance específicos do Windows através do **[WMI](/pt-br/tech/protocolos-coleta/wmi) (*Windows Management Instrumentation*)**. A instalação da Sonda garante um monitoramento profundo e preciso do sistema operacional.

Ou seja, não é necessário instalar agentes nos equipamentos, exceto para monitorar Windows via WMI, que se faz necessário a instalação da Sonda do Monsta. Entretanto, o Monsta possui um [Agente](/pt-br/start/instalacao/agente-instalacao-zero-conf) que pode ser instalado para monitoramento, porém o intuito dele é fornecer o acesso de monitoramento à redes remotas. [Apenas um Agente](/pt-br/faq/conceitos-fundamentais/posso-monitorar-uma-rede-remota-instalando-o-agente-monsta-em-apenas-um-servidor) do Monsta instalado permite monitorar toda a rede remota.
