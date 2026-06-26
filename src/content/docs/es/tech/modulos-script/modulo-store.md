---
title: "Módulo Store"
---

El módulo **store** proporciona un sistema de almacenamiento persistente de datos que utiliza namespacing automático. Cada valor almacenado se asocia automáticamente al identificador de ejecución (EXEC_IDENT) de la métrica o script, creando un espacio de nombres aislado para cada uno. Esto significa que, por defecto, diferentes métricas no comparten datos, pero múltiples ejecuciones de la misma métrica pueden acceder y modificar los valores que ésta almacenó previamente. El módulo es útil para almacenar estados, configuraciones o historiales que necesitan persistir entre reinicios del agente.

- Almacenamiento clave-valor persistente en disco

- Namespacing automático basado en el identificador de la métrica/script

- Timestamp automático para cada entrada

- Thread-safe (seguro para uso concurrente)

- Persistencia garantizada entre reinicios del agente

## Diferencia entre Store, Registry y Cache

### Store vs Registry:

- **Store**: Persiste en disco, sobrevive a reinicios del agente pero es global para todas las métricas/scripts

- **Registry**: Almacenamiento solo en memoria, se pierde al reiniciar

### Store vs Cache:

- **Store**: Persistente, sin políticas de expiración automática

- **Cache**: Optimizado para acceso rápido, con políticas de expiración

### Namespacing:

- **Funciones `put`/`get`/`delete`**: Usan namespacing automático (clave + ident)

- **Funciones `*_global`**: Ignoran el namespacing (clave pura)

## Funciones Disponibles

### 1. `store.put(chave, valor)`

Almacena un valor en el store con namespacing automático.

#### Parámetros:

- **clave** (string): Identificador para el valor (será prefijado con el ident)

- **valor** (cualquier tipo Lua): Valor a almacenar (string, número, booleano, tabla, nil)

#### Retorno:

- **nil**: La función no devuelve valor

#### Comportamiento:

1. Prefija la clave con el identificador de ejecución actual (si está disponible)

2. Almacena el valor asociado a la clave prefijada

3. Registra automáticamente el timestamp actual (UTC)

4. Sobrescribe cualquier valor existente con la misma clave

5. Persiste automáticamente en disco

#### Ejemplo de Uso:

```lua
-- Almacenar datos específicos del script actual
store.put("ultima_execucao", os.time())
store.put("contador_falhas", 0)
store.put("config", {
    timeout = 30,
    intervalo = 60,
    alertas = true
})

-- Los datos se almacenarán con el prefijo del ident
-- Si EXEC_IDENT = "monitor-cpu", la clave se convierte en "monitor-cpu:ultima_execucao"
```

### 2. `store.get(chave)`

Recupera un valor del store con namespacing automático.

#### Parámetros:

- **clave** (string): Clave del valor a recuperar (será prefijada con el ident)

#### Retorno:

- **tupla**: `(valor, timestamp)` donde:

    - **valor** (cualquier tipo o nil): Valor almacenado, o `nil` si la clave no existe

    - **timestamp** (número o nil): Timestamp Unix (segundos) de la última actualización, o `nil` si la clave no existe

#### Comportamiento:

1. Prefija la clave con el identificador de ejecución actual

2. Devuelve el valor y el timestamp si la clave existe

3. Devuelve `(nil, nil)` si la clave no existe

4. Preserva el tipo original del valor almacenado

5. El timestamp está en segundos desde la epoch Unix (UTC)

#### Ejemplo de Uso:

```lua
-- Recuperar datos del script actual
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

-- Verificar existência com valor padrão
local limite, _ = store.get("limite_temperatura")
limite = limite or 70  -- Valor por defecto si no está configurado
```

### 3. `store.delete(chave)`

Elimina una entrada del store con namespacing automático.

#### Parámetros:

- **clave** (string): Clave de la entrada a eliminar (será prefijada con el ident)

#### Retorno:

- **nil**: La función no devuelve valor

#### Comportamiento:

1. Prefija la clave con el identificador de ejecución actual

2. Elimina completamente la entrada del store

3. No hace nada si la clave no existe

4. Libera el espacio en memoria y disco

5. Operación atómica y thread-safe

#### Ejemplo de Uso:

```lua
-- Eliminar datos específicos del script
store.delete("cache_temporario")
store.delete("dados_processados")

-- Limpiar todos los datos del script actual
local function limpar_dados_script()
    -- Nota: No hay listado directo de claves
    -- Es necesario conocer las claves usadas
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

-- Eliminar tras el procesamiento
local function processar_e_limpar(chave)
    local dados, timestamp = store.get(chave)

    if dados then
        -- Procesar datos
        local resultado = processar_dados(dados)

        -- Eliminar tras el procesamiento
        store.delete(chave)
        log.info("Dados processados e removidos:", chave)

        return resultado
    else
        log.warn("Chave não encontrada:", chave)
        return nil
    end
end
```

### 4. `store.put_global(chave, valor)`

Almacena un valor en el store SIN namespacing (clave global).

#### Parámetros:

- **chave** (string): Identificador global para el valor (no se prefija)

- **valor** (cualquier tipo Lua): Valor a almacenar

#### Retorno:

- **nil**: La función no devuelve valor

#### Comportamiento:

1. Almacena el valor con la clave exacta proporcionada

2. No aplica prefijo del identificador de ejecución

3. Compartido entre todos los scripts (global)

4. Persiste en disco

5. Sobrescribe cualquier valor existente con la misma clave

#### Ejemplo de Uso:

```lua
-- Almacenar datos globales compartidos
store.put_global("versao_agente", "2.5.1")
store.put_global("ultima_atualizacao", os.time())
store.put_global("config_global", {
    timezone = "America/Sao_Paulo",
    log_level = "info",
    retencao_logs = 30  -- días
})

-- Los datos serán accesibles por todos los scripts
-- Clave exacta: "versao_agente" (sin prefijo)
```

### 5. `store.get_global(chave)`

Recupera un valor del store SIN namespacing (clave global).

#### Parámetros:

- **chave** (string): Clave global del valor a recuperar (no se prefija)

#### Retorno:

- **tupla**: `(valor, timestamp)` donde:

    - **valor** (cualquier tipo o nil): Valor almacenado, o `nil` si la clave no existe

    - **timestamp** (número o nil): Timestamp Unix (segundos) de la última actualización, o `nil` si la clave no existe

#### Comportamiento:

1. Busca el valor usando la clave exacta proporcionada (sin prefijo)

2. Devuelve el valor y el timestamp si la clave existe

3. Devuelve `(nil, nil)` si la clave no existe

4. Preserva el tipo original del valor almacenado

5. El timestamp está en segundos desde la epoch Unix (UTC)

6. Accede a datos compartidos por todos los scripts

#### Ejemplo de Uso:

```lua
-- Recuperar datos globales compartidos
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

-- Verificar y usar valor por defecto para configuração global
local timezone, _ = store.get_global("timezone")
timezone = timezone or "UTC"  -- Valor por defecto si no está configurado
print("Timezone configurado:", timezone)

-- Verificar existencia de flag global
local manutencao, ts_manutencao = store.get_global("modo_manutencao")
if manutencao then
    log.warn("Sistema em modo de manutenção desde", os.date("%H:%M:%S", ts_manutencao))
    -- Saltar ejecuciones no críticas
    return
end
```