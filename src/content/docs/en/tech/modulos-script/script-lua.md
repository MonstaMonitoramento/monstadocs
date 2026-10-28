---
title: Scripting with Lua
sidebar:
  order: 1
---
Monsta allows you to create custom data collection logic, metric processing and complex alerting rules using the **Lua** programming language.

If the default templates or native expressions are not enough for your needs (such as parsing complex strings, advanced mathematical calculations or loops), the Lua scripting engine offers full flexibility to extend the platform.

---

## Why Lua?

Lua is a Brazilian scripting language, widely used in the tech industry (especially in games and embedded systems) for three main reasons:

- **Extreme Speed**: It is one of the fastest scripting languages in the world, ensuring that your scripts run in milliseconds without overloading the Monsta server.
- **Lightweight**: The interpreter occupies very little memory, allowing large-scale concurrent executions.
- **Simple Syntax**: It is very easy to read and learn, even for those with little programming experience.

---

## Quick Lua Syntax Guide

To help you start creating your first scripts in Monsta, here are the fundamental concepts of the language:

### Variables and Data Types

In Lua, you don't need to define the variable type beforehand (dynamic typing). Always use the `local` keyword to ensure the variable exists only within that script (avoiding memory conflicts).

```lua
local nome_dispositivo = "Servidor Core" -- String
local latencia = 45                     -- Number
local ativo = true                      -- Boolean
```

### Conditional Structures (`if` / `else`)

The syntax uses the keywords `then`, `elseif` and the block must be closed with an `end`.

```lua
if latencia > 100 then
    print("Alerta: Latência Alta!")
elseif latencia > 50 then
    print("Aviso: Latência Moderada.")
else
    print("Status: OK.")
end
```

### Tables (Dictionaries and Arrays)

Tables are the only complex data structure in Lua. They serve both as indexed lists and as key/value objects.

```lua
-- Example of Array/List
local sensores = {"Ping", "CPU", "Memória"}

-- Example of Dictionary (Key/Value)
local dados_coleta = {
    ip = "192.168.1.50",
    status = "Online",
    portas_abertas = 4
}
```

:::caution[Be careful with Indexes!]
Unlike most programming languages (like **JavaScript** or **Python**) where lists start at index `0`, in Lua tables start at index `1`.
Therefore, `sensores[1]` will return "Ping".
:::

## How does Monsta interact with the Script?

Generally, Monsta injects global variables or predefined tables into your script (containing the data collected from the device) and expects your script to return a specific value (such as a number, text or boolean) using the `return` statement.

```lua
-- Example of an SNMP query
local load_linux = snmp.get("1.3.6.1.4.1.2021.10.1.3.2.0") -- Monsta function
return load_linux
```

The `return` can also define the metric status. To return a status, the return must return a dictionary containing `value` (value to be returned) and `status` (a *string* with predefined values).

The accepted values for `status` are:

| status | Color | Metric Status |
| ---------------- | -------- | ----------------- |
| `MetricOk` | Green | Normal |
| `MetricWarning` | Orange | Warning |
| `MetricCritical` | Red | Critical |

```lua
-- Example of an SNMP query with status handling
local volt = snmp.get("1.3.6.1.2.1.33.1.3.3.1.3.1.0")

if volt > 230 then
   -- If the voltage is higher, enter Warning status
   return { value=volt, status="MetricWarning" }
elseif volt < 100 then
   -- If the voltage is lower, enter Critical status
   return { value=volt, status="MetricCritical" }
else
   -- Otherwise, the status will be Normal
   return { value=volt, status="MetricOk" }
end
```

:::caution[Attention!]

When the status is defined inside the script, it is not possible to configure the alert status through the monitor settings, because the script will define that information.

:::

## Full Resources and Manuals

To dive deeper into the language, see the [official Lua language documentation](https://lua.org/docs.html).

Monsta has its own functions used in scripts. To learn about the specific internal modules that Monsta provides (network functions, string manipulation and connection), check the next articles in this area (**Lua Script Modules**).