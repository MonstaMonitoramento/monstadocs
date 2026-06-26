---
title: "Global Functions"
sidebar:
  order: 2
---

This section describes the global functions available in Monsta's Lua environment. These are functions that do not belong to specific modules but are available directly in the Lua global scope. There are features for flow control, time manipulation, among others.



## Available Functions



### `sleep(seconds)`



**Description**: Pauses script execution for a specified number of seconds.



**Parameters**:



- `seconds` (number): Number of seconds to pause execution



**Return**: `nil` (no return value)



**Example**:



```lua
-- Pause for 5 seconds
sleep(5)
print("Execução retomada após 5 segundos")
```



### `signal(signal_name)`



**Description**: Signals the termination of script execution with a specific signal name.



**Parameters**:



- `signal_name` (string): Name of the signal to be emitted



**Return**: Aborts the script execution with the signal name



**Characteristics**:



- Calls the `_execution_done` function if available in the global environment

- Always raises an error, interrupting normal execution

- Useful for flow control and state signaling



**Note**: Currently, this function has a single specific use case: signaling with the name `"RepeatPrevValue"`. When a script emits this signal, the system interprets that the current collection should repeat the last valid metric value instead of generating a new data point. This is useful in situations where the data source is temporarily unavailable or the collection failed, but you don't want to break the time series.



**Specific usage example**:



```lua

-- Try to collect a value
local value, err = collect_metric()
if err then
    -- In case of failure, repeat the previous value
    signal("RepeatPrevValue")
end

```



### `with_timeout(timeout_ms, func, ...)`



**Description**: Executes a function with a time limit (timeout).



**Parameters**:



- `timeout_ms` (number): Timeout in milliseconds

- `func` (function): Lua function to execute

- `...` (optional): Arguments to pass to the function



**Return**: Returns the result of the executed function



**Example**:



```lua

-- Execute a function with a 2-second timeout
local result = with_timeout(2000, function()
    -- Operation that may take long
    return some_long_running_operation()
end)

-- Execute with arguments
local data = with_timeout(1000, http.get, "https://api.example.com/data")

-- Timeout handling
local success, result = pcall(function()
    return with_timeout(500, function()
        -- Operation that must complete quickly
        return critical_operation()
    end)
end)

if not success then
    print("Operação excedeu o timeout de 500ms")
end

```



**Characteristics**:



- Raises an error if the timeout is exceeded

- Preserves the arguments passed to the function

- Useful for network or I/O operations that may hang



### `now()`



**Description**: Returns the number of non-leap seconds since January 1, 1970 00:00:00 UTC (also known as the "UNIX timestamp").



**Parameters**: None



**Return**: Number representing seconds since the Unix epoch



**Example**:



```lua

-- Get current timestamp
local current_time = now()
print("Timestamp atual:", current_time)

-- Calculate operation duration
local start_time = now()

-- Execute some operation
local end_time = now()
local duration = end_time - start_time
print("Operação levou", duration, "segundos")

```



**Characteristics**:



- Same function available as `time.now()`

- Useful for performance measurement



### `print(...)`



**Description**: Print function that formats multiple arguments.



**Parameters**:



- `...` (multiple values): Values to be printed



**Return**: `nil` (no return value)



**Example**:



```lua

print("Valor:", 42, "Status:", true, "Lista:", {1, 2, 3})

```



**Characteristics**:



- Separates multiple arguments with a tab

- Useful for debugging



### `diff(lhs, rhs)`



**Description**: Calculates the difference between two numeric values, with special handling for counters that may roll over.



**Parameters**:



- `lhs` (number): Current value (left-hand side)

- `rhs` (number): Previous value (right-hand side)



**Return**: Number representing the difference between the values



**Behavior**:



- Calculates `lhs - rhs`

- If the result is negative, emits the `"RepeatPrevValue"` signal

- Used internally by `snmp.diff` and `wmi.diff` for difference calculations on counters

- Useful for counter metrics that may roll over (such as 32- or 64-bit counters)



**Example**:



```lua

-- Calculate difference between counter readings
local current_value = 4294967290  -- Current value (near 32-bit rollover)
local previous_value = 4294967280  -- Previous value

local difference = diff(current_value, previous_value)
-- difference = 10 (4294967290 - 4294967280)

-- Case with rollover (value decreased)
local current_with_rollover = 10  -- After rollover
local previous_before_rollover = 4294967295  -- Before rollover

local rollover_diff = diff(current_with_rollover, previous_before_rollover)
-- Emits signal "RepeatPrevValue" because 10 - 4294967295 is negative

```



## Global Variables



### `EXEC_IDENT`



**Description**: Unique identifier of the current script execution.



**Type**: String



**Example**:



```lua

-- Use the identifier in logs
print("Execução ID:", EXEC_IDENT)

-- Include in monitoring data
local metrics = {
    ident = EXEC_IDENT,
    timestamp = now(),
    value = collected_data
}

-- Use as key for storage
store.put("results_" .. EXEC_IDENT, processing_result)

```



**Characteristics**:



- Defined automatically by the environment

- Unique for each script execution

- Useful for tracking and correlating logs



## Limitations



1. **`sleep` Is Not Precise**: Due to the asynchronous nature of the system, `sleep` may have small variations.

2. **`signal` Interrupts Execution**: Once called, normal execution is interrupted.



## Example



```lua

-- Monitor service with backoff on failure
local function monitor_with_backoff(service_url, max_attempts)
    local attempt = 1
    local backoff = 1  -- seconds

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

        -- Increase exponential backoff
        sleep(backoff)
        backoff = math.min(backoff * 2, 60)  -- Maximum 60 seconds
        attempt = attempt + 1
    end

    -- All attempts failed
    return false
end

-- Run monitoring
monitor_with_backoff("https://api.example.com", 5)

```