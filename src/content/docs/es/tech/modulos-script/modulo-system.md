---
title: "Módulo System"
---

El módulo **system** proporciona funciones para obtener información sobre el sistema operativo, la red y el entorno de ejecución del agente. Este módulo es útil para scripts que necesitan adaptar su comportamiento según el entorno, recopilar información de inventario o realizar diagnósticos del sistema.

**Características principales**:

- Información detallada del sistema operativo

- Nombre del host e información de red

- Datos del agente (UUID, versión)

- Información del kernel y de la distribución

- Interfaz unificada para diferentes sistemas operativos

## Funciones disponibles

### 1. `system.env()`

Devuelve información completa sobre el entorno de ejecución del agente.

#### Parámetros:

- Ninguno

#### Retorno:

- **tabla**: Estructura con los siguientes campos:

    - `os_type` (string): Tipo del sistema operativo (ej.: "linux", "windows", "macos")

    - `os_name` (string): Nombre del sistema operativo (ej.: "Ubuntu", "Windows 10", "macOS")

    - `os_version` (string): Versión del sistema operativo

    - `kernel_version` (string): Versión del kernel

    - `agent` (tabla o nil): Información del agente Monagent (si está disponible):

        - `uuid` (string): UUID único del agente

        - `version` (string): Versión del Monagent

#### Ejemplo de uso:

```lua
-- Obtener toda la información del entorno
local env_info = system.env()

print("Tipo do SO:", env_info.os_type)
print("Nome do SO:", env_info.os_name)
print("Versão do SO:", env_info.os_version)
print("Versão do Kernel:", env_info.kernel_version)

if env_info.agent then
    print("UUID do Agente:", env_info.agent.uuid)
    print("Versão do Monagent:", env_info.agent.version)
else
    print("Informações do agente não disponíveis")
end

-- Adaptar comportamento según el SO
local env = system.env()

if env.os_type == "linux" then
    -- Comandos específicos para Linux
    local saida, erro = process.exec("ps", "aux")
elseif env.os_type == "windows" then
    -- Comandos específicos para Windows
    local saida, erro = process.exec("tasklist")
elseif env.os_type == "macos" then
    -- Comandos específicos para macOS
    local saida, erro = process.exec("ps", "-ef")
end
```

### 2. `system.hostname()`

Devuelve el nombre del host del sistema.

#### Parámetros:

- Ninguno

#### Retorno:

- **string**: Nombre del host del sistema, o "unknown" si no puede determinarse

#### Ejemplo de uso:

```lua
-- Obtener nombre del host
local nome_host = system.hostname()
print("Nome do host:", nome_host)

-- Usar en identificadores únicos
local identificador = nome_host .. "_" .. os.date("%Y%m%d_%H%M%S")
print("Identificador único:", identificador)

-- Verificar si es un host específico
if nome_host == "servidor-producao" then
    log.info("Executando em servidor de produção")
    config.modo = "producao"
elseif string.find(nome_host:lower(), "test") then
    log.info("Executando em ambiente de teste")
    config.modo = "teste"
else
    log.info("Executando em host desconhecido:", nome_host)
    config.modo = "desenvolvimento"
end

-- Crear etiquetas para métricas
local tags_metricas = {
    host = nome_host,
    ambiente = config.modo,
    timestamp = os.time()
}
```

### 3. `system.networks()`

Devuelve una lista de direcciones IP de red no loopback del sistema.

#### Parámetros:

- Ninguno

#### Retorno:

- **array de strings**: Lista de direcciones IP de las interfaces de red (excluyendo loopback)

#### Comportamiento:

- Excluye direcciones de loopback (127.0.0.1, ::1, etc.)

- Incluye direcciones IPv4 e IPv6

- Actualiza la lista de interfaces antes de devolverla

- Devuelve solo direcciones IP, no nombres de interfaz

#### Ejemplo de uso:

```lua
-- Obter todos os endereços IP do sistema
local enderecos_ip = system.networks()

print("Endereços IP disponíveis:")
for i, ip in ipairs(enderecos_ip) do
    print("  " .. i .. ". " .. ip)
end

-- Identificar endereços IPv4 vs IPv6
local function classificar_enderecos()
    local enderecos = system.networks()
    local classificacao = {
        ipv4 = {},
        ipv6 = {},
        outros = {}
    }

    for _, ip in ipairs(enderecos) do
        if string.find(ip, ":") then
            -- IPv6
            table.insert(classificacao.ipv6, ip)
        elseif string.match(ip, "^%d+%.%d+%.%d+%.%d+$") then
            -- IPv4
            table.insert(classificacao.ipv4, ip)
        else
            -- Otro formato
            table.insert(classificacao.outros, ip)
        end
    end

    return classificacao
end

local ips = classificar_enderecos()
print("IPv4:", #ips.ipv4, "endereços")
print("IPv6:", #ips.ipv6, "endereços")

-- Encontrar endereço preferido para comunicação
local function encontrar_endereco_preferido()
    local enderecos = system.networks()

    -- Prioridade: IPv4 privado > IPv4 público > IPv6
    for _, ip in ipairs(enderecos) do
        -- Verificar se é IPv4 privado
        if string.match(ip, "^10%.") or
           string.match(ip, "^172%.%d?%d?%d?%.") or
           string.match(ip, "^192%.168%.") then
```