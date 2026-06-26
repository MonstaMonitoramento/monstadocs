---
title: "System Module"
---

The **system** module provides functions to obtain information about the operating system, network, and the agent's runtime environment. This module is useful for scripts that need to adapt their behavior based on the environment, collect inventory information, or perform system diagnostics.

**Key features**:

- Detailed operating system information

- Hostname and network information

- Agent data (UUID, version)

- Kernel and distribution information

- Unified interface for different operating systems

## Available Functions

### 1. `system.env()`

Returns full information about the agent's runtime environment.

#### Parameters:

- None

#### Return:

- **table**: Structure with the following fields:

    - `os_type` (string): Type of the operating system (e.g. "linux", "windows", "macos")

    - `os_name` (string): Name of the operating system (e.g. "Ubuntu", "Windows 10", "macOS")

    - `os_version` (string): Operating system version

    - `kernel_version` (string): Kernel version

    - `agent` (table or nil): Monagent agent information (if available):

        - `uuid` (string): Agent's unique UUID

        - `version` (string): Monagent version

#### Example Usage:

```lua
-- Get all environment information
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

-- Adapt behavior based on OS
local env = system.env()

if env.os_type == "linux" then
    -- Linux-specific commands
    local saida, erro = process.exec("ps", "aux")
elseif env.os_type == "windows" then
    -- Windows-specific commands
    local saida, erro = process.exec("tasklist")
elseif env.os_type == "macos" then
    -- macOS-specific commands
    local saida, erro = process.exec("ps", "-ef")
end
```

### 2. `system.hostname()`

Returns the system's hostname.

#### Parameters:

- None

#### Return:

- **string**: System hostname, or "unknown" if it cannot be determined

#### Example Usage:

```lua
-- Get hostname
local nome_host = system.hostname()
print("Nome do host:", nome_host)

-- Use in unique identifiers
local identificador = nome_host .. "_" .. os.date("%Y%m%d_%H%M%S")
print("Identificador único:", identificador)

-- Check if it's a specific host
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

-- Create tags for metrics
local tags_metricas = {
    host = nome_host,
    ambiente = config.modo,
    timestamp = os.time()
}
```

### 3. `system.networks()`

Returns a list of non-loopback network IP addresses of the system.

#### Parameters:

- None

#### Return:

- **array of strings**: List of IP addresses from network interfaces (excluding loopback)

#### Behavior:

- Excludes loopback addresses (127.0.0.1, ::1, etc.)

- Includes IPv4 and IPv6 addresses

- Updates the interface list before returning

- Returns only IP addresses, not interface names

#### Example Usage:

```lua
-- Get all system IP addresses
local enderecos_ip = system.networks()

print("Endereços IP disponíveis:")
for i, ip in ipairs(enderecos_ip) do
    print("  " .. i .. ". " .. ip)
end

-- Identify IPv4 vs IPv6 addresses
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
            -- Other format
            table.insert(classificacao.outros, ip)
        end
    end

    return classificacao
end

local ips = classificar_enderecos()
print("IPv4:", #ips.ipv4, "endereços")
print("IPv6:", #ips.ipv6, "endereços")

-- Find preferred address for communication
local function encontrar_endereco_preferido()
    local enderecos = system.networks()

    -- Priority: private IPv4 > public IPv4 > IPv6
    for _, ip in ipairs(enderecos) do
        -- Verificar se é IPv4 privado
        if string.match(ip, "^10%.") or
           string.match(ip, "^172%.%d?%d?%d?%.") or
           string.match(ip, "^192%.168%.") then