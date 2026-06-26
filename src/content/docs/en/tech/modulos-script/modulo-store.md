---
title: "Store Module"
---

The **store** module provides a persistent data storage system that uses automatic namespacing. Each stored value is automatically associated with the execution identifier (EXEC_IDENT) of the metric or script, creating an isolated namespace for each. This means that, by default, different metrics do not share data, but multiple runs of the same metric can access and modify values it previously stored. The module is useful for storing states, configurations, or histories that need to persist across agent restarts.

- Persistent key-value storage on disk

- Automatic namespacing based on the metric/script identifier

- Automatic timestamp for each entry

- Thread-safe (safe for concurrent use)

- Persistence guaranteed across agent restarts

## Difference between Store, Registry and Cache

### Store vs Registry:

- **Store**: Persists to disk, survives agent restarts but is global for all metrics/scripts

- **Registry**: Memory-only storage, lost on restart

### Store vs Cache:

- **Store**: Persistent, no automatic expiration policies

- **Cache**: Optimized for fast access, with expiration policies

### Namespacing:

- **`put`/`get`/`delete` functions**: Use automatic namespacing (key + ident)

- **`*_global` functions**: Ignore namespacing (raw key)

## Available Functions

### 1. `store.put(key, value)`

Stores a value in the store with automatic namespacing.

#### Parameters:

- **key** (string): Identifier for the value (will be prefixed with the ident)

- **value** (any Lua type): Value to be stored (string, number, boolean, table, nil)

#### Return:

- **nil**: The function does not return a value

#### Behavior:

1. Prefixes the key with the current execution identifier (if available)

2. Stores the value associated with the prefixed key

3. Automatically records the current timestamp (UTC)

4. Overwrites any existing value with the same key

5. Persists automatically to disk

#### Usage Example:

```lua
-- Store data specific to the current script
store.put("ultima_execucao", os.time())
store.put("contador_falhas", 0)
store.put("config", {
    timeout = 30,
    intervalo = 60,
    alertas = true
})

-- Data will be stored with the ident prefix
-- If EXEC_IDENT = "monitor-cpu", the key becomes "monitor-cpu:ultima_execucao"
```

### 2. `store.get(key)`

Retrieves a value from the store with automatic namespacing.

#### Parameters:

- **key** (string): Key of the value to retrieve (will be prefixed with the ident)

#### Return:

- **tuple**: `(value, timestamp)` where:

    - **value** (any type or nil): Stored value, or `nil` if the key does not exist

    - **timestamp** (number or nil): Unix timestamp (seconds) of the last update, or `nil` if the key does not exist

#### Behavior:

1. Prefixes the key with the current execution identifier

2. Returns the value and timestamp if the key exists

3. Returns `(nil, nil)` if the key does not exist

4. Preserves the original type of the stored value

5. The timestamp is in seconds since the Unix epoch (UTC)

#### Usage Example:

```lua
-- Retrieve data from the current script
local ultima_exec, timestamp = store.get("ultima_execucao")
if ultima_exec then
    local diferenca = os.time() - timestamp
    print("Última execução há", diferenca, "segundos")
end

-- Recuperar configuração
local config, ts = store.get("configuracao")
if config then
    print("Configuração carregada (atualizada em", os.date("%H:%M:%S", ts), ")")
    for chave, valor in pairs(config) do
        print("  ", chave, "=", valor)
    end
end

-- Check existence with default value
local limite, _ = store.get("limite_temperatura")
limite = limite or 70  -- Default value if not configured
```

### 3. `store.delete(key)`

Removes an entry from the store with automatic namespacing.

#### Parameters:

- **key** (string): Key of the entry to remove (will be prefixed with the ident)

#### Return:

- **nil**: The function does not return a value

#### Behavior:

1. Prefixes the key with the current execution identifier

2. Completely removes the entry from the store

3. Does nothing if the key does not exist

4. Frees memory and disk space

5. Operation is atomic and thread-safe

#### Usage Example:

```lua
-- Remove script-specific data
store.delete("cache_temporario")
store.delete("dados_processados")

-- Clear all data of the current script
local function limpar_dados_script()
    -- Note: There is no direct listing of keys
    -- It is necessary to know the keys used
    local chaves_conhecidas = {
        "configuracao",
        "cache",
        "estado",
        "historico",
        "lock_backup"
    }

    for _, chave in ipairs(chaves_conhecidas) do
        store.delete(chave)
        log.debug("Removido:", chave)
    end
end

-- Remove after processing
local function processar_e_limpar(chave)
    local dados, timestamp = store.get(chave)

    if dados then
        -- Process data
        local resultado = processar_dados(dados)

        -- Remove after processing
        store.delete(chave)
        log.info("Dados processados e removidos:", chave)

        return resultado
    else
        log.warn("Chave não encontrada:", chave)
        return nil
    end
end
```

### 4. `store.put_global(key, value)`

Stores a value in the store WITHOUT namespacing (global key).

#### Parameters:

- **key** (string): Global identifier for the value (not prefixed)

- **value** (any Lua type): Value to be stored

#### Return:

- **nil**: The function does not return a value

#### Behavior:

1. Stores the value with the exact provided key

2. Does not apply the execution identifier prefix

3. Shared among all scripts (global)

4. Persists to disk

5. Overwrites any existing value with the same key

#### Usage Example:

```lua
-- Store shared global data
store.put_global("versao_agente", "2.5.1")
store.put_global("ultima_atualizacao", os.time())
store.put_global("config_global", {
    timezone = "America/Sao_Paulo",
    log_level = "info",
    retencao_logs = 30  -- days
})

-- Data will be accessible by all scripts
-- Exact key: "versao_agente" (no prefix)
```

### 5. `store.get_global(key)`

Retrieves a value from the store WITHOUT namespacing (global key).

#### Parameters:

- **key** (string): Global key of the value to retrieve (not prefixed)

#### Return:

- **tuple**: `(value, timestamp)` where:

    - **value** (any type or nil): Stored value, or `nil` if the key does not exist

    - **timestamp** (number or nil): Unix timestamp (seconds) of the last update, or `nil` if the key does not exist

#### Behavior:

1. Looks up the value using the exact provided key (no prefix)

2. Returns the value and timestamp if the key exists

3. Returns `(nil, nil)` if the key does not exist

4. Preserves the original type of the stored value

5. The timestamp is in seconds since the Unix epoch (UTC)

6. Accesses data shared by all scripts

#### Usage Example:

```lua
-- Retrieve shared global data
local versao, ts_versao = store.get_global("versao_agente")
if versao then
    print("Versão do agente:", versao, "(atualizada em", os.date("%Y-%m-%d %H:%M:%S", ts_versao), ")")
end

-- Recuperar configuração global
local config_global, ts_config = store.get_global("config_global")
if config_global then
    print("Configuração global carregada:")
    for chave, valor in pairs(config_global) do
        print("  ", chave, "=", valor)
    end
end

-- Check and use default value for global configuration
local timezone, _ = store.get_global("timezone")
timezone = timezone or "UTC"  -- Default value if not configured
print("Timezone configurado:", timezone)

-- Check existence of global flag
local manutencao, ts_manutencao = store.get_global("modo_manutencao")
if manutencao then
    log.warn("Sistema em modo de manutenção desde", os.date("%H:%M:%S", ts_manutencao))
    -- Skip non-critical runs
    return
end
```