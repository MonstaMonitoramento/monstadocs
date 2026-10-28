---
title: "Time Module"
---

The **time** module provides functions for manipulating time and dates. This module is useful for scripts that need to measure intervals, wait for specific periods, parse dates, and implement timeouts in asynchronous operations.

**Main features**:

- Unix timestamps in seconds

- Parsing dates in RFC 3339 format

- Non-blocking asynchronous sleep

- Timeouts for asynchronous operations

## Available Functions

### 1. `time.now()`

Returns the current Unix timestamp in seconds.

#### Parameters

- None

#### Return

- **number**: Current Unix timestamp (seconds since January 1, 1970, 00:00:00 UTC)

#### Behavior

- Returns the current time in UTC

- Second-level precision (not milliseconds)

- Same value returned by `os.time()` in standard Lua

- Available as a global function and in the `time` module

#### Usage Example

```lua
-- Using the time module
local timestamp_modulo = time.now()
print("Timestamp módulo:", timestamp_modulo)

-- Using the global function (same function)
local timestamp_global = now()
print("Timestamp global:", timestamp_global)

-- Both return the same value
print("São iguais?", timestamp_global == timestamp_modulo)  -- true

-- Calculate operation duration
local inicio = time.now()
-- ... operação demorada ...
local fim = time.now()
local duracao = fim - inicio
print("Operação levou", duracao, "segundos")

-- Log events with timestamp
local evento = {
    tipo = "login",
    usuario = "admin",
    timestamp = now(),
    origem = system.hostname()
}

-- Schedule future execution
local proxima_execucao = time.now() + 3600  -- 1 hora a partir de agora
print("Próxima execução em:", os.date("%H:%M:%S", proxima_execucao))
```

### 2. `time.sleep(segundos)`

Asynchronously waits for a specific number of seconds.

#### Parameters

- **segundos** (number): Number of seconds to wait

#### Return

- **nil**: The function does not return a value (after waiting)

#### Behavior

- Precision depends on the system scheduler

#### Usage Example

```lua
-- Wait 5 seconds
await(time.sleep(5))
print("5 segundos se passaram")

-- Implement polling with interval
local function poll_com_intervalo(url, intervalo_segundos, max_tentativas)
    for tentativa = 1, max_tentativas do
        log.info("Tentativa", tentativa, "de", max_tentativas)

        -- Make request
        local resposta, status = http.get(url)

        if status == 200 then
            log.info("Sucesso na tentativa", tentativa)
            return resposta
        end

        -- Wait before next attempt
        if tentativa < max_tentativas then
            log.info("Aguardando", intervalo_segundos, "segundos...")
            time.sleep(intervalo_segundos)
        end
    end

    log.error("Todas as tentativas falharam")
    return nil
end

-- Usage
local dados = poll_com_intervalo("https://api.exemplo.com/status", 10, 6)

-- Execution control with exponential backoff
local function executar_com_backoff(funcao, max_tentativas)
    local tentativa = 1

    while tentativa <= max_tentativas do
        -- with_coroutine returns (result, err)
        local resultado, err = with_coroutine(funcao)

        if not err then
            return resultado
        end

        -- Exponential backoff: 2^(attempt-1) seconds
        local wait_time = math.pow(2, tentativa - 1)
        log.warn("Tentativa", tentativa, "falhou. Aguardando", wait_time, "segundos")

        if tentativa < max_tentativas then
            time.sleep(wait_time)
        end

        tentativa = tentativa + 1
    end

    error("Todas as tentativas falharam")
end
```

### 3. `time.parse(string_data)`

Parses a date/time string in RFC 3339 format and returns a date object.

#### Parameters

- **string_data** (string): Date/time in RFC 3339 format (e.g., "2024-01-15T10:30:00Z")

#### Return

- **LuaDateTime object**: Object with a `seconds()` method that returns the Unix timestamp

#### RFC 3339 Format

- `YYYY-MM-DDTHH:MM:SSZ` (UTC)

- `YYYY-MM-DDTHH:MM:SS+HH:MM` (with timezone offset)

- Examples: "2024-01-15T10:30:00Z", "2024-01-15T07:30:00-03:00"

#### Usage Example

```lua
-- Parse UTC date
local data_utc = time.parse("2024-01-15T10:30:00Z")
local timestamp_utc = data_utc:seconds()
print("Timestamp UTC:", timestamp_utc)  -- 1705314600

-- Parse date with timezone offset
local data_local = time.parse("2024-01-15T07:30:00-03:00")
local timestamp_local = data_local:seconds()
print("Timestamp local:", timestamp_local)  -- 1705314600 (mesmo momento)

-- Convert to readable format
local function formatar_data_rfc3339(timestamp)
    return os.date("%Y-%m-%dT%H:%M:%SZ", timestamp)
end

-- Calculate difference between dates
local data1 = time.parse("2024-01-15T10:30:00Z")
local data2 = time.parse("2024-01-15T11:45:00Z")
local diferenca = data2:seconds() - data1:seconds()
print("Diferença:", diferenca, "segundos (", diferenca/60, "minutos)")

-- Validate and parse input date using with_coroutine
local function parsear_data_segura(data_string)
    -- with_coroutine returns (result, err)
    local data, err = with_coroutine(time.parse, data_string)
    
    if not err and data then
        return data:seconds()
    else
        log.error("Data inválida:", data_string, "-", err)
        return nil
    end
end

-- Usage
local timestamp = parsear_data_segura("2024-01-15T10:30:00Z")
if timestamp then
    print("Data válida:", os.date("%d/%m/%Y %H:%M:%S", timestamp))
end
```