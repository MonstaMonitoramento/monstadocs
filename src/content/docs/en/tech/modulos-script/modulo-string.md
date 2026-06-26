---
title: "String Module"
---

The **string** module provides utility functions for manipulating strings in Lua, complementing the language's native functions.

**Important**: This module extends Lua's standard `string` table, so functions are accessed through the global `string` table (e.g. `string.split()`).

## Available Functions

### 1. `string.split(s, sep)`

Splits a string into substrings based on a specified separator.

#### Parameters:

- **s** (string): The original string to be split

- **sep** (string): The separator used to split the string

#### Return:

- **table**: An array (numerically indexed table) containing all substrings resulting from the split

#### Behavior:

- If the separator is an empty string (`""`), the function returns an array with each individual character

- If the separator is not found in the string, it returns an array containing only the original string

- The split is performed on all occurrences of the separator

#### Usage Example:

```lua
-- Split a string by comma
local resultado = string.split("maçã,banana,laranja,uva", ",")
-- result = {"maçã", "banana", "laranja", "uva"}

-- Split by space
local palavras = string.split("Olá mundo do Lua", " ")
-- words = {"Olá", "mundo", "do", "Lua"}

-- Split by newline (log processing)
local linhas = string.split("2024-01-15 ERROR: Falha na conexão\n2024-01-15 INFO: Reconectando", "\n")
-- lines = {"2024-01-15 ERROR: Falha na conexão", "2024-01-15 INFO: Reconectando"}

-- Empty separator (split into characters)
local chars = string.split("teste", "")
-- chars = {"t", "e", "s", "t", "e"}

-- Separator not found
local unico = string.split("texto_sem_separador", "|")
-- single = {"texto_sem_separador"}
```

### 2. `string.trim(s)`

Removes whitespace from the beginning and end of a string.

#### Parameters:

- **s** (string): The string to be trimmed

#### Return:

- **string**: The original string without leading and trailing whitespace

#### Behavior:

- Removes spaces (` `), tabs (`\t`), newlines (`\n`), carriage returns (`\r`)

- Does not remove spaces in the middle of the string

- Returns an empty string if the input is only whitespace

#### Usage Example:

```lua
-- Remove extra spaces
local limpo = string.trim("  texto com espaços  ")
-- clean = "texto com espaços"

-- Clean user input
local entrada = "\t\n valor digitado \r\n"
local processado = string.trim(entrada)
-- processed = "valor digitado"

-- Process configuration lines
local config_line = "   timeout = 30   "
local chave_valor = string.trim(config_line)
-- key_value = "timeout = 30"

-- String with only spaces
local vazio = string.trim("   \t\n   ")
-- empty = ""
```

### 3. `string.starts(String, Start)`

Checks if a string starts with a specific prefix.

#### Parameters:

- **String** (string): The string to check

- **Start** (string): The prefix to look for at the beginning of the string

#### Return:

- **boolean**: `true` if the string starts with the specified prefix, `false` otherwise

#### Behavior:

- The comparison is case-sensitive

- Returns `true` if the prefix is an empty string (`""`)

- Works with multibyte (UTF-8) strings

#### Usage Example:

```lua
-- Check if a string starts with "http"
local url = "https://example.com"
local is_http = string.starts(url, "http")
-- is_http = true

-- Check prefix in file paths
local path = "/var/log/app.log"
local is_absolute = string.starts(path, "/")
-- is_absolute = true

-- Check in log processing
local log_line = "ERROR: Database connection failed"
local is_error = string.starts(log_line, "ERROR:")
-- is_error = true

-- Empty prefix always returns true
local always_true = string.starts("qualquer string", "")
-- always_true = true

-- Case-sensitive
local case_check = string.starts("Hello World", "hello")
-- case_check = false (case-sensitive)
```

### 4. `string.ends(string, end)`

Checks if a string ends with a specific suffix.

#### Parameters:

- **string** (string): The string to check

- **end** (string): The suffix to look for at the end of the string

#### Return:

- **boolean**: `true` if the string ends with the specified suffix, `false` otherwise

#### Behavior:

- The comparison is case-sensitive

- Returns `true` if the suffix is an empty string (`""`)

- Works with multibyte (UTF-8) strings

#### Usage Example:

```lua
-- Check file extension
local filename = "document.pdf"
local is_pdf = string.ends(filename, ".pdf")
-- is_pdf = true

-- Check suffix in URLs
local url = "https://api.example.com/v1/data.json"
local is_json = string.ends(url, ".json")
-- is_json = true

-- Check ending in log strings
local log_entry = "Process completed successfully."
local is_success = string.ends(log_entry, "successfully.")
-- is_success = true

-- Empty suffix always returns true
local always_true = string.ends("qualquer string", "")
-- always_true = true

-- Case-sensitive
local case_check = string.ends("Hello World", "world")
-- case_check = false (case-sensitive)
```

### Advantages of Monsta's String Module:

1. **`string.split()`** - Not available natively in Lua; needs to be implemented manually

2. **`string.trim()`** - More performant than pure Lua implementations

3. **Consistency** - Same interface for all functions

### Complementary Functions:

Use alongside Lua's native functions:

- `string.find()` - For complex searches

- `string.gsub()` - For replacements

- `string.match()` - For extraction with patterns

- `string.gmatch()` - For iterating over patterns

## Complete Examples

### Example 1: System Log Processing

```lua
-- Simulate reading system log
local log_data = [[
Jan 15 10:30:45 servidor kernel: [12345.67890] CPU temperature: 65.5C
Jan 15 10:31:15 servidor sshd[1234]: Accepted password for user from 192.168.1.100
Jan 15 10:32:00 servidor crond[5678]: (root) CMD (/usr/bin/backup.sh)
]]

-- Process each log line
local function analisar_logs(logs)
    local eventos = {}

    for linha in string.gmatch(logs, "[^\n]+") do
        local linha_limpa = string.trim(linha)
        if linha_limpa ~= "" then
            -- Split by spaces (syslog format)
            local partes = string.split(linha_limpa, " ")

            if #partes >= 5 then
                local evento = {
                    data = partes[1] .. " " .. partes[2] .. " " .. partes[3],
                    host = partes[4],
                    servico = partes[5],
                    mensagem = table.concat(partes, " ", 6)
                }
                table.insert(eventos, evento)
            end
        end
    end

    return eventos
end

local eventos = analisar_logs(log_data)
```

### Example 2: Simple Configuration Parser

```lua
-- Parser for configuration files in key=value format
local function parse_config(conteudo)
    local config = {}

    for linha in string.gmatch(conteudo, "[^\n]+") do
        local linha_limpa = string.trim(linha)

        -- Ignore empty lines and comments
        if linha_limpa ~= "" and not string.starts(linha_limpa, "#") then
            -- Split by "="
            local partes = string.split(linha_limpa, "=")

            if #partes == 2 then
                local chave = string.trim(partes[1])
                local valor = string.trim(partes[2])

                -- Remove quotes if present
                if string.starts(valor, "\"") and string.ends(valor, "\"") then
                    valor = string.sub(valor, 2, -2)
                end

                config[chave] = valor
            end
        end
    end

    return config
end

-- Usage example
local config_text = [[
# Configurações do monitor
hostname = "servidor-prod"
port = 8080
timeout = 30
debug = false
]]

local config = parse_config(config_text)
-- config.hostname = "servidor-prod", config.port = "8080", etc.
```