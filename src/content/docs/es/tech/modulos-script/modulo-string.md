---
title: "Módulo de cadenas"
---

El módulo **string** proporciona funciones utilitarias para la manipulación de cadenas en Lua, complementando las funciones nativas del lenguaje.

**Importante**: Este módulo extiende la tabla `string` estándar de Lua, por lo tanto las funciones se acceden a través de la tabla global `string` (ej: `string.split()`).

## Funciones disponibles

### 1. `string.split(s, sep)`

Divide una cadena en subcadenas basándose en un separador especificado.

#### Parámetros:

- **s** (string): La cadena original que será dividida

- **sep** (string): El separador usado para dividir la cadena

#### Retorno:

- **table**: Un array (tabla indexada numéricamente) que contiene todas las subcadenas resultantes de la división

#### Comportamiento:

- Si el separador es una cadena vacía (`""`), la función devuelve un array con cada carácter individual

- Si el separador no se encuentra en la cadena, devuelve un array que contiene solo la cadena original

- La división se realiza en todas las ocurrencias del separador

#### Ejemplo de uso:

```lua
-- Dividir una cadena por coma
local resultado = string.split("maçã,banana,laranja,uva", ",")
-- resultado = {"maçã", "banana", "laranja", "uva"}

-- Dividir por espacio
local palabras = string.split("Olá mundo do Lua", " ")
-- palabras = {"Olá", "mundo", "do", "Lua"}

-- Dividir por nueva línea (procesamiento de logs)
local linhas = string.split("2024-01-15 ERROR: Falha na conexão\n2024-01-15 INFO: Reconectando", "\n")
-- linhas = {"2024-01-15 ERROR: Falha na conexão", "2024-01-15 INFO: Reconectando"}

-- Separador vacío (dividir en caracteres)
local chars = string.split("teste", "")
-- chars = {"t", "e", "s", "t", "e"}

-- Separador no encontrado
local unico = string.split("texto_sem_separador", "|")
-- unico = {"texto_sem_separador"}
```

### 2. `string.trim(s)`

Elimina espacios en blanco (whitespace) del inicio y del final de una cadena.

#### Parámetros:

- **s** (string): La cadena que será limpiada

#### Retorno:

- **string**: La cadena original sin espacios en blanco al inicio ni al final

#### Comportamiento:

- Elimina espacios (` `), tabs (`\t`), saltos de línea (`\n`), retornos de carro (`\r`)

- No elimina espacios en el medio de la cadena

- Devuelve cadena vacía si la entrada contiene solo espacios en blanco

#### Ejemplo de uso:

```lua
-- Eliminar espacios extra
local limpo = string.trim("  texto com espaços  ")
-- limpo = "texto com espaços"

-- Limpiar entrada de usuario
local entrada = "\t\n valor digitado \r\n"
local processado = string.trim(entrada)
-- processado = "valor digitado"

-- Procesar configuraciones
local config_line = "   timeout = 30   "
local chave_valor = string.trim(config_line)
-- chave_valor = "timeout = 30"

-- Cadena solo con espacios
local vazio = string.trim("   \t\n   ")
-- vazio = ""
```

### 3. `string.starts(String, Start)`

Verifica si una cadena comienza con un prefijo específico.

#### Parámetros:

- **String** (string): La cadena a verificar

- **Start** (string): El prefijo a buscar al inicio de la cadena

#### Retorno:

- **boolean**: `true` si la cadena comienza con el prefijo especificado, `false` en caso contrario

#### Comportamiento:

- La comparación distingue mayúsculas y minúsculas (case-sensitive)

- Devuelve `true` si el prefijo es una cadena vacía (`""`)

- Funciona con cadenas multibyte (UTF-8)

#### Ejemplo de uso:

```lua
-- Verificar si una cadena comienza con "http"
local url = "https://example.com"
local is_http = string.starts(url, "http")
-- is_http = true

-- Verificar prefijo en rutas de archivo
local path = "/var/log/app.log"
local is_absolute = string.starts(path, "/")
-- is_absolute = true

-- Verificar en procesamiento de logs
local log_line = "ERROR: Database connection failed"
local is_error = string.starts(log_line, "ERROR:")
-- is_error = true

-- Prefijo vacío siempre devuelve true
local always_true = string.starts("qualquer string", "")
-- always_true = true

-- Case-sensitive
local case_check = string.starts("Hello World", "hello")
-- case_check = false (distingue mayúsculas/minúsculas)
```

### 4. `string.ends(string, end)`

Verifica si una cadena termina con un sufijo específico.

#### Parámetros:

- **string** (string): La cadena a verificar

- **end** (string): El sufijo a buscar al final de la cadena

#### Retorno:

- **boolean**: `true` si la cadena termina con el sufijo especificado, `false` en caso contrario

#### Comportamiento:

- La comparación distingue mayúsculas y minúsculas (case-sensitive)

- Devuelve `true` si el sufijo es una cadena vacía (`""`)

- Funciona con cadenas multibyte (UTF-8)

#### Ejemplo de uso:

```lua
-- Verificar extensión de archivo
local filename = "document.pdf"
local is_pdf = string.ends(filename, ".pdf")
-- is_pdf = true

-- Verificar sufijo en URLs
local url = "https://api.example.com/v1/data.json"
local is_json = string.ends(url, ".json")
-- is_json = true

-- Verificar terminación en cadenas de log
local log_entry = "Process completed successfully."
local is_success = string.ends(log_entry, "successfully.")
-- is_success = true

-- Sufijo vacío siempre devuelve true
local always_true = string.ends("qualquer string", "")
-- always_true = true

-- Case-sensitive
local case_check = string.ends("Hello World", "world")
-- case_check = false (distingue mayúsculas/minúsculas)
```

### Ventajas del Módulo String de Monsta:

1. **`string.split()`** - No existe nativamente en Lua, necesita implementarse manualmente

2. **`string.trim()`** - Más eficiente que implementaciones en Lua puro

3. **Consistencia** - Misma interfaz para todas las funciones

### Funciones complementarias:

Úselo en conjunto con funciones nativas de Lua:

- `string.find()` - Para búsquedas complejas

- `string.gsub()` - Para substituciones

- `string.match()` - Para extracción con patrones

- `string.gmatch()` - Para iteración sobre patrones

## Ejemplos completos

### Ejemplo 1: Procesamiento de log del sistema

```lua
-- Simular lectura del log del sistema
local log_data = [[
Jan 15 10:30:45 servidor kernel: [12345.67890] CPU temperature: 65.5C
Jan 15 10:31:15 servidor sshd[1234]: Accepted password for user from 192.168.1.100
Jan 15 10:32:00 servidor crond[5678]: (root) CMD (/usr/bin/backup.sh)
]]

-- Procesar cada línea del log
local function analisar_logs(logs)
    local eventos = {}

    for linha in string.gmatch(logs, "[^\n]+") do
        local linha_limpa = string.trim(linha)
        if linha_limpa ~= "" then
            -- Dividir por espacios (formato syslog)
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

### Ejemplo 2: Parser de configuración simple

```lua
-- Parser para archivos de configuración en el formato clave=valor
local function parse_config(conteudo)
    local config = {}

    for linha in string.gmatch(conteudo, "[^\n]+") do
        local linha_limpa = string.trim(linha)

        -- Ignorar líneas vacías y comentarios
        if linha_limpa ~= "" and not string.starts(linha_limpa, "#") then
            -- Dividir por "="
            local partes = string.split(linha_limpa, "=")

            if #partes == 2 then
                local chave = string.trim(partes[1])
                local valor = string.trim(partes[2])

                -- Eliminar comillas si existen
                if string.starts(valor, "\"") and string.ends(valor, "\"") then
                    valor = string.sub(valor, 2, -2)
                end

                config[chave] = valor
            end
        end
    end

    return config
end

-- Ejemplo de uso
local config_text = [[
# Configuraciones del monitor
hostname = "servidor-prod"
port = 8080
timeout = 30
debug = false
]]

local config = parse_config(config_text)
-- config.hostname = "servidor-prod", config.port = "8080", etc.
```