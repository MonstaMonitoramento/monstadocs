---
title: "Módulo time"
---

El módulo **time** proporciona funciones para la manipulación de tiempo y fechas. Este módulo es útil para scripts que necesitan medir intervalos, esperar por periodos específicos, parsear fechas e implementar timeouts en operaciones asíncronas.

**Características principales**:

- Timestamps Unix en segundos

- Parseo de fechas en el formato RFC 3339

- Sleep asíncrono no bloqueante

- Timeouts para operaciones asíncronas

## Funciones disponibles

### 1. `time.now()`

Devuelve el timestamp Unix actual en segundos.

#### Parámetros

- Ninguno

#### Retorno

- **número**: Timestamp Unix actual (segundos desde 1 de enero de 1970, 00:00:00 UTC)

#### Comportamiento

- Devuelve la hora actual en UTC

- Precisión a segundos (no milisegundos)

- Mismo valor devuelto por `os.time()` en Lua estándar

- Disponible como función global y en el módulo `time`

#### Ejemplo de uso

```lua
-- Usando el módulo time
local timestamp_modulo = time.now()
print("Timestamp módulo:", timestamp_modulo)

-- Usando la función global (misma función)
local timestamp_global = now()
print("Timestamp global:", timestamp_global)

-- Ambos devuelven el mismo valor
print("São iguais?", timestamp_global == timestamp_modulo)  -- true

-- Calcular la duración de la operación
local inicio = time.now()
-- ... operación prolongada ...
local fim = time.now()
local duracao = fim - inicio
print("Operação levou", duracao, "segundos")

-- Registrar eventos con timestamp
local evento = {
    tipo = "login",
    usuario = "admin",
    timestamp = now(),
    origem = system.hostname()
}

-- Programar ejecución futura
local proxima_execucao = time.now() + 3600  -- 1 hora a partir de ahora
print("Próxima execução em:", os.date("%H:%M:%S", proxima_execucao))
```

### 2. `time.sleep(segundos)`

Espera de forma asíncrona durante un número específico de segundos.

#### Parámetros

- **segundos** (número): Número de segundos para esperar

#### Retorno

- **nil**: La función no devuelve valor (tras la espera)

#### Comportamiento

- Precisión dependiente del planificador del sistema

#### Ejemplo de uso

```lua
-- Esperar 5 segundos
await(time.sleep(5))
print("5 segundos se passaram")

-- Implementar sondeo con intervalo
local function poll_com_intervalo(url, intervalo_segundos, max_tentativas)
    for tentativa = 1, max_tentativas do
        log.info("Tentativa", tentativa, "de", max_tentativas)

        -- Realizar la solicitud
        local resposta, status = http.get(url)

        if status == 200 then
            log.info("Sucesso na tentativa", tentativa)
            return resposta
        end

        -- Esperar antes del siguiente intento
        if tentativa < max_tentativas then
            log.info("Aguardando", intervalo_segundos, "segundos...")
            time.sleep(intervalo_segundos)
        end
    end

    log.error("Todas as tentativas falharam")
    return nil
end

-- Uso
local dados = poll_com_intervalo("https://api.exemplo.com/status", 10, 6)

-- Control de execução con backoff exponencial
local function executar_com_backoff(funcao, max_tentativas)
    local tentativa = 1

    while tentativa <= max_tentativas do
        -- with_coroutine devuelve (resultado, err)
        local resultado, err = with_coroutine(funcao)

        if not err then
            return resultado
        end

        -- Backoff exponencial: 2^(tentativa-1) segundos
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

Parsea una cadena de fecha/hora en el formato RFC 3339 y devuelve un objeto de fecha.

#### Parámetros

- **string_data** (string): Fecha/hora en el formato RFC 3339 (ej: "2024-01-15T10:30:00Z")

#### Retorno

- **objeto LuaDateTime**: Objeto con el método `seconds()` que devuelve el timestamp Unix

#### Formato RFC 3339

- `YYYY-MM-DDTHH:MM:SSZ` (UTC)

- `YYYY-MM-DDTHH:MM:SS+HH:MM` (con offset de zona horaria)

- Ejemplos: "2024-01-15T10:30:00Z", "2024-01-15T07:30:00-03:00"

#### Ejemplo de uso

```lua
-- Parsear fecha UTC
local data_utc = time.parse("2024-01-15T10:30:00Z")
local timestamp_utc = data_utc:seconds()
print("Timestamp UTC:", timestamp_utc)  -- 1705314600

-- Parsear fecha con offset de zona horaria
local data_local = time.parse("2024-01-15T07:30:00-03:00")
local timestamp_local = data_local:seconds()
print("Timestamp local:", timestamp_local)  -- 1705314600 (mismo momento)

-- Convertir a formato legible
local function formatar_data_rfc3339(timestamp)
    return os.date("%Y-%m-%dT%H:%M:%SZ", timestamp)
end

-- Calcular diferencia entre fechas
local data1 = time.parse("2024-01-15T10:30:00Z")
local data2 = time.parse("2024-01-15T11:45:00Z")
local diferenca = data2:seconds() - data1:seconds()
print("Diferença:", diferenca, "segundos (", diferenca/60, "minutos)")

-- Validar y parsear fecha de entrada usando with_coroutine
local function parsear_data_segura(data_string)
    -- with_coroutine devuelve (result, err)
    local data, err = with_coroutine(time.parse, data_string)
    
    if not err and data then
        return data:seconds()
    else
        log.error("Data inválida:", data_string, "-", err)
        return nil
    end
end

-- Uso
local timestamp = parsear_data_segura("2024-01-15T10:30:00Z")
if timestamp then
    print("Data válida:", os.date("%d/%m/%Y %H:%M:%S", timestamp))
end
```