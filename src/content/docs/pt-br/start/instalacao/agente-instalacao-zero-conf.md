---
title: 'Agente: Instalação Zero Conf'
sidebar:
  order: 4
---

Esta documentação descreve o funcionamento e a arquitetura do **Agente Monsta**, uma ferramenta para estender o monitoramento da sua plataforma para redes remotas e distribuídas, garantindo performance e segurança por meio do protocolo QUIC.

## Instalação do Agente para Windows

- Baixe o programa do agente:

[![](/src/assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/agent.msi)
[https://www.monsta.com.br/monsta/download/agent.msi](https://www.monsta.com.br/monsta/download/agent.msi)

- Logado com um usuário com permissões de administrador, execute o instalador "agent.msi".
- Quando solicitado, insira a chave de licença do Monsta no qual você deseja conectar o agente.

## Instalação pela linha de comando

O instalador **agent.msi** suporta parâmetros de linha de comando para automação. Integrado ao utilitário **msiexec**, ele permite instalar via **GPO**, eliminando a necessidade de intervenção manual na interface gráfica.

Opções da linha de comando:
|Opção|Descrição|
|---|---|
| `LICENSEKEY=\[chave de licença\]` | Informa a chave de licença no qual o Agente deverá se conectar. |
| `AGREE=\[Y\]` | Confirma a aceitação dos termos de uso. |

:::tip[Exemplo de uso]

```powershell
msiexec /i agent.msi /quiet LICENSEKEY=AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH AGREE=Y
```

:::

:::note
A Chave de Licença pode ser obtida no Monsta dentro do menu "Configuração" na opção "Agentes". Ela é informada no canto superior direito.
:::

:::tip
**Firewall**:  

- Não é necessário redirecionar nenhuma porta para o servidor do Monsta;  
- Para garantir conexões diretas, libere a porta **58580/UDP** (saída) no seu firewall do servidor do Monsta para a Internet;  
- Libere o acesso do servidor do Monsta para os hosts mind.monsta.com.br e agent.monsta.com.br.
:::

## Criação do Dispositivo

Uma vez concluída a instalação, o **Agente** aparecerá automaticamente na tela de **Configuração** no item **Agentes** com a identificação do host. O dispositivo monitorado será **criado e listado instantaneamente** na tela de **Dispositivos** com o mesmo nome do host e pronto para a configuração e adição de novos monitores.

### Como Monitorar Dispositivos pela Conexão do Agente

Para cobrir toda a rede remota com um único agente, cadastre os novos dispositivos no Monsta e defina que o dispositivo está sob a **hierarquia** do host onde o Agente está instalado.

Exemplo de Hierarquia:

![image-1765385133049.png](../../../../../assets/images/p139_image-1765385133049.png)

##
