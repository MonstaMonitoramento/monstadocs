---
title: "UUID Module"
---

The **uuid** module provides functions for generating universally unique identifiers (UUIDs) following the RFC 4122 standard. This module is useful for scripts that need to create unique identifiers for transaction tracking, resource identification, and cases that require guaranteed uniqueness.

**Key features**:

- Generation of version 4 UUIDs (random)

- RFC 4122 standard format (8-4-4-4-12)

- Statistical uniqueness guarantee

- Thread-safe and safe for concurrent use

**UUID v4 Format**:

- `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`

- Where `x` is any hexadecimal digit

- `4` indicates version 4 (random)

- `y` is 8, 9, A or B (indicating variant)

## Available Functions

### 1. `uuid.uuid4()`

Generates a version 4 UUID (random) in the RFC 4122 standard format.

#### Parameters:

- None

#### Return:

- **string**: UUID in the format `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`

#### Behavior:

1. Generates 128 random bits using a cryptographically secure generator

2. Sets the version bits to 4 (0100)

3. Sets the variant bits to RFC 4122 (10)

4. Formats as a string in the 8-4-4-4-12 pattern

5. Ensures statistical uniqueness (extremely low probability of collision)

#### Example Usage:

```lua
-- Generate a simple UUID
local id = uuid.uuid4()
print("UUID gerado:", id)
-- Exemplo: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

-- Generate multiple UUIDs
local ids = {}
for i = 1, 5 do
    ids[i] = uuid.uuid4()
    print("UUID", i, ":", ids[i])
end

-- Use as a transaction identifier
local transacao_id = uuid.uuid4()
local log_entry = {
    id = transacao_id,
    tipo = "pagamento",
    valor = 150.75,
    timestamp = now(),
    status = "processando"
}
print("Transação ID:", transacao_id)

-- Create unique file names
local nome_arquivo = "backup_" .. uuid.uuid4() .. ".tar.gz"
print("Arquivo de backup:", nome_arquivo)

-- Generate session token
local sessao_token = "sess_" .. string.sub(uuid.uuid4(), 1, 8)
print("Token de sessão:", sessao_token)
```

## Additional Information

### Guaranteed Uniqueness:

```lua
-- Extremely low collision probability
-- 2^128 possibilities ≈ 3.4 × 10^38 unique UUIDs
-- Even generating 1 billion UUIDs per second,
-- it would take ~100 years to have a 50% chance of collision

local function testar_unicidade(iteracoes)
    local uuids = {}
    local colisoes = 0

    for i = 1, iteracoes do
        local id = uuid.uuid4()

        if uuids[id] then
            colisoes = colisoes + 1
            log.error("COLISÃO DETECTADA!", "Iteração:", i, "ID:", id)
        else
            uuids[id] = true
        end
    end

    return {
        iteracoes = iteracoes,
        colisoes = colisoes,
        taxa_colisao = (colisoes / iteracoes) * 100
    }
end

-- In practical tests, collisions are virtually non-existent
```

### Standard Format:

```lua
-- UUID always in RFC 4122 format
local id = uuid.uuid4()
-- Format: xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
-- Example: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

-- Validate format
local function validar_uuid(uuid_str)
    local padrao = "^%x%x%x%x%x%x%x%x%-%x%x%x%x%-4%x%x%x%-[89ab]%x%x%x%-%x%x%x%x%x%x%x%x%x%x%x%x$"
    return string.match(uuid_str:lower(), padrao) ~= nil
end

print("UUID válido?", validar_uuid(id))  -- true
print("UUID válido?", validar_uuid("invalid"))  -- false
```

## Usage Examples

### 1. Temporary File Names:

```lua
-- Generate unique file names for processing
local function criar_arquivo_temporario(extensao, dados)
    local nome_arquivo = "tmp_" .. uuid.uuid4() .. "." .. (extensao or "tmp")
    local caminho = "/tmp/" .. nome_arquivo

    -- Write data
    local arquivo = io.open(caminho, "w")
    if arquivo then
        arquivo:write(dados)
        arquivo:close()

        -- Register for cleanup
        local arquivos_temp, _ = store.get("arquivos_temporarios") or {}
        table.insert(arquivos_temp, {
            caminho = caminho,
            criado_em = now(),
            expira_em = now() + 3600  -- 1 hour
        })
        store.put("arquivos_temporarios", arquivos_temp)

        return caminho
    else
        return nil, "Não foi possível criar arquivo"
    end
end

-- Clean up old temporary files
local function limpar_arquivos_temporarios()
    local arquivos_temp, _ = store.get("arquivos_temporarios") or {}
    local removidos = 0
    local agora = now()

    for i = #arquivos_temp, 1, -1 do
        local arquivo = arquivos_temp[i]

        if agora > arquivo.expira_em then
            -- Attempt to remove file
            local ok, _ = pcall(os.remove, arquivo.caminho)
            if ok then
                table.remove(arquivos_temp, i)
                removidos = removidos + 1
                log.debug("Arquivo temporário removido", "Caminho:", arquivo.caminho)
            end
        end
    end

    store.put("arquivos_temporarios", arquivos_temp)
    return removidos
end
```