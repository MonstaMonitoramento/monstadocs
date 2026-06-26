---
title: "Funciones Globales"
sidebar:
  order: 2
---

Esta sección describe las funciones globales disponibles en el entorno Lua de Monsta. Estas son funciones que no pertenecen a módulos específicos, pero están disponibles directamente en el ámbito global de Lua. Existen funcionalidades para control de flujo, manipulación de tiempo, entre otras.



## Funciones Disponibles



### `sleep(seconds)`



**Descripción**: Pausa la ejecución del script durante un número especificado de segundos.



**Parámetros**:



- `seconds` (número): Número de segundos para pausar la ejecución



**Retorno**: `nil` (no devuelve valor)



**Ejemplo**:



```lua
-- Pausar por 5 segundos
sleep(5)
print("Execução retomada após 5 segundos")
```



### `signal(signal_name)`



**Descripción**: Señala la finalización de la ejecución del script con un nombre de señal específico.



**Parámetros**:



- `signal_name` (string): Nombre de la señal a emitir



**Retorno**: Aborta la ejecución del script con el nombre de la señal



**Características**:



- Llama a la función `_execution_done` si está disponible en el entorno global

- Siempre lanza un error, interrumpiendo la ejecución normal

- Útil para control de flujo y señalización de estados



**Nota**: Actualmente, esta función tiene un único caso de uso específico: señalizar con el nombre `"RepeatPrevValue"`. Cuando un script emite esta señal, el sistema interpreta que la recolección actual debe repetir el último valor válido de la métrica, en lugar de generar un nuevo punto de datos. Esto es útil en situaciones donde la fuente de datos está temporalmente indisponible o la recolección falló, pero no se desea interrumpir la serie temporal.



**Ejemplo de uso específico**:



```lua

-- Intentar recolectar un valor
local value, err = collect_metric()
if err then
    -- En caso de fallo, repetir el valor anterior
    signal("RepeatPrevValue")
end

```



### `with_timeout(timeout_ms, func, ...)`



**Descripción**: Ejecuta una función con un límite de tiempo (timeout).



**Parámetros**:



- `timeout_ms` (número): Tiempo límite en milisegundos

- `func` (función): Función Lua a ejecutar

- `...` (opcional): Argumentos para pasar a la función



**Retorno**: Devuelve el resultado de la función ejecutada



**Ejemplo**:



```lua

-- Ejecutar una función con timeout de 2 segundos
local result = with_timeout(2000, function()
    -- Operación que puede tardar
    return some_long_running_operation()
end)

-- Ejecutar con argumentos
local data = with_timeout(1000, http.get, "https://api.example.com/data")

-- Manejo de timeout
local success, result = pcall(function()
    return with_timeout(500, function()
        -- Operación que debe completarse rápidamente
        return critical_operation()
    end)
end)

if not success then
    print("Operação excedeu o timeout de 500ms")
end

```



**Características**:



- Lanza un error si se excede el timeout

- Conserva los argumentos pasados a la función

- Útil para operaciones de red o I/O que pueden bloquearse



### `now()`



**Descripción**: Devuelve el número de segundos no bisiestos desde el 1 de enero de 1970 00:00:00 UTC (también conocido como "timestamp UNIX").



**Parámetros**: Ninguno



**Retorno**: Número que representa segundos desde la época Unix



**Ejemplo**:



```lua

-- Obtener timestamp actual
local current_time = now()
print("Timestamp atual:", current_time)

-- Calcular duración de operación
local start_time = now()

-- Ejecutar alguna operación
local end_time = now()
local duration = end_time - start_time
print("Operação levou", duration, "segundos")

```



**Características**:



- Misma función disponible en `time.now()`

- Útil para medición de rendimiento



### `print(...)`



**Descripción**: Función de impresión que formatea múltiples argumentos.



**Parámetros**:



- `...` (múltiples valores): Valores a imprimir



**Retorno**: `nil` (no devuelve valor)



**Ejemplo**:



```lua

print("Valor:", 42, "Status:", true, "Lista:", {1, 2, 3})

```



**Características**:



- Separa múltiples argumentos con tabulación

- Útil para depuración



### `diff(lhs, rhs)`



**Descripción**: Calcula la diferencia entre dos valores numéricos, con tratamiento especial para contadores que pueden sufrir rollover.



**Parámetros**:



- `lhs` (número): Valor actual (left-hand side)

- `rhs` (número): Valor anterior (right-hand side)



**Retorno**: Número que representa la diferencia entre los valores



**Comportamiento**:



- Calcula `lhs - rhs`

- Si el resultado es negativo, emite la señal `"RepeatPrevValue"`

- Usado internamente por `snmp.diff` y `wmi.diff` para cálculo de diferencias en contadores

- Útil para métricas de contador que pueden sufrir rollover (como contadores de 32 o 64 bits)



**Ejemplo**:



```lua

-- Calcular la diferencia entre lecturas de contador
local current_value = 4294967290  -- Valor actual (cercano al desbordamiento de 32 bits)
local previous_value = 4294967280  -- Valor anterior

local difference = diff(current_value, previous_value)
-- difference = 10 (4294967290 - 4294967280)

-- Caso con rollover (valor disminuyó)
local current_with_rollover = 10  -- Después del rollover
local previous_before_rollover = 4294967295  -- Antes del rollover

local rollover_diff = diff(current_with_rollover, previous_before_rollover)
-- Emite la señal "RepeatPrevValue" pues 10 - 4294967295 es negativo

```



## Variables Globales



### `EXEC_IDENT`



**Descripción**: Identificador único de la ejecución actual del script.



**Tipo**: String



**Ejemplo**:



```lua

-- Usar el identificador en los logs
print("Execução ID:", EXEC_IDENT)

-- Incluir en datos de monitorización
local metrics = {
    ident = EXEC_IDENT,
    timestamp = now(),
    value = collected_data
}

-- Usar como clave para almacenamiento
store.put("results_" .. EXEC_IDENT, processing_result)

```



**Características**:



- Definida automáticamente por el entorno

- Única para cada ejecución de script

- Útil para rastreo y correlación de logs



## Limitaciones



1. **`sleep` No es Preciso**: Debido a la naturaleza asíncrona del sistema, `sleep` puede tener pequeñas variaciones.

2. **`signal` Interrumpe Ejecución**: Una vez llamada, la ejecución normal se interrumpe.



## Ejemplo



```lua

-- Monitorizar servicio con backoff en caso de fallo
local function monitor_with_backoff(service_url, max_attempts)
    local attempt = 1
    local backoff = 1  -- segundos

    while attempt <= max_attempts do
        log.info("Tentativa", attempt, "de", max_attempts)
        local success, status = pcall(function()
            return with_timeout(5000, function()
                return check_service(service_url)
            end)
        end)

        if success and status == "healthy" then
            log.info("Serviço saudável")
            return true
        end

        -- Incrementar backoff exponencial
        sleep(backoff)
        backoff = math.min(backoff * 2, 60)  -- Máximo 60 segundos
        attempt = attempt + 1
    end

    -- Todos los intentos fallaron
    return false
end

-- Ejecutar monitorización
monitor_with_backoff("https://api.example.com", 5)

```