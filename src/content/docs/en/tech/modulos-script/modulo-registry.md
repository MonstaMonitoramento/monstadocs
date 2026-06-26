---
title: "Registry Module"
---

The **registry** module provides a persistent, shared data storage system across Lua script executions. This module is useful for maintaining state between different runs, sharing data between scripts, and implementing caching mechanisms and persistent configuration.

- Persistent key-value storage

- Automatic timestamp for each entry

- Thread-safe (safe for concurrent use)

- Data shared among all Lua scripts

- Persistence across agent restarts

## Available Functions

### 1. `registry.put(chave, valor)`

Stores a value in the registry with the specified key.

#### Parameters:

- **chave** (string): Unique identifier for the value

- **valor** (any Lua type): Value to be stored (string, number, boolean, table, nil)

#### Return:

- **nil**: The function does not return a value

#### Behavior:

1. Stores the value associated with the key

2. Automatically records the current timestamp (UTC)

3. Overwrites any existing value with the same key

4. Accepts any Lua data type supported by Monagent's value system

#### Usage Example:

```lua
-- Store basic values
registry.put("ultima_execucao", os.time())
registry.put("hostname", "servidor-producao")
registry.put("ativo", true)
registry.put("versao", 2.5)

-- Store complex tables
local config = {
    timeout = 30,
    retries = 3,
    servidores = {"srv1", "srv2", "srv3"},
    limites = {cpu = 80, memoria = 90, disco = 95}
}
registry.put("configuracao_monitoramento", config)

-- Store processing results
local metricas = {
    cpu_usage = 45.6,
    memory_usage = 78.3,
    disk_usage = 62.1,
    timestamp = os.time()
}
registry.put("metricas_recentes", metricas)

-- Overwrite existing value
registry.put("contador", 1)
-- ... later ...
local valor, timestamp = registry.get("contador")
registry.put("contador", (valor or 0) + 1)
```

### 2. `registry.get(chave)`

Retrieves a value from the registry by the specified key.

#### Parameters:

- **chave** (string): Key of the value to retrieve

#### Return:

- **tuple**: `(valor, timestamp)` where:

    - **valor** (any type or nil): Stored value, or `nil` if the key does not exist

    - **timestamp** (number or nil): Unix timestamp (seconds) of the last update, or `nil` if the key does not exist

#### Behavior:

1. Returns the value and timestamp if the key exists

2. Returns `(nil, nil)` if the key does not exist

3. Preserves the original type of the stored value

4. The timestamp is in seconds since the Unix epoch (UTC)

#### Usage Example:

```lua
-- Retrieve simple value
local valor, timestamp = registry.get("config_timeout")
if valor then
    print("Timeout configurado:", valor, "desde", os.date("%H:%M:%S", timestamp))
else
    print("Configuração não encontrada")
end

-- Retrieve table
local config, ts = registry.get("configuracao_sistema")
if config then
    print("Configuração carregada:")
    for chave, valor in pairs(config) do
        print("  ", chave, "=", valor)
    end
    print("Última atualização:", os.date("%Y-%m-%d %H:%M:%S", ts))
end

-- Check existence before using
local dados, timestamp = registry.get("dados_processamento")
if dados then
    -- Process existing data
    processar_dados(dados)
else
    -- Initialize new data
    dados = inicializar_dados()
    registry.put("dados_processamento", dados)
end

-- Use default value if not present
local limite, _ = registry.get("limite_cpu")
limite = limite or 80  -- Default value 80% if not configured
```

### 3. `registry.delete(chave)`

Removes an entry from the registry by the specified key.

#### Parameters:

- **chave** (string): Key of the entry to remove

#### Return:

- **nil**: The function does not return a value

#### Behavior:

1. Completely removes the entry from the registry

2. Does nothing if the key does not exist

3. Frees memory associated with the key

4. Atomic and thread-safe operation

#### Usage Example:

```lua
-- Remove specific entry
registry.delete("cache_temporario")
print("Cache temporário removido")

-- Clean all entries with a prefix
local function limpar_prefixo(prefixo)
    -- Note: The registry does not support direct listing
    -- In a real case, you would need to maintain a list of keys
    log.info("Limpando entradas com prefixo:", prefixo)

    -- Example with known keys
    local chaves_conhecidas = {
        prefixo .. "_cache_dns",
        prefixo .. "_cache_http",
        prefixo .. "_metricas",
        prefixo .. "_config"
    }

    for _, chave in ipairs(chaves_conhecidas) do
        registry.delete(chave)
        log.debug("Removido:", chave)
    end
end

-- Clean expired entries
local function limpar_expirados(ttl_segundos)
    local agora = os.time()
    -- Note: Again, without direct listing, a strategy is needed
    log.info("Limpeza de expirados não suportada diretamente")
    log.info("Use timestamps nas chaves ou mantenha lista de chaves")
end

-- Remove after use
local function processar_e_limpar(chave)
    local dados, timestamp = registry.get(chave)

    if dados then
        -- Process data
        local resultado = processar(dados)

        -- Remove after processing
        registry.delete(chave)
        log.info("Dados processados e removidos:", chave)

        return resultado
    else
        log.warn("Chave não encontrada:", chave)
        return nil
    end
end
```