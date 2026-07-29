---
title: "Sonda: Instalação"
description: Aprenda como instalar a Sonda do Monsta no Windows para realizar
  monitoramentos remotos e expandir o alcance da plataforma em sua
  infraestrutura.
sidebar:
  order: 5
---
A **Sonda Monsta** é um software de coleta local projetado para ser instalado diretamente em servidores e dispositivos **Windows** (em breve para **Linux** e **Raspberry PI**). Sua função principal é coletar métricas de performance, integridade e disponibilidade do sistema hospedeiro, funcionando como uma extensão nativa de coleta para a plataforma Monsta.

## Características e Capacidades Técnicas

### 1. Arquitetura Passiva (Sob Demanda)

A sonda opera estritamente sob um modelo **passivo de requisição e resposta**. Ela não inicia comunicações com a rede de forma autônoma; o tráfego de dados ocorre apenas quando o Monsta entra em contato para realizar o *polling* (solicitação de coleta).

### 2. Integração com a API WMI (Windows)

Em ambientes Microsoft, a sonda utiliza de forma nativa a API WMI (*Windows Management Instrumentation*), permitindo extrair contadores de desempenho detalhados de servidores e estações de trabalho sem a necessidade de configurações complexas de gerenciamento remoto na rede.

### 3. Execução de Comandos e Scripts PowerShell

A sonda atua como um braço de automação diretamente no sistema operacional do host.

- **Comandos Locais**: Pode executar comandos diretamente no sistema operacional hospedeiro.
- **Scripts PowerShell**: Suporta o acionamento de scripts customizados, permitindo monitorar aplicações específicas ou criar rotinas de validação sob medida.

### 4. Diagnóstico de Saúde de Discos Físicos

O software possui a capacidade de ler indicadores de hardware e o status de integridade dos discos rígidos e SSDs instalados no dispositivo. Isso possibilita a identificação precoce de falhas físicas (*bad blocks*) e degradação de armazenamento.

### 5. Comunicação Criptografada

Toda a troca de informações entre o servidor central do Monsta e a Sonda instalada no dispositivo é **100% criptografada**, garantindo a segurança das métricas trafegadas e impedindo a interceptação de dados sensíveis da infraestrutura.

## Instalação da Sonda (Windows)

1. Baixe o programa da sonda no sistema operacional Windows que deseja monitorar;


|  | Download |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ![Download da Sonda](/src/assets/images/p139_image-1660325708746.png) | [https://www.monsta.com.br/monsta/download/MonstaProbe.msi](https://www.monsta.com.br/monsta/download/MonstaProbe.msi) |


1. Logado com um usuário administrador, execute o instalador "monstaprobe.msi";
2. Configure os parâmetros de porta e senha que serão solicitados durante a instalação.

### Instalação pela linha de comando

O instalador MonstaProbe.exe aceita opções na linha de comando. Você pode utilizá-las para automatizar a instalação em uma rede através de uma GPO, sem necessidade de interação com a interface gráfica.


| Opção &nbsp; &nbsp; &nbsp; &nbsp; | Descrição |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `AGREE=Y` | Aceita o termo de uso da sonda coletora. |
| `PORT=<num>` | Informa a porta a ser utilizada pela sonda coletora. Se não for informada, o padrão será 7743 (TCP). |
| `PASSWD=<password>` | Atribui a senha a ser utilizada pela sonda coletora. |
| `REMOTE_EXEC=1` | Habilita a execução de comandos e scripts em Powershell. Utilize 1 para habilitar ou 0 para desabilitar. |


**Exemplo de uso**:

```powershell
msiexec /i MonstaProbe.msi /qn AGREE=Y PORT=7743 PASSWD=MinhaSenha REMOTE_EXEC=1
```

### Comandos para alterar a configuração

Os parâmetros da sonda podem ser ajustados via linha de comando.


| Opção &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Descrição |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `--cfg` | Indica que a configuração será alterada. |
| `--port` | Redefine a porta que a sonda deverá escutar. |
| `--passwd` | Redefine a senha. |
| `--remote-exec 1` | Define se a execução de comandos e scripts do PowerShell está habilitada. Utilize **1** para habilitar e **0** para desabilitar. |


**Exemplo de uso**:

```powershell
"C:\Program Files (x86)\MonstaProbe\monsta_probe.exe" --cfg --port 7744 --passwd NovaSenha --remote-exec 1
```

### Execução Remota de Scripts: Segurança e Permissões

A execução de comandos e scripts em PowerShell através da Sonda do Monsta é realizada sob o contexto exclusivo do usuário local **monsta-probe**. Este usuário é criado automaticamente durante o processo de instalação e opera estritamente com permissões de usuário comum, garantindo que todos os serviços, tarefas e scripts disparados pela plataforma rodem isoladamente, sem privilégios de administrador ou acesso a arquivos sensíveis do sistema operacional.

### Configuração no Monsta

Dentro do Monsta, ao criar um dispositivo, apenas configure-o para utilizar os templates da Microsoft.

![image-1741105397485.png](/src/assets/images/p68_image-1741105397485.png)

E preencha o campo "Usuário WMI" com qualquer informação (ele será descartado futuramente) e o campo "Senha WMI" com a senha informada na instalação da sonda.

![image-1741105450183.png](/src/assets/images/p68_image-1741105450183.png)

Após criar o dispositivo você já pode utilizar os monitores disponíveis do template.