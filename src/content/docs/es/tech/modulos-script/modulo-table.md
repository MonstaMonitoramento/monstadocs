---
title: "Módulo table"
---

El módulo **table** extiende las funcionalidades estándar de manipulación de tablas de Lua, proporcionando funciones adicionales útiles para el procesamiento de datos. Este módulo complementa las funciones nativas de la tabla `table` de Lua, añadiendo operaciones comunes que no están disponibles en la biblioteca estándar.

**Características principales**:

- Extensión de la tabla `table` nativa de Lua

- Funciones optimizadas para el rendimiento

## Funciones Disponibles

### 1. `table.contains(tabela, valor)`

Verifica si un valor específico está presente en una tabla Lua.

#### Parâmetros:

- **tabela** (tabela): La tabla a verificar (puede ser array o tabla asociativa)

- **valor** (qualquer tipo Lua): El valor a buscar en la tabla

#### Retorno:

- **boolean**: `true` si el valor se encuentra en la tabla, `false` en caso contrario

#### Comportamento:

1. Recorre todos los pares clave-valor de la tabla usando `pairs()`

2. Compara cada valor con el valor buscado usando igualdad estricta (`==`)

3. Devuelve `true` en la primera ocurrencia encontrada

4. Devuelve `false` si recorre toda la tabla sin encontrar el valor

5. Funciona con tablas indexadas numéricamente (arrays) y tablas asociativas

#### Ejemplo de Uso:

```lua
-- Verificar si un valor existe en un array
local frutas = {"maçã", "banana", "laranja", "uva"}
local tem_banana = table.contains(frutas, "banana")
print("Tem banana?", tem_banana)  -- true

local tem_morango = table.contains(frutas, "morango")
print("Tem morango?", tem_morango)  -- false

-- Verificar em tabela associativa
local configuracoes = {
    timeout = 30,
    retries = 3,
    debug = false,
    hostname = "servidor.local"
}

local tem_timeout = table.contains(configuracoes, 30)
print("Tem valor 30?", tem_timeout)  -- true

local tem_true = table.contains(configuracoes, true)
print("Tem valor true?", tem_true)  -- false

-- Verificar tipos complexos
local usuarios = {
    {id = 1, nome = "Alice", ativo = true},
    {id = 2, nome = "Bob", ativo = false},
    {id = 3, nome = "Carol", ativo = true}
}

-- Para tipos complexos, precisa ser a mesma referência
local usuario_bob = usuarios[2]
local encontrou_bob = table.contains(usuarios, usuario_bob)
print("Encontrou Bob?", encontrou_bob)  -- true

-- Esta busca retornará false porque é um novo objeto
local encontrou_novo_bob = table.contains(usuarios, {id = 2, nome = "Bob", ativo = false})
print("Encontrou novo Bob?", encontrou_novo_bob)  -- false
```

### 2. `table.slice(tabela, primeiro, último)`

Extrae una porción (subarray) de una tabla indexada numéricamente (array).

#### Parâmetros:

- **tabela** (tabela): El array Lua del que extraer la porción

- **primeiro** (número, opcional): Índice inicial de la porción (por defecto: 1)

- **último** (número, opcional): Índice final de la porción (por defecto: longitud de la tabla)

#### Retorno:

- **tabela**: Nuevo array que contiene los elementos de la porción especificada

#### Comportamento:

1. Crea una nueva tabla que contiene los elementos desde el índice `primeiro` hasta `último` (inclusive)

2. Si `primeiro` se omite o es `nil`, empieza desde el primer elemento (índice 1)

3. Si `último` se omite o es `nil`, llega hasta el último elemento de la tabla

4. Si `primeiro` es mayor que `último`, la función aún itera pero los valores serán `nil` para índices inexistentes

5. No realiza verificación de límites: índices fuera del rango de la tabla resultarán en valores `nil`

6. Preserva el orden original de los elementos

#### Ejemplo de Uso:

```lua
-- Extrair parte de um array
local numeros = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

-- Fatia do índice 3 ao 7
local fatia1 = table.slice(numeros, 3, 7)
-- fatia1 = {30, 40, 50, 60, 70}

-- Fatia do início até o índice 5
local fatia2 = table.slice(numeros, nil, 5)
-- fatia2 = {10, 20, 30, 40, 50}

-- Fatia do índice 8 até o final
local fatia3 = table.slice(numeros, 8)
-- fatia3 = {80, 90, 100}

-- Fatia com índices fora dos limites
local fatia4 = table.slice(numeros, -2, 15)
-- fatia4 = {nil, nil, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, nil, nil, nil, nil, nil} (não trata limites)

-- Fatia com primeiro > último
local fatia5 = table.slice(numeros, 5, 3)
-- fatia5 = {50, 40, 30} (itera em ordem decrescente)

-- Processamento de dados em lotes
local function processar_em_lotes(dados, tamanho_lote)
    local lotes = {}
    local total = #dados

    for i = 1, total, tamanho_lote do
        local fim = math.min(i + tamanho_lote - 1, total)
        local lote = table.slice(dados, i, fim)
        table.insert(lotes, lote)
    end

    return lotes
end

local dados_grandes = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
local lotes = processar_em_lotes(dados_grandes, 5)
-- lotes = {{1,2,3,4,5}, {6,7,8,9,10}, {11,12,13,14,15}}
```