---
title: "Cache Module"
---

The **cache** module provides a distributed cache system for Lua scripts. The cache supports read/write operations with automatic expiration (TTL) and synchronization mechanisms for concurrent operations.

The cache system is especially useful for:

- Storing results of expensive operations (such as HTTP requests, database queries)

- Avoiding redundant calls to external APIs

- Synchronizing multiple workers that try to access the same resource simultaneously

- Sharing data between different running Lua scripts

## Available Functions

### `cache.put(key, value, ttl)`

Stores a value in the cache with a specific time-to-live.

**Parameters**:

- `key` (string): Unique key to identify the value in the cache

- `value` (any Lua type): Value to be stored (can be string, number, table, boolean, etc.)

- `ttl` (number): Time To Live in seconds - how long the value will remain in the cache

**Return value**:

- `nil` on success

- Throws an error on failure

**Example**:

```lua
-- Store an API result for 5 minutes (300 seconds)
local resultado_api = {status = "ativo", usuarios = 150}
cache.put("status_sistema", resultado_api, 300)

-- Store a simple string for 1 hour
cache.put("ultima_atualizacao", "2026-01-15T10:30:00Z", 3600)

-- Store a number
cache.put("contador_requisicoes", 42, 60)
```

### `cache.get(key)`

Retrieves a value from the cache.

**Parameters**:

- `key` (string): Key of the value to retrieve

**Return value**:

- The stored value if it exists and is not expired

- `nil` if the key does not exist or the value has expired

**Example**:

```lua
-- Retrieve a value from the cache
local status = cache.get("status_sistema")

if status then
    print("Status do sistema:", status.status)
    print("Usuários ativos:", status.usuarios)
else
    print("Cache expirado ou não encontrado")
    -- Fazer uma nova requisição para obter os dados
end

-- Verificar se um valor existe
local ultima_atualizacao = cache.get("ultima_atualizacao")
if ultima_atualizacao then
    print("Última atualização:", ultima_atualizacao)
end
```

### `cache.mark_pending(key)`

Marks a key as "pending". This function is used to synchronize multiple workers that try to compute the same value simultaneously.

**Parameters**:

- `key` (string): Key to be marked as pending

**Return value**:

- `nil` on success

- Throws an error on failure

**Behavior**:

- When a key is marked as pending, any subsequent call to `cache.get()` for that key will block until a value is stored with `cache.put()`

- The "pending" state automatically expires after 5 minutes (300 seconds)

- Useful to prevent multiple workers from recalculating the same expensive value simultaneously

**Example**:

```lua
-- Typical pattern to avoid cache stampede
local function obter_dados_caros(chave)
    -- First try to get from cache
    local dados = cache.get(chave)

    if dados then
        return dados
    end

    -- If not found, mark as pending
    local sucesso, erro = pcall(cache.mark_pending, chave)

    if not sucesso then
        -- Another worker already marked as pending, wait for the result
        dados = cache.get(chave)  -- Esta chamada irá bloquear até o valor estar disponível
        if dados then
            return dados
        end
    end

    -- This worker is responsible for calculating the value
    -- ... expensive calculation here ...
    local resultado = calcular_dados_caros()

    -- Store it in the cache for other workers
    cache.put(chave, resultado, 300)

    return resultado
end
```

### `cache.delete(key)`

Removes a key from the cache immediately.

**Parameters**:

- `key` (string): Key to be removed

**Return value**:

- `nil` on success

- Throws an error on failure

**Example**:

```lua
-- Remove a specific value
cache.delete("dados_expirados")

-- Clear cache related to a user
cache.delete("usuario_123_perfil")
cache.delete("usuario_123_preferencias")
cache.delete("usuario_123_historico")
```

## Additional Information

### Worker Synchronization

The "pending" mechanism allows multiple workers to synchronize the computation of expensive values:

1. The first worker marks the key as pending and computes the value

2. Other workers that try to access the same key wait for the result

3. When the first worker finishes, it stores the value and all workers receive it

### Supported Data Types

The cache can store any Lua value supported by Monsta's serialization system, including:

- Strings

- Numbers

- Booleans

- Tables

- Null values

## Performance Considerations

1. Fast access: Cache operations are much faster than recalculating values or making external requests

2. Memory: The cache is kept in memory, so very large values can impact performance

3. Concurrency: The system is thread-safe and supports concurrent access from multiple workers

4. Network: The cache is local to the process, there is no network overhead

## Limitations

1. Volatile: Data is lost if the process is restarted

2. Limited memory: Do not use it to store large volumes of data

3. Distribution: This is a local cache, not distributed across multiple servers

## Best Practices

1. Appropriate TTL: Use TTLs appropriate for the type of data (short for dynamic data, long for static data)

2. Descriptive keys: Use key names that clearly describe the content

3. Namespace: Use prefixes to organize keys (e.g., `api_`, `user_`, `config_`)

4. Fallback: Always have a fallback in case the cache is empty or expired

5. Invalidation: Use `delete()` to invalidate cache when data changes