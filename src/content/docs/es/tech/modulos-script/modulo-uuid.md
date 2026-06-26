---
title: "Módulo UUID"
---

El módulo **uuid** proporciona funciones para la generación de identificadores únicos universales (UUIDs) conforme al estándar RFC 4122. Este módulo es útil para scripts que necesitan crear identificadores únicos para el seguimiento de transacciones, la identificación de recursos y casos que requieren unicidad garantizada.

**Características principales**:

- Generación de UUID versión 4 (aleatorio)

- Formato estándar RFC 4122 (8-4-4-4-12)

- Garantía de unicidad estadística

- Thread-safe y seguro para uso concurrente

**Formato UUID v4**:

- `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`

- Donde `x` es cualquier dígito hexadecimal

- `4` indica la versión 4 (aleatorio)

- `y` es 8, 9, A o B (indicando variante)

## Funciones disponibles

### 1. `uuid.uuid4()`

Genera un UUID versión 4 (aleatorio) en el formato estándar RFC 4122.

#### Parámetros:

- Ninguno

#### Retorno:

- **string**: UUID en el formato `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`

#### Comportamiento:

1. Genera 128 bits aleatorios usando un generador criptográficamente seguro

2. Define los bits de versión a 4 (0100)

3. Define los bits de variante para RFC 4122 (10)

4. Formatea como cadena en el patrón 8-4-4-4-12

5. Garantiza unicidad estadística (probabilidad de colisión extremadamente baja)

#### Ejemplo de uso:

```lua
-- Generar un UUID simple
local id = uuid.uuid4()
print("UUID gerado:", id)
-- Exemplo: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

-- Generar múltiples UUIDs
local ids = {}
for i = 1, 5 do
    ids[i] = uuid.uuid4()
    print("UUID", i, ":", ids[i])
end

-- Usar como identificador de transacción
local transacao_id = uuid.uuid4()
local log_entry = {
    id = transacao_id,
    tipo = "pagamento",
    valor = 150.75,
    timestamp = now(),
    status = "processando"
}
print("Transação ID:", transacao_id)

-- Crear nombres de archivo únicos
local nome_arquivo = "backup_" .. uuid.uuid4() .. ".tar.gz"
print("Arquivo de backup:", nome_arquivo)

-- Generar token de sesión
local sessao_token = "sess_" .. string.sub(uuid.uuid4(), 1, 8)
print("Token de sessão:", sessao_token)
```

## Información adicional

### Unicidad garantizada:

```lua
-- Probabilidad de colisión extremadamente baja
-- 2^128 posibilidades ≈ 3.4 × 10^38 UUIDs únicos
-- Incluso generando 1.000 millones de UUIDs por segundo,
-- tomaría ~100 años para tener un 50% de probabilidad de colisión

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

-- En pruebas prácticas, las colisiones son virtualmente inexistentes
```

### Formato estándar:

```lua
-- UUID siempre en el formato RFC 4122
local id = uuid.uuid4()
-- Formato: xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
-- Ejemplo: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

-- Validar formato
local function validar_uuid(uuid_str)
    local padrao = "^%x%x%x%x%x%x%x%x%-%x%x%x%x%-4%x%x%x%-[89ab]%x%x%x%-%x%x%x%x%x%x%x%x%x%x%x%x$"
    return string.match(uuid_str:lower(), padrao) ~= nil
end

print("UUID válido?", validar_uuid(id))  -- true
print("UUID válido?", validar_uuid("invalid"))  -- false
```

## Ejemplos de uso

### 1. Nombres de archivos temporales:

```lua
-- Generar nombres de archivos únicos para procesamiento
local function criar_arquivo_temporario(extensao, dados)
    local nome_arquivo = "tmp_" .. uuid.uuid4() .. "." .. (extensao or "tmp")
    local caminho = "/tmp/" .. nome_arquivo

    -- Escribir datos
    local arquivo = io.open(caminho, "w")
    if arquivo then
        arquivo:write(dados)
        arquivo:close()

        -- Registrar para limpieza
        local arquivos_temp, _ = store.get("arquivos_temporarios") or {}
        table.insert(arquivos_temp, {
            caminho = caminho,
            criado_em = now(),
            expira_em = now() + 3600  -- 1 hora
        })
        store.put("arquivos_temporarios", arquivos_temp)

        return caminho
    else
        return nil, "Não foi possível criar arquivo"
    end
end

-- Limpiar archivos temporales antiguos
local function limpar_arquivos_temporarios()
    local arquivos_temp, _ = store.get("arquivos_temporarios") or {}
    local removidos = 0
    local agora = now()

    for i = #arquivos_temp, 1, -1 do
        local arquivo = arquivos_temp[i]

        if agora > arquivo.expira_em then
            -- Intentar eliminar archivo
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