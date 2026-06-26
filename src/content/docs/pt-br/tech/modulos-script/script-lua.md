---
title: "Scripting com LUA"
sidebar:
  order: 1
---

O Monsta permite que você crie lógicas personalizadas de coleta de dados, processamento de métricas e regras complexas de alertas utilizando a linguagem de programação **Lua**. 

Se os templates padrão ou as expressões nativas não forem suficientes para a sua necessidade (como parsing de strings complexas, cálculos matemáticos avançados ou loops), o motor de scripting em Lua oferece total flexibilidade para estender a plataforma.

---

## Por que Lua?

Lua é uma linguagem de script brasileira, amplamente utilizada na indústria de tecnologia (especialmente em jogos e sistemas embarcados) por três motivos principais:

* **Extrema Velocidade**: É uma das linguagens de script mais rápidas do mundo, garantindo que seus scripts rodem em milissegundos sem sobrecarregar o servidor do Monsta.
* **Leveza**: O interpretador ocupa pouquíssimo espaço em memória, permitindo execuções simultâneas em larga escala.
* **Sintaxe Simples**: É muito fácil de ler e aprender, mesmo para quem tem pouca experiência com programação.

---

## Guia Rápido de Sintaxe Lua

Para ajudar você a começar a criar seus primeiros scripts no Monsta, aqui estão os conceitos fundamentais da linguagem:

### Variáveis e Tipos de Dados
Em Lua, você não precisa definir o tipo da variável antes (tipagem dinâmica). Use sempre a palavra-chave `local` para garantir que a variável exista apenas dentro daquele script (evitando conflitos de memória).

```lua
local nome_dispositivo = "Servidor Core" -- String
local latencia = 45                     -- Number
local ativo = true                      -- Boolean
```

### Estruturas Condicionais (`if` / `else`)
A sintaxe usa as palavras-chave then, elseif e fecha o bloco obrigatoriamente com um end.

```lua
if latencia > 100 then
    print("Alerta: Latência Alta!")
elseif latencia > 50 then
    print("Aviso: Latência Moderada.")
else
    print("Status: OK.")
end
```

### Tabelas (Dicionários e Arrays)
Tabelas são a única estrutura de dados complexa em Lua. Elas servem tanto como listas indexadas quanto como objetos com chave e valor.

```lua
-- Exemplo de Array/Lista
local sensores = {"Ping", "CPU", "Memória"}

-- Exemplo de Dicionário (Chave/Valor)
local dados_coleta = {
    ip = "192.168.1.50",
    status = "Online",
    portas_abertas = 4
}
```
:::caution[Atenção com Índices!]
Ao contrário da maioria das linguagens de programação (como **JavaScript** ou **Python**) onde as listas começam no índice `0`, em Lua as tabelas começam no índice `1`.
Portanto, `sensores[1]` retornará "Ping".
:::

## Como o Monsta interage com o Script?
Geralmente, o Monsta injeta variáveis globais ou tabelas pré-definidas para dentro do seu script (contendo os dados coletados do dispositivo) e espera que o seu script retorne um valor específico (como um número, texto ou booleano) usando o comando return.

```lua
-- Exemplo de uma consulta de SNMP
local load_linux = snmp.get("1.3.6.1.4.1.2021.10.1.3.2.0") -- Função do Monsta
return load_linux
```

## Recursos e Manuais Completos
Para se aprofundar na linguagem, consulte a [documentação oficial da linguagem Lua](https://lua.org/docs.html).

O Monsta possui funções próprias que são utilizadas nos scripts. Para conhecer os módulos internos específicos que o Monsta disponibiliza (funções de rede, manipulação de strings e conexão), verifique os próximos artigos desta área (**Módulos de Script com Lua**).