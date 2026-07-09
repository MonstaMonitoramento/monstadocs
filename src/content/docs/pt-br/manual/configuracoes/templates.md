---
title: "Templates"
sidebar:
  order: 2
---

Template é o conjunto de recursos que podem ser monitorados em um dispositivo. Cada fabricante disponibiliza seus próprios recursos por equipamento.

## Templates

![image-1647448202544.png](../../../../../assets/images/p61_image-1647448202544.png)

---

![image-1647448799678.png](../../../../../assets/images/p61_image-1647448799678.png)
**Importar Templates**: Permite selecionar um arquivo de template para importar. 

---

![image-1647448005833.png](../../../../../assets/images/p61_image-1647448005833.png)
**Filtro de Pesquisa**: Quando utilizado, exibe apenas os templates que contém esse texto em seu nome.

---

![image-1647448121838.png](../../../../../assets/images/p61_image-1647448121838.png)
**Novo Template**: Cria um novo template. Consulte [Criar/Editar um Template](#criareditar-um-template) para maiores informações.

---

![image-1647448227188.png](../../../../../assets/images/p61_image-1647448227188.png)
**Lista de Templates**: Apresenta uma lista com todos os templates disponíveis no sistema.

---

![image-1739983220633.png](../../../../../assets/images/p61_image-1739983220633.png)
**Caixa de Template**: Apresentação visual do template. Ao clicar sobre ele o usuário é redirecionado para a tela de seus monitores. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1647448422172.png](../../../../../assets/images/p61_image-1647448422172.png) | **Remover**: Remove o template em evidência. |
| ![image-1647448460969.png](../../../../../assets/images/p61_image-1647448460969.png) | **Editar**: Edita as propriedades do template, como nome, descrição e ícone. |

### Criar/Editar um Template

![image-1647450145680.png](../../../../../assets/images/p61_image-1647450145680.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1647450183069.png](../../../../../assets/images/p61_image-1647450183069.png) | **Ícone do Template**: Permite selecionar um ícone para o template de uma biblioteca já existente ou a partir de uma nova imagem. |
| **Nome** | Nome dado ao template. |
| **Descrição** | Uma breve descrição sobre o template. |

## Monitores

Monitores são componentes do sistema que checam um determinado recurso em um dispositivo e retornam sua situação atual. São eles que geram informações e alertam sobre possíveis anomalias.

![image-1739984216883.png](../../../../../assets/images/p61_image-1739984216883.png)

---

---

![image-1739984247217.png](../../../../../assets/images/p61_image-1739984247217.png)
**Nome do Template**: Informa o nome do template em evidência.

---

![image-1739984391202.png](../../../../../assets/images/p61_image-1739984391202.png)
**Exportar**: Exporta os monitores selecionados para um arquivo.

---

![image-1739984511244.png](../../../../../assets/images/p61_image-1739984511244.png)
**Editar Template**: Edita as propriedades do template, como nome, descrição e ícone.

---

![image-1647449193273.png](../../../../../assets/images/p61_image-1647449193273.png)
**Filtro de Pesquisa**: Quando utilizado, exibe apenas os monitores que contém esse texto em seu nome.

---

![image-1647449307274.png](../../../../../assets/images/p61_image-1647449307274.png)
**Novo Monitor**: Cria um novo monitor para o template em evidência. Para maiores informações, consulte xxxxxxx.

---

![image-1647449372287.png](../../../../../assets/images/p61_image-1647449372287.png)
**Lista de Monitores**: Apresenta uma lista com todos os monitores disponíveis para o template em evidência. Clicar em um monitor permite editá-lo. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1647449752980.png](../../../../../assets/images/p61_image-1647449752980.png) | **Clonar**: Clona o monitor para um template selecionado. |
| ![image-1647449785056.png](../../../../../assets/images/p61_image-1647449785056.png) | **Remover**: Remove o monitor selecionado. | 


### Criar/Editar um Monitor

#### Monitor

Nesta tela são configuradas informações básicas sobre o monitor.

![image-1769000706570.png](../../../../../assets/images/p61_image-1769000706570.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1739984579878.png](../../../../../assets/images/p61_image-1739984579878.png) | **Ícone**: Permite selecionar um ícone para o template de uma biblioteca já existente ou a partir de uma nova imagem e também serve como prévia de como o monitor será exibido na tela. |
| **Nome Curto** | Informação sobre o monitor que é apresentada no ícone da tela de dispositivos. |
| **Nome** | Informação sobre o monitor que é apresentada na tela dos templates. |
| **Descrição** | É um breve informativo sobre o monitor. Esse texto será exibido ao passar ou mouse sobre os monitores de um dispositivo. |
| **Intervalo de Verificação** | Seleciona o tempo de checagem do monitor. <aside class="starlight-aside starlight-aside--caution">Caso esse valor seja maior que 59 segundos, quando uma métrica sai do estado normal o intervalo de verificação passará a ser, automaticamente, a cada 1 minuto.</aside> |
| **Número de Tentativas** | Número de checagens que serão feitas após o valor do monitor ultrapassar seu limite de normalidade para, posteriormente, trocar seu estado. |
| ![image-1769000749924.png](../../../../../assets/images/p61_image-1769000749924.png) | Ao editar um monitor e clicar neste botão, o sistema permite replicar as alterações para outros dispositivos simultaneamente. Após clicar, selecione na lista os dispositivos que devem receber a nova configuração. |



#### Instâncias

Neste tela é informado o método de listagem das instâncias de um recurso, como por exemplo, a lista de interfaces de rede de um equipamento.

![image-1739984753223.png](../../../../../assets/images/p61_image-1739984753223.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1647535774368.png](../../../../../assets/images/p61_image-1647535774368.png) | **Ativar Instâncias**: Ativa a seleção de instâncias para o monitor. |
| ![image-1647535820722.png](../../../../../assets/images/p61_image-1647535820722.png) | Método de pesquisa utilizado para buscar as instâncias. |
| **Fixar OID** | Quando desabilitado, o Monsta verifica se o nome da instância continua na mesma OID. As seguintes situações podem ocorrer:<br />- **OID igual**: O Monsta coleta os valores na mesma posição;<br />- **OID diferente**: O Monsta descobre a nova OID e coletará os valores na nova posição;<br />Quando habilitada, o Monsta coletará as informações sempre na mesma posição, independente se a instância mudou de OID. |
| **OIDDesc e Nome** | Esta opção permite que o monitor identifique automaticamente múltiplos componentes de um mesmo dispositivo (como diferentes interfaces de rede, discos ou partições). O sistema utiliza scripts do **Monsta Studio** para listar esses itens. Nos parâmetros, você define as propriedades desejadas (como OIDs ou filtros) para extrair exatamente os dados que serão exibidos na listagem de seleção. |



### Métricas

Nesta tela são configurados a forma de coleta dos recursos do dispositivo.

![image-1769002820448.png](../../../../../assets/images/p61_image-1769002820448.png)

---

![image-1647537210606.png](../../../../../assets/images/p61_image-1647537210606.png)
**Métrica**: Informa o nome da métrica e sua posição no gráfico. A métrica superior da lista tem seu gráfico sobreposto pela métrica inferior. 

| Ícone | Descrição |
| :---: | :--- |
![image-1647537418530.png](../../../../../assets/images/p61_image-1647537418530.png) | **Ordenação**: Alterna a posição da métrica para ser impressa no gráfico. | 
![image-1647537403522.png](../../../../../assets/images/p61_image-1647537403522.png) | **Remover**: Remove a métrica selecionada. | 

---

![image-1647537518634.png](../../../../../assets/images/p61_image-1647537518634.png)
**Adicionar**: Adiciona uma nova métrica.

---

![image-1647537560886.png](../../../../../assets/images/p61_image-1647537560886.png)
**Fonte de dados para o valor**: Configura a forma de coleta de dados da métrica. Esse é o valor que será impresso no gráfico.

---

![image-1647538051533.png](../../../../../assets/images/p61_image-1647538051533.png)
**Fonte de dados para o valor máximo**: Método para obtenção do valor máximo da métrica. Esse valor será utilizado para o cálculo do percentual que será utilizado nos limites de alerta.

---

![image-1647538111673.png](../../../../../assets/images/p61_image-1647538111673.png)
**Cor**: Cor da métrica que será apresentado ao acessar seu gráfico.

---

![image-1647538237011.png](../../../../../assets/images/p61_image-1647538237011.png)
**Nome**: Nome da métrica que será apresentado ao acessar seu gráfico.

---

![image-1739986248546.png](../../../../../assets/images/p61_image-1739986248546.png)
**Unidade**: Unidade de medida da métrica.

---

![image-1647538419774.png](../../../../../assets/images/p61_image-1647538419774.png)
**Preencher**: Permite selecionar se a métrica deverá ter seu gráfico preenchido. Quando não selecionada esta opção o gráfico desta métrica irá apenas apresentar uma linha para as leituras.

---

![image-1647538571119.png](../../../../../assets/images/p61_image-1647538571119.png)
**Tipo de valor**: Informa o tipo de valor que a métrica retorna. A escolha dessa propriedade define o tipo de gráfico que será apresentado.

---

![image-1739986284648.png](../../../../../assets/images/p61_image-1739986284648.png)
**Desativar limites**: Desativa os limites para a métrica. Ao ativar essa opção o estado da métrica sempre será "Normal" e a mesma nunca será alarmada.

---

![image-1647539136617.png](../../../../../assets/images/p61_image-1647539136617.png)
**Percentual de limites de alerta**: Em monitores que possuem um valor máximo definido, a barra percentual é exibida. Ela permite visualizar e definir rapidamente os limites definidos para os estados da métrica.

:::note
Disponível quando há um valor máximo configurado.
:::

| Opção | Descrição |
| :---: | :--- |
| ![image-1647539259537.png](../../../../../assets/images/p61_image-1647539259537.png) | **Inverter**: Inverte o percentual de alerta. Por padrão um valor menor será considerado melhor. |
| ![image-1647539419645.png](../../../../../assets/images/p61_image-1647539419645.png) | **Barra de percentuais**:  Permite configurar visualmente os limites de alerta. Arraste os seletores para determinar os percentuais de uso que acionam os estados de "Aviso" e "Crítico". |
| ![image-1647539324004.png](../../../../../assets/images/p61_image-1647539324004.png) | **Valores dos percentuais**: Abaixo da barra de percentuais, o sistema exibe o valor numérico exato correspondente à posição dos marcadores. |

---

![image-1647539661996.png](../../../../../assets/images/p61_image-1647539661996.png)
**Valores dos limites de alerta**: Em monitores sem um valor máximo pré-estabelecido, o usuário tem a liberdade de informar manualmente os valores numéricos para os estados de **Aviso** e **Crítico**.

:::note
Disponível quando não há valor máximo configurado.
:::

| Opção | Descrição |
| :---: | :--- |
| ![image-1647539740732.png](../../../../../assets/images/p61_image-1647539740732.png) | **Valor de Aviso**: Define a condição para a métrica entrar em estado de atenção. |
| ![image-1647539844543.png](../../../../../assets/images/p61_image-1647539844543.png) | **Valor de Crítico**: Define a condição para a métrica entrar em estado crítico. |

---


![image-1739986395801.png](../../../../../assets/images/p61_image-1739986395801.png)
**Fonte de Dados**: Permite selecionar uma fonte de coleta existente e, se necessário, preencher os valores solicitados por ela.

| Opção | Descrição |
| :---: | :--- |
| ![image-1647540152635.png](../../../../../assets/images/p61_image-1647540152635.png) | **Botão Testar**: Testa a fonte contra um dispositivo selecionado. |
| ![image-1647540263038.png](../../../../../assets/images/p61_image-1647540263038.png) | **Botão Remover**: Remove a fonte de dados do valor em evidência. |
| **Coletor** | **Campo Coletor**: Seleciona o método que será utilizado para a coleta de dados do monitor. |
| **Parâmetros** | **Campo Parâmetros**: Permite informar os dados para os parâmetros selecionados. Parâmetros com um "\*" ao lado indicam que seu preenchimento ao adicionar um monitor será obrigatório. |

---

![image-1647539918188.png](../../../../../assets/images/p61_image-1647539918188.png)
**Scripts Customizados**: Permite selecionar a fonte de dados da coleta. Nesta tela é possível utilizar scripts na linguagem LUA para as métricas.

| Opção | Descrição |
| :---: | :--- |
| ![image-1647540152635.png](../../../../../assets/images/p61_image-1647540152635.png) | **Botão Testar**: Testa o script contra um dispositivo selecionado. |
| ![image-1647540263038.png](../../../../../assets/images/p61_image-1647540263038.png) | **Botão Remover**: Remove a fonte de dados do valor em evidência. |
| **Abrir no Editor** | **Botão Abrir no editor**: Abre um editor avançado de desenvolvimento para o script. |

---

### Parâmetros

Nesta tela é possível criar parâmetros com valores pré-definidos para serem utilizados pelas fontes de dados das métricas. Essa opção é útil quando um monitor possui várias métricas que utilizem as mesmas informações, como um usuário e senha para autenticação, por exemplo.

![image-1739986497220.png](../../../../../assets/images/p61_image-1739986497220.png)

| Opção | Descrição |
| :---: | :--- |
| ![image-1739986525205.png](../../../../../assets/images/p61_image-1739986525205.png) | **Nome**: Define um nome para o parâmetro. |
| ![image-1739986588973.png](../../../../../assets/images/p61_image-1739986588973.png) | **Tipo**: É o tipo de informação que o parâmetro deve receber. O tipo "Opção" trará uma lista vinda da aba "Instâncias". |
| ![image-1739986692649.png](../../../../../assets/images/p61_image-1739986692649.png) | **Valor padrão**: Define um valor padrão para o parâmetro ao criar o monitor. Essa opção não está disponível para o tipo "Opção". |
| ![image-1739986788958.png](../../../../../assets/images/p61_image-1739986788958.png) | **Descrição do campo**: É o texto que será informado ao usuário durante a adição de monitores aos dispositivos. |
| ![image-1647546204637.png](../../../../../assets/images/p61_image-1647546204637.png) | **Opção de Campo Obrigatório**: Exige que o parâmetro tenha algum valor. Campos em branco não são permitidos. |
| ![image-1647546282966.png](../../../../../assets/images/p61_image-1647546282966.png) | **Opção de Campo que se repete**: Permite ao usuário inserir o mesmo campo várias vezes com valores diferentes. |
| ![image-1647546340415.png](../../../../../assets/images/p61_image-1647546340415.png) | **Posição**: Alterna a posição do parâmetro na listagem. |
| ![image-1647546392820.png](../../../../../assets/images/p61_image-1647546392820.png) | **Botão Remover**: Remove o parâmetro selecionado. |


:::caution[Importante]
Ao criar ou customizar um monitor, quando o tipo for uma opção e o método selecionado for "Scripts", o retorno deverá ser uma tabela com o seguinte formato:

`local ret = { display = "Texto", instanceId = "valor" }`

- Certifique-se de que o `instanceId` seja único (sem repetições).
- Nomeie a variável como `exec.instance`. Isso possibilita o reaproveitamento em **monitores automáticos** e a **clonagem de métricas**.
:::

:::danger[Atenção]
O uso obrigatório do nome de variável `exec.instance` é um pré-requisito para a automação. Caso outro nome seja utilizado, os **monitores automáticos não funcionarão corretamente** e a **clonagem de métricas ficará indisponível**.
:::

Exemplo:

```lua
local opts = {
    host = "192.168.1.1",
    username = "user",
    password = "password",
    command = "ls /backup/*.sql"
}
local ret = {}

local list = string.split(ssh.exec(opts),"\n")

for i, arq in pairs(list)
do
  local name = string.split(arq,"//")[2]
  table.insert(ret,{display=name,instanceId=i})
end

return ret
```