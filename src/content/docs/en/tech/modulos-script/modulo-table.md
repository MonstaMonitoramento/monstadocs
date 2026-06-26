---
title: "Table Module"
---

The **table** module extends Lua's standard table manipulation functionality, providing additional useful functions for data processing. This module complements Lua's native `table` library by adding common operations that are not available in the standard library.

**Main features**:

- Extension of Lua's native `table`

- Functions optimized for performance

## Available Functions

### 1. `table.contains(tabela, valor)`

Checks whether a specific value is present in a Lua table.

#### Parameters:

- **tabela** (table): The table to be checked (can be an array or an associative table)

- **valor** (any Lua type): The value to search for in the table

#### Return:

- **boolean**: `true` if the value is found in the table, `false` otherwise

#### Behavior:

1. Iterates over all key-value pairs of the table using `pairs()`

2. Compares each value with the searched value using strict equality (`==`)

3. Returns `true` on the first occurrence found

4. Returns `false` if it traverses the entire table without finding the value

5. Works with numerically indexed tables (arrays) and associative tables

#### Usage Example:

```lua
-- Check if a value exists in an array
local frutas = {"maçã", "banana", "laranja", "uva"}
local tem_banana = table.contains(frutas, "banana")
print("Tem banana?", tem_banana)  -- true

local tem_morango = table.contains(frutas, "morango")
print("Tem morango?", tem_morango)  -- false

-- Check in associative table
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

-- Check complex types
local usuarios = {
    {id = 1, nome = "Alice", ativo = true},
    {id = 2, nome = "Bob", ativo = false},
    {id = 3, nome = "Carol", ativo = true}
}

-- For complex types, it must be the same reference
local usuario_bob = usuarios[2]
local encontrou_bob = table.contains(usuarios, usuario_bob)
print("Encontrou Bob?", encontrou_bob)  -- true

-- This search will return false because it's a new object
local encontrou_novo_bob = table.contains(usuarios, {id = 2, nome = "Bob", ativo = false})
print("Encontrou novo Bob?", encontrou_novo_bob)  -- false
```

### 2. `table.slice(tabela, primeiro, último)`

Extracts a slice (subarray) from a numerically indexed table (array).

#### Parameters:

- **tabela** (table): The Lua array from which to extract the slice

- **primeiro** (number, optional): Starting index of the slice (default: 1)

- **último** (number, optional): Ending index of the slice (default: length of the table)

#### Return:

- **table**: New array containing the elements of the specified slice

#### Behavior:

1. Creates a new table containing the elements from index `primeiro` to `último` (inclusive)

2. If `primeiro` is omitted or `nil`, starts from the first element (index 1)

3. If `último` is omitted or `nil`, goes to the last element of the table

4. If `primeiro` is greater than `último`, the function still iterates but values will be `nil` for nonexistent indices

5. Does not perform bounds checking - indices outside the table range will result in `nil` values

6. Preserves the original order of elements

#### Usage Example:

```lua
-- Extract part of an array
local numeros = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

-- Slice from index 3 to 7
local fatia1 = table.slice(numeros, 3, 7)
-- fatia1 = {30, 40, 50, 60, 70}

-- Slice from the start to index 5
local fatia2 = table.slice(numeros, nil, 5)
-- fatia2 = {10, 20, 30, 40, 50}

-- Slice from index 8 to the end
local fatia3 = table.slice(numeros, 8)
-- fatia3 = {80, 90, 100}

-- Slice with indices out of bounds
local fatia4 = table.slice(numeros, -2, 15)
-- fatia4 = {nil, nil, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, nil, nil, nil, nil, nil} (does not handle bounds)

-- Slice with first > last
local fatia5 = table.slice(numeros, 5, 3)
-- fatia5 = {50, 40, 30} (iterates in descending order)

-- Batch data processing
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