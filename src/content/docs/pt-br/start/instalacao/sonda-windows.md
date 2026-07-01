---
title: 'Sonda: Monitoramento Windows'
sidebar:
  order: 5
---

A **Sonda Monsta** é um software de coleta local projetado para ser instalado diretamente em servidores e dispositivos **Windows, Linux e Raspberry PI**. Sua função principal é coletar métricas de performance, integridade e disponibilidade do sistema hospedeiro, funcionando como uma extensão nativa de coleta para a plataforma Monsta.

## Características e Capacidades Técnicas

### 1. Arquitetura Passiva (Sob Demanda)

A sonda opera estritamente sob um modelo **passivo de requisição e resposta**. Ela não inicia comunicações com a rede de forma autônoma; o tráfego de dados ocorre apenas quando o Monsta entra em contato para realizar o _polling_ (solicitação de coleta).

### 2. Integração com a API WMI (Windows)

Em ambientes Microsoft, a sonda utiliza de forma nativa a API WMI (_Windows Management Instrumentation_), permitindo extrair contadores de desempenho detalhados de servidores e estações de trabalho sem a necessidade de configurações complexas de gerenciamento remoto na rede.

### 3. Execução de Comandos e Scripts PowerShell

A sonda atua como um braço de automação diretamente no sistema operacional do host.

- **Comandos Locais:** Pode executar comandos diretamente no sistema operacional hospedeiro.
- **Scripts PowerShell:** Suporta o acionamento de scripts customizados, permitindo monitorar aplicações específicas ou criar rotinas de validação sob medida.

### 4. Diagnóstico de Saúde de Discos Físicos

O software possui a capacidade de ler indicadores de hardware e o status de integridade dos discos rígidos e SSDs instalados no dispositivo. Isso possibilita a identificação precoce de falhas físicas (_bad blocks_) e degradação de armazenamento.

### 5. Comunicação Criptografada

Toda a troca de informações entre o servidor central do Monsta e a Sonda instalada no dispositivo é **100% criptografada**, garantindo a segurança das métricas trafegadas e impedindo a interceptação de dados sensíveis da infraestrutura.

## Instalação da Sonda

1. Baixe o programa da sonda no sistema operacional Windows que deseja monitorar;

[![](/src/assets/images/p139_image-1660325708746.png)](https://www.monsta.com.br/monsta/download/MonstaProbe.exe)

[https://www.monsta.com.br/monsta/download/MonstaProbe.exe](https://www.monsta.com.br/monsta/download/MonstaProbe.exe)

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

| Opção | Descrição |
| --- | --- |
| `--agree` | Aceita o termo de uso da sonda coletora. |
| `--port` | Informa a porta a ser utilizada pela sonda coletora. Se não for informada, o padrão será 7744 (TCP). |
| `--passwd` | Atribui a senha a ser utilizada pela sonda coletora. A senha padrão será *monsta@dm* caso não seja informada. |

:::tip[Exemplo de uso]

```powershell
MonstaProbe.exe --agree --port 1234 --passwd senha
```

:::
